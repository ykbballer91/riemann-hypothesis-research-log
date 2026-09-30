**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/spiral-scale-reduction.md` · Original SHA-256: `613455a5ede8e381d96a1f4e6ff508ae7568809ebd8e24274eb1467ed71e6468`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Scale-flow の保存則と global Weil 形式 — 独立還元監査

2026-09-29。担当: BUILDER。**RH は未証明。新規性の主張はしない。**
対象は新添付の spiral / scale-flow 探索のうち、dilation の domain、global Weil 形式、零点の不定内積表示、Connes / Burnol との接続である。固定窓の数値拡大と停止済み imbalance route は再開しない。

**結論。** 全 test space の Weil 形式は最初から存在し、対数座標の平行移動で厳密に保存される。しかし、その保存則は off-line quartet の増幅・減衰と両立する。自然な保存形式を正の零点ノルムに置き換える独立な根拠は得られなかった。従って「保存則だけから radial drift を禁止する」候補は **STOPPED**。以下の正しい恒等式は監査資料として保存し、RH の新入力には採用しない。

## SS1. 規約と既存監査の再利用

内積は第1変数線形。加法 test space と Fourier 規約は

\[
\mathcal D=C_c^\infty(\mathbb R;\mathbb C),\qquad
F_f(z)=\int_{\mathbb R}f(r)e^{izr}\,dr,\qquad
z_\rho=\frac{\rho-1/2}{i}.
\]

非自明零点は多重度を含む。`rho=1/2+alpha+it` なら `z_rho=t−i alpha`。変数 `s−1/2` と `z_rho` は回転が異なる。

既知入力と収束は [Weil 規約](../../../reports/proofs/lemmas/weil_conventions.md)、[固定 support の連続性](../../../reports/proofs/lemmas/finite_to_infinite.md) に固定する。dilation の一般重みと対称性の監査は [center_scale.md](../../../reports/research/notes/center_scale.md)。global `L²` 非閉包性は [variational_closure.md §2](../../../reports/research/notes/variational_closure.md) を再利用する。本ノートで再証明済みの結果を新規の突破と数えない。

## SS2. Dilation の正規化、生成子、状態の種類

### SS2.1 正確な作用素命題

`H_x=L²(R_+,dx)` とし

\[
(U_u v)(x)=e^{u/2}v(e^u x),\qquad
(Vv)(r)=e^{r/2}v(e^r).
\]

`x=e^r` の変数変換により `V:H_x→L²(R,dr)` は unitary であり

\[
VU_uV^{-1}g(r)=g(r+u).                                      \tag{SS2.1}
\]

したがって `U_u` は強連続 unitary group。規約 `U_u=e^{iuH}` の下で

\[
H=V^{-1}(-i\partial_r)V
  =-i\left(x\frac{d}{dx}+\frac12\right),\qquad
D(H)=V^{-1}H^1(\mathbb R).                                  \tag{SS2.2}
\]

右辺の微分は弱微分として解釈する。`C_c∞(R_+)` は core で、この上の対称微分作用素は本質的自己共役。実際、`V` はこの core を `C_c∞(R)` に写し、Fourier 変換

\[
\widehat g(\lambda)=(2\pi)^{-1/2}\int g(r)e^{-i\lambda r}dr
\]

は `−i∂_r` を domain `{b:lambda b∈L²}` の実乗算作用素に写す。従って `H` のスペクトルは `R`、純絶対連続で、`L²` 固有ベクトルはない。裸の dilation は離散 ζ 零点スペクトルを選ばない。

`1/2` は測度 `dx` の Jacobian の半分である。一般の `L²(x^{2β−1}dx)` なら `e^{βu}v(e^ux)`、生成子 `−i(x∂_x+β)` となり、すべて同じ実直線の translation 模型に unitary 同値。測度を指定する前から `1/2` が唯一の尺度指数だとはいえない。

### SS2.2 純回転の形式解は Hilbert 固有ベクトルではない

\[
v_s(x)=x^{-s},\quad s=1/2+\alpha+it,
\qquad Vv_s(r)=e^{-\alpha r-itr}.
\]

形式計算では

\[
U_uv_s=e^{-\alpha u-itu}v_s,\qquad
Hv_s=(-t+i\alpha)v_s=-z_s v_s.                            \tag{SS2.3}
\]

しかし `∫_0∞|v_s(x)|²dx=∫_0∞x^{-1−2alpha}dx` は **すべての実 alpha で発散**。`alpha=0` の `x^{-1/2+it}` は実固有値 `t` の generalized eigenfunction であり、通常の Hilbert 固有ベクトルではない。`alpha≠0` の対数座標の指数関数は `D'(R)` には属するが `S'(R)` には属さない。一方の端で指数増大するためである。

従って「`||U_uv_s||=||v_s||` を用いて alpha=0」とする計算は、未定義のノルムを使用する。零点を何らかの resonance と呼ぶだけでもこの domain 障害は解消しない。

### SS2.3 双方向有界性が実際に禁止するもの

**補題。** Banach 空間上の群 `G_u` が `sup_{u∈R}||G_u||<∞` を満たし、非零の空間内ベクトル `v` が全実 `u` で `G_uv=e^{(-alpha−it)u}v` を満たすなら `alpha=0`。

証明は `e^{-alpha u}||v||≤C||v||` に `u→±∞` を適用するだけである。unitary 群ならもちろん成立する。片方向の contraction は一方向の減衰を許し、可逆性 `G_{−u}=G_u^{-1}` だけでは有界性を与えない。

この補題を ζ に適用するには、**全非自明零点に対する、非零で空間内にある固有状態の同定**が必要。SS2.3 自体にはその算術的同定がない。全零点の形式解を有界群の真の固有状態に格上げする仮説は RH を含意し、独立な既知入力としては採用できない。

### SS2.4 自己共役作用素でも継続 resolvent に非実 pole がありうる

`K=M_lambda` を `L²(R,dλ)` 上の自己共役乗算作用素とし、`kappa>0` に対して

\[
v(\lambda)=\left(\frac{\kappa}{\pi(\lambda^2+\kappa^2)}\right)^{1/2},
\qquad \|v\|=1.
\]

Cauchy 核の初等積分または留数計算により

\[
\langle e^{iuK}v,v\rangle=e^{-\kappa|u|},\qquad
m(z)=\langle(K-z)^{-1}v,v\rangle
=\begin{cases}
-1/(z+i\kappa),&\Im z>0,\\
-1/(z-i\kappa),&\Im z<0.
\end{cases}                                                \tag{SS2.4}
\]

上半平面の式を meromorphic に継続すると `−i kappa` に pole がある。しかしこれは下半平面における **本来の resolvent** ではない。`K` の実スペクトル・全群の norm 保存とは矛盾しない。ここでは scalar resolvent の継続 pole という限定された resonance 模型であり、ζ との同定は主張しない。`K` は SS2.1 の裸の dilation と unitary 同値なので、unitarity のみから継続 pole を排除できないことを直接示す。

## SS3. 最初から存在する global object と exact restriction

### SS3.1 Test-space Weil 分布

\[
W(h)=\sum_\rho F_h(z_\rho),\qquad
\widetilde g(r)=\overline{g(-r)},\qquad
Q(f,g)=W(f*\widetilde g)
=\sum_\rho F_f(z_\rho)\overline{F_g(\bar z_\rho)}.           \tag{SS3.1}
\]

これは RH を仮定せずに定義される。既知の `|Im zρ|<1/2`、零点計数 `N(T)=O(T log T)` と、固定 support `[-L,L]` における部分積分評価

\[
|F_f(z)|\le C_{L,m}\max_{j\le m}\|f^{(j)}\|_\infty
                 (1+|\Re z|)^{-m}\qquad(|\Im z|\le1/2)
                                                               \tag{SS3.2}
\]

から `m=2` で両和の絶対収束が従う。`W` は通常の LF test-space 位相の連続分布である。`Q` は Hermitian。零点和を臨界線上の絶対平方和に変えるには RH が必要。

`D_L={f∈D:supp f⊂[-L,L]}`、包含 `i_L:D_L→D` に対し

\[
Q_L(f,g)=Q(i_Lf,i_Lg).                                    \tag{SS3.3}
\]

これは厳密な global restriction 関係であり、全窓の正値性を仮定しない。ただし `i_L^*Qi_L` はここでは **形式・分布としての記法**であって、単一の閉 Hilbert 作用素の圧縮を証明したものではない。

### SS3.2 鋭い support projection の domain

`P_L f=1_{[-L,L]}f` は一般の smooth test function を smooth に保たないため、`P_L:D→D` と書いてはいけない。代わりに各固定窓の閉形式 domain

\[
V_L=\left\{f\in L^2([-L,L]):
 \int\log(2+|t|)|(2\pi)^{-1/2}F_f(t)|^2dt<\infty\right\}
\]

を使う。[support-propagation-reduction.md](support-propagation-reduction.md) で、鋭い区間切断がこの log-Fourier domain を保存すること、および `q_M|_{V_L}=q_L` (`L<M`) を監査済み。従って `V_comp=∪_L V_L` 上には整合的な global 形式がある。任意の `f,g∈V_comp` について `q(P_Lf,P_Lg)=q_L(P_Lf,P_Lg)` は意味を持つ。

ここから全実線 `L²` 上の閉形式や非負自己共役作用素は得られない。また SS3.1 の絶対収束した零点和を、証明なしにすべての `V_comp` 元へ拡張しない。

### SS3.3 Global な通常 L² 上の正の閉因子分解は不能

[既存非閉包性監査 §2](../../../reports/research/notes/variational_closure.md) の結論は、`D⊂D(B)⊂L²(R)` で closable な Hilbert 空間値線形作用素 `B` が `Q(f)=||Bf||²` を全 test function で満たすことはない、というもの。

要点だけを再掲する。その仮定は Weil criterion により RH を含意する。従って実零点高度 `gamma0` を固定し、`∫psi=1` の smooth compact bump について

\[
f_R(r)=R^{-1}\psi(r/R)e^{-i\gamma_0r}
\]

を取れる。`||f_R||²=R^{-1}||psi||²→0` だが零点評価ベクトルは `gamma0` の多重度分だけ 1、それ以外 0 の非零ベクトルに `ℓ²` 収束する。よって `Q(f_R−f_S)→0` かつ `Q(f_R)→m_0>0`。これは `B` の closability に反する。

この障害は RH の否定ではない。抽象的 Q-Hilbert 完備化、異なる始域の位相、固定窓の閉形式は排除しない。全実線の通常の `L²` ノルムをそのまま使う余分な要求を排除する。

## SS4. 正確な A*JA 表示と保存則

### SS4.1 不定内積の factorization

零点の多重集合をラベル付きで扱い、`sigma rho=1−bar rho` が多重度ラベルを保つ involution となるようにする。`z_{sigma rho}=bar zρ`。

\[
\mathcal K=\ell^2(Z),\quad
(Af)_\rho=F_f(z_\rho),\quad
(Jc)_\rho=c_{\sigma\rho}.
\]

SS3.2 から `Af∈K`、`A:D→K` は LF 位相で連続な線形写像。`J=J*=J^{-1}` は有界であり

\[
\boxed{\ Q(f,g)=\langle Af,JAg\rangle_{\mathcal K}\ }.       \tag{SS4.1}
\]

従って `A*JA` という表示は **test-space からその反双対への形式として**厳密である。ここでの star はこの pairing の意味であり、global `L²` 上の Hilbert adjoint と同一視しない。`A` は零点を使って定義した解析写像であり、零点を独立に構成する算術的作用素を発見したという主張でもない。

RH なら `J=I`。off-line conjugate pair 上では

\[
J_{\rm pair}=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

となり、固有値は `+1,−1`。`P_±=(I±J)/2` により

\[
Q(f)=\|P_+Af\|^2-\|P_-Af\|^2.                             \tag{SS4.2}
\]

正部分のみを採用すると元の Weil 形式を変更する。`Ran A` 上で負部分が正部分を上回らない、すなわち全 `f` で `Q(f)≥0` と置くことは **Weil criterion による RH 同値条件**であり、新しい補題の仮定に隠さない。

### SS4.2 自然な global 保存則は無条件に成立する

`T_a f(r)=f(r−a)` とすると `F_{T_af}(z)=e^{iaz}F_f(z)`。従って各項で

\[
e^{iaz}\overline{e^{ia\bar z}}=1
\]

であり、絶対収束した和により

\[
\boxed{\ Q(T_af,T_ag)=Q(f,g)\quad(a\in\mathbb R)\ }.        \tag{SS4.3}
\]

同じことは `(T_af)*~(T_ag)=f*~g` からも直接従う。算術側の pole・archimedean・素数冪項を全部含む保存則であり、項の削除や正則化はない。SS2.1 より multiplicative test functions 上の `Q(Vv,Vw)` は **physical dilation `U_u` で保存**される。

ただし translation は中心を動かすので、これは固定された `[-L,L]` 内の一径数群でも、窓幅 `L` の増加に関する保存則でもない。

### SS4.3 Off-line drift は J 保存と両立する

零点座標で

\[
(D_ac)_\rho=e^{iaz_\rho}c_\rho
\]

と置く。`||D_a||≤e^{|a|/2}` なので、これは `K` 上の強連続可逆群である。各固定 `a` での dominated convergence が強連続性を与える。さらに

\[
AT_a=D_aA,\qquad D_a^*JD_a=J.                             \tag{SS4.4}
\]

従って SS4.3 は零点座標の **J-unitarity** そのものである。`z=gamma+i eta` と `bar z` の pair では

\[
D_a=e^{ia\gamma}\begin{pmatrix}e^{-a\eta}&0\\0&e^{a\eta}\end{pmatrix},
\qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.             \tag{SS4.5}
\]

`eta≠0` でも SS4.4 は成立する。共通 phase を除いた実行列は determinant 1、標準交代形式 `Omega=((0,1),(-1,0))` を保存し、swap により逆向き時間と共役になる。すなわち determinant・symplectic form・不定 quadratic flux・可逆性を同時に保っても drift は残る。

全 quartet `±z,±bar z` に拡張すると `z→−z` の置換により時間反転も実現できる。この対称性を加えても正の Hilbert norm の保存にはならない。

## SS5. Mandatory falsification と RH 同値性の境界

### SS5.1 対称 quartet は real-even test 上でも負形式を許す

`gamma eta≠0` とし、synthetic 零点集合を `Z_0={z,bar z,−z,−bar z}`、`z=gamma+i eta` とする。対応する finite 形式を SS3.1 と同じ式で定める。

`F(z)=F(−z)=i`、`F(bar z)=F(−bar z)=−i` なら

\[
Q_{Z_0}(f)=i\,\overline{-i}+(-i)\,\overline i
           +i\,\overline{-i}+(-i)\,\overline i=-4.           \tag{SS5.1}
\]

この値指定は real-even smooth test functions とも整合する。実偶 bump `psi` の台を十分小さくして `F_psi(z)≠0` とする。`Im(z²)=2 gamma eta≠0` なので、実係数の一次多項式 `P(w)=b_0+b_1w` を `P(z²)F_psi(z)=i` となるように一意に選べる。`f=P(−∂_r²)psi` は実偶 smooth compact 関数で、`F_f(w)=P(w²)F_psi(w)`。所要の四値が得られる。

従って functional equation 型の even 性・実型性・全 translation 保存は、relevant real-even subspace の positivity を強制しない。これは実 ζ の反例ではなく、これらの構造だけを使った推論の反例である。実 ζ の prime-power arithmetic がこの synthetic 集合と一致するとは主張しない。

### SS5.2 正の零点ノルムによる stability は正確に RH と同値

次の命題を候補とする。

\[
\text{(B)}\qquad
\forall f\in\mathcal D,\quad
\sup_{a\in\mathbb R}\|AT_af\|_{\ell^2}<\infty.             \tag{SS5.2}
\]

**命題。`(B) ⇔ RH`。** RH なら SS4.4 の `D_a` は Hilbert-unitary なので成立。逆に off-line `z_0` があれば、`F_f(z_0)≠0` となる test function が存在する。例えば `f(r)=e^{-iz_0r}psi(r)`、`∫psi=1` でよい。その座標の絶対値は `e^{-a Im z_0}` なので一方向で無限大になる。よって (B) は成立しない。∎

この安定性は未知情報を短く表すが、独立な追加構造ではない。通常の physical `L²` norm の保存から (B) は出ない。`A` が通常の global `L²` 上の有界写像であるという bridge はなく、正の closable factorization に強化すれば SS3.3 の障害がある。

同様に、全零点を非零の真の状態として表す正定値 metric と群の unitarity を仮定すれば drift を禁止できるが、その metric と同定こそ未証明である。

### SS5.3 数値反証の役割と再現値

小さな finite 模型だけを用いる。`eta=1/4,a=2` として SS4.5 の phase を除いた `E=diag(e^{-1/2},e^{1/2})`、`v=(1,−1)` を取る。

\[
\langle v,Jv\rangle=\langle Ev,JEv\rangle=-2,
\quad\det E=1,\quad E^T\Omega E=\Omega,
\quad\|Ev\|^2=2\cosh1=3.08616126963049\ldots>2.           \tag{SS5.3}
\]

quartet の値ベクトル `(i,−i,i,−i)` の J-energy は `−4`。SS2.4 では `kappa=1/4,u=2` で相関は `e^{-1/2}=0.606530659712633...` だが Hilbert norm は常に 1。これらの数値は反例の位置確認だけであり、証明は SS2.4 と SS4.5 の厳密式にある。固定窓の head や tail certificate は計算していない。

## SS6. Connes / Burnol の一次文献との接続

### SS6.1 Connes: spectral state と resonance の区別が既に本質

[Connes, arXiv:math/9811068v1](https://arxiv.org/pdf/math/9811068v1) §III、Theorem 1 を版本固定で確認した。同節の重み付き Hilbert 空間には `delta>1` が必要で、尺度群は unitary ではなく対数尺度の polynomial bound を持つ。定理の固有スペクトルは **既に臨界線上にある零点**に対応し、多重度にも `delta` による切断がある。一般化を「全零点が unitary 群の固有状態」と読み替えることはできない。

同論文は off-critical zero が存在する場合を resonance として区別し、global trace formula の未完部分と RH の同値性を明示する。これは SS2.4 の domain 区別と同方向だが、同論文の算術的構成を本ノートが再現したわけではない。全 zero が空間内の真の固有状態になる、という追加前提は同文献からは得られない。

### SS6.2 Burnol: Hilbert 評価ベクトルの存在・完全性と固有値実現は別

[Burnol, arXiv:math/0203120v6](https://arxiv.org/pdf/math/0203120v6) §§1–3 を確認した。右 Mellin 変換 `∫v(x)x^{-s}dx` は `L²(dx)` と `Re s=1/2` 上の `d Im(s)/(2pi)` を対応させる。Sonine 空間では completed Mellin transform の複素点評価が連続である（Theorem 2.1）。拡張空間 `L_a` 上の零点評価系は、`a≤1` で極小、`a≥1` で完全となる（Theorem 3.1）。

これらは off-line を除外した後だけの記述ではない。しかし **複素点の評価ベクトルであることは、その点が自己共役生成子の実固有値であることを意味しない**。Sonine 条件・Mellin 完成因子・support 条件を落として裸の dilation に置き換えることもできない。この既知の Hilbert 構造から SS5.2 の一様な全軌道安定性を導く bridge は本探索では得られなかった。

より詳しい既存文献監査は [accumulation_spectrum.md §§3,5](../../../reports/research/notes/accumulation_spectrum.md)。本節は当該一次文献の上記箇所の確認であり、Connes / Burnol 全論文の全証明の再監査ではない。

## SS7. 採用判定と停止点

| 候補 | 厳密な結果 | RH との論理関係・判定 |
|---|---|---|
| 裸の dilation の正の norm 保存 | SS2.1–2、domain も明示 | 無条件に正しいが全零点の状態同定なし。規約として保持 |
| 双方向有界な真の固有状態 | SS2.3 は drift を禁止 | 全 ζ 零点がその状態という未証明入力が必要。証明ルートとして停止 |
| resonance も unitary なら実である | SS2.4 が反例 | 棄却 |
| 一つの global Weil object の窓制限 | SS3.1–3 は厳密 | 無条件。positivity は増えない |
| global `A*JA` と scale conservation | SS4.1、SS4.3–4 は厳密 | 不定符号のまま成立。off-line 禁止にはならない |
| self-dual relevant subspace の positivity | SS5.1 が一般推論を反証 | 実 Weil で全 test positivity と置けば RH 同値 |
| 正の零点評価 norm の全軌道安定性 | SS5.2 | RH 同値。「圧縮に成功しただけ」と分類 |
| global 通常 `L²` の閉 `B*B` 実現 | SS3.3 | 余分な domain 条件が成立不能 |

自然な保存量として `Q` 自体は得られた。しかしユーザーの成功条件にある「独立な保存機構によって off-line が数学的に不可能」を達成していない。**新しい RH 入力・主証明 graph の新規 node としては不採用。** domain と恒等式を保存し、この保存則単独の候補を停止する。

独立 DESTROYER 監査はこのファイルを読み取りで依頼し、その返答を受領後に判定範囲を追記する。Lean 形式化済みの主張は本ファイルにはない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/support-propagation-reduction.md`](support-propagation-reduction.md)
- [`proofs/lemmas/finite_to_infinite.md`](../../../reports/proofs/lemmas/finite_to_infinite.md)
- [`proofs/lemmas/weil_conventions.md`](../../../reports/proofs/lemmas/weil_conventions.md)
- [`research/notes/accumulation_spectrum.md`](../../../reports/research/notes/accumulation_spectrum.md)
- [`research/notes/center_scale.md`](../../../reports/research/notes/center_scale.md)
- [`research/notes/variational_closure.md`](../../../reports/research/notes/variational_closure.md)
