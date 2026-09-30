**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/global-kernel-candidate.md` · Original SHA-256: `d8f6cc28679518392cafb4e51521eb60212106dc903ca5ac90c4f3321a9a85e7`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 独立監査: 全実線上の非負密度に対する人工エネルギー

日付: 2026-09-29。担当: DESTROYER。
ROOT が提示した statement のみから検算し、以下の仮定下では反例・係数誤りを検出しなかった。

**判定: 解析的恒等式と等号分類は PASS。新規性は未判定。RH の結果ではない。**

## 1. 監査対象と必須仮定

\(f:\mathbb R\to[0,\infty)\) は可測で、
\[
f\in L^1(\mathbb R)\cap L^2(\mathbb R),\qquad
\int f=1,\qquad \int |x|f(x)dx<\infty.
\]
CDF とエネルギーを
\[
F(t)=\int_{-\infty}^tf(x)dx,\qquad
E(f)=\int f^2+\int_{\mathbb R^2}|x-y|f(x)f(y)dxdy
\]
とする。第2項は \(|x-y|\le|x|+|y|\) により有限。
f の非負性、質量1、密度としての絶対連続性は以下の変換に必要である。

## 2. CDF 表示: PASS

\[
|x-y|=\int_{\mathbb R}
\bigl|\mathbf1_{x\le t}-\mathbf1_{y\le t}\bigr|dt
\]
を非負関数 \(f(x)f(y)\) に掛け、Tonelli を使えば
\[
\int\!\int|x-y|f(x)f(y)dxdy
=2\int_{\mathbb R}F(t)(1-F(t))dt.
\]
ここで F は連続かつ局所絶対連続、\(F'=f\) a.e.、\(F(-\infty)=0\)、\(F(+\infty)=1\)。
この表示を符号付き f に流用して平方根を取ることはできない。

## 3. 変数変換と平方完成: PASS

\[
G(u)=\int_0^u\sqrt{v(1-v)}dv\quad(0\le u\le1)
\]
は \(C^1([0,1])\) で、その導関数は有界である。局所絶対連続関数の chain rule より、任意の有限区間で
\[
(G\circ F)'(x)=f(x)\sqrt{F(x)(1-F(x))}\quad\text{a.e.}
\]
となる。区間の端を無限へ送る際は、非負性または有界な G と F の端点極限を使用できる。従って
\[
\int_{\mathbb R}f(x)\sqrt{F(x)(1-F(x))}dx
=\int_0^1\sqrt{u(1-u)}du=\frac\pi8.
\]
F が厳密単調であることや、逆関数の存在をこの段階で仮定する必要はない。

CDF 表示を使うと、平方完成から厳密に
\[
\boxed{
E(f)-\frac\pi{2\sqrt2}
=\int_{\mathbb R}\left(f(x)-\sqrt{2F(x)(1-F(x))}\right)^2dx\ge0.
}
\]
係数は \(2\sqrt2\times\pi/8=\pi/(2\sqrt2)\)。両平方項が可積分であり、交差項も上の恒等式で有限だから、無限大同士の差は生じない。

## 4. 等号の完全分類: PASS (平行移動・a.e. 同一視)

等号は
\[
F'(x)=f(x)=\sqrt{2F(x)(1-F(x))}\quad\text{a.e.}
\]
と同値である。右辺は F の連続関数なので、F はこの微分方程式を満たす \(C^1\) 関数として扱える。

**注意:** 右辺は F=0,1 で Lipschitz ではない。通常の初期値問題の一意性を端点に直接使ってはいけない。

代わりに、非空の開区間
\[
J=\{x:0<F(x)<1\}
\]
に制限する。J が区間なのは F が非減少だからである。J 上で
\[
\theta(x)=\sqrt2\arcsin\sqrt{F(x)}
\]
と置けば、内点では問題なく chain rule が使え
\[
\theta'(x)=1.
\]
従って \(\theta(x)=x-b\)。\(0<\theta<\pi/\sqrt2\) と J の最大性・連続性から
\[
J=(b,b+\pi/\sqrt2).
\]
その外では F は左で0、右で1。中心 \(c=b+\pi/(2\sqrt2)\) を用いると
\[
F(x)=\frac{1+\sin(\sqrt2(x-c))}{2}
\quad\left(|x-c|<\frac\pi{2\sqrt2}\right),
\]
従って等号密度は、a.e. の意味で
\[
\boxed{
f_c(x)=
\begin{cases}
\cos(\sqrt2(x-c))/\sqrt2,
 &|x-c|\le\pi/(2\sqrt2),\\
0,&\text{それ以外}.
\end{cases}}
\]
に限られる。端点での waiting はこの平行移動の自由度に含まれ、内部にギャップを持つ解は生じない。

逆方向も確認できる。各 \(f_c\) は非負、compact support、質量1で全仮定を満たし、上の ODE を満たす。\(\int f_c^2=\pi/(4\sqrt2)\) で、相互作用項も同じ値となる。

## 5. 仮定を落とした反例と適用限界

**非負性を落とすと FALSE。**
\[
f(x)=\begin{cases}
5/4,&-2\le x<0,\\
-3/4,&0\le x\le2,\\
0,&\text{それ以外}
\end{cases}
\]
は質量1、L¹∩L²、有限一次絶対モーメントを満たすが、
\[
\int f^2=\frac{17}{4},\qquad
\int\!\int|x-y|f(x)f(y)dxdy=-\frac{28}{3},\qquad
E(f)=-\frac{61}{12}.
\]
従って全実線上の符号付き関数へこの正下界を延長してはいけない。

**RH への未証明な適用は不可。** この E は指定された人工的な汎関数である。既知 pair-correlation 公式の support 制約を外した後も定数が E(f) のままであることは、この恒等式から従わない。高次モーメント、他の不等式、別の核に対する一般的な不可能性も証明していない。

**smooth クラスでは達成と近似を区別する。** 等号密度のゼロ延長は \(C_c^\infty\) ではない。smooth 非負密度への下界はそのまま適用できるが、同じ infimum を主張するには mollification/cutoff と E の収束を別途記載する必要がある。その近似は compact support 内での L²・L¹ 収束から構成できるものの、等号密度自体を smooth と呼んではならない。

## 6. 監査の範囲

使用した解析は非負積分の Tonelli、絶対連続関数の chain rule、平方完成、および開区間上の一次 ODE の直接積分である。数値検算を証明には用いない。

本監査は命題の数学的妥当性を確認したものであり、文献上の新規性を確認したものではない。集積・拡散エネルギー等との既知性調査は継続課題であり、「新定理」との優先権主張を支持しない。形式化コードは未検証。
