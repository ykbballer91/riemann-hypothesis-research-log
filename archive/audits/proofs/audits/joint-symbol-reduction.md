**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/joint-symbol-reduction.md` · Original SHA-256: `141c9c8ca4667969c15d65fae4cdfa28017c85d2c6e7a2886df873b605596613`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Joint symbol の tail floor — 一般還元、単調性、極限の量化

2026-09-29。担当: BUILDER。状態: **以下の条件付き還元と順序・極限定理は証明済み。全窓の正値性と RH は OPEN。** 新規性を主張しない。特定の interval certificate の成功はこのノートの前提にしない。

固定窓の既存規約と tail 定数は [fixed-window-reduction.md](fixed-window-reduction.md) に合わせる。[Zhu v2, §§3–5](https://arxiv.org/html/2608.24827v2) の定数 comb による還元を参考にするが、その数値認証や補助不等式を仮定しない。Weil 幾何側は [Connes–Consani–Moscovici v1, §3](https://arxiv.org/html/2511.22755v1)、digamma の漸近は [DLMF §5.11](https://dlmf.nist.gov/5.11) と照合した。以下の作用素比較と極限は直接証明する。

## J0. 空間、symbol、定義域

`a>0` を固定する。`H_a=L²([-a,a];C)` の元は実線へ零延長し、内積は第一変数に線形とする。

\[
 U_af(t)=(2\pi)^{-1/2}\int_{-a}^{a}f(x)e^{itx}dx,
 \qquad\|U_af\|_2=\|f\|_2.
\]

\[
 h(t)=\Re\psi(1/4+it/2)-\log\pi,\qquad
 P_a(t)=\sum_{\substack{n\ge2\\\log n<2a}}
       \frac{2\Lambda(n)}{\sqrt n}\cos(t\log n),
 \qquad\Psi_a=h-P_a.
\]

有限和の総係数を `A_a=Σ_(log n<2a)2Λ(n)/√n` とする。`Psi_a` は実数値・偶・連続で、

\[
 \Psi_a(t)=\log(2+|t|)+O_a(1)\quad(|t|\longrightarrow\infty).
                                                        \tag{J0.1}
\]

従って `Psi_a(t)→+∞`、`gamma_a:=inf_R Psi_a` は有限である。閉形式の定義域と pole を

\[
 \mathcal D_a=\left\{f\in H_a:
       \int_{\mathbb R}\log(2+|t|)|U_af(t)|^2dt<\infty\right\},
\]
\[
 c_a(x)=\cosh(x/2),\quad s_a(x)=\sinh(x/2),\qquad
 V_a=2|c_a\rangle\langle c_a|-2|s_a\rangle\langle s_a|
\]

とし、

\[
 Q_a(f)=\int_{\mathbb R}\Psi_a(t)|U_af(t)|^2dt
                         +\langle V_af,f\rangle       \tag{J0.2}
\]

を扱う。(J0.1) から十分大きい定数を加えた form norm は上の log ノルムと同値である。`V_a` は有界 rank 2、even sector で正、odd sector で負。以下で pole を落としたり符号を替えたりしない。

## J1. 一般の厳密な tail floor による還元

`T>0` と実数 `beta` が

\[
 \Psi_a(t)\ge\beta\qquad(|t|\ge T)                    \tag{J1.1}
\]

を満たすとき `(T,beta)` を admissible と呼ぶ。この条件のために `beta` が特定の公式で与えられる必要はない。`beta>0` もこの段階では不要である。

`B_Tf=U_af|_[-T,T]` とし、

\[
 R_{T,\beta}=\beta I+B_T^*M_{\Psi_a-\beta}B_T+V_a.
                                                        \tag{J1.2}
\]

これは `H_a` 全体上の有界自己共役作用素である。`||B_T||≤1`、`||B_T||_HS²=2aT/pi` なので、`R_(T,beta)−beta I` は compact。低周波 symbol `Psi_a−beta` は signed のまま保持する。

Plancherel より、全 `f∈D_a` について

\[
 Q_a(f)-\langle R_{T,\beta}f,f\rangle
 =\int_{|t|>T}(\Psi_a(t)-\beta)|U_af(t)|^2dt\ge0.
                                                        \tag{J1.3}
\]

これが必要な還元の全体であり、`beta` を得た方法は以後の論証に影響しない。ただし認証された `beta` と、head 組立・tail 評価で使う `beta` は同じ実数でなければならない。

**正の一様 gap に必要な条件。** `R_(T,beta)≥ell I` なら必ず `beta≥ell`。実際、ノルム 1 の `g∈C_c∞(-a,a)` に対し `g_N(x)=e^(-iNx)g(x)` と置くと、`g_N` は弱く 0 へ収束する。band 部分は `U_ag_N(t)=U_ag(t−N)` より消え、pole も消えるから

\[
 \langle R_{T,\beta}g_N,g_N\rangle\longrightarrow\beta.
                                                        \tag{J1.4}
\]

したがって `beta<0` の lower operator に有限 head の改善だけで全 mode 正値性を与えることはできない。`beta=0` でも正の一様 gap は不可能である。これは `Q_a` の符号についての反証ではない。

## J2. 有限区間の interval evaluation と無限 tail の接続

固定窓ノートで独立導出した digamma 下界は、全 `t>0` に対して

\[
 h(t)\ge\log(t/(2\pi))-1/t.
\]

従って増加関数

\[
 b_a(u)=\log(u/(2\pi))-1/u-A_a                      \tag{J2.1}
\]

は `[u,∞)` 全体での `Psi_a` の下界である。

`0<T<U` と、`[T,U]` を隙間なく覆う有限個の閉区間 `I_j` を取る。各区間について、丸め誤差・特殊関数の誤差を含む厳密な実数下界

\[
 L_j\le\inf_{t\in I_j}\Psi_a(t)
\]

を得たとする。そのとき

\[
 \boxed{\quad\beta\le\min\{b_a(U),L_1,\ldots,L_m\}
       \quad\Longrightarrow\quad(T,\beta)\text{ admissible}.\quad}
                                                        \tag{J2.2}
\]

証明は `[T,U]` と `[U,∞)` を分け、偶性で負周波数へ移すだけである。`b_a(U)` 自体も数値計算するなら、認証された下側端点を使用する。

この方法は `beta>b_a(T)` を許す。`[T,U]` では `h` と有限 prime comb の**同じ t における差**を評価し、遠方だけを (J2.1) で閉じるためである。`P_a(t)` が大きな `t` で総係数 `A_a` に再接近することと矛盾しない。その場所では `h(t)` も増えている。

実装上必要なのは次である。

- 格子点の最小値は `L_j` ではない。区間全体の enclosure、または認証された微分上界と格子誤差を要する。
- `Psi_a` の実区間評価は tail floor の認証であり、head の複素 ellipse 上の求積誤差評価を自動では与えない。両者を別に検証する。
- `P_a` の下界ではなく、`h−P_a` の下界が必要である。`−P_a` の符号を取り違えない。
- 証明書に用いる `beta` は明示した有理数などに固定すると再利用しやすい。最小値の近似値、ball の中点、求積ごとに変化する値を同一の厳密な floor と扱わない。
- 有限 `U` までの成功だけでは (J1.1) を証明していない。遠方の解析的下界または別の完全な tail 証明が必要である。

固定 `a` と候補 `beta` に対し、`b_a(U)→∞` なので遠方を閉じる有限 `U` の存在自体は無条件である。実際の `[T,U]` で `Psi_a≥beta` が真であることや、認証が実用的な費用で終わることは別問題である。

## J3. 切断幅と floor に関する正確な作用素順序

### J3.1 同じ切断幅

任意の実数 `beta_1,beta_2` に対し

\[
 R_{T,\beta_2}-R_{T,\beta_1}
       =(\beta_2-\beta_1)(I-B_T^*B_T).               \tag{J3.1}
\]

従って `beta_2≥beta_1` なら `R_(T,beta_2)≥R_(T,beta_1)`。この比較自体には admissibility は不要である。逆向きは (J1.4) と同じ高周波変調で否定できるので、固定 `T` ではこの条件は必要十分である。

### J3.2 入れ子の切断幅と admissible floors

`0<T_1≤T_2` とし、両 `(T_j,beta_j)` が admissible とする。そのとき

\[
 \boxed{R_{T_2,\beta_2}\succeq R_{T_1,\beta_1}
               \quad\Longleftrightarrow\quad\beta_2\ge\beta_1.}
                                                        \tag{J3.2}
\]

**十分性。** 任意の `f∈H_a` に対して、pole を相殺すると

\[
\begin{aligned}
 \langle(R_{T_2,\beta_2}-R_{T_1,\beta_1})f,f\rangle
  ={}&\int_{T_1<|t|\le T_2}(\Psi_a(t)-\beta_1)|U_af(t)|^2dt\\
    &+(\beta_2-\beta_1)\int_{|t|>T_2}|U_af(t)|^2dt.
\end{aligned}                                         \tag{J3.3}
\]

最初の項は古い floor の admissibility によって非負、次の項も仮定によって非負。

**必要性。** ノルム 1 の `g_N` を (J3.3) に代入する。有限 annulus 上の積分は 0 へ、外側の Fourier 質量は 1 へ収束する。従って差の極限は `beta_2−beta_1`。これが負なら有限の十分大きい `N` で実際の負方向が得られる。これは形式的な全実線 multiplier の議論ではなく、固定 support の test function を使った証明である。∎

admissibility を外した一般の二組については、`beta_2≥beta_1` と annulus 上の `Psi_a≥beta_1` は十分条件になる。symbol の点ごとの順序は圧縮後の作用素順序の必要条件とは一般には言えないため、(J3.2) の仮定を取り除かない。

**計算で得た floors が非単調な場合。** `T_1≤T_2≤…` で各認証値 `beta_j` が上下しても

\[
 \widehat\beta_j=\max_{k\le j}\beta_k                 \tag{J3.4}
\]

は `T_j` で有効な floor である。古い tail の部分集合に新しい tail が含まれるためである。この running maximum を使えば対応する作用素列は単調増加する。`a` 自体を変えた場合は `Psi_a` と prime 集合が変わるので、この再利用則を適用してはいけない。

**数値評価の単調性とは区別する。** 真の作用素の順序から、粗い tail/coupling 定数や得られる Schur 下界の単調性は従わない。`T` の増大に対して固定次数の Legendre tail 上界は増え得る。`beta` の増大に対して `sup_[−T,T]|Psi_a−beta|` も増え得る。認証アルゴリズムが返す余裕は、よりよい作用素に対して悪化する場合がある。

## J4. 最適 floor と微分を使わない形式極限

理論上の最適な定数 floor を

\[
 \beta_*(T)=\inf_{t\ge T}\Psi_a(t)
           =\inf_{|t|\ge T}\Psi_a(t)                 \tag{J4.1}
\]

とする。連続性と `Psi_a(t)→∞` より、各 `T>0` でこの infimum は有限な場所で達成される。さらに

\[
 T_1\le T_2\Longrightarrow\beta_*(T_1)\le\beta_*(T_2),
 \qquad b_a(T)\le\beta_*(T)\le\Psi_a(T),
 \qquad\beta_*(T)\longrightarrow\infty.             \tag{J4.2}
\]

最初の主張は集合の包含から従う。`beta_*'(T)` や最小化点の滑らかな移動は必要ない。最小化点が切り替わる可能性を無視して微分公式を使わない。`beta_*(T)` の定義は数値証明書ではなく、計算には (J2.2) のような認証された下界で足りる。

