# Phase 2 publication safety report

**STATUS: RIEMANN HYPOTHESIS OPEN**

Review date: 2026-09-30. **PASS — reviewed payload and reachable Git history.** The audited export was pushed to the designated PRIVATE repository. Public visibility is not approved.

The publication payload contains 364 selected source artifacts: the 359 Phase 1 candidates and five separately identified cyclicity records. Eleven required machine-reference rewrites are complete. The export also contains an external-reader guide, 18 track pages, build tools, licenses, and review records.

## Evidence and exclusions

- Source preservation: 61,698 regular files and four symlinks checked; zero changes; original source commit unchanged.
- Mathematical-content comparison: TeX spans in 215 text documents match their originals. The 47 original Python programs have unchanged ASTs; 96 JSON objects retain their original fields and values.
- Replay preparation verified all 364 exported source hashes. Historical research experiments were not rerun.
- The 61,334 unselected source files and four symlinks are excluded, together with local environments, third-party paper caches, original Git history, private inventories, and internal working audits.
- Public Git author and committer metadata use the explicitly chosen handle and the authenticated account's GitHub noreply address. No profile real name is substituted.

## Scan scope

The explicit payload is checked for machine-home paths, personal email addresses, credential formats, private keys, local/private URLs, and the requested sensitive keyword families. The same credential/path patterns are applied to every reachable Git blob after commits exist. Broad keyword hits are manually triaged: a literature-access cookie observation, placeholder variable names in the renderer, and the official Pages workflow's identity-token permission contain no credentials.

The build and link validator checks local targets and anchors, JSON, status labels, citation policy, deployment guards, and export hashes. It does not exhaustively crawl external URLs or prove mathematical assertions. Pattern scans are not an absolute guarantee of secret absence.

## Git payload and history checks

The three-commit pre-remote snapshot contained 414 tracked files and 414 reachable blobs, all scanned with zero blocking findings. The later rendering/citation snapshot contained the same 414 tracked files and 418 reachable blobs, again with zero credential/path findings. The tracked paths exactly match the explicit site/export allowlist plus the workflow and ignore file. No original source history or ignored working audit was included.

Author and committer identities use the creator-selected handle and GitHub noreply address only. Broad keyword hits in the safety reports themselves describe the scan rather than containing secrets. Review/report updates and notation-only fixes are subjected to the same pre-push payload/history scan. These are snapshot checks; no claim is made that future edits are automatically safe.

## Publication boundary

The remote was created PRIVATE after the independent local review and initial history check passed. GitHub builds succeeded and deployment was skipped. The Pages deployment job requires manual dispatch, public visibility, and a separate creator-approval variable. No public release date is assigned. Creator approval remains required before public visibility.
