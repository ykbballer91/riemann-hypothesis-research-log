**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/groskin-dictionary.md` · Original SHA-256: `bb89e2c88c1e0fd5c45d5aaee3185007701d6f7b360c70f3a20c24de698fd28c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Groskin v3 有限辞書の独立監査

監査日: 2026-09-29。対象版: Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, [arXiv:2607.02828v3, HTML](https://arxiv.org/html/2607.02828v3), [同 PDF](https://arxiv.org/pdf/2607.02828v3)（2026-08-14）。対象は Lemma 2.1–2.3 と Theorem 2.5、及び `N=0,1` の係数検査である。原公開計算パッケージの証明書、Theorem 3.2 の全 minor、深い固有値の認証はこのノートの範囲外。

## 0. 判定

**Theorem 2.5 の実偶 sector の有限辞書、Lemma 2.2 の admissibility、Lemma 2.3 の source calculus は、以下の独立導出で整合する。Lemma 2.1 の表示された汎関数同定には、引用元の規約を文字通り使うと係数 `2` の不整合がある。** `q(f,f)` に適用する汎関数を半区間版 `Psi^sharp` に直すか、全区間版へ入れる関数を `q(f,f)/2` に直せば、その表示も整合する。これは Theorem 2.5 の零点和の式を反証するものではない。

原文の証明文にはさらに、pole source の push-forward 測度に余計な `L`、archimedean の変数変換に誤記、`W_R` の密度を呼ぶ文に符号の不整合がある。いずれも下で位置と修正式を示す。数学的主張の監査と、校正で修復できる記述上の問題を区別する。

本監査から新しい RH 入力は採用しない。有限辞書が正しいことは有限行列の正値性を与えず、有限行列の正値性も全 support・全周波数の正値性を与えない。数値の符号や最小固有値について先に結論を置いていない。

## 1. 規約を固定する

原文と同じく

\[
 c>1,\qquad L=\log c,\qquad \Delta=\frac{L}{2\pi},
 \qquad \rho=\frac{2\pi}{L}=\Delta^{-1}.
\]

この `rho` は周波数間隔であり、ζ の零点は以下 `varrho` と書く。`v∈R^{N+1}` に対して

\[
 u_0=v_0,\qquad u_k=u_{-k}=v_k/\sqrt2\ (1\le k\le N),
 \qquad T_v(t)=\sum_{m=-N}^{N}u_me^{2\pi imt}.
\]

`T_v` は実数値、偶、周期 `1`。また `∑|u_m|²=∑v_k²` である。Volterra kernel と原文の Fourier weight は

\[
 K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt,
 \qquad
 \widehat g_v(\xi)=
 \begin{cases}
 \pi K_v(1-|\xi|/\Delta),&|\xi|\le\Delta,\\
 0,&|\xi|>\Delta.
 \end{cases}                                                   \tag{1.1}
\]

原文の `g_v(z)=∫ghat_v(xi)e^{2pi i z xi}d xi` と、主 repo の

\[
 F_f(z)=\int_{\mathbb R}f(x)e^{izx}dx,\qquad
 \widetilde f(x)=\overline{f(-x)},\qquad
 z_\varrho=(\varrho-1/2)/i
                                                               \tag{1.2}
\]

との間には、変数と係数 `2pi` の変換が必要である。

### 1.1 自己相関による直接の辞書

零延長された区分的滑らかな関数

\[
 f_v(x)=L^{-1/2}T_v(x/L+1/2)\,\mathbf1_{[-L/2,L/2]}(x)
                                                               \tag{1.3}
\]

を定める。`f_v` は実偶関数で `||f_v||_2²=||v||²`。一般には端点で零にならず、`C_c^∞` ではない。`h_v=f_v*tilde f_v` と置く。

`0≤y≤L` に対して、相関の積分で `x=-L/2+Lt`、`omega=1-y/L` とおくと

\[
 \begin{aligned}
 h_v(y)
 &=\int f_v(x+y)f_v(x)dx\\
 &=\int_0^{\omega}T_v(t+1-\omega)T_v(t)dt\\
 &=\int_0^{\omega}T_v(\omega-t)T_v(t)dt
 =\tfrac12K_v(\omega).
 \end{aligned}
\]

ここで最後から二つ目の等号は周期性と偶性による。`h_v` は偶、support は `[-L,L]` なので

\[
 h_v(y)=\tfrac12K_v(1-|y|/L)\mathbf1_{[-L,L]}(y),
 \qquad \widehat g_v(\xi)=2\pi h_v(2\pi\xi).            \tag{1.4}
\]

従って、**正しい変数変換は `y=2pi xi`** であり、

\[
 \begin{aligned}
 g_v(z)&=\int_{\mathbb R}h_v(y)e^{izy}dy\\
 &=F_{f_v}(z)\overline{F_{f_v}(\overline z)}
 =F_{f_v}(z)^2\\
 &=\int_0^L K_v(1-y/L)\cos(zy)dy.                      \tag{1.5}
 \end{aligned}
\]

`F_f(z)^2` の最後の形は **実偶 `f_v`** に依存する。一般の複素係数や別の sector へこの二乗を無断で延長しない。また複素 `z` での値は `|F_f(z)|²` ではない。臨界線外の零点へ絶対値二乗を代入すると RH を先取りする。

一つの便利な entire 表示は

\[
 F_{f_v}(z)=\frac{2\sin(Lz/2)}{\sqrt L}
       \sum_{m=-N}^{N}\frac{u_m}{z+\rho m}
 =\frac{2\sin(Lz/2)}{\sqrt L}
 \left(\frac{v_0}{z}+\sqrt2\sum_{k=1}^{N}
                  \frac{v_kz}{z^2-\rho^2k^2}\right).             \tag{1.6}
\]

各表示上の極は可除。これは (1.3) を項別積分し、`sin(L(z+rho m)/2)=(-1)^m sin(Lz/2)` と中心移動の係数 `(-1)^m` が相殺することから得る。

## 2. Lemma 2.3 — source calculus の再導出

実数 `alpha` と `omega∈[0,1]` に対し

\[
 \psi_{\alpha,\omega}(x)=\frac\alpha\pi\sin(2\pi\omega x),
 \quad D_{mn}=\begin{cases}
 (\psi(m)-\psi(n))/(m-n),&m\ne n,\\
 \psi'(m),&m=n
 \end{cases}
\]

とする。直接計算すると

\[
 \begin{aligned}
 2\int_0^\omega e^{2\pi imt}e^{2\pi in(\omega-t)}dt
 &=\frac{e^{2\pi im\omega}-e^{2\pi in\omega}}{\pi i(m-n)}
       &&(m\ne n),\\
 &=2\omega e^{2\pi im\omega}&&(m=n).
 \end{aligned}
\]

実部を取り `u_m u_n` で和を取ると、それぞれ `D_mn/alpha` と一致する。虚部は `(m,n)->(-m,-n)` により相殺するため

\[
 u^{\mathsf T}D u=\alpha K_v(\omega).                  \tag{2.1}
\]

`alpha=0` の場合も両辺零。有限符号付き Borel 測度 `mu` に対する積分版は有限和と積分の交換で得る。対角の微分も `|omega cos(2pi omega x)|≤1` により積分下で正当化される。原文の係数 `2`、`1/pi`、対角の `2alpha omega cos` は一致する。

関連する一次出典は [Connes–van Suijlekom v1, Proposition 4.1](https://arxiv.org/html/2511.23257v1) の divided-difference 表示である。整数で source 値が一致しても、対角の source derivative の一致は別途必要である。

## 3. Lemma 2.2 — admissibility と `C_c^∞` への橋

`f_v` は compact support の bounded variation 関数である。分布微分 `df_v` は区間内の滑らかな密度と端点の有限個の原子からなる有限測度。固定 `R>0`、`|Im z|≤R` では

\[
 |F_{f_v}(z)|\le\|f_v\|_1e^{RL/2},\qquad
 |zF_{f_v}(z)|\le\|df_v\|_{\rm TV}e^{RL/2}.            \tag{3.1}
\]

後者は分布の部分積分 `∫e^{izx}df_v(x)=-iz F_fv(z)` による。従って (1.5) から

\[
 |g_v(z)|\le C_{v,L,R}(1+|\Re z|)^{-2}
 \quad (|\Im z|\le R).                               \tag{3.2}
\]

同時に (1.5) は entire 性、指数型 `≤L` を与える。`h_v` は連続で区分的滑らかだから `ghat_v` は連続、compact support。原文の Stieltjes 部分積分による証明と同じ正則性を、自己相関から確認できる。

非自明零点に対して `|Im z_varrho|<1/2`、既知の零点計数は `O(T log(T+2))`。よって dyadic block ごとの上界が `O((j+1)2^{-j})` となり、

\[
 \sum_{\varrho}|g_v(z_\varrho)|<\infty.                \tag{3.3}
\]

この結論は RH を使わない。`h_+(r)=Re digamma(1/4+ir/2)-log pi=O(log(2+|r|))` と (3.2) により archimedean 積分も絶対収束する。

主 repo の滑らかな test function 版から拡張するには、非負・実偶・積分 `1` の mollifier `eta_epsilon` を使い `f_epsilon=f_v*eta_epsilon` とする。これは compact smooth で、

\[
 g_\epsilon(z)=F_{f_v}(z)^2F_{\eta_\epsilon}(z)^2
        \longrightarrow g_v(z).
\]

固定 strip で `|F_eta_epsilon(z)|≤e^{epsilon R}` なので、(3.2) が epsilon に一様な支配を与え、零点和と archimedean 積分を支配収束で通過できる。自己相関 `h_epsilon=h_v*eta_epsilon*eta_epsilon` は `h_v` に一様収束し、全 support は一つの compact 区間に収まる。したがって素数項は固定有限集合上の評価として収束し、極項も収束する。これにより `f_v∉C_c^∞` の問題を隠さずに、既存の明示公式へ接続できる。

## 4. 各 source と Theorem 2.5 の係数

以下 `w_q=Lambda(q)/sqrt(q)`、`omega_q=1-log(q)/L`。

### 4.1 素数項

原文の `psi_prime(x)=-(1/pi)∑_{q≤c}w_q sin(2pi omega_q x)` に (2.1) を使うと

\[
 v^{\mathsf T}Q_{\rm prime}v
 =-\sum_{q\le c}w_qK_v(\omega_q)
 =-2\sum_{q\le c}w_qh_v(\log q)
 =-\frac1\pi\sum_{q\le c}w_q
      \widehat g_v(\log q/(2\pi)).                    \tag{4.1}
\]

これは主 repo の負の prime contribution と一致する。`q=c` の場合でも `K(0)=0` なので端点寄与は零。`q>c` は support 外。

### 4.2 極項

原文の source は

\[
 \psi_0(x)=\frac1\pi\int_0^L 2\cosh(y/2)
               \sin(2\pi x(1-y/L))dy.
\]

従って

\[
 \begin{aligned}
 v^{\mathsf T}Q_{\rm pole}v
 &=\int_0^L 2\cosh(y/2)K_v(1-y/L)dy\\
 &=2L\int_0^1 K_v(\omega)\cosh(L(1-\omega)/2)d\omega\\
 &=2g_v(i/2).                                          \tag{4.2}
 \end{aligned}
\]

これは `g_v` の偶性による `g(i/2)+g(-i/2)` と同じ。

対角も監査するため source の整数以外の式を計算する。`beta=L/(4pi)` とすると

\[
 \psi_0(x)=\frac{Lx}{\pi^2}
       \frac{\cosh(L/2)-\cos(2\pi x)}{x^2+\beta^2}.
                                                               \tag{4.3}
\]

`x=n∈Z` では分子の cosine の微分が零なので、

\[
 \psi_0(n)=C\frac n{n^2+\beta^2},\qquad
 \psi_0'(n)=C\frac{\beta^2-n^2}{(n^2+\beta^2)^2},\quad
 C=\frac{L(\cosh(L/2)-1)}{\pi^2}.
\]

よって全周波数の pole matrix は

\[
 (Q_{\rm pole})_{mn}
 =C\frac{\beta^2-mn}{(m^2+\beta^2)(n^2+\beta^2)}.       \tag{4.4}
\]

これは [CCM v1, Lemma 4.1, (4.2)](https://arxiv.org/html/2511.22755v1) の表示と一致する。ここで一致するのは正しく正規化された **matrix entries** であり、下記の全区間/半区間汎関数の取り違えを免除しない。

### 4.3 Archimedean 項

\[
 S(r,x,L)=\int_0^L\sin(2\pi x(1-y/L))\cos(ry)dy,
 \quad \psi_{{\rm arch},T}(x)=\frac1{2\pi^2}
            \int_{-T}^{T}h_+(r)S(r,x,L)dr.
\]

有限 `T` で (2.1) と有限積分の交換により

\[
 \begin{aligned}
 v^{\mathsf T}Q_{{\rm arch},T}v
 &=\frac1{2\pi}\int_{-T}^{T}h_+(r)
           \left(\int_0^LK_v(1-y/L)\cos(ry)dy\right)dr\\
 &=\frac1{2\pi}\int_{-T}^{T}h_+(r)g_v(r)dr.             \tag{4.5}
 \end{aligned}
\]

`T->∞` は §3 により許される。全 matrix の entrywise 収束を確認するには、整数 `n` で、可除特異点を除いて

\[
 S(r,n,L)=\frac{2\rho n\sin^2(Lr/2)}{r^2-\rho^2n^2},
\]

\[
 \partial_xS(r,x,L)|_{x=n}
 =\frac{2\sin^2(Lr/2)}{\rho}
       \frac{(r/\rho)^2+n^2}{((r/\rho)^2-n^2)^2}         \tag{4.6}
\]

と直接積分する。固定有限 node 集合では両者 `O(r^-2)` で、off-diagonal は整数値の差商、diagonal は二つ目の式だから `O(log r/r²)` の可積分上界を得る。`r=±rho n` は元の積分で解釈する。

**符号:** [CCM v1, (3.8)–(3.10)](https://arxiv.org/html/2511.22755v1) では `W_R=-W_infty`、`W_infty=∫gh_+/(2pi)` である。したがって上の正の `+Q_arch` は全 Weil 形式における `-W_R` に対応する。

### 4.4 零点側

§3 の正則化により既知の明示公式を適用すると、

\[
 \boxed{\;
 v^{\mathsf T}Q_\infty v
 =\sum_{\varrho}g_v(z_\varrho)
 =-\frac1\pi\sum_{q\le c}w_q\widehat g_v(\log q/(2\pi))
  +2g_v(i/2)+\frac1{2\pi}\int_{\mathbb R}h_+(r)g_v(r)dr.
 \;}                                                        \tag{4.7}
\]

これが Theorem 2.5 の正確な辞書で、主 repo の `Q(f_v,f_v)` の正則化による値に等しい。RH なしでは和の引数は複素 `z_varrho` のままである。`g_v(r)≥0` が全 **実数** `r` で成立しても、すべての零点引数が実数だとはまだ分からない。

## 5. Lemma 2.1 の全区間 / 半区間の係数不整合

### 5.1 一次出典同士の照合

[CCM v1, (2.4)](https://arxiv.org/html/2511.22755v1) は

\[
 q(f,g)(y)=(f^**g)(y)+(f^**g)(-y)
\]

と定める。実偶 sector では `q(f_v,f_v)=2h_v`。同じ論文の Proposition 3.2, (3.18) と (4.1) は、`F=q(f,f)∘log` に作用させるものを明確に **`Psi^sharp(F)`** としている。全区間版は (3.10) の `Psi`、関係は (3.12) の

\[
 \Psi(H)=\Psi^\sharp(H+H\circ\iota),\qquad\iota(x)=1/x.
                                                               \tag{5.1}
\]

一方 Groskin Lemma 2.1 は `F_v=q(f_v,f_v)∘log` と置き、表示右辺を sharp なしの `W_{0,2}(F_v)-W_R(F_v)-W_p(F_v)` としている。引用している CCM の full functional の意味のままなら、(5.1) と `F_v=2h_v∘log` により、その右辺は **正しい行列値の 2 倍**になる。

修正は次のどちらかで十分である。

1. `F_v=q(f_v,f_v)∘log` を保ち、右辺を `W_{0,2}^sharp(F_v)-W_R^sharp(F_v)-∑W_p^sharp(F_v)` とする。
2. full functional を保ち、入力を `F_v=(q(f_v,f_v)/2)∘log=h_v∘log` にする。

Lemma 2.1 の後続の **pole matrix の表示 (4.4)** は正しい半区間評価と一致しており、ここを 2 倍へ変更すべきではない。

### 5.2 `N=0` の厳密な区別

`v_0=1` のとき `h(y)=(1-|y|/L)_+`、`q=2h`。source と Theorem 2.5 の pole 値は

\[
 Q_{{\rm pole},00}=2g(i/2)=\frac{32\sinh^2(L/4)}L.
\]

対して CCM の **full** `W_{0,2}` を `F=q∘log` に適用すると

\[
 W_{0,2}(F)=\int_{-L}^{L}2h(y)(e^{y/2}+e^{-y/2})dy
          =\frac{64\sinh^2(L/4)}L.                     \tag{5.2}
\]

これは全 `L>0` で非零であり、項別同定の違いを厳密に検出する。全 functional でも差が偶然常に零になるわけではない。`N=0`、`L->0+` では prime 項はなく、CCM (4.4) の正則な archimedean 表示から

\[
 Q_{\infty,00}=-\log L+1-\gamma-\log(2\pi)+O(L),       \tag{5.3}
\]

従って十分小さい `L` で非零。確認方法は、`q(y)=2(1-y/L)` を (4.4) に入れ、`y=Lt` と置くこと。定数項は `gamma+log(4pi tanh(L/2))`、積分項は

\[
 \int_0^L\frac{2e^{y/2}(1-y/L)-2}{e^y-e^{-y}}dy=-1+O(L),
\]

pole 値は `2L+O(L³)`。これらを足すと (5.3) を得る。

判定は「Lemma 2.1 の表示を引用規約のまま読めば誤り、修復可能な係数不整合」。独立に定義された sources の和と Theorem 2.5 の (4.7) はこの誤記に依存せず正しい。

## 6. 証明文の局所的な修正箇所

次の箇所は [Groskin v3 PDF, 印刷 page 6](https://arxiv.org/pdf/2607.02828v3)（PDF の零始まり page index 5）及び HTML で照合した。

| 箇所 | 原文にある式または呼称 | 正しい式・理由 |
|---|---|---|
| Theorem 2.5 proof, pole の直前 | `2cosh(y/2) L dy` を `omega=1-y/L` で push-forward | 元の測度は `[0,L]` 上の `2cosh(y/2)dy`。push-forward 後に `2L cosh(L(1-omega)/2)domega`。元の `L` は重複 |
| 同 proof, archimedean の直後 | 内側積分から `g` への置換 `xi=Delta(1-y/L)` | 正しくは `xi=y/(2pi)=Delta y/L`。`omega=1-y/L` を先に使うなら `xi=Delta(1-omega)` |
| Lemma 2.1 proof, archimedean density | `h_+` を `W_R` の density と同定 | CCM の符号では `h_+/(2pi)` は `-W_R=W_infty` の density。Groskin の表示された `+Q_arch` はこちらと整合 |

一つ目を文字通り採用すると pole 値がさらに `L` 倍になり、二つ目を文字通り採用すると kernel と cosine の引数が入れ替わる。原文でそれらの前後にある完成した等式 (4.2), (4.5) 自体は、正しい置換により確認できる。

また §2.3 では、有限範囲の零点が臨界線にあるという情報から無限和 `2∑_{n≥1}g(gamma_n)` へ書き換えている文に注意が必要である。有限に検証済みの零点に関する partial sum は使えるが、未検証域を含む全零点を実 ordinates の値だけで評価する根拠にはならない。無条件の全零点側は (4.7) の複素引数の和である。

## 7. `N=0,1` の明示的検査

### 7.1 `N=0`

`v=(a)` とすると

\[
 T=a,\quad K(\omega)=2a^2\omega,\quad
 \widehat g(\xi)=2\pi a^2(1-|\xi|/\Delta)_+,
\]

\[
 F_f(z)=a\sqrt L\,\frac{\sin(Lz/2)}{Lz/2},\qquad
 g(z)=a^2L\left(\frac{\sin(Lz/2)}{Lz/2}\right)^2.       \tag{7.1}
\]

可除点 `z=0` の値は `a²L`。単一 source の行列値は `2alpha omega a²`。各 source は

\[
 Q_{{\rm prime},00}=-2\sum_{q\le c}w_q(1-\log q/L),
 \quad Q_{{\rm pole},00}=\frac{32\sinh^2(L/4)}L,
\]

\[
 Q_{{\rm arch},T;00}=\frac1{2\pi}\int_{-T}^{T}
           h_+(r)L\left(\frac{\sin(Lr/2)}{Lr/2}\right)^2dr.
\]

ここでは entries を書いたので quadratic value は各式に `a²` を掛ける。`a` を二度掛けない。

### 7.2 `N=1`

`v=(a,b)` のとき

\[
 T(t)=a+\sqrt2b\cos(2\pi t),
\]

\[
 K(\omega)=2a^2\omega
    +\frac{2\sqrt2ab}{\pi}\sin(2\pi\omega)
    +b^2\left(2\omega\cos(2\pi\omega)
                     +\frac{\sin(2\pi\omega)}\pi\right).       \tag{7.2}
\]

従って even embedding 後の単一 source の `2×2` 行列は

\[
 Q_{\alpha,\omega}^{\rm even}=\alpha
 \begin{pmatrix}
 2\omega&\sqrt2\sin(2\pi\omega)/\pi\\
 \sqrt2\sin(2\pi\omega)/\pi&
 2\omega\cos(2\pi\omega)+\sin(2\pi\omega)/\pi
 \end{pmatrix}.                                             \tag{7.3}
\]

`omega=0` で零行列、`omega=1` で `2alpha I`、`omega=1/2` で `alpha diag(1,-1)`。したがって正の単一 source ですら一般に PSD ではない。この符号検査は全 Weil 行列の符号についての主張ではない。

Fourier 側は

\[
 F_f(z)=\frac{2\sin(Lz/2)}{\sqrt L}
          \left(\frac a z+\frac{\sqrt2bz}{z^2-\rho^2}\right),
 \qquad g(z)=F_f(z)^2.                                      \tag{7.4}
\]

`g(0)=La²`、`g(±rho)=Lb²/2` は可除点での正確な値。pole matrix は (4.4) を even embedding して

\[
 Q_{\rm pole}^{\rm even}
 =C\begin{pmatrix}
 \beta^{-2}&\sqrt2/(1+\beta^2)\\
 \sqrt2/(1+\beta^2)&2\beta^2/(1+\beta^2)^2
 \end{pmatrix},                                            \tag{7.5}
\]

となり正の rank `1`。full `3×3` の rank `2` の pole matrix と混同しない。

### 7.3 非認証の数値 sanity check

上記解析式とは独立の NumPy 2.3.5、256 点 Gauss–Legendre 積分で次を確認した。公開 package の出力は入力に使っていない。

| 検査 | サンプル | 最大絶対残差 |
|---|---|---:|
| Volterra 積分 `K` と node 値・導関数から直接作った差商行列 | `v=(1),(1,0),(0,1),(1,-.7)`、`omega=0,.125,.3,.5,.75,1` | `6.7e-15` |
| `ghat` の積分と直接積分した `F_f²` | `c=13`、上記 4 vectors、`z=0,.7+.25i,3.1-.3i,rho` | `1.1e-14` |
| `N=0,c=2` の source pole | `C/beta²` | `1.400226064099536` |
| 同じ入力で full `W_02(q)` | `q=2h` を直接積分 | `2.800452128199066` |

最後の比は約 `1.999999999999996`。これは (5.2) の係数 `2` と一致するが、その根拠は解析式である。全検査は binary64 で丸め・求積の区間保証なし。固有値の認証、零点和の全 tail の認証、RH の証拠として扱わない。最初の quadrature helper は定数関数の scalar broadcast を欠いていたため停止し、明示 broadcast を加えて上記結果を再実行した。失敗した実行結果を有効な検査数へ数えていない。

## 8. 採用境界

記録できる成果は、有限 source の係数、自己相関による Fourier 辞書、admissibility、及び引用規約の修正箇所である。Lemma 2.1 を引用する場合は §5 の修正を明記する。Theorem 2.5 は無条件の複素零点和として使う。

本ノートから全 support の positivity、全 Galerkin band の positivity、archimedean tail の区間証明書の成功を主張しない。既存の証明 graph・文献台帳・実装には変更を行っていない。証明書実装の探索は別の監査結果として扱う。