\[
 m_T(t)=
 \begin{cases}
   \Psi_a(t),& |t|\le T,\\
   \beta_*(T),& |t|>T.
 \end{cases}
\]

と置く。(J3.3) の点ごとの比較により `m_T` は `T` について増加し、各固定 `t` で最終的に `Psi_a(t)` に等しい。また `m_T≥gamma_a`。従って単調収束定理で

\[
 \boxed{\quad
  \sup_{T>0}\langle R_{T,\beta_*(T)}f,f\rangle
       =Q_a(f)\qquad(f\in\mathcal D_a).
       \quad}                                        \tag{J4.3}
\]

厳密には任意の増加列 `T_j→∞` に対して `(m_(T_j)−gamma_a)|U_af|²` に単調収束を適用し、`gamma_a||f||²+<V_af,f>` を戻せばよい。実数パラメータ全体の supremum も同じである。(J0.1) により `f∉D_a` の場合の supremum は `+∞`。従って extended closed form としても同じ結論になる。

これは各ベクトルについての form convergence であり、`Q_a` という非有界形式への operator norm convergence ではない。unit sphere 上の一様な誤差収束や最小値と極限の交換をこの証明から主張しない。

### J4.1 認証下界の列に十分な、より弱い仮定

`T_j→∞`、各 `(T_j,beta_j)` が admissible、さらにある実数 `B` に対して `beta_j≥B` とする。この場合は `beta_j` の単調性がなくても、全 `f∈D_a` について

