**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/support-propagation-adversarial.md` · Original SHA-256: `6a0b74a8dd3822da58862da81c87a5d1993f68b57f28aa4648d0c539191d57cd`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Support propagation の敵対監査

2026-09-29。担当 DESTROYER。RH は OPEN。固定窓を拡張して数値認証する作業は停止し、本稿では inner/shell 分割による一般推論だけを監査する。有限 toy matrix の反例と、実 Weil 形式の非零 cross 項を混同しない。

**結論。** 内側の正値性だけでは、任意の指定幅まで support を拡張できない。厳密な gap から十分小さい幅への局所延長は可能だが、全窓への伝播を保証しない。coercivity が失われる場合、裸の逆作用素ではなく relative coupling の制御が必要。Schur complement の正値性を追加仮定するだけなら、次の窓の正値性の言い換えであり、その候補はそこで停止する。全ての別種の算術的 propagation theorem が不可能だとは主張しない。

## 1. 有限ブロックの正しい必要十分条件

まず domain の問題がない有限次元で

$$
M=\begin{pmatrix}A&B\\ B^*&C\end{pmatrix},\qquad A\succ0
$$

とする。実二次形式でも複素 Hermitian 形式でも

$$
\langle M(x,y),(x,y)\rangle
=\|A^{1/2}x+A^{-1/2}By\|^2
 +\langle (C-B^*A^{-1}B)y,y\rangle.
$$

従って

$$
M\succeq0\quad\Longleftrightarrow\quad
S:=C-B^*A^{-1}B\succeq0.
$$

内側 $A$ だけでなく、外側 $C$ 自体が正でも不十分。最小の反例は

$$
A=C=(1),\quad B=(2),\quad
M=\begin{pmatrix}1&2\\2&1\end{pmatrix},\quad
S=-3,\quad M(1,-1)^t=-(1,-1)^t.
$$

従って「内側・shell は各々正なので union も正」は FALSE。これは実 Weil 形式がこの行列になるという主張ではない。

## 2. 小さい gap と relative coupling は区別する

$$
M_{\varepsilon,b}=
\begin{pmatrix}\varepsilon&b\\b&1\end{pmatrix}
$$

なら $A^{-1}=\varepsilon^{-1}$、Schur complement は $1-b^2/\varepsilon$。
例えば $b=1/2,\ \varepsilon=1/16$ では $S=-3$。絶対的な cross bound $|b|\le1/2$ は、内側 gap が縮む時に十分でなくなる。

しかし逆ノルムの発散だけから propagation の不可能性も言えない。

$$
b=\kappa\sqrt\varepsilon
\quad\Longrightarrow\quad S=1-\kappa^2.
$$

$|\kappa|\le1$ なら任意の $\varepsilon>0$ で PSD。$|\kappa|<1$ でも最小固有値は $\varepsilon\to0$ で $0$ に向かうが、正性は保存される。

無限次元版も具体的である。$H=\ell^2$、$A e_n=n^{-2}e_n$、$B=\kappa A^{1/2}$、$C=I$ とすれば

$$
\langle M(x,y),(x,y)\rangle
=\|A^{1/2}x+\kappa y\|^2+(1-\kappa^2)\|y\|^2.
$$

$A^{-1}$ は非有界でも、$A^{-1/2}B=\kappa I$ は有界。$|\kappa|\le1$ で全体は PSD。従って有用な候補は裸の $\|A^{-1}\|\|B\|^2$ だけでなく、例えば

$$
\|A^{-1/2}BC^{-1/2}\|\le\kappa\le1
$$

という相対評価である。ただし $C^{-1/2}$ の定義域、range と全積の有界延長まで証明する必要がある。この不等式を Weil の全窓で仮定しただけでは新しい証明にならない。

## 3. 有限 Schur の記号を無限次元へ移す際の反例

### 3.1 Range 条件が破れる rank-one coupling

再び $A e_n=n^{-2}e_n$ とし、shell は $\mathbb C$、$B y=yb$、$b_n=1/n$ とする。$b\in\ell^2$ なので $B$ と

$$
M=\begin{pmatrix}A&B\\B^*&c\end{pmatrix}
$$

は有界である。しかし $A^{-1/2}b=(1,1,\ldots)\notin\ell^2$。

任意の有限の $c$ に対して、$y=1$ と
$x_n=-n$ for $n\le N$、それ以外 $0$ を選ぶと

$$
\langle M(x,1),(x,1)\rangle=c-N.
$$

従って $N>c$ で厳密に負。全有限 inner block は正でも、shell 一つとの相互作用を有限の $c$ で吸収できない。有限 Schur の値 $c-N$ はその障害を直接示す。

### 3.2 $A^{-1}B$ が未定義でも形式の正値性は成立し得る

今度は $b_n=1/n^2$、$v_n=1/n$、$c=\sum_{n\ge1}1/n^2<\infty$ とする。$b=A^{1/2}v$ なので

$$
\langle M(x,y),(x,y)\rangle=\|A^{1/2}x+yv\|^2\ge0.
$$

一方 $A^{-1}b=(1,1,\ldots)\notin\ell^2$。従って
$x+A^{-1}By$ を Hilbert 空間の元として扱う平方完成は無意味である。
正しい形式レベルの量は
$\|A^{-1/2}b\|^2=\|v\|^2=c$。
固定した $y\ne0$ の infimum は $0$ だが、その実現には $x_n=-y$ が必要なので $\ell^2$ 内では達成されない。

この例は「inverse が書けないから PSD も不可能」という逆の誤推論も否定する。operator Schur と form Schur を区別する必要がある。

### 3.3 Kernel の条件も必要

$A\succeq0$ に kernel がある場合、PSD な全体には $B^*\ker A=\{0\}$ が必要。
そうでなければ kernel 内の $x$ の倍率・位相を変えるだけで cross 項を負に発散させられる。
$A=0,B=1,C=1$ は最小反例。Moore–Penrose inverse を形式的に $A^\dagger=0$ とし、$C-B^*A^\dagger B=1$ だけを見る判定は誤りである。

一般の非有界な形式では、さらに共通の form domain、閉性、inner/shell 射影が domain を保存するか、cross form の連続性を確認する必要がある。support の集合分割だけで、これらの解析的条件を自動的に得たことにはならない。

## 4. 実 Weil 形式では zero-extension increment が既に不定

これは有限 toy model でなく実際の明示公式からの限定反証。
$a_0=\log3$、実数値 $\psi\in C_c^\infty(-1,1)$、$\|\psi\|_2=1$ とし

$$
f_\epsilon(x)=\epsilon^{-1/2}\psi(x/\epsilon),\qquad
g_\epsilon(x)=f_\epsilon(x-a_0).
$$

十分小さい $\epsilon$ では $f_\epsilon$ は旧窓 $[-1,1]$、$g_\epsilon$ は shell $(1,2)$ に支持を持つ。自己相関を $-\log3$ の周囲へ局在させると

$$
b_\epsilon:=Q_W(f_\epsilon,g_\epsilon)
=-\frac{\log3}{\sqrt3}+O(\epsilon)\ne0.
$$

素数 3 の寄与だけが残り、archimedean と pole の cross kernel はその近傍で滑らかなので残りは $O(\epsilon)$。既存の [structural_heuristics.md E2](../../../reports/research/structural_heuristics.md) の解析評価では $0<\epsilon\le1/64$ に対し

$$
\left|b_\epsilon+\frac{\log3}{\sqrt3}\right|\le7\epsilon,
\qquad |b_\epsilon|>25/64.
$$

旧形式を shell に零として延長したものと、新窓形式との差は、この二方向上で

$$
\Delta=\begin{pmatrix}0&b_\epsilon\\
\overline{b_\epsilon}&d_\epsilon\end{pmatrix},
\qquad \det\Delta=-|b_\epsilon|^2<0.
$$

従って「窓を増やす exact increment が PSD」という候補は FALSE。$Q_W$ 自体の負方向を構成したわけではない。元の inner diagonal を戻した full block が正である可能性は残る。

この障害は shell diagonal だけの補正では消えない。任意の有限の $D$ に対して

$$
\det\begin{pmatrix}0&b_\epsilon\\
\overline{b_\epsilon}&d_\epsilon+D\end{pmatrix}
=-|b_\epsilon|^2.
$$

old block を厳密に保存しながら、この意味の increment を正にすることはできない。

## 5. Canonical renormalization と archimedean tail order

「canonical」という名称には符号保存の数学的効力がない。何を変えるかを区別する。

- **有界可逆な座標変更・congruence:** 元の quadratic form と同じなら負方向は変換されて残る。Schur の三角消去そのものも負性を消さない。
- **shell diagonal への加算:** full block を改善できる場合はあるが、必要量は $D\succeq B^*A^{-1}B-C$。その評価が本体である。例えば $A=C=1,B=2$ では $D\ge3$ が必要。単に $D>0$ では足りない。
- **加えた量を別の場所で引く exact renormalization:** 元の form を保つなら、引いた側の符号も計上する必要がある。正項だけを残した判定は別問題になる。
- **archimedean height tail の PSD:** 固定 support・固定 finite basis での tail order は、support の追加という操作とは別である。正の補正として使う場合も、同一のブロック規約、重複計上のない恒等式、補正量の下界が必要。

Groskin 型の archimedean tail positivity だけでは、prime coupling が zero になるとも、Schur cost を必ず上回るとも言えない。前節の exact support increment には旧 block が厳密に零という制約があり、同じ increment を PSD と同定することは非零 cross 項に反する。

一方、十分大きい適切な正の補正が full block の Schur を改善する可能性までは否定していない。その補正が実 Weil 形式の一部であることと、必要な量を全 support で確保できることを独立に証明する必要がある。

## 6. 候補の停止基準と残る構造

各 support step に対して単に

$$
P_L:\quad C_L-B_L^*A_L^{-1}B_L\succeq0
$$

を「propagation lemma」と呼ぶ候補は、inverse の仮定が満たされる範囲で新窓の正値性と同値である。これを前提にして positivity を帰納するだけなら未証明部分を移したにすぎないため、候補はここで停止する。全ての窓での positivity は Weil criterion により RH 同値で、未解決。

有用な構造となり得るのは、既存 positivity を前提にしない、具体的な kernel・素数項・geometry からの relative coupling bound、shell 下界、適切な domain theorem である。本稿はその成立を仮定せず、全て不可能だとも主張しない。

## 7. Sharp support projection の domain 問題は解決できる

上の注意のうち、実 Weil 形式の log Fourier domain が interval の characteristic multiplier で保存されるか、という点には初等な肯定証明がある。これは正値性を仮定しない。

$P_a f=1_{[-a,a]}f$ とし、unitary Fourier 側で $K_a=\mathcal F P_a\mathcal F^{-1}$ と置く。その kernel は

$$
K_a(t,s)=\frac{\sin(a(t-s))}{\pi(t-s)},\qquad \|K_a\|_{L^2\to L^2}\le1.
$$

対角では可除特異点を連続延長する。周波数集合

$$
E_0=\{|t|<2\},\qquad E_j=\{2^j\le|t|<2^{j+1}\}\quad(j\ge1)
$$

とその直交射影 $D_j$ を取る。$|j-k|\ge2$ では
両集合の距離は $2^{\max(j,k)-1}$ 以上、測度は $O(2^j),O(2^k)$。
$|\sin(a(t-s))|\le1$ と Hilbert–Schmidt 評価から

$$
\|D_jK_aD_k\|\le C2^{-|j-k|/2}.
$$

隣接 block は全作用素のノルムから $\le1$。
従って全 $j,k$ に対し summable な数列
$d_m=C'2^{-|m|/2}$ を使って $\|D_jK_aD_k\|\le d_{j-k}$ とできる。

log 重みノルムは

$$
\int\log(2+|t|)|F(t)|^2dt
\asymp\sum_{j\ge0}(j+1)\|D_jF\|_2^2
$$

であり、
$\sqrt{(j+1)/(k+1)}\le\sqrt{1+|j-k|}$。
有限 dyadic sums に対し三角不等式と discrete Young inequality を適用すると

$$
\left(\sum_j(j+1)\|D_jK_aF\|_2^2\right)^{1/2}
\le
\left(\sum_{m\in\mathbb Z}d_m\sqrt{1+|m|}\right)
\left(\sum_k(k+1)\|D_kF\|_2^2\right)^{1/2}.
$$

右の定数は有限で $a$ に依存しない。密度と $L^2$ 上の既知の作用素との一致から、全 log domain へ延長できる。interval を平行移動しても kernel に modulus 1 の位相が付くだけ。shell の characteristic function は有限個の interval multiplier の差・和なので同様に domain を保存する。

従って inner/shell 分割は、この log domain に対して正しく行える。ここを未解決の障害として残す必要はない。ただし分割が可能なことは cross form の消失や Schur complement の正値性を全く意味しない。

## 8. 停止した前 cycle の記録

$a=4/5,T=111,\beta=1/5$ の scalar cosine-taper packet 探索では負方向を見つけなかった。804 点の粗探索と1001点の近傍探索は非認証の候補探索であり、全 $R_{T,\beta}$ の正値性を認証していない。停止指示前に最良候補一つだけの adaptive ACB 積分が正値と確認されたが、これも負方向がないことや全 mode の正値性を示さない。全 head の結果は得られておらず、この固定窓拡張を目的とした refinement は停止した。

## 付録: 同じ log domain を持つ、より強い bootstrap 反例

ROOT の提案を独立に検算した。固定した $c>0$ に対し

$$
q_L(f)=\int_{\mathbb R}\log(1+t^2)|\mathcal Ff(t)|^2dt-c\|f\|_2^2,
\qquad \operatorname{supp}f\subset[-L,L]
$$

とする。ここで $\mathcal F$ は unitary Fourier transform。これは実 Weil 形式ではない。対数型 principal symbol と同じ form domain を持つが、素数項と pole は含まない。

### A. Closed form、compact resolvent、exact restrictions

$1+\log(1+t^2)\asymp\log(2+|t|)$ なので既存の log domain と一致し、形式は閉・下に有界。有限 support 上の form ball に対し

$$
\int_{|t|>R}|\mathcal Ff(t)|^2dt
\le\frac{\int\log(1+t^2)|\mathcal Ff(t)|^2dt}{\log(1+R^2)}
$$

が一様に零へ行く。低周波への Fourier restriction は、有限の spatial support と有限 frequency interval 間の Hilbert–Schmidt 作用素。従って form domain の $L^2$ への埋め込みは compact で、対応する作用素は compact resolvent を持つ。窓を変えても同じ全実線 multiplier を使うので exact nested restrictions である。

### B. Adjacent shell の cross operator は一様に有界

恒等式

$$
\log(1+t^2)=2\int_0^\infty e^{-r}\frac{1-\cos(tr)}r\,dr
$$

より off-diagonal kernel は正確に

$$
K(x,y)=-\frac{e^{-|x-y|}}{|x-y|}\qquad(x\ne y).
$$

対角部分は singular form として保持し、この kernel だけで全形式を定義しない。
inner と右 shell の境界からの距離を $u,v>0$ とすると
$|K|\le1/(u+v)$。重み $w(u)=u^{-1/2}$ に対し

$$
\int_0^\infty\frac{v^{-1/2}}{u+v}\,dv=\pi u^{-1/2}.
$$

weighted Schur test により Carleman 作用素のノルムは $\le\pi$。
左右二つの shell を合わせても cross operator は $\|B\|\le\sqrt2\pi$。
この定数は $L$ と shell 厚 $\delta$ に依存しない。第7節から sharp 分割は form domain を保存するので、block form としての利用も正当である。

### C. 小さい shell の coercivity と局所延長

支持集合の測度が $m$、$\|f\|_2=1$ なら Cauchy–Schwarz により
$|\mathcal Ff(t)|^2\le m/(2\pi)$。質量1の密度をこの高さで制限し、増加するコスト $\log(1+t^2)$ を最小化する bathtub bound から

$$
\int\log(1+t^2)|\mathcal Ff(t)|^2dt
\ge b(m):=\log(1+(\pi/m)^2)-2+
\frac{2m}{\pi}\arctan(\pi/m).
$$

これは高さ $m/(2\pi)$ の密度を $[-\pi/m,\pi/m]$ に満たした積分の値。
$b(m)\to\infty$ as $m\downarrow0$。従って小さい窓では $q_L\ge(b(2L)-c)I\succ0$。

既に inner form $A\ge\lambda I$、$\lambda>0$ が成立するとき、幅 $\delta$ の左右 shell は測度 $2\delta$ なので $C\ge(b(2\delta)-c)I$。

$$
b(2\delta)-c>\frac{2\pi^2}{\lambda}
$$

となるほど $\delta$ を小さく選べば、
$C-B^*A^{-1}B\succ0$。したがって **任意の厳密正値窓は少し広げられる**。

### D. それでも全窓へは広げられない

正規化した固定 $g\in C_c^\infty(-1,1)$ に対し
$f_L(x)=L^{-1/2}g(x/L)$ とすると

$$
q_L(f_L)=\int\log(1+(u/L)^2)|\mathcal Fg(u)|^2du-c
\longrightarrow-c<0.
$$

$L\ge1$ では $\log(1+u^2)|\mathcal Fg(u)|^2$ が可積分な優関数なので dominated convergence が適用できる。従って十分大きい有限窓では負方向がある。

停止機構も厳密に見える。$\lambda(L)=\inf_{\|f\|=1}q_L(f)$ は compact resolvent により達成される。固定区間へ scaling すると

$$
|\lambda(L_2)-\lambda(L_1)|
\le2|\log(L_2/L_1)|.
$$

これは各周波数での multiplier の差に同じ上界があるため。さらに $L_2>L_1$ では multiplier が $t\ne0$ で厳密に減少し、$L_1$ の minimizer を試験関数にすれば $\lambda(L_2)<\lambda(L_1)$。
$\lambda(L)\to+\infty$ as $L\downarrow0$、$\lambda(L)\to-c$ as $L\to\infty$ なので、有限の唯一の $L_{\rm crit}$ で $\lambda(L_{\rm crit})=0$。

従って全ての $L<L_{\rm crit}$ で局所延長できても、その許容幅は一様ではなく、$L_{\rm crit}$ を越える帰納は導けない。これは「log domain、compact resolvent、exact restrictions、有界な隣接 coupling、小 shell の強い coercivity、各正値窓の局所延長」だけから全窓の正値性を導く一般 bootstrap の反例である。Weil 形式に固有の追加構造を使う別定理の不可能性、まして RH の反例は主張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/structural_heuristics.md`](../../../reports/research/structural_heuristics.md)
