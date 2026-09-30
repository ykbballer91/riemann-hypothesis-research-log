**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/one_prime_return_adversarial.md` · Original SHA-256: `c47e8159535fb52bab6ff095591772f2a3422eee4dd79dd56ea66dc89e293247`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-Prime Return 独立敵対監査

2026-09-29。既存ファイルは変更せず、本ファイルのみ作成。Phase III/IV、state、主グラフは対象外。

対象：`research/one_prime/notes/abstract_return.md` AR1–AR6、`arithmetic_space.md` §§2–5、および builder 依頼の `topology_constructions.md` OT2–OT3。`transference_similarity.md` の exact counterexamples と整合を確認した。原論文の全証明、formal/Lean の実行結果、算術 subexponential bound を独立に証明したという監査ではない。

**最終判定：上記範囲は PASS。** 初回に指摘した AR4 の逆冪下界の説明は親が修正し、再読で解消を確認した。新しい RH 証明ではなく、抽象的な sufficient condition と actual zero-retaining Banach completion の限定的な構成である。肝心の quotient-growth estimate は未証明。

## OP-A1. AR1–AR2：スカラー比較と二側 rate

\(a,b>0\)、全 \(m\ge0\) について \(a^m\le Cb^m\) なら \(a\le b\)。\(C\) を \(\varepsilon\) に依存させても、\(a^m\le C_\varepsilon e^{\varepsilon m}\) が全 \(\varepsilon>0\) で成立すれば \(a\le1\)。逆数にも同じ評価を課せば \(a=1\)。固定した非零 scalar observation 一つの両方向成長比較でも十分である。

bounded invertible \(T\) と非零 bounded linear functional \(\ell\) が \(\ell T=\lambda\ell\) を満たすなら、onto 性により \(\lambda\ne0\)。双対 norm を取って
\[
|\lambda|^{\pm m}\le\|T^{\pm m}\|.
\]
したがって
\[
g_\pm=\limsup_{m\to\infty}m^{-1}\log\|T^{\pm m}\|,
\qquad -g_-\le\log|\lambda|\le g_+.
\]
\(\|T^m\|\|T^{-m}\|\ge1\) により \(g_++g_-\ge0\)。従って \(|\log|\lambda||\le\max(g_+,g_-)\) も正しい。\(\lambda=2^{\rho-1/2}\) では rate を \(\log2\) で割る必要があり、AR4 の換算は正確である。

一方向だけの bound は一般には一方の半平面しか与えない。全零点に同じ一方向 estimate が適用でき、零点集合の reflection を別に使う場合の追加帰結とも区別されている。

## OP-A2. AR3：locally convex の量化と Baire

EQUI、SUBEQ、POINTSUB の量化は適切。SUBEQ の入力 seminorm \(r_{q,\varepsilon}\) と定数は \(q,\varepsilon\) に依存してよいが、反復数 \(n\) や vector \(f\) に依存しない。POINTSUB は各 \(f\) ごとに定数を許す。この差を省略していない。

POINTSUB から単一 eigencharacter の modulus 1 を得るには、continuous seminorm \(q=|\ell|\) と \(\ell(f)\ne0\) の一つの vector を固定すればよい。operator norm や一様な vector bound を作る必要はない。

Fréchet における逆含意 POINTSUB⇒SUBEQ も正しい。固定 \(\varepsilon,q\) に対し
\[
A_n=e^{-\varepsilon|n|}T^n,\qquad
E_m=\{f:\sup_nq(A_nf)\le m\}
\]
は閉・絶対凸で、\(\bigcup_{m\ge1}E_m=X\)。Baire によりある \(E_m\) が内点を持ち、\(E_m-E_m\subset E_{2m}\) が零近傍を含む。従って \(\sup_nq(A_n\cdot)\) は continuous seminorm となる。一般 barrelled source での Banach–Steinhaus 版も同じ結論を与える。bornological な個別作用の boundedness、integrated nuclearity をこの family equicontinuity に読み替えていない点は重要である。

## OP-A3. AR4：Jordan 直和の exact norm

\(N_m\) を有限 nilpotent shift、\(0<a<1\)、
\(T=\bigoplus_{m\ge1}(I+aN_m)\) とする。\(\|T\|\le1+a\)、\(\|T^{-1}\|\le(1-a)^{-1}\)。binomial と Neumann 展開によって
\[
\|T^n\|\le(1+a)^n,\qquad
\|T^{-n}\|\le(1-a)^{-n}\quad(n\ge0).
\]
長さ \(m\) の正規化定数 vector では \(N_m v_m-v_m\to0\)。これが正冪の下界を与える。一方、正規化交代符号 vector では \(N_m w_m+w_m\to0\)。\((I+aN_m)^{-1}\) の一様 bound と resolvent identity により、後者から逆冪の下界を得る。従って
\[
\|T^n\|=(1+a)^n,\qquad
\|T^{-n}\|=(1-a)^{-n}.
\]

初回原稿では両方の下界を「\(+1\) のほぼ定数 vector」と記していた。この説明は逆冪に不足するため修正を依頼した。現原稿には \(+1\) の定数 vector / \(-1\) の交代符号 vector の区別が入り、**RESOLVED**。表示された等式自体は当初から正しい。

各有限 block の polynomial growth、有限 support Jordan vector の稠密性は、無限直和の一様 subexponential bound を意味しない。この反例は実際の零点多重度や arithmetic quotient の反例ではない。

## OP-A4. AR5–AR6：離散と連続、必要十分の射程

既に Banach \(C_0\) 群 \(W_u\) があるなら、一つの \(L>0\) における \(T=W_L\) の二側 subexponential norm growth と、全実時間での同じ性質は同値。\(u=nL+r\), \(0\le r<L\), \(|n|\le |u|/L+1\) と局所有界性から
\[
\|W_u\|\le M C_\varepsilon e^\varepsilon e^{\varepsilon|u|/L}.
\]
任意の連続時間 rate \(\delta>0\) には \(\varepsilon=L\delta\) を選ぶ。逆は部分列なので正しい。この証明は最初から存在する同一群を使い、異なる素数の異なる local fiber を接合していない。

RH の実部結論に、no-extra-spectrum、trace class、determinant、compact resolvent、全 Hilbert eigenbasis、simple zeros は不要という AR6 の範囲は正しい。単一 return では高さが \(2\pi/\log2\) modulo に alias するので、full flow の multiplicity と return eigenvalue の multiplicity は自動的に一致しない。

## OP-B1. 算術 sector と閉値域の限定

`arithmetic_space.md` の \(E\) は全指数重み付き scalar test space の Fréchet 表示で、\(p_N\) は増大する seminorm 系である。\(g\mapsto(e^{kt}g)_{k\in\mathbb Z}\) の closed product 表示により完全性・核型性は整合する。\(W=\overline V^E\) を明示して取るので、\(E/W\) は Hausdorff nuclear Fréchet である。

一次原文 [Meyer, math/0311468v1, Theorem 5.1、Lemma 5.4、§5.3](https://arxiv.org/pdf/math/0311468v1) の該当 statement と proof の scope を限定照合した。\(K=\mathbb Q\) の compact-unit invariant sector では \(S=\{\infty\}\) とでき、\(\mathbb Q_S^\times=\{\pm1\}\) の coinvariants は even Schwartz functions である。Lemma 5.4 の embedding をこの固定 Fréchet sector に制限すれば topological embedding として扱え、complete domain の image は閉じる。Poisson の diagonal intersection 条件が \(f(0)=\int f=0\) であるため、この sector の summation range の閉性という帰結は妥当。

これは一般 cyclic module 全体の Fréchet 性・一般閉値域の主張ではない。また critical weighted \(L^2\) の閉包ではない。今回必要な \(q_1\)-retention は、さらに強い \(W=V\) を使わず、\(W=\overline V^E\) だけでも証明できる。

## OP-B2. \(q_1\le4\) ではなく evaluation \(\le4q_1\)

正確な向きは
\[
|\ell_\rho([g])|\le4q_1([g]).
\]
\(\delta=\Re\rho-1/2\)、\(|\delta|<1/2\) とすると、source seminorm の定義から
\[
|g(t)|\le p_1(g)e^{-|t|}(1+|t|)^{-1}
            \le p_1(g)e^{-|t|}.
\]
従って、より一般に
\[
|\ell_{\rho,j}(g)|
\le \frac{2j!}{(1-|\delta|)^{j+1}}p_1(g)
\le 2^{j+2}j!p_1(g).
\]
この定数は高さに依存しない。Mellin factorization
\(\widehat{\Sigma f}(s)=2\zeta(s)\int_0^\infty f(x)x^s\,d^\times x\)
の第二因子は非自明零点の strip 内で holomorphic。従って \(j<m_\rho\) の jets は \(V\) を消す。連続性により \(W\) も消し、representative の infimum を取れば同じ bound が \(q_1\) へ降りる。

有限個の異なる零点とその finite jets の線形独立性は、\(C_c^\infty\) 上の exponential-polynomial 分布の独立性から従う。このため \(q_1\) の radical と completion を通じても、それらは非零・独立な bounded functionals として残る。全無限 jet 列の unrestricted product との同型を意味しない。

## OP-B3. Banach completion と multiplicity の範囲

\(T_2^\pm\) の \(q_1\)-bound により \(\ker q_1\) は両方向不変。\(T_2,T_2^{-1}\) は completion \(X_1\) へ bounded に延長し、dense core での逆作用素関係が全 completion へ延長する。従って bounded invertibility の主張は正しい。

\(2^{\rho-1/2}\) が \(T_2'\) の eigenvalue なので \(T_2\) の spectrum に含まれることも正しい。もし \(T_2-\lambda I\) が bounded inverse を持てば、その transpose も可逆となり非零 eigenfunctional と矛盾する。

この Level 2 は、元の Fréchet 商から \(X_1\) への injectivity、全商位相との同値性、余分な spectrum の排除、trace theorem の延長を証明していない。記載はこの点を適切に限定している。

\(m_\rho\ge2\) なら残った jets は
\[
\ell_{\rho,1}T_2^n
 =2^{n(\rho-1/2)}(\ell_{\rho,1}+n\log2\,\ell_{\rho,0})
\]
を満たす。二側 uniform power bound はまず \(\Re\rho=1/2\) を強制し、その後 \(\ell_{\rho,0}(x)\ne0\) の vector にこの式を適用すると linear growth と矛盾する。従ってこの particular completion の uniform bound / unitary similarity は simple zeros まで要求する。subexponential bound はこの finite polynomial growth を許す。この違いは正しく記載されている。

## OP-C. Builder OT2–OT3 の限定読取監査

**PASS。** \(S\) 上の seminorm \(N\)、range \(R\) に対し、quotient seminorm の completion は \(X_N/\overline{j(R)}\) と等長。距離の infimum は range の closure を取っても変わらず、source の image は商で dense なので証明は完結する。\(R\) を消す \(\ell\) の \(N\)-bound と quotient bound は同じ最良定数を持つ。

\([H_0,H_k]_\theta=H_{\theta k}\) の直接 interpolation proof では、逆向きの analytic pairing の両境界で同じ \(L^2(e^{-2\theta k|t|}dt)\) dual norm が現れる。符号・定数は一致する。translation norm \(2^{a|n|}\)、評価保持閾値 \(a>|\alpha|\)、その norm squared \(a/(a^2-\alpha^2)\)、\(a=0\) で全ての point evaluations が非有界という各式も正しい。

ambient exact norm は arithmetic quotient の下界に使われていない。商代表元による新しい cancellation の可能性まで排除する blanket no-go にはなっていない。OT4 以降は今回の依頼に対する独立監査の対象外。

## 最終 scope

抽象的な growth implication と、実際の arithmetic range を消す evaluation/jet の保持は区別して検証できた。既知の指数上界を準指数上界へ改善する算術入力は未取得。既存閉値域、nuclearity、unitary local return、similarity theorem、dilation のいずれも、この missing estimate を自動的に供給しない。RH は未解決であり、本監査をその解決または反証として扱わない。

## 2026-09-30 JST 追加：real interpolation と最終主文

監査開始日は 2026-09-29、以下の最終読取は 2026-09-30 JST。追加対象は `research/one_prime_return_theorem.md`、`research/one_prime_topology_matrix.md`、builder の OT3.1。

**OT3.1 は PASS。** \(w(t)=e^{2k|t|}\)、\(\tau>0\) に対し
\[
K_2(\tau,f)^2=\inf_{f=f_0+f_1}
 (\|f_0\|_2^2+\tau^2\|f_1\|_{L^2(w)}^2)
\]
の minimizer は
\[
f_1=\frac{f}{1+\tau^2w},\qquad
f_0=\frac{\tau^2wf}{1+\tau^2w}.
\]
\(f\in H_0\) なら \(f_0\in H_0\)、また
\(w/(1+\tau^2w)^2\le1/(4\tau^2)\) により \(f_1\in H_k\)。点ごとの平方完成から
\[
K_2(\tau,f)^2=\int |f(t)|^2
 \frac{\tau^2w(t)}{1+\tau^2w(t)}\,dt.
\]
Tonelli、\(y=\tau\sqrt{w(t)}\)、\(x=y^2\) によって
\[
\begin{aligned}
\int_0^\infty\tau^{-2\theta}K_2(\tau,f)^2\frac{d\tau}{\tau}
 &=\frac12\int_0^\infty\frac{x^{-\theta}}{1+x}\,dx
                 \int |f(t)|^2w(t)^\theta dt\\
 &=\frac{\pi}{2\sin(\pi\theta)}\|f\|_{H_{\theta k}}^2,
 \qquad0<\theta<1.
\end{aligned}
\]
通常の \(K\) には各分解に対する二成分 \(\ell^1/\ell^2\) 比較から \(K_2\le K\le\sqrt2K_2\)。従って usual real interpolation norm は \(H_{\theta k}\) と等価であり、同じ exact norm とは主張しない。その等価定数は反復数に依存しないので、漸近指数率が \(\theta k\) になることと評価保持閾値は正しい。

**主文と比較表の数学的 scope は PASS。** Level 1 と限定 Level 2 は、抽象 implication と全零点の bounded nonzero functional を残す \(X_1\) まで。全零点の相対位置を定義へ埋め込んでいない。既知 bound は指数的な上界であり、actual quotient の最良 bound が指数的との結論ではない。\(q_1(T_2^nx)\) の準指数制御は未証明。三つの主要構成で停止する判断は、試した構成群の停止であって、あらゆる位相・作用素プログラムへの不可能性定理ではない。

alias、多重零点の jets、uniform bound と subexponential bound の差、literal Haar source による torsion 制約は正しく限定されている。形式検証については、既存 `verification.txt` の四宣言と通常の論理公理 `propext, Classical.choice, Quot.sound` の出力を読取確認した。独立に Lean を再実行したとはしない。算術成長評価の形式化ではないという主文の限定は正しい。

最終文言として親へ次の三点を伝えた。

- 「必要条件を subexponential まで弱める」は「成長の十分条件を subexponential まで弱める」が論理的に明確。RH からその fixed-topology estimate が従うとは未証明。
- 必須八分類の対応表は topology matrix、独立監査の範囲は本ファイル、と参照を分ける。OT4 以降の全理論・全数値を独立再実行した意味にはしない。
- global quotient-growth estimate と、全指標を保持する forward intertwiner は二つの十分経路。指標別 transference から global norm estimate が出るとは示していないため、「全候補が同一の (12) へ帰着する」とはしない。

これらは主文での射程を明確にする指摘であり、上記の証明や real interpolation 定数の反例ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/one_prime/notes/abstract_return.md`](../../../reports/research/one_prime/notes/abstract_return.md)
- [`research/one_prime_return_theorem.md`](../../../reports/research/one_prime_return_theorem.md)
- [`research/one_prime_topology_matrix.md`](../../../reports/research/one_prime_topology_matrix.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `formal/Lean` — SOURCE REFERENCE NOT INCLUDED