\[
 \langle R_{T_j,\beta_j}f,f\rangle\longrightarrow Q_a(f).
                                                        \tag{J4.4}
\]

実際 (J1.3) の非負な差は

\[
 0\le Q_a(f)-\langle R_{T_j,\beta_j}f,f\rangle
 \le\int_{|t|>T_j}(\Psi_a(t)-B)_+|U_af(t)|^2dt
       \longrightarrow0.
\]

右辺は (J0.1) と `f∈D_a` により可積分関数の tail である。running maximum (J3.4) は自動的に下に有界であるため、この極限にも適合する。

下側の制御を全く置かない admissible floors では、極限は自動でない。例として `beta(T)=gamma_a−T²` とすると全 `T` で admissible だが、ノルム 1 の `f=(2a)^(-1/2)1_[−a,a]∈D_a` に対し

\[
 \int_{|t|>T}|U_af(t)|^2dt
 =\frac{2}{\pi a}\int_T^\infty\frac{\sin^2(at)}{t^2}dt
 =\frac1{\pi aT}+O_a(T^{-2}).                        \tag{J4.5}
\]

最後は `sin²=(1−cos(2at))/2` と部分積分から従う。(J1.3) の差は `T/(pi a)+O_a(1)+o(1)` となり、`<R_(T,beta(T))f,f>→−∞`。従って (J4.4) のような条件を省略できない。

