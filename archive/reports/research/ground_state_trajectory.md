**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/ground_state_trajectory.md` · Original SHA-256: `b956c37e70555f93670f4fc4947c6cf28e5b53d2c6579b10e5ec075463a3634b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Ground-state trajectory, rate selection, and probability gate

2026-09-30。RH OPEN。今回の Track B/C の限定監査。
既存の 375 ファイル・旧 state・proof graph は変更しない。
本稿の恒等式は既存の actual Weil form からの直接計算であり、新規性を主張しない。
数値結果の所有者は main の Track A。本稿は数値的な branch 選択を証明済みと扱わない。

## 1. 固定する行列と二つの空間識別

\[
 a=\log\lambda,\quad L=2a,\quad
 V_{j,L}(t)=L^{-1/2}e^{2\pi ij(t/L+1/2)},\quad |t|\le L/2,
 \qquad |j|\le N .
\]
区間外では 0 とし、周期 convolution に置換しない。
\(Q_{L,N}=(Q_W(V_{j,L},V_{\ell,L}))\) は Gamma・pole・全 prime-power
項を含む Hermitian 行列である。規約は
[既存 dictionary](common_variational_dictionary.md) (A1)–(A2) と
[CCM 原典 §§3–5](https://arxiv.org/html/2511.22755v1) に固定する。
標準 norm は \(dt\) の \(L^2\) norm。正値性、ground の偶性・単純性は仮定しない。

有限 \(L\) を動かすときは
\[
 U_L:L^2([-L/2,L/2])\longrightarrow L^2([-1/2,1/2]),\qquad
 (U_Lf)(x)=\sqrt L f(Lx)
 \tag{1}
\]
が unitary で、\(U_LV_{j,L}=\phi_j=e^{2\pi ij(x+1/2)}\)。
これで固定 \(N\) の行列を同じ係数空間で比較できる。
ただし prime shift は \(\log n/L\)、Gamma multiplier は
\(h_\Gamma(\omega/L)\)、pole test は \(e^{\pm Lx/2}\) に変わる。
したがって dilation は異なる \(L\) の形式を同一にする intertwiner ではない。

固定 \(L\)、\(M\ge N\) では係数を 0 で延長する \(J_{N,M}\) により
\[
 Q_{L,N}=J_{N,M}^*Q_{L,M}J_{N,M}.
 \tag{2}
\]
従って \(e_0(L,M)\le e_0(L,N)\)。gap の単調性は従わない。
この包含と (1) は基底の識別として整合するが、異なる窓の零延長とは別の map。
大きい窓への零延長は一般に小さい Fourier span を大きい有限 Fourier span へ送らない。

**global limit の座標注意。**
固定された非零の rapidly decreasing \(f(t)\) の normalized cut は、
元の \(\mathbb R_t\) 上の零延長で \(f/\|f\|_2\) に強収束する。
一方、その \(U_L\) 像は \(x=0\) へ集中して弱収束 0、norm は 1。
例えば bounded test に対する pairing は \(O(L^{-1/2}\|f\|_1)\) であり、
density により全 \(L^2\) test でも弱収束 0。
対応する rank-one projector は strong operator topology で 0 に収束しても
operator norm は 1 のままである。
これは座標による集中であり、履歴依存・算術核の消滅を意味しない。
有限 \(L\) の微分には (1)、global kernel の同定には元の log-space の零延長を使い分ける。

## 2. Prime-power event は jump でなく derivative corner

\(n=p^k\)、\(h=\log n\)、\(c_n=\Lambda(n)/\sqrt n=\log p/\sqrt n\) とする。
内積は第 1 変数で線形、\(\tau_hf(t)=f(t-h)\) とし、
\[
 C_{j\ell}(L,h)=\langle\tau_h V_{j,L},V_{\ell,L}\rangle.
\]
\(L\le h\) では overlap は測度 0 なので \(C=0\)。
\(L>h\) では直接積分により
\[
 C_{j\ell}(L,h)=e^{-2\pi ijh/L}e^{\pi i(j-\ell)}
 \int_{-1/2+h/L}^{1/2}e^{2\pi i(j-\ell)x}\,dx .
 \tag{3}
\]
この項の Hermitian form は \(-c_n(C+C^*)\) である。
\(L=h+\delta,\ \delta\downarrow0\) において、固定 \(j,\ell,h\) なら
\[
 C_{j\ell}(h+\delta,h)=\frac{\delta}{h}+O_{j,\ell,h}(\delta^2).
 \tag{4}
\]
両端の全基底値が \(L^{-1/2}\) なので、先頭係数は index に依存しない。
従って、\({\bf1}=(1,\ldots,1)^T\) として
\[
 [\partial_L Q_{L,N}]_{L=h+}-[\partial_L Q_{L,N}]_{L=h-}
 =-\frac{2\Lambda(n)}{\sqrt n\log n}{\bf1}{\bf1}^* .
 \tag{5}
\]
\(\lambda=\sqrt n\) 座標なら
\[
 [\partial_\lambda Q_{\lambda,N}]_+
 -[\partial_\lambda Q_{\lambda,N}]_-
 =-\frac{4}{kn}{\bf1}{\bf1}^* .
 \tag{6}
\]
別の位相規約の基底では同じ rank-one form を unitary conjugation する。
prime-power でない整数の閾値にはこの項はない。

Gamma 項も固定 \(N\) で \(L>0\) に関して smooth：
\[
 Q^\Gamma_{j\ell}(L)
 =\frac1{2\pi}\int_{\mathbb R}h_\Gamma(\omega/L)
       \widehat\phi_j(\omega)\overline{\widehat\phi_\ell(\omega)}\,d\omega .
\]
零延長された \(\phi_j\) の Fourier transform は \(O((1+|\omega|)^{-1})\)。
\(L\) の compact subinterval 上で multiplier の微分を積分内へ移せる。
pole 項は固定有限区間の exponential integrals なので smooth。
局所的に入る prime powers は有限個である。

以上より actual \(Q_{L,N}\) は連続・局所 Lipschitz、prime-power event 間では smooth。
和の cutoff を \(n<\lambda^2\) としても \(n\le\lambda^2\) としても、
等号の項自体が 0 なので行列値は一致する。
偶奇分解の odd block では係数和が 0 であり、(5) の一次 corner は消える。
これは global ground の偶性を証明しない。

## 3. Projector の変化と有限 endpoint の一意性

固定 \(N\)、ある区間で ground が単純、
\(\Delta(L)=e_1(L)-e_0(L)>0\) と仮定する。
固有値を囲む局所 contour により
\[
 P_0(L)=\frac1{2\pi i}\oint_\Gamma(z-Q_{L,N})^{-1}\,dz.
 \tag{7}
\]
これは現在の行列だけで決まる。smooth な点で
\[
 S=(Q-e_0)^{-1}(I-P_0),\qquad
 P_0'=-S Q'P_0-P_0Q'S,\qquad
 \|P_0'\|\le \frac{2\|Q'\|}{\Delta}.
 \tag{8}
\]
右辺の定数 2 は十分な上界で、最適性を主張しない。
compact 区間で gap に正の下界があれば、prime corner を越えても
\[
 \|P_0(L_2)-P_0(L_1)\|
 \le 2\int_{L_1}^{L_2}\frac{\|Q'(L)\|}{\Delta(L)}\,dL .
 \tag{9}
\]
微分は almost everywhere でよい。corner で射影そのものが跳ぶという結論は出ない。

Hellmann–Feynman により、event で ground が単純なら one-sided derivative の差は
\[
 e_{0,L}'(h+)-e_{0,L}'(h-)
 =-\frac{2\Lambda(n)}{\sqrt n\log n}
       \left|\sum_{j=-N}^N v_j(h)\right|^2 .
 \tag{10}
\]
従って有限の算術 event は傾きへ exact に現れる。
これは全区間の \(e_0(L,N)\) 単調性を意味しない。
固定 \(N\) の scaled Fourier spaces は窓について nested ではないからである。

一次資料は Kato,
*Perturbation Theory for Linear Operators*, 1980 edition の reprint,
[原著 PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf)：
II §1.4、printed pp.67–68、(1.16)–(1.19) が contour projection。
VII Thm.1.8、p.370 は holomorphic family の isolated finite eigenvalue system の結果。
(8)–(10) の有限 Hermitian・piecewise smooth 版は本稿で直接微分したもの。
prime event 全体を holomorphic family として定理を無条件適用しない。
gap が 0 へ落ちる場所の個々の projector の連続性もこの議論の結論ではない。

**履歴の判定。**

- 同じ有限 \((\lambda,N)\) の単純 ground line は、そこへ来た path に依存しない。
  vector の符号・複素位相の違いは line の違いではない。
- degeneracy では ground subspace の projector は一意だが、その中の vector は一意でない。
  continuation rule が異なる vector を選んでも、新しい算術的履歴法則にはならない。
- overlap 最大で追跡する branch は、crossing 後に instantaneous ground でなくなり得る。
  数値 branch tracking を ground の定義に代用しない。
- \(N\) の増加は次元を変えるので (8) をそのまま微分として使わない。
  (2) の埋込み、残差 \((I-JJ^*)Q_{L,M}Jv_N\)、大きい行列の spectral separation
  で比較する必要がある。
- 異なる cofinal paths が異なる limiting lines を与える可能性は一般論では排除されない。
  しかし actual \(Q\) についてその二つの極限を証明するまでは
  HISTORY-DEPENDENT SELECTION と判定できない。

## 4. 固定 radical span の Gram は何を制御できるか

\[
 f_j=k^{(2j)},\quad 0\le j\le m,\qquad
 T_{L,N}f=P_N(1_{[-L/2,L/2]}f).
\]
各 \(f_j\) は actual kernel の偶な rapidly decreasing function。
周期 Fourier 投影の境界項は \(f_j(L/2)=f_j(-L/2)\) により消えるので
\[
 \|T_{L,N}f_j-f_j\|_{L^2(\mathbb R)}
 \le \|1_{|t|>L/2}f_j\|_2
       +\frac{L}{2\pi(N+1)}\|f_j'\|_2 .
 \tag{11}
\]
左辺の有限像は零延長で比較している。
sharp cutoff の全実線 weak derivative に jump がないと仮定したのではなく、
区間上の periodic integration by parts を使った。

従って固定 \(m\)、\(L\to\infty,\ N/L\to\infty\) なら
\[
 G_{ij}^{L,N}=\langle T_{L,N}f_i,T_{L,N}f_j\rangle
 \longrightarrow G_{ij}^{\infty}=\langle f_i,f_j\rangle.
 \tag{12}
\]
\(\widehat f_j(z)=(-1)^jz^{2j}\Xi(z)/4\) で \(\Xi\not\equiv0\) だから、
有限個の \(f_j\) は独立で \(G^\infty>0\)。
各列の unit normalization 後の Gram にも対応する正定値極限がある。
これは固定 \(m\) の結果であり、\(m\to\infty\) や数値上の小さい最小 Gram eigenvalue
に一様な良条件性を与えない。energy の convergence rate も (11) からは出ない。

診断用の \(N=\max(4,\lceil a^2\rceil)\) と
\(N=\max(4,\lceil a^3\rceil)\) はともに \(N/a\to\infty\)。
有限の sample 点は cofinal limit を実証せず、この二経路を canonical と主張しない。

## 5. 次次数による選択の必要条件

正規化を線形 map と扱わず、有限像の raw columns から
\[
 M_{ij}=Q_W(Tf_i,Tf_j),\qquad G_{ij}=\langle Tf_i,Tf_j\rangle
\]
を作り、\(Mc=\mu Gc\) を解く。
固定 \(m\) の restricted span で選択が成立する十分条件の一つは、実際に証明された
\(r_\nu>0,\ r_\nu\to0\)、baseline \(b_\nu\)、Hermitian matrix \(K_{\rm eff}\) に対し
\[
 G_\nu^{-1/2}\frac{M_\nu-b_\nu G_\nu}{r_\nu}G_\nu^{-1/2}
 \longrightarrow K_{\rm eff}
 \quad\text{in operator norm},
 \tag{13}
\]
かつ \(K_{\rm eff}\) の最小固有値が単純であること。
このとき whitened coefficients の minimizing line はその固有lineへ収束する。
選ばれた physical function が \(k\) かは別の同定である。
full ground の結論には radical span の補空間と coupling の制御がさらに必要。
restricted Ritz gap を actual full gap の下界として使えない。

(13) は条件付きの有限次元補題であり、今回の actual \(M_\nu\) について
\(r_\nu,K_{\rm eff}\)、path に一様な remainder を得たという主張ではない。
全列の energy が 0 へ行くことや、finite score の大小だけでは (13) を満たさない。
特に signed \(Q(Tf,Tf)\)、その絶対値、\(Q(Tf,Tf)/\|Tf\|^2-e_0\)、
後者を full gap で割った量は異なる。

一次資料の範囲：
[Braides–Truskinovsky, author draft (2007)](https://cvgmt.sns.it/media/doc/paper/727/2007BT.pdf)、
*Asymptotic expansions by Γ-convergence*,
§1.1、draft pp.6–7、(10)–(17)、Remarks 1.5,1.7 は
rescaled functional・minimizing sequences の compactness・適切な scale を要求する。
§1.2 の locking と §3 の parameter nonuniformity も、一般の Γ-limit が
一意の次次数 selector を自動提供しないことを明示する。
published version は *Continuum Mech. Thermodyn.* 20 (2008), 21–62。
上の locator は取得した draft のページで、published pagination とは区別する。

また [Kuwae–Shioya (2003), 原著 PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2003/0011/0004/CAG-2003-0011-0004-a001.pdf)
Defs.2.8,2.11–2.13、pp.622,626–627、Thm.2.4、pp.627–628、
Thm.2.6、p.632、Cor.2.5、p.634 の Mosco/compact spectral convergence は
非負閉形式と空間識別・liminf/recovery・compactness を前件とする。
固有値・部分列固有vector の収束と next-order rate selection は別問題。
actual expanding Weil form にこれらの前件を証明せず適用しない。

## 6. Canonical probability が selector を追加するか

新しい確率モデルは導入しない。既存有限 self-adjoint matrix に標準的に付随する
候補が何を必要とするかだけを点検する。

spectral projection-valued measure \(E_Q\) は \(Q\) から決まるが、scalar probability
\[
 \mu_f(B)=\langle f,E_Q(B)f\rangle/\|f\|^2
 \tag{14}
\]
には非零 input vector \(f\) が必要。
\(f=k\) を入力すればその方向の選択を独立に説明したことにならない。
\((2N+1)^{-1}\operatorname{Tr}E_Q(B)\) は finite counting probability だが、
全 eigenspaces を数えるもので、指定された kernel direction を選ばない。

仮に有限 heat state
\[
 \rho_\beta=\frac{e^{-\beta(Q-e_0)}}{\operatorname{Tr}e^{-\beta(Q-e_0)}}
 \tag{15}
\]
を検査するなら、\(\beta\) は別に指定する scale。
単純 ground、\(d=2N+1\) では
\[
 1-\operatorname{Tr}(P_0\rho_\beta)
 =\frac{\sum_{j\ge1}e^{-\beta(e_j-e_0)}}
        {1+\sum_{j\ge1}e^{-\beta(e_j-e_0)}}
 \le(d-1)e^{-\beta\Delta}.
 \tag{16}
\]
従って増大する系で \(\beta\Delta-\log d\to+\infty\) は十分条件。
gap が潰れるとき、固定 \(\beta\) で ground を選べるとは言えない。
ground multiplicity が \(g>1\) なら fixed finite system の \(\beta\to\infty\) limit は
\(P_0/g\) で、個々の vector を選ばない。
normalized vector heat flow にも初期 vector、非零 ground overlap、time が必要。
無限系の heat trace の存在は、本稿の有限行列計算からは従わない。
各有限系で先に \(\beta\to\infty\) とすれば既存の ground projector を回収するが、
これは同じ finite ground の別表現であり、その cofinal limit が \(k\) になるという追加入力ではない。

以上は heat/Gibbs を新しい研究 route として採用したものではない。
現在の arithmetic input には、外部 scale や input vector を不要にして
\(k\) を一意に選ぶ probability law は同定されていない。

## 7. 限定 verdict

**NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED（Track B/C の範囲）。**

証明できたことは actual prime event の連続性と derivative corner、
gap のある有限 ground projector の制御、固定 radical span の Gram convergence、
および probability 候補の追加入力である。
これらは無条件の limited calculations で、RH の進展や全域正値性ではない。

有限 scores の違い・消失速度・最速方向が \(k\) かという実測判断は Track A の出力に委ねる。
有限 endpoint には intrinsic history は入らない。
cofinal paths の共通 limit も異なる limit も、ここでは actual arithmetic から証明されていない。
従って path-independent selection の証明不足を history-dependent selection の証明へ反転しない。
一般変分・摂動定理の全文再証明、文献網羅、新規性判定はこの bounded audit の対象外。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/common_variational_dictionary.md`](common_variational_dictionary.md)
