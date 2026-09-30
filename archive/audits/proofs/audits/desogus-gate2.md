**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/desogus-gate2.md` · Original SHA-256: `2475de80dcc9d09632201c6ad495a32afdbc0c8184701555e6cd00b7e84d01f2`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus 2609.20367 — Gate II の最小 cut と独立監査

2026-09-29。担当 BUILDER。状態 **UNVERIFIED EXTERNAL PROOF CLAIM**。
主対象は [arXiv:2609.20367v2](https://arxiv.org/html/2609.20367v2)（2026-09-20）。取得物・SHA-256 は provenance（原資料参照・公開版未収録: `research/desogus_source_provenance.json`） に固定する。v1（2026-09-17）の同じ箇所とも照合した。以下は RH の反証でも、実際の Weil 形式の負方向の発見でもない。

**最小の未閉鎖部分は、正しい局所 scalar 不等式から、実際の全 Weil 形式の同一 Schur 残差へ戻す同定である。** とくに v2 Lemma 8.4 の二 arm 平方完成は `2D` を差し引くが、最終集計は `Q−D` のみを非負残差として使用する。正の pivot を持つ有理 3×3 模型で、この二つは置換できない。さらに Corollary 6.29 には一般 one-defect block と実 operator の明示的な同定、および使用する scalar pivot の正値性の証明が見つからなかった。

## DG1. 我々の barrier との対応

```text
OUR BARRIER:
旧 block A>0 と新しい diagonal の局所余裕だけでは、
Schur 形式 D−B* A^{-1}B の符号を制御できない。

WHY GENERIC METHOD FAILS:
coupling の debit が旧 gap の逆数を含み、局所延長は
有限半径の最初の gap closure で止まりうる。
同じ vector 上の恒等式でも、正負の項を省略してよいわけではない。

DESOGUS CLAIMED REPAIR:
共通 source cut、inherited response の同じ metric への配置、
fold の scalar cancellation を結び、算術 budget を最終 Schur 形式に移す。

EXACT THEOREM / LEMMA:
v2 Theorem 6.53; Lemmas 6.28, 6.58, 6.61, 8.1, 8.2, 8.4;
Theorem 8.5。依存の最小 choke point は 6.29→8.4→8.5。

ASSUMPTIONS:
真の閉形式、共通 domain、旧 block の可逆な正 gap、
同じ source metric、正の scalar pivot、同一 primal contribution の完全な項台帳。

IS THE REPAIR ACTUALLY SUFFICIENT?:
印刷された式のままでは YES と判定できない。
二 arm の 2D と一 arm の D の差、および exact identification が未解消。

INDEPENDENTLY REPRODUCED?:
局所 common-cut 模型と scalar algebra: YES。
それらからの actual Weil operator の Theorem 8.5: NO。

