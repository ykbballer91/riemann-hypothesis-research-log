**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic/notes/literature_comparison.md` · Original SHA-256: `c9779a2ab09f1e2a920c9c3921041885fccb1aa654981ffb186066a6aa997c1e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic track：Nyman–Beurling、Möbius 逆変換、cutoff の限定比較

2026-09-30。既存 one-prime の定義を読み、下記の一次資料に限定して照合した。新しい RH proof claim は探索していない。文献全体の独立検証、新規性、今回の構成と NB criterion の同一性は主張しない。旧ファイルは変更しない。

## 1. 一次資料と正確な範囲

**B55.** Arne Beurling, *A closure problem related to the Riemann zeta-function*, PNAS **41** (1955), 312–314, [出版社 PDF](https://www.pnas.org/doi/pdf/10.1073/pnas.41.5.312), DOI 10.1073/pnas.41.5.312。p.312 の番号なし Theorem は、\(1<p<\infty\) に対し \(\zeta\) の \(\Re s>1/p\) での非消滅と、\(\sum c_\nu\{\theta_\nu/x\}\), \(0<\theta_\nu<1\), \(\sum c_\nu\theta_\nu=0\) の \(L^p(0,1)\) における稠密性の同値。p.312–313 の dilation argument は **全ての** \(0<a<1\) を用いる。\(p=2\) が RH に対応する。原文抽出を照合したが、今回 screenshot は出版社の cookie ページへ転送された。Nyman の 1950 年学位論文自体は今回未読。

**BD02.** Luis Báez-Duarte, *A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis*, [math/0202141v2](https://arxiv.org/html/math/0202141v2), 2002-02-18。§1 Theorem 1.1：
\[
\mathrm{RH}\iff
\chi_{(0,1)}\in\overline{\operatorname{span}\{\rho_a:a\in\mathbb N\}}^{\,L^2(0,\infty)},
\qquad \rho_a(x)=\{1/(ax)\}.
\]
全整数 \(a\) が対象で、\(a=2^j\) だけという定理ではない。§2.1 Lemma 2.1 は、指定半平面の zero-free 仮定の下で重み付き Möbius 部分和を評価する。§2.2 / Cor.3.1 では Möbius 近似の \(L^2\) 収束に RH が関わる。局所絶対収束による形式的逆変換と、その大域 \(L^2\) 収束を分離する必要がある。

**BD05.** Luis Báez-Duarte, *A general strong Nyman-Beurling criterion for the Riemann Hypothesis*, [math/0505453v1](https://arxiv.org/html/math/0505453v1), arXiv 2005-05-22（本文 date は 2005-05-16）。§1.1 Eq.(1.1) の Müntz/co-Poisson operator は
\[
Pf(x)=\sum_{n\ge1}f(nx)-x^{-1}\int_0^\infty f(u)\,du.
\]
Def.1.1 の good kernel は \(f\in C^1_0\cap L^1\), \(\int_0^\infty u|f'(u)|du<\infty\)。Theorem 2.1 / Eq.(2.10) は \(\widehat{Pf}(s)=\zeta(s)\widehat f(s)\), \(0<\Re s<1\)。Theorem 1.2 は RH から全整数 dilation による \(L^2\) 近似を与える。逆向きは compact support の下で \(Z(\zeta)\subset Z(\widehat f)\) までであり、Theorem 1.3 の RH 同値には \(\widehat f\) が \(1/2<\Re s<1\) で零点を持たない条件も必要。abstract の短い要約からこの条件を落とさない。

**M03.** Ralf Meyer, *On a representation of the idele class group related to primes and zeros of L-functions*, [math/0311468v1 §5.3](https://arxiv.org/html/math/0311468v1#S5.SS3), 2003-11-26；[指定版 PDF](https://arxiv.org/pdf/math/0311468v1)、pp.40–41, Lemmas 5.3–5.4。これは今回の inverse-plus-cutoff に最も近い既知構成。
\[
\mathcal L_S=\prod_{v\notin S}(1-\lambda_{p_v}^{-1})^{-1},\qquad
\mathcal L_S^{-1}=\prod_{v\notin S}(1-\lambda_{p_v}^{-1}).
\]
Lemma 5.3 は sufficiently large finite \(S\) について summation と \(\mathcal L_S\) を同定し、両作用素を \(L^2(\mathcal C_S)_{>}\), \(\mathcal S(\mathcal C_S)_{>}\) 上で有界とする。証明は \(\|\lambda_{p_v}^{-1}\|_\alpha=q_v^{-\alpha}\), \(\alpha>1\) と Euler 積の絶対収束を使う。Lemma 5.4 は
\[
p_+^S(f_0,f_1)=
M_{1-\phi}\mathcal L_S^{-1}f_0+
\mathfrak F M_{1-\phi}\mathcal L_S^{-1}Jf_1
\]
を構成する。直後の本文が述べるのは **approximate section / approximate projection** であり、恒等な section ではない。critical-line norm の逆作用素評価や type-zero growth はこの定理の結論ではない。

以上は該当 statement の原文照合であり、各論文全体の独立再証明ではない。arXiv の指定版を、未確認の査読最終版と同一視しない。

## 2. 「dyadic」の二つの意味を分ける

今回の商は全整数を使う
\[
\Sigma f(x)=2\sum_{m\ge1}f(mx),\qquad
f\in\mathcal S(\mathbb R)_{\rm even},\quad f(0)=\int_{\mathbb R}f=0
\]
の range で割る。時間だけを \(a=2^n\) に制限しても、算術 range を一つの素数へ制限していない。全整数 Möbius 係数も残る。

これに対し \(A_2f=\sum_{j\ge0}f(2^jx)\) そのものへ交換すると、十分な収束域で逆は \(I-S_2\), \(S_2f(x)=f(2x)\)。Mellin multiplier は \((1-2^{-s})^{-1}\) となり、\(\zeta(s)\) ではない。

次は文献定理への帰属ではなく直接検算。BD02 の生成族を \(a=2^j,\ j\ge0\) のみにすると、\(\chi_{(0,1)}\) はその \(L^2(0,\infty)\) 閉包に入らない。有限和 \(F=\sum_j c_j\rho_{2^j}\), \(A=\sum_j2^{-j}c_j\) は
\[
F(x)=
\begin{cases}
A/x,&x>1,\\
A/x-c_0,&1/2<x<1,\\
A/x-2c_0-c_1,&1/3<x<1/2,\\
A/x-3c_0-c_1,&1/4<x<1/3.
\end{cases}
\]
\(F_k\to\chi\) を仮定すると、順に \(A_k\to0,\ c_{0,k}\to-1,\ c_{1,k}\to1\)。最後の区間では \(F_k\to2\) となり矛盾する。この限定排除は、今回の full-arithmetic quotient の \(T_2^n\) を排除するものではない。負の \(j\) まで許す別の生成問題も扱っていない。

## 3. 今回の代表元 reduction と既知の構成との対応

以下は対象の操作を明確にする直接計算である。\(H\) は正の軸の smooth function で、各 \(x\ge\eta>0\) 上で全導関数が任意の冪より速く減衰するとする。
\[
F(x)=\frac12\sum_{m\ge1}\mu(m)H(mx).
\]
この和は \(x\ge\eta\) 上で導関数ごとに局所一様絶対収束する。また \(\sum_k d(k)|H(kx)|<\infty\) なので
\[
2\sum_{n\ge1}F(nx)
=\sum_{k\ge1}H(kx)\sum_{m\mid k}\mu(m)=H(x).                 \tag{A}
\]
ここには RH も Möbius の符号 cancellation estimate も不要。全整数の Dirichlet convolution inversion を使っている。

\(\chi=0\) on \(x\le1/2\), \(\chi=1\) on \(x\ge1\) とし、\(\psi\in C_c^\infty((1/2,1))\), \(\int_0^\infty\psi=1\) を固定する。
\[
f(x)=\chi(x)F(x)-
\left(\int_0^\infty\chi(u)F(u)\,du\right)\psi(x)\quad(x>0)
\]
を偶延長すれば \(f\) は Schwartz、\(f(0)=0\)、\(\int_\mathbb Rf=0\)。\(x\ge1\) では全 \(nx\ge1\) なので (A) がそのまま残り、\(H-\Sigma f=0\)。したがって既存商における代表元を \(x\le1\) へ押す代数的構成として成立する。mean correction は \(x\ge1\) の一致を壊さない。一方、cutoff 前の \(F\) が \(x=0\) まで Schwartz であるとは主張しない。

M03 の \(\mathbb Q\), \(S=\{\infty\}\), compact-unit invariant sector では、\(\mathcal L_S\) と \(\mathcal L_S^{-1}\) がそれぞれ \(\sum_{m\ge1}S_m\), \(\sum_{m\ge1}\mu(m)S_m\) に対応する。偶関数の \(\{\pm1\}\) summation による 2 を分離すれば (A) と一致する。**Euler inverse と cutoff の組合せ自体は既知である。** ただし M03 の二成分・Fourier 補正付き approximate section と、今回の一側 support reduction・独立 mean correction・特定の \(p_1,p_4\) 評価を、同じ定理とする証拠は今回得ていない。literal な同一公式の最初の出典や新規性は未判定。

BD05 の \(P\) は同じ算術和の zero-mean correction を明示する先行枠組みだが、その \(L^2\) cyclic approximation theorem から、今回の全 class の quotient seminorm growth が自動的に従うわけではない。

## 4. 条件付き cancellation を endpoint の証明へ昇格しない

RH から
\[
M(X):=\sum_{m\le X}\mu(m)=O_\varepsilon(X^{1/2+\varepsilon})            \tag{B}
\]
が従う classical input は BD02 §2.1 が明示的に引用する Littlewood の定理（Titchmarsh, Theorem 14.25(A)）および同節 Lemma 2.1 で確認できる。今回 Titchmarsh 原本自体は未照合。

必要形は引用定理から直接出る。固定 \(1/2<\sigma<1\) に対し、RH の下で \(A_\sigma(X)=\sum_{m\le X}\mu(m)m^{-\sigma}\) は有界。部分積分により
\[
M(X)=X^\sigma A_\sigma(X)-\sigma\int_1^X A_\sigma(u)u^{\sigma-1}\,du
=O_\sigma(X^\sigma).
\]
逆に (B) が全 \(\varepsilon>0\) で成立すれば、部分積分で \(1/\zeta(s)\) の Dirichlet series を \(\Re s>1/2\) へ holomorphic に延長でき、既知の \(\Re s>1\) の恒等式と解析接続で同半平面に零点がない。関数等式と合わせ RH。従って (B) は無条件に追加できる弱い補題ではない。

ROOT が検算している \(H_a(x)=a^{-1/2}H(x/a)\) の explicit representative について、無条件 \(a^{1/2}(1+\log a)\) 型と、仮定 \(|M(X)|\le C X^\theta\) による \(a^{\theta-1/2}\) 型は別の statement。特に \(\theta=1/2+\varepsilon\) を全 \(\varepsilon\) に使う段階で RH 相当の arithmetic cancellation を輸入する。このノートはその代表元評価自体を文献既証明、あるいは独立監査済みとして登録しない。

**Decision:** 全整数 Möbius inversion と cutoff による具体化を、既知の Müntz/Meyer 枠組みに位置付ける。dyadic 時間 sampling を dyadic-only arithmetic と混同しない。NB との文字通りの同一性は未証明。無条件の代表元構成とその検証済み成長率は保持できるが、RH 相当の Mertens bound を使った endpoint 改善を新しい RH 入力とは数えない。限定探索はここで終了する。
