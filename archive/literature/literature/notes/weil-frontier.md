**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/weil-frontier.md` · Original SHA-256: `3f5919bf8c2f09f4b56203db03330c366141fd444246681c21a48d4c34ab9750`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weil 正値性・有限形式・作用素路線の文献監査

取得日: 2026-09-29（Asia/Tokyo）。一次本文と出版社書誌を web で照合した。調査範囲は Weil quadratic form、finite/Galerkin forms、screw function、Connes–Consani–Moscovici（CCM）、Connes–van Suijlekom（CvS）、Suzuki の2025–2026年論文と直接必要な先行研究。網羅的レビューではない。関連する Suzuki の名は **Masatoshi Suzuki** であり、Yoshikazu ではない。

この記録の「確認」は本文中の定理・仮定・版を確認した意味で、証明の完全な独立検証ではない。arXiv 掲載、査読、著者自身の再計算、第三者再現を別扱いとする。初回調査後の限定再現は下記追記に区別した。検索で見つかった Zenodo 等の RH 証明主張は採用しない。

checkpoint03追記: Groskin c13,N4の有限9次例は原著再実行と独立Arb積分で認証済み。
Zhu v2の原著200次headの公開証明書は取得できず、再現未済。
その代わり別実装でsupport[-1/2,1/2]の全complex form-domainについてQ_W≥9e−8||f||²を認証した。
詳細は `proofs/audits/window-half-certificate.md` と関連監査。全窓への拡張・RH・新規性の主張はない。

## 結論と使用可能性

全 test function 上の Weil 正値性を無条件に確立する結果は、今回確認した資料中にはない。使えるのは、閉形式・自己共役作用素・core の構成、条件付きの零点実数性、限定された窓の正値性、および有限行列の誤差評価である。小さい窓、有限個の行列、ある数の零点の検算から、全窓への量化を埋めてはならない。

|文献|確認した状態|当プログラムへの扱い|
|---|---|---|
|CC 2021|査読誌掲載、局所 archimedean 定理|仮定を維持して引用可能|
|CC 2023|査読誌掲載、localized form の基礎|core の根拠、全窓正値性とはしない|
|CvS 2025|査読誌掲載、条件付き無限次元定理|本質的自己共役性と ground state 仮定を明記|
|CCM 2025/2026|2025 arXiv、2026 EMS書籍掲載確認|本文の missing steps を保持|
|Suzuki 2026 v3|preprint、査読確認なし|構成・局所定理の候補、global limit は未証明|
|Groskin 2026 v3|preprint、査読・第三者再現確認なし|有限誤差評価の検証候補|
|Zhu 2026 v2|preprint、査読・第三者再現確認なし|固定窓の計算証明主張、依存採用保留|
|Kimほか 2026 v2|数値 preprint|探索の参考、正値性証明にしない|

## 基準となる domain と三種類の極限

加法座標では、\(\widetilde v(x)=\overline{v(-x)}\)、\(Q_W(v)=W(v*\widetilde v)\)。Weil 基準の量化は \(v\in C_c^\infty(\mathbb R)\) **すべて**に対する非負性である。有限窓は \(\operatorname{supp}v\subset[-a,a]\)、乗法窓は \([\lambda^{-1},\lambda]\)、対応は \(a=\log\lambda\)。閉形式は \(L^2\) 上の extended-valued form として扱い、有限な値を持つ form domain と operator domain を混同しない。[Suzuki v3, §1–2](https://arxiv.org/html/2606.09096v3)

次の区別は監査上の数学的整理である。

1. **積分切断 \(T\to\infty\)**: 固定された窓・固定行列サイズで archimedean 積分の尾を復元する。行列添字 \(Q_\infty\) だけでは無限次元作用素を意味しない。
2. **基底サイズ \(N\to\infty\)**: 同じ窓の form core を密にする。CCM Proposition 3.4 により、この極限と最小 Rayleigh 値の対応自体は既知。全 \(N\) について有限形式非負性を証明できれば、同じ窓の非負性に厳密正の一様 gap は不要。有限個 \(N\) の正値性だけでは足りない。
3. **窓 \(a\to\infty\)**: 任意の compact support を覆う。全窓の非負性、または十分な集合の窓の非負性が RH に必要となる。別の spectral route では、自己共役作用素の特性関数を \(\xi\) に同定する局所一様収束が必要である。

有限部分空間 \(V\subset\mathfrak D(Q)\) に対する \(\inf_V Q/\|\cdot\|^2\) は全空間の下端の**上界**である。数値的に正でも下端が負でないとは言えない。一方、厳密な負の trial value は全形式の負性を示す。この方向は Rayleigh 原理から直接従う。

## 一次資料の定理と限界

### CC 2021: archimedean の局所正値性

Alain Connes, Caterina Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Mathematica 27, 77 (2021), DOI [10.1007/s00029-021-00689-4](https://link.springer.com/article/10.1007/s00029-021-00689-4)。

Theorem 1 の正確な条件は \(g\in C_c^\infty(\mathbb R_+^*)\)、support が \([2^{-1/2},2^{1/2}]\)、乗法 Fourier transform が \(i/2\) と \(0\) で消えること。このとき \(W_\infty(g*g^*)\) は Sonin 圧縮の正作用素 trace 以上。加法座標の半幅は \((\log2)/2\)。この定理を任意の大きさの support または任意の有限素数集合へ拡張してはいけない。Theorem 11 は \(|\widehat g(0)|^2\) の補正項を含む。[著者掲載本文](https://alainconnes.org/wp-content/uploads/Selecta.pdf)

査読誌掲載は出版社で確認。独立の証明再構成・数値再現は今回未実施。符号規約 \(W_\infty=-W_{\mathbb R}\) と全 Weil functional の区別を保持する。

### CC 2023 と CCM 2025/2026: 閉形式、core、有限作用素

CC, *Spectral triples and ζ-cycles*, Enseign. Math. 69 (2023), 93–148, DOI [10.4171/LEM/1049](https://ems.press/journals/lem/articles/11033001)。掲載を確認。CCM の Proposition 3.3–3.4 はこの §2／Proposition 2.3 を参照する。

CCM, *Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1)（2025-11-27）。Proposition 3.3 は \(QW_\lambda\) の下半連続性・下有界性、3.4 は \(E=\operatorname{span}\{V_n\}\) の form-core 性と有限切断最小値の極限。Theorem 3.6 は canonical self-adjoint operator の離散下有界 spectrum。**下有界**は**非負**を意味しない。

Theorem 5.10 は固定 \(\lambda,N\) で最小固有値 \(\epsilon_N\) が simple、対応 \(\xi\) が even、\(\delta_N(\xi)=1\) に正規化されることを仮定する。内積は \(QW_\lambda^N-\epsilon_N I\) を quotient \(E_N/\mathbb C\xi\) に下ろしたもの。結論は構成作用素の自己共役性・\(\widehat\xi\) の実零点性。\(\epsilon_N\ge0\) は結論ではない。

§8 は大域の simple-even 条件と ground-state approximation／零点同定の収束を未解決として列挙する。2026 EMS 書籍収録は [出版社目次](https://ems.press/content/book-chapter-files/53351) と [著者書誌](https://alainconnes.org/publications/) で確認。書籍章の個別査読・独立再現の詳細は未確認。

### CvS 2025: 固定窓での無限次元化は条件付きで既知

Connes, Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, Commun. Math. Phys. 406, 312 (2025), DOI [10.1007/s00220-025-05493-1](https://link.springer.com/article/10.1007/s00220-025-05493-1)、[arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1)。出版社の受理日2025-10-14、掲載日2025-11-18を確認。本文も匿名 referee に謝辞。

引用対象は概略版 Theorem 1.2 より精密な **Theorem 6.1**。\([0,L]\) の実 distribution から式(6)で三角多項式上に定まる \(Q\) が下有界かつ本質的自己共役な作用素を定め、最小 spectral value が simple isolated eigenvalue、eigenfunction が \(x\mapsto L-x\) で不変、という条件で、その Fourier transform の全零点が実数となる。

したがって「文献は有限次元の現象しか証明していない」という総括は不正確。ただし ground state の simple-even 条件を全 Weil 窓で証明すること、Fourier transform を \(\xi\) に同定することは別問題。form core と operator core も同一視しない。独立証明再構成は今回未実施。

### Suzuki 2026: v3 の条件を固定して読む

Masatoshi Suzuki, *Weil's quadratic form via the screw function*, DOI [10.48550/arXiv.2606.09096](https://arxiv.org/abs/2606.09096)、[v3本文](https://arxiv.org/html/2606.09096v3)（2026-09-23）。査読掲載は確認できない。

Theorem 1.1: \(A_a\) は \(B_a=D^*G_aD\)、\(\mathfrak D(B_a)=H_0^1(-a,a)\) の Friedrichs 拡張。\(G_a\) は mean-zero \(L^2\) 部分空間への圧縮。Corollary 1.2: \(C_c^\infty(-a,a)\) が Rayleigh 下端を回復。Theorem 1.3: 下端 \(\lambda_a\) の \(a\) に関する連続性。Theorem 1.4: 正値・simple・even は **十分小さい \(a>0\)** について。

Theorem 1.5 の自己共役構成は shift \(T_a=A_a-\lambda I\)、\(\lambda<\lambda_a\) を使用。Corollary 1.6 の条件は、十分大きい \(a\) で \(\lambda(a)<\lambda_a\)、\(\theta(a)\)、上半平面で analytic な \(\phi(a,z)\) を選び、

\[
 e^{\phi(a,z)}W(a,\theta;z)\longrightarrow
 \frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}
\]

が**上半平面の各 compact 上で一様**となること。これは仮定付き RH 含意で、極限成立の証明ではない。§7 の動機づけは RH を仮定する。shift を0に固定できるとの期待を証明済みにしてはいけない。

版注意: 取得した v1 URL には旧式 \(z^2\xi/\xi'\) と全平面 compact が表示された。v3 は上記の別式・別 domain に変更されており、旧式を最新結果として引用しない。

### Groskin 2026: 積分の尾の誤差は有限行列で閉じる

Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, [arXiv:2607.02828v3](https://arxiv.org/html/2607.02828v3)（2026-08-14）。

Theorem 2.5: 固定 \(c>1,N\ge0\)、real-even Galerkin vector の quadratic value と admissible zero sum の等式。\(Q_\infty\) はこの有限行列の積分切断を外したもの。

Theorem 3.2／Corollary 3.3: \(\rho=2\pi/\log c\)、\(T>\max(\rho N,7)\) なら、\(\mathbb C^{\{-N,\ldots,N\}}\) 上で

\[
0\prec Q_\infty-Q_T\preceq B_T I,\qquad
\lambda_j(Q_T)<\lambda_j(Q_\infty)\le\lambda_j(Q_T)+B_T.
\]

\(B_T\asymp(2N+1)\rho\log T/(\pi^2T)\)（\(c,N\) 固定）。従って \(Q_T\succeq0\) はその有限行列の証明になり、\(\lambda_j(Q_T)<-B_T\) は負性の証明候補となる。曖昧帯の左端処理は `proofs/audits/groskin-tail.md` で修正。査読・外部第三者再現は未確認だが、当プログラムでc13,N4の小例を独立再現した。原著401次例・全 \(c,N\) の正値性は認証していない。

### Zhu 2026: 固定窓の拡張主張と明示的撤回

Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, [arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2)（2026-09-02）。査読・独立再現未確認につき当プログラムでは主張の登録に留める。

Theorem 1.1 は \(A_L=\sum_{\log n<2L}2\Lambda(n)/\sqrt n\)、\(\beta^*=\log(T^\sharp/(2\pi))-1/T^\sharp-A_L>0\) の条件下で、有限 head と tail/coupling の厳密評価へ還元する。Theorem 1.2／Corollary 6.3 は \(\operatorname{supp}f\subset[-0.8,0.8]\) の complex \(L^2\) test functions（有限 form 値を持つ domain を含む）に \(Q(f)\ge8.9\times10^{-18}\|f\|_2^2\) と主張。Theorem 6.2 は同じ固定窓の simple-even ground state。計算条件の一例は \(T^\sharp=200,N=200\)、50桁。

**§7 は旧稿の \(L=1.19\) における証明主張を撤回**し、prime-comb bound の向きが誤っていたと説明する。Landau–Widom の定数は empirical fit、Theorem 1.3 は RH 仮定付き。どちらも全窓の非負性証明ではない。

### Kimほか 2026: 数値的研究

Kim, Hong, Kim, Choi, Jang, Shin, Kim, *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator*, [arXiv:2607.24830v2](https://arxiv.org/abs/2607.24830)（2026-07-29）。書誌と abstract を確認しただけで、本文定理監査は今回の対象外。著者ら自身が RH 証明ではないとする数値的研究。査読・独立再現未確認。小固有値、実零点、archimedean law の数値観測を全パラメータの定理として使用しない。

## 当プログラムで埋めるべき証明義務

以下は文献の要約ではなく、主張を依存関係として採用するときの論理点検である。

- \(A_a-c_aI>0\) から \(A_a\ge0\) への逆算には \(c_a\ge0\) 等の別情報が必要。下端より低い負の shift を選べることは一般の下有界作用素でも成立する。
- \(\lambda_a\) が小 \(a\) で正で連続でも、途中で0を通過しないことは未証明。例えば連続関数 \(1-a\) はこの論法への反例。
- 正値な有限 head、正値な tail だけでは cross coupling を処理できない。block \(\begin{pmatrix}1&2\\2&1\end{pmatrix}\) は対角 block が正でも固有値 −1 を持つ。tail/coupling の Schur complement または operator norm 評価が必要。
- Hurwitz を使うには同じ complex domain での局所一様収束と非零 limit の同定が要る。有限個の零点の近接、実軸上の収束、自己共役性だけでは満たさない。
- 正作用素の trace を式に導入した際、その trace と**全** Weil functional が正しい符号・pole terms・prime powers・boundary terms で一致する必要がある。compact error であることだけではその符号は定まらない。

## 探索記録と残る検証

主な検索文字列: `site.arxiv.org Yoshikazu Suzuki Weil quadratic form Riemann hypothesis positivity 2025 2026`、`site.arxiv.org Connes Consani Moscovici finite Weil quadratic forms positivity 2025 2026`、`Quadratic Forms, Real Zeros and Echoes of the Spectral Action`、`Weil positivity and Trace formula Theorem support`。その後、各 arXiv の abs／versioned HTML、Springer／EMS／Wiley の一次出版社ページ、著者公開PDFへ移動した。検索結果の掲載日や二次サイトの説明だけで theorem を採用していない。

未実施: 上記全論文の逐行査読、原著の大規模証明書の完全再計算、最新全投稿の網羅検索、original Weil/Yoshida 論文との全規約照合。Groskinの有限辞書・tailと小例、独立実装の固定小窓は監査を追加済み。Zhu原著の200次headは未取得。次はjoint symbol h(t)−prime combの区間下界と、定数comb envelopeの限界を切り分ける。CvSのoperator-coreとglobal limit同定は未解決のまま。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/groskin-tail.md`](../../../audits/proofs/audits/groskin-tail.md)
- [`proofs/audits/window-half-certificate.md`](../../../audits/proofs/audits/window-half-certificate.md)
