**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force/notes/theta_off_axis.md` · Original SHA-256: `f07ab550b1742a5172a5f362fe6942c0269fcd7a7b6015104a126233d98628c6`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Track B — actual theta 核の臨界線外条件と PF∞ の範囲

2026-09-30。**RH OPEN。独立した臨界線外零点の排除機構は未取得。**
これは指定された theta / shape 候補の限定監査であり、新しい Hilbert 空間や de Branges 系は導入しない。
旧ファイルは読取り専用。既存の恒等式・反例を新しい成果に数えず、新規性も主張しない。

## B1. actual ξ と核の規約

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi(z)=\xi(1/2+iz).
\tag{B1}
\]

\(\theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}\)、
\(\Psi(v)=e^{v/2}\theta(e^{2v})\) と置く。
Poisson の \(\theta(x)=x^{-1/2}\theta(1/x)\) により \(\Psi\) は偶であり、

\[
\Phi(v)=\frac12(D_v^2-1/4)\Psi(v)
=\sum_{n\ge1}(4\pi^2n^4e^{9v/2}-6\pi n^2e^{5v/2})e^{-\pi n^2e^{2v}}
\tag{B2}
\]

も偶である。右の級数は各実 compact 上で全微分まで収束する。
数値計算で負側の大きな相殺を避ける場合も、偶性はこの全 theta 恒等式から得るものであり、切断和を後から偶延長する操作ではない。

\(v\ge0\)、\(x_n=\pi n^2e^{2v}\ge\pi\) なら各項は
\(e^{v/2}(4x_n^2-6x_n)e^{-x_n}>0\)。従って \(\Phi(v)>0\) は全実線で無条件。
第一項と絶対収束する尾から

\[
\Phi(v)=4\pi^2 e^{9|v|/2-\pi e^{2|v|}}
\bigl(1+O(e^{-2|v|})\bigr)\qquad(|v|\to\infty).
\tag{B3}
\]

特にすべての指数モーメントが有限で、次の積分は複素変数の compact 集合上一様に収束する：

\[
\boxed{\xi(1/2+w)=\int_{\mathbb R}\Phi(v)e^{wv}\,dv,
\qquad \Xi(z)=2\int_0^\infty\Phi(v)\cos(zv)\,dv.}
\tag{B4}
\]

係数の検算には、まず \(\Re s>1\) で Gaussian の Mellin 積分を用いる。
\(h(v)=e^{v/2}\sum_{n\ge1}e^{-\pi n^2e^{2v}}\) について
\(\Phi=(D^2-1/4)h\)、
\(\int h(v)e^{(s-1/2)v}dv=\frac12\pi^{-s/2}\Gamma(s/2)\zeta(s)\)。
二回の部分積分の境界項はこの半平面で消え、因子
\((s-1/2)^2-1/4=s(s-1)\) が出る。両辺の整性により (B4) が全平面へ延長される。
Riemann 原論文の theta–Mellin・cosine 表示は
[Wilkins 訳の本文 p.3、PDF p.4](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-translation.pdf)
と照合した。Riemann の \(\xi(t)\) は本ノートの \(\Xi(t)\) に対応する。

## B2. 二つの必要十分条件は既存 D4 と同じ

実数 \(a,t\) に対して、偶性を用いて (B4) を分けると

\[
\xi(1/2+a+it)=2\{C(a,t)+iS(a,t)\},
\tag{B5}
\]
\[
\boxed{\begin{aligned}
C(a,t)&=\int_0^\infty\Phi(v)\cosh(av)\cos(tv)\,dv,\\
S(a,t)&=\int_0^\infty\Phi(v)\sinh(av)\sin(tv)\,dv.
\end{aligned}}
\tag{B6}
\]

したがって零点条件は正確に \(C(a,t)=S(a,t)=0\)。すべての実 \(a,t\) で絶対収束し、任意回のパラメータ微分も正当化できる。
Fourier 座標は \(z=t-ia\) であることに注意する。
この式は既存 [Phase II Track D, (D4)](../../notes/phase2_modular_generator.md) と同一で、新しい拘束ではない。

- \(t=0\) では \(C(a,0)>0\)。実軸上の消滅は排除できる。
- \(a=0\) では \(S(0,t)=0\) は恒等的であり、残る \(C(0,t)\) が実際の臨界線上の零点を持つ。
- \(a\ne0\) でも \(\sinh(av)/a>0\) なのは重みだけで、\(\sin(tv)\) の符号は変わる。\(\cosh(av)\) が増加する事実も、\(\cos(tv)\) を掛けた積分の下界にはならない。

標準の帯内限定を併用した

\[
\forall\,0<|a|<1/2,\ \forall t\in\mathbb R,
\quad (C(a,t),S(a,t))\ne(0,0)
\tag{B7}
\]

は **RH そのものと同値**。これを「復元力」「二重制約」という新しい独立仮定として採用しない。
また正の測度 \(\Phi(v)e^{av}dv\) の正規化から得られるのは
\[
|\xi(1/2+a+it)|\le\xi(1/2+a),
\tag{B8}
\]
という上界であり、零点を禁じる下界ではない。
実 \(a\) 上の対数凸性は tilted measure の分散から従うが、複素方向の非消滅を意味しない。

## B3. 形状の既知入力と、適用できない強化

actual 核には正値性・偶性・二重指数減衰に加えて、
\(u\mapsto\log\Phi(\sqrt u)\) の厳密凹性という既知の無条件結果がある。
[Csordas–Varga, *Moment Inequalities and the Riemann Hypothesis* (1988)](https://www.math.kent.edu/~varga/pub/paper_161.pdf),
p.178 Theorem 2.1 / pp.178–179 の証明還元を確認した。
原文の核は \(\Phi_{CV}(v)=\Phi(2v)/2\) なので、正のスカラーと変数の正の拡大縮小を通じて本規約にも同じ凹性が成立する。
本監査は原論文 §3 の全補助評価を再証明したものではない。

この形状を臨界線外の同時消滅禁止へ強化することはできない。
既存 [内部構築ノート §3](../../internal_first_principles.md) の

\[
\phi_0(v)=e^{-v^2}(1+3v^2/20+v^4/100)
\tag{B9}
\]

は、正・偶・Schwartz で、\(\log\phi_0(\sqrt u)\) は厳密凹、
さらに \((\log\phi_0)''\le-17/10\)。実際、\(p(u)=1+\alpha u+bu^2\)、
\(\alpha=3/20,b=1/100\) について
\[
\frac{d^2}{du^2}\log p(u)
=-\frac{(\alpha^2-2b)+2\alpha bu+2b^2u^2}{p(u)^2}<0.
\]
しかし Fourier 変換は
\[
\widehat\phi_0(z)=\frac{\sqrt\pi}{1600}e^{-z^2/4}
(z^4-72z^2+1732),
\tag{B10}
\]
であり、\(z^2\) に関する判別式は \(-1744<0\)。四つの非実零点がある。
その零点では (B6) に対応する二つの積分がともに消える。
\(\phi_\varepsilon(v)=\phi_0(v)e^{-\varepsilon(\cosh(2v)-1)}\) とすれば、十分小さい \(\varepsilon>0\) で同じ反例は二重指数減衰・位数1へ延長される。
優収束と Rouché による既存の存在証明であり、今回新しい数値 \(\varepsilon\) を認証したわけではない。

この反例は shape 条件の不足だけを示す。actual theta の反例ではない。
有理係数の変換・負 Gram 証人は既存 [exact 検算](../../../../../artifacts/experiments/results/internal-kernel-checks.json) にあり、非認証求積を符号の根拠にしない。
Gaussian 実一次因子積の閉包から actual 核を除外した三階対数差分も、同じ旧ノートの既存結果として保持するだけである。

より算術構造に近い既存 [自己双対 theta 変形](../../selfdual_theta_boundary.md) は、正 seed・Poisson 反射・正 completed kernel・端点規格化を保ちながら
\[
\widetilde\xi(s)=c^{-1}P(s-1/2)\xi(s),\quad
P(w)=\frac{256}{268468225}
[(w-1/4)^2+32^2][(w+1/4)^2+32^2]
\tag{B11}
\]
を作り、\(s=1/4\pm32i,3/4\pm32i\) を追加する。
標準 Gamma 因子は変更される。これは同じ標準 ξ の反例でも、標準 Gaussian を固定した反例でもない。
したがって「正の核＋modular 対称性」だけから (B7) を出す案は止まるが、actual 算術の未使用の全構造まで否定したとはしない。

## B4. PF∞ は Fourier 変換の Laguerre–Pólya 性とは別条件

ここでいう **PF∞** は可測 \(f\) に対し \(0<\int f<\infty\)、かつ任意の \(r\ge1\)、
\(x_1<\cdots<x_r\)、\(y_1<\cdots<y_r\) について
\[
\det[f(x_i-y_j)]_{i,j=1}^r\ge0
\tag{B12}
\]
を要求する、連続変数の Toeplitz kernel の全順序 total nonnegativity である。
点ごとの正値性、有限個の minor、別の二変数 kernel の正値性とは同一ではない。

[Schoenberg, *On Pólya frequency functions II* (1950)](https://acta.bibl.u-szeged.hu/13626/),
§1 pp.97–98, Eq.(2)–(3) は、PF∞ 関数の bilateral Laplace 変換が 0 を含む strip で
\[
\mathcal Bf(s):=\int_{\mathbb R}f(v)e^{-sv}\,dv=\frac1{\psi(s)},
\quad
\psi(s)=C e^{-\gamma s^2-\delta s}
\prod_j(1+\delta_js)e^{-\delta_js}
\tag{B13}
\]
となることを述べる。\(C>0\)、\(\gamma\ge0\)、\(\delta,\delta_j\in\mathbb R\)、
\(0<\gamma+\sum_j\delta_j^2<\infty\)。
確認したのは著者自身による変換定理の再掲であり、1951年の長い証明全体の再監査ではない。
[原版 PDF](https://sites.stat.washington.edu/jaw/COURSES/580s/581/HO/Schoenberg-50.ASMATHSzeged.pdf) の該当2頁を画像でも確認した。

重要なのは **変換の逆数** が Laguerre–Pólya 型になることである。
これは \(\widehat f\) 自身が entire で全実零点を持つという命題ではない。

**限定された no-go。** 正の偶連続可積分関数 \(f\) がすべての指数モーメントを持ち、PF∞ でもあるなら、\(f\) は Gaussian に限られる。

証明：全指数モーメントにより \(\mathcal Bf\) は entire。
(B13) から \((\mathcal Bf)\psi=1\) は strip 上、従って全平面で成立する。
\(\psi\) に零点があれば矛盾するので、すべての非零 \(\delta_j\) が排除される。
非退化条件から \(\gamma>0\)、偶性から \(\delta=0\)。よって
\(\mathcal Bf(s)=C^{-1}e^{\gamma s^2}\)。虚軸での Fourier 変換の一意性により
\[
f(v)=\frac1{C\sqrt{4\pi\gamma}}e^{-v^2/(4\gamma)}.
\tag{B14}
\]
連続性により a.e. の同一性は全点の同一性になる。証明終。

actual \(\Phi\) は (B3) の減衰なので Gaussian ではない。従って
\[
\boxed{\Phi(x-y)\text{ は上の意味の PF∞ kernel ではない。}}
\tag{B15}
\]
この結論は RH も、ξ の既知零点の利用も必要としない。
これに対し \(\Xi\) 自身の Laguerre–Pólya 所属は RH と同値である。
実際、RH 下では偶・位数1の Hadamard 積を \(\pm\gamma\) で対にし、
\(\Xi(z)=\Xi(0)\prod_{\gamma>0}(1-z^2/\gamma^2)\) が compact 一様に収束する。
有限積は全実零点多項式なので LP に属する。逆向きは Hurwitz による。
PF∞ の不成立から LP の不成立を推論してはならない。

## B5. Pólya の結果の適用範囲と終了判定

[Pólya 1926, *Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion*](https://doi.org/10.1007/BF02565336)
を [原論文の英訳](https://translations.thosgood.net/AM-48-1926-305.pdf) で照合した。
原文 pp.305–307, Eq.(2)–(8) の actual 核と modified \(\xi^*\) は別関数。
§3 と §4 は特定の modified kernel の実零点性を証明し、§4 Lemma II（pp.316–317）は
既に全実零点を持つ genus 0/1 の実 entire 関数に対する imaginary-shift 和の保存命題である。
actual \(\Xi\) の実零点性を仮定せずに供給する命題ではない。
Csordas–Varga p.177 Eq.(2.2)–(2.4) の universal-factor 説明も、元の Fourier 変換の実零点性を前提にしている。

本監査の到達点は、(B4)–(B6) の正確な規約、既存 shape / modular 反例の適用範囲、
そして特定の Toeplitz PF∞ 候補を排除する (B15) である。
核正値性から得る上界や低階の形状を、二つの振動積分の同時消滅を禁止する下界へ移す独立な算術不等式は得られなかった。
既知の零点同値条件に言い換えて補うことはしない。

**Decision: STOP THIS TRACK B CANDIDATE.**
二式の共通零点を \(a\ne0\) で排除するという最終命題は RH 同値であり未証明。
素朴な PF∞ 強化は actual 核に対して偽。LP 強化は RH 同値。
これは actual ξ の反例でも、将来の全 theta 手法への不可能性定理でもない。
新しい数値格子・核族・作用素を追加せず、この bounded comparison で終了する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/internal-kernel-checks.json`](../../../../../artifacts/experiments/results/internal-kernel-checks.json)
- [`research/internal_first_principles.md`](../../internal_first_principles.md)
- [`research/notes/phase2_modular_generator.md`](../../notes/phase2_modular_generator.md)
- [`research/selfdual_theta_boundary.md`](../../selfdual_theta_boundary.md)