## J5. 一般 beta を使う有限 head の十分条件

`Pi_d` を最初の `d` 個の Legendre modes、`E_d=I−Pi_d` とし、

\[
 M_{T,\beta}\ge\sup_{|t|\le T}|\Psi_a(t)-\beta|,
 \quad K_d\ge\|B_TE_d\|_{HS}^2,
 \quad J_d\ge\|E_dc_a\|^2+\|E_ds_a\|^2
\]

を厳密に得たとする。`K_d,J_d` は固定窓ノートの明示式をそのまま使用できる。これらは `beta` の取得法に依存しない。head について、丸め・求積・行列誤差込みで

\[
 \Pi_dR_{T,\beta}\Pi_d\succeq\mu\Pi_d
\]

を認証したなら、同じノートの証明から

\[
 \delta=\beta-M_{T,\beta}K_d-2J_d,
 \qquad\Gamma=M_{T,\beta}\sqrt{K_d}
                   +2\sqrt{\sinh a+a}\sqrt{J_d}     \tag{J5.1}
\]

が tail の下界と head–tail norm の上界になる。従って

\[
 \mu>0,\quad\delta>0,\quad\mu\delta>\Gamma^2          \tag{J5.2}
\]

なら全 `f∈D_a` に `Q_a(f)≥lambda||f||²`、

\[
 \lambda=\frac{\mu+\delta-
       \sqrt{(\mu-\delta)^2+4\Gamma^2}}2>0.
\]

あるいは `mu≥ell+Gamma` と `delta≥ell+Gamma` から `Q_a≥ell I` を得る。後者に使用する実代数だけが [RhAudit.two_block_lower_bound](../../../../artifacts/formal/lean/RhAudit.lean) に形式化されている。tail floor、特殊関数、積分、Arb certificate、無限次元への作用は形式化されていない。

同じ `T` でより高い admissible floor を認証した場合、(J3.1) によって既存の**完全な作用素下界**は保存される。有限 head 下界も保存される。ただし新しい `M_(T,beta)` を旧値のまま新しい Schur 計算へ流用するには、別途その上界の有効性を確認する必要がある。

## J6. 全窓への未証明の量化と RH 同値性

`a` ごとに大きい `T` を取って正の tail floor を得ること自体は、(J2.1) から無条件にできる。これだけでは低周波 head の符号を制御していない。`R_(T,beta)` の本当の負方向は、floor や tail 評価の精密化だけで必ず消えるとは限らない。

単調な下側近似の存在と (J4.3) も正値性の証明ではない。抽象的な反例として pole を 0 とし、`Theta(t)=log(2+t²)−C` を使う。同じ構成に `beta_Theta(T)=log(2+T²)−C` が適用される。任意のノルム 1 の滑らかな compact-support 関数 `g` に対し

