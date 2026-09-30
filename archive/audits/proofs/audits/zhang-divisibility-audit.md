**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/zhang-divisibility-audit.md` · Original SHA-256: `9816c4ab901be07314a15db51a016dcf1e57b80806abb58ecc38545329290a12`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Zhang v61: divisibility / multiplicity uniqueness の最小cut

2026-09-29。**判定: Lemma 6 の Eq. (17)→(19) は成立しない。このproof chainは閉じない。RHはOPEN。**
これは整関数の一般推論への反例であり、ζの線外零点の発見ではない。

## Z1. 原本と監査範囲

Weicun Zhang, *A Proof of the Riemann Hypothesis via the Divisibility of Entire Functions*,
Preprints.org 202108.0146 **v61**、2026-09-09掲載。
[一次本文](https://www.preprints.org/manuscript/202108.0146/v61) は取得時に最新版URLへredirectし、Version 61と明示されていた。
§2のLemmas 3–5、§3 Lemma 6と(11)–(20)、§4の(22)–(30)を読んだ。

raw HTMLのcurl保存はHTTP 403となった。代わりにweb toolが取得した**一次HTMLの抽出response**を
版固定snapshot（原資料参照・公開版未収録: `literature/source_cache/zhang-202108.0146v61.web.json`） に保存した。
これはPDF・raw HTMLの保存と同一ではない。
snapshot SHA-256:
`fb2acf93ed8e13778c8eb1aa51dd0c51c865ca0c25c0c15362213b900ca3f29c`。
著者コードや外部scriptは実行していない。今回の監査は以下の一つのproof-critical代数に限定する。

## Z2. 原論文の主張と、独立に成立する部分

論文は、対称な整関数に対する局所一様・絶対収束積

\[
f(s)=\prod_i g_i(s)^{m_i},\qquad
g_i(s)=1+\frac{(s-\alpha_i)^2}{\beta_i^2},\qquad
f(s)=f(1-s)
\]

から、可除性と重複度の一意性によって全 `α_i=1/2` を導くと主張する。
必要なfactorの範囲は `0<α_i<1`、`β_i≠0`、非減少の `|β_i|`、収束する逆二乗和である。

正当な可除性が与えるのは、各iに対して**ある添字l**が存在して

\[
g_i(s)=g_l(1-s),\qquad
\alpha_i+\alpha_l=1,\quad\beta_i^2=\beta_l^2
\]

となることまで（Eq. (17)–(18)）。これは因子集合の反射による置換を許す。
実際、中心・虚部・multiplicityを保った零点のbijectionは対称性と完全に整合する。
Lemma 6はそこから、零点の重複度が一意であることを理由に **l=i** を強制する（Eq. (19)、(19c)直後）。
この一段が誤りである。重複度の一意性は「一つの零点での次数」を決め、異なる零点・異なるconjugate pairのラベルが反射で交換されることを禁じない。

## Z3. 二因子だけで見える誤り

\[
g_1(s)=1+(s-1/4)^2,\qquad g_2(s)=1+(s-3/4)^2.
\]

これらは実係数の異なる既約二次式であり、

\[
g_1(1-s)=g_2(s),\qquad g_2(1-s)=g_1(s).
\]

従って `g1 g2` は反射対称だが、個々の因子は反射不変ではない。
四つの零点 `1/4±i,3/4±i` はすべて相異なり、すべて単純。
例えば `1/4+i` はg1の単純零点で、g2では零点でないため、積における重複度も正確に1である。
同一quartetを二つのconjugate pairから記述できても、零点を二重に掛けたことにはならない。

中心変数 `z=s−1/2` では正確に

\[
g_1(s)g_2(s)=z^4+\frac{15}{8}z^2+\frac{289}{256}.
\]

この係数式はPython標準Fractionによる独立乗算でも確認した。
問題は浮動小数点・無限積の順序・可除性の微妙な定義には依存しない。

## Z4. 無限積・order 1・strip条件まで満たす反例

Lemma 6の無限積という前提に合わせ、次を取る。

\[
\boxed{
f_*(s)=
 [1+(s-1/4)^2][1+(s-3/4)^2]
 \prod_{n=2}^{\infty}\left(1+\frac{(s-1/2)^2}{n^2}\right).}
\]

各compact Kで
`Σ_(n≥2) sup_(s∈K)|(s−1/2)²/n²|<∞`。
従って積は絶対・局所一様収束し、零点は表示したfactorの零点だけである。
この関数は次の全性質を持つ。

- 非零整関数、実係数型、`f_*(0)>0`、実軸上で正。
- `f_*(s)=f_*(1−s)`。最初の二因子は交換し、残りは個別に不変。
- 全零点は `0<Re(s)<1`、虚部は非零。線上零点 `1/2±in, n≥2` は無限個。
- 全零点は単純でmultiplicityは一意。conjugate-pair indexは `β=(1,1,2,3,…)`、全 `m_i=1`。
- `Σ_i β_i^(−2)=2+Σ_(n≥2)n^(−2)<∞`。
- それでも四つの線外零点 `1/4±i,3/4±i` がある。

order 1も満たす。`z=s−1/2` とすると、標準積
[DLMF 4.36.1](https://dlmf.nist.gov/4.36.E1) により

\[
\prod_{n=2}^{\infty}(1+z^2/n^2)
=\frac{\sinh(\pi z)}{\pi z(1+z^2)}.
\]

z=0,±iの見かけの特異点は可除。実z→+∞では `f_*(1/2+z)∼z exp(πz)/(2π)` であり、
全複素平面でも指数型の上界を持つのでorderは正確に1。
したがって「Euler積の使用目的は零点をstrip内に閉じ込め、収束を確保すること」という原文の限定された役割は、この反例を排除しない。
f_*にζのEuler積があるとは主張していない。

## Z5. quartetのindexを一意にすれば修復できるか

二つの読みを分ける必要がある。

1. **conjugate pairをindexする読み。** これはHadamard積のEq. (22)が実際に列挙するもの。
   同じ線外quartetに二つの異なるpairがあり、各pairを一度ずつ掛けるのが正しい。
   この読みではZ4の反例がLemma 6の構造的仮定を満たし、Eq. (17)→(19)が偽。
2. **相異なるquartetを一回だけindexする読み。** この場合、線外quartetの因子は二次式一つでは足りず、
   `[g_(α,β)(s) g_(1−α,β)(s)]^m` という四次式が必要。
   Eq. (25)で一quartetにつき二次式一つだけを残すと、片側の二零点を落としてしまう。
   この読みではHadamard積からLemma 6の表示積への適用が未証明であり、線外quartetがないことを先取りしている。

また、同じ高さの異なるpairを禁止する `|β_i|` の厳密増加を追加しても、
反射対称な零点集合では線外quartetを既に排除したことになる。これはmultiplicity uniquenessの帰結ではない。

## Z6. 判定と停止

修復可能な正しい結論は、反射がconjugate-pair因子を同じmultiplicityで**置換する**というもの。
その置換は長さ1の軌道（critical line）だけでなく長さ2の軌道（off-line quartet）を許す。
長さ2を排除する独立の算術的入力は今回のlemmaに存在しない。

従って **Lemma 6の一般推論は反例で棄却、ξへの適用を含む当該証明経路は未成立**。
もしLemma 6をξと同じ零点を持つ関数だけへの主張と限定し直すなら、f_*はξの反例ではないが、
証明が実際に用いた対称性・可除性・multiplicity・strip・収束条件だけでは結論が出ないことは変わらない。
ξ固有の新しい排除機構が必要であり、表示の修正だけではRH証明へ進めない。
**RHの反証とは扱わず、この一件のbounded監査を終了する。** 他のstate・主証明グラフは編集しない。

独立監査: ROOTとLITERATUREが一次本文の仮定と無限積反例を別々に確認した。
`PROVED_IN_PAPER=YES` はLemma 6に証明文があるという記録だけであり、
`INDEPENDENTLY_VERIFIED=FAILED_AS_STATED`。明示反例の解析確認はYES。
最短依存は `Hadamard pair product → Lemma 6 (17)→(19) → (30) → RH` で、
この中央の一段がfatal cut。正しい置換結論へ修正しても線外軌道の排除は未証明のままである。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/zhang-202108.0146v61.web.json` — SOURCE REFERENCE NOT INCLUDED
