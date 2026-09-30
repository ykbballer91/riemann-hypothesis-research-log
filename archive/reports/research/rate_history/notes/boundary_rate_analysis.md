**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/rate_history/notes/boundary_rate_analysis.md` · Original SHA-256: `b73e96ddaa1cf47063b3924be2bacdfcaaf7963b83d26feb6a3c41219d94cd5a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Sharp support と Fourier 射影の境界減衰率

2026-09-30。RH OPEN。対象は実際の theta 核と、固定有限次元
\(\mathcal R_m=\operatorname{span}\{k,k'',\ldots,k^{(2m)}\}\)、\(m\le3\)。
新規性を主張しない。旧ファイルは読み取りのみ。

本ノートで証明する実際の Weil 形式の漸近式は、まず **sharp support 制限だけ** に対するものである。
有限 Fourier 射影を含む canonical \(T_{a,N}\) への置換はしない。
後者については exact 分解と Fourier 係数を与えるが、全体の一意な最速状態は特定しない。

## BR1. 規約と実際の核

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\quad
\Xi(z)=\xi(1/2+iz),\quad \widehat f(z)=\int_{\mathbb R}f(t)e^{-izt}\,dt.
\]

\(\theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}\)、
\(\Psi(t)=e^{t/2}\theta(e^{2t})\) とすると Poisson 恒等式により \(\Psi\) は偶で、
\[
k(t)=\tfrac18(D_t^2-1/4)\Psi(t),\qquad \widehat k(z)=\Xi(z)/4.
\tag{BR1}
\]
従って \(k\) は実偶である。\(t\ge0\) では、\(y_n=\pi n^2e^{2t}\) として
\[
k(t)=e^{t/2}\sum_{n\ge1}P_0(y_n)e^{-y_n},\qquad P_0(y)=y^2-\tfrac32y.
\tag{BR2}
\]
全微分について compact 上絶対一様収束する。負側の値は実際の Poisson 偶性から得るのであり、有限和を任意に偶延長する操作ではない。

