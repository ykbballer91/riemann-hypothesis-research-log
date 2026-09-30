**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/groskin-tail.md` · Original SHA-256: `645b79dc87ad9c9e84ba2edcdd406aaf28b8c7f7d6b2f8c92f701bd2711fcee6`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Groskin v3 archimedean tail の独立破壊監査

日付: 2026-09-29。担当: DESTROYER。**RH は未解決。**

固定資料は Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, [arXiv:2607.02828v3 PDF](https://arxiv.org/pdf/2607.02828v3), [同版 HTML](https://arxiv.org/html/2607.02828v3)。[投稿履歴](https://arxiv.org/abs/2607.02828) は v3 を 2026-08-14 の最新版として表示する。HTML 全文を読み、対象の Lemma 3.1 / Theorem 3.2 / Corollary 3.3 を PDF pp.9–12（PDF のページ添字では 8–11）と照合した。v1 の結論を代用していない。

**判定:** 定義された有限行列の切断差について、Theorem 3.2 の複素全係数での正定値性・自然順序での strict total positivity、および Corollary 3.3(i),(iii) は、以下の独立導出に耐えた。主結論への解析的反例は見つからなかった。ただし (ii) の曖昧帯を左端込みで記述するのは不精確であり、下記 §6 の端点処理を要する。これは ζ の反例を得たという意味ではない。全論文、全付属証明書、CCM との全行列同定を認証したという判定でもない。

## 1. 対象を固定する

以下では有限の整数 $N\ge0$、$L>0$、$\rho=2\pi/L$、$I_N=\{-N,\ldots,N\}$ を固定する。行列は真の source の差商、対角は真の微分で定義する。略記として

\[
h(t)=\Re\psi(1/4+it/2)-\log\pi,
\quad
S(t,x)=\int_0^L\sin(\rho x(L-y))\cos(ty)\,dy
\]

を使う。ここで増加させる $T$ は **archimedean 積分の切断値**。support 窓 $L$、基底次数 $N$、零点和の高さ切断を増加させる操作とは異なる。

尾差の監査に、実偶係数という辞書定理の仮定を持ち込む必要はない。逆に、尾差が全複素係数で正だからという理由で、実偶係数用の辞書定理の写像を無断で全係数へ延長することもできない。

## 2. 真の source と対角微分

整数値の補間関数を微分するだけでは通常は不十分である。そこで非整数 $x$ の段階から積分を計算した。$k=\rho x$ とすると、共鳴を除き

\[
S(t,x)=\frac{k\,[\cos(kL)-\cos(tL)]}{t^2-k^2}.
\tag{A1}
\]

これは積の三角関数公式、または Volterra convolution の直接積分から従う。したがって真の微分は

\[
\partial_x S(t,x)
=\rho\left[
\frac{(t^2+k^2)[\cos(kL)-\cos(tL)]}{(t^2-k^2)^2}
-\frac{kL\sin(kL)}{t^2-k^2}
\right].
\tag{A2}
\]

$x=n\in I_N$ でのみ、第2項が消える。$a=t/\rho\notin I_N\cup(-I_N)$ なら

\[
S(t,n)=\frac{2\sin^2(\pi a)}{\rho}\frac{n}{a^2-n^2},
\qquad
\partial_x S(t,n)=\frac{2\sin^2(\pi a)}{\rho}
\frac{a^2+n^2}{(a^2-n^2)^2}.
\tag{A3}
\]

今回は整数値用の有理関数と真の source の微分が一致する。単なる整数値の一致を根拠にした推論ではない。さらに

\[
\frac{m/(a^2-m^2)-n/(a^2-n^2)}{m-n}
=\frac12\left[\frac1{(a-m)(a-n)}+\frac1{(a+m)(a+n)}\right]
\tag{A4}
\]

は対角極限も含めて成り立つ。両端 $[-T,T]$ の微分による係数 $2$ と (A4) の $1/2$ を保持すると

\[
D(t):=\frac{dQ_{\rm arch,t}}{dt}
=\frac{h(t)\sin^2(\pi a)}{\pi^2\rho}
\bigl[p(a)p(a)^t+q(a)q(a)^t\bigr],
\quad p_n(a)=\frac1{a-n},\ q_n(a)=\frac1{a+n}.
\tag{A5}
\]

符号、$\pi^2$、$\rho$、対角の係数は独立に一致した。

### 可除特異点

(A1) の見かけの共鳴は積分そのものの特異点ではない。(A5) も $a=j\in\{1,\ldots,N\}$ で

\[
D(\rho j)=\frac{h(\rho j)}{\rho}
(e_je_j^t+e_{-j}e_{-j}^t)
\tag{A6}
\]

へ連続延長する。実際、$\sin^2(\pi a)\sim\pi^2(a-j)^2$ が二重極を消す。他の成分は $0$ に収束する。$j>N$ では全分母が有限なので $D(\rho j)=0$。また $t=0$ では $D(0)=2h(0)e_0e_0^t/\rho$。したがって、共鳴点に裸の $p,q$ を代入して無限大と判定する実装は誤りとなる。

## 3. 密度 $h$ の符号を独立認証する

[DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6) の部分分数展開から

\[
h'(t)=\frac t2\sum_{k\ge0}
\frac{k+1/4}{[(k+1/4)^2+t^2/4]^2}>0\quad(t>0).
\]

各コンパクト $t$-区間で微分級数の一様収束があり、項別微分に問題はない。単峰関数の和を積分と最大値で抑えると

\[
h'(t)\le \frac1t+\frac{9}{4\sqrt3\,t^2}
\le\frac1t+\frac{13}{10t^2}.
\tag{A7}
\]

原資料の Arb の数値を前提とせず、以下の有理演算だけでも $h(7)>0$ を確認できる。$M=100, a=M+1/4$ と置き

\[
s_M=\sum_{k=0}^{M-1}
\left[\frac1{k+1}-\frac{4(4k+1)}{(4k+1)^2+196}\right].
\]

残りの各項を

\[
-\frac{3}{4(k+1)(k+1/4)}
+\frac{49/4}{(k+1/4)[(k+1/4)^2+49/4]}
\]

と分解し、減少関数の積分上下界を使えば、尾 $r_M$ に対して

\[
-\frac34(a^{-1}+a^{-2})
\le r_M\le
-\frac3{4(M+1)}+\frac{49}{4}(a^{-3}+\tfrac12a^{-2}).
\tag{A8}
\]

したがって $h(7)=s_M+r_M-\gamma-\log\pi$ を挟める。次のコードは $\gamma,\log\pi,\log7$ まで有理上下界で処理し、特殊関数ライブラリも浮動小数点比較も使わない。Euler 定数には $H_m-\log m-1/m<\gamma<H_m-\log m$、$\pi$ には Machin の恒等式を使う。log の誤差は正項級数の幾何上界、atan の誤差は交代級数の隣接部分和である。

```python
from fractions import Fraction as F

