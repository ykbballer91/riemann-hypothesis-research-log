# Phase 3 publication safety review

**STATUS: RIEMANN HYPOTHESIS OPEN**

Review date: 2026-09-30. This report concerns the selected publication payload, not publication of the original research tree or its Git history.

## Original research preservation

A before/after SHA-256 inventory covered **60,812 regular files and four symlinks**, excluding Git metadata directories consistently. The comparison found **0 added, 0 deleted and 0 modified research-tree files**, identical symlink targets, unchanged source HEAD and unchanged tracked/untracked Git status. An intermediate scanner accidentally included 252 nested dependency Git metadata files excluded by the baseline; reconciling the inventory rule removed this apparent discrepancy. No file was deleted or changed to obtain this result. These private inventories are not exported.

## Payload and history safety

The assembled 438-file candidate snapshot and all 425 reachable Git blobs across its five pre-review commits passed the credential, private-key, personal-contact, machine-path and private-URL patterns in [the safety scanner](../tools/scan_publication.py). Author and committer metadata use the selected public handle and GitHub noreply address. There were **0 secret findings and 0 unintended sensitive-path/contact findings**. The final staged snapshot and resulting Git history are rescanned before publication; the publication report records the later public-history scan separately.

No original private Git history, runtime environment, dependency source tree, private full inventory, third-party paper PDF, screenshot or binary research bundle is in the public payload. Only allowlisted publication audits are exported. The source manifest and rewrite records distinguish original hashes from the portable public copies.

## Rights and mathematical scope

The creator-authorized display is **@ykbballer91**. Original text and figures use CC BY 4.0; original code and experiment scripts use MIT. Third-party works retain their rights. [The citation review](phase3_citation_review.md) records the checked sources and access limitations. An independent bounded check of 439 prospective files found no bundled paper/image/archive payload, no Markdown block quotation of 100 words or more, and no apparent third-party full-paper reproduction. An external-code comparison wrapper does not bundle that external implementation and records the reproduction limitation. No material licensing blocker was identified; this is a publication-scope review, not a legal ownership adjudication.

All overview pages retain RH OPEN. The independent content review distinguishes auxiliary proofs, conditional applications, restricted results, numerical diagnostics and open obligations. No public claim of an RH proof, a percentage of completion or external peer review was identified.

## Limits and release controls

Pattern scanners cannot guarantee detection of every possible secret. Static link checks do not verify every external URL, and publication checks do not reprove the mathematics. Their actual scopes are recorded, rather than promoted to universal guarantees.

Before release, the repository remains private and the Pages deployment guard remains intact. The creator's explicit conditional authorization permits publication only after every blocking gate passes. A serious post-publication exposure, false RH-proof claim or rights violation requires immediate rollback to private visibility if technically possible.
