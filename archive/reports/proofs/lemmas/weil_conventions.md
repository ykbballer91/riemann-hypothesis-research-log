**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/lemmas/weil_conventions.md` · Original SHA-256: `21a806f290cc2808e22dba784e905650c78523763a60b86907aa62dbebb71728`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weil 形式の正規化と既知入力

作成日: 2026-09-29。担当: BUILDER / SYMBOLIC ANALYST。
状態: 定義と変換計算は `PROVED`、Weil 判定法と明示公式は `KNOWN`。
このファイルには RH の新しい証明は含まれない。

## 1. 零点、多重度、Fourier 変換

非自明零点の多重集合を \(Z\) とする。以降の \(\sum_{\rho\in Z}\) は多重度を含む。零点の単純性は仮定しない。

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\rho=\beta+i\gamma,\qquad z_\rho=\frac{\rho-1/2}{i}
=\gamma-i(\beta-1/2).
\]

既知の零点の帯 \(0<\beta<1\) から \(|\Im z_\rho|<1/2\) である。
関数等式と実係数対称性により、\(\rho\mapsto1-\bar\rho\) は多重度を保存し、
\(z_{1-\bar\rho}=\bar z_\rho\) となる。\(\gamma\) は実数の零点高度であり、複素数 \(z_\rho\) と混同しない。

\(f,g\in\mathcal D=C_c^\infty(\mathbb R;\mathbb C)\) に対し

\[
F_f(z)=\int_{\mathbb R}f(x)e^{izx}\,dx,
\quad \widetilde g(x)=\overline{g(-x)},
\quad (f*g)(x)=\int_{\mathbb R}f(y)g(x-y)\,dy
\]

と定める。\(F_f\) は entire である。コンパクト台上の微分・積分交換で
\(F_f^{(k)}(z)=\int (ix)^k f(x)e^{izx}dx\) が成立する。

Fubini を適用する積分はコンパクト台上なので絶対可積分であり、

\[
F_{f*g}(z)=F_f(z)F_g(z),\qquad
F_{\widetilde g}(z)=\overline{F_g(\bar z)}. \tag{1}
\]

後者は \(x=-y\) と置換した後、積分の複素共役を取れば得られる。
とくに \(F_f(z)\overline{F_f(\bar z)}\) を \(|F_f(z)|^2\) と置き換えてよいのは、一般には \(z\in\mathbb R\) の場合だけである。

## 2. Mellin 変換との正確な対応

\[
a_f(t)=t^{-1/2}f(\log t),\qquad
\mathcal M a(s)=\int_0^\infty a(t)t^{s-1}dt
\]

とする。\(a_f\in C_c^\infty((0,\infty))\) であり、\(t=e^x\) より

\[
\mathcal M a_f(s)
=\int_{\mathbb R}f(x)e^{(s-1/2)x}dx
=F_f\!\left(\frac{s-1/2}{i}\right). \tag{2}
\]

乗法畳み込みと共役反転を

\[
(a*_\times b)(t)=\int_0^\infty a(u)b(t/u)\frac{du}{u},
\qquad a^\sharp(t)=t^{-1}\overline{a(t^{-1})}
\]

と定めると、直接代入によって

\[
a_{f*g}=a_f*_\times a_g,\qquad
a_{\widetilde g}=a_g^\sharp,\qquad
\mathcal M(a^\sharp)(s)=\overline{\mathcal M a(1-\bar s)}. \tag{3}
\]

これにより、中心化 Fourier 形式と Mellin 形式の対応は

\[
\begin{aligned}
Q(f,g)
&:=\sum_{\rho\in Z}F_f(z_\rho)\overline{F_g(\bar z_\rho)}\\
&=\sum_{\rho\in Z}\mathcal M a_f(\rho)
              \overline{\mathcal M a_g(1-\bar\rho)}\\
&=\sum_{\rho\in Z}\mathcal M(a_f*_\times a_g^\sharp)(\rho).
\end{aligned} \tag{4}
\]

各級数の絶対収束と並べ替えの正当性は `finite_to_infinite.md` の補題 F2 による。
Connes–Consani の Appendix B では、複素共役なしの反転にも類似記号を使用しているため、本稿の \(\sharp\) と無条件に同一視しない。

## 3. 明示公式の算術側

\(h\in\mathcal D\) に対し \(W(h)=\sum_{\rho\in Z}F_h(z_\rho)\) とする。
この単独の零点和も絶対収束する。実際、固定帯で \(F_h(z)=O((1+|\Re z|)^{-2})\) であり、零点計数の \(O(T\log T)\) と組み合わせればよい。

Weil 明示公式の本稿の規約は

\[
\begin{aligned}
W(h)={}&\int_{\mathbb R}h(x)(e^{x/2}+e^{-x/2})dx\\
&-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \{h(\log n)+h(-\log n)\}\\
&-(\log(4\pi)+\gamma_E)h(0)\\
&-\int_0^\infty
 \{h(x)+h(-x)-2e^{-x/2}h(0)\}
 \frac{e^{x/2}}{e^x-e^{-x}}dx .
\end{aligned} \tag{5}
\]

ここで \(\Lambda\) は von Mangoldt 関数、\(\gamma_E\) は Euler 定数である。
素数冪和は \(h\) のコンパクト台により有限である。最後の積分では、原点付近の中括弧が \(xh(0)+O(x^2)\)、係数が \((2x)^{-1}+O(1)\) であり、被積分関数は有界である。台の外では被積分関数は \(-2h(0)/(e^x-e^{-x})=O(e^{-x})\) となる。
したがって原点と無限遠のいずれも通常の絶対収束積分であり、正則化記号は不要である。

式 (5) は [CC2021] Appendix B (148)–(151) に \(a_h(t)=t^{-1/2}h(\log t)\) を代入して得る。零点以外の項、とくに \(s=0,1\) に由来する最初の積分を削除してはいけない。
同一の加法座標の式は [S2026v3] §1.1 に明記されている。
式 (1) によって

\[
Q(f,g)=W(f*\widetilde g). \tag{6}
\]

## 4. Hermitian 性と RH 依存の位置

\(Q\) は第1変数に線形、第2変数に共役線形である。絶対収束した式 (4) で \(\rho\mapsto1-\bar\rho\) と添字を置換すると

\[
\overline{Q(g,f)}
=\sum_\rho \overline{F_g(z_\rho)}F_f(\bar z_\rho)
=Q(f,g). \tag{7}
\]

したがって \(Q(f,f)\in\mathbb R\) は無条件である。

RH を仮定すると \(z_\rho\in\mathbb R\) なので

\[
Q(f,f)=\sum_{\rho\in Z}|F_f(z_\rho)|^2\ge0. \tag{8}
\]

この式を RH を仮定せずに書くことは循環論法である。臨界線外の対 \(z,\bar z\) の寄与は

\[
2\operatorname{Re}\{F_f(z)\overline{F_f(\bar z)}\}
\]

であり、符号は固定されていない。この局所的な事実だけでは、他の零点の寄与を含む全和が負になるテスト関数を構成したことにはならない。

既知の Weil 判定法を、ここでは次の正確な入力として使用する。

> **W1 (`KNOWN`; 同値性そのものは無条件)**:
> \(\mathrm{RH}\iff [\forall f\in C_c^\infty(\mathbb R;\mathbb C),\ Q(f,f)\ge0]\)。

右辺の命題の状態は `EQUIVALENT-TO-RH / OPEN` であり、証明済みの正値性として扱わない。
本ファイルは十分性の歴史的証明を新しく再証明していない。
現在のテスト空間での正確な定式化は [S2023] §3.2 (3.3)–(3.5) と [S2025] §1 を確認した。
Weil の1952年原論文を現代の \(C_c^\infty\) 版と逐語的に一致するものとして引用しない。

## 5. 文献照合の記録

- **CC2021**: Alain Connes and Caterina Consani, *Weil positivity and Trace formula, the archimedean place*, 著者公開版、表紙日付2021-07-04。照合箇所: Appendix B, (148)–(151), PDF p.47。使用内容: Mellin 規約と明示公式。RH依存: NO。
  [著者公開PDF](https://alainconnes.org/wp-content/uploads/Selecta.pdf)
- **S2023**: Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta function*, arXiv:2206.03682v4, 2023-05-30; J. Lond. Math. Soc. 108 (2023), 1448–1487。照合箇所: §3.2, (3.3)–(3.5)。使用内容: \(C_c^\infty\) 版 Weil 判定法の定式化。RH依存: 同値性は NO、正値性の成立は RH 同値。
  [版本固定本文](https://arxiv.org/pdf/2206.03682v4)
- **S2025**: Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*, Canadian Journal of Mathematics, published online 2025-11-03, DOI 10.4153/S0008414X25101739。照合箇所: §1, (1.1), (1.2), §3.1 (3.3)。同論文は \(\xi(1/2-i\gamma)=0\) を用い \(\widehat f(-\gamma)\) と書く。本稿の \(z_\rho=-\gamma\) に対応する。Hilbert 空間同型の Theorem 1.1 は RH を仮定し、本稿の無条件補題の根拠には使用しない。
  [出版社本文](https://doi.org/10.4153/S0008414X25101739)
- **S2026v3**: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, 2026-09-23, PREPRINT。照合箇所: §1.1 と (3.1)。使用内容: 規約の独立照合のみ。後段の予想的極限公式は本稿で使用しない。
  [版本固定本文](https://arxiv.org/html/2606.09096v3)
- **W1952**: André Weil, *Sur les “formules explicites” de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund, supplément (1952), 252–265。原論文書誌を確認。原版の全文の独立監査は未完了であり、現代版判定法の細部は上記の研究論文本文で照合した。
  [書誌記録](https://cds.cern.ch/record/471308)

独立に再計算した範囲: (1)–(4)、(5) の変数変換と端点収束、(6)–(8)。
文献定理として受け入れた範囲: Weil 明示公式そのもの、Weil 判定法の正値性から RH への含意。

書誌監査追記: S2023 は versioned PDF の表紙 Version of May 31, 2023 と arXiv header 30 May 2023 を照合。HTML側の2026本文日付は引用しない。
