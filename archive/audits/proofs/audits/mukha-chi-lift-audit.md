**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/mukha-chi-lift-audit.md` · Original SHA-256: `f1b65a08420470043f94b663cd7f1b8f6bf59125878666948aaa13b387263d10`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Mukha v4 — χ 座標と全零点・スペクトル同定の bounded audit

判定日: 2026-09-29。担当: DESTROYER。**この DIRECT 証明経路は STOPPED。RH 自体は未解決。**

対象は Anatolii Mukha, *Riemann Hypothesis as a χ-∞ Boundary Law: Complete Operator-Spectral Proof in ZEBTS-∞*, Cambridge Open Engage, version 4, 2026-09-11。全95頁の網羅的監査ではなく、座標辞書と全零点のスペクトル同定だけを検査した。

## 1. 一次資料の固定と版の区別

- [v4 公開ページ](https://www.cambridge.org/engage/coe/article-details/6a9d8b60810b9dcc82acf85f)
- DOI: [10.33774/coe-2026-m9xcx-v4](https://doi.org/10.33774/coe-2026-m9xcx-v4)
- [ページの citation_pdf_url が指す v4 PDF](https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/6a9d8b60810b9dcc82acf85f/original/riemann-hypothesis-as-a-boundary-law-complete-operator-spectral-proof-in-zebts.pdf)
- PDF: 95頁、SHA256 2f288cf39a480d9c24c367a804df54512d48b760164090f5138a5d39f25f3d51。
- 恒久原本: `literature/source_cache/mukha-chi-v4.pdf`（Git/release対象外）。pypdf 抽出に加え、実ページ3・4・50を画像表示して核心式と前提を照合した。以下の頁番号は PDF の先頭を1とする。

公開ページの abstract / version notes は \(\chi=\exp(s-\tfrac12)\) を説明する。一方、v4 **本文** Definition 2.2.A（p.3）、Definition 4.1.A（p.8）、Definition 10.1.E（p.50）は

\[
 \chi(s)=\frac{s-1}{s+1},\qquad s(\chi)=\frac{1+\chi}{1-\chi}
 \tag{M1}
\]

を使用する。また Lemma 2.3.A（p.4）は局所的な lift のみを扱うとしている。指数写像の非単射性だけで v4 本文を反証したことにはしない。PDF 自体の組版で分数等の上下配置が平坦化しているが、対になった逆写像と Möbius map という明記から (M1) を読める。

## 2. 座標計算は表示どおりには偽。ただし技術的修復を分離する

Theorem 2.2.B と Corollary 2.2.C（pp.3–4）は

\[
 \Re s=\tfrac12
 \quad\Longleftrightarrow\quad
 \chi\in E_{\rm printed}:=
 \{|\chi-\tfrac12|=\tfrac12\}
 \tag{M2}
\]

を主張する。Theorem 10.3.A（p.51）も同じ写像と同じ円を使う。

**表示どおりの独立再証明: NO。厳密反例あり。**

有限点 \(s\ne-1\) について、

\[
 \chi(s)-\tfrac12=\frac{s-3}{2(s+1)},\qquad
 |\chi(s)-\tfrac12|=\tfrac12
 \iff |s-3|=|s+1|\iff\Re s=1.
 \tag{M3}
\]

最後は、\(s=\sigma+it\) として平方を展開すればよい。特に

\[
 s=\tfrac12:\quad \chi=-\tfrac13,\qquad
 |\chi-\tfrac12|=\tfrac56\ne\tfrac12.
 \tag{M4}
\]

これは有理数だけによる反例で、RH や未証明の零点仮説を使わない。\(s=\tfrac12\) が ζ の零点だとは主張していない。反証対象は本文の**全点についての座標同値式**である。

(M1) を維持する場合の正しい臨界像は

\[
 \Re s=\tfrac12
 \iff \left|\chi-\tfrac13\right|=\tfrac23,\quad \chi\ne1.
 \tag{M5}
\]

\(\Re((1+\chi)/(1-\chi))=(1-|\chi|^2)/|1-\chi|^2\)
から直接従う。\(\chi=1\) は有限の \(s\) に対応せず、円に含めるには臨界線の無限遠点を加えた compactification と明記する必要がある。

ただし ROOT が提示した、より自然な修正

\[
 \widetilde\chi(s)=\frac{2s-1}{2s+1},
 \qquad s=\frac{1+\widetilde\chi}{2(1-\widetilde\chi)}
 \tag{M6}
\]

を独立に代入確認すると、本文の他の掲示式と一括して整合する:

\[
 \widetilde\chi(\tfrac12+it)
 =\frac{t^2+it}{1+t^2},\quad
 \widetilde\chi(1)=\tfrac13,\quad
 \widetilde\chi(-2n)=\frac{4n+1}{4n-1}.
\]

また \(\Re s=\tfrac12\iff|\widetilde\chi-\tfrac12|=\tfrac12\)
（\(\widetilde\chi\ne1\)）となる。したがって (M1) の誤りは **TECHNICAL な修復候補がある**。これだけをもって修復後の全論証まで反証したとはしない。以下はこの修正を認めた後にも残る、全零点同定の主 cut である。

## 3. 主 cut: Theorem 10.2.C は境界所属を既に仮定している

ここでは (M6) へ修正し、さらに本文の局在化定理まで仮に認める。これは局在化定理を独立に検証したという意味ではない。

Definition 10.1.E（p.50）は、すべての非自明零点が、境界近傍に支持されたポテンシャルで局在する固有関数等に対応する、と宣言する。しかし、その直後の **Theorem 10.2.C の実際の左辺には境界所属が含まれる**:

\[
 [\zeta_\chi(\chi_0)=0\ \land\ \chi_0\in E_\chi]
 \quad\Longleftrightarrow\quad
 \exists\phi_n:\;(\chi_0,\phi_n)
 \text{ is a }\chi\text{-spectral zero}.
 \tag{M7}
\]

Definition 10.2.A の右辺は、ζ の消失、固有方程式、点近傍への質量局在、および
\(\operatorname{supp}V_{\varepsilon,\delta}\subset N_\delta(E_\chi)\)
を同時に要求する。Theorem 6.5.A（p.20）と Theorem 10.4.A（pp.52–54）は、全非自明零点についてこの右辺が成立することを **RH と同値な命題**として表示する。

\(Z(\chi)\) を非自明零点であること、\(S(\chi)\) を要求されたスペクトル局在が存在することと書けば、

\[
 [Z(\chi)\land\chi\in E]\iff S(\chi)
 \quad\not\Longrightarrow\quad
 \forall\chi\,[Z(\chi)\Rightarrow S(\chi)].
 \tag{M8}
\]

(M7) から後者を得るには、先に
\(\forall\chi\,[Z(\chi)\Rightarrow\chi\in E]\)
が必要になる。修正された正しい座標ではこれはまさに RH である。

**独立確認: YES — 境界所属の前提は実 PDF にある。NO — Theorem 10.2.C は境界外候補も含む全零点のスペクトル同定を証明していない。**

この欠落は抽象的な自己共役性に対する一般論だけではない。本文の固有方程式は

\[
 (-\Delta_\chi+1+V_{\varepsilon,\delta})\phi_n
 =\lambda_n^{\varepsilon,\delta}\phi_n
\]

である。\(\lambda_n^{\varepsilon,\delta}\) は実の固有値、\(\chi_0\) は球面上の位置であり、別の変数である。Definition 10.2.A / Theorem 10.2.C は、零点の高さや重複度を単一作用素の固有値へ写すスペクトル恒等式を与えていない。ポテンシャルは局在点・許容誤差等に応じて選ばれるため、点ごとの局在可能性と、ζ を一つの自己共役作用素へ完全同定することも区別する必要がある。

実ポテンシャルが滑らかなら、コンパクト球面上の
\(H_\chi=L^2(S_\chi^2,d\mu_\chi)\), \(D(T_\chi)=H^2(S_\chi^2)\)
という設定で自己共役性・コンパクト resolvent を得る標準部分は、この主 cut の対象ではない。それらは指定された**算術的な全零点**について (M8) の右側の全称命題を供給しない。

Theorem 12.7.A と §12.7.2（pp.80–81）も RH から出発して RH に戻る同値の連鎖を記載する。同値な条件の定式化と、そのうち一条件が無条件に真であることの証明は異なる。Definition 10.1.E を全零点についての追加仮定として採用するなら、本文の幾何・局在同値の下で RH 相当の bridge を仮定していることになる。

## 4. 指数写像への周期性反証の適用範囲

これは **公開 metadata の指数写像説明に限る条件付き検査**であり、Möbius 写像を採用した v4 本文の確定 cut ではない。

仮に一価な関数 \(Z\) が存在し、
\(\zeta(s)=Z(e^{s-1/2})\)
が全対象点で成立すると主張するなら、\(\zeta(s+2\pi i)=\zeta(s)\) が必要になる。これは偽である。例えば絶対収束する Dirichlet 級数において

\[
 |\zeta(2+2\pi i)|
 =\left|\sum_{n\ge1}n^{-2}e^{-2\pi i\log n}\right|
 <\sum_{n\ge1}n^{-2}=\zeta(2).
\]

厳密不等号は \(n=1\) と \(n=2\) の位相が異なることから従う。\(\log2\in(0,1)\) なので二つの位相は一致しない。まずこの二項に厳密三角不等式を用い、残りに通常の三角不等式を用いれば十分である。

しかし局所的な対数の枝、または deck index を保持した普遍被覆上の構成には、この global descent 反証をそのまま適用できない。v4 の Möbius 座標は \(\widehat{\mathbb C}\setminus\{1\}\) 上で ζ と合成できる一価な座標であり、対数の枝を必要としない。\(\chi=1\) における特異性と対数の多価性も別問題である。

## 5. bounded gate の結論

| 対象 | 独立判定 |
|---|---|
| 公開ページと v4 PDF が同じ χ 写像を使う | NO。指数写像と Möbius 写像が異なる |
| Definition 2.2.A と Theorem 2.2.B の表示どおりの整合性 | NO。有理数反例 (M4) |
| 因子2を入れた座標修正 (M6) と後続の円・極・自明零点 | YES。TECHNICAL 修復候補 |
| Theorem 10.2.C が境界所属を前提に含む | YES。p.50 の画像で確認 |
| この定理から全非自明零点を漏れなく局在固有関数へ送れる | **FAILED。境界所属を先に仮定する bridge が残る** |
| 全95頁の作用素・Agmon・resolvent 論証 | NOT AUDITED。この bounded task の範囲外 |
| RH の反例 | なし |

主 cut は座標の誤記そのものではなく、修正後にも残る全零点のスペクトル同定である。この入力を定義として与えても RH の独立証明にはならない。新しい修復候補へ拡張せず、この DIRECT claim の gate 検査を終了する。

独立確認: ROOTが本文pp.3–4・50・52–56を読み、p.4を画像確認し、修正前後の座標をFractionで検算。LITERATUREも§6と§10を別途確認し、全零点bridgeが残るとの限定判定に一致した。`PROVED_IN_PAPER`と独立確認は分離し、全作用素論証の独立検証はNOのまま。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/mukha-chi-v4.pdf` — SOURCE REFERENCE NOT INCLUDED
