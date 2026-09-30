**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/higher_order_gamma_selection.md` · Original SHA-256: `d8c937dbd2d49c3da5e167b29fcbf6429675241d2acdac8dffecf42f5121b29a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Higher-order selection：support-only fixed \(m\) の決着

2026-09-30。RH OPEN。既存ファイルは不変更。
本担当は support-only に限る。Fourier resolution、prime-event flow、Sonine は他担当の独立 gate。

## 1. 得られた定理

\(f_j=k^{(2j)}\)、\(\widehat k=\Xi/4\)、\(Y=\pi e^{2a}\)、
\(R_a=1_{[-a,a]}\) とする。
任意の固定有限 \(m\) について、実際の Weil 形式を
\(\operatorname{span}\{R_ak,\ldots,R_ak^{(2m)}\}\) へ制限した standard \(L^2\) 一般化固有値問題は、十分大きい \(a\) で正定値かつ最小固有値が単純。
位相を選んだ単位最小固有関数は
\[
u_{a,m}\longrightarrow k/\|k\|_2.
\]
その最小値は
\[
\boxed{\mu_{a,m}\sim
\frac{a(m!)^2}{\sqrt\pi\,\|k\|_2^2}
Y^{7/2-2m}e^{-2Y}.}
\tag{HG1}
\]

| \(m\) | \(\mu_{a,m}\sqrt\pi\|k\|_2^2/(ae^{-2Y})\) |
|---|---|
| 1 | \(Y^{3/2}\) |
| 2 | \(4Y^{-1/2}\) |
| 3 | \(36Y^{-5/2}\) |

表は漸近式。有限窓の数値 fit ではない。
切る前の最小関数の raw 係数は
\[
\frac{c_j}{c_0}\sim
\frac{(-1)^j\binom mj}{4^jY^{2j}},\qquad c_0\to1/\|k\|_2.
\tag{HG2}
\]
有限 \(a\) の関数が \(R_ak\) そのものだとは言わない。

完全な証明と domain は [support_hierarchy.md](hierarchical_selection/notes/support_hierarchy.md) SH1–SH7。
旧 \(m=1\) 定理に名前を付けただけではなく、高次消去後の全 profile 空間で relative coercivity を証明した。

## 2. 高次消去後にも実際の素数項を残した理由

第1 theta 項の多項式 \(P_0,P_2,\ldots,P_{2m}\) について、境界 \(Y\) の Taylor jet を exact な座標に取る。
この基底は profile 空間全体で
\[
\frac{Q(R_af)}{2a\kappa_Y}=z^*H_Yz,\qquad
H_Y\to H>0,\quad
H_{rs}=\frac{(r+s)!}{2^{r+s+1}},\quad
\kappa_Y=\pi^{-1/2}Y^{-1/2}e^{-2Y}
\tag{HG3}
\]
を満たす。全整数 theta tail は exponentially small。
polar と全 prime-power 和は、同じ座標で
\(O_m(\kappa_Y\log Y/\sqrt Y)|z|^2\)。
archimedean 主項は \(2a\kappa_Yz^*Hz\)。従って相殺する raw 係数にも一様な relative error となる。
raw 行列の絶対誤差を小さい Schur pivot へそのまま流用する危険を、この評価で避けた。

## 3. Exact Schur と Gram を同時に運ぶ

actual \(Q\) の高階方向を逆順に直交化する exact congruence \(U_Y\to I\) により
\[
U_Y^*MU_Y=\operatorname{diag}(d_0,\ldots,d_m),\quad
U_Y^*GU_Y\to G_\infty>0,
\]
\[
d_j\sim a\kappa_Y16^j((m-j)!)^2Y^{6j+4-2m}.
\tag{HG4}
\]
Schur pivot を一般化固有値そのものと同一視しない。
同じ合同変換で physical Gram も運ぶ。
最小化後の境界多項式は weighted \(L^2(e^{-2v}dv)\) の Laguerre polynomial であり、係数の大小だけからの選択ではない。

## 4. Anzellotti–Baldo 原典と適用前件

