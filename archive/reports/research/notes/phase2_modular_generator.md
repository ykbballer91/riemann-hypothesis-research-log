**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase2_modular_generator.md` · Original SHA-256: `71e5501d76d245cd191f69d5786de13f62b56f35ac50ded94f5ee85f153e674c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase II Track D — actual Gaussian の固定点と整数格子 lift の障害

2026-09-29。内部導出を先に行い、その後に Riemann 原論文と標準公式を照合した。
これは初期候補の限定検査であり、RH の証明・反証・新規性の主張ではない。
標準 Gaussian、全整数格子、標準 Euler 積、標準 Gamma 因子を固定する。
Phase I の Gamma 因子を変更した模型は新しい反例として再利用しない。

## Candidate generator

Fourier 変換を \(\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}dx\) とする。
\(L^2(\mathbb R,dx)\) 上で

\[
 B=\frac d{dx}+2\pi x,\qquad
 G=\overline B^{\,*}\overline B
   =-\frac{d^2}{dx^2}+4\pi^2x^2-2\pi\ge0.
\]

最初は \(C_c^\infty\) 上で定義し、\(B\) を閉包し、\(B^*B\) による自己共役実現を用いる。
その核は \(g(x)=e^{-\pi x^2}\) の一次元空間である。
実際 \(Gf=0\) なら \(Bf=0\)、弱微分方程式から \(f=Cg\) となる。
\(g(0)=1\) により標準 Gaussian が一意に固定される。
\(\widehat g=g\) も正確であり、ここには RH の仮定はない。

検査する具体的移送候補は、整数 dilation lift

\[
 (Tf)(x)=\sum_{n\ge1}f(nx),\quad x>0,
\]

を用いてこの正の固定点生成子を actual theta 側へ移すことである。
以下はこの素朴な intertwining を直接反証する。

## Arithmetic input

\[
 h(x)=Tg(x)=\sum_{n\ge1}e^{-\pi n^2x^2},\qquad
 \Theta(x)=1+2h(x).
\]

\(x>0\) の各 compact 区間では任意回微分した級数まで一様収束する。
\(\Re s>1\) では絶対収束により

