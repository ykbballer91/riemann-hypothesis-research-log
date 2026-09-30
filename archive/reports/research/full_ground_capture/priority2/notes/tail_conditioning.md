**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `research/full_ground_capture/priority2/notes/tail_conditioning.md`; original SHA-256: `d1ebde4f59a381a6bdaefb76fe89e2e23355b4421a85b1e2d1225eaa63c73fe8`. Publication formatting does not constitute a new mathematical audit.

---

# Priority 2 — sharp tail と有限 head の定量的条件数

2026-09-30。RH OPEN。固定有限 head のみ。旧ファイルを変更しない。
記号・基底は [algebraic_rank.md](algebraic_rank.md) の AR1–AR9 と同じ。
以下の証明は RH、Weil positivity、零点単純性を使わない。

## TC0. 射影と全線標本を区別する

区間の正規直交基底を零延長した実際の射影では
\(P_NR_a=P_N\)、\(P_N(1-R_a)=0\) である。
従って依頼中の「no-tail \(P_Nf\)」を文字通りこの射影として扱うと、tail の比較にならない。

本ノートでは、偶 \(L^1\) 関数の全線 Fourier 標本写像を
\[
(S_{a,N}f)_n=\kappa_n\widehat f(\omega_n),\quad
\kappa_0=(2a)^{-1/2},\quad \kappa_n=(-1)^n a^{-1/2}\ (n\ge1)
\]
と明記する。これは新しい算術対象ではなく積分の記法であり、global \(L^2\) 上の有界射影ではない。
実際の区間係数に対する正しい exact identity は
\[
B_{\cdot j}=S_{a,N}(R_af_j)
=S_{a,N}f_j-S_{a,N}((1-R_a)f_j)=A_{\cdot j}-E_{\cdot j}.
\tag{TC1}
\]
すべての積分はこの関数族について絶対収束する。

## TC1. 完全に明示した tail majorant

\(Y=\pi e^{2a}\)、\(P_0(y)=y^2-3y/2\)、
\[
P_{r+1}=2yP_r'+(1/2-2y)P_r,\qquad
P_{2j}(y)=\sum_{\ell=1}^{2j+2}c_{j\ell}y^\ell.
\tag{TC2}
\]
係数は有限回の有理数演算で得る。
theta 表示を絶対値で項別評価し、\(y=\pi q^2e^{2t}\) と変数変換すると
\[
T_j(a):=\int_{|t|>a}|k^{(2j)}(t)|dt
\le\pi^{-1/4}\sum_\ell|c_{j\ell}|
\sum_{q\ge1}q^{-1/2}\Gamma(\ell+1/4,q^2Y).
\tag{TC3}
\]
ここで \(\Gamma(\nu,x)=\int_x^\infty y^{\nu-1}e^{-y}dy\)。

有限和だけの上界として、\(j\le m\)、\(Y\ge4m+4\) なら
\[
\boxed{T_j(a)\le\mathcal T_j(a):=
\frac{2\pi^{-1/4}e^{-Y}}{1-e^{-Y/2}}
\sum_{\ell=1}^{2j+2}|c_{j\ell}|Y^{\ell-3/4}.}
\tag{TC4}
\]
証明：\(x\ge2(\nu-1)\) なら \(y=x+v\) と
\((1+v/x)^{\nu-1}\le e^{v/2}\) より
\(\Gamma(\nu,x)\le2x^{\nu-1}e^{-x}\)。
残る和は \(q^{2\ell-2}e^{-q^2Y}\) である。
\(\log q\le(q^2-1)/2\)、\(Y\ge2(\ell-1)\) より
\[
\sum_{q\ge1}q^{2\ell-2}e^{-q^2Y}
\le e^{-Y}\sum_{q\ge1}e^{-(Y/2)(q^2-1)}
\le\frac{e^{-Y}}{1-e^{-Y/2}}.
\]
指定した \(Y\) の条件は全 \(j\le m\) の両条件を満たす。