一次原版：G. Anzellotti and S. Baldo, *Asymptotic Development by Γ-Convergence*,
Applied Mathematics and Optimization **27** (1993), 105–123,
[DOI](https://doi.org/10.1007/BF01195977)、[大学公開の原版 PDF](https://www.mat.univie.ac.at/~stefanelli/cv/paper3.pdf)。
取得 PDF の SHA-256 は `677062924535a6c25540780f08f9b4a14ab91cb594a3d382b11fb31eb3b5dca0`。
§1 の本文 pp.106–112 を読み、pp.108–109 の式と証明は原版画像でも照合した。

- Definition 1.1 (p.107)：位相を固定した liminf と recovery sequence。
- Definition 1.3 (p.108)：前の limit の minimum を引き、再尺度化して minimizer set 上で次の Γ-limit を取る。
- Theorem 1.2 と直後の remark (p.109)：収束する minimizer 列への選択・最小値展開。compactness を欠けば全列の最小値展開は従わない。
- 反復の定義 (pp.109–110)、Example 1.4 と尺度についての remark (pp.111–112)：尺度の選び方は実質的条件。

このノートの定理を原論文から直接引用したのではない。
今回の前件は次の通り内部で満たした：

| 前件 | 今回の実現 |
|---|---|
| 固定位相 | raw coefficient の \(G_\infty\)-unit sphere、通常の有限次元位相 |
| compactness | sphere が compact、phase quotient も compact |
| 第1尺度 | actual formula から \(s_m=a\kappa_Y16^mY^{4m+4}\) |
| successive scale | \(\varepsilon=Y^{-6}\) |
| liminf | exact positive Schur diagonal の各項から導出 |
| recovery | \(U_Y\to I\) により高い座標を exact に消し、元の Gram で正規化 |
| 余項 | jet 空間全体で (HG3)、固定 \(m\) に一様 |

最初に \(s_m\) で割らず、raw の exponentially small \(Q\) を単に \(Y^{-1}\) のべきで展開すれば、各有限次数で零が残る。
外部理論は正しい尺度を自動で供給しない。

## 5. 実際の Γ hierarchy

\(S=\{c:c^*G_\infty c=1\}\) 上で
\[
\mathcal F_Y(c)=\frac{c^*Mc}{s_m c^*G(a)c},\qquad\varepsilon=Y^{-6}
\]
と置く。
\(r=0,\ldots,m\) に対し、\(\varepsilon^{-r}\mathcal F_Y\) の Γ-limit は
\[
\frac{(r!)^2}{16^r}|c_{m-r}|^2
\quad\text{on }\{c_m=\cdots=c_{m-r+1}=0\},
\tag{HG5}
\]
それ以外で \(+\infty\)。\(r<m\) の各 minimum は0。
最高階から順に零成分が増え、最後に projective \(\operatorname{span}k\) が残る。
\(m=1\) の方向選択は最初の rank-one limit だけで足りる普通の行列摂動でもある。
\(m=2,3\) と一般 fixed \(m\) は、exact Schur と recovery を含むこの有限 hierarchy で整理できる。

## 6. Positive transfer lemma の範囲

別の実現 \(T_a\) でも、同じ exact jet 座標で
\(c(2a\kappa_Y)|z|^2\le Q(T_af_c)\le C(2a\kappa_Y)|z|^2\)
が fixed \(m\) に一様で、raw physical Gram が \(G_\infty>0\) に収束するなら、
同じ有限次元 rank-one metric argument は raw coefficient line \(\to\operatorname{span}e_0\) を与える。
物理関数の restricted lowest direction \(\to k\) には、さらに各固定列
\(T_af_j\to f_j\) in \(L^2\) が必要である。
Gram convergence だけなら等長回転が残り、物理関数の収束までは従わない。
この補題と、可変係数に対する physical Gram 誤差の一様性は
[詳細 SH8](hierarchical_selection/notes/support_hierarchy.md#sh8-一様に正な-jet-形式への有限次元-transfer-lemma) で証明した。
極限 profile 行列が存在する場合、その行列を (HG3) の \(H\) に代えればよい。
ただし本担当は \(P_NR_a\) についてこの前件を証明した扱いにしない。
full transfer は root の別担当ノートで actual 誤差を確認する必要がある。

**HIERARCHICAL SELECTION IDENTIFIED: actual Weil form の support-only regularization は、任意の fixed finite \(m\) で一意な restricted lowest eigenline を \(\operatorname{span}k\) へ選ぶ。**

全 \(H_a\) の ground 比較、\(m\to\infty\)、任意の Fourier cofinal path、G*、RH は未証明。

独立監査：DESTROYER が詳細ノート SH1–SH9 の内部証明を再計算し PASS。
高次相殺後にも使える一様誤差、Gram の同時変換、recovery sequence を監査対象に含む。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/hierarchical_selection/notes/support_hierarchy.md`](hierarchical_selection/notes/support_hierarchy.md)
