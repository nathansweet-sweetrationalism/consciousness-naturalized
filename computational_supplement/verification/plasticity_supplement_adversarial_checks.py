#!/usr/bin/env python3
"""Exact boundary tests of claims in O'Reilly-Shah et al. 2026 S1.

These target stated *inferences from* Theorems 3.2 and 7.2 and Remark 7.4,
not the narrow mathematical truth of the two theorems themselves.
"""
import itertools
import json
from fractions import Fraction


def relu(x):
    return max(Fraction(0), x)


def interpolating_static_relu_network(x, n):
    """Fixed ReLU FNN f_n on [0,1], all parameters rational."""
    x = Fraction(x)
    return x / n + Fraction(2, n) * sum(
        (relu(x - Fraction(k, n)) for k in range(1, n)), Fraction(0)
    )


def piecewise_linear_secant(x, n):
    """Independent exact oracle using linear interpolation of square."""
    k = min(int(x * n), n - 1)
    a, b = Fraction(k, n), Fraction(k + 1, n)
    return a * a + (x - a) * (b * b - a * a) / (b - a)


def check_approximation():
    data = []
    for n in (1, 2, 4, 8, 16, 32):
        candidates = [Fraction(i, 2 * n) for i in range(2 * n + 1)]
        errors = []
        for x in candidates:
            approx = interpolating_static_relu_network(x, n)
            assert approx == piecewise_linear_secant(x, n)
            errors.append(abs(approx - x*x))
        measured_max = max(errors)
        exact_sup = Fraction(1, 4*n*n)
        assert measured_max == exact_sup
        data.append({"n_segments":n,"max_error_exact":str(measured_max),
                     "max_error_float":float(measured_max),"formula_sup_exact":str(exact_sup)})
    return {
        "claim_under_test":"S1 Remark 7.4: any finite or countable union of static FNNs has bounded approximation capacity",
        "construction":"Countable family of finite static rational-weight ReLU nets f_n(x)=x/n+(2/n)Σ_k ReLU(x-k/n), n positive integer",
        "target":"g(x)=x^2 on [0,1]",
        "proof":"Each f_n is exact piecewise-linear interpolant; f_n(x)-x²=(x-a)(b-x) on [a,b], length=1/n, hence sup error=1/(4n²)→0.",
        "checks":data,
        "result":"A countable family of individually fixed FNNs approximates a target g not equal to any family member arbitrarily closely; refutes blanket countable-family inference, not Theorem 7.2's fixed-f positive distance.",
        "scope":"One explicit target suffices against an unqualified no-arbitrary-approximation claim. Full C([0,1]) density also follows via standard piecewise-linear interpolation but is not machine-proved here."
    }


def check_input_domain():
    counts=[]
    for t in range(1,8):
        domain = list(itertools.product((0,1),repeat=t))
        counts.append({"history_length":t,"history_domain_cardinality":len(domain)})
        assert len(domain)==2**t
    return {
        "claim_under_test":"S1 Theorem 3.2 labels growing input-history domains a plasticity condition",
        "fixed_weight_model":"h_t = h_(t-1) + x_t, y_t = h_t, h_0=0, x_t∈{0,1}; parameters never update",
        "history_domains":counts,
        "result":"The theorem's growing-history-domain premise holds for a fixed-weight recurrent model; its non-equivalence under strict domain matching is not specific to plasticity.",
        "scope":"A counterexample to the characterization of the premise as plasticity, not a counterexample to Theorem 3.2 under its stated domain-equality definition."
    }


if __name__ == "__main__":
    print(json.dumps({"source":"O'Reilly-Shah, Selvitella & Schurger (2026), S1 pp. 8–9, 22–23",
                      "cases":[check_approximation(),check_input_domain()]},indent=2))
