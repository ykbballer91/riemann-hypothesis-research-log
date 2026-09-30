**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/strategy_reset/notes/closure_causality.md` · Original SHA-256: `c4343f838bdbe9bd566c8dd08025bd60b91c945e2177e5a527e54f868564fc57`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Strategy reset：算術 closure、過去側境界、一意性と安定性の分離

2026-09-30。Candidate B の限定監査。新しい証明ルート・位相・計量・作用素を提案しない。旧ファイルは read-only。以下の summation 記号は、指定した関数上での絶対収束和を短く書くために用いる。

**結論：C1/C2、過去 Gaussian class 内の一意性、高次 log-moment の係数正値性は成立する。しかし causality/boundary ⇒ subexponential growth の独立評価は得られない。Candidate B の成功条件は未達（NO independent bound）。** 零点での指数関数を、この class の classical homogeneous solutions と呼ぶ部分は訂正が必要である。

## CC1. C1/C2 の絶対交換

\[
 \phi(u)=e^{-u^2},\quad R(u)=\sum_{n\ge1}\mu(n)\phi(u-\log n),\quad
 A(u)=e^{-u/2}R(u),\quad g(u)=e^{-u^2-u/2}.
 \tag{1}
\]
各 \(u\in\mathbb R\)、\(c>1\) に対して
\[
 \begin{split}
 \sum_{m,n\ge1}|\mu(n)|\phi(u-\log(mn))
 &\le\sum_{k\ge1}d(k)\phi(u-\log k)\\
 &\le e^{cu+c^2/4}\sum_{k\ge1}d(k)k^{-c}
 =e^{cu+c^2/4}\zeta(c)^2<\infty.
 \end{split}                                                   \tag{2}
\]
ここで \(d=\mathbf1*\mathbf1\)、\(*\) は Dirichlet convolution、\(\mathbf1(n)=1\)。compact \(u\)-interval 上で同じ majorant を取れる。微分や有限個の \(\log m,\log n\) の冪も、Gaussian の有限階微分と絶対収束 Dirichlet series に吸収できる。

従って和を交換でき、\(\sum_{n\mid k}\mu(n)=\mathbf1_{k=1}\) から
\[
 \boxed{\sum_{m\ge1}R(u-\log m)=\phi(u).}\qquad\text{C1}
 \tag{3}
\]
\(m^{-1/2}A(u-\log m)=e^{-u/2}R(u-\log m)\) なので
\[
 \boxed{\sum_{m\ge1}m^{-1/2}A(u-\log m)=g(u).}\qquad\text{C2}
 \tag{4}
\]
特にこれらの outer sums 自体も絶対収束する。C1/C2 は正しい arithmetic closure identities であり、有限打切りや RH を必要としない。

## CC2. 自然な過去側 class と明示的逆変換

右側に growth condition を置かず、次の具体的な class を固定する：
\[
 \mathcal P=\left\{f\in C(\mathbb R):
 \exists \eta>0,\ b\ge0,\ C<\infty\quad
 |f(u)|\le C e^{-\eta u^2+b|u|}\ (u\le0)\right\}.
 \tag{5}
\]
これは左側の Gaussian bound と局所有界性だけであり、subexponential stability を定義へ入れていない。新しい norm や completion は導入しない。\(\phi,g,R,A\in\mathcal P\) は (1) と Gaussian majorant から直接従う。
実際の boundary asymptotic は \(R(u)/\phi(u)=A(u)/g(u)=1+O(2^{2u})\) as \(u\to-\infty\)。\(n\ge2\) の項で \(n^{2u}\le2^{2u}\) を使えば得られる。

polynomial growth の算術係数 \(|a(n)|\le C_a n^{B_a}\) に対し
\[
 D_a f(u)=\sum_{n\ge1}a(n)f(u-\log n)
 \tag{6}
\]
は \(\mathcal P\) 上で absolutely/locally uniformly convergent で、\(\mathcal P\) を保つ。実際 \(u\le0,v=\log n\ge0\) なら
\[
 -\eta(u-v)^2+b|u-v|
 \le-\eta u^2+b|u|-\eta v^2+bv.
\]
従って和は \(Ce^{-\eta u^2+b|u|}\sum n^{B_a+b}e^{-\eta(\log n)^2}\) で抑えられる。
固定 positive \(u\) または compact sets については \(u-\log n\le0\) の tail と有限個の項に分ければよい。

二つの polynomial-growth coefficients \(a,b\) に対して、同じ estimate と \(d(k)\le k\) により
\[
 \sum_{m,n}|a(m)b(n)f(u-\log(mn))|<\infty,
 \qquad D_aD_bf=D_{a*b}f.                                  \tag{7}
\]
従って \(\mu*\mathbf1=\varepsilon\)（\(\varepsilon(1)=1\)、他は0）から
\[
 D_\mu D_{\mathbf1}=D_{\mathbf1}D_\mu=I\quad\text{on }\mathcal P.
 \tag{8}
\]
**一意性の量化：任意の \(h\in\mathcal P\) に対し \(D_{\mathbf1}f=h\) を満たす \(f\in\mathcal P\) は唯一で、\(f=D_\mu h\)。**
存在・一意性とも (7)–(8) だけを使い、右側の bound を仮定していない。homogeneous equation の \(\mathcal P\)-solution は0だけ。

normalized 記号
\[
 S_a f(u)=\sum_{n\ge1}a(n)n^{-1/2}f(u-\log n)
          =e^{-u/2}D_a(e^{u/2}f)(u)
 \tag{9}
\]
でも同じ結果が成り立つ。\(e^{\pm u/2}\) は (5) の \(b\) を増やすだけで \(\mathcal P\) を保つ。
従って C2 は \(S_{\mathbf1}A=g\)、その唯一の \(\mathcal P\)-solution は \(S_\mu g=A\)。
これは既存の \(A\) を別の解へ置換していない。

単に \(f(u)\to0\) as \(u\to-\infty\) という境界条件とは区別する。CC5 の homogeneous exponential は左で0へ行くが Gaussian bound は満たさない。「過去側で消える」だけを一意性条件に読み替えない。

## CC3. 零点 exponential は classical homogeneous solution ではない

形式代入したい \(f_z(u)=e^{zu}\) について
\[
 S_{\mathbf1}f_z(u)=e^{zu}\sum_{m\ge1}m^{-1/2-z}
                  =\zeta(1/2+z)e^{zu}
 \tag{10}
\]
を **絶対収束和として**使えるのは \(\Re z>1/2\)。この領域では Euler 積により \(\zeta\ne0\)。
非自明零点 \(\rho\) での \(z=\rho-1/2\) はこの領域にない。
さらに \(0<\Re\rho<1\) では
\[
 \sum_{m\le N}m^{-\rho}
    =\frac{N^{1-\rho}}{1-\rho}+\zeta(\rho)+O_\rho(N^{-\Re\rho})
 \tag{11}
\]
なので、普通の Dirichlet sum は収束しない。(11) は各区間の
\(m^{-s}-\int_m^{m+1}x^{-s}dx=O_s(m^{-\Re s-1})\) を足して得られる。

またどの有限 \(z\) に対しても \(e^{zu}\notin\mathcal P\)。左側で指数減衰しても Gaussian より遅い。
従って \(\zeta(1/2+z)=0\) に基づく「homogeneous zero modes」は **analytically continued symbol の formal modes** であり、(4),(5) の classical solutions ではない。
この区別は、旧 quotient-space の dual zero evaluations が存在するという別の正しい定理を否定しない。

零点 mode を含む無限 residue expansion に (4) の無限和を項別に作用させることも、各 exponential に対する和が既に発散する以上、絶対交換では正当化できない。regularized action を別に定義しても、その domain、境界、元の和との一致は追加の証明義務である。ここでは導入しない。

## CC4. Higher convolutions / log moments / derivatives

### CC4.1. Divisor powers

\(d_r=\mathbf1^{*r}\)、\(d_0=\varepsilon\) とする。固定整数 \(r\ge1\) に対し、(7) から
\[
 S_{\mathbf1}^{\,r}A=S_{d_{r-1}}g.
 \tag{12}
\]
元の同じ \(A\) に何回 closure を作用させても、右辺は一般に0ではなく、\(r>1\) では \(g\) とも異なる。
\(S_{\mathbf1}^{\,r}f=g\) の逆係数は \(\mu^{*r}\) であり、\(r=1\) の \(\mu\) をそのまま使う式ではない。
\(|\mu^{*r}(n)|\le d_r(n)\)、\(\sum d_r(n)n^{-c}=\zeta(c)^r\)（\(c>1\)）が必要な交換を保証する。\(r\) を固定した結果を、\(r\to\infty\) の一様評価としない。

### CC4.2. 二つの log の符号

\(\ell(n)=\log n\) は pointwise arithmetic function、\(\mu\ell\) は pointwise product と区別する。
\[
 \boxed{\mu*\ell=+\Lambda,\qquad (\mu\ell)*\mathbf1=-\Lambda.}
 \tag{13}
\]
第一式は \(\ell=\mathbf1*\Lambda\)。第二式は
\(\delta a(n)=(\log n)a(n)\) の convolution Leibniz rule
\(\delta(a*b)=(\delta a)*b+a*(\delta b)\) を
\(\mu*\mathbf1=\varepsilon\)、\(\delta\varepsilon=0\) に適用したもの。
prime \(p\) では両辺がそれぞれ \(+\log p\)、\(-\log p\) となるので符号も直接点検できる。

### CC4.3. Generalized Mangoldt の genuine coefficient positivity

\(\ell_k(n)=(\log n)^k\)、\(\ell_0=\mathbf1\)、\(\Lambda_k=\mu*\ell_k\) と定める。
\(n>1\) の異なる素因数を \(p_1,\ldots,p_r\)、\(v=\log n\)、\(a_i=\log p_i\) とすると
\[
 \Lambda_k(n)=\sum_{S\subseteq[r]}(-1)^{|S|}
                 \left(v-\sum_{i\in S}a_i\right)^k.
 \tag{14}
\]
\(v\ge\sum_i a_i\) なので finite difference の integral formula から
\[
 \Lambda_k(n)=
 \begin{cases}
 0,&0\le k<r,\\
 \displaystyle\frac{k!}{(k-r)!}
  \int_0^{a_1}\!\cdots\!\int_0^{a_r}
       (v-t_1-\cdots-t_r)^{k-r}dt_1\cdots dt_r\ge0,&k\ge r.
 \end{cases}                                                \tag{15}
\]
\(n=1\) は \(\Lambda_0(1)=1\)、\(\Lambda_k(1)=0\) for \(k\ge1\) と別に扱う。
従って genuine arithmetic constraints として
\[
 \boxed{S_{\ell_k}A(u)=S_{\Lambda_k}g(u)
       =\sum_{n\ge1}\Lambda_k(n)n^{-1/2}g(u-\log n)\ge0}
       \quad(k\ge0,\ u\in\mathbb R)
 \tag{16}
\]
が成立する。これは存在しない正値性として捨ててはいけない。一方、C2 と有限差分の係数代数から導かれるため、独立な subexponential estimate が追加されたという意味ではない。

\(\Re s>1\) で (16) に対応する Dirichlet symbol は
\[
 \sum_n\Lambda_k(n)n^{-s}=\frac{(-1)^k\zeta^{(k)}(s)}{\zeta(s)}.
 \tag{17}
\]
右辺は0ではなく、meromorphic continuation 後には denominator の零点が残り得る。
従って (16) から \(\zeta^{(k)}(\rho)=0\) を要求する推論は成立しない。
全 monomial moments が非負という一般条件だけでも測度正性は出ない：
\(\delta_0-\delta_1+\delta_2\) は0次 moment が1、\(k\ge1\) は \(2^k-1>0\) だが負の atom を持つ。
これは actual \(\mu\) の反例ではなく、その抽象的推論だけへの反例。新たな平方形式の正値性を追加しない。

### CC4.4. Derivative hierarchy

Gaussian の全微分で絶対交換できるので
\[
 S_{\mathbf1}A^{(j)}=g^{(j)}\quad(j\ge0).                  \tag{18}
\]
右辺を消して homogeneous equation にしない。\(u\)-微分と係数 \(\log n\) の挿入も異なる操作である。
一般の係数 Leibniz hierarchy は
\[
 \sum_{j=0}^k\binom kj(\mu\ell_j)*\ell_{k-j}=0\quad(k\ge1),
 \tag{19}
\]
で、(13) は \(k=1\) の場合。個々の summand が0という主張ではない。

## CC5. 有限遅延反例：一意な過去 Gaussian 解にも不安定 poles が残る

固定 \(a>1\)、\(L>0\) とし
\[
 f(u)+a f(u-L)=\phi(u).                                   \tag{20}
\]
解
\[
 f_+(u)=\sum_{j=0}^\infty(-a)^j\phi(u-jL)                 \tag{21}
\]
は Gaussian の \(j^2\) 減衰により absolutely/locally uniformly convergent、全微分も同様。
\(u\le0\) では
\(|f_+(u)|\le e^{-u^2}\sum_{j\ge0}a^j e^{-j^2L^2}\) なので \(f_+\in\mathcal P\)。
さらに \(f_+(u)/\phi(u)=1+O_{a,L}(e^{2Lu})\) as \(u\to-\infty\) であり、forcing と同じ leading Gaussian boundary を保つ。
index shift により (20) が成立する。
二つの \(\mathcal P\)-solutions の差 \(h\) は
\(h(u)=(-a)^N h(u-NL)\)。固定 \(u\) で \(N\to\infty\) とすると Gaussian bound が \(a^N\) を上回り \(h(u)=0\)。
従って (21) は唯一の過去 Gaussian 解。

しかし \(\kappa=(\log a)/L>0\)、\(\Re s>\kappa\) に対し
\[
 \int_{\mathbb R}f_+(u)e^{-su}du
   =\frac{\sqrt\pi e^{s^2/4}}{1+a e^{-Ls}}.                \tag{22}
\]
Fubini の絶対条件は \(\sum_{j\ge0}a^j e^{-jL\Re s}<\infty\) そのもの。
\[
 s_k=\kappa+i(2k+1)\pi/L\quad(k\in\mathbb Z)
\]
は simple poles で、residue は \(\sqrt\pi e^{s_k^2/4}/L\ne0\)。
もし全 \(\varepsilon>0\) で \(f_+(u)=O_\varepsilon(e^{\varepsilon u})\) for \(u\ge0\) なら、左側 Gaussian と合わせて transform は \(\Re s>0\) で正則となり (22) の poles と矛盾する。
**causality + Gaussian past boundary + uniqueness から stability は出ない。**

右側増大をより具体的に見るには
\[
 B(u)=\sum_{j\in\mathbb Z}(-1)^j
           e^{-(u-jL)^2-\kappa(u-jL)}
\]
と置く。これは非零の smooth \(L\)-antiperiodic function、\(B(u+L)=-B(u)\)。
非零性は odd frequencies \(\omega_k=(2k+1)\pi/L\) における Fourier coefficients
\(L^{-1}\sqrt\pi e^{(\kappa+i\omega_k)^2/4}\ne0\) から分かる。
\[
 f_+(u)=e^{\kappa u}B(u)+O_a(e^{-(u+L)^2})\quad(u\ge0).
 \tag{23}
\]
従って適切な算術列 \(u=u_0+2NL\) 上で指数増大する。振動を無視した全点下界は主張しない。

同じ (20) には bounded な別の解
\[
 f_-(u)=\sum_{j=1}^\infty(-1)^{j-1}a^{-j}\phi(u+jL),
 \qquad\|f_-\|_\infty\le1/(a-1)                          \tag{24}
\]
もある。これは未来の値を用いる逆変換であり、\(\mathcal P\) には属さない。
実際、もし属すれば一意性から \(f_-=f_+\) となり (23) と矛盾する。
real-frequency symbol \(1+a e^{-itL}\) は \(|1+a e^{-itL}|\ge a-1>0\) だが、これだけでは (21) を選ばず、(24) のような反対側 inverse を許す。
零点を持たない boundary symbol と、指定した causal inverse の右半平面 regularity は別の要件である。

この模型は actual \(\zeta\) でも actual prime kernel でもない。否定しているのは一般原理「一意な過去側解だから右側は安定」だけ。

## CC6. Renewal tilt と Wiener–Hopf の適用条件

### Infinite mass と符号

C2 の delay measure \(\nu=\sum_{m\ge1}m^{-1/2}\delta_{\log m}\) は locally finite だが総質量は無限。
\(m=1\) を左へ残せば
\(A=g-\sum_{m\ge2}m^{-1/2}A(\cdot-\log m)\)。通常の probability renewal equation の positive feedback とは符号も異なる。

\(A_\sigma(u)=e^{-\sigma u}A(u)\) と tilt すると
\[
 \sum_{m\ge1}m^{-1/2-\sigma}A_\sigma(u-\log m)
            =e^{-\sigma u}g(u).                           \tag{25}
\]
この kernel の総質量が有限となるのは \(\sigma>1/2\) のみ。
同じ域では \(1<c<\sigma+1/2\) を用いた Gaussian の絶対値評価と左側減衰から、実際に \(A_\sigma\) は bounded である。
さらに例えば \(\sigma=3/2\) では off-zero mass は \(\zeta(2)-1<1\) で、bounded forcing に対する elementary Neumann bound が使える。
しかし undo tilt には \(e^{\sigma u}\) が必要。\(A_\sigma\) の boundedness から \(A\) の subexponential bound は出ない。
total mass で規格化して probability と呼んでも、その倍率・符号・forcing を失ってはならない。

### Canonical inverse の選択は growth theorem ではない

Wiener–Hopf の scalar factorization では、指定された半平面で factors **およびその inverses** が正則であること、境界値と無限遠の成長、index が役割を持つ。
actual symbol の \(\zeta(1/2+z)^{-1}\) を \(\Re z>0\) 全域で pole-free に使うなら、まさに RH に必要な zero-free statement を入力している。
境界の factorization が存在するというだけで、CC2 の明示的な過去 inverse が subexponential class に入るとはいえない。(21)/(24) は selection の差を計算可能に示している。

一次資料照合の範囲：

- A. V. Kisil, I. D. Abrahams, G. Mishuris, S. V. Rogosin, [*The Wiener–Hopf technique, its generalizations and applications* (2021), 著者の published manuscript](https://api.repository.cam.ac.uk/server/api/core/bitstreams/12287d6b-ab94-4fbc-8166-d16f94bfcc7f/content), §2(a), pp.3–4, Eqs.(2.2),(2.6)、§2(b), pp.5–6：analytic invertibility、growth、indices の条件を原文確認。この現代の著者による review を読んだ範囲であり、Wiener–Hopf 1931 原版を読んだとはしない。
- S. Lalley, [著者講義録 *Renewal Theory*](https://galton.uchicago.edu/~lalley/Courses/313/RenewalTheory.pdf), §1.2 p.2、§2.2–2.4 pp.5–7、Example 6 p.8：probability step law、右辺、one-sided boundary と tilting の規格化を確認。renewal theorem の仮定を infinite-mass signed equation に移植していない。原著 Feller–Erdős–Pollard 論文は今回未読。

今回の一意性・反例・係数符号は上の直接証明による。外部の抽象 factorization theorem で未確認の domain を埋めない。

## CC7. Candidate B の停止判定

| 問い | 限定的な結論 |
|---|---|
| C1/C2 は actual 全算術で正しいか | YES、(2) の絶対交換 |
| 自然な過去 Gaussian 境界で canonical solution を一意に選べるか | YES、Möbius inversion (8) |
| その class に off-line classical homogeneous exponentials が残るか | NO、そもそも exponential は class 外で、零点での series も発散 |
| 高次 log closures に正の情報はあるか | YES、\(\Lambda_k\ge0\) と (16)。消去せず記録 |
| 一意性・因果性・positive moments だけで actual \(A\) の subexponential bound を得たか | NO |
| finite-delay toy は RH の反例か | NO、一般的な causality⇒stability 推論のみを反証 |

残る最小の算術的評価は、同じ \(A=S_\mu g\) に対する
\[
 \forall\varepsilon>0\ \exists C_\varepsilon\quad
 |A(u)|\le C_\varepsilon e^{\varepsilon u}\quad(u\ge0).
\]
既存 Global Remainder track でこれは RH 同値と確認済み。C1/C2 の一意性をこの評価の証明へ昇格しない。
**Candidate B は既知の厳密恒等式・canonical selection として保存するが、独立な closure/stability 入力を供給する候補としては未成立。今回ここで停止する。**
