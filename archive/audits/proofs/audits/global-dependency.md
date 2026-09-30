**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/global-dependency.md` · Original SHA-256: `b4c98f955fd62b8ff45144ccad46cb5e16494d5828d153db2c57b8192b3c20ca`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Audit B: 補助ノートの global dependency audit

監査日: 2026-09-29。担当: LOGIC AUDITOR（LITERATURE AUDITOR から役割変更）。初回読取から2026-09-29 05:48 UTC頃までの作業中スナップショットを対象とする。

**範囲限定の判定: 補助補題の依存・量化について重大な論理ギャップを検出せず。初回に指摘した文献台帳の条件表示は修正確認済み（第9節）。Lean の抽象6宣言も独立再実行済み。RH は OPEN のまま。**

これは完成した RH 証明候補への Audit B ではない。固定支持の Weil 形式、可算稠密族、全称有限 Gram 正値性との同値化を記述した補助ノートへの監査である。独立した査読、Lean による全解析の形式検証、引用論文すべての再証明を意味しない。

## 読取対象

- `theorem_graph/graph.md`
- `theorem_graph/nodes.yaml`
- `theorem_graph/assumptions.md`
- `proofs/lemmas/finite_to_infinite.md`
- `proofs/lemmas/weil_conventions.md`
- `literature/notes/frontier-overview.md`
- 追加照合: 作成後の `literature/ledger.md`、versioned arXiv 本文・PDF、研究者公開出版版。

他の担当者が編集する上記ファイルは変更していない。本監査で保存したのはこのファイルだけである。

## 1. 検出事項

### B-01: 台帳の RH 依存欄を主張ごとに分ける必要がある

確認時の `literature/ledger.md` の Zhu2026v2 は、Exact theorem に Theorem 1.3 も含める一方、Depends on RH? が一律 NO だった。しかし [2608.24827v2 Theorem 1.3](https://arxiv.org/html/2608.24827v2) は RH を仮定した下端の上界である。固定窓の Theorem 1.2／Corollary 6.3 の主張と区分が必要。

同様に Suzuki2026v3 の列挙に §7 を含める場合は、構成定理の無条件性、§7 の RH 下の動機づけ、Corollary 1.6 の未証明の極限仮定を区別する必要がある。[2606.09096v3](https://arxiv.org/html/2606.09096v3)

影響: 文献の依存情報としては実質的な誤分類になる。現在の T020–T050 はどちらの条件付き結果にも依存しておらず、補助証明に RH が混入したことは検出していない。root へ修正依頼済み。これは「論文全体が RH を仮定する／しない」の二値分類では解決しない。

### B-02: Suzuki2023 の HTML 日付不整合

[2206.03682v4 HTML](https://arxiv.org/html/2206.03682v4) は version header が2023-05-30で、本文 Date が2026-08-24と表示された。別途取得した [同じ v4 のPDF](https://arxiv.org/pdf/2206.03682v4) は、表紙 header が2023-05-30、本文 Date が2023-05-31である。PDF p.10 §3.2 (3.3)–(3.5) でも必要な \(C_c^\infty\) 版 Weil criterion を確認した。

影響: 数学的な入力の取り違えは検出しない。再現可能な引用として versioned PDF を優先し、arXiv提出日と本文日付を分けて記すのが妥当。この不整合は独立担当 DESTROYER も確認し、PDFによる解消を共有した。

### B-03: 形式化の証拠は今回未監査

読取時点では `formal/lean/README.md` が未作成だった。`graph.md` はそこに実際の compile／axiom 出力を記録する方針で、T020–T050 の `formalized` は false。そのため形式化範囲の過大主張は検出しない。

後で README と実ログが完成しても、この監査結果だけをもって解析補題全体が形式化されたとは扱えない。Lean が検証した一般含意と、ζ・Weil criterion・稠密族の外部入力を分離して報告すること。

## 2. グラフの機械点検

`nodes.yaml` は JSON として解析可能だった。全13ノードについて深さ優先走査を行い、未知の依存先0、循環0を確認した。

|PROVEDノード|推移依存|OPENな前件を依存として密輸しているか|
|---|---|---|
|T020|T001|いいえ|
|T030|T001, T020|いいえ|
|T040|なし（明記した初等解析による内部証明）|いいえ|
|T050|T001, T020, T030, T040|いいえ|

T100 と T110 は `status: EQUIVALENT-TO-RH`、`resolution: OPEN`。T000 も OPEN。T050 の PROVED は **全称正値性を前件とした含意／同値化**の証明であり、前件の成立ではない。この区別は F5 本文・graph.md の注記と一致する。

Mermaid の矢印は通常の図だけでは AND 依存を表さないが、本文は「依存条件がすべてそろう」ことを明記している。T050 から T100 への一本の矢印だけを reachability proof と読んではならない。T110 の依存リストが空なのも「証明不要」を意味せず、未解決の独立義務として保持されている。

改善余地: T100/T110 に `equivalence_evidence: [T050,T010]` のような**証明依存とは別**の provenance を付すと、同値属性の根拠を機械的にも追える。現状は F5 の明記で数学的に追跡可能であり、必須の証明修正ではない。

## 3. 外部の既知入力

### 零点の帯・対称性・計数

T001 は RH を使わない標準ゼータ理論として受け入れられている。とくに必要なのは全非自明零点の多重度込み計数 \(N_*(T)=O(T\log(T+2))\) であり、臨界線上だけの計数ではない。

[Hasanalizade–Shen–Wong の出版版](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf) §2（PDF p.4）は \(0<\beta<1, |\gamma|\le T\) の \(N_{\mathbb Q}(T)\) を定義し、通常の正高度計数との対応を与える。必要な粗い上界はこの無条件零点計数の帰結で、同論文の鋭い数値定数を移植する必要はない。

T001 は新しく再証明した成果ではない。台帳の RVM2022 に書誌と使用範囲が記録されたことを再確認した。

### Weil criterion と明示公式

Weil criterion の「同値定理を既知とする」ことと「非負性が成立すると仮定する」ことは区別されている。[Suzuki v4 PDF §3.2](https://arxiv.org/pdf/2206.03682v4) は compactly supported smooth test functions に対する基準を明記する。1952原典が同じ現代的テスト空間を逐語的に述べると主張していない点も適切。

Suzuki2025 の [出版社PDF Theorem 1.1](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD33EBD117A6B448053450DD8D62ADB6/S0008414X25101739a.pdf/on-the-hilbert-space-derived-from-the-weil-distribution.pdf) が RH を仮定する Hilbert 空間同型であることを再確認した。本プロジェクトはそれを無条件な正値性の根拠にしていない。

明示公式自体も KNOWN。規約の再計算は明示公式全体の新証明ではない。

## 4. 規約・収束・連続性の依存点検

`weil_conventions.md` について、以下を式から再確認した。

- \(z_\rho=(\rho-1/2)/i\) の実部は零点高度 \(\gamma\)。\(\rho\mapsto1-\bar\rho\) は \(z\mapsto\bar z\) に対応し、単純零点仮説は使わない。
- \(F_{\widetilde g}(z)=\overline{F_g(\bar z)}\)。複素 \(z\) に対する積を無条件に \(|F_g(z)|^2\) と置いていない。
- \(a_f(t)=t^{-1/2}f(\log t)\)、\(a^\sharp(t)=t^{-1}\overline{a(t^{-1})}\) は記載された Mellin 変換と畳み込みに整合する。
- Hermitian 性の再添字付けは F2 の絶対収束の後で行われる。F2 の絶対値評価自体は Hermitian 性に依存せず、相互参照は循環証明になっていない。
- 算術側の pole term と prime-power weight \(\Lambda(n)/\sqrt n\) が保持されている。原点の中括弧は \(xh(0)+O(x^2)\) であり、最後の積分の収束説明は成立する。

`finite_to_infinite.md` の F1–F3 は次の依存順で成立する。

1. 固定 support の滑らかな関数の全導関数は端点で0となるため、部分積分の境界項が消える。
2. 固定帯 \(|\Im z|\le1/2\) 上の Fourier decay と零点計数により、\(m=1\) でも積の零点和の絶対収束が得られる。
3. dyadic tail は \(\sum(k+1)2^{-k}\) に帰着する。RH、tail の正符号、未知の零点の実数性を仮定していない。
4. sesquilinear estimate から同一 support 内の \(p_1\) 連続性が得られる。support を無限に動かす一様評価、作用素ノルム収束、trace-norm 収束は結論に含まれない。

この範囲の PROVED は数学的に妥当と判断する。より深い作用素閉包や大域算術の新結果は得られていない。

## 5. 稠密性と全称量化

F4 は \(L^2\) 稠密性だけを使わず、各固定 \(\mathcal D_L\) の全導関数半ノルムで近似する。shrink により境界の余裕を作り、mollify し、有理中心・有理幅の bump の有限和で Riemann 和近似する手順は妥当。

有理係数である必要はない。可算なのは bump のリストであり、その複素線形 span の稠密性を述べている。線形独立性がなくても Gram 行列の PSD と有限 span 上の非負性は対応する。

F5 の添字 \(M_{jk}=Q(\phi_k,\phi_j)\) は第1変数線形の convention と整合し、\(Q(\sum c_j\phi_j)=c^*Mc\) となる。任意の近似関数が有限個の列挙要素だけを含むため、その最大 index を取れる。すべての \(L,N\) の PSD という前件の量化が保存され、任意の compact support を整数 \(L\) が覆う最後の段階にも欠落はない。

F6 の行列誤差上界は Hermitian 性と単位 coefficient vector 上の Cauchy–Schwarz から従う。ただしこれは symbolic bound で、具体的な certified tail constant を計算したという成果ではない。全零点の網羅性を保証した cutoff と、既知の臨界線上零点だけの和を区別する注意も必要十分に明示されている。

従って次の二命題は異なる状態を持つ。

\[
\bigl[\forall L,N\ M_{L,N}\succeq0\bigr]\Longleftrightarrow RH
\quad\text{（既知入力からの証明済み同値化）}
\]

\[
\forall L,N\ M_{L,N}\succeq0
\quad\text{（OPEN、RH同値の算術的前件）}.
\]

## 6. Frontier ノートと新規性

`frontier-overview.md` の2026年文献は「原稿の主張を確認」「独立検証未済」「主依存に不採用」と扱われており、RH 証明への昇格はない。Lamzouri の [Theorem 1.1 と Remark 3.4](https://arxiv.org/html/2609.02882v1) は記載された割合と限定された最適化定数に対応する。核クラスの最適性を全手法の不可能性としていない点も適切。

Wang の [Theorem 1.1](https://arxiv.org/html/2609.07918v1) は固定 \(0<\theta<1\)、長さ \(T^\theta\) の短区間に関する liminf 比率である。現ノートの広い説明は過大ではないが、今後具体的に使う場合は \(\theta\) 条件と、下界が非正になる範囲も保持すること。

他の行はルート選択の短い文献案内であり、独立定理監査完了とは表示されていない。今回すべての案内行の原典を再監査したわけではない。例えば Li 原典の定理番号などは自ら未確認と表示されている。

T020–T050 は `novelty: NO_CLAIM`。固定supportの連続性・稠密性・Gram同値化は既知の解析機構を明記した補助成果であり、RHへの距離が縮んだことを意味しない。graph.md の「未解決核心1クラス」も、同値な命題を1つのclassにまとめた論理上の数え方だと明記されている。

## 7. この監査を通じても残るもの

- T110 の全称正値性は未証明。
- 外部の古典的入力をゼロから再証明していない。
- 最新固定窓の計算証明書を独立再実行していない。
- 初回監査では Lean の compileログ・axiom出力は未監査だった。後続の抽象6宣言の再監査は第9節を参照。全解析の形式化は引き続き未実施。
- 既知の form-core route とは別の新しい正値性機構を示していない。

文献台帳の B-01/B-02 を修正しても、この数学的な未解決状態は変わらない。補助ノートの整合性を確認したことを RH 証明の監査通過と呼ぶことはできない。

## 8. 監査スナップショット SHA-256

以下は初回グラフ点検時の fingerprint。作業中の後続編集があり得るため、将来のファイルへの無期限な承認を意味しない。

```text
117473393df24b515c751ddd7c8eb755a794e1c4c8dfce328eec67c77f7deec7  theorem_graph/graph.md
022fb3403175de471f1214463d19c841cdbd6ec158f3c12bfbdbfb4f5d466f00  theorem_graph/nodes.yaml
e4c67ff58f6a5003ec115f7d601c0fcc54709f709dcbeaed6cf42264b746bb36  theorem_graph/assumptions.md
d0bdfa65e79a65c5a7ddfd9747ed53b15805c45e4b63c24692c7881516544006  proofs/lemmas/finite_to_infinite.md
2851af5325b8c3a0a32f71ac6f85bf72f5d24d12849288de3985cac6f1aa86b5  proofs/lemmas/weil_conventions.md
7eb9f203cbca2ba2fd937d3d38a0ad3f0b9777ddd8350e4cfcfdb0fabe0a0d8c  literature/notes/frontier-overview.md
```

## 9. 修正確認と Lean の独立再監査（2026-09-29）

この追記は B-01–B-03 の修正、`RhAudit.lean` の型・実装・axiom出力を対象とする。初回の13ノードから作業が進んだため、新しい17ノードのグラフ構造も点検した。ただし追加された kernel 最適化ノート T070 の解析証明や F006 は本追記の数学的監査対象に追加していない。

### B-01: 修正確認済み

`literature/build_ledger.py` と生成された `literature/sources.json`、`literature/ledger.md` を照合した。台帳は26件である。

- Zhu2026v2 の無条件欄から Theorem 1.3 が除かれ、別項目 Zhu2026Conditional が `depends_on_RH: YES`、依存不採用となった。元の固定窓の計算証明主張は独立再現未済のままである。
- Suzuki2026v3 の無条件の構成定理と §7 が分離され、Suzuki2026Heuristic は `depends_on_RH: YES`、依存不採用となった。
- Corollary 1.6 は「conditional limit」と表示され、上半平面 compact 上の局所一様収束という未証明条件と v3 の極限関数を保持する。「RH を前提にした定理ではない」ことを「前件なしに RH を結論できる」と読み替えていない。

従って初回の条件表示の混同は修正された。これらの項目を現行の補助証明の新たな無条件依存に採用した形跡はない。

### B-02: 修正確認済み

`weil_conventions.md` の S2023、台帳の Suzuki2023、生成書誌は [arXiv:2206.03682v4 の PDF](https://arxiv.org/pdf/2206.03682v4) を指す。PDF 本文日付 May 31, 2023 と arXiv header May 30, 2023 が区別され、HTML に表示された2026年の日付を使わない旨が記録された。初回に照合した §3.2 (3.3)–(3.5) の数学的入力は変わらない。

### B-03: 抽象6宣言の独立再実行済み

`formal/lean/README.md`、`RhAudit.lean`、`lean-toolchain`、`lakefile.toml`、`lake-manifest.json` と `verification/{build,axioms}.txt` を読んだ。LOGIC AUDITOR が `formal/lean` を作業ディレクトリとして次を再実行し、終了コード0を確認した。

```sh
ELAN_HOME='[source repository]/formal/lean/.elan' .elan/bin/lake env lean RhAudit.lean
```

別途の `lake env lean --version` も終了コード0で、`Lean (version 4.19.0, x86_64-apple-darwin22.6.0, commit 6caaee842e94, Release)` を返した。manifest の Mathlib は `c44e0c8ee63ca166450922a373c7409c5d26b00b`、inputRev は `v4.19.0` で README と一致する。今回は保存済み環境でのソース再実行であり、依存物のクリーン再取得・全再ビルドを独立実施したとは表示しない。厳密に同じ依存で再現するときは保存した manifest を保持する。

6宣言の出力は保存済み `verification/axioms.txt` と一致し、いずれも次の3公理だけを報告した。

```text
[propext, Classical.choice, Quot.sound]
```

`sorryAx`、独自の RH 公理の依存は出力されなかった。ソースにも `sorry`、`admit`、独自 `axiom` 宣言は存在しない。これは下記の**仮定付きの型**を Lean が検証したという意味である。型の引数に明示された解析的前件を証明したことにはならない。

|宣言|Lean が実際に確認した範囲|残る前件・範囲外|
|---|---|---|
|`nonneg_of_pointwise_limit`|任意の実数値関数列が各点で収束し、すべての `n,x` で非負なら極限が各点非負|収束 `hlim` と全称非負性 `hpos` は引数。有限個の検査で代用できない|
|`nonneg_of_vanishing_lower_error`|各点収束に加え、各点で0へ収束する誤差と `-err n x ≤ qN n x` から非負性を導く|誤差消滅と全称下界は引数。実際の零点 cutoff や明示定数は実装していない|
|`nonneg_on_dense`|指定した位相で連続な実数値写像の稠密集合上の非負性を全域へ延長|`Continuous q`、`Dense s`、集合上の非負性は引数。具体的 bump 族の稠密性は未形式化|
|`coordinate_restrictions_nonneg`|`x²+4xy+y²` の各座標軸への制限が非負|全2次元空間の非負性を主張していない|
|`larger_block_negative`|同じ形式の `(1,-1)` での値が厳密に `-2`|一般論の反例であり、ζ の反例ではない|
|`quartet_coefficient`|有理数の式 `(-32)(1/4)²(1-(1/4)²)=-15/8`|Fourier 変換・積分による witness の構成は未形式化|

最初の2宣言の各点収束にはベクトル全体にわたる一様収束は不要であり、コメントと実装は一致する。一方で `qN` が Weil 形式から得られること自体は定義していない。一般含意として正しいことと、RH 同値の前件を無条件に供給することを混同してはならない。

README の「RH の形式検証ではない」という限定、および T020–T050 の `formalized: false` は適切である。T060 の `formalized: true` はこの6宣言だけを指し、数学的新規性も `NO_CLAIM` となっている。

### 後続グラフの構造と最終範囲

17ノードを再解析し、未知の依存先0、循環0を確認した。T060 は RH に至る未解決前件を満たす依存辺として追加されていない。T000・T100・T110 はすべて resolution が OPEN で、全称 Gram PSD を証明済みへ昇格していない。

**Audit B の判定対象は、引き続き補助ノートの依存整合性と限定された形式検証である。完成した RH 証明候補の監査通過ではない。** B-01/B-02 は修正確認済み、B-03 は抽象6宣言について検証証拠を確認した。未形式化の解析、全称正値性、最新文献の計算証明書の独立再現はこの追記で完了していない。

再監査時の SHA-256:

```text
c2cad16df8451fe38fe8c969d6754070433efb6d9d00610b1b8b1785bce94351  formal/lean/RhAudit.lean
ca1749cbd0897889de62b52ffeca3913bc9cae2b860725960a78e15613ae1c58  formal/lean/README.md
48480f02afd78049a6a0a106c42c125f0c8188324f195b7d24c71968b99013d1  formal/lean/lake-manifest.json
ffc47c870e780b55bfc050c1e719c4a707df43dda3103bb552c347402528acbd  formal/lean/verification/build.txt
dfcfa3c1f7ca563da41918ceb07313fd305ea695f0edfb9b7b0b9081951a2a11  formal/lean/verification/axioms.txt
21a806f290cc2808e22dba784e905650c78523763a60b86907aa62dbebb71728  proofs/lemmas/weil_conventions.md
046cee3c14ec0019c231e80713207c4a527084052f42509792a18dc3c138d292  literature/build_ledger.py
18f22303d8411a14e15c6afc1e275c050ded7c1893c5c7f7731a94a2662e4af3  literature/sources.json
12897042239dd2c106a485ca150c64df8699014c63cf8ba8465d51fb2891f5eb  theorem_graph/nodes.yaml
```


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`formal/lean/README.md`](../../../../artifacts/formal/lean/README.md)
- [`formal/lean/RhAudit.lean`](../../../../artifacts/formal/lean/RhAudit.lean)
- [`formal/lean/lake-manifest.json`](../../../../artifacts/formal/lean/lake-manifest.json)
- [`formal/lean/verification/axioms.txt`](../../../../artifacts/formal/lean/verification/axioms.txt)
- [`formal/lean/verification/build.txt`](../../../../artifacts/formal/lean/verification/build.txt)
- [`literature/build_ledger.py`](../../../literature/literature/build_ledger.py)
- [`literature/ledger.md`](../../../literature/literature/ledger.md)
- [`literature/notes/frontier-overview.md`](../../../literature/literature/notes/frontier-overview.md)
- [`literature/sources.json`](../../../literature/literature/sources.json)
- [`proofs/lemmas/finite_to_infinite.md`](../../../reports/proofs/lemmas/finite_to_infinite.md)
- [`proofs/lemmas/weil_conventions.md`](../../../reports/proofs/lemmas/weil_conventions.md)
- [`theorem_graph/assumptions.md`](../../../reports/theorem_graph/assumptions.md)
- [`theorem_graph/graph.md`](../../../reports/theorem_graph/graph.md)
- [`theorem_graph/nodes.yaml`](../../../reports/theorem_graph/nodes.yaml)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `formal/lean` — SOURCE REFERENCE NOT INCLUDED
- `formal/lean/.elan` — SOURCE REFERENCE NOT INCLUDED
