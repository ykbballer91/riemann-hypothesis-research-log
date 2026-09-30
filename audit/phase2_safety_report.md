# Phase 2 publication safety report

**STATUS: RIEMANN HYPOTHESIS OPEN**

Review date: 2026-09-30. **PASS — local payload and initial Git history.** Private remote creation may proceed after the independent local review also passes. Public visibility is not approved.

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

## Initial history check

The first two logical commits contain 409 reachable blobs. All were scanned with zero credential/path findings. The complete prospective payload contains 414 files and also has zero blocking findings. Author and committer identities use the chosen handle and GitHub noreply address only. Review-report additions will be rescanned before the private push; subsequent updates must pass the same checks.

## Publication boundary

Only a PRIVATE remote may be created after the initial history check passes. The Pages deployment job requires manual dispatch, public visibility, and a separate creator-approval variable. No public release date is assigned. Creator approval remains required before public visibility.