STATUS:
PROOF-CRITICAL GAP。局所の記号・係数を直す案はあるが、
完全な operator bridge の修復は未完。
```

既存の独立 barrier は [support-propagation-reduction.md](support-propagation-reduction.md)、[flow-renormalization](support-propagation-flow-renormalization.md)、[adversarial audit](support-propagation-adversarial.md)。一般的反例だけを理由に ζ 固有の修復可能性を排除しない。

## DG2. 共通切断の局所模型は独立に成立する

論文の `b` と同じ明示的な one-cell form を、ここでは新しく定義して直接調べる。

\[
b[u]=\frac14\iint_{(0,1)^2}\frac{|u(x)-u(y)|^2}{|x-y|}\,dxdy
       -\frac12\int_0^1\log(x(1-x))|u(x)|^2dx.
\]

定義域は右辺が有限な `L²(0,1)` の元。無限なら不等式は拡張実数の意味で成立する。`L=log2`、`β0=L+1/2` として

\[
L_0=\beta_0I-\tfrac12|1\rangle\langle1|,\qquad b=l_0+r,
\]

\[
r[u]=\frac14\iint\left(\frac1{|x-y|}-1\right)|u(x)-u(y)|^2
 +\int\left[-\tfrac12\log(x(1-x))-\log2\right]|u(x)|^2\ge0. \tag{DG2.1}
\]

係数はともに非負。`|I_j|=ε` の disjoint slots を取り、その合併を `S`、`s=|S|=Mε≤1` とする。共通 complement 上の `L0` block は `≥L I`。rank-one inverse を直接計算すると、source 側の short は

\[
L_{0,S}^{\rm short}
 =\beta_0I_S-\frac{\beta_0}{2L+s}|1_S\rangle\langle1_S|.   \tag{DG2.2}
\]

各 slot の正規化定数基底では `β0I−q uu*`、`q=β0 ε/(2L+Mε)`。`qM≤1/2` は `s≤1` と同値。slot 内平均零空間には `β0 I` が残る。これは v2 Lemma 6.48 の模型を独立に再導出したもの。

### 残差の独立な capacity 計算

slot `I_j=(a_j,a_j+ε)` における `u` の平均零部分を `f_{j,0}` とする。

1. 内部の residual difference energy は `≥(1−ε)||f_{j,0}||²/2`。
2. complement の点 `y` について `∫_{I_j}|u(x)−u(y)|²dx≥||f_{j,0}||²`。外側 kernel の最小値を積分してよい。
3. 二つの slot の左端距離が `Dε` なら、pair の residual energy は
   `[(D+1)^{-1}−ε](||f_{j,0}||²+||f_{l,0}||²)/2` 以上。
4. 外側の one-slot charge との差は、各 incident pair ごとに
   `δ_D/2`、`δ_D=log(1+1/D)−1/(D+1)>0`。

内部・左右 complement・endpoint potential を加えると slot の位置 `a_j` が消え、pair deficit を除く係数は `log(1/(2ε))` になる。`δ_D` は減少し、

\[
\sum_{j\ge1}\delta_j=1-\gamma_E<0.422785=:d_0.
\]

したがって

\[
r[u]\ge\left(\log\frac1{2\varepsilon}-d_0\right)
                   \sum_j\|f_{j,0}\|^2.                    \tag{DG2.3}
\]

右辺は source data だけに依存するので、**一つの共通 complement の infimum** を取る際にそのまま残る。DG2.2 と合わせ、ground と transverse を同時に下から抑える block lower bound が得られる。ここでは同じ予算を二回使用していない。

**判定:** v2 Theorem 6.53 の **明示された one-cell 模型**は独立再導出 `YES / VALIDATED`。ただしこれを、prime terms・polar term・既存 old-core short を含む実際の全 operator の source metric と同一視するには別の恒等式が必要。局所模型の成立だけでその bridge を `YES` にしない。

## DG3. Inherited response の恒等式が与える範囲

一般の一変数形式

\[
p|a|^2-2\Re(\bar a\omega)+R,\qquad p>0
\]

の minimizer は `a=ω/p`、寄与は `−p|a|²`。`0<θ<1`、`a=θX` と書けば

\[
-p\theta^2|X|^2=-p|X|^2+(1-\theta^2)p|X|^2.                \tag{DG3.1}
\]

これは v2 Lemma 8.1 の中核を独立に検算した正しい恒等式である。正の comparator surplus は発生するが、同時に負の comparator reference term がある。例えば `p=1,θ=1/2,X=2` なら左辺 `−1`、右辺は `−4+3`。`+3` だけを新しい余裕として使用することはできない。

Lemma 8.2 の Young 不等式も、**その表示左辺に対して**は成立する。`A=(1−θ²)Π` を `3A/5+2A/5` に分ければ、mixed forcing と aligned forcing を別々に支払える。`(5/3)c_*<189/250` の係数関係も整合する。

ここで未検証なのは局所平方完成ではない。Theorem 8.5 が actual total parent loss をその表示左辺だけで集計するとき、DG3.1 の負の reference term を、別の同一 primal contribution が本当に支払っているかである。その支払先は Lemma 8.4 の fold bridge と同時に特定する必要がある。`P_ex≥Π0` という lower bound だけでは負項 `−P_ex|X|²` の lower bound にはならない。

**判定:** stationarity / homogeneity / Young は `YES`。actual full-form への予算配置は `NO / GAP`。恒等式自体が偽だとは判定しない。

## DG4. Scalar cancellation は pivot の符号を証明しない

v2 Lemma 6.28 は一般の multiplication-minus-rank-one block を扱い、scalar debit には `Π_phys>0` を明示的に要する。Corollary 6.29 の harmonic row identity だけではこの符号は得られない。

この点は有理 2×2 模型で完結する。両区間長を 1、両 multiplication coefficient を 1 とし

\[
M_\beta=
\begin{pmatrix}1-\beta&-\beta\\-\beta&1-\beta\end{pmatrix},
\qquad \beta=\tfrac34.
\]

旧 block は `1/4>0`。新 coordinate を 1 に固定した旧 minimizer は `x=(3,1)` であり

\[
M_\beta x=(0,-2),\qquad
\operatorname{Schur}_{\rm old}M_\beta=-2.
\]

この場合 `I=J=1`、`γ^c=3`、`Π_phys=−2`、`Q=−2`。形式的に `D=|−2|²/(−2)=−2` と書けば `Q−D=0` である。しかし `D` は正の Schur debit ではなく、その scalar variable での infimum は `−∞`。分子が pivot と同じ因子を含むことは、pivot が正であることを意味しない。

本例は Lemma 6.28 の **条件付き恒等式への反例ではない**。その条件を外して old positivity と harmonicity だけから全 positivity を出す推論への反例である。zero pivot で商が連続に延びても、負側に横切らないことは保証されない。

版固定した v2 TeX で `a_{k,±},β_k` の導入は一般模型の Lemma 6.28。Corollary 6.29 は実 row をこの模型と同定すると述べるが、これらの係数を実 localized operator から算出する式、および使用時の `Π_phys>0` の証明はこの監査では見つからなかった。root の独立全文検索も同じ結果。

**必要な修復:** 実閉形式上の明示 unitary / domain / 残存 block を与え、`Π_phys>0` を帰納結論に依存せず証明する。単に全 step の正 pivot を追加仮定するだけなら、欠けた伝播内容を仮定へ移したにすぎない。

## DG5. 正の pivot でも残る一 arm / 二 arm の不一致

### DG5.1 一般の二 arm Schur 計算

`P>0`、`bx` が target に属するとし、形式

\[
\Phi(x,t_+,t_-)=q[x]+B|\gamma|^2
 +\langle Pt_+,t_+\rangle+\langle Pt_-,t_-\rangle
 +2\Re\langle bx,t_+\rangle+2\Re\langle bx,t_-\rangle
\]

を取る。有限次元なら domain の問題はなく、直接平方完成して

\[
\inf_{t_+,t_-}\Phi
 =q[x]+B|\gamma|^2-2\|P^{-1/2}bx\|^2.                      \tag{DG5.1}
\]

`t_s=(t_++t_-)/sqrt2`、`t_a=(t_+−t_-)/sqrt2` に回転しても、coupling が `sqrt2 b` となるため同じ `2` が残る。

これは v2 Lemma 8.4 の式 (207)–(212) 自身とも一致する。一方、その statement の MASTER-P3b と Theorem 8.5 の final assembly は `Q−D` を残差として使用し、同じ `D=||P^{-1/2}bx||²` に対するもう一つの `D` の支払いが明示されていない。

### DG5.2 正の one-defect pivot と完全に整合する反証模型

DG4 の係数を今度は `β=1/4` にする。旧 block は `3/4>0`、`x_L=1/3,x_R=1` は旧 harmonic vector である。

\[
I=J=1,\qquad \gamma^c=\tfrac13,
\qquad \Pi_{\rm phys}=Q=D=\tfrac23>0,
\qquad Q-D=0.                                               \tag{DG5.2}
\]

この positive pivot を二 arm 表示にそのまま入れ、`P=b=2/3` とする。ground/arm/arm の行列は

\[
M=\frac23
\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]

arms の block は `(2/3)I>0` だが、その exact Schur complement は

\[
\frac23-2\frac{(2/3)^2}{2/3}=-\frac23<0.                    \tag{DG5.3}
\]

実際 `(1,−1,−1)` の二次形式は `−2/3`。この模型では `Q−D=0` という主張は真でも、二 arm 残差 `Q−2D≥0` は偽である。したがって DG4 の符号条件を追加するだけでは最終の欠落 debit は直らない。

これは実 Weil operator にこの数値行列が出現するという主張ではない。**同一の印刷された変数・同一の primal form として各式を使用する場合、その一般代数が接続しない**ことを示す。著者の意図が別 stage の `Q` なら、stage の違いを数式で定義し直す必要がある。

### DG5.3 修復可能な局所 bookkeeping の選択肢

次のいずれかを実 operator から証明できれば、係数 `2` 自体は処理できる。

1. 各 arm の coupling が実は `b/sqrt2` であり、合計 debit が `D`。
2. 計算時点で既に一 arm を除去していて、残存 primal form にあるのは一 arm のみ。
3. `Q_pre=Q_cut+D` という別 stage の関係があり、`Q_pre−2D=Q_cut−D`。
4. 二 arm をそのまま保ち、実際に `Q−2D` を支える追加の独立 budget を証明する。

印刷式のまま、`Q_pre=Q_cut` と扱いながら `2D` を `D` に置換することはできない。上記のどれが実 Weil geometry と一致するかは未確認であり、修復済みとは報告しない。

**Normalization による修復試行は、それだけでは失敗する。** unitary な symmetric/antisymmetric 座標なら coupling が `sqrt2 b` となる。非等長な表示 `t_+=t_-=t` でも diagonal は `2P`、coupling は `2b` なので debit は `4b*(2P)^{-1}b=2b*P^{-1}b`。odd channel と逆符号の二 coupling でも同じ係数が残る。選択肢1の `b/sqrt2` を `P,Q` を固定したまま入れることは operator 自体の変更であり、無害な正規化とは呼べない。実際の算術的変換がその係数を与えることの証明が必要。

**分類:** 一 arm / 二 arm の局所表記は `REPAIRABLE` な候補がある。しかし現行の 8.4→8.5 の証明経路では `PROOF-CRITICAL GAP`。完全証明の修復は `UNKNOWN`。論文の全定理が偽だという `FATAL` 判定には拡張しない。

## DG6. Domain と split-unitary の追加注意

非有界閉形式の short は `inf_{x:(x,y)∈D(q)}q[x,y]` と定義しなければならない。旧 block が単に positive-injective なだけでは inverse が有界とは限らない。固定 support の Weil 形式では compact resolvent を別途証明すれば、strict positivity から正 gap が得られる。この部分は既存の log-Fourier domain の議論で技術的に整備可能であり、DG5 の有限次元問題を解消するものではない。

また quadratic form の unitary transport と、特定 one-defect model への exact identification は異なる。前者が正しくても、後者の multiplication coefficients、rank、domain、残存 forcing を計算せずに同一視してはいけない。

Möbius については、`φ_k(rcrit)=ucrit` という異なる二つの切断点をつなぐ関係が使われている。同一 `L²(0,1)` 上の一つの projection に対する commutation と読むと一般に偽である。正しい式は input/output の二 projection を使った intertwining でありうる。本件は異座標の記号整理で修復可能なため、独立の致命的 gap とは分類しない。

## DG7. 版差、再現範囲、次の最小課題

v1 HTML と v2 TeX / HTML の Lemmas 8.1, 8.4、および fold remainder を比較した。二 arm の `−2D` と final `Q−D` は **両版に存在する**。v2 は「同じ scalar debit を一回だけ引く」説明を追加しているが、二 arm の明示式は維持されている。本監査の指摘は v1 のみの省略を v2 へ転用したものではない。

有理反例は Python の `fractions.Fraction` で独立評価し、次を再現した。

| 検査 | Exact 結果 |
|---|---:|
| `β=3/4` の旧 block | `1/4` |
| 同じ模型の新 Schur pivot | `−2` |
| `β=1/4` の旧 block | `3/4` |
| positive-pivot 模型の `Q=D` | `2/3` |
| 二 arm の exact residual | `−2/3` |

これは有限算術の完全再現であり、arXiv の大規模 certificate の独立検証を代用しない。prime-power sweep、Arb base certificate、analytic arithmetic tail はこのファイルの担当外であり、`INDEPENDENTLY-VERIFIED=YES` にしていない。

最短の修復課題は、新しい finite-window 計算ではない。**実際の同一 harmonic vector に対し、source / inherited-reference / target / fold の全項を一つの block matrix または閉形式恒等式で書き、消去前後の `Q_pre,Q_cut,D_one,D_total` を別記号にすること。** これが得られれば DG5 の四選択肢を決定し、残る正値性 budget を再評価できる。現時点では主証明 graph の unknown node は閉じていない。

## DG8. 補足 V2 の静的検索 — 修復情報は検出せず

2026-09-29、`literature/source_cache/desogus-The_Three_Gates_Supplementary_V2.zip` を **実行・import・compile せず**検査した。

- ZIP SHA-256: `c46356c7961dba2651a22000564652779f6153eb8ecfcd8250208dd8a95106d1`。
- 全213 archive members の名前・サイズを確認。うち166 text members、合計1,482,284 bytes を復号して静的検索した。
- 検索対象は P2/P3、two-arm / one-arm、post-short、physical pivot、inherited/reference debit、harmonic graph、common cut、FOLD-FORCING、係数 `a_{k,±}` 等。
- binary `npz` は `Y=7` 数値行列、三つの nested archive は Gate I の raw box data という名前・配置である。この検索では binary 内容や nested payload の数学的検証はしていない。

`independent_checks/gateII/GATEII_FULL_COMB_SCALARIZATION_AUDIT_2026-09-19.md`（SHA-256 `a1ef1779f2d59614eb6a023e4dfc2f4b9c2a525b404e544c5e96548016072448`）以外に、P3 の行列や pivot を証明する追加文書は見つからなかった。この audit の対象は full prime comb の特定の pointwise scalarization の有無であり、全定理の独立証明を主張していない。P3 部分も本文の exact identification を前提に評価していて、欠落する係数式や `D` と `2D` の追加相殺式は記載しない。

`additional_cross_checks/root_lift_constants_verify.py` を全文静読した。内容は `delta_*,beta,d_*,rho_aff,epsilon_7,gamma_7,q_F` 等の scalar comparison で、operator identity は本文へ委ねられている。`true_affine_routing_verify.py`、`master/README.md`、`Y7_base/rh_fifth_cell_certificate_summary.md` も scope を確認した。これらは枝の算術・有限 scalar sweep・単一 base endpoint の資料であり、全 step の actual folded row を定義しない。

**結果:** 補足の未読証明による DG4–DG5 の即時修復は `NOT FOUND`。これは archive 内の全数値結果の否定ではない。graph の未閉鎖 status は変更しない。

## DG9. 次の一つの precise repair lemma

修復を曖昧な「同じ vector だから相殺する」説明から切り離すため、以下の **actual cut / one-arm reconciliation identity** 一つを次の課題にする。これは未証明の候補であり、成立を仮定して RH を得た扱いにはしない。

### 入力を actual operator で固定する

算術 step `k→k+1` における実際の odd Weil 形式を、物理的 old/shell 分割で

\[
\mathcal A_{k+1}=\begin{pmatrix}A_k&G_k\\G_k^*&D_k^{\rm sh}\end{pmatrix},
\qquad A_k\ge c_k I>0,
\qquad T_k=D_k^{\rm sh}-G_k^*A_k^{-1}G_k                 \tag{DG9.1}
\]

とする。これらは pole と全 prime-power term を含むもとの operator から定める。domain は既存の compact-support log-Fourier domain。

次に本文で指定された transport と common-complement/source shorts を **lower model に置換する前に**実行する。最後の二 arm を残した actual reduced form を `M_k^act` とする。すでに short した inherited-source の負寄与は、その ground-ground block `R_k^act` に必ず含める。`R_k^act` は desired positivity や comparator difference を使って再定義してはいけない。

### 候補修復補題 RL-k（未証明）

残存する全非 arm 座標の空間を `E_k` とする。actual の二 arm diagonal/coupling が、本当に `P_k>0` と同じ `b_k:E_k→H_arm` であることを確認し、

\[
d_k=b_k^*P_k^{-1}b_k
\]

を actual block から定義する。その上で、本文の one-defect cut model `C_k^fold` を **実 kernel から明示的に計算した**係数・domain によって独立に構成し、次の一つの閉形式恒等式を証明する。

\[
\boxed{
M_k^{\rm act}
=
\begin{pmatrix}
C_k^{\rm fold}+d_k&b_k^*&b_k^*\\
b_k&P_k&0\\
b_k&0&P_k
\end{pmatrix}.
}                                                            \tag{RL-k}
\]

つまり証明すべき非自明な成分は `R_k^act=C_k^fold+d_k` である。他の retained transverse coordinates があれば `E_k` に含め、対角だけでなく全 mixed entry に関して等式を示す。`C_k^fold:=R_k^act−d_k` と **定義して済ませることは禁止**し、本文が使用する multiplication-minus-rank-one model との一致を kernel/pairing から示す必要がある。

この式が成立すれば、二 arm を short した結果は正しく

\[
\operatorname{Short}_{\rm arms}M_k^{\rm act}
=C_k^{\rm fold}-d_k.                                      \tag{DG9.2}
\]

従って `Q_pre=Q_cut+D` という DG5.3 の選択肢3が実 operator で実現され、二 arm の `2D` を一 arm の `D` と誤認せずに、残存 `Q_cut−D` を評価できる。すでに消去した負の reference debit は `R_k^act` に含まれているため、同じ exact identity の検査でその行方も判定できる。

**この候補の意味と限界。** RL-k が恒等式として得られても、`P_k` の正値性・domain、独立に定義した `C_k^fold−d_k` の下界は監査しなければならない。逆に計算で actual diagonal が `C_k^fold` のままと判明すれば、RL-k は偽で、現行の一 arm cancellation による修復は終了する。その場合は本当に `2d_k` を支払う新しい算術的 lower bound が必要になる。

補足 ZIP には、RL-k の左辺を全 `k` で組み立てる式・右辺の `a_{k,±},β_k` の actual coefficient dictionary・追加 `+d_k` の支払元は見つからなかった。**新規仮定として採用せず、未証明の算術的 operator identity に課題を限定する。** 大規模 scalar certificate の再実行だけではこの等式は検証できない。

### 独立監査の受領

DESTROYER は原文の v2 (207)–(212) と Theorem 8.5 を読み取り、`2D` と `D` の相違、DG4 の負 pivot 模型、DG5.2 の正 pivot 模型を独立に確認した。実 Weil への反例でないという scope にも同意。記録は同担当の Gate III 監査の短い付録に保存予定との返答を受領した。RL-k 自体を証明・監査 PASS にしたものではない。

## DG10. Prop. 5.3 → Cor. 6.29 の full-form 再構築

### DG10.1 半密度の変数変換で残る canonical な対角項

本文の変換 `U_A` を、単なる off-diagonal kernel ではなく差分形式に直接代入する。`A>0`、`ell<r`、`I=(e^{A ell},e^{Ar})`、`phi(u)=e^{Au}`、`J(u)=A e^{Au}` とし、

\[
q_I[f]=\frac14\iint_{I^2}\frac{|f(x)-f(y)|^2}{|x-y|}\,dxdy,
\qquad g(u)=\sqrt{J(u)}f(\phi(u)).
\]

最初は `f∈C_c∞(I)`。置換すると正確に

\[
q_I[U_A^{-1}g]
=\frac14\iint_{(\ell,r)^2}K_A(u,v)|g(u)-g(v)|^2\,dudv
 +\int_\ell^r v_A(u)|g(u)|^2du,                           \tag{DG10.1}
\]

\[
K_A(u,v)=\frac{\sqrt{J(u)J(v)}}{|\phi(u)-\phi(v)|}
 =\frac{Ae^{-A|u-v|/2}}{1-e^{-A|u-v|}},
\]

\[
v_A(u)=\frac12\int_\ell^rK_A(u,v)
       \left(\sqrt{\frac{J(v)}{J(u)}}-1\right)dv
 =\log\frac{(1+e^{A(r-u)/2})(1+e^{-A(u-\ell)/2})}{4}.       \tag{DG10.2}
\]

導出は、変換後の integrand の diagonal coefficient が
`J(v)|g(u)|²+J(u)|g(v)|²`、mixed coefficient が
`−2sqrt(J(u)J(v)) Re(g(u)bar g(v))` であることから従う。差分形式の kernel を `K_A` とすると、diagonal の比 `sqrt(J(v)/J(u))` が残る。原点近傍の singularity はこの比と 1 の差で相殺され、DG10.2 の積分は絶対収束する。

最後の積分は `v<u` と `v>u` に分ければ、それぞれ
`−A/(1+e^{A|u-v|/2})` と `A/(1+e^{-A|u-v|/2})` の初等積分になる。有限 `ell,r` では `v_A` は有界なので、等式は適切な閉形式 domain へ延長できる。

**核だけを置換して `v_A=0` とする推論への smooth-core 反例。** `A=1,ell=0,r=1` とする。`u≥3/4` では

\[
(1+e^{(1-u)/2})(1+e^{-u/2})
\le(1+e^{1/8})(1+e^{-3/8})
<\frac{15}{7}\frac{19}{11}<4.
\]

ここで `e^{1/8}<8/7`、`e^{-3/8}<8/11` を使った。従って `v_A(u)<0`。任意の非零 `g∈C_c∞((3/4,7/8))` について、DG10.1 と kernel-only の差は厳密に負である。

数値 sanity check でも `v_1(3/4)=−0.1055720616628815...` を DG10.2 と、左右に分けた積分の Simpson 評価で独立比較し、通常浮動小数点で差 `3×10^{-17}` 未満だった。証明は上の有理不等式であり、この数値は interval certificate ではない。

### DG10.2 Full form を運ぶ際に追跡すべき項

既知の potential `V0` は `V0∘phi` に移り、DG10.2 の補正と合わせた新 potential は `V0(phi(u))+v_A(u)` である。元の bounded integral kernel `K0(x,y)` は `sqrt(J(u)J(v))K0(phi(u),phi(v))` に移る。rank-one vector `s` は `U_A s` に移る。prime-power operator は `U_A S_n U_A*` に移る。この辞書に任意 counterterm を導入する余地はない。

Carleman kernel についても同様で、差分/和形式のどちらを使うかを指定した上で、`K_A` を対応する transported kernel に置き換えた同型の対角補正が出る。二つの off-diagonal kernels の half-sum が簡約することだけでは、これらの diagonal corrections の相殺は証明されない。

したがって Prop. 5.3 を **抽象的に元の完全形式の unitary image を定義する命題**と読めば、それ自体は問題ない。しかし「その image が、後で使う明示 one-cell / one-defect form と等しい」という追加結論は、各 potential と gamma term を DG10.1 の辞書で照合しなければ得られない。本文は `c_A` を Cauchy–Carleman realization と呼ぶが、その元の完全形式と target の killing coefficient をこの精度で指定していない。ゆえに kernel identity だけでは RL-k の係数を復元できなかった。

### DG10.3 下界の one-defect model を exact と扱うことはできない

DG2 の実 one-cell form `b` と lower model `L0` は異なる。定数関数で

\[
b[1]=1,\qquad \langle1,L_01\rangle=\log2,
\qquad b[1]-\langle1,L_01\rangle=1-\log2>0.                \tag{DG10.3}
\]

さらに、disjoint supports の mixed kernel は `−1/(2|x-y|)`。multiplication-minus-constant-rank-one の mixed kernel は定数 `−beta` である。例えば `x=(1/8,1/4)`、`y=(3/4,7/8)` で前者の絶対値の 2×2 kernel matrix は

\[
\begin{pmatrix}4/5&2/3\\1&4/5\end{pmatrix},\qquad
\det=-\frac2{75}\ne0.                                    \tag{DG10.4}
\]

disjoint smooth bumps を各点へ局在させれば、同じ違いを test-space pairing で検査できる。従って、元の one-cell form をそのまま保持している段階では exact rank-one model ではない。後続の本当の compression / Schur short が特殊な one-defect form を生む可能性は排除しないが、その計算が別に必要である。

Corollary 6.29 の「complementary coordinates を固定し forcing 側へ移す」操作は、retained-retained block 自体を変更しない。仮に実 block が `L0+R` なら、`R` の retained-retained 部分を forcing に移して `L0 x=g` と書くと `g` は未知の `x` に依存する。これは固定 forcing の Schur 最小化と同じ問題ではなく、`R` の二次エネルギーを消してよい理由にもならない。

最小の scalar 検査は `q(a)=2a²−2a` である。真の minimizer は `a=1/2`、値は `−1/2`。`L0=1,R=1` と分け、残差を右辺へ移すと row equation は `a=g(a):=1−a` となる。これを固定 forcing と誤認して `−|g|²/L0` だけ残せば `−1/4` になり、実際の負費用を `1/4` 過小評価する。正しい式には `−Ra²=−1/4` も残る。したがって `g=Apre x` を成立させるだけでは、same-vector energy の同定は完了しない。

### DG10.4 この段階での停止判定

full difference form の canonical transport 自体は DG10.1–2 により再構築できた。しかし本文と補足からは、その結果を Corollary 6.29 の `M_{a_{k,-}}⊕M_{a_{k,+}}−beta_k|1><1|` に一致させる係数・projection・domain の辞書が得られなかった。**RL-k 右辺の `C_fold` は、actual Weil operator によって一意に指定された対象としてまだ実装・検証可能な形で定義されていない。**

従ってこの一段の修復は `NOT REPAIRED` で停止する。Prop. 5.3 の抽象 unitary 性を否定するのでなく、off-diagonal identity から exact folded one-defect operator への未証明の昇格を止める。任意 counterterm や `C_fold:=R_act−d` は採用しない。graph の critical unknown は変わらない。

最小の追加補題は DG9 の RL-k をそのまま **実 kernel の完全な transport 辞書付きで証明すること**である。具体的な未指定費用は、(i) DG10.2 の killing term と元の potential の合計、(ii) source/inherited short 後の retained-retained 残差、(iii) 二 arm debit のうち final assembly で使われていないもう一つの `d_k`。これらを actual block `R_act` に保持したうえで、独立に定義した `C_fold` に対する `R_act=C_fold+d_k` を示す必要がある。現状、その算術的係数式はなく、補題を立てたこと自体を証明上の前進とは数えない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/support-propagation-adversarial.md`](support-propagation-adversarial.md)
- [`proofs/audits/support-propagation-flow-renormalization.md`](support-propagation-flow-renormalization.md)
- [`proofs/audits/support-propagation-reduction.md`](support-propagation-reduction.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/desogus-The_Three_Gates_Supplementary_V2.zip` — SOURCE REFERENCE NOT INCLUDED
- `research/desogus_source_provenance.json` — SOURCE REFERENCE NOT INCLUDED
