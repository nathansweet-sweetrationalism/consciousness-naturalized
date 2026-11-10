# Consciousness Naturalized: verified article and executable companion archive

**Author:** Nathan Sweet  
**Canonical publication:** https://sweetrationalism.com/articles/consciousness/consciousness-naturalized-a-falsifiable-substrate-agnostic-consciousness-theory-ai-biology/  
**Version:** November 10, 2026 audited publication text (subsequent DOI metadata may be appended)  
**Article-specific GitHub repository:** https://github.com/nathansweet-sweetrationalism/consciousness-naturalized (created privately for archival synchronization).  
**Zenodo version/concept DOI:** **not assigned**. Do not cite a placeholder as a deposit.

The author personally completed his source review and approved this article edition for publication and deposit on 2026-11-10. This is a research publication and a bounded executable audit, not external peer review or a proof that any organization realizes phenomenality. The WordPress page remains the canonical reading edition; GitHub contains the archival companion, executable materials, typed claims and correction history. Zenodo identifiers will be inserted only when real deposits exist.

## Contents

- `article.html`: complete, unabridged exact WordPress Gutenberg HTML readback of the approved publication edition.
- `metadata.json`: article-specific publication and release state. Null DOI fields mean no verified deposit yet.
- `CLAIM_DEPENDENCY_MAP.json`: target-specific claim dependencies, rival models, observable differentiators and loss conditions. No immutable conclusion graph.
- `public_revision_diff.txt`: unified diff of the earliest recovered HTML and approved substantive edition; final link metadata changes are tracked in WordPress revision history and Git.
- `WordPress_Reconstruction_History_2026-11-10.zip`: owner-approved lossless 12-revision WordPress history, with historical complete post bodies and hashes.
- `computational_supplement/`: source code, countermodels, solver files, mathematical checks, exact calculations and SHA-256 manifest. Check the enclosed README for the exact scope and reproduction steps.

## Reproducibility

Install Python 3.11 or newer, `z3-solver==5.4.0.0` and `sympy==1.14.0` as specified in `computational_supplement/verification/requirements.txt`; then execute:

```sh
python computational_supplement/verification/run_checks.py
```

For the two SMT-LIB countermodels use:

```sh
z3 computational_supplement/verification/partition_non_strict.smt2
z3 computational_supplement/verification/thermodynamic_units.smt2
```

Expected `sat` means a satisfiable *formal countermodel under specified encoding*. Neither result tests actual clinical consciousness, constitutes an experiment, nor resolves the phenomenal bridge.

## Provenance and permissions

The owner explicitly authorized publication of the **full WordPress reconstruction history** on 2026-11-10. The source-verification working ledger, correspondence, private audit dialogue, copied third-party source PDFs and credentials are **not** included. Owner signoff closes source review as an author decision, not an independent full-text-verified scientific certification. The article's WordPress status and indexing/unlisting settings must be checked separately from repository and DOI creation.
