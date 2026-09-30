**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/weighted_prime_halfspace/notes/finite_difference_boolean.md` · Original SHA-256: `616b0214935280eae5be0b7d49dfcb183a55bbb52d064cbe3fea4a60d7849823`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weighted prime halfspace：有限差分・Boolean parity の厳密な範囲

2026-09-30。旧ファイルは変更しない。正の重み \(\lambda_1,\ldots,\lambda_m\) と threshold \(L\) について、有限差分の構造、一般の最良境界、算術固有の不足を分離する。新規性を主張しない。RH は OPEN。正負の状態を対応させる state-count pairing は用いない。

## FD1. Translation の符号と exact recurrence

\(\tau_a f(u)=f(u-a)\)、\(J(u)=\mathbf1_{u\ge0}\)、\(H_L(u)=\mathbf1_{u\le L}\) と定める。empty subset を含めて
\[
 F_m(L)=\sum_{S\subseteq[m]}(-1)^{|S|}
             \mathbf1_{\sum_{i\in S}\lambda_i\le L}.
\]
正しい二つの有限差分表示は
\[
 \boxed{F_m(L)=\Bigl[\prod_{i=1}^m(I-\tau_{\lambda_i})J\Bigr](L)
             =\Bigl[\prod_{i=1}^m(I-\tau_{-\lambda_i})H_L\Bigr](0).}
 \tag{1}
\]
後者に \(\tau_{+\lambda_i}\) を入れると \(H_L\) の引数は負の subset sum になり、目的の式ではなくなる。

\(F_0(L)=J(L)\) から、任意の重み順序で
\[
 \boxed{F_k(L)=F_{k-1}(L)-F_{k-1}(L-\lambda_k).}
 \tag{2}
\]
互いに素な index blocks \(A,B\) についても
\[
 F_{A\cup B}(L)=\sum_{S\subseteq B}(-1)^{|S|}
                    F_A\left(L-\sum_{i\in S}\lambda_i\right).
 \tag{3}
\]
これは signed convolution の結合則である。一般に右辺の各項が小さくなる、または独立になるとは述べていない。

\(m\ge1\) では \(L<0\) と \(L\ge\sum_i\lambda_i\) で \(F_m(L)=0\)。従って distribution の support は \([0,\sum_i\lambda_i]\) に含まれ、右端での点値は0である。actual \(P=\{p\le X\}\) ではこの区間の幅は \(\vartheta(X)=\sum_{p\le X}\log p\)（既知の prime number theorem により \(\vartheta(X)\sim X\)）。算術 readout \(L=\log X\) はこの全幅よりずっと小さい。広い support の記述だけでは、readout での局所的 cancellation は制御されない。

## FD2. Peano box integral と spline の次数

\(f\in C^m(\mathbb R)\) に対し fundamental theorem of calculus を \(m\) 回使うと
\[
 \prod_{i=1}^m(I-\tau_{\lambda_i})f(L)
 =\int_0^{\lambda_1}\cdots\int_0^{\lambda_m}
            f^{(m)}(L-t_1-\cdots-t_m)dt_1\cdots dt_m.
 \tag{4}
\]
従って使える直接評価は
\[
 |\Delta_{\lambda_1}\cdots\Delta_{\lambda_m}f(L)|
       \le\left(\prod_i\lambda_i\right)\|f^{(m)}\|_\infty.
 \tag{5}
\]
逆符号の translation を \(f(0)\) に作用させる表示では、右辺は \((-1)^m\int f^{(m)}(t_1+\cdots+t_m)dt\) となる。

\[
 B_{\boldsymbol\lambda}
   =\mathbf1_{[0,\lambda_1]}*\cdots*\mathbf1_{[0,\lambda_m]},\qquad
 b_{\boldsymbol\lambda}=B_{\boldsymbol\lambda}/\prod_i\lambda_i
\]
とすると、\(b\) は独立一様変数 \(U_i\sim\mathrm{Unif}[0,\lambda_i]\) の和の probability density。積分は1、分散は \(\sum_i\lambda_i^2/12\)。\(B\) は一変数 box spline で、equal weights のとき cardinal B-spline の尺度変更となる。

\(m\ge1\) について distribution の意味で
\[
 \begin{split}
 B_{\boldsymbol\lambda}(L)
  &=\frac1{(m-1)!}\sum_{S\subseteq[m]}(-1)^{|S|}
                   (L-\lambda(S))_+^{m-1},\\
 F_m&=D^{m-1}B_{\boldsymbol\lambda},\qquad
 D F_m=\mathop{*}_{i=1}^m(\delta_0-\delta_{\lambda_i}).
 \end{split}                                                \tag{6}
\]
最初の式は \(m\) 回微分した後の delta measure と、左端での vanishing 条件からも検証できる。jump point での代表値は (1) の右連続規約を採用する。

**正の spline 自体が目的量なのではない。** 目的量はその \((m-1)\) 階導関数であり、\(m\) とともに微分次数も増える。例えば step を \(\eta_h*J\) で smooth にすると (5) は
\[
 |\Delta_{\boldsymbol\lambda}(\eta_h*J)(L)|
 \le\left(\prod_i\lambda_i\right)h^{-m}\|\eta^{(m-1)}\|_\infty
 \tag{7}
\]
となる。固定微分次数の smoothness estimate を任意の \(m\) に流用できない。

## FD3. Total variation と標準 norm での非収縮

subset sums が相異なるとき、(6) の derivative measure は相異なる \(2^m\) 点に質量 \(\pm1\) を持つ。よって
\[
 \operatorname{Var}_{\mathbb R}(F_m)=\|D F_m\|_{TV}=2^m.
 \tag{8}
\]
実際の \(\lambda_i=\log p_i\) では素因数分解の一意性からこの仮定が成立する。collisions のある一般の重みでは \(\|D F_m\|_{TV}\le2^m\) であり、同じ点に来た符号を合計してから variation を取る。

標準 \(L^\infty(\mathbb R)\) 上では \(\|I-\tau_a\|\le2\)、従って product norm は高々 \(2^m\)。相異なる subset sums がある場合は **exact に \(2^m\)** である。固定 \(L\) に対し点 \(L-\lambda(S)\) の周囲に disjoint smooth bumps を置き、そこで \(f=(-1)^{|S|}\)、\(\|f\|_\infty=1\) とすれば、有限差分の値は \(2^m\)。\(f\in C_c^\infty\) でも達成できる。

標準 \(L^2(\mathbb R)\) 上の Fourier multiplier は \(\prod_i(1-e^{-it\lambda_i})\)。重みが \(\mathbb Q\)-linearly independent なら continuous Kronecker flow により全位相を \(-1\) へ同時に任意に近づけられるので、operator norm はここでも \(2^m\)。特に actual prime logs に当てはまる。従って有限差分作用素そのものを標準 norm の contraction として使うことはできない。別の norm を結果に合わせて定義しない。

## FD4. 全 parity coefficient の sharp bound：任意の downset

\(m\ge1\)。\(D\subseteq\{0,1\}^m\) が coordinatewise downset とする。positive weighted threshold はこの条件を満たす。
\[
 a_r=\#\{x\in D:|x|=r\},\qquad q_r=\frac{a_r}{\binom mr}
       \quad(0\le r\le m).
\]
隣接二層の incidence を数えると
\[
 (r+1)a_{r+1}\le(m-r)a_r,\qquad
 1\ge q_0\ge q_1\ge\cdots\ge q_m\ge0.                       \tag{9}
\]
理由は、\(D\) の各 \((r+1)\)-subset の全ての \(r\)-subsets が \(D\) に入り、一方各 \(r\)-subset の上方 extensions は高々 \(m-r\) 個だから。この normalized layer inequality は正負 parity の状態を対応させる議論ではない。

\(q_{m+1}=0\)、\(p_j=q_j-q_{j+1}\ge0\) を \(j=0,\ldots,m\) で定める。\(\sum_{j=0}^m p_j=q_0\le1\)。有限和を入れ替えると
\[
 \begin{split}
 \sum_{x\in D}(-1)^{|x|}
 &=\sum_{r=0}^m(-1)^r\binom mr q_r\\
 &=\sum_{j=0}^m p_j\sum_{r=0}^j(-1)^r\binom mr\\
 &=\sum_{j=0}^{m-1}p_j(-1)^j\binom{m-1}{j}.
 \end{split}                                                \tag{10}
\]
最後の恒等式は Pascal identity、\(j=m\) の交代和は0。注意すべき mass は \(\sum_{j<m}p_j=q_0-q_m\le1\) であり、一般には \(q_0\) と等しくない。

従って
\[
 \boxed{\left|\sum_{x\in D}(-1)^{|x|}\right|
 \le\binom{m-1}{\lfloor(m-1)/2\rfloor}.}
 \tag{11}
\]
これは sharp。\(D=\{|x|\le j\}\)、\(j=\lfloor(m-1)/2\rfloor\) では (10) の一項だけが残り等号となる。equal weights \(\lambda_i=1\)、\(L=j+1/2\) がこの threshold を実現する。

uniform Boolean probability measure と \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) を使うと、\(f=\mathbf1_D\) の Fourier coefficient は
\[
 \widehat f([m])=2^{-m}F_m(L),\qquad
 |\widehat f([m])|\le2^{-m}\binom{m-1}{\lfloor(m-1)/2\rfloor}
          \sim\frac1{\sqrt{2\pi m}}.                         \tag{12}
\]
これは **normalized** coefficient の減衰である。未正規化和は \(2^m/\sqrt m\) の規模を達成する。factor \(2^m\) を失って算術和の改善と呼ばない。\(m=0\) は別に \(F_0=J\) と扱う。

## FD5. 固定 \(m\) の例と irrational perturbation

equal weights 1 のとき、\(L\in[j,j+1)\)、\(0\le j<m\) で
\(F_m(L)=(-1)^j\binom{m-1}{j}\)。\(L<0\) と \(L\ge m\) では0。小例は

| \(m\) | \([0,1),[1,2),\ldots,[m-1,m)\) 上の値 | 最大絶対値 |
|---:|---|---:|
| 1 | \(1\) | 1 |
| 2 | \(1,-1\) | 1 |
| 3 | \(1,-2,1\) | 2 |
| 4 | \(1,-3,3,-1\) | 3 |

equal weights の衝突を除いても extremum は残る。\(\tau\in(0,1)\) を transcendental、\(\varepsilon>0\) を rational かつ \(m\varepsilon<1/2\) とし
\[
 \lambda_i=1+\varepsilon\tau^i\quad(1\le i\le m),\qquad L=j+1/2.
 \tag{13}
\]
\(|S|\le j\) なら \(\lambda(S)<j+1/2\)、\(|S|\ge j+1\) なら \(\lambda(S)>j+1/2\)。従って Boolean function は同じ cardinality threshold で、(11) の等号がそのまま成立する。

また \(\sum_i c_i\lambda_i=0\)、\(c_i\in\mathbb Q\) は \(\sum_i c_i+\varepsilon\sum_i c_i\tau^i=0\) を与える。transcendence から全 \(c_i=0\)。従って rational independence、distinct subset sums、任意に小さい equal-weight perturbation を同時に満たす。**irrationality だけでは (11) を改善できない。** これは一般重みの反例であり、actual prime logs がこの等号配置を持つと主張したものではない。

## FD6. Influence・noise・hypercontractivity の係数監査

\(f:\{0,1\}^m\to\{0,1\}\) に対し
\[
 I_i=\Pr(f(x)\ne f(x\oplus e_i)),\qquad
 \delta_i f(x_{-i})=\tfrac12(f(x_i=0)-f(x_i=1)).
\]
uniform Fourier normalization では
\[
 I_i=4\sum_{S\ni i}|\widehat f(S)|^2,\qquad
 \widehat f([m])=\mathbb E_{x_{-i}}\delta_i f(x_{-i})\chi_{[m]\setminus i}(x).
 \tag{14}
\]
\(\{0,1\}\)-valued のため factor4が必要。decreasing monotone \(f\) なら \(\delta_i f\ge0\)、\(\mathbb E\delta_i f=I_i/2\) なので
\[
 |\widehat f([m])|\le I_i/2,\qquad
 |F_m(L)|\le2^{m-1}\min_i I_i.
 \tag{15}
\]
cardinality threshold \(|x|\le j\) では全 \(i\) に対し \(I_i=2^{-(m-1)}\binom{m-1}{j}\) で (15) は等号。小 influence だけから未正規化和の余分な指数利得は出ない。

standard noise operator は
\(T_\rho f=\sum_S\rho^{|S|}\widehat f(S)\chi_S\)、\(0\le\rho\le1\)。従って
\[
 \widehat{T_\rho f}([m])=\rho^m\widehat f([m]).               \tag{16}
\]
Bonami の hypercontractivity は uniform probability norms で
\[
 \|T_\rho f\|_q\le\|f\|_p,
 \qquad1<p\le q<\infty,\quad(q-1)\rho^2\le p-1.
 \tag{17}
\]
例えば \(q=2,p=1+\rho^2\)、\(\alpha=\mathbb Ef\) なら
\[
 |F_m(L)|\le2^m\rho^{-m}\alpha^{1/(1+\rho^2)}\quad(\rho>0).
 \tag{18}
\]
小さな \(\rho^m\) を gain として用いる場合、original coefficient へ戻す \(\rho^{-m}\) を省けない。noise は observable を変更し、(17) だけで original parity sum の新しい bound は出ない。

## FD7. Martingale と order averaging の gate

座標順序 \(\pi\) に対し \(M_j=\mathbb E[f\mid x_{\pi(1)},\ldots,x_{\pi(j)}]\)、\(D_j=M_j-M_{j-1}\) とする。Fourier 展開では \(M_j\) に現れるのは revealed coordinates の subsets だけ。従って
\[
 \mathbb E[D_j\chi_{[m]}]=0\ (j<m),\qquad
 \widehat f([m])=\mathbb E[D_m\chi_{[m]}]
 \tag{19}
\]
である。全次数の coefficient は最後まで現れない。順序を平均しても、全ての順序が同じ coefficient を返す。

最後の座標を平均する形では (14) から
\[
 \widehat f([m])=\frac1m\sum_{i=1}^m
      \mathbb E_{x_{-i}}\delta_i f\chi_{[m]\setminus i},\qquad
 |F_m(L)|\le\frac{2^{m-1}}m\sum_i I_i.                     \tag{20}
\]
cardinality threshold では右の全 \(m\) 項が同符号・同絶対値を持ち、(20) も等号。順序平均を独立標本平均とみなして \(m^{-1/2}\) や \((m!)^{-1/2}\) を追加する推論は、この threshold と (13) の independent-weight 例で反証される。martingale の分散分解は有効だが、全次数への算術固有の追加条件を供給しない。

### FD7.1. 反集中・threshold degree・spline から移せない結論

Littlewood–Offord 型の反集中は、短い区間へ入る **符号を付ける前の個数または確率** を評価する。例えば Erdős の Theorem 1 は、実数 \(|a_i|\ge1\) に対し \(\sum_i\varepsilon_i a_i\)（\(\varepsilon_i\in\{-1,1\}\)）が長さ2の **開区間** に入る個数を \(\binom m{\lfloor m/2\rfloor}\) で抑える。必要な重みの下限、区間幅、端点規約を保たねばならない。この種の unsigned shell bound を (14) に使うことはできるが、shell 内の parity に新しい cancellation を生まない。FD4 の central-binomial bound も一般 downset の次元依存評価であって、actual prime logs の signed arithmetic estimate ではない。

weighted threshold の threshold degree が1という意味は「一次多項式の **符号** で表現できる」であり、Boolean Fourier degree が1という意味ではない。FD5 の equal-weight 例では最高次数係数が (12) の等号を達成する。symmetric functions を Krawtchouk basis へ落とす方法も、equal-weight cardinality threshold には適用できるが、一般の異なる重みでは関数が座標交換に不変ではない。従って同じ一変数化を actual prime weights に適用する追加根拠はない。

spline の total positivity または variation-diminishing theorem は、各定理の仮定を満たす場合でも、それだけで \(D^{m-1}B_{\boldsymbol\lambda}\) の振幅や \(m\) に一様な評価定数を与えない。ここでは任意の unequal-box convolution を \(PF_\infty\) と仮定せず、(6) の明示式と (8) の variation を使う。正の spline の存在と目的の高階導関数の小ささを同一視しない。

## FD8. Actual large-prime block：multiplicity を保持する

\(A_{\le Y}(L)=\sum_{n\ {m squarefree},\,p\mid n\Rightarrow p\le Y}
                 \mu(n)\mathbf1_{n\le e^L}\) とする。\(X\ge1\)、\(\sqrt X\le Y\le X\) なら、\(n\le X\) は \(Y\) より大きい素因数を高々一つ持つ。従って exact block decomposition は
\[
 \boxed{M(X)=A_{\le Y}(\log X)
           -\sum_{Y<p\le X}A_{\le Y}(\log(X/p)).}
 \tag{21}
\]
\(p>Y\) では \(X/p<X/Y\le Y\) なので内側 cutoff は full \(M(X/p)\) に一致する。cofactor ごとに有限和を交換すれば
\[
 \boxed{M(X)=A_{\le Y}(\log X)
       -\sum_{r\le X/Y}\mu(r)\bigl(\pi(X/r)-\pi(Y)\bigr).}
 \tag{22}
\]
endpoint \(r=X/Y\) では括弧は0。重複係数 \(\pi(X/r)-\pi(Y)\) は同じ cofactor に付く大素数の個数であり、各 cofactor を一回だけに数え直してはいけない。\(Y<\sqrt X\) では二個以上の large primes の項も存在し、(21) の二項形式は一般に偽；その場合は (3) の全 block subsets を保持する。

例として \(X=10,Y=\sqrt{10}\) では \(A_{\le Y}(\log X)=1-1-1+1=0\)。\(r=1\) の multiplicity は2（素数5,7）、\(r=2\) は1（素数5）、\(r=3\) は0。従って (22) は \(M(10)=0-(2-1)=-1\)。multiplicity を全部1へ潰した式ではこの計算を保持できない。

この再帰は actual prime logs と Möbius 係数を保持するが、\(\mu(r)\) と prime-count weight の相関評価を自動的に与えない。nonnegative な multiplicity を得たこと自体は、その signed sum の平方根 cancellation の証明ではない。

## FD9. 一次照合、独立検算、判定

- D. N. Kozlov, [*Convex Hulls of f- and β-Vectors* (1997), DOI](https://doi.org/10.1007/PL00009326), Theorem 4.1 と §5, pp.429–430：normalized layer densities の単調性と skeleton vectors の convex hull。FD4 は同じ既知構造から parity functional の extremum を直接計算したもの。[原論文 PDF の転載](https://scispace.com/pdf/convex-hulls-of-f-and-b-vectors-4pmf8cxdk7.pdf)で本文を確認した。
- Paul Erdős, [*On a Lemma of Littlewood and Offord* (1945)](https://www.renyi.hu/~p_erdos/1945-04.pdf), Theorem 1, p.898：実重みの下限と開区間の幅を指定した unsigned concentration bound。FD7.1 ではこの範囲だけを使う。
- Aline Bonami, [*Étude des coefficients de Fourier des fonctions de Lᵖ(G)* (1970)](https://www.numdam.org/item/10.5802/aif.357.pdf), chapitre III, Théorème 2 と Théorème 3, pp.374–376：tensorization と \((q-1)\rho^2\le p-1\) の二点群 noise multiplier。原文を確認した。
- Ryan O’Donnell, [*Analysis of Boolean Functions*, 著者公開版](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), Chapters 2, 5, 9–10、特に Chapter 5 の linear threshold functions と §10.1 p.284 の uniform noise normalization。本文の一般 product-space 版を、別の確率測度へ無条件に適用していない。
- DESTROYER は FD4 の全 downset bound、\(p_m\) の mass に関する例外、FD5 の transcendental perturbation を独立検算して PASS。有限差分・prime block は本ノートに直接導出を記載した。原論文全体の再検証は主張しない。

**Decision:** exact finite-difference / spline identities、sharp universal parity bound、actual large-prime recursion を保持する。一般重みの irrationality、positive spline、noise contraction、martingale order averaging だけでより強い arithmetic cancellation を得る候補は、上記の係数・extremizer・復元費用により止める。actual prime-log weights に特有の追加評価は未証明であり、一般重みの反例をその不可能性と呼ばない。RH は OPEN。
