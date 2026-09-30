**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_complex/notes/literature.md` · Original SHA-256: `236bc89d78197d2bca4bde8421c26f49fd52ad6009272bd0574ab4e47849fc42`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime Complex Parity Pairing：限定一次文献監査

2026-09-30。対象は \(X\ge2\) と
\[
\Delta_X=\{F:\ F\text{ は有限素数集合},\ \prod_{p\in F}p\le X\}
\]
で、空集合も含む。新規性を主張しない。既存ファイルは変更しない。

## 固定した資料と使用箇所

| 資料 | 版・一次 URL | 今回確認した locator と範囲 |
|---|---|---|
| Anders Björner, *A cell complex in number theory* | [arXiv:1101.5704v1](https://arxiv.org/html/1101.5704v1), 2011-01-29；[PDF](https://arxiv.org/pdf/1101.5704v1)；査読誌 DOI [10.1016/j.aam.2010.09.007](https://doi.org/10.1016/j.aam.2010.09.007)（arXiv 書誌では online 2010-10-20） | §1 Eqs.(1.1)–(1.2)：reduced Euler 規約。Thm.2.1, pp.3–4：shifted complex の wedge 型と最小頂点による Betti 公式。Thm.3.1, p.5：本 \(\Delta_X\) の正確な公式。Thm.3.4, pp.5–6：Betti 総数。Thm.3.5, p.6：偶数・奇数次 Betti 総数の漸近。 |
| Oliver Knill, *On Primes, Graphs and Cohomology* | [arXiv:1608.06877v1](https://arxiv.org/html/1608.06877v1), 2016-08-22（本文 date 2016-08-20） | §§1.1, 3.1–3.4, 4.2：squarefree 整数の divisibility graph、\(\chi=1-M\)、Poincaré–Hopf index。今回は preprint の該当 statement を照合し、査読状況は未確認。 |
| Robin Forman, *A User's Guide to Discrete Morse Theory* | Sém. Lothar. Combin. **48** (2002), B48c, [掲載 PDF](https://www.mat.univie.ac.at/~slc/wpapers/s48forman.pdf) | Thm.2.5, p.10：critical simplices による CW 模型。Thm.2.11, p.13：weak Morse inequalities。Thms.6.2–6.3, p.22：acyclic Hasse matching と空集合の規約。著者自身による理論の解説であり、今回その全証明は再監査していない。 |

Björner Thm.2.1 が指す原始文献は Björner–Kalai, *An extended Euler-Poincaré theorem*, Acta Math. **161** (1988), 279–303, p.292。この原始文献自体の全文は今回未照合。使用 statement は Björner の上記指定版で確認した。頁はそれぞれの掲載 PDF の本文頁。

## 既知の正確な結論

\(\widetilde\beta_k=\operatorname{rank}\widetilde H_k(\Delta_X;\mathbb Z)\) とする。Björner の \(\chi,\beta\) は reduced 規約である。
\[
M(X)=-\widetilde\chi(\Delta_X)
=-\sum_{k\ge0}(-1)^k\widetilde\beta_k .
\tag{1}
\]
小さい素数への置換は積を減らすため \(\Delta_X\) は shifted。上記 Thms.2.1, 3.1 は
\[
\Delta_X\simeq\bigvee_{k\ge0}\bigvee^{\,\widetilde\beta_k}S^k,\qquad
\widetilde\beta_k
=\#\{b:\ X/2<b\le X,\ b\text{ odd squarefree},\ \omega(b)=k+1\}.
\tag{2}
\]
Thm.3.4 は無条件に
\[
B(X):=\sum_k\widetilde\beta_k
=\frac{2X}{\pi^2}+O_\theta(X^\theta)
\quad\text{for every }\theta>17/54.
\tag{3}
\]
Thm.3.5 では偶数次・奇数次の総数が各 \(X/\pi^2\) に漸近する。その差の RH 級評価は供給しない。整数で述べられた結果は \(\Delta_X=\Delta_{\lfloor X\rfloor}\) により実数 \(X\) へ移せる。

符号上の小注意：指定版 Thm.3.5 証明の \(a-b=M\) は Eq.(1.2) と逆符号で、ここでは \(a-b=-M\) を使う。漸近結論は変わらない。Knill §3.4 にも index を一度 \(\mu\) とする文があるが、§1.1・同節末尾の \(-\mu\) と整合する規約を採る。素数追加の index は \(+1=-\mu(p)\) なので直接確認できる。

## 今回の直接検算と文献結果の一致

素数 \(2\) を含まない \(F\) で \(2\prod F\le X\) のとき
\[
F\longleftrightarrow F\cup\{2\}
\tag{4}
\]
と組にする。augmented face poset では \(\varnothing\leftrightarrow\{2\}\) も含む。残余は (2) の odd squarefree \(b\in(X/2,X]\) と正確に一致する。

この matching の acyclicity は直接分かる。matched edge を上向き、他の inclusion edge を下向きにしたとき、上向き移動は \(2\) の追加だけ。いったん \(2\) を含む面へ入ると \(2\) を除く辺は matched edge の逆向きなので進めず、再び上向き移動もできない。残る移動は次元を減らすため閉路はない。

さらに \(C=\operatorname{star}_{\Delta_X}(2)=\{F:F\cup\{2\}\in\Delta_X\}\) は cone である。残余面 \(F\) の積を \(b\) とすると、全 proper faces は素数 \(p\ge3\) を少なくとも一つ除くので積が \(b/p\le X/3<X/2\)。したがって全境界が \(C\) に入る。contractible subcomplex \(C\) を潰すと各残余面が一つの球面になり、(2) が得られる。これは既知公式の今回の直接確認であり、新定理ではない。

通常の非空 face poset の Morse 規約では (4) から空集合の組を外すので、\(\{2\}\) が基点の critical 0-cell として残る。critical 数は \(1+B(X)\)、reduced の数は \(B(X)\)。この \(+1\) を落とさない。

線形主項だけなら初等的にも検算できる。odd squarefree 計数 \(Q_{\rm odd}(Y)\) について
\[
Q_{\rm odd}(Y)
=\sum_{\substack{d\le\sqrt Y\\d\text{ odd}}}\mu(d)
 \#\{r\le Y/d^2:r\text{ odd}\}
=\frac{Y}{2}\prod_{p>2}(1-p^{-2})+O(\sqrt Y)
=\frac{4Y}{\pi^2}+O(\sqrt Y).
\]
従って \(B(X)=Q_{\rm odd}(X)-Q_{\rm odd}(X/2)=2X/\pi^2+O(\sqrt X)\)。強い誤差指数 \(17/54\) の数論的証明は今回再証明していない。

## Divisor graph と、排除できる戦略の範囲

Knill の graph \(G(X)\) の頂点は squarefree な \(2\le b\le X\)、辺は一方が他方を割る組である。その clique complex は非空 faces の inclusion chain を表すため \(\Delta_X\) の barycentric subdivision に一致する。従って ordinary Euler 規約では \(\chi(G(X))=1-M(X)\)。これは (1) と整合する。

一方、「素数を頂点、\(pq\le X\) を辺」とした graph の clique completion は一般に \(\Delta_X\) ではない。例えば \(X=15\) で \(\{2,3\},\{2,5\},\{3,5\}\) の全辺は存在するが、triple product \(30\) は cutoff を越える。flag completion はこの cycle を三角形で埋め、元の複体を変える。divisor order complex とこの別の flag complex を混同しない。

Forman の weak Morse inequalities と (2)–(3) により、同じ \(\Delta_X\) の acyclic face matching では critical 数を各次数の Betti 数より減らせない。(4) は既にその下界を達成している。したがって homotopy/homology を保つ通常の discrete Morse cancellation によって、reduced critical 総数を \(o(X)\)、特に \(O_\varepsilon(X^{1/2+\varepsilon})\) へ減らす戦略は失敗する。

これは任意の符号反転 involution や、homology を保たない arithmetic parity pairing 全般を反証するものではない。残余の符号和は依然として \(M(X)\) そのものであり、正・負の個数がそれぞれ線形であることから、その差の平方根級 cancellation は出ない。

**Decision:** 複体、Euler–Mertens 対応、shifted/wedge 型、素数 \(2\) の残余と Betti 総数の線形漸近は既知として固定する。今回の直接検算はその再確認と規約の整理。Morse matching の残余個数を小さくする路線は上記範囲で排除できるが、新しい arithmetic cancellation、RH の証明、新規性はいずれも得ていない。限定探索はここで終了。
