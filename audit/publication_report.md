# Publication report — version 0.1.0

**STATUS: RIEMANN HYPOTHESIS OPEN**

**Publication status: PUBLIC**

- GitHub repository: [ykbballer91/riemann-hypothesis-research-log](https://github.com/ykbballer91/riemann-hypothesis-research-log)
- GitHub Pages: [public documentation site](https://ykbballer91.github.io/riemann-hypothesis-research-log/) — **PUBLIC / DEPLOYED**
- Actual publication date: **2026-09-30**
- Author display: **@ykbballer91**
- Research text and original figures: **CC BY 4.0**
- Original code and experiment scripts: **MIT**
- Third-party works: retain their original rights.

## Authorization and observed release

The creator expressly authorized publication if and only if the complete Phase 3 review passed every listed gate and ended with **READY FOR CREATOR PUBLICATION APPROVAL**. No additional approval was requested or presumed. That [review](phase3_final_content_review.md), its independent adversarial review and the final private-branch CI passed before the repository visibility changed.

The PUBLIC setting was confirmed at **2026-09-30 05:39:26 UTC**; GitHub reported its visibility update at 05:39:21 UTC. The date in CITATION was added only after that observed transition. UTC and the creator's Asia/Tokyo calendar both give 2026-09-30. No earlier research date was substituted for the publication date.

The existing guarded Pages workflow then completed its build and deployment. The first successful deployment finished at **05:43:50 UTC**. The guard remains: explicit workflow dispatch, deploy input, public visibility and the creator-approval repository variable.

## Verification results

| Gate | Result |
|---|---|
| Phase 3 content review | **PASS**; 0 blocking mathematical/content issues |
| Misleading RH-proof implications | **0** |
| Citation review | **PASS within recorded Phase 3 scope**; 0 unresolved material blockers |
| Licensing | **PASS within publication scope**; 0 unresolved material blockers |
| Security/privacy | **PASS**; 0 unresolved findings |
| Secret scan | **PASS**; 0 findings |
| Unintended local absolute paths | **0** |
| Internal links | **0 broken** in Markdown and generated site |
| README rendering | **PASS** on actual GitHub; nine math elements rendered without observed errors |
| Mathematics rendering | **PASS on the checked public pages**; current state, roadmap and finite-head page rendered 23, 9 and 36 math elements with no observed MathJax errors |
| Anonymous repository access | **PASS**; unauthenticated API, repository HTML, raw README and Git mirror retrieval |
| Anonymous Pages access | **PASS**; HTTP 200 for landing, current state, roadmap, finite-head page and publication metadata |
| Landing banner | **STATUS: RIEMANN HYPOTHESIS OPEN** visibly present |
| CI | **PASS**; verified runs listed below |
| Pages workflow | **PASS**; build and deploy jobs both succeeded |
| Source research modifications | **0** |
| Emergency rollback trigger | None found; rollback was not required |

The current state and roadmap distinguish unconditional auxiliary cyclicity, fixed-order restricted selection, fixed-head algebraic spanning, finite numerical diagnostics, and the open quantitative joint-limit/full-ground comparison. Growing-order control, parity/ES, G* and RH remain open. The publication does not imply a nearly complete proof.

## Reproducible evidence

- [Final private-branch CI, run 36674309588](https://github.com/ykbballer91/riemann-hypothesis-research-log/actions/runs/36674309588), commit `4bf0eb8a65db33cf63cd593c7d92fad765a19da9`: PASS before the PUBLIC action.
- [Public-date update CI, run 36674586866](https://github.com/ykbballer91/riemann-hypothesis-research-log/actions/runs/36674586866), commit `9bba2c079bf114744c6c4d662796bd53e04c88c4`: PASS.
- [First public Pages build/deploy, run 36674703523](https://github.com/ykbballer91/riemann-hypothesis-research-log/actions/runs/36674703523), same release commit: both jobs PASS.
- [Latest workflow runs](https://github.com/ykbballer91/riemann-hypothesis-research-log/actions/workflows/pages.yml) record CI and deployment for the report commit and any later update. This report is a dated evidence summary, not a substitute for the live commit-specific Actions status.
- [Claim scope and 19-track discrepancies](phase3_track_discrepancies.md), [25-claim traceability](phase3_traceability.md), [independent review](phase3_independent_review.md), [critical citation review](phase3_citation_review.md), [safety scope](phase3_safety_report.md), and [local validation snapshot](phase3_validation_summary.json).

The initial post-publication safety check used a fresh **anonymous** Git mirror, with credential helpers and global Git configuration disabled. It scanned all **479 reachable blobs across eight commits**, including commit messages and author/committer identities, through the public-date update. It found no tested credentials, private keys, unintended sensitive paths or contact information. The report commit is subjected to the same scan and workflow before handoff. [The scanner](../tools/scan_publication.py) records categories/locations without printing matching secret values. Scanning is bounded by its patterns; it is not a guarantee against every possible secret format.

A complete post-publication rehash of the source research tree, using the same Git-metadata exclusion as the before snapshot, compared **60,812 regular files and four symlinks**. Added, deleted and modified files were all **0**; symlink targets, source HEAD and tracked/untracked Git status were unchanged. Private full inventories and the original Git history were never exported.

## Nonblocking publication notes

1. This is an unfinished research log with internal AI-assisted audits, not external peer review or formal verification of the whole mathematical program.
2. The critical citation review checked 22 source groups at stated depths. Some historical or ancillary URLs were not fetched; a bot-protected Weil record and source-version/resolver limitations are explicitly documented. No unresolved issue material to publication was identified.
3. Historical archive text remains predominantly Japanese. The English reader guide explains its context; dated private/draft statements in older audits remain historical checkpoints.
4. Original mathematical experiments were not all rerun for publication. The latest raw rank certificates, floating diagnostics, proof artifacts and reproduction limits retain separate labels.
5. Math rendering uses MathJax from a public CDN. The recorded browser checks are page/browser-specific, not an assertion about every artifact on every client.

**Final verdict: PUBLICATION COMPLETE**
