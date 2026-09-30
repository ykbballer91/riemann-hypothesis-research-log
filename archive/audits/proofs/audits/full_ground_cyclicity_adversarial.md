**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/full_ground_cyclicity_adversarial.md` · Original SHA-256: `139adc9253baeefc86a708127d1ab51d4af388f661bacdee326d8d933f21a536`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Even derivative cyclicity — 独立敵対監査

**STATUS: RIEMANN HYPOTHESIS OPEN**

2026-09-30。Priority 1 のみ。既存研究ファイルと公開準備 audit は変更しない。
本書は内部の独立AI監査であり、外部査読・Lean形式検証・新規性認証ではない。

## 1. 判定と対象

**PASS：** 実際の theta 核を
\[
 \widehat k(x)=\int_{\mathbb R}k(t)e^{-ixt}\,dt=\Xi(x)/4,
 \qquad \Xi(x)=\xi(1/2+ix)
\]
と固定すると、無条件に
\[
 \overline{\operatorname{span}_{\mathbb C}\{k,k'',k^{(4)},\ldots\}}^{L^2(\mathbb R)}
 =L^2_{\rm even}(\mathbb R).
 \tag{1}
\]
実係数・実Hilbert空間でも同じ結論となる。
これは **L²ノルムでの稠密性だけ** であり、Weil形式のcore性・閉包可能性・正性、
全有限空間のground捕捉、G*、RHを結論しない。

## 2. RHを使わない指数モーメント

固定した \(\sigma=1/2\) でEuler summationを
\(N=\lceil |t|\rceil+1\) に適用すると
\[
 \zeta(\sigma+it)
 =\sum_{n\le N}n^{-\sigma-it}
  +\frac{N^{1-\sigma-it}}{\sigma+it-1}
  +O_\sigma((1+|t|)N^{-\sigma}).
\]
従って \(|\zeta(1/2+it)|\le C(1+|t|)^{1/2}\)。小さい \(t\) はcompact上の連続性で吸収できる。
Stirling評価と
\(|(1/2+it)(-1/2+it)|=t^2+1/4\) から
\[
 |\Xi(t)|\le C(1+|t|)^{9/4}e^{-\pi|t|/4}.
 \tag{2}
\]
ここでconvexity bound、零点の位置、単純性は不要である。
\(d\mu(x)=|\Xi(x)|^2dx\) と置くと、任意の \(0<\delta<\pi/2\) について
\[
 \mu(\mathbb R)<\infty,
 \qquad \int e^{\delta|x|}\,d\mu(x)<\infty.
 \tag{3}
\]
endpoint \(\delta=\pi/2\) の可積分性はこの評価から主張しない。

## 3. Polynomial density の直接証明

一般に有限正測度 \(\nu\) が (3) を満たすとする。
\(h\in L^2(\nu)\) が全多項式に直交するなら
\[
 H(z)=\int_{\mathbb R}\overline{h(x)}e^{izx}\,d\nu(x)
 \tag{4}
\]
は \(|\operatorname{Im}z|<\delta/2\) で正則である。
実際、各compact substripと各 \(r\ge0\) に対しCauchy–Schwarzを使うと
\(\int |h(x)||x|^r e^{b|x|}\,d\nu(x)<\infty\)（\(2b<\delta\)）。
余裕のある指数に多項式を吸収でき、積分内微分が正当化される。

全ての \(H^{(r)}(0)=i^r\int\overline h x^r\,d\nu=0\) なので恒等定理より
\(H\equiv0\)。有限複素測度 \(\overline h\,\nu\) のFourier変換の一意性から
\(\overline h\,\nu=0\)、従って \(h=0\) \(\nu\)-a.e. である。
これにより全多項式は \(L^2(\nu)\) に稠密である。
Fourier一意性は、例えばGaussian approximate identityとの畳込みが全て0となることからも従う。

本件の \(\mu\) は偶測度なので、
\(P_{\rm ev}f(x)=(f(x)+f(-x))/2\) は直交射影である。
任意のeven \(h\) の多項式近似を \(P_{\rm ev}\) で射影すると
\[
 \overline{\mathbb C[x^2]}^{L^2(\mu)}=L^2_{\rm even}(\mu).
 \tag{5}
\]
**全 \(L^2(\mu)\) に \(\mathbb C[x^2]\) が稠密とは言えない。**
例えば非零の奇関数 \(x\in L^2(\mu)\) は全even polynomialに直交する。
Hamburger決定性からの一般定理を省略して使う必要はなく、(4)だけで本件は完結する。

## 4. 零点と乗算逆写像

\(\Xi\) は恒等的に0でないentire関数である。その実軸上の零点は離散で、Lebesgue零測度を持つ。
これは全非自明零点が実軸上にあるという主張ではなく、RHを仮定しない。

乗算写像
\[
 M_\Xi:L^2(\mu)\longrightarrow L^2(dx),\qquad h\longmapsto\Xi h
 \tag{6}
\]
は \(\|\Xi h\|_2^2=\int|h|^2d\mu\) を満たすonto isometryである。
任意の \(g\in L^2(dx)\) に対して、零点以外で \(h=g/\Xi\)、零点で任意に0と置けば
\(\|h\|_{L^2(\mu)}=\|g\|_2\)。零点付近で \(g/\Xi\) がunboundedでも障害ではない。
この逆写像を **unweighted L² 上のbounded division operator** と読み替えてはいけない。
\(\Xi\) が偶なので (6) はeven sectorもontoに保つ。

非unitary Fourier規約に対するPlancherelは
\(\|\widehat f\|_2^2=2\pi\|f\|_2^2\) である。
unitary写像 \(\mathcal U f=(2\pi)^{-1/2}\widehat f\) を用いると
\[
 \mathcal U(k^{(2j)})(x)
 =\frac{(-1)^jx^{2j}\Xi(x)}{4\sqrt{2\pi}}.
 \tag{7}
\]
全ての微分はL²に属する。これはtheta表示の急減少、または (2) と微分のFourier対応から従う。
(5)–(7)より (1) が成立する。共通因子 \(1/4\) とFourierの \(2\pi\) は稠密性を変えないが、
等長写像の式から省略しない。

## 5. Carleman補助検算

\(c=\pi/2\)、\(m_{2n}=\int x^{2n}d\mu(x)\) とする。
(2) の平方と \((1+x)^{9/2}\le C(1+x^5)\) により
\[
 m_{2n}\le C\left\{\frac{\Gamma(2n+1)}{c^{2n+1}}
              +\frac{\Gamma(2n+6)}{c^{2n+6}}\right\}
 \le C'\frac{\Gamma(2n+6)}{c^{2n+6}}.
 \tag{8}
\]
したがって
\[
 \liminf_{n\to\infty}n\,m_{2n}^{-1/(2n)}\ge\frac{e\pi}{4},
 \qquad \sum_{n\ge1}m_{2n}^{-1/(2n)}=\infty.
 \tag{9}
\]
(8)からは \(\sim\) の等号漸近を導かない。密度証明は (9) やmoment問題の決定性を経由せずに済む。

Builder提示の精密漸近については、指定された平均二乗誤差
\[
 E(T)=\int_0^T|\zeta(1/2+it)|^2dt
       -T\log(T/(2\pi))-(2\gamma-1)T
 =O(T^{1/3}\log^{5/3}(2+T))
 \tag{10}
\]
を入力した後の定数と式変形を独立確認した。
\(v=2n+9/2\)、\(a=\pi/2\) とすれば
\[
 m_{2n}=\sqrt{2\pi}\,\Gamma(v)a^{-v}
 \left[\psi(v)+2\gamma-\log(\pi^2)
       +O(v^{-1/6}\log^2v)\right].
 \tag{11}
\]
両側積分の係数は \(\sqrt{2\pi}\)、Stirling後の冪は \(t^{2n+7/2}\) である。
\(X\sim\mathrm{Gamma}(v,\text{rate }a)\) について
\[
 \mathbb E\left[\left((v-1)/X-a\right)^2\right]=a^2/(v-2)
\]
とCauchy–Schwarzを使うと (10) の寄与は上記誤差以内となる。
Gamma因子の相対 \(O(t^{-1})\) 誤差は別途 \(O((\log v)/v)\) に収まる。
従って (10) を採用すれば \(m_{2n}^{-1/(2n)}\sim e\pi/(4n)\)。
**(10) の必要な原定理statementは今回直接確認済みである。**
その読取範囲と、全原論文の証明を再検証してはいないという限定を§8に記録した。
(1)はこの追加入力に依存しない。

## 6. 証明された閉包の限界

L²近似の係数・必要次数・誤差率は本証明から得られない。
固定有限 \(m\) の選択定理を \(m\to\infty\) に一様化することも、
\(a,N,m\) の極限順序を交換することもできない。
正規化Fourier変換の複素strip上の収束や、全Weil行列のgroundとの比較も別の義務である。

零点拘束が帰結しないことは、限定された合成例でも確認できる。
\(q(x)=(x^2+1)e^{-x^2}\) は実偶・Schwartzで実軸上非零、
\(|q|^2dx\) は全ての正の指数momentを持つが、\(q(z)\) は \(z=\pm i\) に零点を持つ。
\(\widehat h=q\) と定めた実偶Schwartz関数 \(h\) に同じ証明を適用すると、
\(\{h^{(2j)}\}\) もeven L²でcyclicである。
これはcyclicityから一般に実零点性を推論する規則の反例であり、
actual theta・Euler/Gamma規約を保持する例でも、RHの反例でもない。

一般にL²で稠密でもform coreとは限らない。例えば
\(q(f)=\|f'\|_2^2\)、\(D(q)=H^1(0,1)\) は非負閉形式だが、
\(C_c^\infty(0,1)\) はL²で稠密であってもform norm閉包は \(H_0^1(0,1)\) にとどまる。
これは一般論の限定反例であり、実際のWeil形式の反例とはしない。

さらに、各 \(k^{(2j)}\) のcomplex zero evaluationが消えることと (1) は矛盾しない。
それらのevaluationは本件のunweighted L²ノルムで連続な汎関数ではない。
Weil形式の既存radical恒等式をL²閉包へ無条件に移送して、
形式全体が0、正、あるいは閉じると推論してはいけない。

## 7. 監査状態

| 項目 | 判定 |
|---|---|
| 指数モーメントと直接 polynomial density | PASS・無条件 |
| even sectorでの \(x^2\) polynomial density | PASS |
| weighted乗算のonto性とFourier因子 | PASS |
| (8)–(9) のCarleman上界・発散 | PASS |
| 精密moment式 (11) の導出 | PASS。入力statementの一次確認範囲は§8参照 |
| L²稠密性からform core・全ground捕捉・G*へ | NOT ESTABLISHED |
| RH | OPEN |

## 8. 最終稿の通読監査と固定snapshot

2026-09-30、rootの `research/full_ground_capture/cyclicity.md` を全節通読した。
補助note `moment_asymptotic.md` のMA14–25、`moment_problem_sources.md` のM3–M6も
読み取りで照合した。**最終判定：PASS。重大な未修正の数式誤り・過大主張は検出しなかった。**

主稿の粗いEuler積分 (5) は \(\zeta(1/2+it)=O(1+|t|)\) を正当に与える。
従ってその (6) の冪 \(11/2\)、(8) のGamma引数 \(2n+13/2\)、
(9) の余裕付き下界 \(ce/(4n)\) は整合する。
本監査§2のやや強い初等上界と矛盾するものではなく、どちらでもcyclicityは閉じる。

主稿 (4) の片側係数 \(\sqrt{\pi/2}\)、(11) の両側係数 \(\sqrt{2\pi}\)、
\(v=2n+9/2\)、\(-\log\pi^2\)、(12) の \(\pi e/(4n)\) を確認した。
最終稿のStirling誤差は \(O(t^{-1})\) に統一され、正規化momentへの寄与は
\(O(v^{-1}\log v)=o(1)\) と正しく記載されている。

追加入力は [Simonič–Starichkova, arXiv:2105.06821v3](https://arxiv.org/html/2105.06821v3)
の式(1)、Corollary 1・式(15)、§7 Theorem 3を今回直接読んだ。
固定 \(T_0\ge10^{30}\)、\(T\ge1.1T_0\) での無条件上界
\(|E(T)|\le C(T_0)T^{1/3}\log^{5/3}T\) がstatementに含まれる。
従って \(E(T)=O((1+T)^{5/12})\) への弱化と
MA14の \(O(v^{-1/12})\) は正当である。主稿の固定 \(0<\delta<1/6\) から得る
\(o(1)\) も同様に正しい。原論文全証明の再証明・機械検証をしたとは主張しない。

唯一の文言指摘は§2見出しの「必要十分な上界」であり、**「十分な上界」へ修正済み**。
指数moment条件の必要性は証明対象ではない。
主稿はeven sector、weighted逆写像、非unitary Fourier定数、
定性的L²閉包と未着手の有限head・uniform rate・full groundを明確に分けている。
RH独立性とPriority 1での停止範囲も適切である。

監査対象のSHA-256（source rootからの相対path）：

| ファイル | SHA-256 |
|---|---|
| `research/full_ground_capture/cyclicity.md` | `52507e842fee06329585b2ecc46c9b91ab9619b619fbd4c163a5b2237103935e` |
| `research/full_ground_capture/notes/moment_asymptotic.md` | `f633625f109e913be7f21dc91e7df35b69a3405e94b314191a164e9126a7c6ec` |
| `research/full_ground_capture/notes/moment_problem_sources.md` | `c9979e20369490291872eb777965d65ae80aaefb33b48df7f456454d0211ce98` |

編集したのは本新規auditだけである。既存研究・state・proof graph・公開準備auditは変更せず、
Priority 2以降の研究や数値実験を開始していない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/full_ground_capture/cyclicity.md`](../../../reports/research/full_ground_capture/cyclicity.md)
- [`research/full_ground_capture/notes/moment_asymptotic.md`](../../../reports/research/full_ground_capture/notes/moment_asymptotic.md)
- [`research/full_ground_capture/notes/moment_problem_sources.md`](../../../reports/research/full_ground_capture/notes/moment_problem_sources.md)
