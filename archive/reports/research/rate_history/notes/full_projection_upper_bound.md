**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/rate_history/notes/full_projection_upper_bound.md` · Original SHA-256: `46da953ab9ae37bf2dcf5740d1053df097a530b1bc0bdac95b15502f15614121`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Full support-plus-Fourier projection: unconditional recognition upper bound

2026-09-30。RH OPEN。固定された derivative family についての限定補題。
actual Weil form、sharp support、既存の \(P_N\)、標準 \(L^2(dt)\) を使う。
旧ファイルは変更しない。新規性・leading asymptotic・ground selection を主張しない。

## 1. 主張と量化

既存の規約で actual even log kernel を \(k(t)\) と書く：
\[
 \widehat k(z)=\int_{\mathbb R}k(t)e^{-izt}dt=\Xi(z)/4,\qquad
 \Xi(z)=\xi(1/2+iz).
\]
固定 \(m\ge0\) に対して
\[
 f_j=k^{(2j)},\quad 0\le j\le m,\qquad
 a=\log\lambda\ge1,\quad
 \omega_n=\pi n/a,\quad \Omega=\pi(N+1)/a\ge1,\quad N\ge1,
\]
\[
 p_j=T_{a,N}f_j
   =P_N(f_j|_{[-a,a]})\quad\text{を区間外 0 として延長する}.
\]
Fourier basis は \(V_n(t)=(2a)^{-1/2}e^{i\omega_n(t+a)}\)。
以下の定数は固定 \(m\) と actual kernel に依存してよいが、\(a,N\) には依存しない。

\[
 \boxed{\quad
 |Q_W(p_i,p_j)|
 \le C_m\left[
 a(1+\Omega)^{4m+8}
       e^{\,a-\pi\Omega/2}
 +\lambda^{8m+24}e^{-2\pi\lambda^2}
 \right],\qquad 0\le i,j\le m .
 \quad}
 \tag{1}
\]
多項式指数は便宜的に大きく取った上界であり、最適性はない。
未知定数 \(C_m\) の数値的 interval certificate を今回生成したわけではない。
構成する \(p_j\) に個別零点の位置を入力しない。

したがって実験の二経路
\[
 N=\max(4,\lceil a^2\rceil),\qquad
 N=\max(4,\lceil a^3\rceil)
 \tag{2}
\]
のどちらでも、固定 \(m\) の全 recognition matrix \(M_{ij}=Q_W(p_i,p_j)\)
は無条件に 0 へ行く。これは signed recognition の絶対上界であり、
energy の符号、first nonzero term、最速方向を同定しない。

## 2. 実軸 Fourier decay と actual theta tail

\[
 \widehat f_j(\omega)=(-1)^j\omega^{2j}\Xi(\omega)/4.
\]
Gamma の vertical Stirling formula
[DLMF 5.11.9](https://dlmf.nist.gov/5.11#E9) は
\[
 |\Gamma(1/4+i\omega/2)|
 \le C(1+|\omega|)^{-1/4}e^{-\pi|\omega|/4}
 \tag{3}
\]
を与える。ここで必要な zeta bound は無条件の粗い多項式 bound だけ。
実際、Euler summation から \(\Re s>0,\ s\ne1\) で
\[
 \zeta(s)=\frac{s}{s-1}
          -s\int_1^\infty\{x\}x^{-s-1}dx
 \tag{4}
\]
となり、\(\Re s=1/2\) では \(|\zeta(s)|\le C(1+|\Im s|)\)。
(4) は \(\Re s>1\) の \(\lfloor x\rfloor=x-\{x\}\) による部分積分を
右半平面へ解析接続した恒等式である。
\(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\) と合わせて
\[
 |\widehat f_j(\omega)|
 \le C_m(1+|\omega|)^d e^{-c|\omega|},\qquad
 d=2m+3,\quad c=\pi/4.
 \tag{5}
\]
RH、subconvexity、零点密度の改良は使用しない。

actual theta expansion の各導関数は、\(t\ge1\) で
polynomial in \(n^2e^{2t}\) を掛けた \(e^{-\pi n^2e^{2t}}\) の和である。
例えば最高 power の粗い評価として、\(j\le m,\ r=0,1,2\) なら
\[
 |f_j^{(r)}(t)|
 \le C_m e^{(4m+2r+9/2)t}e^{-\pi e^{2t}}.
 \tag{6}
\]
\(n\ge2\) の和は \(e^{-\pi(n^2-1)e^{2t}}\) で一様に抑えられる。
偶性から左端にも同じ bound がある。
従って
\[
 B_j(a):=2\left(|f_j'(a)|+\int_a^\infty|f_j''(t)|dt\right)
 \le C_m\lambda^{4m+9}e^{-\pi\lambda^2},
 \tag{7}
\]
また \(|f_j(a)|\) と
\(\int_{|t|>a}e^{|t|/2}(|f_j(t)|+|f_j'(t)|)dt\)
にも polynomial in \(\lambda\) times \(e^{-\pi\lambda^2}\) の上界がある。
固定 normalization の定数は \(C_m\) に含める。

Fourier/actual radical の既知入力は
[CCM 2310.18423v2, §3.6 Proposition 3.6](https://arxiv.org/html/2310.18423v2#S3.SS6)
の polynomial-times-\(\Xi\) framework と、
[Connes–Consani, 公刊版 §3 p.118](https://ems.press/content/serial-article-files/44477)
の summation-range radical。
今回の scalar \(1/4\) と log-coordinate は
[既存の独立 domain 検算 §7](../../common_parent/notes/variational_limits_and_prior_art.md)
に固定する。原著が本稿 (1) を既に述べているとの主張ではない。

## 3. Grid 上の二回積分が cutoff tail を制御する

まず固定 \(f=f_j\) と書く。periodic Fourier coefficient は exact に
\[
 c_n=\langle f|_{[-a,a]},V_n\rangle
 =\frac{(-1)^n}{\sqrt{2a}}\left(\widehat f(\omega_n)-T_a(\omega_n)\right),
 \qquad
 T_a(\omega)=2\int_a^\infty f(t)\cos(\omega t)\,dt.
 \tag{8}
\]
\(n\ne0\) では \(\sin(\omega_na)=0,\ \cos(\omega_na)=(-1)^n\)。
二回の積分部分積分で
\[
 T_a(\omega_n)
 =-\frac{2}{\omega_n^2}
    \left((-1)^n f'(a)+\int_a^\infty f''(t)\cos(\omega_nt)\,dt\right),
 \qquad |T_a(\omega_n)|\le B_j(a)/\omega_n^2.
 \tag{9}
\]
この \(1/\omega_n^2\) は grid と偶性によるもので、
任意の real frequency の sharp tail に同じ bound を課したのではない。

\(e=p-f\) を区間の内側で定義する。
\(f(a)=f(-a)\) なので restriction は periodic \(H^1\) に入り、
\[
 \|e\|_{H^1(-a,a)}^2
 =\sum_{|n|>N}(1+\omega_n^2)|c_n|^2.
 \tag{10}
\]
spacing \(h=\pi/a\)、\(\Omega=h(N+1)\) の elementary sum bounds より
\[
 \begin{split}
 \|e\|_{H^1(-a,a)}
 &\le C_m(1+\Omega)^{d+1}e^{-c\Omega}
           +C B_j(a)\Omega^{-1/2},\\
 |e(a)|=|e(-a)|
 &\le C_m(1+\Omega)^d e^{-c\Omega}
           +C B_j(a)\Omega^{-1}.
 \end{split}
 \tag{11}
\]
例えば
\(a^{-1}\sum_{n>N}\omega_n^{-2}\le C/\Omega\)、
\(a^{-1}\sum_{n>N}\omega_n^{-4}\le C/\Omega^3\)、
および
\[
 \frac1a\sum_{n>N}(1+\omega_n)^q e^{-b\omega_n}
 \le C_{q,b}(1+\Omega)^q e^{-b\Omega}
 \tag{12}
\]
を使う。\(a,\Omega\ge1,\ N\ge1\) で定数を一様にできる。
trace bound は \(\sum|c_n|<\infty\) による一様収束から取る。
sharp zero extension が全実線の \(H^1\) に入るとは主張しない。

## 4. Weighted BV norm と strip 全体の Fourier bound

全実線上で \(\delta=p-f\) とし、distributional derivative の全変動を含めて
\[
 \mathcal B(\delta)=
 \int_{\mathbb R}e^{|t|/2}|\delta(t)|dt
 +\int_{\mathbb R}e^{|t|/2}\,d|D\delta|(t).
 \tag{13}
\]
内側の derivative は \(e'\)、外側は \(-f'\)。
境界の jump の絶対値は **\(|p(a)|,|p(-a)|\)** であり、
\(|e(a)|\) だけではない。従って
\[
 \begin{split}
 \mathcal B(\delta)\le{}&
 e^{a/2}\bigl(\sqrt{2a}(\|e\|_2+\|e'\|_2)
                 +2|e(a)|+2|f(a)|\bigr)\\
 &+\int_{|t|>a}e^{|t|/2}(|f(t)|+|f'(t)|)dt\\
 \le{}& C_m\sqrt a(1+\Omega)^{2m+4}
                 e^{\,a/2-\pi\Omega/4}
          +C_m\lambda^{4m+12}e^{-\pi\lambda^2}.
 \end{split}
 \tag{14}
\]
\(\Omega\ge1\)、\(\sqrt a\le e^{a/2}\) を使い tail powers を緩く吸収した。

\(z=x+iy,\ |y|\le1/2\) なら、weighted \(L^1\) bound と distributional
integration by parts の二つを合わせて
\[
 |\widehat\delta(z)|
 \le \frac{\mathcal B(\delta)}{1+|x|}.
 \tag{15}
\]
詳細には \(A=\int e^{|t|/2}|\delta|\)、\(V=\int e^{|t|/2}d|D\delta|\) とすると
\(|\widehat\delta(z)|\le A\)、また \(x\ne0\) で
\(|\widehat\delta(z)|\le V/|z|\le V/|x|\)。
\(\min(A,V/|x|)\le(A+V)/(1+|x|)\) である。
低い \(|x|\) や \(x=0\) もこの式で処理し、最低零点の数値情報を使わない。

## 5. Compact BV に対する actual explicit formula

使用する Weil pairing は
\[
 Q_W(p,q)=\sum_\rho
       \widehat p(z_\rho)\overline{\widehat q(\overline{z_\rho})},
 \qquad z_\rho=(\rho-1/2)/i .
 \tag{16}
\]
零点は全て重複度付き。\(\overline{z_\rho}\) を \(z_\rho\) に置換しない。
無条件で \(|\Im z_\rho|<1/2\) であり、
Riemann–von Mangoldt の \(N(T)=O(T\log(T+2))\) から
\[
 C_\zeta=\sum_\rho(1+|\Im\rho|)^{-2}<\infty.
 \tag{17}
\]
これは既知の零点計数 bound で、RH の仮定ではない。

本稿の \(p,q\) は compact piecewise smooth BV なので (16) の延長を検査できる。
非負 even smooth approximate identity \(\eta_\epsilon\) で
\(p_\epsilon=p*\eta_\epsilon\) とする。次が成立する：

1. \(p_\epsilon\to p\) in \(L^2\)。support は固定された少し大きい compact 区間内。
2. strip \(|\Im z|\le1/2\) で Fourier transform は点毎収束し、
   weighted BV の一様 bound により \(C/(1+|\Re z|)\) で抑えられる。
   従って零点側は (17) により dominated convergence。
3. Gamma 側は \(|\widehat p(\omega)|=O((1+|\omega|)^{-1})\) と
   \(h_\Gamma(\omega)=O(\log(2+|\omega|))\) により可積分。
   実軸で \(|\widehat\eta_\epsilon|\le1\) なので dominated convergence。
4. pole 側は複素点での Fourier 値の収束。
   prime 側は共通 compact support により有限和であり、
   correlation は \(L^2\) convergence から shift に一様に収束する。
   threshold ちょうどの shift でも correlation が連続である。

smooth test に対する actual explicit formula をこの極限で移せる。
従って (16) は零点側だけで定義した別形式ではなく、
有限行列に使う Gamma・pole・prime 側と同じ \(Q_W\) である。
非 compact \(\delta\) の form domain を無説明に仮定する必要はない。

## 6. Radical factor と recognition bound

\(\widehat f_j(z)=(-1)^jz^{2j}\Xi(z)/4\) は
\(z_\rho\) と \(\overline{z_\rho}\) の双方で 0。
後者も functional equation と conjugation の零点対称性によるもので、RH ではない。
(16) に代入すると
\[
 Q_W(p_i,p_j)
 =\sum_\rho\widehat\delta_i(z_\rho)
            \overline{\widehat\delta_j(\overline{z_\rho})},\qquad
 |Q_W(p_i,p_j)|\le C_\zeta\mathcal B(\delta_i)\mathcal B(\delta_j).
 \tag{18}
\]
(14) を平方し mixed term を \(2uv\le u^2+v^2\) で処理すれば (1) を得る。
これが support と Fourier projection を同時に含む full \(T_{a,N}\) の上界である。
sharp support-only asymptotic として解釈しない。

二経路の exponent は
\[
 a-\pi\Omega/2=a-\frac{\pi^2(N+1)}{2a}.
 \tag{19}
\]
\(N\sim a^2\) なら \(-( \pi^2/2-1)a+o(a)\)、
\(N\sim a^3\) なら \(-\pi^2a^2/2+a+o(a^2)\) で、どちらも
(1) の polynomial factor に勝つ。
より一般には \(N\sim C a^2,\ C>2/\pi^2\) でも十分。
任意の \(N/a\to\infty\) に対して (1) が消失するとは主張しない。

固定 \(m\) の Gram が正定値極限を持つことは
[trajectory note §4](../../ground_state_trajectory.md) (11)–(12) の直接評価による。
したがって raw \(M\) だけでなく、その span の全 generalized Ritz values の絶対値にも、
十分大きい \(a\) で定数を変えた同じ上界がある。
固定 finite span での係数の一様性であり、\(m\to\infty\) は含まない。

**結論の境界。** recognition の消失は両経路で無条件に定量化できた。
この上界から、実際の decay の leading rate、unique fastest state、
ground excess/gap ratio、global positivity、ground の \(k\) への収束は出ない。
特に full \(e_0\) が未知の負方向にある可能性を除かず、
小さい signed energy を ground と同一視しない。
Rate A の upper estimate を追加しただけで、Track B/C の selection verdict は変えない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/common_parent/notes/variational_limits_and_prior_art.md`](../../common_parent/notes/variational_limits_and_prior_art.md)
- [`research/ground_state_trajectory.md`](../../ground_state_trajectory.md)
