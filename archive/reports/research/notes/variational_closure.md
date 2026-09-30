**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/variational_closure.md` · Original SHA-256: `d8b20552eac7564af4467d91314c22603be721bac5a401c66429e6449dda9987`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# D/E 独立監査: Weil 作用・エネルギー・作用素による閉鎖候補

作成: 2026-09-29。担当: DESTROYER。現時点で **RH は未解決**。

対象は `proofs/lemmas/finite_to_infinite.md` と `proofs/lemmas/weil_conventions.md` の Q である。既存の固定 support における連続性・稠密性・Gram 橋渡しは再検算後も生存する。しかし、正値性を伝播する新しい原理はそれらから得られない。本ノートでは、その先の候補を正確に書き、同値化・過剰仮定・反例・有用な局所構造を区別する。

以下の有限行列や Schrödinger 作用素の反例は **ζ の反例ではない**。実際の Weil 形式について示す反例は、誤った作用素実現や window 差分の単調性への反例であり、Weil 正値性自体を否定するものではない。

## 0. 規約と候補の判定表

\[
\mathcal D=C_c^\infty(\mathbb R;\mathbb C),\quad
F_f(z)=\int f(x)e^{izx}dx,\quad
z_\rho=\frac{\rho-1/2}{i},\quad
Q(f,g)=\sum_\rho F_f(z_\rho)\overline{F_g(\bar z_\rho)}.
\]
Q は第1変数線形、Hermitian で、固定 support 上では \(p_1\) に連続である。\(Q(f)=Q(f,f)\) と略記する。

| 候補 | 正確な内容 | 判定 |
|---|---|---|
| D1 抽象因子分解 | ある Hilbert 空間と線形 A により、全 \(f\in\mathcal D\) で \(Q(f)=\|Af\|^2\) | RH と同値。A の具体的構成なしでは言い換え |
| D2 通常 L² 上の閉因子分解 | D1 に加え、A は \(L^2(\mathbb R,dx)\) を始域とする closable 作用素 | FALSE。§2 の拡大 support 列で閉可能性が破綻 |
| D3 正核 | 指定した変換 T と測度 μ について \(Q(f)=\int k|Tf|^2d\mu\)、\(k\ge0\) | 恒等式を独立に証明すれば有効。任意の T を許す存在命題は D1 と同型 |
| D4 ground state | 明示的な正関数 g を使う ground-state transform | 局所/跳躍形式・境界・固有値符号が必要。一般 Hermitian 形式には不可 |
| E1 全窓 coercivity | 各 L で \(Q(f)\ge c_L\|f\|_2^2\)、\(c_L>0\) | 全 L の主張は RH を含意。局所定理のみでは伝播しない |
| E2 一様 coercivity | 全 support で同じ \(c>0\) | FALSE。RH を仮定しても Fourier packet で下界0 |
| E3 PSD 残差 flow | 新窓の形式−旧窓の零拡張が PSD | FALSE。非零の旧新 coupling と両立しない。実 Weil でも §5 の反例 |
| E4 Schur 帰納 | 各追加ベクトルの Schur complement を非負と証明 | 正しい判定式。必要な coupling 支配が新しい未証明命題 |
| E5 finite certified tail | 有限 block の spectral margin が厳密誤差を上回る | 個別有限 block には有効。全窓・全基底の自動認証にはならない |

## 1. D1: 抽象エネルギー因子分解は何を証明するか

**候補 D1.** ある複素 Hilbert 空間 \(\mathcal K\) と線形写像 \(A:\mathcal D\to\mathcal K\) があり、全 f で \(Q(f)=\|Af\|^2\)。

D1 は直ちに Weil 正値性を与え、RH を含意する。逆に Q が PSD なら、零空間で商を取り Q の内積で完備化すれば D1 が得られる。したがって「適切な Hilbert 空間があるはず」という存在論だけは RH と同値である。

進展と呼べるには、A と \(\mathcal K\) を Q の正値性に依存せずに定義し、元の明示公式と厳密に一致させ、定義域・完備化・境界項を証明する必要がある。\(\langle f,g\rangle:=Q(f,g)\) と宣言して「内積だから正」とするのは循環論法。

\(Q=\|Af\|^2+R(f)\)、\(R\ge0\) も、R の正値性に独立な根拠がなければ同じ問題である。有限行列の Cholesky 分解は、当該行列が PSD と分かった後の結果であって、全サイズの正値性を作り出さない。

## 2. D2: 通常の全実線 L² 上の閉因子分解は成立不能

ここは単なる「未証明」とは異なる、具体的な domain 障害である。

**命題.** \(\mathcal D\subset D(A)\subset L^2(\mathbb R,dx)\) で、A が Hilbert 空間値の closable 線形作用素かつ
\[
Q(f)=\|Af\|^2\qquad(f\in\mathcal D)
\]
を満たすことはない。特に通常の全実線 L² 上の非負自己共役 H による \(Q(f)=\|H^{1/2}f\|^2\) という実現もない。

**背理法。** そのような A があれば Q≥0、既知の Weil 判定法から RH が従う。以下では、この帰結である RH の下で矛盾を得る。

RH の下では全零点パラメータは実数であり
\[
Q(f)=\sum_\rho|F_f(\gamma_\rho)|^2.
\]
一つの零点高度 \(\gamma_0\) とその多重度 \(m_0\ge1\) を固定する。\(\psi\in C_c^\infty\) を \(\int\psi=1\) となるように選び、\(\Psi=F_\psi\)、R≥1 に対して
\[
f_R(x)=R^{-1}\psi(x/R)e^{-i\gamma_0x}
\]
と置く。各 \(f_R\in\mathcal D\) だが support は拡大する。
\[
\|f_R\|_2^2=R^{-1}\|\psi\|_2^2\to0,\qquad
F_{f_R}(\gamma)=\Psi(R(\gamma-\gamma_0)).
\]
\(\Psi(0)=1\)。Schwartz 減衰と重複度込みの零点数評価から、例えば m≥1 について
\[
\sum_\rho(1+|\gamma_\rho-\gamma_0|)^{-2m}<\infty.
\]
R≥1 での一様支配を使った可算和の dominated convergence により、零点評価の \(\ell^2\) ベクトルは、\(\gamma_0\) の多重度ブロックで1、それ以外で0のベクトルへ収束する。従って
\[
Q(f_R)\to m_0>0,\qquad
Q(f_R-f_S)\to0\quad(R,S\to\infty).
\]
仮定より \(Af_R\) は Cauchy、したがってある \(v\ne0\) に収束する。一方 \(f_R\to0\) in L²。これは A の closability の定義に反する。∎

**結論の範囲。** この命題は RH を否定しない。RH を「候補の帰結」として使って、その余分な L²-domain 要求を否定する背理法である。抽象的 Q-Hilbert 完備化、別の重み付き空間、各固定窓の閉形式を否定しない。固定窓では一つの Fourier 評価は L² に有界であり、上記の拡大 support 列は同じ固定窓に入らない。

実際の出発点としては、全実線の無修正 Q に単一の閉 L² 作用素を求めるより、文献の **固定窓の閉形式と Friedrichs 拡張**を使用する方が整合的である。ただし、その局所自己共役性は非負性とは別問題である。

## 3. D3: 正核・素数平行移動・対称性

### 正しい核条件

二変数 kernel K に対して必要なのは、任意の有限点列と係数について
\[
\sum_{j,k}c_j\overline{c_k}K(x_j,x_k)\ge0
\]
という正定値性であり、単なる \(K(x,y)\ge0\) ではない。
\[
K=\begin{pmatrix}1&2\\2&1\end{pmatrix},\qquad
(1,-1)K(1,-1)^T=-2
\]
は実対称、すべての成分が正、交換対称性あり、それでも不定値である。

平行移動不変の正定値分布として Weil 分布を宣言するだけなら Weil criterion の言い換えである。一方、指定した T に対する **独立に既知の非負測度/乗数**への恒等式は有用になり得る。その恒等式が算術項を全て保持しているかを最初に監査すべき。

### 素数平行移動はユニタリでも、その Hermitian 和は正とは限らない

\(\tau_a f(x)=f(x-a)\) とする。\(\tau_a\) は L²-unitary だが
\[
\tau_a+\tau_{-a}
\]
の Fourier symbol は \(2\cos(a\xi)\)。周波数を \(a\xi\approx\pi\) に集めれば負になる。有限周期モデルでも、循環 shift S の \(S+S^*\) は負固有値を持つ。

Weil 明示公式の素数部分は正の係数 \(\Lambda(n)/\sqrt n\) と、符号の定まらない平行移動相関を含む。素数の重みが正であることから、全項がエネルギーになるとは結論できない。

跳躍形式 \(\|\tau_af-f\|^2\) 自体は非負だが
\[
\|\tau_af-f\|^2=2\|f\|^2-2\Re\langle\tau_af,f\rangle
\]
なので、その置換には対角項が伴う。正の平方項だけを残し、対角補正やその発散する正則化を落とすと元の Q ではなくなる。この点は別の算術的恒等式を必要とする。

## 4. D4: ground-state transform の成立条件と誤用

**成立する局所モデル。** \(p>0\)、実 V、\(H=-(p\,d/dx)'+V\) とし、正の十分正則な g が \(Hg=\lambda g\) を満たす。境界項が消える compact test f に対し
\[
q(f)-\lambda\|f\|_2^2
=\int p(x)g(x)^2\left|\left(f/g\right)'(x)\right|^2dx.
\]
これは構造を持つ局所微分形式の恒等式である。積分核型への拡張には、非負の跳躍重みなど、それに代わる構造が必要。

**誤用1: 正の ground state だけから q≥0。**
\[
H=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}
\]
は正成分の ground vector \((1,1)\)、固有値 −1 を持つ。ground state の正値性は ground energy の非負性を保証しない。

**誤用2: 正の固有関数なら最低固有関数。** 上の \(\begin{psmallmatrix}1&2\\2&1\end{psmallmatrix}\) では正の固有vector \((1,1)\) の固有値は3、最低固有値は−1。一般 Hermitian/nonlocal 形式には、Perron–Frobenius 型の順序保存仮定はない。

**誤用3: λ=0 の正解を仮定して核心を解いた扱いにする。** 適切な Schrödinger クラスでは正解/正上解の存在自体が形式の非負性に結びつく。その存在を未証明に置けば正値性を移しただけである。

**精密候補 D4-W。** 各固定窓で Weil 形式を、非負の局所/跳躍エネルギーと制御された potential に一致させ、正関数 \(g_L\) と非負 \(\lambda_L\) を算術情報から独立に構成する。これが全 L で証明できれば RH を含意する。ただし、今のところ局所/跳躍形への一致も \(\lambda_L\ge0\) も未証明。自己共役性のみからはどちらも出ない。

## 5. E3: window の「正残差」は実 Weil 形式でも壊れる

### 変分最小値の単調性は逆方向

\[
\lambda(L)=\inf_{0\ne f\in\mathcal D_L}\frac{Q(f)}{\|f\|_2^2}
\]
と定める。正確な制限の入れ子 \(\mathcal D_{L_1}\subset\mathcal D_{L_2}\) により
\[
L_1<L_2\quad\Longrightarrow\quad\lambda(L_2)\le\lambda(L_1).
\]
有限次元の入れ子でも同じ。有限 Gram 行列を任意の非正規直交 basis で比較するなら、L² Gram に対する一般化 Rayleigh 商を使う必要がある。

局所 positivity の伝播を continuity だけから得ることもできない。Dirichlet 作用素 \(-d^2/dx^2-1\) on \((-L,L)\) では
\[
\lambda_1(L)=\frac{\pi^2}{4L^2}-1
\]
が連続かつ減少し、L=π/2で正から負へ横切る。全 L で正の ground function が存在するが、固有値の符号は保たれない。

### 零拡張による PSD 残差は非零 coupling と両立しない

旧 block A、新方向との coupling b、新 diagonal d の行列を
\[
M_{\rm new}=\begin{pmatrix}A&b\\b^*&d\end{pmatrix}
\]
とする。旧形式を新空間にゼロ拡張すると差は
\[
R=\begin{pmatrix}0&b\\b^*&d\end{pmatrix}.
\]
R が PSD なら b=0 でなければならない。b≠0なら適当な旧方向と新方向の2次元圧縮の determinant は負である。例えば全体が PSD の \(\begin{psmallmatrix}1&1/2\\1/2&1\end{psmallmatrix}\) でさえ、その旧1次元blockとの差は determinant −1/4。

**実 Weil における coupling の明示。** \(a=\log3\)、\(\psi\in C_c^\infty((-1,1);\mathbb R)\)、\(\|\psi\|_2=1\) として
\[
f_\epsilon(x)=\epsilon^{-1/2}\psi(x/\epsilon),\qquad
g_\epsilon(x)=f_\epsilon(x-a).
\]
εを十分小さく取れば \(f_\epsilon\in\mathcal D_1\)、\(g_\epsilon\in\mathcal D_2\) で、その support は \([-1,1]\) と交わらない。

\(h_\epsilon=f_\epsilon*\widetilde g_\epsilon\) は −a 近傍だけに support を持ち、
\[
h_\epsilon(-a)=1,\quad h_\epsilon(0)=0,\quad
\|h_\epsilon\|_1\le\epsilon\|\psi\|_1^2.
\]
εを小さくして他の prime-power 点を除外する。明示公式では −log3 の素数項だけが固定寄与を持つ。pole 項と archimedean kernel はこの原点から離れた compact support 上で有界なので、その積分は O(ε)。従って
\[
Q(f_\epsilon,g_\epsilon)
=-\frac{\log3}{\sqrt3}+O(\epsilon)\ne0.
\]
よって、この2次元空間における「新窓形式−旧窓形式の零拡張」は不定値。

これは RH を仮定せず、Weil 明示公式から導いた **literal な単調残差候補の反例**である。\(Q|_{\mathcal D_2}\) 自体が不定値だという主張ではない。

### 修復候補としての differential control

例えば \(\lambda(L_0)>0\) と、独立に評価した局所可積分 a(L) について
\[
\lambda'(L)\ge-a(L)\lambda(L)
\]
を適切な微分/絶対連続性の下で証明できれば、Gronwall による正値伝播が可能。ただし a を未確定の λ から定義するだけでは循環的であり、\(-d^2-1\) の例では crossing でこの不等式が破れる。Weil 形式に対するそのような算術的相対評価は得られていない。

## 6. E4: Schur complement は修復の正しい位置を示す

A が正定値なら
\[
\begin{pmatrix}A&b\\b^*&d\end{pmatrix}\succeq0
\iff d-b^*A^{-1}b\ge0.
\]
A≥αI、d≥δ、\(\|b\|^2\le\alpha\delta\) を独立に示せれば十分である。これは実行可能な有限 block の目標だが、A>0 と d>0 だけでは不足する。
\[
A=(1),\ b=(2),\ d=1
\quad\Longrightarrow\quad d-b^*A^{-1}b=-3.
\]

A が singular PSD の場合には、さらに \(b\in\operatorname{Ran}A\) と generalized Schur 条件が必要。A=0,b=ε≠0,d=1 はどれほど ε が小さくても不定値である。零固有値を丸めて「ほぼ正」とする帰納は無効。

Weil 形式の固定 support 連続性は \(|Q(f,g)|\le C_Lp_1(f)p_1(g)\) を与えるが、これを \(|Q(f,g)|^2\le Q(f)Q(g)\) に置き換えるのは新しい positivity を仮定することになる。必要なのは p1 に対する上界ではなく、旧エネルギーの逆行列を含む \(b^*A^{-1}b\) の制御である。旧最小固有値が小さいほど条件は悪化する。

**使える構造:** 有限の新方向群について、この Schur 条件を interval arithmetic と解析的 tail で証明すること。**言い換えに留まるもの:** 全 L,N で Schur complement が非負と仮定すること。

## 7. E1/E2: coercivity とゼロへの近づき方

固定 L での正の下界 \(c_L>0\) は局所結果として有用。しかし有限個の L での下界から全 L への結論は出ない。一般の PSD 形式では strict positivity と coercivity も異なる。例 \(\sum_{n\ge1}|x_n|^2/n\) は非零ベクトルで正だが、単位球上の下限は0。

**全実線一様下界は不可能。** 仮に \(Q(f)\ge c\|f\|_2^2\) が全 \(f\in\mathcal D\) に成立する c>0 があれば RH が従う。その下で零点高度ではない実 \(t_0\) を選び、
\[
u_R(x)=R^{-1/2}\psi(x/R)e^{-it_0x}.
\]
\(\|u_R\|_2=\|\psi\|_2\) だが
\[
Q(u_R)=R\sum_\rho|\Psi(R(\gamma_\rho-t_0))|^2\to0.
\]
実際、零点の離散性から \(|\gamma_\rho-t_0|\) は0から離れ、Schwartz 減衰と零点計数により右辺は任意の m≥1 について O(R^{1−2m})。矛盾。

従って、全窓で同じ正の coercivity を維持する修復は棄却する。局所 \(c_L\) の消失を許す必要があり、その消失速度と block/tail の誤差を比較することが残る。

## 8. E5: 有限 certified tail の効力と限界

固定 L,N で
\[
M=M(T)+R(T),\qquad\|R(T)\|_{op}\le E(T)
\]
を保証し、\(\lambda_{\min}(M(T))\ge E(T)\) を保証すれば、正確な M の PSD は証明できる。既存 F6 のこの含意は有効。

ただし \(\operatorname{diag}(1,0)\) に \(\pm\epsilon\operatorname{diag}(0,1)\) を加えた二つの正確な行列は、同じ近似行列・同じ誤差上界を持ち、符号判定は異なる。絶対値の tail 上界だけではゼロ近傍の符号を決められない。

さらに、有限の零点高さ T による \(Q_T\) は有限個の Fourier 評価を経由するので有限 rank。\(\mathcal D_L\) は無限次元だから、非零 f でそれらの評価が全てゼロになるものが存在する。その方向では \(Q_T(f)=0\)。従って、有限 T と対称な絶対 tail 誤差だけから、窓の全関数に正の下界を与えることはできない。tail-nullspace を支配する追加構造が必要である。

既存の誤差上界
\[
E_{L,N}(T)=A_{L,1}^2S_1(T)\sum_{j\le N}p_1(\phi_{L,j})^2
\]
は、L と basis の細かさに依存する。稠密化で細い bump を加えると導関数ノルムが増える。固定 N の T→∞ 収束から、N→∞ と同時に維持される margin は得られない。全 L,N に対して成功する停止時間 T(L,N) を数値的に期待するだけでは、停止性の証明がない。

**別パラメータを区別する。** 文献には特定の有限 Galerkin matrix の **archimedean 積分 cutoff**について、十分高い帯域の tail が PSD になる定理がある。これは零点高さ cutoff の tail、support の拡大、basis 次元の拡大のいずれとも同一ではない。元の matrix 定義・帯域条件・共役規約を照合して初めて使える。

## 9. 一次資料・適用境界

以下は今回、原文で該当 statement を確認したもの。引用論文の全証明・計算証明書を独立に再検証したという意味ではない。

1. **Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, Selecta Math. 27 (2021).** [著者PDF](https://alainconnes.org/wp-content/uploads/Selecta.pdf)、[arXiv:2006.13771](https://arxiv.org/abs/2006.13771)。archimedean の構造から全ての場所の正値性へ移る部分は別問題。Hilbert 空間の存在を全 Weil positivity と混同しない。
2. **Suzuki, *Weil’s quadratic form via the screw function*, arXiv:2606.09096v3, 2026-09-23, PREPRINT.** [固定版](https://arxiv.org/html/2606.09096v3)。Theorem 1.1 は局所作用素の Friedrichs 拡張、Theorem 1.4 は十分小さい窓の正値・単純最低固有値。§2.4 には素数の cosine symbol が現れる。全窓での符号はこれらの局所結果に含まれない。
3. **Pinchover–Tintarev, *A ground state alternative for singular Schrödinger operators*.** [原稿PDF](https://arxiv.org/pdf/math/0411658)。Lemma 2.4, (2.6) は local elliptic form の ground-state identity。Theorem 1.4 は非負性を仮定しているので、これを Q の非負性を新しく導く根拠として逆用しない。PDF の arXiv header と本文の生成日表示は異なるため、定理番号を主な照合位置とした。
4. **Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828v3, 2026-08-14, PREPRINT.** [固定版](https://arxiv.org/html/2607.02828v3)。Theorem 3.2 / Corollary 3.3 の cutoff 順序は、固定 c,N での archimedean cutoff に限る。公開計算 package の独立再実行は未実施。全 support への単調性として引用しない。
5. **Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, arXiv:2608.24827v2, header 2026-09-02 / 本文 2026-09-03, PREPRINT.** [固定版](https://arxiv.org/html/2608.24827v2)。固定窓の有限 block と捨てた方向の coupling を同時に評価する設計は参考になる。局所下界の公表値と計算証明書は本監査では未独立再検証であり、主 proof graph の KNOWN 入力へは昇格させない。以前の版を根拠とする support 拡大主張は採用しない。

書誌注意: 今回返された 2608.24827v1 HTML と v2 HTML は著者表示にも不一致があった。本ノートは v2 の Xuefeng Zhu 表示だけを固定版の書誌として使用し、v1 の著者・数値・拡張範囲から新しい判定を行っていない。

## 10. 残す構造と棄却する短絡

**残す:** 固定窓の閉形式、正確な finite block、Schur complement、basis の L² metric、明示 tail と spectral margin の比較、対象を限定した archimedean tail order。これらは個別局所命題を厳密に証明する道具となる。

**棄却:** Hermitian/対称性だけによる正値性、unitary shift の和の正値性、通常の全実線 L² での閉 \(A^*A\) 実現、support 拡大の正残差、全 support に一様な coercivity、positive ground function だけによる固有値符号、有限高さだけで全窓を閉じる主張。

**核心のまま残るもの:** 全窓の Schur complement または最低固有値を独立した算術構造で非負と制御すること。これを単に仮定するなら RH 同値性の移し替えであり、証明の完成にはならない。

本ノートに RH の新証明はない。閉可能性障害と literal な window 残差の反例は、本リポジトリ内で解析的に導いたルート選別結果であり、文献上の新規性・優先権は主張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/lemmas/finite_to_infinite.md`](../../proofs/lemmas/finite_to_infinite.md)
- [`proofs/lemmas/weil_conventions.md`](../../proofs/lemmas/weil_conventions.md)
