#!/usr/bin/env python3
"""Independently check the small, selected Reser 2021 complete-recall counts.

This checks arithmetic in a published report, not its randomization, analysis
plan, sampling, selection, confidence intervals or clinical generalizability.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
import json


def two_sided_fisher(a: int, b: int, c: int, d: int) -> Fraction:
    n1, n2 = a + b, c + d
    successes, n = a + c, n1 + n2

    def mass(x: int) -> Fraction:
        if not (max(0, successes - n2) <= x <= min(n1, successes)):
            return Fraction(0)
        return Fraction(comb(successes, x) * comb(n - successes, n1 - x), comb(n, n1))

    observed = mass(a)
    return sum(
        (mass(x) for x in range(max(0, successes - n2), min(n1, successes) + 1)
         if mass(x) <= observed),
        Fraction(0),
    )


def main() -> None:
    # Exact source counts, doi:10.1371/journal.pone.0251710, Fig. 3/Results.
    aboriginal_success, aboriginal_total = 12, 19
    palace_success, palace_total = 10, 22
    population_baseline_success, population_total = 17, 76
    ratio_reported = Fraction(aboriginal_success, aboriginal_total) / Fraction(
        population_baseline_success, population_total
    )
    conventional_baseline_odds_ratio = Fraction(
        aboriginal_success, aboriginal_total - aboriginal_success
    ) / Fraction(population_baseline_success, population_total - population_baseline_success)
    direct_odds_ratio = Fraction(
        aboriginal_success * (palace_total - palace_success),
        (aboriginal_total - aboriginal_success) * palace_success,
    )
    exact_p = two_sided_fisher(
        aboriginal_success, aboriginal_total - aboriginal_success,
        palace_success, palace_total - palace_success,
    )
    # Independent implementation check when SciPy is present.
    scipy_result = None
    try:
        from scipy.stats import fisher_exact
        result = fisher_exact([[12, 7], [10, 12]], alternative="two-sided")
        assert abs(result.statistic - float(direct_odds_ratio)) < 1e-12
        assert abs(result.pvalue - float(exact_p)) < 1e-12
        scipy_result = {"odds_ratio": result.statistic, "p": result.pvalue}
    except ImportError:
        pass
    assert ratio_reported == Fraction(48, 17)
    assert direct_odds_ratio == Fraction(72, 35)
    record = {
        "source": "Reser et al. 2021, doi:10.1371/journal.pone.0251710; Results/Fig.3",
        "source_counts": {"Aboriginal_perfect_after_below_perfect_baseline": "12/19", "memory_palace": "10/22", "overall_perfect_at_baseline": "17/76"},
        "authors_label": "OR=2.82, 95% CI 1.15-6.09 for Aboriginal method",
        "reproduces_2_82_as_ratio_of_proportions": str(ratio_reported),
        "reproduces_2_82_as_ratio_of_proportions_float": float(ratio_reported),
        "conventional_odds_ratio_against_population_baseline": float(conventional_baseline_odds_ratio),
        "direct_aboriginal_vs_memory_palace_odds_ratio": float(direct_odds_ratio),
        "fisher_exact_2sided_enumerated": float(exact_p),
        "fisher_exact_2sided_scipy": scipy_result,
        "scope": "Exploratory, unadjusted direct 2-by-2 comparison among participants below perfect recall at baseline; independence/selection and multiple outcomes not validated; no claim of randomized treatment effect or source-author statistical intent",
        "interpretation": "The published 2.82 numerically matches a ratio of post-training perfect-recall proportions to the overall baseline fraction, rather than a conventional odds ratio. The selected 12/19 vs 10/22 comparison is not decisive under Fisher's two-sided test; it does not establish direct superiority on the perfect-recall measure.",
    }
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
