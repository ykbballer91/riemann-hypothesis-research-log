**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/full_ground_capture/notes/moment_asymptotic.md` · Original SHA-256: `f633625f109e913be7f21dc91e7df35b69a3405e94b314191a164e9126a7c6ec`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Actual ξ-weight の偶数モーメントと cyclicity

**STATUS: RIEMANN HYPOTHESIS OPEN**

2026-09-30。Priority 1（cyclicity）のみ。新規性を主張しない。
旧研究・公開監査snapshotは読み取りのみ。有限head、増大する微分次数の
uniform selection、全ground captureは本ノートの対象外である。

## MA1. 規約と結論

[既存SH1](../../hierarchical_selection/notes/support_hierarchy.md)と同じく
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\mathscr X(x)=\xi(\tfrac12+ix),\qquad
\widehat k(x)=\mathscr X(x)/4,\quad k=\Phi/4.
\tag{MA1}
\]
Fourier変換は \(\widehat f(x)=\int_{\mathbb R}f(t)e^{-ixt}\,dt\)。
偶数階微分には反対符号のFourier規約でも同じ式が成り立つ。
以下のモーメントは確率規格化せず、両半直線を含む
\[
d\mu(x)=|\mathscr X(x)|^2dx,\qquad
m_{2n}=\int_{\mathbb R}x^{2n}\,d\mu(x),\qquad n\ge0
\tag{MA2}
\]
である。\(\mu\) は有限・偶・正測度で、全モーメントを持つ。
\(a=\pi/2\)、\(v=2n+9/2\)、\(\psi=\Gamma'/\Gamma\) とすると、無条件に
\[
\boxed{
m_{2n}=\sqrt{2\pi}\,\frac{\Gamma(v)}{a^v}
\left\{\psi(v)+2\gamma-\log(\pi^2)+O(v^{-1/12})\right\}.}
\tag{MA3}
\]
従って特に
\[
m_{2n}\sim \sqrt{2\pi}\,
\frac{\Gamma(2n+9/2)}{(\pi/2)^{2n+9/2}}\log n,
\qquad
m_{2n}^{-1/(2n)}\sim\frac{e\pi}{4n}.
\tag{MA4}
\]
最初の漸近式は \(n\to\infty\) の意味であり、\(n=0,1\) へ代入する近似ではない。
さらに括弧内は \(\log n+\log2+2\gamma-2\log\pi+o(1)\)。

**依存の分離。** MA3の鋭い係数と加法定数には、既知の無条件平均二乗誤差を使う。
全モーメント、Carleman条件、モーメント決定性、偶多項式の密度、
\(\overline{\operatorname{span}\{k^{(2j)}:j\ge0\}}=L^2_{\rm even}(\mathbb R)\)
にはその強い平均二乗入力は不要である。MA2以降の正測度は
actual Weil形式の正値性を仮定したものではない。

## MA2. 初等上界だけで全モーメントとCarleman

整数 \(N\ge1\)、\(\Re s>0\)、\(s\ne1\) に対するEuler summationは
\[
\zeta(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1}
-s\int_N^\infty\{u\}u^{-s-1}\,du.
\tag{MA5}
\]
まず \(\Re s>1\) で部分積分し、右辺の正則性により指定領域へ延長できる。
\(s=1/2+it\)、\(N=\lceil1+|t|\rceil\) とすれば
\[
|\zeta(1/2+it)|\ll(1+|t|)^{1/2}.
\tag{MA6}
\]
ここでは三項を絶対値で抑えるだけでよく、convexity、RH、Lindelöfは不要。
\(N=1\) のさらに粗い \(O(1+|t|)\) でも以下の目的には十分である。

Stirlingから、\(t\ge1\) において
\[
\begin{aligned}
|\mathscr X(t)|^2
&=\frac{(t^2+1/4)^2}{4\sqrt\pi}
 |\Gamma(1/4+it/2)|^2|\zeta(1/2+it)|^2,\\
|\Gamma(1/4+it/2)|^2
&=2\pi(t/2)^{-1/2}e^{-\pi t/2}\{1+O(t^{-1})\},\\
|\mathscr X(t)|^2
&=\sqrt{\pi/2}\,t^{7/2}e^{-at}
 |\zeta(1/2+it)|^2\{1+O(t^{-1})\}.
\end{aligned}
\tag{MA7}
\]
定数には \(s(s-1)\)、\(t/2\)、最後の両半直線の因子2を全て保持した。
Stirlingの規約は[DLMF 5.11.1, 5.11.3, 5.11.9](https://dlmf.nist.gov/5.11)
と照合した。相対誤差 \(O(t^{-1})\) で十分であり、より細かい展開は不要。

従って
\[
|\mathscr X(t)|^2\le C(1+|t|)^{9/2}e^{-a|t|},\qquad
\int e^{b|t|}\,d\mu(t)<\infty\quad(0\le b<a),
\tag{MA8}
\]
および、\(C\) を調整して全 \(n\ge1\) に
\[
m_{2n}\le C\left(1+a^{-2n-11/2}\Gamma(2n+11/2)\right).
\tag{MA9}
\]
実軸のStirlingを右辺へ適用すれば
\(m_{2n}^{1/(2n)}\le C'(n+1)\)。ゆえに
\[
\sum_{n\ge1}m_{2n}^{-1/(2n)}=\infty.
\tag{MA10}
\]
これは \(\mu\) に対するHamburger Carleman条件である。
MA3/MA4を使わずに成立する点が重要。

## MA3. 鋭い平均式に使う既知入力と帰属

\[
M(T)=\int_0^T|\zeta(1/2+it)|^2dt
=T\log(T/(2\pi))+(2\gamma-1)T+E(T).
\tag{MA11}
\]
採用する一次文献はAleksander Simonič and Valeriia V. Starichkova,
*Atkinson's formula for the mean square of ζ(s) with an explicit error term*,
[arXiv:2105.06821v3](https://arxiv.org/html/2105.06821v3)（2022-12-13）、
J. Number Theory 244 (2023), 111–168。
同v3の式(1)、Corollary 1・式(15)（PDF p.4）、
§7 Theorem 3（PDF p.41）とその直後の証明を照合した。
同定理は、固定した十分大きい \(T_0\) と \(T\ge1.1T_0\) で
\[
|E(T)|\le J(T_0)T^{1/3}(\log T)^{5/3}
\tag{MA12}
\]
を与える。有限区間では定数を拡大できるので、本ノートで使う弱い帰結は
\[
E(T)=O((1+T)^{5/12}).
\tag{MA13}
\]
原著の全42頁を再証明・機械検証したという意味ではなく、既知定理を入力として使う。
当該一次原著の版と定理、必要な帰結を固定したものである。

**帰属訂正。** \(T^{1/3}\log^2T\) をInghamに帰属させない。
同v3の序論・式(2)はInghamに \(\sqrt T\log T\) を、式(12)は
\(T^{1/3}\log^2T\) をMotohashiに帰属する。今回は未取得のIngham原版や
Motohashi原版を直接確認済みとは記載せず、MA12を採用する。

## MA4. 集中するLaplace重みへの誤差転送

必要な一般補題を示す。\(0\le\theta<1/2\) とし、MA11の誤差が
\(|E(t)|\le C(1+t)^\theta\) を満たすとする。
固定 \(a>0\)、\(v\to\infty\) に対し
\[
J_v:=\int_0^\infty t^{v-1}e^{-at}|\zeta(1/2+it)|^2dt
=\frac{\Gamma(v)}{a^v}
\left\{\psi(v)-\log(2\pi a)+2\gamma
+O(v^{\theta-1/2})\right\}.
\tag{MA14}
\]

証明：\(w_v(t)=t^{v-1}e^{-at}\) とする。MA11の主項を微分すれば
\(\log(t/(2\pi))+2\gamma\) であり、Gamma積分とその \(v\) 微分から
MA14の主項が正確に得られる。誤差はStieltjes部分積分により
\[
\int_0^\infty w_v(t)\,dE(t)=-\int_0^\infty w_v'(t)E(t)\,dt.
\tag{MA15}
\]
\(v>2\) なら0での境界項は消え、無限大ではexponential重みが消す。
\(X\) をshape \(v\)、rate \(a\) のGamma分布とすれば、正規化した誤差は
\[
\left|\frac{a^v}{\Gamma(v)}\int w_v\,dE\right|
\le C\,\mathbb E\left[
\left|\frac{v-1}{X}-a\right|(1+X)^\theta\right].
\tag{MA16}
\]
負モーメントを直接積分すると
\[
\mathbb E(X^{-1})=\frac a{v-1},\quad
\mathbb E(X^{-2})=\frac{a^2}{(v-1)(v-2)},\quad
\mathbb E\left[\left(\frac{v-1}{X}-a\right)^2\right]=\frac{a^2}{v-2}.
\tag{MA17}
\]
またGamma比または \(0\le2\theta<1\) の凹性により
\(\mathbb E(1+X)^{2\theta}=O(v^{2\theta})\)。Cauchy–Schwarzで
MA16は \(O(v^{\theta-1/2})\)、従ってMA14が成立する。
MA13により \(\theta=5/12\) を取れば誤差は \(O(v^{-1/12})=o(1)\)。

この一段が必要な理由は、重みの中心が \(t\asymp v\)、幅が
\(\asymp\sqrt v\) だからである。全域平均 \(M(T)\sim T\log T\) だけから
この集中幅で正しい係数を取り出せると推論していない。
誤差を絶対積分してもよいが、\(w_v'\) の \(v^{-1/2}\) のgainを
失わない評価が必要である。

## MA5. MA3の完成と正規化

MA7の相対 \(O(t^{-1})\) を使い、\(v=2n+9/2\) とすると
\[
m_{2n}=\sqrt{2\pi}\,J_v+O(J_{v-1})+O(1).
\tag{MA18}
\]
最後の有界項は \(0\le t\le1\) を分離したもの。
MA14を \(v-1\) にも適用すれば
\[
\frac{J_{v-1}}{\Gamma(v)a^{-v}}=O(\log v/v).
\tag{MA19}
\]
\(O(1)/(\Gamma(v)a^{-v})\) も無視できる。
\(2\pi a=\pi^2\) を代入してMA3が得られる。
\(\psi(v)=\log v+O(v^{-1})\) と実StirlingからMA4も従う。

本ノートの \(m_{2n}\) と物理側のSobolev normには
\[
\int x^{2n}|\widehat k(x)|^2dx=\frac{m_{2n}}{16},\qquad
\|k^{(j)}\|_2^2=\frac{m_{2j}}{32\pi},\qquad
\|k^{(2j)}\|_2^2=\frac{m_{4j}}{32\pi}
\tag{MA20}
\]
という関係がある。\(1/16\) とPlancherelの \(1/(2\pi)\) を混同しない。

## MA6. 決定性と偶多項式の密度を直接確認する

Carlemanという名称だけに依存しない短い証明を付す。
MA8から任意 \(0<b<a\) について指数momentが有限。
もし正測度 \(\widetilde\mu\) が \(\mu\) と全モーメントを共有すれば、
単調収束により
\[
\int\cosh(bx)\,d\widetilde\mu
=\sum_{n\ge0}\frac{b^{2n}m_{2n}}{(2n)!}
=\int\cosh(bx)\,d\mu<\infty.
\tag{MA21}
\]
両測度のFourier–Laplace変換は \(|\Im z|<b\) に正則で、0での全Taylor係数が一致。
一致定理と有限測度のFourier変換の一意性から \(\widetilde\mu=\mu\)。
すなわちHamburger moment problemはdeterminateである。

次に \(h\in L^2(\mu)\) が全多項式に直交するとする。
\(0<r<a/2\) ならCauchy–Schwarzにより
\[
\int |h(x)|e^{r|x|}\,d\mu(x)
\le\|h\|_{L^2(\mu)}
\left(\int e^{2r|x|}\,d\mu(x)\right)^{1/2}<\infty.
\tag{MA22}
\]
従って \(F_h(z)=\int h(x)e^{-izx}\,d\mu(x)\) は \(|\Im z|<r\) に正則。
全導関数が0で消えるため \(F_h=0\)、Fourier一意性で \(h=0\) \(\mu\)-a.e.。
これは全多項式が \(L^2(\mu)\) に稠密であることの直接証明である。
\(\mu\) が偶なので、偶関数への有界射影により
\[
\overline{\{p(x^2):p\text{ polynomial}\}}^{L^2(\mu)}
=L^2_{\rm even}(\mu).
\tag{MA23}
\]

\(y=x^2\) によるpushforwardは
\[
d\nu(y)=\frac{|\mathscr X(\sqrt y)|^2}{\sqrt y}\,dy\quad(y>0),
\qquad \nu_n=m_{2n}.
\tag{MA24}
\]
これはStieltjes問題であり、適用するCarleman和は
\(\sum\nu_n^{-1/(2n)}=\infty\)。対称square-root liftを用いれば
\(\mu\) のHamburger決定性から \(\nu\) のStieltjes決定性も直接従う。
一方、\(\nu\) にHamburger型の \(\sum\nu_{2n}^{-1/(2n)}\) を代入すると
項は \(O(n^{-2})\) で和は収束する。これはその十分条件の不成立にすぎず、
\(\nu\) の不定性を意味しない。

## MA7. Priority 1への帰結と停止範囲

\(\mathscr X\) は非零entire関数なので、実軸の零点集合はLebesgue null。
従って \(h\mapsto\mathscr X h\) は \(L^2(\mu)\) から
\(L^2(dx)\) へのonto isometryである。
逆は零点集合以外で \(g\mapsto g/\mathscr X\) と定義する。
\(\mathscr X\) は偶なので、この写像はeven sectorも保つ。
MA23とPlancherel、\(\widehat{k^{(2j)}}=(-1)^jx^{2j}\mathscr X/4\) から
\[
\boxed{\overline{\operatorname{span}\{k^{(2j)}:j\ge0\}}^{L^2(dx)}
=L^2_{\rm even}(\mathbb R).}
\tag{MA25}
\]
実零点が存在しても、その点集合はnullなのでこの密度を妨げない。
複素零点の位置については一切仮定していない。

これは**無条件のL² cyclicity**である。Weil form normでのdensity、
cutoffとの一様交換、次数 \(m\) を増やすときの安定性、finite-head capture、
全groundとのgap比較、ES、G*、RHを証明したものではない。
Priority 2以降へ移らず、ここで停止する。

独立検算：別担当はMA7の係数、MA14の主項、MA17のGamma score恒等式、
MA4のCarleman定数を確認した。平均二乗入力の原典自体の独立再監査とは区別する。

**STATUS: RIEMANN HYPOTHESIS OPEN**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/hierarchical_selection/notes/support_hierarchy.md`](../../hierarchical_selection/notes/support_hierarchy.md)
