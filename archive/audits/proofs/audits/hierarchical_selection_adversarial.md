**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/hierarchical_selection_adversarial.md` · Original SHA-256: `dc5d36261b2026345b893b7cd33e982631106492a0533158fd5e2a98998483d9`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Hierarchical selection / resolution scale の独立敵対監査

2026-09-30。RH OPEN。新規 request と既存の確定式を読み、今回の新規監査ファイルだけを編集する。旧成果物・旧 state・保存 baseline・proof graph は変更しない。有限模型は actual Weil や RH の反例と取り違えない。

## HS1. 境界座標の係数 — 修正必須 / 規約を固定

\(Y=\pi e^{2a}\)、\(A=f(a)\) とし、固定 derivative column の第一 theta 項を考える。\(v=Y(t-a)\) なら
\[
\pi e^{2t}=Y e^{2v/Y}=Y+2v+O(Y^{-1}),
\qquad \frac{f(a+v/Y)}{A}\longrightarrow e^{-2v}.
\]

旧ノートの \(e^{-v}\) は
\[
\beta=2Y,\qquad v=\beta(t-a)
\]

という別の座標で成立する。本監査の以下の式は後者を用いる。周波数変数は \(\xi=\omega/\beta\)、最大周波数比を \(h=\Omega/\beta\) とする。\(c=N/(aY)\) なら \(h\sim\pi c/2\)。\(Y\) と \(\beta\) を途中で取り替え、Lorentzian や resolution threshold の係数を失わない。

## HS2. 周期 Fourier 射影は片側連続 cutoff と異なる

even \(f\) の外側 tail transform を
\[
T_a(\omega)=2\int_a^\infty f(t)\cos(\omega t)\,dt
\]

とする。periodic grid \(\omega_n=\pi n/a\) では、片側 profile が \(F(v)\) のとき
\[
T_a(\omega_n)\sim
\frac{2A}{\beta}(-1)^n C_F(\xi_n),\qquad
C_F(\xi)=\int_0^\infty F(v)\cos(\xi v)\,dv.
\]

\(F=e^{-v}\) では \(C_F(\xi)=(1+\xi^2)^{-1}\)。左右二つの端点が同じ periodic seam に写るので、片側 Fourier transform \((1+i\xi)^{-1}\) をそのまま単一 cutoff の symbol として用いてはならない。

exact な periodization による確認もできる。区間 \(I=[-a,a]\) 上で
\[
G_a(t)=\sum_{\ell\in\mathbb Z}f(t+2a\ell),\qquad
H_a(t)=G_a(t)-f(t)
\]

とすると
\[
\delta:=P_NR_af-f,\qquad
\delta|_I=(I-P_N)H_a-(I-P_N)G_a.
\]

これは algebraic identity であり、近似ではない。\(H_a\) の seam profile が \(F(|v|)\) となり、\(G_a\) の grid coefficients は full \(\widehat f(\omega_n)\) により決まる。

full-transform high-frequency 項を相対的に捨てられる regime で、\(\delta\) の右端の scaled profile は
\[
D_hF(v)=
\begin{cases}
-F(v),&v>0,\\
((I-\Pi_h)EF)(v),&v<0,
\end{cases}
\qquad EF(v)=F(|v|),
\]

である。ここで \(\Pi_h\) は全実線の \(|\xi|\le h\) への Fourier 正射影であり、original periodic \(P_N\) と同一視したのではなく、seam scaling の極限で現れる。

\(F=e^{-v}\) では内側 profile は
\[
K_h(v)=\frac2\pi\int_h^\infty
\frac{\cos(\xi v)}{1+\xi^2}\,d\xi,\qquad v<0.
\]

内側の符号は正、外側は \(-e^{-v}\)。\(K_h\) は一般に符号を変え、単調な正の境界層ではない。

## HS3. 正しい profile mass と formal threshold

folding した profile の norm は
\[
J_h(F)=\|F\|_{L^2(0,\infty)}^2+
\frac12\|(I-\Pi_h)EF\|_{L^2(\mathbb R)}^2,
\]

であり、正射影の contraction から
\[
\|F\|_2^2\le J_h(F)\le2\|F\|_2^2.
\]

特に
\[
J_h(e^{-v})=\frac12+\frac2\pi\int_h^\infty
\frac{d\xi}{(1+\xi^2)^2}
=1-\frac{\arctan h+h/(1+h^2)}{\pi}.
\]

\(\operatorname{arctanh}\) ではない。\(J_0=1,J_\infty=1/2\)。archimedean 主項が \(\log\beta\) times norm で支配されれば、単一 column の support-only との比は \(2J_h\) となる。ただしこの最後の actual \(Q\) への接続には、prime/pole と remainder の相対評価が必要であり、profile algebra だけから宣言しない。

Gamma bound からの full \(\widehat f(\Omega)\) の exponential scale は \(e^{-\pi\Omega/4}\)、boundary amplitude は \(e^{-Y}\) times polynomial。従って固定の
\[
h>2/\pi\quad\Longleftrightarrow\quad
\Omega/Y>4/\pi\quad\Longleftrightarrow\quad
c>4/\pi^2
\]

では、full-transform 項を boundary scale に対して exponential に小さくできる。これは上界に基づく十分な regime。逆向きに \(h<2/\pi\) なら必ず何かが発散・不成立だとする lower bound は得ていない。等号の transition behavior も、この上界比較だけでは決まらない。

## HS4. \(\Omega/Y\to\infty\) だけから gap transfer は出ない

独立の厳密有限模型を示す。元の Gram を \(I_3\) とし
\[
A_Y=\operatorname{diag}(0,Y^{-6},1),\qquad
E_Y=(\log Y)^{-3}
\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix}.
\]

\(\|E_Y\|\to0\) であり、parameter \(h(Y)=\log Y\to\infty\) を resolution ratio として割り当てられる。しかし \(A_Y\) の ground は \(e_1\)、perturbed lowest line は
\[
\operatorname{span}(e_1-e_2)
\]

へ行く。理由は \(\|E_Y\|/Y^{-6}\to\infty\)。従って、大きい尺度での matrix convergence や解像度比の発散だけでは、より小さい gap に対する比較を代用できない。

これは actual \(P_N\) の反例ではない。実際の claim を採用するには、例えば次のいずれかが必要である。

* relevant support gap より小さい **同じ Gram metric での** operator error。
* 全有限 jet-profile 空間に一様な relative form bound と coercivity。
* 全 generalized matrix pencil を保つ、別の直接固有方向収束証明。

特に単独列の leading expansion の subtraction で、cancellation 後の小さな次項が正確だと決めない。basis と parameter に依存する係数で先頭項が消える場合、絶対 remainder のサイズを再点検する。

## HS5. Schur と generalized eigenproblem の違い

\(Mc=\mu Gc\) を block 分割したとき、exact elimination は \(M-\mu G\) に対して行う。単に \(A-BD^{-1}B^*\) を作って次の固有問題とするのは、一般に正しくない。

zero-energy congruence で \(M\) を block diagonal にする方法は使えるが、同じ congruence を \(G\) にも施す必要がある。新 Gram の極限や conditioning を無視しない。固定 low coefficient に関する非拘束 quadratic minimization と、unit \(G\)-norm 上での eigenproblem は異なる。

## HS6. Actual prime/pole 制御を点検するための十分条件

root の次の envelope は、成立すれば actual arithmetic 接続に十分な強さを持つ。

\[
|\delta(t)|\le
\begin{cases}
C A/(1+\beta\,\operatorname{dist}(t,\{-a,a\})),&|t|<a,\\
C A e^{-c\beta(|t|-a)},&|t|>a.
\end{cases}
\]

この envelope の original periodic coefficient からの一様導出は、別に示す必要がある。単に \(K_h(v)\) の pointwise limit だけでは足りない。periodization の exact split と coefficient の Abel summation は、その候補となる。

上の envelope を前提にすると、同側の相関は
\[
|C_\delta(d)|\lesssim
\frac{A^2}{\beta}
\frac{\log(2+\beta d)}{1+\beta d}
\]

で制御でき、反対側は \(d\le2a\) において \(d\) を \(|2a-d|\) に置き換えた同型の項が現れる。\(X=e^{2a}\asymp\beta\) の近くで \(r=|n-X|\) とすれば、\(\beta|\log(n/X)|\) は \(r\) と比較できる。整数間隔の和と \(\Lambda(n)\le\log n\) から
\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
|C_\delta(\log n)|
=O\!\left(\frac{A^2\log^3Y}{Y^{3/2}}\right)
\]

という粗い bound は得られる。\(d>2a\) では少なくとも一方が区間外となるため exponential suppression が復活し、同じ主尺度より小さくできる。pole は weighted \(L^1\) の評価から \(O(A^2\log^2Y/Y^{3/2})\)。いずれも \(A^2\log Y/Y\) より小さい。

これらは各 column の amplitude を用いた段階の点検であり、階層選択に必要な **全 jet space に一様な** bound へ移す箇所も監査する。

archimedean 項では内側の oscillatory \(1/v\) tail により絶対 \(L^1\) norm が対数的に増え得る。半直線 \(L^1\) 収束を勝手に仮定しない。scaled \(L^2\) と \(H^s\), \(0<s<1/2\), が一様有界なら高周波 log moment を抑えられる。低周波は Fourier sup の対数 bound と小区間分割から \(O(\log\log(a\beta))=o(\log\beta)\) に抑える方法がある。sharp gluing に \(H^1\) regularity を課す必要はなく、課すと一般に誤る。

## HS7. Support jet hierarchy — 先行代数の独立検算

builder の完成稿を待つ段階で、以下の algebraic spine を独立検算した。ここではまだ未読の remainder/domain の証明を承認したとはしない。

\(P_{2j}(y)\) の \(Y\) における Taylor jet matrix は
\[
W_{\ell j}
=4^jY^{2j+2-\ell}
\left(\binom{2j+2}{\ell}+O(Y^{-1})\right).
\]

\(C_{\ell j}=\binom{2j+2}{\ell}\), \(0\le\ell,j\le m\), は可逆で
\[
(C^{-1})_{0m}=(-1)^m/2^m.
\]

等間隔 nodes \(2j+2\) 上の polynomial interpolation により確認できる。jet basis の profile は \(w^r e^{-w}\) となり、極限 Gram は
\[
H_{rs}=\int_0^\infty w^{r+s}e^{-2w}\,dw
=\frac{(r+s)!}{2^{r+s+1}}>0.
\]

tail の共通尺度は
\[
\kappa_Y=\pi^{-1/2}Y^{-1/2}e^{-2Y}.
\]

jet coefficient \(z\) に対して \(\eta=Y^{m-2}z\) とすると、physical metric の候補極限は \(\|k\|_2^2\,4^{-m}|\eta_m|^2\)。先頭 coefficient を固定した \(H\)-minimum の profile は
\[
\frac{m!}{\|k\|_2}L_m(2w)e^{-w},
\qquad
\int_0^\infty L_m(2w)^2e^{-2w}\,dw=\frac12.
\]

したがって予測される minimum は
\[
\mu_{\min}\sim
\frac{a\kappa_Y(m!)^2Y^{4-2m}}{\|k\|_2^2}.
\]

特に \(m=1\) では最適値と \(k\) 単独の比は \(Y^{-2}\)。旧結果の境界を完全に消す trial の比 \(2Y^{-2}\) より小さく、矛盾しない。最小 profile は境界値0を強制したものとは異なる。

uniform positive profile form が実際に証明されれば、その逆平方根で physical metric を whiten し、rank-one limit の最大固有方向を見る方法で、縮退した generalized minimum を保護できる。これは HS4 の単なる operator-small perturbation と違い、全 profile 空間での relative control を利用する。

## 現時点の判定

座標係数、periodic folding、\(J_h\)、Schur pencil の注意、generic gap counterexample は独立確認済み。support hierarchy の代数係数も一致した。actual critical/resolved full form と support hierarchy の完成稿については、domain・一様 remainder・最終定理の範囲を追加監査する。現時点で full ground、G*、RH を得たとは主張しない。

## HS8. Fourier resolution 完成稿の独立監査

research/fourier_resolution_transition.md の F1–F16 を読取検算した。参照される旧外部論文の全再監査ではなく、この新規計算の定義・exact split・一様誤差・prime/Gamma/pole の整合を対象とする。

**F1–F7: PASS。** Periodization の係数 \(1/(2a)\)、grid tail の \(2B_Y/\beta\)、\((-1)^n\)、cosine transform、complex coefficient に対する polarization は整合している。内外の \(L^2\) norm は support が分かれるので直接加算でき、periodic Parseval の係数は
\[
\kappa_Y=\frac{2B_Y^2}{\beta},\qquad
\frac{\|\delta\|_2^2}{\kappa_Y}\longrightarrow J_h(F)
\]

となる。\(J_h\) の半係数は左右両端が同じ seam に折り返される計算と一致する。F2 の文章について、\(H_a=G_a-f\) 自体は全実線上の自然な periodic function ではないので、区間への restriction を periodic extension する意味だと明記するよう依頼した。exact interval identity には問題がない。

**F10–F12: PASS。** Cosine-transform coefficients の total variation と geometric partial-sum bound により、seam からの距離について \(C B_Y/(1+\beta d)\) が得られる。near seam は absolute coefficient sum、away は Abel summation を使い分けている。\(h\ge h_0>0\) で定数は一様。outside tail の polynomial を指数へ吸収できるのも fixed \(m\) に限るという条件に適合する。

same-edge と opposite-edge の correlation を分離し、\(n\approx X=e^{2a}\) で整数間隔を使う prime estimate の \((\log Y)^3/Y^{3/2}\)、pole estimate の \((\log Y)^2/Y^{3/2}\) を確認した。これらは \(\kappa_Y a\asymp B_Y^2\log Y/Y\) より小さい。素数について振動相殺や RH を仮定していない。\(n>X\) の外側 exponential factor を落として無限和を誤評価することもしていない。

**F13: より強い \(O(B_Y^2/\beta)\) で PASS。** HS6 の慎重な \(o(\log\beta)\) 型評価へ弱める必要はない。低い scaled frequency \(|\xi|\le h_0/2\) では、interior high-pass の Fourier 積分に
\[
\left|\int_{-a}^a e^{i(\omega_n-\beta\xi)t}dt\right|
\le \frac4{|\omega_n|}
\]

を使える。coefficients を代入し、grid sum を積分へ比較すると
\[
|\widehat d(\beta\xi)|\le
\frac{CB_Y}{\beta}\int_{h_0}^\infty
\frac{|\Psi(\eta)|}{\eta}\,d\eta
\le\frac{C_mB_Y}{\beta}.
\]

従って低周波の \(|\log|\xi||\) は一様に可積分である。高周波は任意の固定 \(0<s<1/2\) の scaled \(H^s\) bound で制御する。circle の fractional norm は Fourier coefficients から得られ、zero extension で追加される endpoint cross term は
\[
C_s\int |d(v)|^2\operatorname{dist}(v,\partial I)^{-2s}\,dv
\]

である。endpoint の一様 sup、区間内の \(L^2\) bound、\(s<1/2\) によりこれも一様。sharp jump に \(H^1\) を課す誤りを避けている。両端の phase はこれらの norm bound に影響しない。

**F14–F15: PASS。** 以上と \(\log(\beta/(2\pi))=2a\) から、fixed jet unit ball 全体に一様に
\[
\frac{Q_W(P_NR_a e_{z,Y})}{2a\kappa_Y}\to J_h(F_z)
\]

が成立する。\(h_N\to h>2/\pi\) または \(h_N\to\infty\) の場合を覆う。\(h_N\) が収束しなくても、\(\liminf h_N>2/\pi\) と compactified interval \([h_0,\infty]\) 上の subsequence argument により、uniform coercivity が得られる。元の derivative basis の悪条件性を無視した各 column の引き算ではなく、jet unit ball 全体を先に制御しているため、HS4 の一般反例を回避している。

**F16 の論理 gate。** Uniform positive jet form と、同じ jet basis の scaled physical metric の rank-one limit があれば、後者を前者で whiten した reciprocal eigenproblem の最大固有値は一様に分離する。jet form 自体が \(h_N\) により変わってもよい。物理空間への map の rank-one limit が \(k\) を向くため、restricted minimum の normalized physical line は \(k\) へ行く。これは full matrix ground の gap を推定する手法ではない。support hierarchy 完成稿でこの metric limit を確認して、最終接続を固定する。

**Scope:** ここで確認した separation \(\liminf N/(aY)>4/\pi^2\) は十分条件である。これを真の必要閾値、未解像域での selection failure、全 \(N/a\to\infty\) 経路への定理、全 Weil matrix の positivity、G*、RH へ拡張しない。

## HS9. 完成した support hierarchy と transfer の監査

research/hierarchical_selection/notes/support_hierarchy.md SH1–SH9 と research/higher_order_gamma_selection.md を読取検算した。HS7 の未読 remainder/domain という留保は、以下の内部証明の範囲で解消した。外部原典をすべて再読したという意味ではない。

**Exact jet と actual arithmetic: PASS。** SH8 の逆行列係数、SH9 の有限 Taylor 余項、SH11 の exact profile を確認した。SH12a は必要な固定有限階の微分と polynomial moments を明記しており、even extension の cusp を smooth と扱っていない。第2 theta 項以降の指数差 \(e^{-3Y}\) は、固定次数の \(Y,n\) の polynomial と jet 座標変換を吸収する。従って full jet unit ball での weighted norm convergence が得られる。SH14–SH18 は既存 weighted-BV 延長上で global radical を用い、prime/pole を同じ jet 座標で制御している。global \(L^2\) 形式の closability や RH は仮定していない。

**最小方向と定数: PASS。** Raw physical Gram は \(G(a)\to G_\infty>0\)。変換
\[
L_Y=Y^{2-m}W(Y)^{-1}
\longrightarrow e_0\ell^*,\qquad
\ell_m=(-1)^m2^{-m}
\]
は一様有界であり、変換後の physical metric は
\(\|k\|_2^24^{-m}e_me_m^*\) へ行く。逆 Rayleigh 商の唯一の非零極限固有値は
\[
\|k\|_2^24^{-m}(H^{-1})_{mm}
=2\|k\|_2^2/(m!)^2.
\]
Laguerre の monic norm \((m!)^2/2^{2m+1}\) と一致する。その結果
\[
\mu_{a,m}\sim
\frac{a(m!)^2}{\sqrt\pi\|k\|_2^2}
Y^{7/2-2m}e^{-2Y},\qquad
\frac{c_j}{c_0}\sim
\frac{(-1)^j\binom mj}{4^jY^{2j}}
\]
を確認した。SH25 は切断前の関数の外側 tail を評価しており、零延長した minimizer を区間外で非零と扱う誤りは修正済み。

**Schur と Γ hierarchy: PASS。** 逆順の exact quadratic minimization の pivots は
\[
d_j\sim a\kappa_Y16^j((m-j)!)^2Y^{6j+4-2m}.
\]
同じ合同変換を Gram へも適用しており、pivot を generalized eigenvalue と同一視していない。SH31 の liminf は正な対角項の一つを残すことで成立する。Recovery は exact triangular coordinates の高次成分を零にし、その後固定 \(G_\infty\)-sphere へ戻すので、単なる raw truncation ではない。各 \(r<m\) の極限最小値が0であり、最後に projective \(k\) のみが残る。SH29 の行列は列 \(j\) の行 \(i>j\) に係数を持つので、記載「上三角」は「下三角」への表記修正を依頼した。

**Uniform positive jet transfer: PASS、条件を分離。** \(b_-I\le K_Y\le b_+I\) と raw Gram convergence の下では、SH33 は一様に孤立した rank-one 最大固有値へ \(o(1)\) で近づく。\(K_Y\) 自体の極限は不要。Physical normalization 後の jet vector は coercivity から有界で、raw coefficient line は \(e_0\) へ収束する。

ただし physical function が \(k/\|k\|_2\) へ収束するためには、固定列 \(\mathcal T_af_j\to f_j\) in \(L^2\) も必要である。Gram だけなら全列へ共通の等長回転を施せる。この条件は SH8 本文にあり、canonical \(P_NR_a\) について \(N/a\to\infty\) から証明されている。higher_order_gamma_selection.md §6 の要約ではこの条件が落ちていたので、併記を依頼した。これは actual Fourier transfer への反例ではなく、抽象要約の限定修正である。

従って HS8 の F16 接続は、固定列収束と uniform jet coercivity をともに使う形で **PASS**。各固定 \(m\) と \(\liminf N/(aY)>4/\pi^2\) に対し、canonical restricted minimum の単純性と normalized physical line の \(k\) への収束を得る。Support-only の Laguerre 定数を有限 \(h\) の別 profile form に転用していない。全 matrix ground、\(m\to\infty\)、underresolved path、G*、RH はここから出ない。

この読取時点の SHA-256（その後の表記修正前の snapshot）：

| 対象 | SHA-256 |
|---|---|
| research/fourier_resolution_transition.md | bbd44dc790984831155129d8be0acd6e71f615652e114a74879bf2968ee45b93 |
| research/hierarchical_selection/notes/support_hierarchy.md | d5be25c7c216fd4bdfa3a20b1a8f66c879e8e1419e848af9709e2f5678d278d3 |
| research/higher_order_gamma_selection.md | 703d9993cadfde976e08b2a63e354c80900f2f91a5b835185591c8fa12536e8e |

## HS10. 統合主文・Track B/C・数値転記の限定監査

research/hierarchical_selection.md、research/hierarchical_selection_candidate_matrix.md、research/hierarchical_selection_state.json を読取確認した。固定有限 \(m\) の restricted selector を全 finite Weil matrix の ground と取り違えておらず、未解像経路と小さい critical 比を失敗定理としていない。Level 2–4 の限定達成と Level 5 / G* / RH 未達の区別は整合している。state の Sonine dictionary が false という値には「現在の二 cutoff の energy/selection-preserving replacement」という限定があり、別の既知 exact dictionary の存在と矛盾しない。

HS9 の二点は解消済み：support ノートの三角方向は下三角へ、higher_order_gamma_selection.md §6 は raw coefficient line と fixed-column \(L^2\) convergence を必要とする physical line を分離した。Fourier F7 の要約にも固定列収束を明記するよう依頼した。canonical projector についてその証明は既に SH8 に存在するので、論証の追加仮定を未供給のまま置いたものではない。

### B. Rank-one 誤用の gate

research/prime_rank_one_flow.md の内部式を独立検算した。B1–B6 の determinant lemma、resolvent の右側にも \(R_0(z)\) を置く規約、重複固有空間の非結合方向、negative rank-one interlacing、Hellmann–Feynman と projector derivative の符号は整合する。複素 \(z\) で最後の resolvent を adjoint にしていない。

B7 の overlap は変数 \(u\mapsto\delta-u\) で \(j,\ell\) を交換でき、元の translated basis の積分と一致する。B9 の entrywise phase error と matrix dimension の係数から、relative approximation の十分条件 \((N+1)\delta/h\to0\) が出る。\(N\to\infty\) を隠した fixed-\(N\) Taylor 展開ではない。

B11 では \(0<\delta<a\) により、constant trial の相関が正、odd sine trial の相関が負となる。従って finite new-prime term は actual form 内で indefinite、Hermitian rank one ではない。これは full \(Q_W\) が不定であることを示さない。B12 の endpoint factor \(L=h\) の cancellation も正しい。背景 drift、finite-width higher rank、増える basis を落とす実際の反復模型は採用されていない。

この監査は掲示された内部恒等式・反例・適用限定を対象とする。引用された Dobosevych–Hryniv の原論文全体をこちらが再監査したとはしない。

### C. Sonine と current realization の gate

research/sonine_filtration_audit.md の定義から、次を直接検算した：

* \(Jg(t)=e^{t/2}g(e^t)\) の unitary 性と right Mellin/Fourier の \(s=1/2-iz\) 辞書。
* \(u_\Gamma(z)=\pi^{-iz}\Gamma(1/4+iz/2)/\Gamma(1/4-iz/2)\) による \(J\mathcal C C_0J^{-1}\) と anti-linear \(\mathsf K_{u_\Gamma}\) の一致、\(\mathcal V_t(u_\Gamma)=JK_{e^t}\)。
* 有限 \(b\) の compressed cosine operator は compact で norm \(<1\) だが、\(b\to\infty\) で norm \(\to1\)。strict finite-parameter inequality は uniform inverse bound ではない。
* pole-free self-Fourier seed について co-Poisson の積分項が零となり、\(J\mathcal P_{\rm co}(Ih)=k(-t)=k(t)\)。その input は compact-input gap theorem の前提を満たさない。
* current finite vector の自然な multiplicative image は compact support を持つ。cosine transform の entire continuation と Riemann–Lebesgue により、その非零 vector がどの \(L_b\) にも属さないという C11。
* \(u=1\) に対して \(\mathsf K_1f(t)=\overline{f(-t)}\)、従って \(\mathcal V_{-a}(1)=L^2[-a,a]\) という support-only Paley–Wiener chain。

この自然な辞書の失敗を、任意の抽象 unitary や未来の別近似の不可能性へ一般化していない。Suzuki の additional positivity/regularity axioms の全独立検証や、Burnol 全原証明の再読をこの監査に帰属しない。主文は energy・norm・ground selection を同時に運ぶ写像が未取得、と適切に限定している。

### 数値診断

新規 check_actual_resolution.py と check_scaled_boundary.py を静的読取し、結果 JSON の対象値と照合した。前者の columns は raw derivative basis であり、restricted Gram \(B^TB\) と matrix \(B^TQB\) を同じ列で組み立て、Cholesky whitening 後の coefficient を raw basis へ戻している。以前の unit-normalized-column coefficient と取り違えていない。Arb midpoints 以後の固有解析・quadrature は非認証であり、この監査では再実行していない。

\(\lambda=3\) の \(k''\) 係数は \(N=4,8,12,20,40\) の順に
\[
0.00444311123479,\quad0.00153958755961,\quad
-0.000347016579514,\quad-0.000382055743119,\quad
-0.000378820932108.
\]
主文/F9 の丸め値と一致する。192→256-node column norm difference は
\(1.5683141265\ldots\times10^{-95}\)。これは精度認証や全誤差上界ではない。

Scaled-profile script の \(J_h\) 行列は
\[
H_{rs}+\frac2\pi\int_h^\infty
\Re\frac{r!}{(1+i\xi)^{r+1}}\,
\Re\frac{s!}{(1+i\xi)^{s+1}}\,d\xi
\]
で、F7 の Plancherel 係数と一致する。12 profile problems と20 Fourier diagnostics は JSON の件数と一致。後者の theta tail は第1項かつ有限 quadrature と明記され、full actual coefficient の rigorous enclosure として扱っていない。

**この段階の結論：blocking mathematical error は未検出。** 修正後の限定付き解析定理と有限診断は分離されている。最終 snapshot hash は親の確定版連絡後に記録する。

## HS11. 確定版の最終判定・snapshot

**PASS（限定範囲）。** HS10 後の F7 は fixed-column physical convergence を明記した。main 第7問と final_report 第7問の解像度条件も「十分な」に統一され、必要性未証明という判定と整合する。state は COMPLETED_LIMITED_AUDIT、RH OPEN、G* false、full-ground comparison false。新規 completion report の七問を含め、blocking error は見つからなかった。

HS7 の未読留保、HS8 の F16 接続留保、HS9–HS10 の要約条件脱落は上記の確定版で resolved。履歴として前節を残す。独立確認したのは今回の内部解析と適用範囲であり、外部全原典や数値 enclosure の完全監査とはしない。旧408ファイルの hash 保存検査そのものは root の validation に委ね、こちらが別に全旧ファイルを hash 検証したとは書かない。

機械照合用の同じ snapshot は research/hierarchical_selection/notes/independent_audit_snapshot.json に保存した。以下は最終読取対象の SHA-256。audit 自身の hash は循環を避けるため含めない。

| 対象 | SHA-256 |
|---|---|
| research/hierarchical_selection.md | d707a1fb03b61273e71161c148186cf1c7a992846d9919b987e97a30e5182beb |
| research/hierarchical_selection_candidate_matrix.md | 11743ad1eafed38a04d4318c3d177224a1be39252db5bed222350977bac93c38 |
| research/hierarchical_selection_state.json | b4f57fe270afe210ad4ed3883bd3dbe4bdd3aa5d3778c5e8aad155c608b51294 |
| research/higher_order_gamma_selection.md | d8c937dbd2d49c3da5e167b29fcbf6429675241d2acdac8dffecf42f5121b29a |
| research/hierarchical_selection/notes/support_hierarchy.md | 49d4eaae5246290681ff45d30fd551b590aead13e9161df1880ec844df95c03e |
| research/fourier_resolution_transition.md | ac2b80d86f43521954c2b240db27be7fd082d123ad0d9b08992acae79f568aa9 |
| research/prime_rank_one_flow.md | 233051a64789382f58740dcf1193923713bc3bdba19b4c02deab1b95e4e42229 |
| research/sonine_filtration_audit.md | 57154ab8795bf1c0068cd523fb3a8c36defb8a3808d1c1a9afbe3ad54a4ea05c |
| research/hierarchical_selection/experiments/check_scaled_boundary.py | ae8ca40bd771faef22642381e97e5bbd385bbdd6e2248a05e2a37c38ccad0f9e |
| research/hierarchical_selection/experiments/scaled_boundary_results.json | 9c93754026c72a7830f1af08caf4735e5cc0264a70e872dd28f4856adec7444f |
| research/hierarchical_selection/experiments/check_actual_resolution.py | 076ab9c0e3f547bb3d5be39d747d60e7b5ce24e6308f6599fdbb3f25e8f8bf2d |
| research/hierarchical_selection/experiments/actual_resolution_results.json | 4efa77de0284519368a9c71ccd4708865756740a5c47b598102781ca4ba3da1f |
| research/hierarchical_selection/final_report_ja.txt | 87fcfc43aa6c51ea75247ad5709a955dbc8709718c0fbdc128aaa0daab46abed |


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/fourier_resolution_transition.md`](../../../reports/research/fourier_resolution_transition.md)
- [`research/hierarchical_selection.md`](../../../reports/research/hierarchical_selection.md)
- [`research/hierarchical_selection/experiments/actual_resolution_results.json`](../../../../artifacts/research/hierarchical_selection/experiments/actual_resolution_results.json)
- [`research/hierarchical_selection/experiments/check_actual_resolution.py`](../../../../artifacts/research/hierarchical_selection/experiments/check_actual_resolution.py)
- [`research/hierarchical_selection/experiments/check_scaled_boundary.py`](../../../../artifacts/research/hierarchical_selection/experiments/check_scaled_boundary.py)
- [`research/hierarchical_selection/experiments/scaled_boundary_results.json`](../../../../artifacts/research/hierarchical_selection/experiments/scaled_boundary_results.json)
- [`research/hierarchical_selection/final_report_ja.txt`](../../../reports/research/hierarchical_selection/final_report_ja.txt)
- [`research/hierarchical_selection/notes/independent_audit_snapshot.json`](../../research/hierarchical_selection/notes/independent_audit_snapshot.json)
- [`research/hierarchical_selection/notes/support_hierarchy.md`](../../../reports/research/hierarchical_selection/notes/support_hierarchy.md)
- [`research/hierarchical_selection_candidate_matrix.md`](../../../reports/research/hierarchical_selection_candidate_matrix.md)
- [`research/hierarchical_selection_state.json`](../../../../data/source-records/research/hierarchical_selection_state.json)
- [`research/higher_order_gamma_selection.md`](../../../reports/research/higher_order_gamma_selection.md)
- [`research/prime_rank_one_flow.md`](../../../reports/research/prime_rank_one_flow.md)
- [`research/sonine_filtration_audit.md`](../../../reports/research/sonine_filtration_audit.md)