def log_bounds(x, J=64):
    u = (x-1)/(x+1)
    assert 0 <= u < 1
    s = 2*sum((u**(2*j+1)/F(2*j+1) for j in range(J)), F())
    err = 2*u**(2*J+1)/(F(2*J+1)*(1-u*u))
    return s, s+err

def atan_bounds(x, J=16):
    s = sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(J)), F())
    t = s + (-1)**J*x**(2*J+1)/F(2*J+1)
    return min(s, t), max(s, t)

al, au = atan_bounds(F(1, 5))
bl, bu = atan_bounds(F(1, 239))
pi_lo, pi_hi = 16*al-4*bu, 16*au-4*bl
lp_lo, lp_hi = log_bounds(pi_lo)[0], log_bounds(pi_hi)[1]
assert F(1144,1000) < lp_lo < lp_hi < F(1145,1000)

l2,u2 = log_bounds(F(2))
l3,u3 = log_bounds(F(3))
l54,u54 = log_bounds(F(5,4))
l3000,u3000 = l3+9*l2+3*l54, u3+9*u2+3*u54
H = sum((F(1,k) for k in range(1,3001)), F())
glo, ghi = H-u3000-F(1,3000), H-l3000
assert F(577,1000) < glo < ghi < F(578,1000)

M = 100
a = F(4*M+1,4)
s = sum((1/F(k+1)-F(4*(4*k+1),(4*k+1)**2+196)
         for k in range(M)), F())
