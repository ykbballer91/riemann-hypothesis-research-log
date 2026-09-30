**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `research/full_ground_capture/priority2/notes/conditioning_literature.md`; original SHA-256: `8ee50f66fa18cc433b6508507afd975c36f969148e5ada4b9cfd517ddcaf0a51`. Publication formatting does not constitute a new mathematical audit.

---

# Priority 2 — 有限 head の補間・条件数と正規化：原典監査

**STATUS: RIEMANN HYPOTHESIS OPEN**

2026-09-30。対象は有限次数・有限 head の線形代数と、その文献上の根拠だけである。
既存ファイルは変更しない。新規性、次数に一様な評価、growing-m、全 ground の捕捉、
RH を主張しない。actual sharp-support tail の厳密評価と数値認証は別担当であり、
本ノートの文献確認だけで完了したとは扱わない。

## CL1. 規約と今回必要な行列

[cyclicity の規約](../../cyclicity.md)を使い、
\[
 f_j=k^{(2j)},\qquad \widehat k(x)=\Xi(x)/4,
 \qquad \widehat f_j(x)=(-1)^jx^{2j}\Xi(x)/4.
\]
\(h=\pi/a\)、\(t_n=h^2n^2\)、\(w_n=\Xi(hn)/4\) と置く。
まず \(0\le n,j\le m\) の平方 ideal head を
\[
 V_{nj}=t_n^j,\quad D=\operatorname{diag}(w_n),\quad
 S=\operatorname{diag}((-1)^j),\quad A=DVS                         \tag{CL1}
\]
とする。これは full Fourier の標本値行列である。
正規直交 cosine 係数として使う際の \(a\) 依存因子と原点行の因子は、
実際の規約に従って別途左側の対角行列へ入れる。その因子を落としたまま
物理的な特異値下界と呼ばない。

有限 \(a>0\) では \(t_0,\ldots,t_m\) は相異なる。
\(A\) の可逆性には各 \(w_n\ne0\) も必要である。
「Xi は非零 entire」から、指定された全格子点で非零とは結論できない。
有限の値は別途解析下界または区間演算で確認する。
固定 \(m\)、十分大きい \(a\) なら、\(\Xi(hn)\to\Xi(0)\ne0\) により
非零性は従うが、この議論は具体的な有限 cutoff の認証値を与えない。

<a id="cl2-gautschi-の原典と-cardinal-係数"></a>

## CL2. Gautschi の原典と cardinal 係数

Walter Gautschi, *Norm Estimates for Inverses of Vandermonde Matrices*,
Numerische Mathematik **23** (1975), 337–347。
[著者の公開 PDF](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf)。
原典の §3、p.339、(3.3) は Lagrange 多項式による逆行列、
§4、p.340、(4.1) は逆行列ノルム上界と同一半直線上の点での等号を与える。
該当本文・式を確認した。論文全体の独立再証明や計算機検証ではない。

重要な転置の違い：原著の Vandermonde は **nodes が列**である。
今回の (CL1) は nodes が行なので、原著の \(\infty\)-norm の結論は
今回の \(1\)-norm へ読み替える。

ここから先の今回の行列への適用は、以下の直接計算でも確認できる。
\[
 L_n(t)=\prod_{r\ne n}\frac{t-t_r}{t_n-t_r}
       =\sum_{j=0}^m b_{jn}t^j,
 \qquad V^{-1}=(b_{jn}).                                        \tag{CL2}
\]
全 \(t_r\ge0\) なので分子の係数は次数ごとに符号が交代し、絶対値和は
\[
 B_n:=\sum_{j=0}^m|b_{jn}|
 =\prod_{r\ne n}\frac{1+t_r}{|t_n-t_r|}.                        \tag{CL3}
\]
零ノードを含む場合も、この多項式係数の直接計算で等号が保たれる。
したがって、全 \(w_n\ne0\) の下で
\[
 \|A^{-1}\|_1=\max_n\frac{B_n}{|w_n|},\qquad
 \boxed{\sigma_{\min}(A)\ge
  \left[\sum_{n=0}^m\left(\frac{B_n}{|w_n|}\right)^2\right]^{-1/2}}.
                                                                    \tag{CL4}
\]
第二式は各逆行列列の \(\ell^2\) norm を \(\ell^1\) norm で抑え、
\(\|A^{-1}\|_2\le\|A^{-1}\|_F\) とする、今回の初等的帰結である。
これは通常の Euclidean coefficient norm に関する下界である。

今回の平方ノードでは分母を閉形式で計算できる：
\[
 \prod_{r\ne n}|t_n-t_r|
 =h^{2m}
 \begin{cases}
 (m!)^2,&n=0,\\[2pt]
 (m-n)!(m+n)!/2,&1\le n\le m.
 \end{cases}                                                     \tag{CL5}
\]
\(m=0\) は空積を1とする。\(n\ge1\) の式は
\(n^2\prod_{r\ne n,\,r\ge1}|n-r|(n+r)\) を分解して得る。
従って (CL3)–(CL5) は有限積と有限個の Xi 下界だけで評価できる。

