**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/global_remainder/notes/completed_two_sided.md` · Original SHA-256: `2212d7de24a1f22e341513ddea36ed87f33cda6afed89058753a94330061aa01`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 完成関数の双側逆変換：積分路と temperedness の限定監査

記録日: 2026-09-30。Track B の内部導出と一次資料による規約確認。実際の Euler/Gamma 因子を保持する。RH の証明・反証、新規性、零点から構成した正定値計量は主張しない。旧 track は変更しない。

**判定:** 右側の算術的逆変換を先に固定すれば、その temperedness は RH の十分条件となる。ただしこの temperedness は零点多重度の一様有界性も要求し、ここでは RH からの逆含意を証明していない。中央線の Fourier/PV 逆変換を先に選び「tempered にした」ことは、右側の逆変換の評価にはならない。有限極の厳密模型で両者は異なる。

## CT1. 規約、極、無条件に定義できる逆変換

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 \Xi(z)=\xi(\tfrac12+z),\qquad E(z)=e^{z^2},\qquad
 G(z)=\frac{E(z)}{\Xi(z)}.
\]

\(\Xi\) と \(G\) は偶・real entire/meromorphic、\(E\) は非消失である。非自明零点 \(\rho\) の重複度が \(m_\rho\) なら、\(G\) は \(z_\rho=\rho-\tfrac12\) に**同じ次数**の極を持つ。\(z=\pm\tfrac12\) は \(G\) の極ではない。完成関数の規約と反射は [NIST DLMF 25.4.3–25.4.4](https://dlmf.nist.gov/25.4) に一致する。

固定 \(c>\tfrac12\) で
\[
 H_c(u)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}G(z)e^{zu}\,dz
       =\frac{e^{cu}}{2\pi}\int_\mathbb R G(c+it)e^{itu}\,dt. \tag{CT1}
\]

これは実数 \(u\) で絶対収束し、実数値を持つ。実際、\(\sigma=\tfrac12+c>1\) では
\[
 |\zeta(\sigma+it)^{-1}|
 \le\sum_{n\ge1}|\mu(n)|n^{-\sigma}\le\zeta(\sigma).
\]
固定実部の Stirling 評価より
\[
 |G(c+it)|\ll_c
 e^{-t^2+\pi|t|/4}(1+|t|)^{-7/4-c/2}.                 \tag{CT2}
\]
\(\Gamma(\sigma/2+it/2)\) の冪は \(\sigma/2-\tfrac12\)、さらに \(s(s-1)\) が二次であることを用いた。[DLMF 5.11.9](https://dlmf.nist.gov/5.11#E9)

縦方向の任意階微分も Schwartz となる。これは絶対収束する \(1/\zeta\) の微分級数と、Gamma の Stirling 評価/Cauchy 評価から従う。従って \(e^{-cu}H_c(u)\in\mathcal S(\mathbb R)\)。また Gaussian が \(e^{-t\operatorname{Im}u}\) を吸収するので、\(H_c\) は複素 \(u\) にも entire に延びる。ここで \(E\) は縦方向に減衰するだけで、全方向で減衰する関数ではない。

二つの \(c,C>\tfrac12\) の間には極がなく、有限幅の水平線上でも (CT2) 型の評価が一様なので \(H_c=H_C\)。以下この固定された関数を \(H\) と書く。特に
\[
 |H^{(j)}(u)|\le C_{C,j}e^{Cu}\quad(C>\tfrac12)
                                                               \tag{CT3}
\]
であり、負の方向は任意の指数より速く減衰する。一方、正の方向に現段階で得たものは \(O_c(e^{cu})\) だけである。\(C\to0\) は許されていない。また Gaussian 正則化後の \(H\) を、負半軸で厳密にゼロの causal function と呼ばない。

## CT2. 左右の積分路、留数、対称化

同じ upward orientation で左側を定義すると、偶性と \(z\mapsto-z\) の置換から
\[
 H_{-c}(u)=H_c(-u).                                     \tag{CT4}
\]
これは \(H_c(u)=H_c(-u)\) ではない。対称性は被積分関数と積分路を同時に移す。

高さ \(\pm T\) に極がないとき、切断積分を \(H_{\pm c,T}\) とし、水平辺を右上から左上、左下から右下へ向けると
\[
 H_{c,T}(u)-H_{-c,T}(u)
 =\sum_{\substack{|\Re z_\rho|<c\\|\Im z_\rho|<T}}
       \operatorname{Res}_{z=z_\rho}(G(z)e^{zu})
 -\frac1{2\pi i}\left(\int_{\rm top}+\int_{\rm bottom}\right)
             G(z)e^{zu}\,dz.                            \tag{CT5}
\]
これは有限和の厳密恒等式であり、重複零点も含む。両縦辺は \(T\to\infty\) で収束する。従って右辺全体の極限は \(H(u)-H(-u)\)。水平辺を捨てた無限留数和を使うには、別途その水平辺が消える高さ列と収束方式の証明が要る。本監査の temperedness 判定はその無限和を必要とせず、絶対収束を仮定しない。

極 \(a\) の Laurent 主部を \(\sum_{k=1}^m c_{a,-k}(z-a)^{-k}\) とすれば
\[
 \operatorname{Res}_a(G(z)e^{zu})
 =e^{au}P_a(u),\qquad
 P_a(u)=\sum_{k=1}^m c_{a,-k}\frac{u^{k-1}}{(k-1)!}.    \tag{CT6}
\]
\(\deg P_a=m-1\) で最高係数は非零。偶性より
\(c_{-a,-k}=(-1)^k c_{a,-k}\)、従って \(\pm a\) の寄与は
\[
 e^{au}P_a(u)-e^{-au}P_a(-u).                           \tag{CT7}
\]
共役極では係数も共役となる。単純な軸外 quartet
\(a=\alpha+i\gamma,-a,\bar a,-\bar a\)、\(\alpha,\gamma>0\) の寄与は
\[
 4\Re\!\left(r_a\sinh(au)\right),\qquad
 r_a=\frac{e^{a^2}}{\Xi'(a)}.                           \tag{CT8}
\]
これは一般に純粋な \(\cosh\) ではなく、
\(4[\Re r_a\,\sinh(\alpha u)\cos(\gamma u)
-\Im r_a\,\cosh(\alpha u)\sin(\gamma u)]\)。
振動するので、その絶対値が各点で \(C e^{\alpha|u|}\) 以上という下界は出ない。無限個の異なる寄与に対して、最大指数一項が支配すると仮定もしない。

\[
 S(u)=H(u)+H(-u),\qquad D(u)=H(u)-H(-u)
\]
はそれぞれ偶・奇である。しかし \(H(-u)\) は \(u\to+\infty\) で急減衰するため、\(S\) または \(D\) が tempered なら \(H\) も tempered となる。実際、正半軸 cutoff 上では \(H\) と \(S,D\) の差が Schwartz、負側の \(H\) 自体も Schwartz である。従ってこの**左右の同じ算術的逆変換から作った**対称化は、増大 obstruction を投影で消す操作ではない。対称化したというだけで tempered になったわけでもない。

## CT3. 実際の Euler/Gamma 因子を残す展開

\[
 A(z)=\frac{2e^{z^2}\pi^{z/2+1/4}}
            {(z^2-1/4)\Gamma(z/2+1/4)},\qquad
 G(z)=A(z)\sum_{n\ge1}\mu(n)n^{-1/2}e^{-z\log n}
 \quad(\Re z>\tfrac12).                                \tag{CT9}
\]
\(a_c(v)=(2\pi i)^{-1}\int_{(c)}A(z)e^{zv}\,dz\) と置けば
\[
 H(u)=\sum_{n\ge1}\mu(n)n^{-1/2}a_c(u-\log n).          \tag{CT10}
\]
固定 \(c>\tfrac12\) で \(|a_c(v)|\le C_c e^{cv}\) なので、この交換と和は
\(C_c e^{cu}\sum n^{-c-1/2}<\infty\) により正当化できる。微分も同様。

これは arithmetic を失わない exact formula だが、絶対値を取れば依然 \(e^{cu}\) の評価である。Möbius の符号付き相殺を独立に評価していない。\(A\) の \(z=\tfrac12\) の極は完成された \(G\) では \(1/\zeta\) の零点により消えるので、Gamma 側と Euler 側を別々に「正」と扱ってこの cancellation を省略することもできない。

## CT4. 右側の \(H\) が tempered なら RH：無限留数和を使わない証明

**仮定:** (CT1) で先に定義した smooth function \(H\) が、その regular distribution として \(\mathcal S'(\mathbb R)\) に属する。

固定 smooth cutoff \(\eta\) を \(\eta=0\) on \(u\le0\)、\(\eta=1\) on \(u\ge1\) とする。すると
\[
 \mathcal L_H(z)=
 \langle H,\eta(u)e^{-zu}\rangle
 +\int_\mathbb R(1-\eta(u))H(u)e^{-zu}\,du               \tag{CT11}
\]
は \(\Re z>0\) で正則である。第1項では \(\eta e^{-zu}\in\mathcal S\) が同半平面で Schwartz topology に関して正則。第2項では (CT3) の任意指数減衰により全平面で正則。両者とも compact subset ごとに微分を正当化できる。

\(\Re z=c>\tfrac12\) では Fourier inversion により
\[
 \int_\mathbb R H(u)e^{-zu}\,du=G(z).                   \tag{CT12}
\]
収束は \(e^{-cu}H\in\mathcal S\) で保証される。従って (CT11) は (CT9) と同じ meromorphic function を \(\Re z>0\) に正則延長する。\(E\) が非消失である以上、\(\Xi\) はこの半平面でゼロを持てない。反射対称性で左半平面も排除され、全零点は \(\Re z=0\)、すなわち RH となる。

この distributional Laplace の cutoff 操作は、Schwartz の一次講義録 *Lectures on Partial Differential Equations and Representations of Semi-groups*, Lecture 8, Propositions 8.4–8.5 と Definition 8.4（印刷 pp42–43、PDF pp50–51）にある半直線支持の場合の構成と整合する。本ノートでは負側の急減衰項を別に足して直接証明した。[TIFR 原本](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr11.pdf)

**逆含意の注意。** \(H\in\mathcal S'\) の有限個の seminorm による連続性を (CT11) に使うと、ある固定整数 \(N\) に対し
\[
 |G(\sigma+it)|\le C(1+|t|)^N\sigma^{-N},
          \qquad 0<\sigma\le1.                         \tag{CT13}
\]
必要なら \(N\) を増やす。第2項はこの範囲で \(t\) に一様に有界、第1項は
\(\sup_u(1+|u|)^N|\partial_u^j(\eta e^{-zu})|\) で評価する。

各 \(i\gamma\) に固定して \(\sigma\downarrow0\) とすれば、その極次数は \(N\) 以下。したがってこの temperedness は**全零点の多重度の一様上限**も含む。\(e^{z^2}\neq0\) は pole order を変えず、この問題を消さない。RH から必要な boundary estimates、multiplicity/residue の一様制御をこの監査では導いていない。従って「RH と temperedness は同値」とは採用しない。有限個の極だけで成立する逆推論を、無限個の算術零点へ移さない。

**L² はもっと強すぎる。** もし \(H\in L^2(\mathbb R)\) なら、正側の Cauchy–Schwarz と負側の急減衰から
\[
 |G(\varepsilon+i\gamma)|
 \le \frac{\|H\|_{L^2(0,\infty)}}{\sqrt{2\varepsilon}}+O(1),
 \qquad \varepsilon\downarrow0.                        \tag{CT14a}
\]
ここで Laplace transform は \(\Re z>0\) で正則に定義され、(CT12) との一致から meromorphic continuation に一致する。ところが臨界線上には無条件で既知の零点があり、固定したその一点で \(G(\varepsilon+i\gamma)\sim c_\gamma\varepsilon^{-m}\)、\(m\ge1\)、\(c_\gamma\neq0\)。矛盾する。従って **この \(H\) は無条件に L² ではない**。RH を仮定してもこの障害は残る。臨界線上の零点の存在に関する標準的事実の確認先は [DLMF 25.10(i)](https://dlmf.nist.gov/25.10#i)。

特に実際の \(H\) は偶関数ではない。もし偶なら (CT3) の負側の急減衰が正側にも移り、\(H\in L^2\) となるからである。

同じ argument は、別 track の実際の未完成 Gaussian 和
\[
 R(u)=\sum_{n\ge1}\mu(n)e^{-(u-\log n)^2},\qquad
 A(u)=e^{-u/2}R(u)
\]
にも適用できる。その右側 Laplace transform は
\(\sqrt\pi e^{(z+1/2)^2/4}/\zeta(z+1/2)\) で、負側は Gaussian tail、numerator は非消失である。従って \(A\notin L^2\) も同じ結論。ただし \(A\) と (CT1) の完成関数 \(H\) は異なる対象であり、両者を同一視しない。

一方、正側に \(|H(u)|\le C(1+u)^d\)（\(d\ge0\)）を仮定した場合は
\(|G(\varepsilon+i\gamma)|=O(\varepsilon^{-d-1})\) だから \(m\le d+1\) を要求する。特に bounded は \(m\le1\)。これらも各条件の**必要な帰結**であり、simple zeros/RH だけから boundedness が従うという逆向きはここでは示していない。

## CT5. 中央線を選ぶだけで極を隠せる厳密模型

まず \(a>0\)、\(G_0(z)=1/(z^2-a^2)\)。中央線 \(\Re z=0\) の逆 Fourier 変換と、両極の右 \(\Re z=c>a\) の逆 Laplace 変換は、それぞれ
\[
 K_0(u)=-\frac{e^{-a|u|}}{2a},\qquad
 K_R(u)=\mathbf1_{\{u\ge0\}}\frac{\sinh(au)}a.          \tag{CT14}
\]
直接変換すると \(K_0\) の bilateral Laplace は \(|\Re z|<a\) で \(G_0\)、\(K_R\) のものは \(\Re z>a\) で \(G_0\)。同じ meromorphic formula でも**一致を要求する strip が異なる**。前者は tempered だが \(\pm a\) の極は実際に残っている。

今回と同じ固定 Gaussian \(E\) まで保った模型にする。\(g(u)=(2\sqrt\pi)^{-1}e^{-u^2/4}\)、その bilateral Laplace transform は \(e^{z^2}\) である。よって \(e^{z^2}/(z^2-a^2)\) の二つの逆変換は
\[
 K_C=g*K_0,\qquad K_R^{E}=g*K_R,\qquad
 K_R^{E}(u)-K_C(u)=\frac{e^{a^2+au}}{2a}.              \tag{CT15}
\]
最後は右へ移したときに横切る \(a\) の留数そのもの。\(K_C\) は smooth exponential-decaying、従って Schwartz。一方 \(K_R^E\) は \(u\to+\infty\) で指数増大し、負側は Gaussian tail となる。さらに
\[
 K_R^E(u)-K_R^E(-u)=e^{a^2}\frac{\sinh(au)}a,
\quad
 K_R^E(u)+K_R^E(-u)=\frac{e^{a^2}\cosh(au)}a+2K_C(u).
\]
Gaussian convolution も even symmetrization も、正しい右側から取った極寄与を消していない。

複素 quartet や高重複度でも同じ論点が残る。例えば
\[
 G_m(z)=\frac{e^{z^2}}
 {[(z-a)(z+a)(z-\bar a)(z+\bar a)]^m},
 \quad \Re a>0,\ \Im a>0,
\]
は偶・real meromorphic で、中央線上に極がない。その中央線 restriction は Schwartz なので逆 Fourier 変換も Schwartz。しかし四つの軸外極は次数 \(m\) のままであり、全極の右からの逆変換との差は右半平面の有限留数和 \(e^{au}P(u)+e^{\bar a u}\overline{P(u)}\) である。これを tempered な中央線 object と同一視してはならない。

これらは完成 \(\zeta\) 自体ではなく、**contour choice だけを growth theorem と取り違える推論**への反例である。実際の \(\Xi(it)\) には無限個の零点があるので、中央線の PV/finite-part 分布を採用する場合も、その存在・大域的 temperedness・境界値の向きは別の義務となる。

## CT6. 残った入力と停止判定

- 実際に構成済み: 右側の \(H\)、任意指数の負側減衰、Euler/Gamma を保つ (CT10)、有限高さの留数恒等式、\(H_{-c}(u)=H_c(-u)\)。
- 条件付きで証明済み: この同じ \(H\) の temperedness（または同じ \(H\) からの \(S,D\) の temperedness）なら RH。ただし多重度の一様上限も要求する。
- 未供給: 正側の必要な growth bound。偶性、Gaussian regularization、symmetrization、別 contour の tempered Fourier inverse はその bound ではない。
- 不採用: 軸外 quartet から振動を無視した点ごとの指数下界、無条件の絶対留数和、RH からの無検証な temperedness、中央線への contour 変更を算術的相殺と呼ぶこと。

この track は剰余を正確な対象へ固定し、誤った symmetrization/contour closure を排除した。独立な算術的相殺評価はまだ得ていない。RH は OPEN。
