#!/usr/bin/env python3
"""Finite toy models of Kleiner–Hoel dependence, *not* consciousness tests.

The physical system p has one deterministic observation pair (i,r). The exact
2021 definitions use a more general observation correspondence and variations
of physically realizable systems. The finite deterministic case below is a
strictly declared special case, useful for checking quantifier structure.
"""

import itertools
import json


def assess(name, pairs, conceivable_pairs):
    pairs = frozenset(pairs)
    conceivable_pairs = frozenset(conceivable_pairs)
    assert pairs <= conceivable_pairs
    internal = sorted({i for i, _ in pairs})
    reports = sorted({r for _, r in pairs})
    # In this deterministic-observation specialization, Definition 3.8
    # requires all (i,r) combinations to be realizable within the class P.
    missing = sorted(set(itertools.product(internal, reports)) - pairs)
    strong_independence = not missing

    # Definition A.2 is weaker; here every differing binary internal value
    # predicts a disjoint experience, so a minimally different partner to i
    # must be available with the same report r for *each* observed (i,r).
    weak_independence = all(
        any(i2 != i and r2 == r for i2, r2 in pairs)
        for i, r in pairs
    )

    # Definition 4.2 quantifies over all *conceivable* datasets O_bar, not
    # merely observed/physically realizable O. The chosen O_bar is explicit.
    report_fibers = {
        str(r): sorted(i for i, report in pairs if report == r)
        for r in reports
    }
    conceivable_fibers = {
        str(r): sorted(i for i, report in conceivable_pairs if report == r)
        for r in sorted({r for _, r in conceivable_pairs})
    }
    strict_dependence = all(len(set(values)) == 1 for values in conceivable_fibers.values())

    # Predict(i)={i}; minimal informativeness holds because I={0,1}
    # for the examples below. Substitution demands same report, different
    # (thus disjoint) predictions, for at least one physical pair per report.
    local_substitution = {
        str(r): len({i for i, r2 in pairs if r2 == r}) > 1 for r in reports
    }
    universal_substitution = all(local_substitution.values())
    return {
        "model": name,
        "P_observable_pairs": sorted([list(pair) for pair in pairs]),
        "conceivable_O_bar_pairs": sorted([list(pair) for pair in conceivable_pairs]),
        "missing_physically_feasible_pair_candidates": [list(p) for p in missing],
        "strong_independence_Def3_8": strong_independence,
        "weak_independence_DefA_2_binary_specialization": weak_independence,
        "strict_dependency_Def4_2_on_O_bar": strict_dependence,
        "report_fibers": report_fibers,
        "conceivable_report_fibers": conceivable_fibers,
        "local_substitutions_by_report": local_substitution,
        "universal_substitution_in_model": universal_substitution,
        "notes": "No empirical or phenomenal inference; finite deterministic obs, binary predictions, feasible systems stipulated for countermodel only.",
    }


def main():
    examples = [
        ("full_product_independence_control", {(0, 0), (1, 0), (0, 1), (1, 1)}, {(0, 0), (1, 0), (0, 1), (1, 1)}),
        ("strict_dependency_control", {(0, 0), (1, 1)}, {(0, 0), (1, 1)}),
        ("middle_dependency_candidate", {(0, 0), (1, 0), (1, 1)}, {(0, 0), (1, 0), (0, 1), (1, 1)}),
    ]
    results = [assess(name, pairs, conceivable_pairs) for name, pairs, conceivable_pairs in examples]
    assert results[0]["strong_independence_Def3_8"] and results[0]["universal_substitution_in_model"]
    assert results[1]["strict_dependency_Def4_2_on_O_bar"] and not results[1]["strong_independence_Def3_8"]
    mid = results[2]
    assert not mid["strong_independence_Def3_8"]
    assert not mid["weak_independence_DefA_2_binary_specialization"]
    assert not mid["strict_dependency_Def4_2_on_O_bar"]
    assert mid["local_substitutions_by_report"] == {"0": True, "1": False}
    assert not mid["universal_substitution_in_model"]
    print(json.dumps({"reference": "Kleiner & Hoel (2021), Definitions 3.8, A.2, 4.2; Proposition 3.9", "results": results}, indent=2))


if __name__ == "__main__":
    main()
