**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/lemmas/kernel_optimization_barrier.md` · Original SHA-256: `724461b130ec5d5386a33eaa0bf3bd735af579ffb6e0d6deef7ecf519051924d`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定支持の二次モーメント核における最適定数

作成日: 2026-09-29。担当: BUILDER / SYMBOLIC ANALYST。
状態: `PROVED`。既知の Montgomery–Taylor 最適定数の初等的な再導出であり、新規性は主張しない。
RH の証明や、RH の証明全般に対する不可能性定理ではない。

## K0. 検討する変分問題

\(I=[-1/2,1/2]\) とし、実 Hilbert 空間 \(L^2(I;\mathbb R)\) 上で

\[
\mathcal C(f)=\int_I f(x)^2dx+
 \int_I\int_I |x-y|f(x)f(y)dxdy,\qquad \int_I f(x)dx=1
\]

を最小化する。\(|I|=1\) なので \(L^2(I)\subset L^1(I)\)。また \(|x-y|\le1\) より二重積分は絶対収束する。
偶関数性や非負性を課さない、より大きなクラスで証明する。

\[
a=1/\sqrt2,\qquad
f_0(x)=\frac{\cos(\sqrt2x)}{\sqrt2\sin a},\quad x\in I,
\qquad C_{\rm MT}=\frac12+\frac{\cot a}{\sqrt2}
\]

と置く。\(f_0\) を区間外でゼロ延長すると端点で不連続であり、\(C_c^\infty((-1/2,1/2))\) の元ではない。
この点は極限処理で明示的に扱う。

## K1. 平均ゼロ部分空間での強制的正値性

**補題.** \(h\in L^2(I;\mathbb R)\)、\(\int_I h=0\) とする。
\(H(x)=\int_{-1/2}^x h(y)dy\) と置くと

\[
\mathcal C(h)=\|h\|_2^2-2\|H\|_2^2
\ge\frac23\|h\|_2^2. \tag{1}
\]

**証明.** \(H\) は絶対連続、\(H'=h\) a.e.、\(H(-1/2)=H(1/2)=0\) である。
\(V(x)=\int_I |x-y|h(y)dy\) とすると、差商の絶対値は \(|h(y)|\) で支配でき、

\[
V'(x)=\int_{-1/2}^x h(y)dy-\int_x^{1/2}h(y)dy=2H(x)
\]

が成り立つ。弱微分としても同一である。
よって絶対連続関数の部分積分から

\[
\int_I\int_I |x-y|h(x)h(y)dxdy
=\int_I H'(x)V(x)dx
=[H(x)V(x)]_{-1/2}^{1/2}-\int_I H(x)V'(x)dx
=-2\|H\|_2^2.
\]

ここで平均ゼロ条件により境界項が厳密に消える。
\(t=x+1/2\in[0,1]\) と書けば

\[
H(x)=\int_I h(y)\{\mathbf1_{[-1/2,x]}(y)-t\}dy.
\]

括弧の \(L^2\) ノルムの二乗は
\(t(1-t)^2+(1-t)t^2=t(1-t)\) なので Cauchy–Schwarz により

\[
|H(x)|^2\le \|h\|_2^2t(1-t),\qquad
\|H\|_2^2\le\|h\|_2^2\int_0^1t(1-t)dt=\tfrac16\|h\|_2^2.
\]

これを前式に代入すれば (1) を得る。∎

\(2/3\) はこの安定性評価に十分な係数である。その係数自体の最適性は主張しない。

## K2. 最小化関数の同定と安定性

**定理.** \(\int_I f=1\) を満たす全ての実 \(f\in L^2(I)\) に対し

\[
\boxed{\mathcal C(f)-C_{\rm MT}
 =\mathcal C(f-f_0)
 \ge\frac23\|f-f_0\|_2^2.} \tag{2}
\]

従って \(f_0\) は唯一の最小化関数（a.e. の同一視）であり、最小値は \(C_{\rm MT}\) である。

**証明.** 直接積分で

\[
\int_I f_0(x)dx
=\frac{2\sin(\sqrt2/2)}{2\sin a}=1.
\]

\(T\) を実対称な有界作用素

\[
(Tf)(x)=f(x)+\int_I|x-y|f(y)dy
\]

とする。有界性は、例えば核の絶対値が1以下であることと Cauchy–Schwarz から従う。
\(\mathcal C(f)=\langle f,Tf\rangle\) である。

\(f_0''=-2f_0\)、また \(V_0(x)=\int_I|x-y|f_0(y)dy\) は \(V_0''=2f_0\) を満たす。
従って \((Tf_0)''=0\) であり、\(Tf_0\) は区間上で affine な関数となる。
\(f_0\) は偶関数、核は反射 \((x,y)\mapsto(-x,-y)\) に不変なので \(Tf_0\) も偶関数である。
ゆえに \(Tf_0\) は定数である。その値を端点で計算すると

\[
\begin{aligned}
(Tf_0)(1/2)
&=\frac{\cos a}{\sqrt2\sin a}
 +\int_I(1/2-y)f_0(y)dy\\
&=\frac{\cot a}{\sqrt2}+\frac12=C_{\rm MT},
\end{aligned}
\]

となる。最後の等号は \(\int f_0=1\) と \(\int y f_0(y)dy=0\) による。
したがって
\(\mathcal C(f_0)=\langle f_0,Tf_0\rangle=C_{\rm MT}\)。

\(h=f-f_0\) は平均ゼロなので

\[
\begin{aligned}
\mathcal C(f)
&=\mathcal C(f_0)+2\langle h,Tf_0\rangle+\mathcal C(h)\\
&=C_{\rm MT}+2C_{\rm MT}\int_Ih+\mathcal C(h)
=C_{\rm MT}+\mathcal C(h).
\end{aligned}
\]

K1 を適用すれば (2) となり、等号の場合は \(h=0\) a.e. が従う。∎

## K3. 平滑な非負偶関数への移行

Lamzouri の核クラスでは、実偶関数
\(\eta\in C_c^\infty((-1/2,1/2))\)、\(\int\eta^2=1\) を使い、\(f=\eta^2\) とする。
この小さいクラスでも

\[
\inf_\eta\mathcal C(\eta^2)=C_{\rm MT}. \tag{3}
\]

**証明.** 下界は K2 から従う。
\(0<a<\pi/2\) より \(f_0\) は \(I\) 上で厳密に正である。
\(0\le\psi_\delta\le1\) で、\(|x|\le1/2-\delta\) では1となる実偶関数
\(\psi_\delta\in C_c^\infty((-1/2,1/2))\) を選ぶ。

\[
A_\delta=\int_I\psi_\delta(x)^2f_0(x)dx,\quad
\eta_\delta(x)=\frac{\psi_\delta(x)\sqrt{f_0(x)}}{\sqrt{A_\delta}},\quad
f_\delta=\eta_\delta^2.
\]

\(A_\delta>0\)、\(A_\delta\to1\) であり、\(f_\delta\to f_0\) は \(L^2(I)\) で成り立つ。
これは境界層の長さがゼロに収束し、\(f_0\) が有界だからである。
\(T\) が有界なので \(\mathcal C\) は \(L^2\) 上で連続であり、
\(\mathcal C(f_\delta)\to C_{\rm MT}\) を得る。∎

各平滑コンパクト台の \(\eta\) は端点近傍で消えるので、\(\eta^2=f_0\) a.e. にはならない。
従ってこの小さいクラスでは最小値は達成されず、infimum として達する。
\(\delta\to0\) に伴って導関数の一様評価が保たれるとは主張しない。

## K4. 一次文献の定数との接続

ここだけ Fourier 規約を Lamzouri の

\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{-2\pi izx}dx
\]

に合わせる。`weil_conventions.md` の \(F_f\) とは \(\widehat f(z)=F_f(-2\pi z)\) という関係である。
実偶関数 \(f=\eta^2\)、\(K=\widehat f\)、\(P=f*f\) と置く。
Lamzouri, arXiv:2609.02882v1, Lemma 3.2 で生じる定数は

\[
C_\eta=P(0)+2\int_0^1 \alpha P(\alpha)d\alpha.
\]

偶関数性より \(P(0)=\int_I f^2\)。また Fubini と \(y\mapsto-y\) により

\[
2\int_0^1\alpha P(\alpha)d\alpha
=\int_{-1}^1|\alpha|P(\alpha)d\alpha
=\int_I\int_I|x+y|f(x)f(y)dxdy
=\int_I\int_I|x-y|f(x)f(y)dxdy.
\]

従って \(C_\eta=\mathcal C(f)\)。文献の規約との差を含めて、この一致を独立に計算した。

Lamzouri の適用順序は、まず平滑な \(\eta\) を固定して \(T\to\infty\) とするものである。
Lemma 3.1 の入力は、実偶関数、支持 \([-1,1]\)、\(L^1\)、原点での Lipschitz 性である。
重み除去では \(P\) と \(P''\) をそれぞれ固定したテスト関数として適用し、
\(P-P''/(4\log^2T)\) に関する未証明の一様性を仮定しない。
得られた下界の後で \(\delta\to0\) とする。ここでその pair-correlation 定理全体を再証明したとはしない。
[Lamzouri v1, Lemma 3.2 と Remark 3.4](https://arxiv.org/html/2609.02882v1)

先行する純解析の確認として、Carneiro–Chandee–Littmann–Milinovich の §3.5, Corollary 14 は、非負 admissible 関数 \(R\)、\(R(0)\ge1\) に対し

\[
M(R):=\int_{\mathbb R}R(t)
\left\{1-\left(\frac{\sin\pi t}{\pi t}\right)^2\right\}dt
\ge\frac{\cot(1/\sqrt2)}{\sqrt2}-\frac12
\]

を与えている。これは純解析の不等式で、同論文の零点への応用の RH 仮定と区別する。
\(R=K^2\) に対して Plancherel と三角関数核の Fourier 対応から
\(M(K^2)=\mathcal C(f)-1\) であり、本稿の最小値と一致する。
[CCLM, arXiv:1406.5462v1, Corollary 14](https://arxiv.org/html/1406.5462v1)

## K5. 得られる方法上の限界

Lamzouri の固定支持・同じ二次モーメント式・同じ有限多重集合不等式から得られる単純臨界線零点の割合の下界は \(2-C_\eta\) である。
K2–K4 より、この数式の右辺を核の変更だけで最大化した値は

\[
\sup_\eta(2-C_\eta)=2-C_{\rm MT}
=\frac32-\frac{\cot(1/\sqrt2)}{\sqrt2}
=0.6725007\ldots . \tag{4}
\]

この最後の小数は既知定数の表示であり、証明は厳密式 (2)–(3) による。
\(C_{\rm MT}>1\) も小数評価なしに分かる。
\(a=1/\sqrt2\)、\(\sin a\le a\)、\(\cos a\ge1-a^2/2=3/4\) から

\[
C_{\rm MT}=\tfrac12+a\cot a\ge\tfrac12+\tfrac34=\tfrac54>1.
\]

従ってこの枠内の核最適化は100%に到達しない。
これは実際の臨界線零点の割合の上界ではない。
支持・pair-correlation 入力・不等式・高次モーメント情報などを変更した別の方法の可能性も排除していない。
また、仮に密度100%を証明できても、有限個や零密度の例外を排除する別の議論なしに RH は従わない。

## K6. 文献と検証範囲

- Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, 2026-09-02, PREPRINT。本文で確認した箇所: Proposition 2.1 の仮定と結論、Lemma 3.1 のテスト条件、Lemma 3.2、Remark 3.4、Theorem 1.1 の最終的な不等式。RH依存: これらの記載は無条件。新しい変分定数としては引用しない。
  [版本固定](https://arxiv.org/abs/2609.02882v1)
- Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann, Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, arXiv:1406.5462v1; J. Reine Angew. Math. 725 (2017), 143–182, DOI 10.1515/crelle-2014-0078。本文で確認した箇所: §3.5, Corollary 14 とその証明。純解析の最適化と RH 条件付きの零点応用を区別した。
  [版本固定PDF](https://arxiv.org/pdf/1406.5462v1)

独立な数学的再検算: K1–K4 の変分計算と規約変換。
未実施: pair-correlation 定理の全文の独立再証明、当該定理の Lean 形式化の全依存関係の検査。
このファイル単独から主張できるのは、上記の変分問題の厳密解と、その数式を固定した方法上の限界である。