規約の一次照合は CCM, *Zeta Spectral Triples*, [arXiv:2511.22755v1, (7.1)–(7.2)](https://arxiv.org/html/2511.22755v1#S7) の seed と arithmetic sum。
本ノートは上記の標準 \(\xi\) を固定するため、Fourier 係数の全体因子は明示的に \(1/4\) とする。
Weil 形式は同原稿 [(3.19)](https://arxiv.org/html/2511.22755v1#S3.SS1) の全 archimedean・polar・prime-power 項を使う。

微分多項式は
\[
P_{r+1}(y)=2yP_r'(y)+(1/2-2y)P_r(y),\qquad
k^{(r)}(t)=e^{t/2}\sum_{n\ge1}P_r(y_n)e^{-y_n}.
\tag{BR3}
\]
帰納法で
\[
P_r(y)=(-2)^r y^{r+2}\left(1-\frac{(2r+3)(r+2)}{4y}+O_r(y^{-2})\right).
\tag{BR4}
\]
実際、先頭係数は毎回 \(-2\) 倍され、次係数/先頭係数の比は
\(b_{r+1}=b_r-r-9/4\)、\(b_0=-3/2\) を満たす。
\(n\ge2\) の和は第一項に対して \(O_r(e^{-3y_1})\) である。

以下、\(a\to\infty\)、\(Y=\pi e^{2a}\)、\(\beta=2Y\)、
\(f_j=k^{(2j)}\)、\(A_j=f_j(a)\) とする。固定 \(j=0,1,2,3\) について
\[
A_j=4^j\pi^{-1/4}Y^{2j+9/4}e^{-Y}(1+O_j(Y^{-1})).
\tag{BR5}
\]

## BR2. Sharp tail が属する domain と radical identity

ここでは global \(L^2\) 上の閉形式の存在を仮定しない。
次の明示的な test class で古典的 Weil explicit formula を連続延長する：
\(f\) は piecewise smooth で分布微分 \(Df\) が局所有限測度、かつ全 \(b>0\) について
\[
\|e^{b|t|}f\|_1+\|e^{b|t|}f\|_2+
\int e^{b|t|}\,d|Df|(t)<\infty.
\tag{BR6}
\]
本ノートで現れる \(f_j\)、その sharp 内外制限、有限 Fourier 多項式の零延長とこれらの有限線形結合はすべてこの class に属する。
特に sharp cut の jump は測度 \(Df\) に含める。sharp cut が \(H^1(\mathbb R)\) に属するとは主張しない。

\(|\Im z|\le1/2\) で部分積分により \(|\widehat f(z)|\le C_f/(1+|\Re z|)\)。
零点計数 \(N(T)=O(T\log T)\) より
\[
Q(f,g)=\sum_\rho\widehat f(z_\rho)
           \overline{\widehat g(\overline{z_\rho})},\qquad
z_\rho=(\rho-1/2)/i,
\tag{BR7}
\]
は絶対収束する。零点は重複度込みで、RH や単純性を仮定しない。
Fourier の負符号は零点集合の \(z\mapsto-z\) 対称性でこの表示と整合する。

同じ形式の算術表示は、\(C_f(d)=\int f(x+d)\overline{f(x)}dx\) として
\[
\begin{split}
Q(f)={}&\frac1{2\pi}\int h(\omega)|\widehat f(\omega)|^2d\omega
 +2\Re\{\widehat f(i/2)\overline{\widehat f(-i/2)}\}\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n),\qquad
h(\omega)=\Re\psi(1/4+i\omega/2)-\log\pi.
\end{split}
\tag{BR8}
\]
すべて絶対収束する。例えば任意の \(b>1/2\) で
\[
|C_f(d)|\le e^{-b|d|}\|e^{b|x|}f\|_2^2,
\quad \sum_{n\ge2}\Lambda(n)n^{-b-1/2}<\infty.
\tag{BR9}
\]
Archimedean 積分は \(h=O(\log(2+|\omega|))\) と Fourier の \(O(1/|\omega|)\) で収束する。

延長の正当化を明記する。smooth compact cutoff、次いで mollification により
\(f_\nu\in C_c^\infty\) を作ると、各 exponential-weighted \(L^1,L^2\) ノルムで収束し、対応する weighted variation は一様有界にできる。
零点側は strip 上の一様 \(O((1+|\Re z|)^{-1})\) と点ごとの収束で優収束。
Archimedean 側も同じ上界で優収束、polar は weighted \(L^1\)、prime 側は (BR9) と weighted \(L^2\) で収束する。
従って smooth compact core での explicit formula が (BR6) へ延びる。
これで sharp・noncompact tail における形式等号を、global \(L^2\) closability を使わずに得る。

\[
\widehat f_j(z)=(-1)^jz^{2j}\Xi(z)/4
\quad\Longrightarrow\quad Q(f_j,g)=Q(g,f_j)=0
\tag{BR10}
\]
がこの test class で成立する。
\(R_af=1_{[-a,a]}f\)、\(r_a=(I-R_a)f\) とすれば、全 \(f\in\mathcal R_m\) について
\[
\boxed{Q(R_af)=Q(r_a).}
\tag{BR11}
\]
これは正値性の使用ではなく sesquilinear radical の等号である。

## BR3. 境界 profile と窓外のノルム

固定 \(j\) の片側 profile を
\[
F_{j,a}(v)=\frac{f_j(a+v/\beta)}{A_j},\qquad v\ge0
\]
とする。(BR3)–(BR5)、\(y_1=Ye^{v/Y}\) から
\[
F_{j,a}(v)=e^{-v}\left[1+\frac{(2j+9/4)v-v^2/2}{Y}\right]
  +O_j\left(Y^{-2}(1+v)^K e^{-v/2}\right)
\tag{BR12}
\]
を、固定された十分大きい整数 \(K\) で得る。
これは例えば \(v\le Y^{1/3}\) で Taylor の余項を評価し、残りで
\(e^{v/Y}-1\ge v/Y\) と exponential decay を使って証明できる。
同じ分割で一回の \(v\) 微分にも integrable な一様上界がある。
特に
\[
\|F_{j,a}\|_2^2=\tfrac12+O_j(Y^{-1}),\quad
\|F_{j,a}\|_1+\|F'_{j,a}\|_1\le C_j,\quad
|F_{j,a}(v)|\le C_je^{-v/2}.
\tag{BR13}
\]
従って、\(r_{j,a}=(I-R_a)f_j\) に対して
\[
\|r_{j,a}\|_2^2=\frac{A_j^2}{2Y}(1+O_j(Y^{-1}))
\sim\frac{16^j}{2\sqrt\pi}Y^{4j+7/2}e^{-2Y}.
\tag{BR14}
\]
また固定 \(b\ge0\) について
\[
\int_{|t|>a}e^{b|t|}|f_j(t)|dt
\sim\frac{A_je^{ba}}{Y}.
\tag{BR15}
\]
これは compact Fourier strip 上の support error の上界にもなる。
これらはノルム・変換の誤差であり、次節まで Weil 形式の値とは同一視しない。

## BR4. 実際の sharp-support Weil defect

**命題。** 固定 \(j=0,1,2,3\) について無条件に
\[
\boxed{Q(R_af_j)=\frac{A_j^2}{2Y}\,[2a+o(1)]
\sim\frac{a16^j}{\sqrt\pi}Y^{4j+7/2}e^{-2Y}.}
\tag{BR16}
\]
特にこの support-only signed defect は十分大きい \(a\) で正である。

### BR4.1 Archimedean 項

\(g_+(t)=1_{t>a}f_j(t)\)、\(g_-(t)=g_+(-t)\) とし、
\(\varphi_a(\xi)=\int_0^\infty F_{j,a}(v)e^{-i\xi v}dv\)。
すると
\[
\widehat g_+(\omega)=\frac{A_j}{\beta}e^{-ia\omega}\varphi_a(\omega/\beta),\qquad
|\varphi_a(\xi)|\le\frac{C_j}{1+|\xi|},\quad
\varphi_a(\xi)\longrightarrow\frac1{1+i\xi}.
\tag{BR17}
\]
Digamma の漸近式から \(h(\omega)=\log(|\omega|/(2\pi))+O(|\omega|^{-2})\)。
一次照合は [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)（本計算では bounded \(\omega\) も含む上界を別に用いる）。
\[
|h(\beta\xi)-\log(\beta/(2\pi))|\le C+|\log|\xi||\quad(\xi\ne0,\ \beta\ge2).
\]
実際 \(|\beta\xi|\le1\) なら \(-\log|\xi|\ge\log\beta\)、それ以外は上記漸近式を使う。
よって (BR17) の優収束と
\(\int_{\mathbb R}\log|\xi|/(1+\xi^2)d\xi=0\) により
\[
\frac1{2\pi}\int h(\omega)|\widehat g_+(\omega)|^2d\omega
=\frac{A_j^2}{\beta}\left[\tfrac12\log\frac{\beta}{2\pi}+o(1)\right].
\tag{BR18}
\]
ここで \(O(Y^{-1})\log\beta=o(1)\) を用いた。

左右の混合項も評価する。Digamma 級数から直接
\[
h(\omega)=h(0)+2\int_0^\infty
 w(v)(1-\cos(\omega v))dv,\qquad
w(v)=\frac{e^{-v/2}}{1-e^{-2v}}.
\tag{BR19}
\]
従って、互いに離れた support の間の off-diagonal kernel は \(-w(|x-y|)\)。
左右 tail の距離は \(2a\) 以上なので、\(a\ge1\) なら
\[
|Q_{\rm arch}(g_+,g_-)|
\le C e^{-a}\|g_+\|_1\|g_-\|_1
\le C_j e^{-a}A_j^2/\beta^2.
\tag{BR20}
\]
したがって両 edge の合計は \(A_j^2\beta^{-1}[\log(\beta/(2\pi))+o(1)]\)。

### BR4.2 Polar 項と全 prime-power 和

(BR13) より、全 \(s\ge0\) について
\(|f_j(a+s)|\le C_jA_je^{-Ys}\)。従って polar 項の絶対値は
\[
O_j(A_j^2e^a/Y^2)=O_j(A_j^2/Y^{3/2}).
\tag{BR21}
\]
同じ側の二つの tail の相関は、\(d\ge0\) に対して
\(O_j(A_j^2Y^{-1}e^{-Yd})\)。従ってその prime 和は
\[
O_j\left(\frac{A_j^2}{Y}\sum_{n\ge2}(\log n)n^{-Y-1/2}\right)
=O_j(A_j^2Y^{-1}2^{-Y}).
\tag{BR22}
\]
反対側の tail は \(d<2a\) で交わらない。
\(d=2a+s\)、\(s\ge0\) なら重なる区間の長さは \(s\) であり、相関の絶対値は
\(O_j(A_j^2s e^{-Ys})\)。\(X=e^{2a}=Y/\pi\) と置くと、その prime 和は
\[
O_j\left(A_j^2\sum_{n>X}\frac{\log n}{\sqrt n}
 \log(n/X)(n/X)^{-Y}\right)
=O_j(A_j^2\log Y/Y^{3/2}).
\tag{BR23}
\]
最後の bound は prime number theorem を使わない。
\(X<n\le2X\) で \(r=n-X>0\) とすると
\(r/(2X)\le\log(n/X)\le r/X\)。各項は
\(C(\log X)X^{-3/2}r e^{-\pi r/2}\) 以下であり、
\(r\) は間隔1の列だから、その総和は \(X\) の小数部分に一様に有界。
\(n>2X\) は積分比較で \(O(\sqrt X\log X\,2^{-Y})\) となり小さい。
\(n=X\) が整数なら \(s=0\) なのでその項は零である。
\(\Lambda(n)\le\log n\) のみを使い、素数冪の重複度を省いていない。

(BR21)–(BR23) はいずれも \(o(A_j^2/Y)\)。
\(\log(\beta/(2\pi))=\log(Y/\pi)=2a\) と (BR11) により (BR16) が従う。

### BR4.3 固定基底の率と rank-one 境界形式

共通因子 \((a/\sqrt\pi)e^{-2Y}\) を除いた support-only 主項は次の通り。

| 関数 | 主項の係数と \(Y\) の次数 |
|---|---|
| \(k\) | \(Y^{7/2}\) |
| \(k''\) | \(16Y^{15/2}\) |
| \(k^{(4)}\) | \(256Y^{23/2}\) |
| \(k^{(6)}\) | \(4096Y^{31/2}\) |

単位 \(L^2\) 正規化なら、それぞれさらに固定定数 \(\|f_j\|_2^{-2}\) を掛ける。
\(\|R_af_j\|_2\to\|f_j\|_2>0\) なので次数は変わらない。

混合項にも同じ edge 計算が適用できる。\(M^{\rm sup}_{ij}=Q(R_af_i,R_af_j)\)、
\(D_a=\operatorname{diag}(A_0,\ldots,A_m)\) とすると、固定 \(m\) で
\[
\frac{\beta}{2a}D_a^{-1}M^{\rm sup}D_a^{-1}
\longrightarrow\boldsymbol1\boldsymbol1^*.
\tag{BR24}
\]
従って leading functional は境界値 \(|\sum c_jf_j(a)|^2\)。
rank は1で、\(m\ge1\) なら kernel が残る。
これは generalized Gram metric を恒等行列にした式ではない。
\(D_a\) による座標変更後は global \(L^2\) Gram も同時に変換する必要がある。

### BR4.4 境界消去で \(k\) 単独より速くなる具体例

十分大きい \(a\) で
\[
g_a=k-\frac{k(a)}{k''(a)}k'',\quad g_a(a)=0,\quad
\frac{k(a)}{k''(a)}=\frac1{4Y^2}\left(1+\frac{11}{2Y}+O(Y^{-2})\right).
\tag{BR25}
\]
従って \(g_a\to k\) in global \(L^2\)。しかし (BR12) を引くと
\[
\frac{Yg_a(a+v/\beta)}{k(a)}\longrightarrow-2ve^{-v},
\qquad\int_0^\infty4v^2e^{-2v}dv=1.
\tag{BR26}
\]
収束は一様な exponential majorant を持つ weighted \(L^1,L^2\) と variation の範囲で成立する。
BR4.1–BR4.2 の同じ proof を amplitude \(k(a)/Y\)、limit profile \(-2ve^{-v}\) に適用できる。
主項に必要な profile の \(L^2\) 質量は1なので
\[
Q(R_ag_a)\sim\frac{2k(a)^2}{Y^2\beta}\log\frac{\beta}{2\pi},\qquad
\boxed{\frac{Q(R_ag_a)}{Q(R_ak)}\sim\frac2{Y^2}.}
\tag{BR27}
\]
ここでは leading \(\sim\) を主張している。新しい profile の Fourier 画像は
\(-2/(1+i\xi)^2\) で、その log moment は
\((2\pi)^{-1}\int 4\log|\xi|/(1+\xi^2)^2d\xi=-1\)。
従って (BR18) の「log moment が0」という定数項まで再利用してはいない。
正規化後の比も同じ。従って「列挙した固定基底の中で \(k\) が最速」は
「有限 \(a\) で span 内の最速状態が \(k\) そのもの」と異なる。
(BR25) は \(k\) を極限に持つ一つの良い組合せであり、全 \(\mathcal R_m\) の最適化・一意性定理ではない。

## BR5. Canonical Fourier 射影と二つの極限

\(\omega_n=\pi n/a\)。基底の符号を区別する：
\[
e_n(t)=\frac{e^{i\omega_nt}}{\sqrt{2a}},\qquad
V_n(t)=(-1)^n e_n(t).
\tag{BR28}
\]
既存実験の基底は \(V_n\)。\(|n|\le N\) への正射影 \(P_N\) 自体はこの位相変更で変わらない。
偶 smooth \(f\) の unshifted 係数を \(c_n=\langle R_af,e_n\rangle\) とする。
繰り返し部分積分により、\(n\ne0\)、任意の整数 \(R\ge1\) で
\[
\begin{split}
c_n={}&\frac{2(-1)^n}{\sqrt{2a}}
\sum_{r=1}^R\frac{(-1)^{r-1}f^{(2r-1)}(a)}{\omega_n^{2r}}\\
&+\frac{(-1)^R}{\sqrt{2a}\,\omega_n^{2R}}
\int_{-a}^a f^{(2R)}(t)e^{-i\omega_nt}dt.
\end{split}
\tag{BR29}
\]
端点の関数値は \(f(a)=f(-a)\) で周期的に一致するため \(n^{-1}\) 項が消える。
最初の不一致は \(f'(a)-f'(-a)=2f'(a)\)。固定 \(a\) で
\[
c_n=\frac{2(-1)^nf'(a)}{\sqrt{2a}\,\omega_n^2}+O_a(n^{-4}).
\tag{BR30}
\]
実際の \(V_n\) 係数は \((-1)^nc_n\) なので先頭の \((-1)^n\) は消える。
平方ノルムは同じで、\(f'(a)\ne0\) なら
\[
\|(I-P_N)R_af\|_2^2
\sim\frac{4a^3|f'(a)|^2}{3\pi^4N^3}\qquad(N\to\infty,\ a\text{ fixed}).
\tag{BR31}
\]
一般に \(f'(a)=\cdots=f^{(2q-3)}(a)=0\)、\(f^{(2q-1)}(a)\ne0\) なら
\[
\|(I-P_N)R_af\|_2^2
\sim\frac{4a^{4q-1}|f^{(2q-1)}(a)|^2}{(4q-1)\pi^{4q}N^{4q-1}}.
\tag{BR32}
\]
この周期的な endpoint matching と、\(R_af\) の global 零延長の jump は別である。

**Joint limit の注意。** \(f=f_j\) なら、全 \(a,n\) で exact に
\[
c_{j,n}=\frac1{\sqrt{2a}}
\left\{(-1)^j\omega_n^{2j}\Xi(\omega_n)/4-
\int_{|t|>a}f_j(t)e^{-i\omega_nt}dt\right\}.
\tag{BR33}
\]
従って \(a\to\infty\) も動く場合、(BR30) の \(O_a\) を一様とみなしてはならない。
例えば共に admissible な \(N_1(a)=\lceil a^2\rceil\)、\(N_2(a)=\lceil a^3\rceil\) では
\(N_i/a\to\infty\) だが \(N_i/(aY)\to0\)。この条件だけでは、幅 \(Y^{-1}\) の boundary profile を周波数側で解像していない。
対照的に \(N_3(a)=\lceil aY^2\rceil\) は \(N_3/(aY)\to\infty\)。
後者も、(BR31) の uniform remainder を証明せずそのまま代入する理由にはしない。

Gamma の [DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9) と elementary Euler summation bound
\(\zeta(1/2+it)=O((1+|t|)^{1/2})\) から
\[
|\Xi(\omega)|\le C(1+|\omega|)^{9/4}e^{-\pi|\omega|/4}.
\tag{BR34}
\]
後者の粗い \(\zeta\) bound は \(M\asymp1+|t|\) で Dirichlet sum を打ち切り、
Euler remainder \(O(|s|M^{-1/2})\) を用いるだけで得られる。
(BR33) にはこの intrinsic Fourier tail と、\(e^{-Y}\) 級の support tail が両方ある。
多項式 \(N(a)\) では前者の上界の尺度ははるかに大きい。
これは actual projection error や actual \(Q\) の下界・漸近を証明するものではない
（\(\Xi\) の零点と係数の相殺もある）。
従って二つの cofinal path の full rate が異なるという定理もここからは出さない。

射影の leading functional は \(f'(a)\) なので、例えば
\(k-[k'(a)/k'''(a)]k''\) はこれを消す。
\[
\frac{k'(a)}{k'''(a)}=\frac1{4Y^2}\left(1+\frac{15}{2Y}+O(Y^{-2})\right),
\tag{BR35}
\]
であり、support 値を消す (BR25) と同じ係数ではない。
\(m\ge2\) なら境界値と一階導関数の二つの線形条件を同時に満たす非零組合せもある。
有限 \(a,N\) での最適化には、その次の項と actual Gram が必要である。

## BR6. 全 finite defect と算術項の二重計上禁止

\(T_{a,N}=P_NR_a\)、\(r=(I-R_a)f\)、\(p=(I-P_N)R_af\) とする。
\(f\in\mathcal R_m\) なら BR2 の同じ test class 上で
\[
\boxed{Q(T_{a,N}f)=Q(r)+2\Re Q(r,p)+Q(p).}
\tag{BR36}
\]
従って (BR16) は第一項だけを扱う。
\(Q\) は RH なしに global 正形式とはされていないので、
\(|Q(r,p)|\le Q(r)^{1/2}Q(p)^{1/2}\) を使うことも、混合項を落とすこともできない。

左辺は \([-a,a]\) support を持つので prime 和は \(\log n<2a\) の有限和である。
右辺の \(r\) は noncompact であり、反対側の tails の相関には \(\log n\ge2a\) も現れる。
この全 prime 和はすでに (BR8)、(BR23)、(BR36) に入っている。
さらに独立な「missing-prime error」を足すと二重計上になる。

未正規化 columns \(v_j=T_{a,N}f_j\) から
\[
M_{ij}=Q(v_i,v_j),\quad G_{ij}=\langle v_i,v_j\rangle,
\qquad \mathcal R(v_c)=\frac{c^*Mc}{c^*Gc}
\tag{BR37}
\]
を作る。正規化はこの後。\(G\) が正定値な実現 span での stationary equation は
\(Mc=\mu Gc\)。near cancellation による小固有値を、Gram conditioning の検査なしに認証してはいけない。

## BR7. 三つの rate の区別と停止点

1. **Rate A:** (BR16)、(BR27) は actual \(Q\) の signed support-only defect の定理。
   正値の結論はここで扱った各列・特定組合せの十分大きい窓に限る。
   \(|Q|\) の最小化、full \(Q(Tf)\) の最小化、全 test positivity を同一視しない。
2. **Rate B:** 同じ有限行列の ground \(e_0\) に対する excess は
   \(\mathcal R(v)-e_0\)。ground が simple なら距離を得るには全 gap \(e_1-e_0\) で割る。
   小さい絶対 defect だけから ground との overlap は出ない。
3. **Rate C:** compact strip 上の変換誤差には、support の (BR15) に加えて
   \[
   \sup_{|\Im z|\le b}|\widehat{p}(z)|
   \le\left(\int_{-a}^ae^{2b|t|}dt\right)^{1/2}\|p\|_2
   \le\sqrt{2a}\,e^{ba}\|p\|_2
   \tag{BR38}
   \]
   という growing-window loss がある。値正規化の分母も別に制御する。

特に \(j\ge1\) では \(\widehat f_j(0)=0\)。有限 cut により微小非零となった分母で割ることは安定な global 正規化ではない。
固定 \(f=\sum c_jf_j\) で \(c_0\ne0\) なら
\[
\frac{\widehat f(z)}{\widehat f(0)}
=\frac{\Xi(z)}{\Xi(0)}
\left[1+\sum_{j\ge1}\frac{c_j}{c_0}(-1)^jz^{2j}\right].
\tag{BR39}
\]
固定有限 \(m\) でこの正規化された全変換が \(\Xi(z)/\Xi(0)\) に locally uniformly 収束するなら、各 \(c_j/c_0\to0\)。
これは値正規化した target を指定したことの帰結であり、Weil radical 認識から導いた state selection ではない。

**到達点。** Sharp support に限れば、固定四つの列の actual defect は異なる率を持つ。
leading boundary matrix は rank one と明示でき、境界消去により \(k\) 単独より速い組合せも証明できる。
しかしその leading kernel 上の全次形式、uniform joint projection remainder、full generalized gap をここでは得ていない。
従って canonical \(T_{a,N}\) の一意な最速状態、prolate proxy との同定、cofinal path 独立性は未証明。
固定 \(m\) の結果を \(m\to\infty\) に交換しない。新たな第四候補は導入しない。
本担当の結論は **NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED**（support-only の上記定理を除外せずに保持）。

独立読取監査：DESTROYER は BR2 の weighted-BV 延長、BR4 の support-only 主係数・全 prime bound、BR25–27 の係数と cancellation 比、BR29–32 の Fourier 定数、BR36 の混合項を独立に再計算し PASS とした。
新 profile の log moment は上記の通り0ではないという注意を反映した。
監査は full \(T_{a,N}\) の rate、ground 選択、RH を証明したものではない。

## BR8. 限定された選択定理：support-only、\(m=1\)

**補足命題。** Fourier 射影 \(P_N\) を入れず、二次元空間
\[
\mathcal V_a=\operatorname{span}\{R_ak,R_ak''\}
\]
の standard \(L^2\) Rayleigh 商を考える。
十分大きい \(a\) では、この空間に制限した **signed** Weil 形式の最小固有値は単純である。
その単位固有関数 \(u_a\) の位相を \(\langle u_a,k\rangle>0\) と選ぶと
\[
\boxed{u_a\longrightarrow k/\|k\|_2\quad\text{in }L^2(\mathbb R).}
\tag{BR40}
\]
これは support-only、固定 \(m=1\) についての実際の限定選択結果である。
leading rank-one matrix の null space はこの場合一次元なので、その projective null line は一つである。

**証明。** raw 固定基底 \((f_0,f_1)=(k,k'')\) で
\[
M^{\rm sup}_{ij}(a)=Q(R_af_i,R_af_j),\qquad
G^{\rm sup}_{ij}(a)=\langle R_af_i,R_af_j\rangle.
\]
(BR24) と \(A_1/A_0\sim4Y^2\) より、正のスカラー
\[
s_a=\frac{a}{Y}A_1^2
\]
について
\[
\frac{M^{\rm sup}(a)}{s_a}\longrightarrow
E_{11}:=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
G^{\rm sup}(a)\longrightarrow
G_\infty:=\begin{pmatrix}
\|k\|_2^2&-\|k'\|_2^2\\
-\|k'\|_2^2&\|k''\|_2^2
\end{pmatrix}>0.
\tag{BR41}
\]
後半は tail の \(L^2\) 収束と部分積分による。
正定値性は \(k,k''\) の線形独立性から従う。
実際、\(c_0k+c_1k''=0\) なら Fourier 変換は
\((c_0-c_1z^2)\Xi(z)/4=0\) であり、\(\Xi\) は零関数ではないので \(c_0=c_1=0\)。
従って大きい \(a\) で \(G^{\rm sup}(a)>0\) である。

正定値平方根で whiten した実対称行列は
\[
B_a=(G^{\rm sup}(a))^{-1/2}\frac{M^{\rm sup}(a)}{s_a}
            (G^{\rm sup}(a))^{-1/2}
\longrightarrow B_\infty=G_\infty^{-1/2}E_{11}G_\infty^{-1/2}.
\tag{BR42}
\]
\(B_\infty\) の固有値は
\[
0,\quad \nu=(G_\infty^{-1})_{11}
=\frac{\|k\|_2^2}{\det G_\infty}>0
\tag{BR43}
\]
（添字は \(0,1\)）。二次対称行列の固有値公式から、大きい \(a\) で二固有値は分離する。
固有射影も
\((\lambda_+(B_a)I-B_a)/(\lambda_+(B_a)-\lambda_-(B_a))\)
という明示式で極限の零固有射影へ収束する。

raw coefficient に戻した零固有空間は \(E_{11}c=0\)、すなわち \(c_1=0\)。
\(c^*G^{\rm sup}(a)c=1\) と位相の指定により、最小固有方向の係数は
\((c_0,c_1)\to(1/\|k\|_2,0)\)。\(R_af_j\to f_j\) in \(L^2\) だから (BR40) が従う。
さらに restricted generalized eigenvalues を \(\mu_-(a)<\mu_+(a)\) と書けば
\[
\frac{\mu_-(a)}{s_a}\to0,\qquad
\frac{\mu_+(a)}{s_a}\to\nu,\qquad
\frac{\mu_+(a)-\mu_-(a)}{s_a}\to\nu.
\tag{BR44}
\]

**正確な範囲。** この証明は最小 eigenvalue の次の非零係数や符号を決めていない。
\(|Q|\) 最小化の一意性でもない。
(BR27) の改良された線形結合が \(k\) へ収束する事実と矛盾せず、有限 \(a\) の固有関数が \(R_ak\) そのものだとも主張しない。
\(P_N\) を含む full realization、全 \(H_a\) の ground、任意 cofinal path、\(m\ge2\) や無限 radical への拡張はこの補足命題に含まれない。
従って full track の停止判定は維持する一方、**support-only \(m=1\) には限定された最小方向の選択が実際に成立する**、と区別する。

独立監査追記：DESTROYER は (BR41)–(BR44)、\(\nu=G_{00}/\det G_\infty\)、
唯一の projective null line と元の \(L^2\) 空間での方向収束を独立に確認し PASS とした。
最小 energy の次項・符号はこの監査結果にも含まれない。
