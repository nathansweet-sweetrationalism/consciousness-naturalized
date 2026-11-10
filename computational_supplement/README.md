# Consciousness Naturalized: public computational supplement

Author: Nathan Sweet. Released with the article **Consciousness Naturalized: A Falsifiable Substrate-Agnostic Consciousness Theory**.

**Canonical article:** https://sweetrationalism.com/articles/consciousness/consciousness-naturalized-a-falsifiable-substrate-agnostic-consciousness-theory-ai-biology/

The public ZIP contains executable, bounded mathematical checks of the paper's repaired and rejected formal inferences. It includes hand-coded finite countermodels, dimensional consistency checks, a simple numerical Landauer example, propositional validity tests, finite Kleiner–Hoel dependency examples, and an independent check on cited statistics. It also supplies an explicitly empty experimental record template. No private communications, private audit dialogue or unlicensed source PDFs are included.

## Reproduce

Use Python 3.11 or newer in an isolated environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The two `.smt2` examples can additionally be checked with `z3 verification/partition_non_strict.smt2` and `z3 verification/thermodynamic_units.smt2` if the Z3 command-line executable is installed. These examples exhibit satisfiable countermodels, not empirical constraints on real consciousness studies.

## Map of claims to scripts

| Target | Checker | What the result can establish |
| --- | --- | --- |
| Part I, §1.7: erasure, second-law dimensions, finite viability, bare graph cycles | `foundational_formal_checks.py` | Correct arithmetic/units and restricted logical countermodels |
| Section XII: thermodynamic reporting, intersections, three-channel partition, illustrative non-full/non-functional dependence, functor/measure allegations | `section_xii_formal_checks.py` | Local formal validity or explicit finite countermodels; not physical implementation |
| Section XII, Kleiner–Hoel Definitions 3.8/A.2/4.2 | `kh_dependency_finite_model.py` | Exact outcomes in one deliberately stipulated binary deterministic observation model |
| Section XII, 2026 plasticity supplement | `plasticity_supplement_adversarial_checks.py` | Explicit constructed mathematical tests of statements as translated; not a proof of full published theorems |
| Selected argumentative entailments | `logic_audit.py` plus `article_2115_classical_logic_claims.json` | Propositional validity/countermodels under specified translations |
| Indigenous memory pedagogy discussion | `reser_exact_statistical_audit.py` | Calculation and chosen contingency-test results from reported aggregate counts, not a replication of the study |

The `experiment_record_template.json` is a schema-shaped starting point, **not experimental data**. A biologist testing a hypothesis must specify the boundary, timescale, instruments, interventions, negative controls, comparison models, sample size and preregistered loss before collecting data. Clinical markers and participant reports require independent calibration; no mathematical result here identifies phenomenality by stipulation.

## Interpretation and correction

Checks verify **encodings and assumptions**, never an unexamined translation from prose or a source paper. Several tests intentionally reject claims in earlier article revisions. Such a countermodel defeats the stated unrestricted inference only. It does not establish the opposite empirical proposition. Formal and biological critics can revise any test or present a physically instantiated rival; the proper response is to update the dependencies and the article's claim accordingly.

The canonical page is the publication of record. The article-specific repository and DOI are pending, and their links must not be represented as active until verified. See `SHA256SUMS.txt` in the archive to verify the files.
