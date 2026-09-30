**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_parent/notes/variational_limits_and_prior_art.md` · Original SHA-256: `4f520ccf00ecde42931a7cd42e6feab8680a9bfb8c58b2bd98ef76451de1daa3`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Common parent: actual Weil 残差・gap・変分極限の限定監査

2026-09-30。**RH OPEN。新しい common parent の存在は証明していない。**
既知の摂動定理を actual finite Weil matrix に使うための量を固定する。
既存 local_to_global / accumulation / variational_closure は読取のみ。
以下の十分評価は標準的な spectral decomposition と Cauchy–Schwarz からの
具体化であり、新規性・算術的評価の達成を主張しない。

## 1. 比較する対象と、原典が既に与えている範囲

\[
a=\log\lambda,\quad \lambda>1,\quad
H_\lambda=L^2([-a,a],dt),\quad
V_j(t)=(2a)^{-1/2}e^{i\pi jt/a},\quad
E_N=\operatorname{span}\{V_j:|j|\le N\}.
\]
位相を掛けた原著の basis と同じ部分空間で、\(P_N\) は \(L^2\) 直交射影。
\(A_{\lambda,N}=Q_{\lambda,N}\) は **Gamma・極項を含む actual Weil form**
の \(E_N\) への行列制限。素数項は \(p^k\le\lambda^2\) までだが、
\(N\) は Fourier 次数であり素数 cutoff と同じではない。

比較対象 B は、prolate の \(h_{0,\lambda},h_{4,\lambda}\) の積分零の組合せ
\(h_\lambda\) を \([-\lambda,\lambda]\) の外で零にした後の
\[
b_\lambda(t)=k_\lambda(e^t)
=e^{t/2}\sum_{m\ge1}h_\lambda(me^t),\qquad -a\le t\le a.
\tag{1}
\]
これは Weil 最小固有vector として定義したものではない。

[CCM, Zeta Spectral Triples, 2511.22755v1](https://arxiv.org/html/2511.22755v1)
§7 Lemmas 7.2–7.3 は、適切なスカラー規格化で
\[
\|h_\lambda-h\|_{L^\infty[-\lambda,\lambda]}=O(\lambda^{-2})
\]
と proxy transform の収束を与える。§8 は、Weil 最低固有値の
simple-even 条件と、true ground state に対する proxy の精度を未解決とする。
原典が引用する Meixner–Schäfke (1954), §3.2, Satz 9, p.243 は
固定 prolate 次数 \(0,4\) の漸近であり、Weil gap の評価ではない。
本ノートでは同書原本まで独立確認したとはしない。

既存の定数・Gaussian tail の検算を採用すると、\(\mathscr X(z)=\xi(1/2+iz)\) に対し
\[
\sup_{|\Im z|\le r}
\left|\widehat b_\lambda(z)-\mathscr X(z)/4\right|
\le C_r\lambda^{-1/2+r}
+ C_r\lambda^{C_r}e^{-\pi\lambda^2},\qquad 0<r<1/2.
\tag{2}
\]
ここで \(\widehat b(z)=\int_{-a}^a b(t)e^{-izt}dt\)。
印刷式のスカラー差 \(1/4\) は零点に影響しない。
詳細は既存 [spectral_approximants_and_exact_gap.md](../../local_to_global/notes/spectral_approximants_and_exact_gap.md)
§4。今回 (2) を Weil energy の収束に読み替えない。

## 2. actual finite matrix について測るべき四つの量

\[
p_{\lambda,N}=P_Nb_\lambda\ne0,\quad
s_{\lambda,N}=\|p_{\lambda,N}\|_2,\quad
w_{\lambda,N}=p_{\lambda,N}/s_{\lambda,N},
\]
\[
\rho_{\lambda,N}=\langle A_{\lambda,N}w_{\lambda,N},w_{\lambda,N}\rangle,
\qquad
r_{\lambda,N}=(A_{\lambda,N}-\rho_{\lambda,N})w_{\lambda,N}.
\tag{3}
\]
固有値を **全 complex \(E_N\)** で重複度付きに
\(e_0\le e_1\le\cdots\) と並べ、
\[
\Delta_{\lambda,N}=e_1-e_0,\quad
\mathcal E_{\lambda,N}=\rho_{\lambda,N}-e_0,\quad
\tau_{\lambda,N}=\|(I-P_N)b_\lambda\|_2.
\tag{4}
\]
even sector だけで計算した第2固有値を、全空間の \(e_1\) と混同しない。
有限 matrix は Hermitian であることを式・基底・質量行列まで揃えて使う。
非正規直交 basis なら対応する一般化固有値問題が必要。

### 2.1 Rayleigh excess / gap

\(e_0\) が単純、単位 ground vector を \(v\) とする。固有展開から
\[
1-|\langle v,w\rangle|^2\le \mathcal E/\Delta.
\tag{5}
\]
位相を選べば
\[
\|w-v\|_2\le \sqrt{2\mathcal E/\Delta}.
\tag{6}
\]
単に \(\rho\) が小さい、あるいは \(\rho\to0\) では不十分。
必要なのは **ground energy との差と gap の比**。
\(\Delta\ge c>0\) の一様下界自体は必要条件ではない。
認証された \(e_0\) の下界 \(\ell_0\) と gap 下界 \(\underline\Delta>0\) があれば、
\(\mathcal E/\Delta\) を \((\rho-\ell_0)/\underline\Delta\) で上から抑えられる。

### 2.2 residual と Temple

全空間の第2固有値に対する下界 \(\beta\le e_1\) があり、
\[
\rho<\beta,\qquad \eta=\beta-\rho>0
\tag{7}
\]
なら、ground の直交補空間上 \(|A-\rho|\ge\eta\)。従って
\[
\|(I-|v\rangle\langle v|)w\|_2\le\|r\|_2/\eta,\qquad
\min_\theta\|w-e^{i\theta}v\|_2\le\sqrt2\,\|r\|_2/\eta .
\tag{8}
\]
さらに \((A-e_0)(A-\beta)\ge0\) から
\[
e_0\ge\rho-\frac{\|r\|_2^2}{\beta-\rho}.
\tag{9}
\]
これは ground に特化した Temple bound。第2固有値を隔離する (7) を省略できない。
例えば \(A=\operatorname{diag}(0,1)\)、\(w=(0,1)\) は residual 0 だが ground ではない。

**原典照合：** Zhu–Argentati–Knyazev,
*Bounds for the Rayleigh Quotient and the Spectrum of Self-Adjoint Operators*,
SIAM J. Matrix Anal. Appl. 34 (2013), DOI
[10.1137/120884468](https://epubs.siam.org/doi/10.1137/120884468)。
著者機関の [TR2013-068 PDF](https://merl.com/publications/docs/TR2013-068.pdf)
本文 p.3 (PDF p.5), (2.3) が Temple の空隙条件、
本文 p.12 (PDF p.14), (6.3) が residual / spectral separation の sin-angle bound。
同節は residual を任意に projected residual に置換する誤りの反例も示す。
有界自己共役作用素が原設定なので finite \(A_{\lambda,N}\) へ直接使える。
Davis–Kahan (1970), §2 p.10 の sin-angle 定理が同論文の一次引用先。
その1970原本は今回取得できず、厳密に確認した式は上記著者原稿 (6.3)。
(5)–(9) の rank-one 版はここで固有展開により直接確認した。

### 2.3 parity を勝手に補わない

raw (1) は有限 \(\lambda\) で \(t\mapsto-t\) に関して偶と仮定しない。
有限区間 Fourier の prolate 固有値は次数0と4で異なり、
積分零の組合せを full Fourier 固有vector と扱えない。
従って (3) の \(w\) も当然には even ではない。

もし別途 \(A\) が反転と可換、\(w\) が exact even、(7) が認証されれば、
\(\rho<e_1\) より \(w\) は ground に非零射影を持つ。
ground は単純なので反転固有値は +1、すなわち ground-even を導ける。
これは explicit \(w\) の偶性を独立に証明した場合に限る。
canonical symmetrization \(E_+b=(b(t)+b(-t))/2\) を採るなら、その変更と
\(\|b-E_+b\|\) を別の比較誤差として記録する。

## 3. 残差から weighted transform へ：\(N,\lambda\) を残した十分条件

ground の位相を (8) に合わせ、\(c_{\lambda,N}=s_{\lambda,N}e^{i\theta}\) と取ると
\[
\|c_{\lambda,N}v_{\lambda,N}-b_\lambda\|_2
\le
\underbrace{\sqrt2\,s_{\lambda,N}\frac{\|r_{\lambda,N}\|_2}
 {\beta_{\lambda,N}-\rho_{\lambda,N}}+\tau_{\lambda,N}}_{d_{\lambda,N}}.
\tag{10}
\]
Rayleigh 版では残差比を \(\sqrt{\mathcal E_{\lambda,N}/\Delta_{\lambda,N}}\) に置換する。
これは元の b の大きさに合わせて比較するためのスカラーであり、
ground の境界値を1とする正規化ではない。

各 \(r>0\) に対し
\[
C_r(\lambda)=
\left(\int_{-a}^{a}e^{2r|t|}dt\right)^{1/2}
=\sqrt{\frac{\lambda^{2r}-1}{r}}
\]
として Cauchy–Schwarz により
\[
\sup_{|\Im z|\le r}
\left|c_{\lambda,N}\widehat v_{\lambda,N}(z)-\widehat b_\lambda(z)\right|
\le C_r(\lambda)d_{\lambda,N}.
\tag{11}
\]
従って \(\lambda_j\to\infty\) の cofinal 列について、ES
（全空間の simple-even ground）と (7)、および
\[
\forall\,0<r<1/2,\qquad
C_r(\lambda_j)
\left[
\sqrt2\,s_j\frac{\|r_j\|_2}{\beta_j-\rho_j}+\tau_j
\right]\longrightarrow0
\tag{V}
\]
が **actual matrix** について認証できれば、(2) と合わせて
\(c_j\widehat v_j\to\mathscr X/4\) が閉部分帯上で一様に成立する。
同じ列で各 rational \(r\in(0,1/2)\) を扱えば全 compact を尽くせる。

ここで \(z_*=i/4\) の極限値は \(\mathscr X(z_*)/4\ne0\)。
従って十分大きい \(j\) で、分母を含む値規格化
\[
\mathscr X(z_*)\frac{\widehat v_j(z)}{\widehat v_j(z_*)}
\longrightarrow\mathscr X(z)
\]
まで従う。非零スカラー \(c_j\) は零点を変えない。
(V) はその正規化の conditioning も解消する強い十分条件であり、
必要最小の条件・既に証明された算術評価とは主張しない。
既知の ES 条件付き実零点定理と合わせれば RH へ至るので、
本ノートは (V) の成立を仮定して進展に数えない。

この finite diagonal route 自体には、途中で continuous Weil ground との
Galerkin 収束を挟む必要はない。逆に continuous ground を主張するなら、
finite residual のほかに complementary rows が必要：
\[
\|(QW_\lambda-\rho)w\|_2^2
=\|P_N(QW_\lambda-\rho)w\|_2^2+
 \|(I-P_N)QW_\lambda w\|_2^2 .
\tag{12}
\]
(12) は \(w\in\operatorname{Dom}QW_\lambda\) のときの恒等式。
form domain だけなら普通の \(L^2\) residual を書けない。
有限 Ritz vector の matrix residual が0でも、第2項は0とは限らない。

**より鋭い line-projection 版。**
上では unit vector の位相距離を使ったが、零点比較では scalar の絶対値も
自由に選べる。\(P_v\) を ground line への直交射影とし、
\(c^{\rm proj}_{\lambda,N}v=P_vp_{\lambda,N}\) と定義すれば、
内積の線形側の規約に依存せず
\[
\|c^{\rm proj}_{\lambda,N}v-b_\lambda\|_2
\le s_{\lambda,N}
\sqrt{\frac{\rho_{\lambda,N}-e_0}{\Delta_{\lambda,N}}}
+\tau_{\lambda,N}.
\tag{10'}
\]
residual 版でも \(s_{\lambda,N}\|r_{\lambda,N}\|_2/(\beta-\rho)\)
でよく、\(\sqrt2\) は不要。この右辺を \(d^{\rm proj}_{\lambda,N}\) と置き、
\[
\forall\,0<r<1/2,\qquad C_r(\lambda_j)d^{\rm proj}_{\lambda_j,N_j}\to0
\tag{V'}
\]
でも (11) 以下が成立する。\(c^{\rm proj}\) は零点位置を用いず、
Hilbert 空間の直交射影だけで定まる。
初期の \(c^{\rm proj}=0\) を形式的に除外する仮定は不要：
(V') と (2) が成立すれば
\(c^{\rm proj}_j\widehat v_j(i/4)\to\mathscr X(i/4)/4\ne0\) なので、
十分後では自動的に \(c^{\rm proj}_j\ne0\)。
これは root の sharp formulation を独立に検算したものである。

## 4. 実際の切断関数には BV 射影誤差を使える

(1) の \(h_\lambda(\lambda)\ne0\) の場合、
\(t=\log(\lambda/m)\) に内部 jump が生じる。
従って無条件の periodic \(H^1\) Fourier-tail bound を使わない。

\(b_\lambda\) の周期化について、内部 jump と
端点の継ぎ目 \(b_\lambda(-a+)-b_\lambda(a-)\) を含む全変動を
\(V_\lambda<\infty\) とする。Stieltjes 積分による部分積分から \(j\ne0\) で
\[
|\langle b_\lambda,V_j\rangle|
\le\frac{\sqrt{a/2}}{\pi|j|}V_\lambda .
\]
従って \(N\ge1\) に対し
\[
\tau_{\lambda,N}\le
\frac{\sqrt a}{\pi\sqrt N}\,V_\lambda .
\tag{13}
\]
これは finite prolate の滑らかな区間内部分と有限個の跳びに適用可能な
直接の Fourier 計算であり、\(V_\lambda\) の一様算術評価ではない。
具体的には \(g_\lambda(x)=\sqrt{x}h_\lambda(x)\) として
\[
V_\lambda\le
|b_\lambda(a-)-b_\lambda(-a+)|
+\sum_{1\le m\le\lambda^2}m^{-1/2}
\left[
\int_{m/\lambda}^{\lambda}|g_\lambda'(x)|\,dx+
|g_\lambda(\lambda)|
\right].
\tag{14}
\]
endpoint の jump を余分に数えることは上界として無害。
(14) は微分・jump を実際に評価する入口を示すだけで、
Lemma 7.2 の sup bound からその導関数評価を推論しない。

もし別途 \(b_\lambda\in H^m_{\rm per}\) を証明した場合には、より強い
\[
\tau_{\lambda,N}\le
\left(\frac{a}{\pi(N+1)}\right)^m\|b_\lambda^{(m)}\|_2
\]
が使える。raw construction でその前件を省略しない。
既存の determinant-tail の必要条件 \(N_j/\log\lambda_j\to\infty\)
も維持する。(13) と (V) の条件はこの UV 条件だけより強い。

## 5. prolate で小さい誤差が Weil energy で小さいとは限らない

二つの operator を同じ Hilbert 空間と domain に移した **明示的な恒等式**
\[
A_{\lambda,N}=B_{\lambda,N}+R_{\lambda,N}
\tag{15}
\]
があり、\(B w=\nu w\) を満たすなら
\[
(A-\rho_A(w))w=(R-\langle Rw,w\rangle)w.
\]
この場合は右辺のノルムを制御すればよい。
ただし proxy (1) は h 側の prolate eigenfunctions を算術和で移したもの。
その写像・圧縮・境界を保持する (15) は今回得られていない。
異なる operator の「ともに小さい固有値」だけは (15) の代わりにならない。

同一の finite Weil matrix 内なら一般に
\[
|\langle Af,f\rangle-\langle Ag,g\rangle|
\le\|A\|\,\|f-g\|_2(\|f\|_2+\|g\|_2).
\tag{16}
\]
\(\|A_{\lambda,N}\|\) は \(\lambda,N\) 依存であり、さらに比較相手の
energy が \(e_0\) に近いことも別途必要。
有限 prime-power 部だけでも、零延長 translation \(\tau_h\) を使えば
\[
P_\lambda(f,f)=
-\sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}
\langle(\tau_{\log n}+\tau_{-\log n})f,f\rangle
\]
から、(16) のその部分の定数として
\(2\sum_{n\le\lambda^2}\Lambda(n)/\sqrt n\) が現れる。
素数係数の正値性はこの signed correlation の符号を決めない。
Gamma 側と pole 側の比較も残る。
sup-norm の h 近似だけから、残差・Rayleigh excess・gap のいずれも出ない。

また \(A_j=\operatorname{diag}(0,\varepsilon_j)\)、
\(B_j=\operatorname{diag}(\varepsilon_j,0)\)、\(\varepsilon_j\downarrow0\) は
\(\|A_j-B_j\|\to0\) でも ground が直交する例。
絶対誤差だけでなく gap 比を使う必要を示す模型であり、actual Weil の反例ではない。

## 6. Γ/Mosco を common parent の代用にしない

確認した一次資料は Kuwae–Shioya,
*Convergence of spectral structures: a functional analytic theory and its applications to spectral geometry*,
Commun. Anal. Geom. 11 (2003), 599–673,
[原著 PDF](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2003/0011/0004/CAG-2003-0011-0004-a001.pdf),
[DOI](https://doi.org/10.4310/CAG.2003.v11.n4.a1)。
Defs.2.8,2.11–2.13 (pp.622,626–627) は recovery sequence・liminf・
asymptotic compactness を区別する。Thm.2.4 (pp.627–628) は
Mosco と strong resolvent、compact form convergence と compact spectral convergence
の対応。Thm.2.6 p.632 と Cor.2.5 p.634 は compact convergence の下で
重複度を含む固有値、および部分列での固有vector 収束を扱う。
非負閉形式が前件。Mosco (1969) の原本は今回取得せず、
正確な使用 formulation はこの一次論文に固定する。

本件に適用するには、少なくとも次を actual arithmetic から証明する必要がある：

1. \(\lambda,N\) の異なる空間の共通埋込み／識別と、閉形式・domain の指定。
2. 比較したい **同じ** limit functional に対する liminf と recovery sequence。
3. energy と norm の有界性から strong compactness を得る条件。拡大窓への質量逃走を除く。
4. normalized minimizer を比較する制約と、limit minimizer の一意性（位相を除く）。
5. その limit minimizer の transform が actual \(\mathscr X\) である同定、
   および (11) に代わる weighted transform の連続性。

このリストは一般論の適用条件を本件で具体化したもので、どれも
「A と B に同じ Γ-limit があるはず」という宣言で証明できない。
単位球制約付き最小化は凸問題ではないため、閉非負形式の Mosco と
normalized minimizer の convergence を無説明に同一視しない。
各 stage で \(e_0\) を引くことは vector を変えないが、原 Weil form の
正値性を証明せず、未知の limit energy とその shift の同定も自動ではない。
一般の Γ/Mosco 定理は (V) の速度を供給しない。

通常の全実線 \(L^2\) に raw Weil form をそのまま正の閉形式として置く案は、
既存 [variational_closure.md](../../notes/variational_closure.md) §2 の
expanding Fourier packet による closability 障害も持つ。
これは固定窓の閉形式や、別に正しく定義した weighted/domain モデルを否定しない。

## 7. actual arithmetic summation range の radical：近零 energy が ground を選ばない理由

以下は追加の安全な拡張 domain での直接検算である：
\[
\mathcal T_{\exp}=
\left\{f\in C^\infty(\mathbb R):
\int_{\mathbb R} e^{A|t|}|f^{(m)}(t)|dt<\infty
\quad\forall A>0,\ m\ge0\right\}.
\tag{17}
\]
usual \(L^2\)-completion を採ったのではない。全指数重みを持つ test 空間であり、
compact cutoff \(\chi_R f\to f\) はこの位相で成立する。
actual limit \(b(t)=k(e^t)\) は theta tail と modular evenness により
両端で super-exponential に減衰し、全導関数も (17) に入る。
その transform は既存の規約で
\[
\widehat b(z)=\mathscr X(z)/4.
\tag{18}
\]

非自明零点を重複度付きに \(z_\rho=(\rho-\frac12)/i\) と書く。
safe domain (17) では
\[
Q(f,g)=\sum_\rho
\widehat f(z_\rho)\overline{\widehat g(\overline{z_\rho})}
\tag{19}
\]
を定義できる。これは RH を使った \(\sum\widehat f\,\overline{\widehat g}\)
への変更ではなく、**共役点を区別した Weil pairing** である。
無条件の \(|\Im z_\rho|<1/2\) と、積分部分積分により
\[
|\widehat f(z)|\le C_m(f)(1+|\Re z|)^{-m}
\qquad(|\Im z|\le1/2)
\]
が成立する。\(C_m(f)\) は指数重み付き導関数 seminorm で抑えられ、
cutoff 誤差では0へ行く。\(N(T)=O(T\log(T+2))\) と合わせて、
(19) の絶対収束と cutoff 極限の交換が正当化される。

Gamma・極・prime 側も失われない。convolution
\(f*\widetilde g\) とその導関数は任意指数重みで減衰するため、
prime samples における
\(\sum_{n\ge2}\Lambda(n)n^{-1/2}|(f*\widetilde g)(\pm\log n)|\)
は絶対収束する。原点での archimedean principal-value/cancellation は
smooth seminorm で、pole 項は \(e^{|t|/2}\) 重みで制御できる。
従って compact test に対する actual explicit formula を同じ cutoff 極限で
(17) へ延長でき、(19) は零点側だけから捏造した別形式ではない。

(18) の各因子が全非自明零点で消えるので
\[
Q(b,g)=0\qquad(g\in\mathcal T_{\exp}).
\tag{20}
\]
これは **無条件**。RH も零点の単純性も不要で、重複度付き和の各項が0。
\(b(t-c)\) と \(b^{(m)}(t)\) の transform はそれぞれ
\(e^{-icz}\widehat b(z)\)、\((iz)^m\widehat b(z)\) だから同じ radical に入る。
異なる有限個の translates は一次独立である。実軸上の
\(\widehat b\ne0\) の開区間で exponential polynomial の独立性に帰着する。

**既知 framework との関係。**
[Connes–Consani, Spectral triples and ζ-cycles, 公刊 PDF](https://ems.press/content/serial-article-files/44477)
§3, p.118, (3.1) 直前は、
\(f\in\mathcal S_{\rm ev},\,f(0)=\widehat f(0)=0\) に対する
\(\mathcal E(f)\) が Weil radical に入ることを **明記** している。
従って summation range の radical という命題自体は literal な既知入力である。
[CCM, 2310.18423v2, §3.6 Proposition 3.6, p.15](https://arxiv.org/html/2310.18423v2#S3.SS6)
は、算術和 \(\mathcal E\) で得られる関数の transform が
\(R_\ell^\pm(z)\mathscr X(z)\) となり、全 polynomial multiples を得るとする。
本件の \(h\) も integral-zero Hermite combination であり、
この summation-range/factorization framework の中にある。
原著がここでの全 \(\mathcal T_{\exp}\) radical 命題をそのまま述べると主張せず、
(17)–(20) はその既知因子分解と Weil 公式からの直接の domain 検算と位置付ける。
新しい ground-selection 原理ではない。

特に \(b_R=\chi_Rb\) とすると
\[
Q(b_R,b_R)=Q(b_R-b,b_R-b)\longrightarrow0,\qquad
\|b_R\|_2\longrightarrow\|b\|_2>0.
\tag{21}
\]
交差項が0になることも (20) から正当化される。
従って near-zero Rayleigh energy を持つ actual arithmetic trial は、
global positivity を仮定しなくても存在する。
未知の負方向があれば、radical vector は ground ではない。
これは「actual Weil に負方向が存在する」という主張ではない。

さらに任意固定 \(m\) 個の独立 translates を同じ拡大窓へ cutoff すると、
その \(L^2\) Gram matrix は正定値極限へ、Weil matrix は0へ収束する。
固定窓 closed operator の min–max が適用できる設定では、従って
第 \(m\) 固有値の **上界** は \(o(1)\) となる。
もし全窓非負性（RH による帰結）もあれば、各固定低固有値は0へ行き、
特に bottom gap も0へ行く。無条件には上界だけであり、
gap collapse 自体をここから証明したとはしない。
有限 \(N\) への移行にも、これら cutoff vectors を form domain で近似する
Galerkin 精度を別途払う必要がある。

この actual radical は、小さな energy と同程度の低 eigenvalues が
ground 選択や向きの決定には不十分である理由を具体的に示す。
(V) のように **相対 gap よりさらに小さい誤差**を要求する必要は消えない。

## 8. 1999 trace formula と 2023 prolate motivation の追加照合

[Connes, math/9811068v1](https://arxiv.org/pdf/math/9811068v1),
§VII Theorem 4, 原稿 p.31、(12)–(13) で
\(P_\Lambda\) は \(|x|\le\Lambda\) cutoff、
\(\widehat P_\Lambda=\mathcal F P_\Lambda\mathcal F^{-1}\)、
\(R_\Lambda=\widehat P_\Lambda P_\Lambda\)。
有限 place set \(S\) と **固定した compact support の**
\(h\in\mathcal S(C_S)\) に対して
\[
\operatorname{Tr}(R_\Lambda U(h))-2h(1)\log'\Lambda
=\sum_{v\in S}\int_{k_v^\times}'\frac{h(u^{-1})}{|1-u|}\,d^\times u+o(1).
\tag{22}
\]
prime local terms・archimedean term と trace を結ぶ本物の定理である。
主値は選択した additive character と自己双対 Haar 規約で固定する。
ここで \(\Lambda\) は trace regularization cutoff で、上記 trial support \(\lambda\)
とは別変数。\(R_\Lambda\) は二つの射影の積であり、
一般に直交射影でも非負作用素でもない。

自己相関を h に代入すれば trace 側も元の test に二次的になるが、
それは正則化された **scaling operator の trace** である。
個々の \(h_\lambda\) に対する prolate concentration energy と
\(QW_\lambda(\mathcal E h_\lambda)\) の Rayleigh energy を同一視する式でも、
その差を gap より小さく抑える定理でもない。
さらに fixed-h の \(o(1)\) を、support・次数・norm が変化する
\(h=h_{\lambda,N}\) へ一様に流用できない。
したがって (22) は共通の算術的背景として有効だが、
本件の (15) や (V) が既に成立する根拠にはならない。

CC2023（Enseign. Math. 69, pp.93–148, DOI
[10.4171/LEM/1049](https://doi.org/10.4171/LEM/1049)）§3 pp.118–120 は、
radical と近似 simultaneous support の動機から
\(P_\lambda\widehat P_\lambda P_\lambda\) の prolate eigenfunctions を使う。
concentration の正作用素には通常の変分原理がある。しかし p.120 (3.4) は
有限 Fourier eigenvalue が約 \(\pm1\) であることによる parity 近似を使い、
算術和の成分を Gram–Schmidt して **比較候補**を定義する。
その候補が actual Weil の制約付き最小化問題の解である定理は、
確認した §3 にない。§3 の numerical agreement をその同定定理としない。

CCM2025 §8 の「cornerstone」としての1999公式の引用は、この背景と整合する。
同じ §8 が明記する ground/proxy comparison の missing step を、
引用一つで解決済みに読み替えない。

## 9. bounded decision

- 使用可能：有限 actual Weil matrix の Rayleigh / residual / Temple 評価、
  BV Fourier projection、(11) の weighted transform bound、
  前件が証明された場合の Γ/Mosco spectral convergence。
- 今回未取得：actual \(\rho-e_0\)、full spectral separation、
  \(\|r_{\lambda,N}\|\)、\(V_\lambda\)、およびそれらの (V) に届く
  cofinal quantitative bound。prolate concentration eigenvalue を Weil gap としない。
- 「common parent」を支持する同一 operator/form の恒等式は未取得。
  本稿は bridge に必要な評価対象を数値・解析の双方から検査可能にしただけ。
  一般定理の適用を RH 解決や新しい算術入力として数えない。
- actual limit kernel は安全な test 拡張上で Weil radical に入る。
  これは既知 summation-range framework と整合し、近零 energy から
  unique ground を選ぶ推論を支持しない。新規性は主張しない。

全論文・原著証明を独立再証明したとは主張せず、指定した formulation と
上記の短い直接導出に監査範囲を限定する。新しい RH 経路の完了なし。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/local_to_global/notes/spectral_approximants_and_exact_gap.md`](../../local_to_global/notes/spectral_approximants_and_exact_gap.md)
- [`research/notes/variational_closure.md`](../../notes/variational_closure.md)
