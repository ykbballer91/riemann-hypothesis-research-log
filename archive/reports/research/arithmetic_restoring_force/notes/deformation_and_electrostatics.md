**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_restoring_force/notes/deformation_and_electrostatics.md` · Original SHA-256: `1dce218d255dd472c7de373c11235f10bf9d0daabeb5c61a33a03d58f7b06055`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Track C — actual heat deformation と electrostatics の限定監査

2026-09-30。ARITHMETIC RESTORING FORCE の独立監査。**RH OPEN。新しい独立な算術復元則は未取得。**
旧 [Newman generator](../../notes/phase2_newman_generator.md) と
[generator/boundary 判定](../../generator_boundary_hypothesis.md) は読取のみ。
本稿の有限多項式計算は既知原理の直接検算であり、新規性・RHへの進展・actual ξ の反例を主張しない。

## C1. actual family、時間方向、domain

旧ノートと同じ規約を固定する：
\[
\Phi(u)=\sum_{n\ge1}
(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})e^{-\pi n^2e^{2u}},
\qquad \Phi(-u)=\Phi(u),
\]
\[
H_\tau(z)=\int_{\mathbb R}e^{\tau u^2}\Phi(u)e^{izu}\,du,\qquad
H_0(z)=\xi(1/2+iz).
\]
右辺の級数はまず \(u\ge0\) で用いる。theta 反転が偶性を与える。
二重指数減衰により任意の compact な複素 \((\tau,z)\) 集合上で積分と全導関数が一様収束する。
従って時間原点は正則であり、初期値の指定そのものに相転移条件は含まれない。
直接微分して
\[
\partial_\tau H_\tau=-\partial_z^2H_\tau. \tag{C1}
\]
これは \(\tau\) 増加方向には backward heat equation。
通常の forward heat 時間を \(b=-\tau\) と取れば符号が反転する。
\(u^2\) の乗算作用素は正自己共役だが、\(e^{\tau u^2}\) は \(\tau>0\) で全 \(L^2\) 上の有界作用素ではない。
actual \(\Phi\) が各指数の domain に入ることと、零点実軸性は別である。

Rodgers–Tao の規約とは
\[
H_t^{RT}(z)=\tfrac18 H_{t/4}(z/2),\qquad
\Lambda_{\rm repo}=\Lambda_{RT}/4. \tag{C2}
\]
これは原論文 (1),(3),(4) への \(u\mapsto u/2\) の代入で検算した。
[Rodgers–Tao, arXiv:1801.05914v3, 2020-03-06, §1](https://arxiv.org/html/1801.05914v3#S1)。

## C2. 単純零点 ODE と多重零点

単純零点 \(z_j(\tau_0)\)、すなわち \(H_z\ne0\) では複素陰関数定理から局所解析的な枝が存在し、
\[
z_j'(\tau)=\frac{H_{zz}(\tau,z_j(\tau))}{H_z(\tau,z_j(\tau))}. \tag{C3}
\]
この式は線上・線外とも成立するが、多重零点では分母が零となる。
そこで単純枝の ODE を無条件に継続してはならない。
無限零点の対相互作用表示には積表示、指数因子、和の順序・収束の管理が別途必要。

有限実多項式なら \(P_\tau=e^{-\tau D^2}P_0\) は有限和で定義でき、
全零点が単純な時間区間で、最高次係数は不変だから
\[
z_j'=2\sum_{k\ne j}\frac1{z_j-z_k}. \tag{C4}
\]
actual 無限系について照合した一次定理は Rodgers–Tao **Theorem 4.1, (56)**。
その本文の範囲は \(\Lambda_{RT}<t\le0\) で、実・単純零点を番号付けし、
\(\mathbb Z^*\) 上の対称主値和を用いる。(43),(50) が収束に使われる。
同論文は \(\Lambda<0\) の背理法の中でこの範囲を使っている。
したがって、これを未証明の「時刻 0 の全零点は実数」の入力に転用できない。
[原文 §4, Theorem 4.1](https://arxiv.org/html/1801.05914v3#S4)。

最小の衝突例は
\[
P_\tau(z)=(z-a)^2+b^2-2\tau,\qquad b>0.
\]
\(\tau<b^2/2\) では \(a\pm i\sqrt{b^2-2\tau}\)、等号で二重零点、
以後は \(a\pm\sqrt{2\tau-b^2}\)。
衝突前の上側枝は \(y'=-1/y\)、衝突後の実枝は互いに離れる。
枝の速度の発散と、多項式自体の時間解析性は両立する。
この模型の任意の衝突時刻を actual 算術の時刻 0 に同定する理由はない。

## C3. 各零点の横方向復元と、最外帯の収縮は異なる

\(z_j=x_j+iy_j\) として有限系 (C4) の虚部を取ると
\[
y_j'=-2\sum_{k\ne j}
\frac{y_j-y_k}{(x_j-x_k)^2+(y_j-y_k)^2}. \tag{C5}
\]
上端 \(y_j=Y>0\) を達成する零点では各項が非正であり、
共役零点の項だけで \(Y'\le-1/Y\)、従って \((Y^2)'\le-2\)。
これは単純枝の有限区間上の計算である。上端を達成しない無限系へ
この微分計算だけを移すことはしない。

一方、**全ての内側非実枝が常に実軸へ動くという命題は偽**。
偶・実多項式
\[
P_0(z)=\prod_{a\in\{-2,2\}}
\big((z-a)^2+1\big)\big((z-a)^2+4\big)
\]
の単純零点 \(z_*(0)=2+i\) では
\[
\Im z_*'(0)
=\frac13-\frac15+\frac2{17}-\frac6{25}
=\frac{14}{1275}>0. \tag{C6}
\]
最初の \(1/3\) は同じ実部 2 の他の三零点から、
残りは実部 \(-2\) の四零点から得る。陰関数定理により正の微小時間で外向きの枝が存在する。
共役・反転対称、純虚零点なしを満たすが、actual theta 核・正の Fourier 核・Euler 積は共有しない。
反証対象は heat equation と対称性だけからの普遍的な各零点復元則である。
実軸上の (C4) は零点間の反発であり、原点への radial confinement でもない。

ζ 座標 \(s=1/2+iz\) では \(\Re s-1/2=-\Im z\)。
したがって帯の虚方向収縮は ζ 側の横方向収縮に対応し、
実 \(z\) 同士の反発は ζ 零点の高さの運動に対応する。二つを取り違えない。

## C4. de Bruijn の定理は存在するが、時刻 0 を証明しない

原著 de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17 (1950), 197–226：
**Theorem 10 (p.204), Theorem 13 / (3.8) (p.205)**。
\(F\in L^1\)、\(F(u)=\overline{F(-u)}\)、
\(F(u)=O(e^{-|u|^b})\)（ある \(b>2\)）、変換の全零点が \(|\Im z|\le\Delta\)
という条件から、\(F(u)e^{\lambda^2u^2/2}\) の変換の全零点は
\[
|\Im z|\le\sqrt{\max(\Delta^2-\lambda^2,0)}.
\]
つまり本稿の時間増分 \(h\ge0\) では幅
\(\sqrt{\max(\Delta^2-2h,0)}\)。
[原著 PDF, pp.204–205](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da)。
検索結果の自動 OCR は指数の \(1/2\)・平方を落とすため、その裸の表示は採用しない。
同じ係数は [Newman, Theorem 1, p.246](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf)
の \(e^{\delta u^2}\)、幅 \(\sqrt{\max(\Delta^2-2\delta,0)}\) とも照合した。

actual \(H_0\) は古典的 critical strip から \(\Delta=1/2\) を使える。
得られるのは \(\tau\ge1/8\) での全実零点性であり、逆向きに時刻 0 へ進む結論ではない。
より良い既知上界の最新値をここで調査・主張しない。

Newman の **Theorem 3, p.247** は閾値の有限性を与える。
原著の変数は \(e^{-bu^2}\) で、本稿と \(b=-\tau\)。
端点は局所一様収束と Hurwitz により含まれる。
Rodgers–Tao **Theorem 1.1** は \(\Lambda_{RT}\ge0\)。
以上と定義から、本稿の \(\lambda=\Lambda_{\rm repo}\) に対し
\[
0\le\lambda\le1/8,\qquad
H_\tau\text{ の全零点が実数}\iff\tau\ge\lambda,\qquad
{\rm RH}\iff\lambda=0. \tag{C7}
\]
これらは既知入力であり、今回独立に全証明を再監査したという意味ではない。
[Newman 原著](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf)、
[Rodgers–Tao 定理](https://arxiv.org/html/1801.05914v3#S1)。

したがって「任意の正時間で実零点」「全高さで逆向きの衝突を 0 まで禁止」
を実零点保存定理から追加するのは正当化されない。
前者は Hurwitz と (C7) により RH と同値。後者も 0 の全零点回収を含めて成立させれば RH を供給するが、
必要な全高さ一様の算術評価は未取得である。
既知の \(\lambda\ge0\) は要求する向きの上界ではない。

Pólya の universal factor の役割も preservation である。
\(e^{hu^2}\), \(h\ge0\) は全実零点性を保存するが、保存の前件を証明しない。
1927 原著の書誌・DOI は
[Über trigonometrische Integrale mit nur reellen Nullstellen, pp.6–18](https://doi.org/10.1515/crll.1927.158.6)。
今回その原著全文の取得は失敗したため原定理番号は未確認。
使用する特殊例は de Bruijn 原著 p.197 の Pólya の定式化と pp.204–205 で確認した。
原著を直接読んだと偽らない。

## C5. Stieltjes と正の直交性が供給する条件

比較用の Hermite の場合は直接検算できる。
正の重み \(e^{-x^2}dx\) に関する次数 \(n\) の直交多項式は、
直交性と符号変化の標準証明によって実・単純零点を持つ。
\[
H_n''-2xH_n'+2nH_n=0
\quad\Longrightarrow\quad
\sum_{k\ne j}\frac1{x_j-x_k}=x_j.
\]
これは順序付けた実配置上の
\[
\mathcal E(x)=\sum_jx_j^2-2\sum_{j<k}\log|x_j-x_k|
\]
の平衡条件であり、
\[
D^2\mathcal E(x)[v,v]
=2\sum_jv_j^2+2\sum_{j<k}\frac{(v_j-v_k)^2}{(x_j-x_k)^2}>0
\]
なのでその chamber で平衡は一意。境界衝突と無限遠で energy が発散する。
ここには独立に与えられた正の直交測度と二階 ODE がある。
未知の ξ 零点を先に実配置へ置くことは、その代替にならない。

一次論文による条件付き一般化は Ismail (2000), **§1 (1.1)–(1.15), §2 Theorem 2.1,
pp.358–360**。正の直交重み \(w=e^{-v}\)、所定の微分・積分条件、
\(v\) と \(v+\log A_n\) の凸性、境界で \(T=e^{-\mathcal E}\to0\) の条件を用いる。
外場は任意の \(-\log w\) だけでなく \(V=v+\log(A_n/a_n)\)。
この定理は actual ξ の外場や直交性を構成しない。
[Ismail 原著 PDF](https://msp.org/pjm/2000/193-2/pjm-v193-n2-p06-s.pdf)。

Stieltjes の原著候補
[Sur certains polynômes, Acta Math. 6 (1885), 321–326](https://doi.org/10.1007/BF02400421)
は今回書誌を確認したが、本文取得が失敗した。
その原文定理を独立確認済みとはしない。
Stieltjes 型の Jacobi/Laguerre 配置の歴史的帰属は Ismail §1, p.355 で確認し、
本稿で必要な Hermite の等式・Hessian は上の直接計算で賄った。
これは限定された原典取得不足であり、未読の古典を actual RH 用の定理として採用してはいない。

## C6. random matrix の log gas は別の前件を持つ

Dyson (1962), *A Brownian-Motion Model for the Eigenvalues of a Random Matrix*,
J. Math. Phys. 3, 1191–1198,
[出版社一次 abstract](https://doi.org/10.1063/1.1703862) は
Hermitian 行列要素の Brownian 運動と固有値の反発過程の対応を明記する。
今回確認範囲は abstract と書誌であり、全文の SDE の係数を確認済みとはしない。
Hermitian という前件が固有値の実数性を既に供給している。

例えば実数変数で定義した密度
\(\exp[-\sum_jV(x_j)]\prod_{j<k}|x_j-x_k|^\beta\) は定義域が \(\mathbb R^n\)。
反発項と外場は明示できるが、actual ξ の全零点を同じ確率法則の実変数へ同定する定理はここから出ない。
熱零点 ODE は一次の速度の法則であり、Newton の加速度の法則でも、
Brownian noise を含む SDE でもない。統計の一致から全零点の支持を決めない。

## C7. 判定と再利用可能な境界

- **KEEP（既知入力・限定検算）:** 正しい時間符号、actual kernel の domain、
  単純枝公式、多重衝突例、forward strip contraction、閾値の規約換算。
- **REJECT（具体的な誤推論）:** 各非実枝の普遍的な単調復元は (C6) で偽。
  実零点間の反発から線外排除、正自己共役 heat generator から零点実数性、
  log-gas の実配置を ξ に移す推論には必要な同定がない。
- **MISSING:** actual 算術初期値に対し、全高さを覆って閾値を 0 以下へ押す独立評価。
  \(\lambda\le0\) をそのまま「復元則」と再命名しても同値条件の言い換えである。
- **Scope:** 有限 synthetic 計算は actual ξ の反例ではない。全ての変形法・energy 法の不可能性は未主張。
  Pólya/Stieltjes 原著全文の取得不足、Dyson の abstract-only を明記。
  定理全文の独立再証明・査読済み新結果・新 operator はない。
  **Track C はこの bounded gate で終了。RH OPEN、主 graph への独立新入力 0。**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/generator_boundary_hypothesis.md`](../../generator_boundary_hypothesis.md)
- [`research/notes/phase2_newman_generator.md`](../../notes/phase2_newman_generator.md)
