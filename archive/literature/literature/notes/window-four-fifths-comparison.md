**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/window-four-fifths-comparison.md` · Original SHA-256: `00f71a53b254987700c054bb21d7f4e8924b35d318fdd6a8473e85d52f8b97be`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 半幅 a=4/5: Zhu v2 の固有値・切断損失・既存結果との比較

調査日: 2026-09-29（JST）。対象は root の \(a=0.8,T=111,\beta=0.2\) という比較作用素の試みへの、限定した一次文献照合である。新規性を主張しない。以下で「認証主張」は原著の記載を意味し、当方が原著証明書を再現したという意味ではない。RH と全窓の正値性は未解決のままである。

## 1. 版と比較する量

主資料は Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, [arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2), 2026-09-02 提出／本文日付 September 3, 2026。TeX は既存 cache の `literature/source_cache/zhu/arxiv-v2/main.tex` を使用した。原著コード・200次行列・因子・JSON は以前の取得調査で未発見であり、今回も未実行。査読公刊は未確認、全証明の独立検証 **NO**。取得版・hash と未解決の reduction 点は [既存監査](zhu-certificate-audit.md) を参照。

Zhu の \(L\) は本ノートの半幅 \(a\) である。\(a=0.8\) では試験関数 support は \([-0.8,0.8]\)、自己相関 support は \([-1.6,1.6]\)。素数冪は \(\{2,3,4\}\)。原著の「support 1.6」はこの区別に注意する。

実偶関数に対して、\(F(t)=\int f(x)e^{itx}dx\) とすると

\[
 Q(f)=2F(i/2)^2+\frac1\pi\int_0^\infty\Psi_a(t)|F(t)|^2dt,
\quad
 \Psi_a(t)=\Re\psi(1/4+it/2)-\log\pi
 -\sum_{\log n<2a}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
\]

固有値の単位は \(Q(f)/\|f\|_{L^2(dx)}^2\)。Legendre 基底は \(T_n(x)=\bar P_n(x/a)/\sqrt a\)、\(\int_{-1}^1\bar P_n^2=1\) で **正規直交**。原著の \(N=200\) は偶数次数 \(0,2,\ldots,398\) の200次元であり、次数199まででも、偶奇を合わせた200次元でもない。[Zhu v2 §1.6、§5.1](https://arxiv.org/html/2608.24827v2#S5.SS1)

## 2. a=0.8 の値を混同しない

| 量 | 原著の値・状態 | locator |
|---|---|---|
| 偶 \(R_{200,\beta_{200}}\) の exact 200次 head 下界 | \(9\times10^{-18}-4\times10^{-43}\) 以上という認証主張 | §5.4、Lemma 5.2 |
| 偶の全窓 \(Q\) 下界 | \(8.9\times10^{-18}\) | Theorem 1.2 |
| \(T=200\) の条件 | \(\beta_{200}=0.5134667\ldots\)、50桁、800 panels、幅1/4、32点 Gauss | §5.1 |
| head 求積誤差 | \(c_{err}\le2.06\times10^{-42}\) | Lemma 5.1 |
| 無限 tail と coupling | \(\epsilon_D,\epsilon_B\le10^{-100}\) という主張 | §5.3 |
| 偶 \(T=150\) の全比較形式下界 | \(1.2\times10^{-18}\)、\(\beta_{150}=0.2241\ldots\) | §5.5(a) |
| 偶 \(R_{150}\) の参考スペクトル | \(1.356\times10^{-18},2.32\times10^{-12},2.9\times10^{-7},2.1\times10^{-3},\beta_{150},\ldots\) | §5.5(c)、**非認証参考値** |
| 元の偶形式 \(Q\) の下端参考値 | \(1.656\times10^{-17}\) | §5.5(b)、time-domain assembly の参考値 |
| 元の偶形式 \(Q\) の変分上界 | \(2.27\times10^{-17}\) | §8、Table 2／§11.4 の幾何側認証主張 |

原文 §5.4 は assembled matrix と exact head を分け、shifted Cholesky の residual \(1.06\times10^{-50}\)、roundoff slack \(3.6\times10^{-43}\) と求積誤差を払う。原著の表示 \(9\times10^{-18}\) を、誤差を引く前の exact 下界として引用しない。全窓への移行には head だけでなく無限 tail と coupling の見積りが要る。[Zhu v2 §§5.2–5.5](https://arxiv.org/html/2608.24827v2#S5)

## 3. 小ささは R だけの人工現象か

原著は両方を区別する。§8 は元の \(Q\) 自体の小さい変分上界を挙げ、§14.2 は \(R\) への比較がさらに下界を下げることを説明する。§10 は幾何側の相殺、周波数 tail の切捨て、浮動小数点のノイズが偽の負固有値や偽の減衰則を作る例を報告する。従って、原著の幾何側上界が正しければ、\(a=0.8\) の微小な下端を全て切断のせいにする説明は成立しない。一方、Landau–Widom 定数や大窓での難易度法則は fitted law／上界実験であり、全方式に対する計算量下界として採用しない。

今回の実装比較に必要な正確な式は次である。\(\Psi_a(t)\ge\beta\) が全 \(|t|\ge T\) で証明されたなら

\[
 R_{T,\beta}(f)=\mathcal P(f)+\beta\|f\|^2
 +\frac1{2\pi}\int_{-T}^{T}(\Psi_a(t)-\beta)|F(t)|^2dt,
\]

\[
 Q(f)-R_{T,\beta}(f)
 =\frac1{2\pi}\int_{|t|>T}(\Psi_a(t)-\beta)|F(t)|^2dt\ge0. \tag{*}
\]

ここで \(\mathcal P\) は正負両方の pole 成分を含む。これは Zhu §4 の計算を任意の認証済み exterior floor に適用したもの。原著の粗い envelope で算出した \(\beta^*(T)\) を使うことは十分条件であり、joint symbol の直接認証で得た \(\beta\) に置き換えるには、その exterior inequality 自体を新しく証明すればよい。

\(T=111,\beta=0.2\) の exterior floor が成立しても、head の正値性は従わない。周波数範囲を縮めると、真の \(\Psi\) の代わりに floor を使う領域が増える。また原著の \(\beta_{150}>0.2\) も併せれば、(*) から

\[
 R_{111,0.2}\preceq R_{150,\beta_{150}}\preceq Q
\]

が従う。この向きでは \(R_{150}\) の正値性を \(R_{111}\) に移せない。原著の小さい値は比較資料であり、root の新しい head に値や margin をコピーできない。有限 head の Ritz 最小値と全 \(R\) の下界も別で、基底を増やすだけでは誤差込み認証下界の単調改善は保証されない。

## 4. 偶奇・複素と spectral gap

Zhu Lemma 6.1 は実関数の偶奇分解、複素関数の実部・虚部分解で \(Q\) が直和に分かれることを述べる。偶部分の pole は \(+2|\int f_e\cosh(x/2)dx|^2\)、奇部分は \(-2|\int f_o\sinh(x/2)dx|^2\)。奇部分を偶の正 pole で代用しない。

§6 の奇部分は **別の** \(T=150\)、200奇数次数 \(1,3,\ldots,399\) の計算であり、参考最小値 \(9.1183\times10^{-15}\)、認証主張の shift \(8.2065\times10^{-15}\)。Theorem 6.2 の安全側定数は

\[
 8.9\times10^{-18}\le\lambda_1^{even}\le2.523\times10^{-16},\quad
 \lambda_2^{even}\ge2.085\times10^{-12},\quad
 8.206\times10^{-15}\le\lambda_1^{odd}\le2.347\times10^{-14}.
\]

第二偶値は codimension-one restriction の認証と無限部分への lift を必要とする。参考固有値をその代わりに使わない。偶の上界より奇の下界と第二偶下界が大きいので、これら全証明書が成立すれば simple-even ground state が従う。Corollary 6.3 の一般複素全窓下界は、偶奇双方の下界を使う。[Zhu v2 §6](https://arxiv.org/html/2608.24827v2#S6)

## 5. 作用素の正規化の辞書

Connes–Consani–Moscovici, [*Zeta Spectral Triples*, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1), (3.5)、(3.9)、(3.19)–(3.20) と比較する。\(\lambda=e^a\)、\((Uf)(u)=f(\log u)\) とすれば

\[
 U:L^2([-a,a],dx)\longrightarrow L^2([\lambda^{-1},\lambda],du/u)
\]

はユニタリ。乗法 Fourier の符号は反対だが \(\widehat{Uf}(t)=F(-t)\)。さらに
\(2\theta'(t)=\Re\psi(1/4+it/2)-\log\pi\)。したがって pole の実部付き共役 pairing、対称 prime shifts、archimedean 項をそのまま対応させると、共通の smooth complex domain で \(QW_\lambda(Uf)=Q(f)\) となり、この辞書では余分な正定数倍は不要である。これは表示式の直接照合であって、双方の証明書の検証ではない。

CCM の加法区間 \([0,L]\) の \(L=2\log\lambda\) は**全幅**、Zhu の \(L=a\) は**半幅**。従って本ケースは CCM \(\lambda=e^{0.8}\)、加法全幅1.6である。Zhu §6 は辞書の逐行確認を未実施と明記しているので、原著が operator theorem への全面照合まで完了したとは引用しない。一般 \(L^2\) 上の元の閉形式には値 \(+\infty\) も許し、全 \(L^2\) で有限値となる有界比較形式 \(R\) と区別する。

## 6. 既存のどの範囲が a=0.8 を覆うか

| 一次資料 | 正確な比較範囲と判定 |
|---|---|
| Connes–Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. 27,77 (2021), [著者公刊本文 Theorem 1](https://alainconnes.org/wp-content/uploads/Selecta.pdf), [DOI](https://doi.org/10.1007/s00029-021-00689-4) | support \([2^{-1/2},2^{1/2}]\)、Fourier が \(i/2,0\) で消える条件付き archimedean 比較。加法半幅は \((\log2)/2\approx0.3466\)。この定理を無制約 \(a=0.8\) の強い定数へ流用できない。査読掲載 YES、当方全面検証 NO。 |
| Connes–Consani, *Spectral triples and ζ-cycles*, Enseign. Math.69 (2023), [公刊本文 §2, Proposition 2.3](https://ems.press/content/serial-article-files/44477?nt=1), DOI10.4171/LEM/1049 | 任意 \(\lambda\) の下半連続・下半有界形式と core、最小 Ritz 値の極限。§2.4 の大きい窓の positive matrix は数値調査。全窓の有限定数付き coercivity 定理ではない。査読掲載 YES、全面検証 NO。 |
| CCM arXiv:2511.22755v1, Props.3.3–3.4、Theorem3.6 | \(a=0.8\) でも形式・作用素の定義と離散下半有界 spectrum を与えるが、下端が非負であるとは証明しない。書籍章の個別査読は未確認、全面検証 NO。 |
| Suzuki [arXiv:2606.09096v3 Theorem1.4](https://arxiv.org/html/2606.09096v3#Thmtheorem1.4) | 正・単純・偶は sufficiently small \(a>0\)。この定理文から \(a=0.8\) の適用や数値下界を取り出せない。プレプリント、全面検証 NO。 |
| Zhu v2 | 同じ \(a=0.8\) を覆う明示的下界の**主張**がすでにある。公開証明書を当方未取得・未再現。撤回された \(a=1.19\) は比較定理に含めない。 |

追加の一次資料として Vincent Liu, *Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function*, 2026-09-14 を確認した。[固定 commit の原稿 TeX](https://raw.githubusercontent.com/luciferyu666/certified-weil-positivity/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/frozen-source/publication/manuscript.tex) の Theorem A (3) は \(C_c^\infty((-1,1);\mathbb C)\) に \(2^{-151}\)、Theorem B (6) は半幅 \(17/16\) に \(2^{-49162}\) の下界を主張する。式 (1) の幾何側正規化は本ノートと一致する。support はより大きいが、定数は Zhu の \(8.9\times10^{-18}\) より小さい。小さい窓に制限すれば適用可能という意味でのみ \(a=0.8\) を覆う。

[著者の固定 release](https://github.com/luciferyu666/certified-weil-positivity/releases/tag/v1.0-mcom-submission) と [再現説明](https://github.com/luciferyu666/certified-weil-positivity/blob/b6cd2183c1e79c6c27a34267812a7b2d73ed1b59/REPRODUCIBILITY.md) の実在は確認した。著者は journal acceptance と external reproduction を主張しておらず、今回も **未査読・未独立再現のプレプリント主張**に分類する。原稿 TeX の定理文と正規化だけを短く読んだ。634,659,625-byte package の取得、hash 照合、コード実行、tail・coupling の数学的監査は行っていない。alphaXiv の紹介記事や内蔵 PASS 表示を証明として採用しない。

今回確認した一次資料から、root の \(T=111,\beta=0.2\) の比較形式に既存の正値 margin を移す根拠は得ていない。必要なのは同一正規化での新しい head 誤差・全 tail・coupling の認証である。仮に完成しても固定窓の独立検査であり、RH の証明や先行例のない結果とはしない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/zhu-certificate-audit.md`](zhu-certificate-audit.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/zhu/arxiv-v2/main.tex` — SOURCE REFERENCE NOT INCLUDED
