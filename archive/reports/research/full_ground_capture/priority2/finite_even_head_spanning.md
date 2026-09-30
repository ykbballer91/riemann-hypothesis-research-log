**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `research/full_ground_capture/priority2/finite_even_head_spanning.md`; original SHA-256: `b5af4c2a73f0388a401b99533191258ec5f47a4744ed71c71ce3b7b3a3dc60e5`. Publication formatting does not constitute a new mathematical audit.

---

# PRIORITY 2 — 有限偶 Fourier head の spanning と conditioning

2026-09-30。**STATUS: RIEMANN HYPOTHESIS OPEN.**

**FINITE EVEN HEAD SPANNING: PROVED.**
この判定の範囲は、各固定有限 head の有限 prefix による exact spanning と、
以下に明示した範囲の最小 prefix \(m=N\) による spanning である。
全 \((a,N)\) で最小次数を明示した、または一様に安定な lift を得た、という意味ではない。
Priority 3（growing-m）、Priority 4（full-ground capture）、parity は開始していない。
新規性を主張せず、既存 CY1 と通常の有限次元解析から得た auxiliary theorem として保存する。

## 結論となる定理

\(\widehat k(x)=\Xi(x)/4\)、\(\Xi(x)=\xi(1/2+ix)\)、
\(R_af=\mathbf1_{[-a,a]}f\) とする。
\(E_N^+\) は周波数 \(\pi n/a\)、\(0\le n\le N\) の偶 cosine head、
\(P_N\) は実際の区間 Fourier 射影。

1. **任意の固定 \(a>0,N\ge0\)** に対し、有限 \(m(a,N)\) が存在して
   \[
   \operatorname{span}\{P_NR_ak^{(2j)}:0\le j\le m(a,N)\}=E_N^+.
   \]
   これは密度だけの表現ではなく、有限次元の像における exact equality。
   ただしこの存在証明から明示的な \(m(a,N)\) は出ない。
2. **各固定 \(N\)** では、十分大きい \(a\) で最小本数 \(N+1\)、すなわち \(m=N\) が十分。
   さらに \(m=N\) が失敗し得る正の \(a\) の集合は有限。
   その集合の空性・個数・位置は未確定。\(N=0\) ならすべての \(a>0\) で \(m=0\)。
3. \(m=N\) の十分条件は、明示的に計算する ideal inverse bound \(L\) と
   sharp-tail bound \(\tau\) に対する **\(L\tau<1\)**。
   これにより \(\sigma_{\min}(B)\ge L^{-1}-\tau>0\)。
   実際に次の連続範囲を Arb 区間演算で認証した：
   \[
   a\in[1.499999,1.500001],\ N=m=4;
   \qquad a\in[1.999999,2.000001],\ N=m=6.
   \]
4. 固定 \(N=m\)、\(a\to\infty\) では raw 最小特異値は
   \(\Theta_N(a^{-2N-1/2})\)、raw 条件数は \(\Theta_N(a^{2N})\)。
   global physical Gram で正規化した最小特異値も同じ次数で小さくなる。
   **exact spanning は一様な良条件性を意味しない。**

証明は [algebraic_rank.md](notes/algebraic_rank.md) AR4–AR6、
[tail_conditioning.md](notes/tail_conditioning.md) TC1–TC5。

## A. \(\dim E_N^+\) は何か

\[
b_0(t)=\frac{\mathbf1_{[-a,a]}(t)}{\sqrt{2a}},\qquad
b_n(t)=\frac{(-1)^n}{\sqrt a}\cos(\pi nt/a)\mathbf1_{[-a,a]}(t),\quad1\le n\le N.
\]
これが既存 shifted Fourier convention に対応する正規直交基底。
**次元は \(N+1\)**。\(+n,-n\) を別方向として二重計上しない。

## B. Ideal no-tail model の最小 \(m\) は何か

\[
A_{nj}=D_n(-1)^j\omega_n^{2j},\quad
D_0=\frac{\Xi(0)}{4\sqrt{2a}},\quad
D_n=\frac{(-1)^n\Xi(\omega_n)}{4\sqrt a},\quad\omega_n=\pi n/a.
\]
従って \(A=D_\Xi VJ\)、\(V_{nj}=(\omega_n^2)^j\)、\(J_{jj}=(-1)^j\)。
非零対角行の個数を \(r\) とすると
\[
\boxed{\operatorname{rank}A=\min(m+1,r).}
\]
**grid hit がなければ最小 \(m=N\)**。\(m<N\) は列数不足。

ここで ideal は全線 Fourier **標本**であり、実際の \(P_N\) ではない。
実際の区間射影には \(P_N(1-R_a)=0\) が成り立つため、
tail 比較は別記号 \(S_{a,N}\) を用い
\(S_{a,N}R_af=S_{a,N}f-S_{a,N}(1-R_a)f\) と固定した。
詳細は TC0。

## C. Xi grid zeros は正確にいつ rank を落とすか

