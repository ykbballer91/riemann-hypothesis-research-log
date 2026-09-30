**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/finite_negative_index_gate.md` · Original SHA-256: `593fb80b1fe0cc8a2fa36f4d84e4f789d1026761dbd55288ba78b240eddec2a8`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 有限負指数から RH への gate

2026-09-29 / DESTROYER。**有限負指数だけで RH を閉じる案は採用しない。RH は未解決。** 新しい全窓計算・RH の証明・ζ の反例は含まない。

## 一次資料と適用範囲

Enrico Bombieri, *Remarks on Weil’s quadratic functional in the theory of prime numbers, I*, Rend. Mat. Acc. Lincei, s.9, 11 (2000), 183–233。

- [一次 PDF](http://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0)
- 固定原本: bombieri-weil-2000.pdf（原資料参照・公開版未収録: `literature/source_cache/bombieri-weil-2000.pdf`）。53 PDF 頁（表紙等を含む）。
- 原本 SHA256: 20bd544fc5297766966630092aba4c1e10c6a7e663d14be89bbe1d0c8220b7fd。
- 本文の Theorems 8–11、Introduction p.185、Corollary p.224 を読み取り。p.185 は画像でも照合した。以下は印刷頁番号。

**Theorem 8（p.213）:** §8 の有限 multiset \(\Gamma\) は共役・符号反転で不変で、重複度も対称である。固定 \(t>0\) の有限行列 \(H(\Gamma;t)\) の負固有値数は、\(\Gamma\) 内の**相異なる非実共役対**の数に等しい。

**Theorem 9（p.217）:** §9 の有限行列 \(K_E(\Gamma)\) について同じ計数が成立する。ここで \(E\) は有界閉区間の有限和（非退化な区間を含む）である。さらに \(E=-E\) なら even/odd 部分の計数を区別する。これは有限行列の定理であり、全テスト空間や、固定 support の無限極限の正負指数へ無条件に読み替えない。

**重複度:** 原定理の語は distinct である。重複した評価点を独立の負方向として重複度回だけ数えてはならない。

**無限極限の残り:** §10 は対称な無限 multiset に
\(\sum_\gamma(1+|\gamma|)^{-1-\varepsilon}<\infty\)
（各 \(\varepsilon>0\)）を課して有限 truncation から極限を取る。有限個の非実点が存在しても、固定 support の負固有値が極限で0へ近づく可能性を残す。Theorems 10–11 はその場合の線形依存関係を扱う。

Introduction p.185 と §11 Corollary p.224 の結論は、概略

\[
 \mathrm{RH}\quad\text{または}\quad
 \text{軸外零点が無限個}\quad\text{または}\quad
 \text{指定された }\ell^2\text{ 係数の線形依存関係}
\]

という三者択一である。第三の場合を排除した「有限例外なら無例外」という定理ではない。p.224 の corollary は指定された集合に support を持つ全 smooth test での Weil positivity を仮定してなお、この第三の場合を残す。

したがって、**この既存定理を引用して有限負指数から RH を結論してはならない**。「ζ の有限例外をすべて排除する」追加命題は今回供給されていない。一次資料に書かれていない未解決性の文言や、証明済みという評価を帰属させない。

## 必要最小限の独立代数

\(F(z)=\int f(x)e^{izx}dx\) とする。非実共役評価対の Hermitian 寄与は

\[
 m\{F(z)\overline{F(\bar z)}
    +F(\bar z)\overline{F(z)}\},
 \qquad m>0,
\]

すなわち \(mJ,\ J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\)。
signature は \((1,1)\)。全複素テスト空間では通常の軸外 quartet は二つの共役対を与える。有限個の対があれば、臨界線上の非負和を加えても負指数の上界は対の数であり、positivity は従わない。

平行移動 \(f(x)\mapsto f(x-t)\) は、\(z=b-ia\) の対上で

\[
 D_t=e^{ibt}\operatorname{diag}(e^{at},e^{-at}),
 \qquad D_t^*JD_t=J
\]

として作用する。\(v=(1,-1)\) の二つの移動 \(D_tv,D_uv\) の Gram 固有値は
\(-2\pm2\cosh(a(t-u))\)。
各移動の値が負であることから、その span が負定値とはならない。translation invariance は負指数を無限化しない。

## 対称 entire toy（ζ ではない）

中心変数 \(w=s-\tfrac12\)、\(a,b>0\) として

\[
 H(w)=\cosh w\,[(w-a)^2+b^2][(w+a)^2+b^2]
\]

は実型・偶・order 1 の entire function である。虚軸上の無限零点と、軸外 quartet \(\{\pm a\pm ib\}\) 一つを持つ。

その零点に対し
\(Q_H(f)=\sum_\lambda Lf(\lambda)\overline{Lf(-\bar\lambda)}\),
\(Lf(w)=\int f(x)e^{wx}dx\)
を定めると、虚軸部分は非負で、負指数は高々2。実際2に達する: 軸外4点で非零の \(L\psi=\Psi\) を持つ \(\psi\in C_c^\infty\) を選び、
\(Lf(w)=\cosh w\,p(w)\Psi(w)\)
とする。次数3以下の補間多項式 \(p\) によって軸外4評価値を任意に指定でき、虚軸零点での寄与はすべて零になる。この \(f\) は \(\psi\) の平行移動と有限階微分の線形結合なので \(C_c^\infty\) に属する。従って二つの \(J\) block の負部分空間が実現される。

これは対称性・translation invariance・有限負指数の組合せが positivity を強制しない厳密例である。ζ の Euler product や算術構造を再現した例ではなく、ζ の有限例外の存在証明でもない。

## 採用しない強い主張

全 compact core の負指数が、相異なる軸外零点数の半分に厳密に等しいという式は、今回 **導出候補・採用不使用** とする。完全な有限補間・tail suppression 証明をこのノートでは提示しておらず、Bombieri の有限行列定理から直接転記もしない。

今回の判定に必要なのは、有限例外の場合には有限の不定 block が残り得ること、translation がそれを排除しないこと、引用した既存定理が finite-exceptions ⇒ none を供給しないことだけである。従って有限 rank / Pontryagin 化を RH の閉鎖として扱う案は、追加の算術的排除定理なしには採用しない。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/bombieri-weil-2000.pdf` — SOURCE REFERENCE NOT INCLUDED
