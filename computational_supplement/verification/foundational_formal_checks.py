#!/usr/bin/env python3
"""Exact bounded checks for the private Part I mathematical reconstruction.

These demonstrate specific valid calculations and invalid inferences. They are
not a proof of any theory of consciousness or an experimental validation of
Landauer's principle, organizational closure, or causal emergence.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import json

from sympy.physics.units import joule, kelvin
from sympy.physics.units.systems.si import SI
import z3


def landauer_one_bit():
    getcontext().prec = 42
    k_b = Decimal("1.380649e-23")  # exact defined SI numerical value, J/K
    temperature = Decimal("300")  # illustrative K, not an observed dataset
    ln2 = Decimal(2).ln()
    bound_j = k_b * temperature * ln2
    assert Decimal("2.8e-21") < bound_j < Decimal("2.9e-21")
    return {
        "name": "illustrative_isothermal_one_bit_reset_bound",
        "temperature_K": "300",
        "k_B_J_per_K": str(k_b),
        "Q_min_J": str(bound_j),
        "units": "(J/K)*K = J",
        "scope": "Average reservoir heat for a symmetric, initially unknown bit reset in the ideal isothermal setting; neither a universal cost of maintaining distinctions nor a measured heat.",
        "result": "pass",
    }


def identity_is_not_erasure():
    identity = {b: b for b in (0, 1)}
    reset = {b: 0 for b in (0, 1)}
    assert len(set(identity.values())) == 2
    assert len(set(reset.values())) == 1
    return {
        "name": "bijective_memory_persistence_versus_logically_irreversible_reset",
        "identity_bijective": True,
        "reset_bijective": False,
        "scope": "Logical state-map check only. It rejects automatic application of the one-bit erasure bound to an identity operation. It does not assert cost-free indefinite physical retention.",
        "result": "pass",
    }


def finite_viability():
    """Two-step finite analogue of the quantified viability definition."""
    states = set(range(4))
    acceptable = {0, 1}
    controlled = {-1, 0}

    def viable(horizon, controls):
        survivors = acceptable.copy()
        for _ in range(horizon):
            survivors = {
                x for x in acceptable
                if any(x + 1 + u in survivors for u in controls)
            }
        return survivors

    controlled_set = viable(2, controlled)
    uncontrolled_set = viable(2, {0})
    assert controlled_set == {0, 1}
    assert uncontrolled_set == set()
    assert acceptable <= states
    return {
        "name": "finite_horizon_viability_depends_on_admissible_controls",
        "dynamics": "x[t+1] = x[t] + 1 + u[t]",
        "K": sorted(acceptable),
        "horizon_steps": 2,
        "control_set": sorted(controlled),
        "viability_with_control": sorted(controlled_set),
        "viability_without_control": sorted(uncontrolled_set),
        "scope": "Exact finite countermodel to suppressing the control quantifier. Does not validate the continuous physical system or equate viability with conscious experience.",
        "result": "pass",
    }


def closure_cycle_needs_implementation():
    """Model with a structural graph cycle and absent physical power supply."""
    graph_arcs = {(0, 1), (1, 0)}
    has_cycle = (0, 1) in graph_arcs and (1, 0) in graph_arcs
    external_energy_available = False
    constraints_maintained = has_cycle and external_energy_available
    assert has_cycle and not constraints_maintained
    return {
        "name": "graph_cycle_does_not_entail_real_constraint_maintenance",
        "arcs": sorted([list(edge) for edge in graph_arcs]),
        "has_cycle": has_cycle,
        "external_energy_available": external_energy_available,
        "maintained_in_toy_model": constraints_maintained,
        "scope": "Logical independence test. Real Montévil–Mossio closure requires identifying maintained physical constraints, processes, environmental support, and appropriate timescales.",
        "result": "pass",
    }


def local_success_not_exhaustive_ontology():
    """One explicit finite first-order countermodel for invalid promotion."""
    local_targets = [z3.Bool(f"p_{i}") for i in range(3)]
    solver = z3.Solver()
    solver.add(local_targets[0], local_targets[1], z3.Not(local_targets[2]))
    status = solver.check()
    assert status == z3.sat
    return {
        "name": "bounded_success_does_not_logically_entail_universal_physicalism",
        "tested_target_successes": 2,
        "additional_unsettled_target": 1,
        "countermodel_satisfiable": str(status),
        "scope": "Formal quantifier point only; existence of an actual nonphysical entity is not asserted or supported by this model.",
        "result": "pass",
    }


def dimension_consistency():
    entropy_dimension = SI.get_dimensional_expr(joule / kelvin)
    heat_over_temperature_dimension = SI.get_dimensional_expr(joule / kelvin)
    heat_dimension = SI.get_dimensional_expr(joule)
    assert entropy_dimension == heat_over_temperature_dimension
    assert entropy_dimension != heat_dimension
    return {
        "name": "second_law_balance_dimensional_contract",
        "entropy_units": "J/K",
        "heat_units": "J",
        "temperature_units": "K",
        "Q_over_T_units": "J/K",
        "symbolic_SI_entropy_dimension": str(entropy_dimension),
        "symbolic_SI_heat_over_T_dimension": str(heat_over_temperature_dimension),
        "scope": "Unit ledger and symbolic expression shape only. A thermodynamic entropy balance requires the physical assumptions and proper sign convention stated in the prose.",
        "result": "pass",
    }


if __name__ == "__main__":
    checks = [
        landauer_one_bit(), identity_is_not_erasure(), finite_viability(),
        closure_cycle_needs_implementation(), local_success_not_exhaustive_ontology(),
        dimension_consistency(),
    ]
    print(json.dumps({"status": "passed", "checks": checks}, indent=2))
