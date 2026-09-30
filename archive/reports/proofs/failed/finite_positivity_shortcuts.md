**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/failed/finite_positivity_shortcuts.md` · Original SHA-256: `36984712e850a96b5b6976a2a233d12d5f2b67e5e4fe4f9f06580173f14023cb`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 有限正値性・スペクトル実現の偽短絡を破壊する

監査日: 2026-09-29。担当: DESTROYER / NUMERICAL FALSIFIER。

**ここで使う零点集合は人為的な有限モデルであり、ζ の零点ではない。RH の証明・反証はいずれも得ていない。** 以下は探索時に採用してはいけない推論への反例である。新規数学だという主張も行わない。

計算の再現: `python3 experiments/scripts/falsify_models.py`。
出力: `experiments/results/falsify_models.json`。標準ライブラリのみを使う。

## F01 — 有限圧縮の正値性から、収束条件なしで全定義域に延長する

**Hypothesis:** 有限座標圧縮がすべて PSD で、その定義域の和が Hilbert 空間で稠密なら、元の形式も PSD。

**Why plausible:** 連続な有界形式ならこの推論が成立するため、形式の連続性や form core を省略しやすい。

**Test performed:** `c00` を有限台の複素列全体とし、
\[
u=(2^{-1},2^{-2},\ldots)\in\ell^2\setminus c_{00},\qquad
D=c_{00}\oplus\mathbb C u
\]
とおく。分解の一意性から
\[
B(x+\alpha u,y+\beta u)=\sum_j x_j\overline{y_j}-\alpha\overline\beta,
\qquad Q(v)=B(v,v)
\]
は曖昧さのない Hermitian 形式である。

**Counterexample / failure:** 最初の N 座標への直交射影を \(P_N\) とすると、
\[
Q|_{\operatorname{span}(e_1,\ldots,e_N)}=\sum_{j=1}^N|x_j|^2\ge0
\]
で、有限 Gram 行列は全 N に対して恒等行列である。しかし
\[
Q(u)=-1,
\qquad Q(P_Nu)=\sum_{j=1}^N4^{-j}=\frac{1-4^{-N}}3\longrightarrow\frac13.
\]
したがって \(P_Nu\to u\) の Hilbert ノルム収束は、形式値の収束を保証しない。

**Can it be repaired?:** 各目的関数 f に対する近似列で \(Q(f_N)\to Q(f)\) を証明すればよい。十分条件の一例は、稠密性を示したものと同じ位相に関する形式の連続性である。適切に定義された閉形式の form core を使う修復もある。単なる Hilbert 空間での稠密性では足りない。

**Final status:** FALSE。形式収束なしの有限→無限延長を棄却。

### F01b — 「各固定サイズで最終的にPSD」の量化を交換する

\(A_n=I-2\langle\cdot,e_n\rangle e_n\) とすると、固定 k について \(n>k\) なら \(P_kA_nP_k=I_k\) である。それでも \(\langle A_ne_n,e_n\rangle=-1\) が全 n で成立する。

この例は「各固定圧縮で eventually PSD」から「ある段階以後、全体 PSD」への量化交換だけを反証する。**実際には \(A_n\to I\) strongly なので、この例を極限作用素の正値性への反例と呼ぶのは誤りである。** 固定ベクトルでの形式収束があり、すべてのベクトルの近似も正当なら極限の正値性は保存される。

## F02 — 基底または window を増やすと PSD が保存する

**Hypothesis:** 既存の有限 Gram 行列が PSD なら、基底の追加または window の拡張でも PSD。

**Why plausible:** 小さい行列が大きい行列の主小行列であることと、PSD の保存方向を取り違える。

**Test performed / counterexample:**
\[
M=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
最初の 1 次元圧縮は PSD だが、2 次元では \(e_2^*Me_2=-1\)。PSD は大行列から主小行列へは継承されるが、逆方向へは継承されない。

window パラメータを模した例として
\[
M_L=\begin{pmatrix}1&L\\L&1\end{pmatrix},\qquad L\ge0
\]
を取る。固有値は \(1-L,1+L\) なので \(M_0\succeq0\) だが \(M_2\) は不定値。\(v=(1,-1)\) について
\[
v^*M_Lv=2-2L,\qquad v^*(M_2-M_0)v=-4.
\]

**Can it be repaired?:** 真の window 形式を定義した上で増分の PSD を別途証明する必要がある。上記は window 理論そのものの反例ではなく、「拡張だから自動的にPSD」という一般推論の反例。増分 PSD を仮定に置き換えるだけでは核心は未解決のまま。

**Final status:** FALSE。

## F03 — 零点の虚部を自己共役作用素のスペクトルにするだけで臨界線性を得る

**Hypothesis:** 零点の虚部を重複度込みで自己共役作用素のスペクトルに実現すれば、零点の実部は 1/2。

**Why plausible:** 零点の虚部 \(\gamma\) と、臨界線からのずれを保持する複素数 \(-i(\rho-1/2)\) を混同する。

**Test performed / counterexample:**
\[
F(s)=\left((s-\tfrac12-\tfrac14)^2+1\right)
     \left((s-\tfrac12+\tfrac14)^2+1\right).
\]
これは整関数であり
\[
F(1-s)=F(s),\qquad F(\overline s)=\overline{F(s)}
\]
を満たす。四つの零点は
\[
\tfrac14\pm i,\qquad\tfrac34\pm i
\]
で、すべて臨界線から外れる。それでも虚部の多重集合は自己共役行列 \(\operatorname{diag}(-1,1,-1,1)\) のスペクトルそのものである。

**Can it be repaired?:** 必要なのは虚部 \(\gamma\) の実現ではなく、例えば全零点に対応する
\[
z_\rho=-i(\rho-\tfrac12)=\gamma-i(\beta-\tfrac12)
\]
自体を、自己共役作用素の実スペクトルに一致させる独立した恒等式である。その一致には実部・重複度・欠落零点・余剰スペクトルを含めた証明が必要。零点をあらかじめ並べて対角作用素を作るだけでは不足する。

**Final status:** FALSE。これは ζ/ξ の性質をすべて再現するモデルではない。

## F04 — 軸外の反射点対を Weil 型和に加えても正値

**Hypothesis:** 反射対称性または複素共役対称性があるため、各点対の Weil 型寄与は非負。

**Why plausible:**
\(F(z)\overline{F(\bar z)}\) を \(|F(z)|^2\) と読み違える。

**Test performed:** Fourier 規約を
\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx
\]
とする。\(z\notin\mathbb R\) での反射点対の寄与は
\[
\widehat f(z)\overline{\widehat f(\bar z)}+
\widehat f(\bar z)\overline{\widehat f(z)}
=2\Re\left(\widehat f(z)\overline{\widehat f(\bar z)}\right),
\]
一般には絶対値の二乗ではない。二つの値が 1 と −1 なら寄与は −2。

### 実際の \(C_c^\infty\) 関数による、全対称四重点への反例

任意の \(0<a<1/2\) と
\[
Z=\{1+ia,1-ia,-1+ia,-1-ia\}
\]
を取る。\(h\in C_c^\infty(\mathbb R)\) を偶・非負・非零とし、
\[
A=\int h(x)e^{ax}\,dx=\int h(x)e^{-ax}\,dx>0,
\quad g(x)=e^{-ix}h'(x),
\quad f=((iD+1)^2+a^2)g,
\quad D=d/dx
\]
とおく。微分作用素と乗法は compact support と smoothness を保つ。部分積分の境界項はゼロなので
\[
\widehat {iDg}(z)=z\widehat g(z),\qquad
\widehat g(z)=-i(z-1)\widehat h(z-1),
\]
従って
\[
\widehat f(z)=((z+1)^2+a^2)\widehat g(z).
\]
ここから厳密に
\[
\widehat f(-1\pm ia)=0,\qquad
\widehat f(1+ia)=4a(1+ia)A,\qquad
\widehat f(1-ia)=-4a(1-ia)A.
\]
よって四点の Weil 型形式は
\[
Q_Z(f)=\sum_{z\in Z}\widehat f(z)\overline{\widehat f(\bar z)}
=-32a^2(1-a^2)A^2<0.
\]
特に \(a=1/4\) で \(Q_Z(f)=-15A^2/8\)。この計算は任意の補間値を仮定せず、許容関数 \(f\in C_c^\infty\) を明示している。

具体的な bump として \(|x|<1\) で \(h(x)=\exp(-1/(1-x^2))\)、その外でゼロとする。偶性より
\[
A=\int h(x)\cosh(x/4)\,dx
\ge\int_{-1/2}^{1/2}e^{-4/3}\,dx=e^{-4/3}.
\]
従って数値積分に依存しない符号証明
\[
Q_Z(f)\le-\frac{15}{8}e^{-8/3}<0
\]
が得られる。

**Numerical check (EXPERIMENTAL EVIDENCE):** 70 桁の Decimal 演算による Simpson 積分で、2048 分割時に \(A\approx0.44619144450158421509\)、\(Q_Z(f)\approx-0.37328775964951932505\)。演算精度と積分誤差は別であり、これらの全桁の精度は保証していない。厳密な負符号は上記解析計算だけから従う。

**Can it be repaired?:** 軸上 \(z\in\mathbb R\) なら各項は絶対値二乗で非負。ζ の全零点についてこの事実を使うために軸上性を仮定すると、証明したい RH を仮定した循環論法になる。他の項との補償を使うなら、その補償を全テスト関数について独立に証明しなければならない。

**Final status:** FALSE。対称性だけによる正値性を棄却。有限集合の不定値性から ζ の完全な Weil 形式が不定値だとは推論しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/falsify_models.json`](../../../../artifacts/experiments/results/falsify_models.json)
- [`experiments/scripts/falsify_models.py`](../../../../artifacts/experiments/scripts/falsify_models.py)
