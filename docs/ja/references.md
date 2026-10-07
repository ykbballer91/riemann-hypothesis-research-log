# 参考文献と確認範囲

**STATUS: RIEMANN HYPOTHESIS OPEN**

本研究記録の公開者は **@ykbballer91**。引用した数学的成果の著者への帰属はそのまま保持します。引用は指定の前提下の特定主張の根拠であり、論文中の全主張への承認ではありません。

[機械可読な参照記録](../../data/references.json)は、旧6台帳の108件と巡回性ノートの3件の使用記録を保存します。同じ論文も定理・条件付き判定・類比で依存関係が違えば複数回現れます。後続の本文引用には参照元付き外部リンク索引もありますが、検証済み定理一覧や網羅的文献表ではありません。

## 確認ラベルの読み方

- 出版状態は雑誌・プレプリント等の区別で、証明を独立検証したという意味ではない。
- 一次本文確認は指定の主張・箇所を読んだこと。論文全補題の再構成ではない。
- 範囲を限定した独立検査は別AI担当の導出・監査・計算。外部査読や無関係な主張の認証ではない。
- 条件付き・RH依存は使用する命題に付ける。適用時も前提を残す。
- `verification_as_recorded` の `NO`、`PARTIAL`、真偽値、範囲注記は型と文言を保持する。欠落は欠落・nullのままで、非空文字列を真偽値に変えない。

過去の証明主張の限定監査や類比は履歴であり、採用済みRH入力ではありません。公開編集で文献を新たに「独立検証済み」へ昇格させていません。論文タイトルと著者名は原表記を保持します。

## 主な数学的参照先

