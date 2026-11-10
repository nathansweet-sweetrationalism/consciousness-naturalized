# Consciousness Naturalized: article and revisable research programme

**Author:** Nathan Sweet (independent researcher)  
**Canonical reading edition:** https://sweetrationalism.com/articles/consciousness/consciousness-naturalized-a-falsifiable-substrate-agnostic-consciousness-theory-ai-biology/  
**Article-specific source archive:** https://github.com/nathansweet-sweetrationalism/consciousness-naturalized  
**Research hub mirror:** https://github.com/nathansweet-sweetrationalism/sweet-rationalism-research/tree/main/articles/consciousness-naturalized-a-falsifiable-substrate-agnostic-consciousness-theory-ai-biology  
**Zenodo v1.1.0 DOI:** https://doi.org/10.5281/zenodo.24119682  
**Zenodo all-versions DOI:** https://doi.org/10.5281/zenodo.24119681  
**Website reading-edition revision date:** November 10, 2026  
**Consolidated WordPress history ZIP:** https://sweetrationalism.com/wp-content/uploads/2026/11/Consciousness_Naturalized_2115_Reconstruction_2026-11-10_FINAL.zip
**Zenodo status:** v1.1.0 DOI is immutable; a subsequent version for the updated reading edition remains to be deposited.

The article evaluates consciousness theories by their explanatory targets, scope, rival predictions, interventions, independent evidence and explicit conditions for losing support. Its organizational hypothesis is an open **research claim**, not a validated identity between closure and experience. No executable check establishes a phenomenal bridge. The WordPress edition is canonical for reading and ongoing corrections; GitHub and Zenodo preserve versioned, independently inspectable copies.

## What this archive contains

- `article.html`: the entire unabridged Gutenberg/HTML body, including current live metadata links; the immutable Zenodo v1.1.0 ZIP contains the edition at the moment it was deposited, before post-deposit DOI self-links could be added.
- `public_revision_diff.txt`: an exact unified text diff retaining removed formulations. It is a public correction record, not a source-verification certification.
- [Consolidated WordPress revision archive](https://sweetrationalism.com/wp-content/uploads/2026/11/Consciousness_Naturalized_2115_Reconstruction_2026-11-10_FINAL.zip): WordPress-hosted combined recovery ZIP (media attachment 218725759, 1,460,691 bytes); its described contents are earlier history, current snapshot, diff and manifest. Media registration and canonical article link are verified; ZIP member-level inspection is still outstanding.
- `WordPress_Reconstruction_History_2026-11-10.zip`: the earlier twelve-revision reconstruction retained here as a separate historical predecessor; do not confuse it with the consolidated ZIP.
- `CLAIM_DEPENDENCY_MAP.json`: claim types, dependencies, rival accounts, interventions and conditions under which support should fall. It stores no protected set of conclusions.
- `PROSPECTIVE_PROTOCOL.md`, `PROSPECTIVE_COMPARISON_PROTOCOL_v0.1.0.json`, and `prereg_proposals/`: five pre-data protocol proposals with explicitly unresolved registration fields.
- `computational_supplement/`: self-contained finite-model logic checks, arithmetic, solver examples, source, and integrity hashes. Read its bounded proof-duty disclaimer.
- `metadata.json`, `CITATION.cff` and `RELEASE_CHECKLIST.md`: version and release provenance, including the verified Zenodo identifiers.

## Does this count as preregistration?

**No complete empirical study is registered yet.** A date-stamped, publicly frozen proposal prevents retrospective invention of predictions *from that date onward*, but is not a substitute for a study-specific registry record with population, recruitment, sample size or justified precision, instruments, exclusions, interventions, decision thresholds, allocation and analysis plan. Neither clinical recordings nor machine trials have yet been analyzed under these protocols. The frozen proposal is a prospective *protocol precursor*; results must not be presented as confirmatory unless their test-specific rules were fixed before looking at outcomes.

### The crucial proposed discriminator

Compare systems or states matched on a rival theory's specified recurrent processing, broadcast, integration, metarepresentation, reporting capacities and resource budget while deliberately varying **causally endogenous, temporally restored self/world/action regulation**. Only independently calibrated human/animal phenomenal evidence can test the proposed consciousness bridge. Engineered closed-loop vs yoked-controller performance can test causal agency and control **without labeling a robot conscious**. The same design must permit IIT, active inference/enactive models and other serious alternatives to win when their own prospectively specified variables explain the outcome better.

The proposed decisive evidence is **not already in hand**. Relative cross-validated predictive and intervention-sensitive gains, replicated over calibrated endpoints and perturbations with no shared label/marker definition, would strengthen the organizational account. Equal or better gains from a simpler rival, an independently confirmed dissociation or failure to reproduce the phenomenon under prospective controls would reduce its scope. No reduction or preservation of a philosopher's problem-form proves metaphysical physicalism.

## Reproducibility and limits

Install the versions in `computational_supplement/verification/requirements.txt`, then run:

```sh
python computational_supplement/verification/run_checks.py
z3 computational_supplement/verification/partition_non_strict.smt2
z3 computational_supplement/verification/thermodynamic_units.smt2
```

The expected `sat` responses are countermodels within stipulated formal languages, not empirical test outcomes. Separate prior runs checked all six Python groups; a new environment without `z3` cannot independently reproduce those groups until that dependency is installed. The public source review was closed by Nathan Sweet on November 10, 2026; this is author review, not external peer review or an unqualified verification claim.

## Provenance and privacy

Nathan explicitly authorized public preservation of the complete historical WordPress reconstruction. The private source-verification working ledger, private research conversation, correspondence, copied third-party PDFs, local tokens and credentials are not included. The author explicitly authorized public visibility and search indexing of this specific article on November 10, 2026; current WordPress SEO is `index,follow`. Do not generalize that authorization to other previously protected articles. No theme or plugin updates are authorized.

When a claim fails, correct the specific dependent claim and propagate the change to the article, both repositories, public TXT diff, and subsequent Zenodo version. Do not silently rewrite an immutable DOI version or delete the older counterexample.
