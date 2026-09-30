**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/global-energy-prior-art.md` · Original SHA-256: `74fa4201687e2950575aea8f96ef0bfd767302579a156874d20bff2b43ba0155`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 全実線距離エネルギー G1 の先行研究照合

調査日: 2026-09-29。開始05:58 UTC、約5分の限定調査。担当: LITERATURE AUDITOR。対象は一次資料に書かれた汎関数・定義域・平衡プロファイルの照合であり、網羅的な新規性調査や G1 本文の独立証明監査ではない。

**判定: 同じ汎関数の既存研究と、CDF 変換後の同じ sine profile を確認した。汎関数・余弦型最小化関数・鋭い定数を新規成果とは表示しない。CDF を用いた平方完成の完全に同じ記述は今回発見していないが、それは新規性の証明にならない。RH への接続はない。**

## 1. 照合対象と係数

対象は \(f\ge0\)、\(f\in L^1(\mathbb R)\cap L^2(\mathbb R)\)、\(\int f=1\)、\(\int|x|f(x)dx<\infty\) に対する

\[
 E[f]=\int f^2+\iint|x-y|f(x)f(y)\,dxdy.
\]

G1 の主張は最小値 \(\pi/(2\sqrt2)\)、平行移動を除く最小化関数

\[
 f_*(x)=\frac1{\sqrt2}\cos(\sqrt2x)\,
 \mathbf1_{|x|\le\pi/(2\sqrt2)},
\]

および CDF \(F(x)=\int_{-\infty}^x f\) による

\[
 E[f]-\frac{\pi}{2\sqrt2}
 =\int\bigl(f-\sqrt{2F(1-F)}\bigr)^2dx.
\]

以下の係数換算は本調査で計算したものであり、引用元がこの記号・規約で述べたとの主張ではない。

## 2. 同じ変分問題: aggregation–diffusion

**Carrillo, Hittmeir, Volzone, Yao**, *Nonlinear aggregation-diffusion equations: radial symmetry and long time asymptotics*, Invent. Math. **218** (2019), 889–977。[DOI 10.1007/s00222-019-00898-x](https://doi.org/10.1007/s00222-019-00898-x)、[出版版 PDF](https://d-nb.info/1204815410/34)、[arXiv:1603.07767](https://arxiv.org/abs/1603.07767)。査読掲載: YES（出版版に2019-06-09受理、07-25公開）。原文照合: YES。論文全体の独立再証明: NO。

確認箇所: §2 の (K1)–(K4)、§3 冒頭 pp.933–934 の汎関数と \(Y_M\)、(3.1)、(K5)、Theorems 3.3 / 3.7 / 3.10、(3.8)–(3.9)。エネルギーは

\[
 \mathcal E[\rho]=\frac1{m-1}\int\rho^m
  +\frac12\iint W(x-y)\rho(x)\rho(y)\,dxdy.
\]

Theorem 3.10 は指定条件下で、全質量 \(M>0\) に対する大域最小化関数の存在、対称減少性、compact support、連続性を与える。Theorem 3.7 は支持内部での Euler–Lagrange 条件を与える。今回、これらの条件・結論を本文照合した。

**対象との対応（本調査の代入）:** \(d=1,m=2,M=1,W(x)=2(|x|-1)\) とすれば、\(\omega(1)=0\) の規約に一致し、\(\mathcal E[f]=E[f]-1\)。\(\omega'=2\) なので (K1)–(K3)、線形成長から (K4)、\(\omega_+(r)\to\infty\) から (K5)、\(m>\max\{2-2/d,1\}\) は成立する。\(\omega(1+|x|)=2|x|\) なので \(Y_1\) の可積分性は今回の有限一次 moment 条件に対応する。重心0の条件は平行移動で処理できる。

同じ代入で (3.8) は支持内部の \(2f+W*f=\mathrm{const}\)。分布として \(W''=4\delta_0\) なので \(f''+2f=0\)。対称減少・連続・compact support と質量1から上記の余弦型が得られる。従って**既存の大域最小化定理と初等的 ODE 計算から G1 の最小化関数が回収できる**。この最後の代入計算は当ノートでの推論であり、原論文中に数値定数 \(\pi/(2\sqrt2)\) が印字されていることは確認していない。

**補足資料:** Craig–Topaloglu, *Aggregation-Diffusion to Constrained Interaction: Minimizers & Gradient Flows in the Slow Diffusion Limit*。[arXiv:1806.07415v2](https://arxiv.org/pdf/1806.07415v2)、[出版版 DOI 10.1016/j.anihpc.2019.10.003](https://www.numdam.org/item/10.1016/j.anihpc.2019.10.003.pdf)。査読掲載: YES。v2 (1.1)–(1.3) も同じ二項エネルギーと \(|x|^p/p\) の族を明記する。今回は汎関数の照合のみで、slow-diffusion 極限定理を G1 の証明に使っていない。

## 3. さらに直接的な対応: double-obstacle phase-field

**Tschukin, Silberzahn, Selzer, Amos, Schneider, Nestler**, *Concepts of modeling surface energy anisotropy in phase-field approaches*, Geothermal Energy **5**, 19 (2017)。[出版社本文／DOI 10.1186/s40517-017-0077-9](https://link.springer.com/article/10.1186/s40517-017-0077-9)。査読掲載: YES（2017-10-03受理、10-11公開）。原文照合: YES。全論文の独立検証: NO。

“Isotropic phase-field model for two phases” の (6) は

\[
 \mathcal F[\phi]=\gamma\int
 \left(\epsilon|\phi'|^2+\frac1\epsilon w(\phi)\right)dx,
 \qquad w(\phi)=\frac{16}{\pi^2}\phi(1-\phi)
 \quad(0\le\phi\le1),
\]

外側では \(w=+\infty\)。式 (7) は、0から1へ遷移する有限幅の平衡プロファイル \(\tfrac12[1+\sin(4x/(\pi\epsilon))]\) を明記する。

**対象との厳密な係数対応（本調査の計算）:**

\[
 \phi=F,\qquad \epsilon=\frac{2\sqrt2}{\pi},\qquad
 \gamma=\frac{\pi}{2\sqrt2}.
\]

このとき \(\gamma\epsilon=1\)、\(16\gamma/(\pi^2\epsilon)=2\)。距離項の CDF 恒等式を使えば

\[
 E[f]=\int\{(F')^2+2F(1-F)\}dx=\mathcal F[F].
\]

式 (7) は \(F_*=(1+\sin(\sqrt2x))/2\)（\(|x|\le\pi/(2\sqrt2)\)、外側0または1）へ一致し、その微分が G1 の \(f_*\) である。phase-field 一般には非単調の関数も許されるが、ここでは単調 CDF の部分クラスに制限しており、同じプロファイルがそのクラスに入る。

G1 の平方完成で現れる境界定数は

\[
 2\int_0^1\sqrt{2s(1-s)}\,ds=\frac{\pi}{2\sqrt2}.
\]

従って本件は、既知の double-obstacle 界面エネルギーとプロファイルの CDF 表示に正確に対応する。上記論文の主目的は異方性であり、これを CDF 不等式の原典または最古の発見と指定してはいけない。

より古い確認例として **Charlie Elliott**, *A Sharp Diffuse Interface Tracking Method for Approximating Evolving Interfaces*, Oberwolfach Report **10/2005**, p.546 は、\(W(u)=(1-u^2)/2\)（\(|u|\le1\)、外側無限大）と \(u=\sin r\)、\(|r|\le\pi/2\) を記す。[EMS の報告原文](https://ems.press/content/serial-article-files/45985)。これは著者自身の研究報告／survey talkであり、単独の査読付き原著定理として数えない。本文内の早期文献は今回未追跡。

## 4. 同じ形だが結論を区別すべき資料

**Yuta Ito**, *Gravitational polarization of test-mass potential in equilibrium polytropic sheets with non-negative polytropic indexes*, [arXiv:2303.14876v1](https://arxiv.org/html/2303.14876v1)。区分: PREPRINT、査読掲載は今回未確認。§2.1 (2.7) は \(\rho=\rho_c(-\phi)^n\)、§3.2 (3.7)–(3.8) は \(n=1\) の \(\phi=-\cos z\)、支持端 \(z_M=\pi/2\) を明記する。したがって余弦型の compact density 自体にも先行例がある。ただしこの資料は重力シートの平衡・摂動研究であり、今回の全 \(L^1\cap L^2\) クラスに対する G1 の最小値や平方剰余恒等式の証明としては採用しない。

**Burger–Di Francesco–Franek**, *Stationary states of quadratic diffusion equations with long-range attraction*, [arXiv:1103.5365](https://arxiv.org/pdf/1103.5365)。使用版: PREPRINT、出版版照合未実施。§1 と Theorem 4.13 の案内は1次元の一意な compact steady state を扱うが、核 \(G\) は非負・可積分・滑らかで、エネルギーは負の \(G\) 相互作用を用いる。\(|x|\) をそのまま入れるのは仮定違反であり、同じ定理として扱わない。

## 5. 検索範囲と残る不確実性

主な検索語: `aggregation diffusion quadratic diffusion one dimensional Newtonian cosine stationary minimizer energy`、`quadratic diffusion Newtonian`、`Gini mean difference density inequality`、`polytropic sheet n=1 cosine`、`double obstacle sine energy profile`。検索結果から arXiv、出版社本文、出版版 PDF、EMS 原文を照合した。外部データベースの全引用網・書籍の全原典・非英語文献・過去の定数表は追跡していない。検索エンジンの crawl date を刊行日として採用していない。

|問い|この限定調査の答え|
|---|---|
|同じ距離相互作用＋二次密度の汎関数は既知か|YES。上記 aggregation–diffusion 汎関数の特殊化|
|同じ余弦型密度／sine CDF は既知か|YES。係数換算を明示できる|
|G1 の sharp constant と minimizer を先行定理から回収できるか|YES。全最小化定理の特殊化と初等計算、または phase-field 表示で回収できる|
|CDF の平方剰余式が全く同じ文字列で既刊論文にあるか|今回未確認|
|その未発見から平方完成の新規性を主張できるか|NO|
|RH 証明または査読済みの新成果として扱えるか|NO|

推奨状態: **既知の機構の再導出／新規性主張なし**。本調査は G1 本文の別担当による監査を置き換えず、主依存グラフに新しい RH 到達経路を追加する根拠にもならない。