| 分野 | 一次資料・公式資料 | 使用箇所と限界 |
|---|---|---|
| Weil判定と明示公式 | [Weil, 1952](https://cds.cern.ch/record/471308); [Connes, trace formula](https://arxiv.org/pdf/math/9811068v1) | 正値性判定と算術的トレースの枠組み。大域正値性はなお必要。 |
| 算術商とFrobenius比較 | [Connes–Consani–Marcolli, math/0703392v1](https://arxiv.org/pdf/math/0703392v1); [Deligne, Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf) | 対象領域・トレース・重複度。有限体の純性を自動的に数体へ移さない。 |
| 偏極と高さ | [Gillet–Soulé](https://www.numdam.org/item/10.1007/BF02699132.pdf); [Milne, Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf) | 正の構造は定理が指定する幾何学的空間でのみ使用。全ゼータ零点空間との同一性は導かない。 |
| 熱変形 | [Rodgers–Tao, 1801.05914v5](https://arxiv.org/pdf/1801.05914v5) | de Bruijn–Newman定数の非負性。時刻0で不足する上界は証明しない。 |
| 局所Weil形式と算術radical | [Connes–Consani, Spectral triples and ζ-cycles](https://ems.press/journals/lem/articles/11033001) | 既知の算術radicalの帰属を明示。それだけで一意の有限最低状態を選ばない。 |
| 実零点定理とプロレート近似 | [Connes–van Suijlekom, 2511.23257v1](https://arxiv.org/html/2511.23257v1); [Connes–Consani–Moscovici, 2511.22755v1](https://arxiv.org/html/2511.22755v1) | 条件付き最低状態の前提、既知の近似収束、未証明の規格化比較を分離する。 |
| CORE-Sの有限構造入力 | [Connes–Consani–Moscovici, 2511.22755v1, §5.1–5.2, Lemmas 5.1–5.2](https://arxiv.org/html/2511.22755v1#S5) | 行列の差商・交換関係は既知入力。厳密な偶奇順序から単純性への帰結と、未証明の共終的順序を分離する。 |
| Sonin空間 | [Burnol, math/0203120v6](https://arxiv.org/pdf/math/0203120v6) | 指定空間の完備性・極小性。現在の射影Weilエネルギーをこの空間列で置換しない。 |
| モーメント稠密性 | [de Jeu, math/0111019v2](https://arxiv.org/pdf/math/0111019v2), 定理2.3、p.5 | 定理2.3、p.5のCarleman条件から有限正測度のL²多項式稠密性を使う。定理5.1のStieltjes条件は別。 |
| Xiの指数減衰 | [DLMF 5.11.9](https://dlmf.nist.gov/5.11#E9), [25.9.3](https://dlmf.nist.gov/25.9#E3), [25.4.4](https://dlmf.nist.gov/25.4#E4) | 標準Gamma減衰、無条件ゼータ評価、完備化規約。RHは不要。 |
| 補足モーメント | [Simonič–Starichkova, 2105.06821v3](https://arxiv.org/html/2105.06821v3) | 補足モーメント漸近に二乗平均誤差評価を使う。巡回性証明はこの精密化に依存しない。 |

## 有限空間の補間と条件数

[Priority 2](tracks/19-finite-even-head-spanning.md)は次の既知道具を使います。旧台帳の確認状態を変更しません。

| 出典 | 確認箇所と範囲 |
|---|---|
| Walter Gautschi, *Norm Estimates for Inverses of Vandermonde Matrices*, Numerische Mathematik 23 (1975), 337–347. [著者公開版](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf). | §3 p.339 (3.3)はLagrange基底による逆行列、§4 p.340 (4.1)はそのノルム評価。原典は節点を列に置くため、本記録の転置規約では無限大ノルムの式が1ノルムになる。 |
| Pablo D. Brubeck, Yuji Nakatsukasa and Lloyd N. Trefethen, *Vandermonde with Arnoldi*, SIAM Review 63(2) (2021), 405–415. [著者公開版](https://people.maths.ox.ac.uk/trefethen/vandermonde_arnoldi.pdf), [DOI:10.1137/19M130100X](https://doi.org/10.1137/19M130100X). | §4 p.409 (4.2)–(4.5)はQRを通じた単項式と離散直交座標の対応。張る多項式空間は保つが、物理ノルムや支持制限の摂動は自動的に制御しない。 |
| NIST Digital Library of Mathematical Functions, [§18.2.3](https://dlmf.nist.gov/18.2#E3), [§18.2.5](https://dlmf.nist.gov/18.2#E5), [§18.2.12–13](https://dlmf.nist.gov/18.2#E12). | 離散直交性、そのノルム、Christoffel–Darboux核。射影先Gramの正規化と全域・支持制限後の物理Gramを同一視しない。 |
| Albert Cohen, Mark A. Davenport and Dany Leviatan, *On the stability and accuracy of least squares approximations*, [arXiv:1111.4422v3](https://arxiv.org/pdf/1111.4422v3), 2018年6月15日改訂、初稿2011年。 | 定理1 p.3 (1.2)は指定測度からの独立標本に関する確率的Gram評価。本記録の決定論的Xi重み付き格子の認証ではない。論文中の別の標本化結果を一律に否定したものではない。 |

[条件数ノート](../../archive/reports/research/full_ground_capture/priority2/notes/conditioning_literature.md)に行列規約、係数・有限空間・物理ノルムの区別を記録しています。指定箇所の読解であり、引用論文の全証明の新たな検証ではありません。

## 命題単位の原記録

- [初期定理・計算台帳](../../archive/literature/literature/sources.json)
- [Weil評価の出典](../../archive/literature/literature/notes/weil-sources.json)
- [構造的類比](../../archive/literature/research/structural_sources.json)
- [生成作用素・境界](../../archive/literature/research/phase2_sources.json)
- [Frobenius比較](../../archive/literature/research/phase3_sources.json)
- [偏極・交点](../../archive/literature/research/phase4/sources.json)

後続は各主報告・補足に定理番号、前提、版、不適用の理由を記録しています。[局所大域の定理構成](../../archive/reports/research/local_global_theorem_stack.md)、[Sonin監査](../../archive/reports/research/sonine_filtration_audit.md)、[巡回性の出典](../../archive/reports/research/full_ground_capture/notes/moment_problem_sources.md)を参照してください。

## 権利と取得情報

掲載するのは本プロジェクトの説明と書誌情報です。第三者全文・PDF/HTML/TeXキャッシュ・補助ソフトは除外しています。外部リンク先の内容と権利はこの公開の管理外です。元の記録にある取得日と版は保持し、記録のない閲覧日、査読結果、著者名は補いません。
