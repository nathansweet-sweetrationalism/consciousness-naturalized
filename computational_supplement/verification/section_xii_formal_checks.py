#!/usr/bin/env python3
"""Reproducible countermodels and dimensional tests for WordPress article #2115.

These are checks of particular formal implications, not proofs of any
consciousness ontology. They use explicit finite encodings and print JSON.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
import platform

import sympy
from sympy.physics.units import boltzmann_constant, joule, kelvin, second
from sympy.physics.units.systems.si import SI
import z3


def unit_contract() -> dict:
    """Article §12.3.1: dot-sigma [entropy/time] vs R k_B T ln2 / dt [power]."""
    lhs = SI.get_dimensional_expr(joule / (kelvin * second))
    rhs = SI.get_dimensional_expr(boltzmann_constant * kelvin / second)
    repaired_entropy_rate_rhs = SI.get_dimensional_expr(boltzmann_constant / second)
    assert lhs != rhs and lhs == repaired_entropy_rate_rhs
    return {
        "claim": "§12.3.1 formula uses entropy-production rate on LHS and energy/time on RHS",
        "test": "SymPy SI dimensional-expression comparison",
        "lhs": str(lhs), "rhs": str(rhs), "same_dimension": lhs == rhs,
        "entropy_rate_candidate": str(repaired_entropy_rate_rhs),
        "scope": "Units only. Replacing k_B*T by k_B corrects dimensions but does not prove report encoding requires erasure.",
        "result": "dimensional mismatch confirmed",
    }


def reversible_reporting_logic() -> dict:
    """CNOT is bijective, copies source when initialized target is zero."""
    mapping = {(x, y): (x, x ^ y) for x, y in product((0, 1), repeat=2)}
    bijective = len(set(mapping.values())) == len(mapping) == 4
    copies_when_blank = all(mapping[(x, 0)] == (x, x) for x in (0, 1))
    assert bijective and copies_when_blank
    return {
        "claim": "§12.3.1(A): encoding a distinguishable report logically requires erasure of the encoded bit count",
        "test": "Exact 2-bit reversible CNOT truth-table enumeration",
        "mapping": {str(k): list(v) for k, v in mapping.items()},
        "bijective": bijective, "copies_source_when_target_zero": copies_when_blank,
        "result": "counterexample to logical necessity of erasure in the copying operation",
        "scope": "Does not claim a cost-free reusable physical recorder. Initialization, reset, noise and control need separate physical accounting.",
    }


def intersection_properness() -> dict:
    """§12.3.3 TC.1: intersection is always subset, not always proper subset."""
    universe = ("a", "b")
    sr = frozenset(universe)
    stheta = frozenset(universe)
    sc = frozenset(universe)
    intersection = sr & stheta & sc
    assert intersection == sr

    # Second route: SMT satisfiability of the negation of proper inclusion.
    sr_vars = [z3.Bool(f"r_{i}") for i in range(2)]
    theta_vars = [z3.Bool(f"t_{i}") for i in range(2)]
    closure_vars = [z3.Bool(f"c_{i}") for i in range(2)]
    solver = z3.Solver()
    solver.add(*sr_vars, *theta_vars, *closure_vars)
    strict = z3.Or(*[
        z3.And(sr_vars[i], z3.Not(z3.And(theta_vars[i], closure_vars[i])))
        for i in range(2)
    ])
    solver.add(z3.Not(strict))
    status = solver.check()
    assert status == z3.sat
    return {
        "claim": "§12.3.3 TC.1: S_r ∩ S_theta ∩ S_c is strictly smaller than S_r automatically",
        "test": "Explicit finite sets, independently encoded SMT satisfiability",
        "S_r": sorted(sr), "S_theta": sorted(stheta), "S_c": sorted(sc),
        "intersection": sorted(intersection),
        "strict_subset": intersection < sr,
        "smt_result_for_non_strict_case": str(status),
        "result": "counterexample to universal strict inclusion",
        "scope": "Does not refute strictness after an additional, empirically defended exclusion premise; that premise is the missing obligation.",
    }


def three_channel_flattening() -> dict:
    """Any finite triple can be represented as a pair with grouped prediction data."""
    triples = list(product((0, 1), repeat=3))
    encoded = [((theta, closure), report) for theta, closure, report in triples]
    decoded = [(prediction[0], prediction[1], report) for prediction, report in encoded]
    assert decoded == triples and len(set(encoded)) == len(triples)
    return {
        "claim": "§12.3.3: exactly three measurement channels escape the general prediction/inference split",
        "test": "Exhaustive finite product bijection (theta, closure, report) ↔ ((theta, closure), report)",
        "triple_domain_size": len(triples), "paired_domain_size": len(set(encoded)),
        "bijection": True,
        "result": "three channels alone do not escape a two-part partition with unrestricted internal prediction data",
        "scope": "Additional instruments can improve empirical discrimination; this only tests the claimed representational escape.",
    }


def lenient_dependency_toy() -> dict:
    """Construct a finite possible-data relation that is neither full nor functional."""
    internal = (0, 1)
    reports = (0, 1)
    feasible = {(0, 0), (1, 0), (1, 1)}  # (internal observable, report)
    cartesian = set(product(internal, reports))
    full_product = feasible == cartesian
    internal_determined_by_report = all(
        len({i for i, r in feasible if r == report}) == 1 for report in reports
    )
    assert not full_product and not internal_determined_by_report
    return {
        "claim": "A middle logical regime can exist between Cartesian independence and strict report→internal determination",
        "test": "Exhaustive finite relation over two internal and two report values",
        "feasible_pairs": sorted([list(p) for p in feasible]),
        "full_cartesian_product": full_product,
        "internal_function_of_report": internal_determined_by_report,
        "result": "constructive bounded example of non-full, non-functional pairing",
        "scope": "Only a toy data relation. Does not establish K&H's full variation conditions, physical realizability, an organizational closure mechanism or a phenomenal identity.",
    }


def refines(finer: tuple[frozenset, ...], coarser: tuple[frozenset, ...]) -> bool:
    return all(any(cell <= old for old in coarser) for cell in finer)


def functor_refinement() -> dict:
    """Countermodel to automatic refinement preservation by an unspecified map."""
    domain = frozenset((1, 2, 3))
    old = (frozenset((1, 2)), frozenset((3,)))
    new = (frozenset((1, 3)), frozenset((2,)))
    assert frozenset().union(*old) == domain
    assert frozenset().union(*new) == domain
    assert not refines(new, old)

    # The article describes closure-preserving source arrows but supplies no
    # axiom linking their existence to refinement of environmental partitions.
    source_arrow = z3.Bool("closure_preserving_source_arrow")
    induced_refinement = z3.Bool("environment_partition_refines")
    solver = z3.Solver()
    solver.add(source_arrow, z3.Not(induced_refinement))
    status = solver.check()
    assert status == z3.sat
    return {
        "claim": "§12.6.3 CF.1: closure-preserving maps necessarily induce refinement of threat/support partitions",
        "test": "Two explicit partitions plus SMT missing-bridge countermodel",
        "old_partition": [sorted(s) for s in old],
        "new_partition": [sorted(s) for s in new],
        "new_refines_old": refines(new, old),
        "source_arrow_without_target_refinement": str(status),
        "result": "the alleged implication needs a distinct monotonicity/compatibility axiom",
        "scope": "Illustrative formalization, not a physical counterexample to all possible closure morphisms. A stronger definition may restore a functor but must be justified and tested.",
    }


def thermodynamic_collision_measure() -> dict:
    """§12.5.2 TD.1 needs a specified measure and an injectivity/genericity proof."""
    structures = ("A", "B")
    profiles = {"A": (1, 2), "B": (1, 2)}
    pairs = list(product(structures, repeat=2))
    distinct_pairs = [(x, y) for x, y in pairs if x != y]
    collisions = [(x, y) for x, y in distinct_pairs if profiles[x] == profiles[y]]
    frequency = Fraction(len(collisions), len(distinct_pairs))
    assert frequency == 1
    return {
        "claim": "§12.5.2 TD.1: different closures have identical thermodynamic profiles only on a measure-zero set",
        "test": "Exact discrete ensemble with two distinct structures and identical profiles",
        "distinct_pairs": distinct_pairs, "profile": profiles["A"],
        "collision_fraction": str(frequency),
        "result": "measure-zero assertion is not universal without an ensemble/measure and a proof of genericity",
        "scope": "Countermodel to unrestricted measure claim, not evidence that physical closure networks usually share profiles under a specified continuous distribution.",
    }


def main() -> None:
    results = [
        unit_contract(), reversible_reporting_logic(),
        intersection_properness(), three_channel_flattening(), lenient_dependency_toy(),
        functor_refinement(), thermodynamic_collision_measure(),
    ]
    print(json.dumps({
        "source": "Nathan Sweet, Consciousness Naturalized, WordPress #2115; original §12 formal assertions",
        "scope": "Reproducible local checks, not peer-reviewed proof or demonstration of consciousness",
        "python": platform.python_version(), "sympy": sympy.__version__,
        "z3": z3.get_version_string(),
        "checks": results,
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
