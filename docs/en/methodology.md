# Methodology and evidence {#methodology-and-evidence}

**STATUS: RIEMANN HYPOTHESIS OPEN**

This is an AI-assisted research log curated by @ykbballer91. It records proposed mechanisms, exact calculations, literature comparisons, attempted constructions, counterexamples, and reasons to stop. The public prose has been edited so that readers do not need the original conversation.

## Human direction and AI assistance {#human-direction-and-ai-assistance}

The creator supplied problem framing, hypotheses, changes of abstraction, interpretation and instructions about which avenues to continue or stop. AI/Codex assisted with literature retrieval, symbolic derivations, numerical diagnostics, proof attempts, counterexample searches, separate internal reviews, and preparation of this repository. The author display is @ykbballer91; this is neither a claim of human-only derivation nor of an autonomous AI proof of RH.

## What an audit means here {#what-an-audit-means-here}

An internal independent audit means a separate AI reviewer examined the stated mathematical argument or computational artifact. It is useful adversarial checking; it is not external peer review, endorsement by a named mathematician, or machine verification of all claims. The archived audit identifies the material and scope it checked.

A validation script may check hashes, finite numerical identities, links, syntax, or a designated computational certificate. Its `PASS` applies only to those checks. Historical source validation records are retained as evidence of the original run, not as a claim that all experiments were rerun during publication.

Formal Lean files cover selected lemmas in the recorded environment. A successful build of those files does not certify the entire research program, the numerical code, or RH.

## Claim discipline {#claim-discipline}

- A theorem states its space, domain, quantifiers, normalization, and hypotheses.
- A conditional implication keeps its unproved premise visible.
- A synthetic counterexample refutes a proposed inference from specified properties; it is not a counterexample to the actual zeta function unless explicitly proved to be one.
- A finite computation is diagnostic or a component of a specified certificate. It is not evidence that an untested limiting estimate holds.
- A result in one topology is not transferred to another without proof.
- A fixed finite-dimensional result is not made uniform in dimension by notation alone.

## L0–L7 summaries and verification level

The [2026-10-09 update](updates/2026-10-09-logic-rh-l7.md) selectively summarizes privately preserved research manuscripts. Complete new proofs, audits and code are not public, so the summary is neither a complete proof nor full reproduction evidence. The researcher's choice of B is distinguished from a mathematical proof of independence.

L7 is established at the level of usual arguments inside ZFC and a syntactic length bound in the same proof system. PA-provability of global violation preservation, a complete Hilbert proof string, machine proof and numerical cost constants are not certified. Exact finite checks and internal AI review of the original work have separate scopes.

L6 adopts an external 7/8 nonvanishing result. External Lean/kernel success logs, version comparison and local mathematical checks were examined; our own kernel/comparator was not run. Full reproof of the paper, machine translation from Lean to ZFC and external peer review are not certified. Publication builds, links, bilingual and safety checks do not add mathematical verification.


## Source and editorial policy {#source-and-editorial-policy}

The source research tree is preserved. Public archive copies have separate hashes and a [rewrite manifest](../../audit/rewrite_manifest.md). Editorial changes remove machine-local references, explain internal shorthand, and improve navigation. They do not strengthen mathematical claims or erase failed routes.

The timeline distinguishes Git timestamps from dates explicitly recorded in later uncommitted research documents. Navigation order is not a fabricated chronology of parallel work. The original 17-track inventory is retained, and the subsequent cyclicity and finite-head results are identified as separate updates.

Known results are attributed to primary literature where the research records provide it. A statement-level verification note is not a declaration that every theorem in a cited paper has been independently reproved. External papers are linked, not redistributed.

## Publication scope {#publication-scope}

Version 0.1.0 was made public on 2026-09-30, after the creator-authorized Phase 3 review gates and final private-branch CI passed. Publication metadata records release state separately from the historical research snapshots. This repository's licenses govern original exported material; third-party works retain their own rights.