\[
 C=1+\int\log(2+t^2)|U_ag(t)|^2dt
\]

と選べば、その極限形式は `q(g)=−1`。最適 floor が単調に無限大へ行き、lower operators が形式へ収束しても、極限の正性は従わない。これは実際の Weil symbol に対する反例ではない。

既知の Weil criterion による **RH 同値の命題**は

\[
 \forall a>0\;\forall f\in C_c^\infty((-a,a);\mathbb C),
                     \quad Q_a(f)\ge0.             \tag{J6.1: RH-equivalent}
\]

である。(J4.3) と組み合わせると、次も同じ内容の言い換えにすぎない。

\[
 \forall a>0\;\forall f\in C_c^\infty((-a,a);\mathbb C)
 \;\forall\varepsilon>0\;\exists T>0:\quad
 \langle R_{T,\beta_*(T)}f,f\rangle
                  \ge-\varepsilon\|f\|^2.          \tag{J6.2: RH-equivalent}
\]

`f=0` は自明。`f≠0` では supremum の定義と (J4.3) により両方向が従う。この量化を「十分大きい cutoff の存在」とだけ呼んで無条件の補題に置き換えない。特に `∀f∃T` と `∃T∀f` を交換していない。

次の**未証明の十分条件**も RH を導く。

> 全 `a>0` に対して、ある admissible `(T,beta)` と有限 `d` があり、認証された head と tail/coupling が (J5.2) を満たす。

本ノートはこれを証明せず、RH からこの特定の certificate schema が必ず成功するという逆向きも主張しない。任意有限個の窓での成功、最適 floor の存在、floor の計算費用改善のいずれからも、この全称量化は従わない。固定窓の解析的還元と、全窓で必要な新しい算術的・スペクトル的入力を分けて記録する。

<a id="j7-joint-symbol-scanner-の独立監査"></a>

## J7. Joint symbol scanner の独立監査

対象: [joint_symbol_certificate.py](../../../../artifacts/experiments/scripts/joint_symbol_certificate.py)、保存結果 [joint-symbol-tail-certificates.json](../../../../artifacts/experiments/results/joint-symbol-tail-certificates.json)。ソースの SHA-256 は JSON の `source_sha256` に保存されており、監査時のソースとの一致を確認した。**読み取り監査 PASS。** さらに root の関数を import しない別の短い検証コードで、整数因数分解による素数冪再列挙、区間の両端包含、全 leaf の下界、遠方 envelope を 224 bit で再計算し、全 **115,995 区間で PASS** を得た。保存された実行は python-flint 0.9.0 / 160 bit である。

版の記録: 独立した全 cover 再計算はソース SHA-256 `60e8fb0b6dc53adc0c2a57ac6474e5664a0db80099faeeb4f9bafc64eb3813bb` の時点で実施した。その後、`g` は正周波数で定義して `g(|t|)` を使用するという説明と、midpoint の失敗が `g` の floor への反例であって `Psi` の floor の反例とは限らないというエラー表示を修正した。計算式・区間 cover は変更していない。修正後の SHA-256 は `7cb0c430b247d1f9097ad3912a6159d5cc62545860f841fdca6f9a0946135012`。ソースと再生成 JSON の hash 一致、および leaf 総数 115,995 が保存されたことを再確認した。修正後に独立な全 leaf 再計算をもう一度行ったとは主張しない。

### J7.1 実際に認証した命題

実装は digamma を直接区間評価せず、

\[
 g_a(t)=\log(t/(2\pi))-1/t-P_a(t)\le\Psi_a(t)
 \qquad(t>0)
\]

を用いる。次の有限 cover 全体で `g_a>1/5` を認証し、`[U,∞)` は (J2.1) によって閉じた。偶性を使うのは `Psi_a` と `g_a(|t|)` であり、負の `t` に実対数 `log t` を代入しない。

| `a` | `T` | `U` | cover の leaf 数 | 結論 |
|---:|---:|---:|---:|---|
| `0.8` | `111` | `148` | `39` | `Psi_a(t)>1/5` for `|t|≥T` |
| `1` | `1552` | `2674` | `1153` | 同上 |
| `1.19` | `5549` | `9074` | `3580` | 同上 |
| `1.2` | `21231` | `38520` | `17444` | 同上 |
| `1.4` | `132510` | `225986` | `93779` | 同上 |

