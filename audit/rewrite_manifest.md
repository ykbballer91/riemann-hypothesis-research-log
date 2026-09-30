# Phase 2 export rewrite manifest

**STATUS: RIEMANN HYPOTHESIS OPEN**

本書は公開コピーの生成・書換えを記録する。sourceと旧Phase 1監査は変更しない。Git/remote/publication状態はphase2_publication_review.mdを参照。

## Scope

- 既選定359件＋Priority 1 cyclicityの5件、合計364原資料。
- 11件のREDACT_REQUIREDは機械パス・一時パス・内部リンクを公開用に書換えた。
- 数学、historical status、時系列、原検証hashを保存し、export hashを別記した。
- 全MarkdownにOPEN/historical snapshotを明記。外部引用URLと書誌識別子は保持し、第三者原著・cache・旧binary archiveは再配布しない。
- public creditは@ykbballer91。text/dataはCC BY 4.0、codeはMIT。旧authors-unassigned等の原記録は当時の履歴として保持する。
- Python 47ファイルはcomment header追加前後のASTが一致。数学的アルゴリズムは変更していない。Leanはcomment headerのみで今回build未実行。

## Header exceptions preserving machine-readable formats

JSON arrayの2結果とlean-toolchainはschemaを壊さず、そのprovenance/status/licenseはsource manifestに置く。JSON objectはadditiveな`_public_export`を追加する。原結果のsource hashは変更しないため、現在のsanitized script hashとは一致しない場合がある。再実行時のhashを旧認証へ遡及させない。

## Eleven reviewed rewrite targets

Here content semantics means mathematical statements, logical status, chronology and saved check outcomes. NO does not mean byte-identical: headers, additive JSON metadata, paths and links are changed and disclosed.

| Original relative source | Public copy | Reason | Content semantics changed? | Changes |
|---|---|---|---|---|
| `release/research_handoff_2026-09-29.txt` | `archive/reports/release/research_handoff_2026-09-29.txt` | Remove the local working-directory path; preserve the dated handoff and claims. | **NO** | source_absolute_prefix_removed: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/structural_heuristics.md` | `archive/reports/research/structural_heuristics.md` | Remove the private input-document location; preserve its stated non-evidentiary role. | **NO** | internal_link_rewritten: 23, machine_path_redacted: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/finite_negative_index_gate.md` | `archive/reports/research/finite_negative_index_gate.md` | Replace the local third-party PDF link with non-clickable provenance; retain external citations. | **NO** | nonexport_link_to_provenance_note: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/scale_flow/notes/spectral_growth.md` | `archive/reports/research/scale_flow/notes/spectral_growth.md` | Map the absolute internal program-comparison link to the selected public copy. | **NO** | internal_link_rewritten: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/one_prime/notes/topology_constructions.md` | `archive/reports/research/one_prime/notes/topology_constructions.md` | Map the absolute arithmetic-space reference to the selected public copy. | **NO** | internal_link_rewritten: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/dyadic/notes/dyadic_relations.md` | `archive/reports/research/dyadic/notes/dyadic_relations.md` | Map absolute cross-track source links to their curated public destinations. | **NO** | internal_link_rewritten: 3, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/strategy_reset/notes/correlations_and_short_intervals.md` | `archive/reports/research/strategy_reset/notes/correlations_and_short_intervals.md` | Map the absolute Gaussian-note link to the curated public copy. | **NO** | internal_link_rewritten: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `research/notes/phase3_finite_field_audit.md` | `archive/reports/research/notes/phase3_finite_field_audit.md` | Remove the temporary PDF-download path while retaining bibliographic URL and source hash. | **NO** | machine_path_redacted: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `proofs/audits/global-dependency.md` | `archive/audits/proofs/audits/global-dependency.md` | Remove the machine-specific Lean toolchain path from a historical command. | **NO** | source_absolute_prefix_removed: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `proofs/audits/window-half-independent.md` | `archive/audits/proofs/audits/window-half-independent.md` | Remove local interpreter, script-root and temporary-workspace paths from historical replay details. | **NO** | internal_link_rewritten: 4, source_absolute_prefix_removed: 2, machine_path_redacted: 1, provenance_header_added: 1, tex_spans_preserved: 1 |
| `experiments/README.md` | `archive/reports/experiments/README.md` | Remove the machine-specific Python interpreter location; retain the environment qualification. | **NO** | machine_path_redacted: 1, provenance_header_added: 1, tex_spans_preserved: 1 |

## Links and nonexported provenance

全364件のmappingを先に固定し、相対・絶対internal Markdown linksを公開配置へ写した。収録しない原資料へのリンクはクリック不可のprovenance注記へ置換した。本文中のhistorical source-relative識別子は、追加の参照案内とmanifestで公開パスへ対応させる。原著引用の外部URLは変更しない。

Markdownのlocal file targetsは全件存在確認済み。fragmentの歴史的section名は保持し、過去資料のsource-line数と公開コピーのline数が等しいとは主張しない。

## Reproducibility limits

scriptsは原本の相対配置を前提とするため、公開treeで直接走らせると保存済み結果を上書きしたり参照を失ったりする。`artifacts/replay.py`は独立workspaceへ元相対配置を復元する補助であり、依存ライブラリ・第三者原著・認証の正しさを供給しない。今回historical experiment、Arb certificate、Lean buildは再実行していない。

以下は特に制限を持つ：

- `research/common_parent/experiments/rayleigh_probe.py`: USES_INCLUDED_HISTORICAL_INTERVAL_MATRIX_FOR_DIAGNOSTIC_COMPARISON
- `research/rate_history/experiments/validate_outputs.py`: HISTORICAL_REPOSITORY_AND_PRESERVATION_VALIDATOR_NOT_PORTABLE
- `research/hierarchical_selection/experiments/validate_outputs.py`: HISTORICAL_REPOSITORY_AND_PRESERVATION_VALIDATOR_NOT_PORTABLE
- `experiments/scripts/desogus_targeted_checks.py`: REQUIRES_EXCLUDED_THIRD_PARTY_TEX_SOURCE
- `experiments/scripts/groskin_compare_assemblies.py`: REQUIRES_EXCLUDED_THIRD_PARTY_ANCILLARY_CODE
- `experiments/scripts/window_four_fifths_certificate.py`: HISTORICAL_RUN_INTERRUPTED_NO_COMPLETED_CERTIFICATE_CLAIM
- `literature/build_ledger.py`: HISTORICAL_METADATA_GENERATOR_NOT_A_MATHEMATICAL_CHECK

実験のcompleted/diagnostic/interval-certified/interrupted区分は各原記録を優先する。`window_four_fifths_certificate.py`の保存は完了認証を意味しない。旧repository保存validatorは公開版の検証器として実行しない。

## Verification

- source SHA-256をselection/current Priority 1読み取り値と照合。Markdown/テキストの全TeX spanは原文と一致を検査し、数式やcode spanをリンクとして書き換えない。
- export SHA-256は書換え後の実bytesから算出。
- JSONは再parse、PythonはAST同一性、Markdownは公開local target存在、機械絶対パス不在を確認。
- phase2_export_summary.jsonはファイル変換の検証であり数学証明の新しいPASSではない。

**STATUS: RIEMANN HYPOTHESIS OPEN**