固定 \(m\) では
\(V=V_0\operatorname{diag}(1,h^2,\ldots,h^{2m})\)、
\((V_0)_{nj}=n^{2j}\) であり、\(D\) と \(D^{-1}\) は十分大きい \(a\) で有界。
この分解による下界と最終列による上界から
\[
 \sigma_{\min}(A)=\Theta_m(a^{-2m})\quad(a\to\infty)             \tag{CL6}
\]
が従う。ここでも cosine 規格化因子は含まない。
定数は \(m\) に依存し、growing-m 評価ではない。

## CL3. 離散直交多項式は span を変えない

Pablo D. Brubeck, Yuji Nakatsukasa, Lloyd N. Trefethen,
*Vandermonde with Arnoldi*, SIAM Review **63**(2) (2021), 405–415。
[著者公開 PDF](https://people.maths.ox.ac.uk/trefethen/vandermonde_arnoldi.pdf)、
[DOI](https://doi.org/10.1137/19M130100X)。
§4、p.409、(4.2)–(4.5) は同じ多項式を異なる係数で表す
\(A=QR\)、\(d=Rc\) と、離散直交多項式との関係を明記する。
原著の列 norm は便宜上 \(\sqrt{\text{標本数}}\) であり、unit norm と混同しない。
これは実装と基底選択の根拠であり、任意の重み・格子に対する機械精度の保証を
本ノートが新たに採用するものではない。

標準定義の確認には [DLMF 18.2.3](https://dlmf.nist.gov/18.2#E3)
（有限個の相異なる実ノードと正の重み）、
[18.2.5](https://dlmf.nist.gov/18.2#E5)（離散 norm）を用いた。

今回、非零重みのノード上で
\[
 \mu_{\rm head}=\sum_n|w_n|^2\delta_{t_n}
\]
に関する次数 \(0,\ldots,m\) の正規直交多項式を \(p_j\) とすると、
\(U_{nj}=w_np_j(t_n)\) は \(U^*U=I\) を満たす。
各 \(p_j\) の係数変換は可逆で、対応する関数は依然
\(F_m=\operatorname{span}\{f_0,\ldots,f_m\}\) に属する。
正規化は物理的な有限 span を変更しない。

しかし、**どの norm を正規化したか**は別の問題である。
\[
 G=A^*A,\quad U=AG^{-1/2},\quad U^*U=I                         \tag{CL7}
\]
は head の pullback metric に関する恒等式である。
full physical \(L^2\) の Gram
\[
 C_{ij}=\langle f_i,f_j\rangle_{L^2(\mathbb R)}                 \tag{CL8}
\]
とは一般に異なる。物理 norm を係数の Euclidean norm に揃える行列は
\(AC^{-1/2}\) であり、その特異値が1になるとは限らない。
\(C\) の正定値性は actual 関数族の線形独立性による。
support-restricted 関数を domain に選ぶ場合は、対応する \(C_a\) を使う。
この選択を明示せず \(G\) と \(C\) を置き換えない。

例えば平方行列の場合、\(z_n\) を \(A^{-1}\) の第 \(n\) 列とすれば
\[
 \sigma_{\min}(AC^{-1/2})
 \ge\left(\sum_n z_n^*Cz_n\right)^{-1/2}.                      \tag{CL9}
\]
これは \((AC^{-1/2})^{-1}=C^{1/2}A^{-1}\) の Frobenius norm から得る。
各項は cardinal 応答関数の **physical \(L^2\) norm の二乗**である。
単項式係数が大きいことと物理応答が大きいことを同一視せず、必要ならこの量を使う。

## CL4. Christoffel 表示が与えるもの・与えないもの

[DLMF 18.2.12–18.2.13](https://dlmf.nist.gov/18.2#E12) で
Christoffel–Darboux kernel の規約を確認した。
今回の有限離散空間では
\[
 K_m(t,t)=\sum_{j=0}^m|p_j(t)|^2.
\]
\(UU^*\) が直交射影なので、直接
\[
 0\le |w_n|^2K_m(t_n,t_n)\le1,\qquad
 \sum_n|w_n|^2K_m(t_n,t_n)=m+1.                                \tag{CL10}
\]
平方補間なら \(UU^*=I\) であり、各積は1、従って
\(K_m(t_n,t_n)=|w_n|^{-2}\)。小さい Xi 値の逆数コストは消えず、
別の表示に移っているだけである。

多項式の右側基底変換と、標本行を Christoffel weight で掛け直す操作を区別する。
後者は一般に観測 norm または最小二乗の metric を変更する。
元の物理的 head norm と同一という主張には、逆変換と norm 比較が別途必要である。

## CL5. Sharp support 誤差を移すときの十分条件

actual head を \(\widetilde A=A+E\) とする。
ここで \(E\) は **同じ列・同じ head 規格化**で求めた切断誤差である。
三角不等式だけで
\[
 \sigma_{\min}(A+E)\ge\sigma_{\min}(A)-\|E\|_2.               \tag{CL11}
\]
ideal head Gram を用いる場合は
\[
 \varepsilon=\|EG^{-1/2}\|_2<1
 \quad\Longrightarrow\quad
 1-\varepsilon\le\sigma_j((A+E)G^{-1/2})\le1+\varepsilon.       \tag{CL12}
\]
full-column-rank の範囲で、任意の unit vector に (CL7) と三角不等式を適用すればよい。
raw tail の絶対値だけではなく、\(G^{-1/2}\) による増幅まで評価する必要がある。
actual 行列自身の Gram を正定値と仮定して正規化し、その結果を rank の証明に
使うのは循環である。

物理 norm なら評価対象は
\[
 \sigma_{\min}((A+E)C^{-1/2})
 \ge \sigma_{\min}(AC^{-1/2})-\|EC^{-1/2}\|_2.                 \tag{CL13}
\]
例えば \(\|EC^{-1/2}\|_2\le\|E\|_2/\sqrt{\lambda_{\min}(C)}\)
という粗い上界は使えるが、その Gram 下界も明示する。
本ノートは \(E\) の actual 数値、tail の明示定数、認証成功を供給していない。

長方形行列についても次の区別が必要：

- 行数が列数以上なら、非零重みを持つ相異なる \(m+1\) 行の部分行列で
  (CL4) を証明すると、全行列の \(A^*A\) はその部分の Gram 以上なので
  同じ最小特異値下界が使える。
- 行数が列数未満なら \(A^*A\) は特異。full-row-rank を別途示した場合の
  \((AA^*)^{-1/2}A\) は coisometry だが、元の物理 norm の安定性を
  自動的に証明するものではない。

## CL6. 確率的最小二乗定理は固定格子の証明にならない

Albert Cohen, Mark A. Davenport, Dany Leviatan,
*On the stability and accuracy of least squares approximations*。
[arXiv:1111.4422 PDF](https://arxiv.org/pdf/1111.4422)、
Theorem 1、原稿 p.3、(1.2) を確認した（今回取得したリンクは版未固定）。
指定確率測度に関する独立同分布標本 \(x_1,\ldots,x_n\)、
その測度で正規直交な \(d\) 次元基底を前提に
\[
 \Pr\{\|G-I\|_2>\delta\}
 \le2d\exp[-c_\delta n/K(d)],\qquad
 c_\delta=(1+\delta)\log(1+\delta)-\delta,
 \quad0<\delta<1,                                              \tag{CL14}
\]
を与える。\(K(d)\) は正規直交基底の二乗和の上限である。

今回の \((\pi n/a)^2\) は決定論的な固定格子で、Xi 重みも指定されている。
従って (CL14) をそのまま actual head の認証に適用しない。
別の sampling measure を設計して良条件にしても、そのまま元の物理的問題を
証明したことにはならない。これは適用条件の不一致であり、確率定理の否定ではない。

## CL7. Confluent Vandermonde は今回不要

現在の head は \(n\ge0\) の偶 Fourier/cosine 成分なので、
\(+n\) と \(-n\) を別々に二重登録しない。有限 \(a>0\) では
\(t_n=h^2n^2\) が相異なり、通常の Lagrange 補間で十分である。

\(a\to\infty\) で物理的なノードが0へ集まることは、各有限段階に
重複ノードがあることを意味しない。\(t\mapsto t/h^2\) という正確な変数変更で
ノードは \(n^2\) に固定され、代わりに列係数の scaling が現れる。
その scaling を norm 評価に残せばよい。

Confluent/Hermite 補間が必要なのは、同じノードで関数値に加えて導関数値を
データとして指定する別の問題である。Xi 標本値が0である行を導関数観測で
置換する操作も、今回の readout を変更するため自動的な修復ではない。

## CL8. 採用範囲

採用できるのは (i) 原典で裏付けられた cardinal 逆行列表示、
(ii) 今回の平方ノードへの有限積・特異値下界、
(iii) 同じ有限 span 内での直交基底への変更、
(iv) ideal/actual、head/physical の norm を固定した摂動十分条件である。

未完の個別義務は、使用する有限 Xi 標本の下界、actual tail、選択した Gram と
規格化を含めた定数・誤差の認証である。これらを本ノートの文献確認によって
検証済みにはしない。固定有限次数を超える一様性、全 ground、ES、G*、RH は扱わない。

文献確認は上記の関連 statement と適用条件に限る。内部 AI-agent による確認であり、
外部査読、各原論文の完全独立検証、新規性の認定を意味しない。