\[
 \int_0^\infty h(x)x^{s-1}dx
 =\frac12\pi^{-s/2}\Gamma(s/2)\sum_{n\ge1}n^{-s}
 =\frac12\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

したがって、この候補の算術は全整数係数、すなわち標準 Euler 積そのものである。
有限素数の切断や新しい completion を挿入していない。

## Boundary data

Poisson により

\[
 \Theta(x)=x^{-1}\Theta(1/x),\qquad
 h(x)=x^{-1}h(1/x)+\frac{x^{-1}-1}{2}.
\tag{D1}
\]

\(Jf(x)=x^{-1}f(1/x)\) は \(L^2(\mathbb R_+,dx)\) の unitary involution。
ただし \(\Theta\) はその Hilbert 空間のベクトルではない。
\(h(x)=1/(2x)-1/2+O(x^{-1}e^{-\pi/x^2})\) as \(x\downarrow0\) なので
\(h\notin L^2(\mathbb R_+,dx)\)。
\(\Theta(x)\to1\) as \(x\to\infty\) も別の非可積分端点を与える。
形式的な \(J\)-固定点と Hilbert 空間内の正規化状態を同一視できない。

\(x=e^t\) と半密度 \(e^{t/2}\) を用いれば (D1) は
\(e^{t/2}\Theta(e^t)=e^{-t/2}\Theta(e^{-t})\) となる。
これは尺度反転の正確な固定点だが、なお両端で増大する。
既存の subtraction による \(U\)、\(\Phi\) の構成は
`research/selfdual_theta_boundary.md` と `research/continuum_subtraction.md` にある。
その再導出は今回の新しい成果に数えない。

## Evolution law

\(e^{-\tau G}\), \(\tau\ge0\), は非負自己共役生成子の contraction semigroup で、
\(e^{-\tau G}g=g\)。しかし \(T\) はこの flow をそのまま theta に移さない。
\(D_nf(x)=f(nx)\)、\(g_n=D_ng\) とおくと、直接微分で

\[
 Gg_n
 =2\pi(n^2-1)\bigl[1-2\pi(n^2+1)x^2\bigr]g_n.
\tag{D2}
\]

従って \(N\ge2\)、\(T_N=\sum_{n=1}^ND_n\) なら

\[
 GT_Ng-T_NGg
 =\sum_{n=2}^N2\pi(n^2-1)
  \bigl[1-2\pi(n^2+1)x^2\bigr]e^{-\pi n^2x^2}<0
 \quad(x\ge1).
\tag{D3}
\]

全和にも compact 一様収束で同じ厳密不等式が成立する。
よって \(GT=TG\) は、標準 Gaussian という一つの入力だけで既に偽である。
有限 \(N\) でも成立しないため、無限和の誤差評価だけでは修復できない。
これは \(G\ge0\) と矛盾しない。作用結果の点ごとの符号は二次形式の符号ではなく、
全和 \(h\) はさらに \(G\) の Hilbert 空間の外にある。

他方、尺度微分 \(A=x\partial_x+1/2\) は各 \(D_n\) と形式的に可換である。
\(Vf(t)=e^{t/2}f(e^t)\) により \(-iA\) は \(-i\partial_t\) へ unitary に移る。
ここでも \(Tg\) は \(L^2\) の外なので、点ごとの交換式から unitary spectral
identification は得られない。裸の dilation spectrum に関する Phase I の障害は
既存結果として参照するだけで、今回の新しい RH 制約とはしない。

## Why 1/2 appears

\(dx=e^t dt\) の半密度が \(e^{t/2}\) を与え、尺度反転は Mellin パラメータを
\(s\leftrightarrow1-s\) と交換する。その不変な鉛直線が \(\Re s=1/2\) である。
これは測度と反転の正規化の説明であって、全零点がこの線上に属する証明ではない。
\(G\) の非負性は Gaussian を固定するが、(D3) のため actual lattice lift には
同じ非負生成子がそのまま作用していない。

## What forbids off-line states

現時点では、この候補にその禁止機構はない。
actual completed kernel の規約
\(\xi(s)=\int_{\mathbb R}\Phi(t)e^{(s-1/2)t}dt\)
を使うと、\(s=1/2+\delta+i\gamma\) に対して

\[
 \xi(s)=2\int_0^\infty\Phi(t)
 \left[\cosh(\delta t)\cos(\gamma t)
       +i\sinh(\delta t)\sin(\gamma t)\right]dt.
\tag{D4}
\]

すべての積分は actual theta の両側 superexponential decay により収束する。
\(\delta\ne0\) はこの exact representation の domain から排除されていない。
反転は二つの積分の対称性を与えるが、同時消滅を妨げる符号評価は与えていない。
これは actual off-line zero の存在を主張する式ではない。

## Known prior art

Riemann 1859 の原論文（Wilkins 訳、本文 p.3／PDF p.4）に、全整数 Gaussian 和の
Mellin 表現、Jacobi の反転公式、標準 completion、臨界線パラメータへの変換がある。
次頁で零点がすべて実であることは別途の未証明事項とされている。
[一次資料](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-translation.pdf)。
現代規約は [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32)、
[25.4.3–4](https://dlmf.nist.gov/25.4.E3)、
[25.5.13–14](https://dlmf.nist.gov/25.5.E13) と照合した。
生成子と (D2)–(D3) はここで直接計算した初等式であり、既知性の網羅調査や新規性の
主張は行わない。

## RH-equivalent hidden assumption?

\(G\) の構成、正性、Gaussian の一意性、(D1) に RH 同値の仮定はない。
しかし、すべての零点パラメータを \(-i\partial_t\) の実スペクトルへ漏れなく
同定できる、と追加すれば、その実数性は既に要求する結論を含む。
対応写像、domain、全零点と重複度の回収を示さずにこの追加を行わない。

## Synthetic counterexample status

全 Euler 積を同じ半平面 \(\Re s>1\) で保ち、同じ標準 Gamma と解析接続を持つ
別の completed function を作ることはできない。同一の収束域で一致すれば、
連結な解析接続領域では恒等定理で actual \(\xi\) と一致する。
この一意性は零点位置の証明ではない。

したがって、ここで新しい synthetic off-line function を「全算術保持模型」とは
称さない。候補 intertwining の試験は actual \(g\) と actual integer dilations
による厳密な (D3) で完了する。Gamma を変えた旧模型、対称 quartet、直和の
\(\sum1/n\) 発散を新しい進展として追加しない。

## Exact missing lemma

この特定の \(G,T\) について必要だった \(GT=TG\) は欠けた補題ではなく偽である。
別の arithmetic generator を採用するなら、(D2) の非零残差と (D1) の端点項を
含む exact map、その閉作用素 domain、正性の独立証明、actual \(\xi\) の
全零点との対応を新しく指定する必要がある。残差を黙って削除する修復は不可。
そのような別の生成子が存在しないという一般的不可能性は示していない。

## Decision

**STOP THIS INTERTWINING CANDIDATE / KEEP TRACK D AS INITIAL SCREEN.**
標準 Gaussian の正の固定点生成子から、整数格子和を単に通して全零点の自己共役
スペクトル同定を得る機構は、actual data のまま (D3) で止まる。
modularity／renormalization 一般の否定ではない。RH は未解決のままであり、
主証明グラフへの追加、数値全窓探索、旧反例の再計上は行わない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/continuum_subtraction.md`](../continuum_subtraction.md)
- [`research/selfdual_theta_boundary.md`](../selfdual_theta_boundary.md)
