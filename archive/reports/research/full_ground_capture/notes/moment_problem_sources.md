**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/full_ground_capture/notes/moment_problem_sources.md` · Original SHA-256: `c9979e20369490291872eb777965d65ae80aaefb33b48df7f456454d0211ce98`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 偶数階微分族の L²-cyclicity：moment criterion と直接証明

**STATUS: RIEMANN HYPOTHESIS OPEN**

2026-09-30。今回の範囲は cyclicity のみ。既存ファイル・公開用 audit は変更しない。
新規性を主張しない。既知の指数 moment / polynomial-density 原理を actual kernel に適用する。
Priority 2 以降の ground capture、form domain、gap、選択の一様性へは進まない。

## M1. 結論と規約

既存の actual normalization を固定する：
\[
 \widehat k(x)=\int_{\mathbb R}k(t)e^{-ixt}dt=\frac14\Xi(x),
 \qquad \Xi(x)=\xi(1/2+ix).
 \tag{M1}
\]
すると無条件に
\[
 \boxed{\overline{\operatorname{span}_{\mathbb C}
       \{k^{(2j)}:j=0,1,\ldots\}}^{\,L^2(\mathbb R)}
       =L^2_{\mathrm{even}}(\mathbb R).}
 \tag{M2}
\]
real even 空間でも real span が稠密である。
これは**全次数を取った閉包**についての定理であり、
固定有限 \(m\) の誤差、係数の大きさ、\(a,N,m\) の joint rate を与えない。

既存 normalization の出所は read-only の
[full projection bound](../../rate_history/notes/full_projection_upper_bound.md) §1–2。
その無条件 Fourier decay は以下でも独立に確認する。

## M2. 一次・標準資料の照合範囲

### Marcel de Jeu

*Determinate multidimensional measures, the extended Carleman theorem and
quasi-analytic weights*。
[arXiv:math/0111019v2 原文](https://arxiv.org/pdf/math/0111019v2)、
版日 2002-06-17。刊行書誌は
Annals of Probability **31** (2003), 1205–1227、
[DOI](https://doi.org/10.1214/aop/1055425776)。
[arXiv の書誌](https://arxiv.org/abs/math/0111019v2)も確認した。
DOI 本文取得は今回 tool error のため、以下の頁は **v2 原稿頁**。

- **Theorem 2.3、p.5、式 (2.1)**：
  finite positive measure、全 absolute moments 有限、
  各座標の \(\sum_{n\ge1}s(2n)^{-1/(2n)}=\infty\) の下で、
  determinacy に加え、polynomials が全 \(1\le p<\infty\) の \(L^p\) で稠密。
  本稿では一次元・\(p=2\) だけを使う。
- **Theorem 1.1 p.2 と p.3 冒頭**：
  正の指数 moment は上の結論の既知の十分条件。
- **Theorem 5.1、p.15、式 (5.1)**：
  正半直線での Stieltjes 条件は
  \(\sum s(n)^{-1/(2n)}=\infty\)。
  原定理の結論は cone 内の determinacy。これを無断で
  \(L^p\)-density の一般 cone 定理と読み替えない。

使用 statement と証明の該当箇所を確認した。論文の全証明を独立再検証したとはしない。
以下の指数 moment 特殊例は文献定理を使わずにも証明する。

### NIST DLMF

- [5.11.9](https://dlmf.nist.gov/5.11#E9)：
  bounded real part に一様な Gamma の vertical Stirling asymptotic。
- [25.9.2–25.9.3](https://dlmf.nist.gov/25.9#E3)：
  critical line の approximate functional equation。
  25.9.3 の原典 locator は Titchmarsh (1986), (4.12.4), p.79。
  今回 Titchmarsh 原書全文は取得せず、公式 DLMF の式を確認した。
- [25.4.3–25.4.4](https://dlmf.nist.gov/25.4#E4)：
  completed \(\xi\) の規約と functional equation。

これらは標準入力であり、RH や新しい算術的評価を仮定しない。

## M3. Actual weight の指数 moment

\(q(x)=\Xi(x)\) と置く。
DLMF 25.9.3 で \(m=\lfloor\sqrt{x/(2\pi)}\rfloor\)、\(x\to+\infty\) とすれば、
critical line の \(|\chi|=1\) と
\(\sum_{n\le m}n^{-1/2}\le2\sqrt m\) により
\[
 |\zeta(1/2+ix)|=O(x^{1/4}).
 \tag{M3}
\]
negative \(x\) は共役対称性で同じ。これは coarse classical upper bound であり、
RH や Lindelöf を使わない。
Gamma の式は
\[
 |\Gamma(1/4+ix/2)|
 \le C(1+|x|)^{-1/4}e^{-\pi|x|/4}.
 \tag{M4}
\]
completed factors \(s(s-1)/2\)、\(\pi^{-s/2}\) を含めて
\[
 |q(x)|\le C(1+|x|)^2 e^{-\pi|x|/4}.
 \tag{M5}
\]
小さい \(x\) は連続性で定数へ吸収する。
さらに粗い既存 Euler-summation bound \(\zeta=O(1+|x|)\) を使って
polynomial exponent を 3 にしても以下は変わらない。

従って finite positive Borel measure
\[
 d\mu(x)=|q(x)|^2\,dx
 \tag{M6}
\]
は全 \(0<\eta<\pi/2\) について
\[
 K_\eta:=\int_{\mathbb R}e^{\eta|x|}\,d\mu(x)<\infty.
 \tag{M7}
\]
\(\mu\) は even である。\(q\) は非零 entire function なので、実軸の零点集合は
discrete、従って Lebesgue measure 0。
ここで必要なのは **実軸上で nonzero almost everywhere** だけであり、
全 complex zeros が実軸にあるという RH は一切用いない。

## M4. Hamburger Carleman と even symmetrization

\(m_n=\int x^n\,d\mu(x)\) と置く。
任意の固定 \(\eta\in(0,\pi/2)\) に対し
\[
 m_{2n}\le K_\eta(2n)!\eta^{-2n}.
 \tag{M8}
\]
よって、\((2n)!\le(2n)^{2n}\) から
\[
 m_{2n}^{-1/(2n)}
 \ge\frac{\eta K_\eta^{-1/(2n)}}{2n},\qquad
 \sum_{n=1}^{\infty}m_{2n}^{-1/(2n)}=\infty.
 \tag{M9}
\]
de Jeu Theorem 2.3 は polynomials の \(L^2(\mu)\)-density を与える。
determinacy という語だけを density の証明の代わりにしない。

even \(F\in L^2(\mu)\) に対し polynomial \(P_n\to F\) を取り、
\[
 P_n^{\rm ev}(x)=\frac{P_n(x)+P_n(-x)}2
 \tag{M10}
\]
とすると、reflection が unitary だから
\(\|P_n^{\rm ev}-F\|_{L^2(\mu)}\le\|P_n-F\|_{L^2(\mu)}\)。
従って even polynomials \(\operatorname{span}\{x^{2j}\}\) は
\(L^2_{\rm even}(\mu)\) で稠密。

さらに
\[
 U:L^2_{\rm even}(\mu)\to L^2_{\rm even}(dx),\qquad UF=qF
 \tag{M11}
\]
は onto isometry。onto 性は、任意の \(G\in L^2_{\rm even}(dx)\) に対し
\(F=G/q\) を \(q\ne0\) 上で定義すれば
\(\int|F|^2\,d\mu=\int|G|^2dx\) となることから従う。
real zeros での割り算は null set を除くだけであり、pointwise lower bound は不要。

(M1) と \(\widehat{k^{(2j)}}=(-1)^jx^{2j}q(x)/4\)、
Plancherel により (M2) が従う。
Fourier の \(2\pi\) normalization と定数 \(1/4\) は閉包に影響しない。

## M5. \(x^2\) pushforward の正しい criterion

\(\nu=(x\mapsto x^2)_*\mu\) と置くと、\([0,\infty)\) 上の measure で
\[
 s_n:=\int_0^\infty y^n\,d\nu(y)=m_{2n}.
 \tag{M12}
\]
また
\[
 d\nu(y)=\frac{|q(\sqrt y)|^2}{\sqrt y}\,dy\quad(y>0),
 \tag{M13}
\]
原点 atom はない。正しい Stieltjes Carleman sum は
\[
 \sum_{n\ge1}s_n^{-1/(2n)}
 =\sum_{n\ge1}m_{2n}^{-1/(2n)}=\infty.
 \tag{M14}
\]
de Jeu Theorem 5.1 の一次元版と一致する。
この \(\nu\) の polynomial density 自体は
\(F(y)\mapsto F(x^2)\) の onto isometry と M4 の even density から既に従う。

一方、\(\nu\) に **Hamburger** criterion を直接掛けると別の sum
\[
 \sum_{n\ge1}s_{2n}^{-1/(2n)}
 =\sum_{n\ge1}m_{4n}^{-1/(2n)}
 \tag{M15}
\]
になる。これを (M14) と同一視してはならない。
指数 moment の上界だけでは (M15) の発散を証明できない。
例えば比較模型 \(d\mu_0=e^{-|x|}dx\) では
\(m_{4n}=2(4n)!\) だから (M15) は \(n^{-2}\) 型で収束するが、
(M14) は \(n^{-1}\) 型で発散する。
これは criterion の十分性と変数変換の違いであり、actual \(\mu\) の (M15) の
収束を証明したという意味ではない。

## M6. 指数 moment だけによる直接証明

文献の polynomial-density theorem を使わずに同じ結論を得る。
\(G\in L^2_{\rm even}(dx)\) が全 \(x^{2j}q(x)\) に直交すると仮定し、
\[
 h(x)=G(x)\overline{q(x)}
\]
と置く。Cauchy–Schwarz と (M7) から、全 \(0<b<\pi/4\) について
\[
 \int|h(x)|e^{b|x|}dx
 \le\|G\|_2
 \left(\int |q(x)|^2e^{2b|x|}dx\right)^{1/2}<\infty.
 \tag{M16}
\]
従って
\[
 H(z)=\int_{\mathbb R}h(x)e^{izx}dx
 \tag{M17}
\]
は connected strip \(|\operatorname{Im}z|<\pi/4\) で holomorphic。
compact substrip ごとに少し大きい \(b\) を選べば、全導関数の積分交換も正当化できる。

直交条件で even moments はすべて 0、\(h\) が even なので odd moments も 0。
よって \(H^{(n)}(0)=0\) が全 \(n\ge0\) で成立する。
holomorphic identity theorem で \(H\equiv0\)。
\(h\in L^1\) の Fourier uniqueness から \(h=0\) almost everywhere、
\(q\ne0\) almost everywhere から \(G=0\) となる。
これで直交補空間が零、従って (M2) が証明される。

有限個の moments だけを使った議論ではない。
同じ全 analytic jet が零であることを確認してから identity theorem を使った。

## M7. 採用できる結論と今回の停止点

採用可能なのは無条件の **\(L^2_{\rm even}\)-cyclicity**。
指数 moment を持つ非零 a.e. multiplier の標準的な density 原理であり、新規性なし。

これは \(k,k'',\ldots\) の既知 Weil-radical 関係と矛盾しない。
radical を支配する form topology と ambient \(L^2\) topology が同じだとは証明していない。
\(L^2\)-dense であることから未証明の boundedness / closability を補ってはならない。

本ノートは form-core density、finite-cutoff uniform approximation、
actual full ground の捕捉、\(m\to\infty\) と cutoff 極限の交換、
ES、\(G^*\)、RH を主張しない。それらの追加探索も行わない。
当面の判定：**cyclicity YES、RH OPEN、Priority 1 のみ完了。**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/rate_history/notes/full_projection_upper_bound.md`](../../rate_history/notes/full_projection_upper_bound.md)