これらは J1 の admissible pairs `(T,1/5)` を与える。`beta_*(T)` の正確な値や最小可能な `T` を求めたという意味ではない。

### J7.2 区間・列挙・無限 tail

`arb(mid,rad)` の第 2 引数は上端でなく半径である。[python-flint 0.9.0 の公式仕様](https://python-flint.readthedocs.io/en/latest/arb.html) と実 API を確認した。本コードは中心 `(2k+1)/2^(d+1)`、半径 `1/2^(d+1)` を渡すので、`[k/2^d,(k+1)/2^d]` を覆う。今回の整数サイズと精度では中心・半径はともに exact dyadic である。半径が一般に上向き丸めされても enclosure は狭くならない。再検証では各 leaf の両端が ball に含まれることも確認した。

生成時は左の子、右の子の順に区間を二分するため重なりのない順序付き cover が得られる。保存された `[depth,count]` の run を読む側は、`Fraction` で現在位置を更新して、`T` から `U` までの連続 cover を再構成する。幅の総和だけを根拠に隙間がないと推測しているわけではない。両端を含む区間評価なので境界点も覆われる。

素数冪列挙の float は候補の整数 `bound` を作るためだけに使用され、`log(bound)>2a` を Arb で確認する。その下の全整数の素数判定は整数の試し割り、各素数からの冪は整数積である。`n<bound` の全素数冪について `log n<2a` または `log n>2a` を認証するため、判定不明を除外扱いにしない。係数は `2log p/sqrt(p^k)` であり、`2log(p^k)/sqrt(p^k)` ではない。境界で等号なら現実装は assert で停止するが、それは偽の成功ではない。独立列挙は `n<20` の各整数を因数分解し、`log20>2a` を Arb で確認する別手順で行い、5 件の保存 prime-power lists と一致した。

`U` も float からの候補値であるが、`log(U/(2pi))−1/U−A_a>1/5` を Arb で再確認している。後者の envelope は全 `t>0` で増加するので、無限 tail 全体を保証する。float による候補が不適切なら停止し、誤って認証を通過する経路ではない。

### J7.3 信頼範囲と追加で従うこと

ball の厳密な大小比較 `value>beta` を成功条件にしている。表示した最小 margin や elapsed time は補助情報であり、証明の代わりではない。検証器は全区間を再評価する。Python の `assert` を検証機構として使うため、`python -O` や assert を無効化する実行は本認証手順に含まれない。信頼基盤には Python の整数・有理数演算、python-flint/Arb の包含演算、実行環境、および解析的な digamma 下界が含まれる。Lean で scanner を形式化した結果ではない。

各行について、有界な lower operator `R_(T,1/5)` の構成が正当化される。さらに任意の厳密な有限上界

\[
 C\ge\sup_{|t|\le T}(1/5-\Psi_a(t))_+
\]

を用いれば

\[
 Q_a(f)\ge\tfrac15\|f\|^2
       -C\|B_Tf\|^2-2|\langle f,s_a\rangle|^2.       \tag{J7.1}
\]

右辺の負の摂動は正の trace-class 作用素 `K=C B_T*B_T+2|s_a><s_a|` で、

\[
 \operatorname{Tr}K=C\frac{2aT}{\pi}+2(\sinh a-a).
\]

従って `Q_a` が負定値となる部分空間の最大次元は高々

\[
 \left\lfloor5\left(C\frac{2aT}{\pi}+2(\sinh a-a)\right)\right\rfloor.
                                                        \tag{J7.2}
\]

実際、負定値な `m` 次元部分空間の正規直交基底を (J7.1) に代入すれば `m/5<Tr K`。この粗い次元上界は有限低周波部分に残る問題を示すだけで、負方向が存在しないとは言わない。head の PSD、pole と head–tail coupling、全 `Q_W` の正値性、RH は今回の scanner によって認証されていない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/joint-symbol-tail-certificates.json`](../../../../artifacts/experiments/results/joint-symbol-tail-certificates.json)
- [`experiments/scripts/joint_symbol_certificate.py`](../../../../artifacts/experiments/scripts/joint_symbol_certificate.py)
- [`formal/lean/RhAudit.lean`](../../../../artifacts/formal/lean/RhAudit.lean)
- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