lo = s-F(3,4)*(1/a+1/a**2)-ghi-lp_hi
hi = s-F(3,4*(M+1))+F(49,4)*(1/a**3+F(1,2)/a**2)-glo-lp_lo
assert lo > F(105,1000)
assert hi < F(109,1000)
assert hi+F(13,70)-log_bounds(F(7))[0] < -F(165,100)
print('All exact rational bounds PASS')
```

実行結果: 全 assert PASS。従って少なくとも $0.105<h(7)<0.109$ が独立認証され、(A7) の積分から $h(t)<\log t-1.65<\log t-8/5$（$t\ge7$）も従う。この認証は原資料の小数桁全部を保証するという主張ではない。

## 4. 複素全係数、strict PD、parity

$z\in\mathbb C^{I_N}$ に対し、実ベクトル $p,q$ を使う (A5) は

\[
z^*D(t)z=\frac{h(t)\sin^2(\pi a)}{\pi^2\rho}
\left(\left|\sum_n\frac{z_n}{a-n}\right|^2+
\left|\sum_n\frac{z_n}{a+n}\right|^2\right).
\tag{A9}
\]

ここでは $z^tDz$ でなく $z^*Dz$ が必要。複素係数の共役を落とすと、例えば $iz$ の「二乗」で符号が反転してしまう。

$t\ge7$ の非退化区間上で積分した値が $0$ なら、区間から離散的な共鳴点・sin の零点を除いた部分で有理関数

\[
R_z(a)=\sum_{n=-N}^N\frac{z_n}{a-n}
\]

が消える。恒等的に $0$ となり、各極の留数から $z_n=0$。これは全複素係数の strict PD の独立証明である。点ごとの密度は rank $\le2$ なのに積分は full rank となることと矛盾しない。

反転行列 $Jz=(z_{-n})$ は $Jp=q$ を満たすので $JD(t)J=D(t)$。偶・奇の両部分空間への圧縮が正で、偶部分だけを調べたことによる偽の正性ではない。isometric な偶埋込 $E$ では $E^*\Delta E\succ0$、かつ全空間の trace budget をそのまま上界として使える。

**条件の強弱:** PD だけなら $T_1>\rho N$ は不要で、(A6) を使えば $T_2>T_1\ge7$ で同じ議論が通る。post-band 条件は次節の全 minor の符号には必要となる。原定理の条件が十分であることは崩れない。

## 5. Cauchy minor の符号と反例

$T_1>\rho N$ なら、$a=t/\rho$ の支持は全節点の外にある。正負の両区間への push-forward 測度で

\[
\Delta_{mn}=\int\frac{d\nu(s)}{(s-m)(s-n)}
\]

と書ける。$k$ 本の増加する行節点 $x_i$ と、相異なる昇順 $s_\ell$ に対して Cauchy 行列式を直接展開すると

\[
\det[(s_\ell-x_i)^{-1}]
=\frac{\prod_{i<j}(x_i-x_j)\prod_{\ell<r}(s_r-s_\ell)}
{\prod_{i,\ell}(s_\ell-x_i)}.
\]

負の支持点が $r_-$ 個なら分母の符号は $(-1)^{kr_-}$、分子の符号は $(-1)^{k(k-1)/2}$。列節点 $y_j$ に対しても全く同じ符号になる。Andréief の積分ではこの2行列式の符号が打ち消し合う。支持の開区間から相異なる $k$ 点を選ぶ領域は正測度なので minor は strict positive。混合した正負の支持点を無視した証明ではない。

以下は定理の境界を攻撃する厳密例であり、ζ や RH の反例ではない。

1. **帯の内部では strict total positivity が壊れる。** $\rho=10, N=1, L=\pi/5$ とし、$15/2<t<17/2$ を採る。$h(t)>0$、$a\in(3/4,17/20)\subset(0,1)$ だが
   \[
   D(t)_{-1,1}=\frac{h(t)\sin^2(\pi a)}{\pi^2\rho}\frac{2}{a^2-1}<0.
   \]
   よってこの区間の増分には負の $1\times1$ minor がある。それでも §4 により増分全体は PD。PD と全 minor の正性は別の結論である。

2. **低い $t$ での PD は壊れる。** $h(0)=-\gamma-\pi/2-3\log2-\log\pi<0$。部分分数展開から $h(t)-h(0)\le18t^2$。ここでは 
   $\sum_{k\ge0}(k+1/4)^{-3}\le64+\int_0^\infty(x+1/4)^{-3}dx=72$ を使った。従って $0\le t\le1/4$ で $h(t)<0$。$N=0,\rho=1,T_1=1/8,T_2=1/4$ の増分は負の $1\times1$ 行列になる。

3. **密度そのものの strict TP は誤り。** $N\ge1$ の非共鳴点では密度の rank は高々2。全 $3\times3$ 行列式は $0$。原定理は正の長さの区間で積分した増分についての主張である。

4. **任意の基底での strict TP は誤り。** 自然基底で全成分が正でも、一つの座標の符号を反転する対角直交行列 $U$ により $U^*\Delta U$ は負の非対角成分を持つ。固有値・PD は保たれる。parity 基底や任意の unitary 座標へ移した後に natural-order の minor 主張を無断で使えない。

## 6. 尾 budget と認証規則の端点

$R_T=Q_\infty-Q_T$ と置く。各 entry は $O(\log t/t^2)$ で可積分。§4 より $R_T\succ0$、定義された $B_T$ は **正確に** $\operatorname{tr}R_T$ である。従って

\[
0\prec R_T\preceq B_TI.
\tag{A10}
\]

有限次元の min–max 原理により、同じ順序の固有値に対する strict 下界と非 strict 上界が従う。固有ベクトルが $T$ と共に不変である必要はない。

**指摘 E1 — 曖昧帯の左端:** 正確な $B_T=\operatorname{tr}R_T$ を用い、$N\ge1$ なら次元 $d=2N+1>1$ なので

\[
\|R_T\|<\operatorname{tr}R_T=B_T.
\]

よって条件 $\lambda_j(Q_T)=-B_T$ からは

\[
\lambda_j(Q_\infty)\le\lambda_j(Q_T)+\|R_T\|<0
\]

と負性を認証できる。$N=0$ では $R_T=[B_T]$ なので同じ等号から cutoff-free 固有値は $0$ と決まる。従って「何も認証できない帯」は少なくとも開区間 $(-B_T,0)$ と書く必要がある。計算用上界 $\overline B_T\ge B_T$ を代用しても $N\ge1$ では $\lambda_j(Q_T)\le-\overline B_T$ で負性が従う。

この指摘は、実際の ζ 行列にその等号を満たすパラメータを発見したという意味ではない。その存在を主張すれば未解決の負性問題に踏み込む。ここで訂正するのは与えられた PSD/trace 情報から導く **条件付き認証規則の論理** である。例えば一般の行列データ $R=I_3,A=\operatorname{diag}(-3,0,0)$ なら $\operatorname{tr}R=3$、左端 $-3$ に対応する $A+R$ の固有値は $-2$ と実際に負になる。この toy model を ζ の反例とは扱わない。

## 7. 明示上界と漸近

$b=\rho N>0$ とすると

\[
\|p_t\|^2+\|q_t\|^2
\le\frac{2(2N+1)\rho^2}{(t-b)^2}.
\]

§3 の $0<h(t)\le\log t$ と $\sin^2\le1$ を代入し、部分積分で

\[
\int_T^\infty\frac{\log t}{(t-b)^2}\,dt
=\frac{\log T}{T-b}+\frac1b\log\frac T{T-b}
\]

を得る。したがって Corollary 3.3 の係数 $2(2N+1)\rho/\pi^2$ を含む上界は一致する。$N=0$ は $b=0$ を式へ裸で代入せず、別に

\[
B_T\le\frac{2\rho}{\pi^2}\frac{\log T+1}{T}
\]

と処理できる。$T\downarrow b$ で掲示上界は発散し得るが、これは可除共鳴を捨てた粗い上界の性質であり、真の行列積分の発散ではない。

[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) より $h(t)=\log(t/(2\pi))+O(t^{-2})$。$L,N$ を固定して 
$\|p_t\|^2+\|q_t\|^2=2(2N+1)\rho^2t^{-2}(1+O(t^{-2}))$ と展開できる。$\sin^2(Lt/2)=(1-\cos Lt)/2$ の振動部分を部分積分すると $O_{L,N}(T^{-2}\log T)$。従って

\[
B_T=\frac{(2N+1)\rho}{\pi^2T}
\left(\log\frac{T}{2\pi}+1\right)(1+o(1))
\]

が独立に再現される。ここで $L,N$ が固定という量化は不可欠。$T,N,L$ を同時に動かす一様漸近や全窓の下界はこの式から得られない。

## 8. 正の尾は coercivity や全窓の正値性ではない

高次 moment cancellation により、tail の方向別尺度は trace よりずっと小さくなる。固定の非零ベクトル $z$ に対し $\mu_k=\sum_n z_n n^k$、$K=\min\{k:\mu_k\ne0\}\le2N$ とする。有理関数の無限遠展開から

\[
z^*R_Tz\sim
\frac{|\mu_K|^2\rho^{2K+1}}{\pi^2(2K+1)T^{2K+1}}
\left(\log\frac{T}{2\pi}+\frac1{2K+1}\right).
\tag{A11}
\]

例えば $N=1,z=(1,-2,1)$ は $K=2,\mu_2=2$ なので $O(\log T/T^5)$。他方 $B_T\asymp\log T/T$。trace 上界を各方向の下界や spectral gap と読み替えることはできない。

また任意の Hermitian $A$ に正の増分 $R$ を足しても $A+R\succeq0$ は従わない。原定理は初期の prime/pole/archimedean 部分の負方向を消す保証ではない。$T$ 増加の順序を $N$ 増加の順序と混同することもできない。厳密な nested compression の最小固有値は通常は非増加であり、ここでの固定サイズ $T$-flow と向きが逆になる。

## 9. 採用範囲

- 採用可能: 定義された固定有限行列についての切断差の Gram 表示、複素 strict PD、post-band の natural-order strict TP、trace budget と正しい条件付き認証規則。
- 要修正: Corollary 3.3(ii) の曖昧帯の左端表現。主たる有限不等式の反例ではない。
- 本監査で認証していない: 論文付属の $401\times401$、9000-bit 証明書、任意の古い版の数値、CCM source 同定の全証明、全 $L,N$ での PSD、RH、あるいは新規性。
- 主な反証成果: post-band 条件を外した TP、低切断の PD、密度単体の strict TP、基底に依存しない TP、trace からの coercivity への誤った拡張は明示的に排除した。

このファイルだけを新規作成した。親担当の数値実装を見ずに核恒等式・符号・有理認証を独立導出した。
