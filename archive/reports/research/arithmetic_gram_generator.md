**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_gram_generator.md` · Original SHA-256: `c3969e4af9a434746ba6f926858a5839700dceec0010176ceabf484b0d3ce9da`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 全整数のGram構造と、その対数生成子

2026-09-29、内部構築 cycle 23。**正の算術構造は構成できるが、Weil正値性への移行は未成立。**
前巡の有限theta近似は再開せず、全整数の相関、Möbius反転、素数冪の係数を直接計算した。
以下はRHを仮定しない。物理資料、最新proof claim、任意のcountertermを使わない。

## 1. 整数相関からの厳密な平方和

\(b(x)=\{x\}-1/2\) を周期1の \(L^2\) 関数とする。整数点の値は任意。
Fourier級数とParsevalで共通周波数だけを拾うと

\[
\int_0^1b(mx)b(nx)dx=\frac{\gcd(m,n)^2}{12mn}. \tag{1}
\]

そこで、零点についての仮定を入れずに

\[
G_\alpha(m,n)=\left(\frac{\gcd(m,n)^2}{mn}\right)^\alpha,
\quad
J_{2\alpha}(d)=d^{2\alpha}\prod_{p\mid d}(1-p^{-2\alpha}),\quad \alpha>0
\]

を考える。(1) そのものは \(\alpha=1\) に対応する。
Möbius反転 \(\sum_{d\mid n}J_{2\alpha}(d)=n^{2\alpha}\) より

\[
G_\alpha(m,n)=\sum_{d\mid m,n}\frac{J_{2\alpha}(d)}{(mn)^\alpha},\qquad
q_\alpha(c)=\sum_{m,n}\overline{c_m}G_\alpha(m,n)c_n=\|A_\alpha c\|_2^2, \tag{2}
\]
\[
(A_\alpha c)_d=\sqrt{J_{2\alpha}(d)}\sum_{d\mid n}n^{-\alpha}c_n,
\qquad c\in c_{00}(\mathbb N).
\]

全ての和はここでは有限。\(A_\alpha\) は \(c_{00}\) 上で可逆で

\[
(A_\alpha^{-1}y)_n=n^\alpha\sum_{n\mid m}
\frac{\mu(m/n)}{\sqrt{J_{2\alpha}(m)}}y_m. \tag{3}
\]

特に全有限Gramは正定値。\(\alpha=1/2\) では \(J_1=\varphi\)、Eulerのtotientである。
この正値性は既に全整数について成立しており、大きい有限行列の数値検査は不要。

## 2. 正形式と通常の係数空間との関係

「有限Gramが正だから通常の \(\ell^2(\mathbb N)\) 上の閉正形式になる」という
候補を、実際の算術行列に対して検査する。

\(\alpha>1/2\) なら各行の係数列が \(\ell^2\) に属するため
\(c_{00}\subset D(A_\alpha^*)\)。従って \(A_\alpha\) と形式 \(q_\alpha\) はclosable。
逆に \(0<\alpha\le1/2\) では、非closableな部分は一つのchannelにとどまらない。

固定 \(d\) に対し

\[
c^d_k=\begin{cases}
k^\alpha\mu(d/k)/\sqrt{J_{2\alpha}(d)},&k\mid d,\\
0,&k\nmid d
\end{cases}
\quad\Longrightarrow\quad A_\alpha c^d=e_d.
\]

\(S_pe_k=e_{pk}\) とすると、\(p\nmid d\) に対して正確に

\[
A_\alpha S_pc^d=p^{-\alpha}e_d+\sqrt{1-p^{-2\alpha}}\,e_{pd}. \tag{4}
\]

\(P\) を \(d\) を割らない有限素数集合、\(W_P=\sum_{p\in P}p^{-2\alpha}\) とし

\[
c_P=\frac1{W_P}\sum_{p\in P}p^{-\alpha}S_pc^d.
\]

異なる \(p\) の入力supportsは交わらないので

\[
\|c_P\|_2^2=\frac{\|c^d\|_2^2}{W_P},\qquad
\|A_\alpha c_P-e_d\|_2^2
=\frac{\sum_{p\in P}p^{-2\alpha}(1-p^{-2\alpha})}{W_P^2}\le W_P^{-1}. \tag{5}
\]

Eulerの \(\sum_p1/p=\infty\) だけで、この範囲の \(W_P\to\infty\) が従う。
従って入力は0に収束するのに像は \(e_d\) に収束する。全 \(d\) について成立し、

\[
\boxed{D(A_\alpha^*)=\{0\},\qquad
\overline{\operatorname{Graph}(A_\alpha)}=\ell^2\times\ell^2
\quad(0<\alpha\le1/2).} \tag{6}
\]

証明：随伴domainの \(y\) に対して (5) を内積評価すると \(y_d=0\)。
graph閉包は全ての \((0,e_d)\) と元のgraphを含むので全直積になる。
さらに \(0\le r\le q_\alpha\) を同じcore上のclosable形式とすると、(5) から
\(r(c_P)\to0\)、\(q_\alpha(c^d-c_P)\to0\)、従って \(r(c^d)=0\)。
\(c^d\) は \(c_{00}\) を張るので \(r=0\)。この限定した意味で全体がsingularである。

有界性の閾値は別である。素数ごとのToeplitz核
\(r^{|j-k|}\)、\(r=p^{-\alpha}\) のnormは \((1+r)/(1-r)\)。有限tensorと
長い指数区間上のほぼ定数なベクトルを使い、

\[
\boxed{G_\alpha\text{ が標準 }\ell^2\text{ 上で有界}\iff\alpha>1,
\qquad \|G_\alpha\|=\frac{\zeta(\alpha)^2}{\zeta(2\alpha)}.} \tag{7}
\]

\(\alpha>1\) では逆数の正下界もあり可逆。
\(\alpha\le1\) での非有界性にはsquarefree divisors上の等係数ベクトルだけで十分で、
そのRayleigh比は \(\prod_{p\in P}(1+p^{-\alpha})\to\infty\)。
従って \(1/2<\alpha\le1\) はclosableだが非有界、\(\alpha=1/2\) はclosable側に入らない。
ここで \(1/2\) が現れるのは明確な算術的domain閾値であり、ζ零点の所属定理ではない。

## 3. 別の完備化には、正確な等長構造がある

\(q_\alpha\) のnormで \(c_{00}\) を完備化すること自体は全 \(\alpha>0\) で可能。
(3) より \(A_\alpha(c_{00})=c_{00}\) なので、このGram完備化はfeature座標で \(\ell^2(d)\)。
(6) は完備化の存在を否定せず、元の係数 \(\ell^2(n)\) との同一視を否定する。

\(G_\alpha(pm,pn)=G_\alpha(m,n)\) より整数倍shiftは等長。
\(V_p=A_\alpha S_pA_\alpha^{-1}\) の延長は

\[
V_pe_d=\begin{cases}
p^{-\alpha}e_d+\sqrt{1-p^{-2\alpha}}\,e_{pd},&p\nmid d,\\
e_{pd},&p\mid d.
\end{cases} \tag{8}
\]

異なる素数についてdoubly commuting isometriesとなり、
\(\langle e_1,V_ne_1\rangle=n^{-\alpha}\)。各 \(V_p\) は非全射。
全 \(\alpha>0\) で同じ構造があるので、等長性だけでは中心値を選ばない。

さらに \(r_p=p^{-\alpha}\)、
\(P_r(\theta)=(1-r^2)/|1-re^{i\theta}|^2\) とすると、
無限torus上の積確率測度

\[
d\nu_\alpha=\bigotimes_p P_{r_p}(\theta_p)\frac{d\theta_p}{2\pi}
\]

のcharacter内積は \(G_\alpha\) である。有理数characterまで含めれば乗算はunitary。
このモデルも全 \(\alpha>0\) で成立する。

この測度と積Haar測度 \(m\) の違いも明示できる。
\(0<\alpha\le1/2\) のとき

\[
T_P=\frac{\sum_{p\in P}r_p\cos\theta_p}{\sum_{p\in P}r_p^2}
\]

は \(\nu_\alpha\) で平均1、\(m\) で平均0、両者で分散は \(1/W_P\) 以下。
\(W_{P_j}\ge j^2\) の入れ子の部分列を選べば、ChebyshevとBorel–Cantelliより
\(T_{P_j}\to1\)、それぞれ0がほとんど至る所で成立する。
従って \(\nu_\alpha\perp m\)。
\(\alpha>1/2\) では有限積密度の \(L^2(m)\) normの二乗が
\(\prod_p(1+r_p^2)/(1-r_p^2)<\infty\) なのでmartingaleの \(L^2\) 極限が密度を与える。
この積測度を、解析接続されたζの臨界線上の密度と同一視しない。

また \(G_{\alpha+\beta}=G_\alpha\circ G_\beta\) は**成分積**の恒等式。
通常の行列積のsemigroupではない。例えば \(\alpha,\beta>1\) でも
\((G_\alpha G_\beta)_{11}=\zeta(\alpha+\beta)>1=G_{\alpha+\beta}(1,1)\)。

## 4. 全算術的な対数操作にはMangoldt係数と負方向が現れる

\((Mc)_n=(\log n)c_n\) として、\(c_{00}\) 上で
\(B=A_\alpha M A_\alpha^{-1}\) を計算する。(3) と

\[
\sum_{j\mid k}\log(dj)\mu(k/j)
=(\log d)\mathbf1_{k=1}+\Lambda(k)
\]

により

\[
\boxed{(By)_d=(\log d)y_d+
\sum_{k\ge2}\Lambda(k)\sqrt{\frac{J_{2\alpha}(d)}{J_{2\alpha}(dk)}}\,y_{dk}.} \tag{9}
\]

入力が有限なら全て有限。\(\alpha=1/2\)、\(k=p^j\) の係数は

\[
\frac{\Lambda(p^j)}{\sqrt{p^j}}\times
\begin{cases}1,&p\mid d,\\(1-1/p)^{-1/2},&p\nmid d.
\end{cases} \tag{10}
\]

素数冪の係数は確かに現れるが、新しい素数が入る境界因子が残る。
\(B\) はfeature \(\ell^2\) 上で対称ではない。
実際 \(A_\alpha e_n\) は固有値 \(\log n\) の固有ベクトルだが、異なる \(n\) 同士も
内積 \(G_\alpha(m,n)>0\) を持つ。異なる固有値の直交性に反する。

\(\alpha=1/2\) で \(h(y)=\Re\langle y,By\rangle\) を考える。
これは \(c_{00}\) 上のHermitian二次形式であり、\((B+B^*)/2\) という
通常の作用素と同一視しない。\(e_1\notin D(B^*)\) だからである。
有限圧縮 \(\operatorname{span}\{e_1,e_p:p\in P\}\) では

\[
h(y)=\sum_{p\in P}(\log p)|y_p|^2+
\sum_{p\in P}\frac{\log p}{\sqrt{p-1}}\Re(\overline{y_1}y_p).
\]

すでに \(y=e_1-e_2/2\) で \(h(y)=-\log2/4<0\)。
しかも任意の \(\beta>0\) に対して \(h+\beta\|\cdot\|^2\) のSchur complementは

\[
\boxed{\beta-\sum_{p\in P}
\frac{(\log p)^2}{4(p-1)(\beta+\log p)}\longrightarrow-\infty.} \tag{11}
\]

十分大きい \(p\) の項は \(\log p/[8(p-1)]\) 以上で、素数逆数和の発散だけで結論できる。
従ってこの自然なHermitian formは下半有界でなく、有限scalar shiftでは直らない。
これは実際のWeil形式や、そのarchimedean項による補償の不可能性を示すものではない。

## 5. Euler対数微分との別の正確な接続

標準係数 \(\ell^2\) 上の \(S_pe_n=e_{pn}\) と有限素数集合 \(P\) に対し

\[
R_{\alpha,P}=\prod_{p\in P}(I-p^{-\alpha}S_p)^{-1},\qquad
-R_{\alpha,P}^{-1}\partial_\alpha R_{\alpha,P}
=\sum_{p\in P,j\ge1}(\log p)p^{-j\alpha}S_{p^j}. \tag{12}
\]

この有限素数・無限冪の恒等式は作用素normで成立。
\(\alpha=1/2\) の係数は厳密に \(\Lambda(n)/\sqrt n\) だが、全素数へ移すと
右辺を \(e_1\) に適用したnormの二乗は
\(\sum_{p\in P}(\log p)^2/(p-1)\to\infty\)。
したがって同じ有界作用素として全素数極限を取れない。

正のPoisson因子でも、対数微分は

\[
-\partial_\alpha\log P_{p^{-\alpha}}(\theta)
=2\log p\left[\sum_{j\ge1}p^{-j\alpha}\cos(j\theta)
-\frac{p^{-2\alpha}}{1-p^{-2\alpha}}\right]. \tag{13}
\]

\(\theta=0,\pi\) で値はそれぞれ \(\pm2\log p\,p^{-\alpha}/(1-p^{-2\alpha})\)。
正密度の対数微分には、単一素数でも両符号がある。
\(\theta_p=t\log p\) とすれば明示公式と同じcosine周波数が現れるが、
\(\alpha=1/2\) の定数項 \(2\sum_p\log p/(p-1)\) は発散する。
Weilのarchimedean・pole項への同定を証明せずにこれを除去しない。

## 6. 連続Mellin相関との違い

周期的な (1) とは別に、実際のscale相関

\[
C(a,b)=\int_0^\infty\{ax\}\{bx\}\frac{dx}{x^2},\qquad a,b>0
\]

もGramである。\(u=\log x\)、\(g(u)=e^{-u/2}\{e^u\}\in L^1\cap L^2\) とし、
この節では \(\widehat g(t)=\int_{\mathbb R}g(u)e^{-itu}du\) の規約を使う。すると

\[
\widehat g(t)=-\frac{\zeta(1/2+it)}{1/2+it},\qquad
C(a,b)=\frac{\sqrt{ab}}{2\pi}\int_{\mathbb R}
\frac{|\zeta(1/2+it)|^2}{t^2+1/4}e^{it\log(a/b)}dt. \tag{14}
\]

Mellin式は \(0<\Re s<1\) での \(\int_0^\infty\{x\}x^{-s-1}dx=-\zeta(s)/s\)
から得られ、Plancherelにより表示積分は絶対収束。
整数 \(a,b\) でも (1) と同じ内積ではない：
\(C(a,b)=\int_0^1\{ax\}\{bx\}\sum_{j\ge0}(j+x)^{-2}dx\)。

この正値性から微分した形式へ移る際には、分布恒等式

\[
(D_u+1/2)g=e^{u/2}-\sum_{n\ge1}n^{-1/2}\delta(u-\log n) \tag{15}
\]

を保持する必要がある。\(g\) は跳躍を持ち \(H^1\) ではない。
また「相関では位相が失われるのでactual \(\Xi\) は定まらない」とも言わない。
\(w(t)=|\zeta(1/2+it)|^2/(t^2+1/4)\) から

\[
Q(t)=\Xi(t)^2=\frac{(t^2+1/4)^3}{4\sqrt\pi}
|\Gamma(1/4+it/2)|^2w(t)
\]

が決まり、実整関数性と \(\Xi(0)>0\) で符号も固定される。
不足するのは微分の符号制御で、例えば \(Q>0\) の実区間上で
\((\Xi'^2-\Xi\Xi'')/4=-Q(\log Q)''/8\)。
(14) の \(w\ge0\) だけでは右辺の非負性が従わない。
この実対角条件だけをRHの十分条件とも扱わない。

## 7. 構成後に行った限定的な既知性照合

[Nicola Thorn (2018), Theorems 2.1–2.2](https://arxiv.org/html/1801.09478)
は正のmultiplicative Toeplitz記号の \(\ell^2\) normを \(\ell^1(\mathbb Q_+)\) normと同定する。
既約分数 \(m/n\) に \(f(m/n)=(mn)^{-\alpha}\) を置けば (7) は直接の特殊化である。
非可積分側は有限の正記号の切断にも定理を適用して判定できる。

[Báez-Duarte–Balazard–Landreau–Saias (2003), §9.1 Proposition 86](https://arxiv.org/html/math/0306251)
は \(A(\lambda)=C(1,\lambda)\) のMellin変換を
\(-\zeta(-s)\zeta(s+1)/(s(s+1))\)、\(-1<\Re s<0\) で与える。
(14) はこの既知の自己相関表示の中心線上の形である。
ROOTも両原文の該当定理文を確認した。両論文全体の独立再証明はしていない。

(6) のliteralなGCD形式の閉可能性分類と (11) の具体的共役生成子の結果は、
今回の限定検索では掲載先を特定していない。§3の積測度についても上記の直接証明を使う。
既知性の未特定を新規性の主張とは扱わない。外部proof claimを追う探索には戻っていない。

## 8. 判定と独立検証

正確な平方和、共通Gram完備化、全素数の等長構造、別のunitary拡張までは構成できた。
しかし、通常の係数 \(\ell^2\) への閉包は臨界指数で破綻し、
Mangoldt係数を持つ対数形式は下半有界でなく、Poisson対数微分も符号不定。
これらを無条件Weil正値性の新しい根拠として採用する候補は終了する。
既存のRH同値条件を新しい完備性・正値性公理として採用していない。

ROOT/BUILDERが (9)〜(11)、ROOT/DESTROYERが (4)〜(7) を独立導出。
BUILDERは (1)〜(3)、(8)、(12) を確認し、LITERATURE担当も最初は内部計算として
(14)〜(15) と位相に関する注意を導出した。新規性は主張しない。
再現: `experiments/scripts/arithmetic_gram_checks.py`、
`experiments/results/arithmetic-gram-checks.json`。
有理数検算・Arb符号包含と、無限範囲の解析証明を区別する。Lean形式化はしていない。

主グラフ合流0、RHは未証明。次に必要なのは単なる正Gramの追加ではなく、
実際のWeil全形式への等式と、そこに現れる算術交差項の独立な評価である。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/arithmetic-gram-checks.json`](../../../artifacts/experiments/results/arithmetic-gram-checks.json)
- [`experiments/scripts/arithmetic_gram_checks.py`](../../../artifacts/experiments/scripts/arithmetic_gram_checks.py)