\(\Xi(\pi n/a)=0\) の各非負 index は ideal の一行を全列について零にする。
\(m\ge N\) なら欠損次元は hit 数に等しい。
一般の \(m\) では hit があっても \(r\ge m+1\) なら column rank は落ちない。

一つの多重零点が消すのは一行であり、零点重複度の分だけ追加方向を失うわけではない。
\(n=0\) は \(\Xi(0)>0\) なので hit しない。
\(a=\pi n/\gamma\) を実零点 \(\gamma\) から選べば hit は実際に起こり得る。
RH・零点単純性は使わない。confluent 補間への置換は異なる観測問題になる。

## D. Actual sharp support は rank を保存するか

\(B=A-E\) という exact perturbation があり、
\[
B_{nj}=-(\pi n/a)^2B_{n,j-1}+d_nk^{(2j-1)}(a),\quad
d_0=\sqrt{2/a},\quad d_n=2/\sqrt a\ (n\ge1).
\]
端点項があるため、ideal の grid-zero 行が actual でも零とは限らない。
対象は \(R_aD^{2j}k\) であり、端点 delta を含む \(D^{2j}R_ak\) ではない。

最小 prefix の rank 保存は TC7 が保証し、上記の区間で認証済み。
全 \(a,N\) について \(m=N\) を証明したわけではない。
しかし列数を十分増やせば **任意の固定 head の欠損は0**、という定理は成立する。

## E. 定量的 conditioning は何が得られたか

\(t_n=\omega_n^2\)、
\[
\beta_n=\prod_{r\ne n}\frac{1+t_r}{|t_n-t_r|},\qquad
L=\left[\sum_n(\beta_n/|D_n|)^2\right]^{1/2}
\]
とすると \(\sigma_{\min}(A)\ge L^{-1}\)。
\(\tau\) は theta の微分多項式と incomplete Gamma による明示上界。
\(L\tau<1\) なら \(\sigma_{\min}(B)\ge L^{-1}-\tau\)。
sharper な \(\|EA^{-1}\|<1\) も有効。

原典の inverse-Vandermonde norm、discrete orthogonal polynomial/Arnoldi、
Christoffel leverage を監査した。[文献・適用範囲](notes/conditioning_literature.md)。
基底変換は span を保持するが、head Gram による whitening は物理的な lift cost を消さない。

global physical Gram \(G_m\) を用いると、固定 head に対して
\[
B_mG_m^{-1}B_m^*=P_NR_a\Pi_{\mathcal R_m}R_aP_N\longrightarrow I_{E_N^+}
\]
が operator norm で成立する。十分多い列を使えば physical にも安定化できるという**固定 head の存在定理**。
必要次数の定量評価は未取得で、窓や \(N\) を変えるときの一様性はない。

数値診断では raw 条件数と physical 最小特異値が大きく異なる。
例えば \((a,N,m)=(1,4,4)\) は raw 条件数約 \(1.33\cdot10^7\)、physical 最小特異値約0.297。
一方 \((2,6,6)\) の physical 最小特異値は約 \(8.10\cdot10^{-5}\) で、
座標だけでは解消しない損失もある。[診断と再現手順](notes/diagnostics.md)。

## F. Actual finite even ground は derivative hierarchy 内にあるか

**固定有限 head の射影済み hierarchy という意味では yes。**
そこに住む任意の even ground vector \(v\) は、十分な有限 \(m\) に対し
\[
v=P_NR_a\sum_{j=0}^m c_j k^{(2j)}
\]
と exact に書ける。上記の認証範囲では \(m=N\) でよい。
これは ground を計算・選択した結論ではなく、head 全体の spanning の帰結。
\(v\) 自体が global radical に属する、global ground を捕捉した、
または係数 \(c_j\) が小さいとは主張していない。

## G. Hierarchical selector を使う前に何が残るか

\((a,N)\) に依存する ground を近似する際の必要次数・係数・physical lift cost と、
既存 fixed-m 階層定理の全定数の次数依存を同時に制御する必要がある。
さらにその近似を実際の Weil energy の誤差へ運ぶ評価が必要。
密度や固定 head の exact equality はこれらの代わりにならない。
これが Priority 3 以降の別の義務であり、今回は開始していない。

## 保存・監査

- 独立監査：[full_ground_finite_head_adversarial.md](../../../../audits/proofs/audits/full_ground_finite_head_adversarial.md)。
- 機械可読 state：[state.json](../../../../../data/source-records/research/full_ground_capture/priority2/state.json)。
- 既存318研究・監査ファイルの不変更検算：preservation_check.json (historical source identifier, not exported: `research/full_ground_capture/priority2/preservation_check.json`)。
- 旧 state、proof graph、公開用repositoryは編集・自動mergeしていない。

**FINITE EVEN HEAD SPANNING: PROVED — 固定有限 head と明示認証範囲に限定。**
**STATUS: RH OPEN.**