\(|E_{nj}|\le|\kappa_n|\mathcal T_j\) なので
\[
\boxed{\|E\|_2\le\|E\|_F\le
\tau(a,N,m):=
\left(\frac{2N+1}{2a}\sum_{j=0}^m\mathcal T_j(a)^2\right)^{1/2}.}
\tag{TC5}
\]
これは raw derivative 座標の評価であり、Gram 正規化後の評価ではない。

## TC2. Vandermonde の明示下界と rank certificate

ここでは \(m=N\)。\(t_n=(\pi n/a)^2\)、
\(D_n=\kappa_n\Xi(\omega_n)/4\)、\(J_{jj}=(-1)^j\) として
\[
A=D_\Xi VJ,\quad V_{nj}=t_n^j.
\]
全 \(D_n\ne0\) とする。
Lagrange cardinal 多項式の係数絶対値和は
\[
\beta_n=\prod_{r\ne n}\frac{1+t_r}{|t_n-t_r|}.
\]
従って [原典と直接証明](conditioning_literature.md#cl2-gautschi-の原典と-cardinal-係数) の通り
\[
\|A^{-1}\|_2\le L(a,N):=
\left[\sum_{n=0}^N(\beta_n/|D_n|)^2\right]^{1/2},
\qquad \sigma_{\min}(A)\ge L^{-1}.
\tag{TC6}
\]
特に
\[
\boxed{Y\ge4N+4,\quad D_n\ne0\ (0\le n\le N),\quad L\tau<1}
\tag{TC7}
\]
は、actual 最小 prefix \(m=N\) の full rank を保証し、
\[
\sigma_{\min}(B)\ge L^{-1}-\tau>0.
\tag{TC8}
\]
数値 determinant の非零判定を証明の代用にしていない。

より鋭い十分条件は \(\|A^{-1}E\|_2<1\) または \(\|EA^{-1}\|_2<1\)。
後者は ideal cardinal basis への右変換で \(BA^{-1}=I-EA^{-1}\) となることによる。
\(D_\Xi\) を落として \(\|V^{-1}E\|<1\) だけを使うことはできない。
TC7 の失敗は rank loss を意味しない。上界が粗いだけの場合がある。

## TC3. 認証した具体的な範囲

[certify_tail_criterion.py](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/certify_tail_criterion.py) は
有理係数 TC2 と Arb/acb の包含演算で TC7 を評価する。
256 bit と384 bitで同じ結論を得た。
\(\Xi\) は completed-zeta の定義から acb で計算し、実性を確認したうえで実部の enclosure を用いる。
ゼロ位置表や RH を入力しない。詳細は [tail_certificates.json](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/tail_certificates.json)。

|範囲|\(N=m\)|認証 \(L\tau\) 上界|認証 \(\sigma_{\min}(B)\) 下界（raw）|
|---|---:|---:|---:|
|\(a\in[1.499999,1.500001]\)|4|\(<4.529\cdot10^{-7}\)|\(>0.0517\)|
|\(a\in[1.999999,2.000001]\)|6|\(<7.135\cdot10^{-40}\)|\(>0.0340\)|

各区間は単一点の近傍を推測したものではない。\(a\) 自体をその区間を含む Arb ball にし、
同時に全値を包含した計算である。これは有限範囲の計算機援用 certificate。
抽象的な全窓定理とは区別する。
単一点 \((a,N)=(1.5,4),(2,4),(2,6),(3,6)\) も認証済み。
\((1,2),(1,4)\) ではこの粗い十分条件は不成立、\((0.5,2)\) では TC4 の前件が不成立。
これらを非可逆の反例と分類しない。

## TC4. 三種類の conditioning

1. **raw 座標**：\(\sigma_{\min}(B)\)、\(\kappa_2(B)\)。微分列の単位・倍率に依存する。
2. **head の pullback Gram**：\(B^*B\) で whitening すると、独立列について特異値が1になる。
   これは射影後の norm を選んだ恒等式で、元の関数の大きさを評価していない。
3. **physical Gram**：\(G_m=(\langle f_i,f_j\rangle_{L^2(\mathbb R)})\) または
   \(G_{a,m}=(\langle R_af_i,R_af_j\rangle)\) を使う。
   元の norm を保持した写像は \(BG_m^{-1/2}\) または \(BG_{a,m}^{-1/2}\)。

\(G_m>0\) は \(p(x^2)\Xi(x)=0\) a.e. が多項式 \(p=0\) を強いることによる。
\(G_{a,m}>0\) は同じ有限線形結合が区間で零なら、解析性から全実線で零になることによる。
両方とも RH 不要。

physical norm での摂動評価は
\[
\sigma_{\min}(BG_m^{-1/2})
\ge\sigma_{\min}(AG_m^{-1/2})-\|EG_m^{-1/2}\|_2,
\tag{TC9}
\]
であり、例えば square case では
\[
\sigma_{\min}(BG_m^{-1/2})\ge
\frac{L^{-1}-\tau}{\sqrt{\lambda_{\max}(G_m)}}.
\tag{TC10}
\]
Gautschi 下界を得ただけで physical 条件数が良いとは言わない。
離散直交多項式・Arnoldi は同じ span の基底変更として採用できるが、
その基底に変換した tail と physical Gram を一緒に運ぶ必要がある。

さらに固定 \(N\)、\(m=N\)、\(a\to\infty\) では
\[
\sigma_{\max}(B)=\Theta_N(a^{-1/2}),\quad
\sigma_{\min}(B)=\Theta_N(a^{-2N-1/2}),\quad
\kappa_2(B)=\Theta_N(a^{2N}).
\tag{TC11}
\]
最小特異値は AR5、最大特異値は最初の列による下界と有限成分の上界から従う。
global \(G_N\) は \(a\) に依存しない正定値行列なので
\(\sigma_{\min}(BG_N^{-1/2})=\Theta_N(a^{-2N-1/2})\) でもある。
最悪方向の最小 global-\(L^2\) lift cost はその逆数で増える。
この極限では不安定さの全部を単項式座標のせいにはできない。

## TC5. 固定 head に限る physical approximation theorem

\(\mathcal R_m=\operatorname{span}\{f_0,\ldots,f_m\}\)、\(\Pi_m\) をその global \(L^2\) 射影、
\(T=P_NR_a\) を head への写像とする。\(TT^*=I\) で、正確に
\[
K_m:=B_mG_m^{-1}B_m^*=T\Pi_mT^*.
\tag{TC12}
\]
CY1 より \(\Pi_m\to I\) strongly。対象 head は固定有限次元なので
\[
0\le K_m\uparrow I,\qquad\|K_m-I\|\to0.
\tag{TC13}
\]
証明：固定有限基底上の行列成分がすべて収束するため、有限行列の operator norm でも収束する。
従って任意固定 \(a,N\) と \(0<\epsilon<1\) に対し、ある有限 \(m\) 以降
\((1-\epsilon)I\le K_m\le I\)。full row rank と、最小 norm right inverse の
\(\|J_m\|\le(1-\epsilon)^{-1/2}\) が従う。
これは存在定理であり、必要 \(m(a,N,\epsilon)\) の評価は与えない。

\(BG_m^{-1/2}\) の非零特異値は、\(E_N^+\) と **射影前** \(\mathcal R_m\) の principal-angle cosines。
一方、射影後 span が \(E_N^+\) になった時の角度は全部0であり、lift cost の証拠にならない。
TC11 と TC13 は矛盾しない。前者は \(N=m\) を固定して窓を増やし、後者は窓・headを固定して列を増やす。
窓・head・次数を同時に増やす定量評価は本監査の対象外。

## TC6. 数値の正当な範囲

実験では Cholesky \(G=LL^*\) を使い \(B(L^*)^{-1}\) の特異値を求める。
これは \(BG^{-1/2}\) と同じ特異値を持つ。
monomial 条件数、physical Gram、tail、projected span を混ぜない。
全線 Fourier 標本評価は global \(L^2\) 上の有界写像ではないので、
fixed-column tail が小さいという事実を、無制限の次数で一様に小さい operator と読み替えない。

実験・認証・一般証明を分けた結果は [diagnostics.md](diagnostics.md) を参照。
Priority 3 の定数抽出、growing-m、ground/parity/Weil-energy convergence は開始しない。
