# リーマン予想が解けるか。

[日本語サイト](https://ykbballer91.github.io/riemann-hypothesis-research-log/ja/) · [English](README.md)

**STATUS: RIEMANN HYPOTHESIS OPEN.**

**[@ykbballer91](https://github.com/ykbballer91)** が編集するAI支援研究ログです。試み、補助結果、反例、未解決の依存関係を記録しており、リーマン予想を証明したものではありません。失敗した方針も証拠として保存します。

## 読み始める

- [読み方](docs/ja/index.md)
- [現在地](docs/ja/current-state.md)
- [履歴](docs/ja/timeline.md)
- [ロードマップ](docs/ja/roadmap.md)
- [出典](docs/ja/source-map.md)・[参考文献](docs/ja/references.md)
- [方法と証拠](docs/ja/methodology.md)・[状態ラベル](docs/ja/status-legend.md)
- [再現手順](docs/ja/reproducibility.md)・[サイトのビルド](docs/ja/site-building.md)

## 最新の研究更新 — 2026-10-05

[共同移送の再検証](docs/ja/updates/2026-10-05-joint-transfer.md)では、同じ列でESと強L²捕捉が成立するなら、実零点構造により指定の速度なしで複素比較へ移せる条件付き接続を採用しました。ES・実際の捕捉・CMP・RHは未証明です。ESを使わない旧CMP-Rも保持し、新しく解決した実際の漸近義務は0件です。

## 保存した更新 — 2026-10-01

[CMP / ES更新](docs/ja/updates/2026-10-01-cmp-es.md)では、現在の直接ルートを、有限Weil最低状態と既知のプロレート近似の複素領域での比較、および同じ共終列上での最終的な単純・偶性へ絞りました。どちらも未証明です。通常のL²収束や一点の有限認証では代用できません。

委譲件数、CASE D、CMP-Rの十分速度条件は、更新本文の技術的詳細に保存しています。12個のRH障害を解いたという意味でも、証明目前という意味でもありません。

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

## 以前の補助結果と境界

各固定有限微分空間での制限付き選択、RHを使わない偶L²巡回性、固定有限偶フーリエ空間の正確な生成を記録しています。これらは変化する最低状態の一様近似・Weil形式制御を与えません。固定次数、増大次数、全体の最低状態、ES、複素比較の範囲は[現在地](docs/ja/current-state.md)で分離しています。

日英化するのは編集・案内層です。原文資料は元の言語を保ち、過去の状態を最新の結論へ黙って変更しません。`PROVED` は指定された補助主張の範囲に限ります。内部AI監査、数値検査、Leanの一部宣言は外部査読や全研究の形式検証ではありません。

## 公開・引用・ライセンス

版 **0.1.0** はPhase 3検査と最終CI後、**2026-09-30**に公開しました。[公開報告](audit/publication_report.md)と[公開前レビュー](audit/phase3_final_content_review.md)を保存しています。Pagesの明示的配信条件も維持します。

引用には [CITATION.cff](CITATION.cff) を使ってください。著者表示は `@ykbballer91`。独自の本文・図は [CC BY 4.0](LICENSE-TEXT)、コード・実験スクリプトは [MIT](LICENSE-CODE) です。第三者の著作物には元の権利が残ります。構造化記録の独自説明文は本文ライセンス、実行コード・形式証明はコードライセンスです。過去の帰属欄は当時の記録で、現在の公開方針を上書きしません。[ライセンス](docs/ja/licensing.md)を参照してください。
