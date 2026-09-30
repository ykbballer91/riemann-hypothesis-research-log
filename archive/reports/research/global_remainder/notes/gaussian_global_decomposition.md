**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/global_remainder/notes/gaussian_global_decomposition.md` · Original SHA-256: `9e2fe4c412db3ba6a9acd297f402424612baaa6bed6ab7884f789485de73e7ca`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Global remainder：固定 Gaussian の全算術分解

2026-09-30。Track A の限定導出。旧ファイルを変更しない。新規性を主張せず、RH は OPEN。零点の単純性・RH・逆微分係数の評価を無条件な入力にしない。

## G1. 定義、収束、bilateral Laplace の正則域

\[
 \phi(v)=e^{-v^2},\qquad
 R(u)=\sum_{n\ge1}\mu(n)\phi(u-\log n),\qquad
 A(u)=e^{-u/2}R(u),\qquad K(s)=\sqrt\pi e^{s^2/4}.
 \tag{1}
\]
\(u\) は実数、後述の contour では複素変数を \(s\) とする。任意の \(c>1\) に対し
\[
 e^{-(u-\log n)^2}\le e^{cu+c^2/4}n^{-c}.
 \tag{2}
\]
従って固定 \(u\) の和は絶対収束し、\(u\) の compact sets 上で各階微分も一様収束する。複素 \(u\) の compact sets でも同様なので \(R,A\) は entire。これは正の実軸での成長が小さいという主張ではない。

左端では、\(u\le0\) に対して
\[
 R(u)=e^{-u^2}\left(1+O(2^{2u})\right),\qquad
 |A^{(j)}(u)|\le C_j(1+|u|)^j e^{-u^2-u/2}.
 \tag{3}
\]
最初の誤差は \(n\ge2\) で \(n^{2u}\le2^{2u}\) と
\(\sum_{n\ge2}e^{-(\log n)^2}<\infty\) を使う。微分版も \(\log n\) の有限冪を同じ収束和へ吸収すればよい。

bilateral Laplace の規約を \(\mathcal Lf(s)=\int_{\mathbb R}f(u)e^{-su}du\) と固定する。
\(\sigma=\Re s>1\) では Tonelli に使う絶対値積分は
\[
 \sum_n|\mu(n)|\int_{\mathbb R}e^{-(u-\log n)^2-\sigma u}du
 =\sqrt\pi e^{\sigma^2/4}\sum_n|\mu(n)|n^{-\sigma}<\infty.
\]
Gaussian 積分と Euler 積から
\[
 \boxed{\mathcal LR(s)=\frac{K(s)}{\zeta(s)}\quad(\Re s>1),\qquad
 \mathcal LA(z)=\frac{K(z+1/2)}{\zeta(z+1/2)}\quad(\Re z>1/2).}
 \tag{4}
\]
右辺の meromorphic continuation と、左辺の積分が収束する領域を同一視しない。
\(K\) は entire でどこにも零点を持たない。

## G2. 固定 Gaussian inversion と有限長方形

\(c>1\) を固定し、\(G_u(s)=K(s)e^{su}/\zeta(s)\) とする。Fourier inversion により
\[
 R(u)=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}G_u(s)ds.
 \tag{5}
\]
この積分は絶対収束する。\(C_c=\sum|\mu(n)|n^{-c}=\zeta(c)/\zeta(2c)\) とすると
\(\lvert\zeta(c+it)^{-1}\rvert\le C_c\)。右辺を \(|t|\le T\) に切った remainder
\(E_{c,T}(u)\) は \(T>0\) について
\[
 |E_{c,T}(u)|\le \frac{2C_c}{\sqrt\pi T}
                  e^{cu+c^2/4-T^2/4}.
 \tag{6}
\]

\(a<c\)、\(T>0\) を、長方形 \(a\le\Re s\le c,|\Im s|\le T\) の境界に
\(\zeta\) の零点がないよう選ぶ。\(s=1\) は逆数の removable zero なので許される。
\[
 \begin{split}
 V_{a,T}(u)&=\frac1{2\pi i}\int_{a-iT}^{a+iT}G_u(s)ds,\\
 H_{a,c,T}(u)&=\frac1{2\pi i}
  \left(\int_{a+iT}^{c+iT}G_u(s)ds-
              \int_{a-iT}^{c-iT}G_u(s)ds\right).
 \end{split}                                                     \tag{7}
\]
右辺の向きを含む exact identity は
\[
 \boxed{R(u)=
 \sum_{\substack{\zeta(\rho)=0\ \text{distinct}\\a<\Re\rho<c,\ |\Im\rho|<T}}
       \operatorname{Res}_{s=\rho}G_u(s)
       +V_{a,T}(u)+H_{a,c,T}(u)+E_{c,T}(u).}
 \tag{8}
\]
右辺の和は有限で、各零点を一回だけ数え、その位数は residue に含める。
counterclockwise contour の右辺は上向き、上辺は左向きであることから (7) の符号が出る。

例えば
\[
 B_{a,c}(T)=\max_{a\le\sigma\le c,\,\epsilon=\pm1}
                    |1/\zeta(\sigma+i\epsilon T)|,
\]
と置けば、有限であり
\[
 |H_{a,c,T}(u)|\le\frac{c-a}{\sqrt\pi}B_{a,c}(T)
       \exp\left(-T^2/4+\max_{a\le\sigma\le c}(\sigma^2/4+\sigma u)\right).
 \tag{9}
\]
\(V\) も
\[
 |V_{a,T}(u)|\le\frac{e^{a^2/4+au}}{2\sqrt\pi}
       \int_{-T}^T\frac{e^{-t^2/4}}{|\zeta(a+it)|}dt.
 \tag{10}
\]
これらは contour 上で測定・評価すべき量を明示した式で、small remainder を仮定していない。

## G3. Multiplicity、trivial zeros、quartets

\(\rho\) が位数 \(m\ge1\) の零点なら
\(\zeta(s)=(s-\rho)^m h_\rho(s)\)、\(h_\rho(\rho)=\zeta^{(m)}(\rho)/m!\ne0\)。
\(K(s)/h_\rho(s)=\sum_{j\ge0}b_{\rho,j}(s-\rho)^j\) と展開すれば
\[
 \operatorname{Res}_{s=\rho}G_u(s)
 =e^{\rho u}\sum_{j=0}^{m-1}b_{\rho,j}
                 \frac{u^{m-1-j}}{(m-1-j)!}.
 \tag{11}
\]
polynomial の degree は **exact に \(m-1\)**、最高係数は
\[
 \frac{b_{\rho,0}}{(m-1)!}
       =\frac{mK(\rho)}{\zeta^{(m)}(\rho)}\ne0.
 \tag{12}
\]
simple zero なら \(K(\rho)e^{\rho u}/\zeta'(\rho)\)。これは cumulative Mertens kernel
\(e^{su}/(s\zeta(s))\) ではないため、**\(1/\rho\) は現れない**。

- \(s=1\)：\(\zeta\) の pole は \(1/\zeta\) の zero。residue はない。
- \(s=0\)：\(\zeta(0)=-1/2\) なので regular。\(1/s\) を入れていない以上、residue はない。
- \(s=-2k\)、\(k\ge1\)：simple trivial zeros であり、実際に residues が出る。

simple off-line quartet \(\rho_+=1/2+\delta+i\gamma\)、\(\rho_-=1/2-\delta+i\gamma\)
とその conjugates を考える。\(c_\pm=K(\rho_\pm)/\zeta'(\rho_\pm)\) と書くと
normalized contribution は exact に
\[
 2\Re\left[e^{i\gamma u}
        \{c_+e^{\delta u}+c_-e^{-\delta u}\}\right].
 \tag{13}
\]
一般には同じ amplitude の \(\cosh(\delta u)\) ではない。
\(\zeta(s)=\chi(s)\zeta(1-s)\)、
\(\chi(s)=\pi^{s-1/2}\Gamma((1-s)/2)/\Gamma(s/2)\) から
\[
 c_-=-\chi(\overline{\rho_+})
              e^{(1-2\overline{\rho_+})/4}\overline{c_+}.
 \tag{14}
\]
この Gamma/phase factor を消して \(c_-=c_+\) と置く根拠はない。

## G4. 無条件 good heights：Gaussian に十分な弱い評価

必要なのは sharp な \(1/\zeta\) bound ではない。以下を古典的な既知入力として用いる：
\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
       =e^{A_0+B_0s}\prod_\rho(1-s/\rho)e^{s/\rho},
 \quad N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T).
 \tag{15}
\]
product は非自明零点を重複度込みで数える genus-1 product。RH は使わない。
locators は G9 に記す。以下の弱い reciprocal bound 自体は直接導出する。

\(N(j+2)-N(j-1)=O(\log j)\) なので、\([j,j+1]\) 内に
\[
 T_j\in[j,j+1],\qquad |T_j-\Im\rho|\ge d/\log j
 \tag{16}
\]
を全零点に対し満たす点がある。十分小さい固定 \(d>0\) を取り、\([j-1,j+2]\) 内の各 ordinate の
半径 \(d/\log j\) の区間を除けば、除かれる総長は1未満。外の ordinates は距離1以上。
conjugation で \(-T_j\) も同様。

固定 \(a,c\) に対して \(s=\sigma\pm iT_j\)、\(a\le\sigma\le c\) とする。
大きい \(j\) では \(|s|\le2T_j\)。\(|\rho|\le4T_j\) の factors について
\[
 \log|1-s/\rho|\ge-\log(4T_j\log j/d),\qquad
 \Re(s/\rho)\ge-|s|/|\rho|.
\]
\(N(r)=O(r\log(r+2))\) の partial summation は
\[
 \#\{|\rho|\le4T\}=O(T\log T),\quad
 \sum_{|\rho|\le4T}|\rho|^{-1}=O(\log^2T),\quad
 \sum_{|\rho|>4T}|\rho|^{-2}=O((\log T)/T)
\]
を与える。従って finite part の log modulus は \(-O(T\log^2T)\) 以上。
tail では \(|s/\rho|\le1/2\) と
\(\log|(1-w)e^w|\ge-C|w|^2\) から \(-O(T\log T)\) 以上。
\(e^{A_0+B_0s}\) の損失は \(O(T)\) に過ぎない。従って (15) と固定 strip の Stirling estimate から
\[
 \boxed{B_{a,c}(T_j)\le\exp(C_{a,c}T_j\log^2T_j).}
 \tag{17}
\]
これは explicit numerical constant を求めた certificate ではなく、定数の存在を証明した無条件 bound。
\(T\log^2T=o(T^2)\) なので (9) は compact \(u\)-sets 上で0へ行く。各固定階 \(u\)-微分を加えても成立する。
個別の \(\zeta'(\rho)\) やその逆数を評価していない。

## G5. 固定した左線への exact global decomposition

今度は \(a<0\)、\(a\notin\{-2,-4,\ldots\}\) を固定する。
functional equation と \(\Re(1-a-it)>1\) の絶対収束から
\[
 |1/\zeta(a+it)|\ll_a(1+|t|)^{a-1/2}.
 \tag{18}
\]
compact \(t\)-interval でも線上に零点はないので定数へ吸収できる。
従って \(V_a(u)=\lim_{T\to\infty}V_{a,T}(u)\) は絶対収束し
\[
 |V_a(u)|\le C_a e^{au},\qquad
 C_a=\frac{e^{a^2/4}}{2\sqrt\pi}
          \int_{\mathbb R}\frac{e^{-t^2/4}}{|\zeta(a+it)|}dt<\infty.
 \tag{19}
\]
(8) に \(T=T_j\to\infty\) を適用して
\[
 \boxed{R(u)=V_a(u)+
  \sum_{\substack{k\ge1\\a<-2k}}\frac{K(-2k)e^{-2ku}}{\zeta'(-2k)}
  +\lim_{j\to\infty}\sum_{\substack{\rho\ \text{distinct nontrivial}\\|\Im\rho|<T_j}}
                   \operatorname{Res}_{s=\rho}G_u(s).}
 \tag{20}
\]
trivial-zero sum は有限。非自明零点の和は指定された good heights で grouping し、compact \(u\)-sets 上で各固定階微分まで一様収束する。隣接する二つの good heights の contour difference に (6),(9),(18) を用いれば、**block sums** の絶対値の和も compact sets 上で収束する。
これは個々の零点項の絶対収束、任意順序の並べ替え、\(u\to\infty\) と \(j\to\infty\) の交換を認めるものではない。

特に \(a=-1\) なら trivial sum は空で、全非自明零点の grouped sum と explicit line integral だけになる。
\(e^{-u/2}V_{-1}(u)=O(e^{-3u/2})\) は \(u\to+\infty\) で小さいが、残った全 zero sum の subexponential estimate は未証明。

**無限左移動は不可。** functional equation を \(-2k\) で微分すると
\[
 \zeta'(-2k)=\frac{(-1)^k(2k)!\zeta(2k+1)}{2(2\pi)^{2k}}.
\]
従って各 trivial residue の大きさの対数は固定 \(u\) に対し
\[
 \log\left|\frac{K(-2k)e^{-2ku}}{\zeta'(-2k)}\right|
 =k^2-2ku+2k\log(2\pi)-\log((2k)!)+O(1)
 =k^2-2k\log k+O_u(k)\longrightarrow+\infty.                 \tag{21}
\]
全 trivial residues をそのまま足す級数は、項が0へ行かない。\(K(s)\) は real direction に増大し、
左線 integral が無条件に消えるという cumulative Perron kernel の推論は移植できない。

## G6. 正確な subexponential criterion：RH 同値として扱う

次の条件は新しい無条件入力ではなく **RH と同値** である。
\[
 \forall\varepsilon>0\ \exists C_\varepsilon<\infty\quad
 |A(u)|\le C_\varepsilon e^{\varepsilon u}\quad(u\ge0).
 \tag{22}
\]

**(22) ⇒ RH.** (3) と (22) により \(\mathcal LA(z)\) は \(\Re z>0\) で absolutely convergent holomorphic。
(4) から meromorphic identity theorem により
\(\zeta(z+1/2)\mathcal LA(z)=K(z+1/2)\)。右辺は非零なので \(\Re\rho>1/2\) の零点は存在しない。
functional equation の反射が \(\Re\rho<1/2\) も排除する。

**RH ⇒ (22).** 既知の RH 下の Mertens bound
\(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\) を明示的に条件付き入力とする。
Stieltjes partial summation は、境界 \(M(1^-)=0\)、無限遠の Gaussian decay により
\[
 R(u)=2\int_0^\infty M(e^v)(v-u)e^{-(u-v)^2}dv.
 \tag{23}
\]
\(\alpha=1/2+\varepsilon\) として
\[
 |R(u)|\le2C_\varepsilon e^{\alpha u}
       \int_{\mathbb R}|w|e^{-w^2+\alpha w}dw,
\]
なので (22)。同じ議論は任意の固定階 \(A^{(j)}\) にも適用できる。
Mertens bound の一次確認は Soundararajan, G9 の §1 Eq.(1)。

ここで (20) の各 off-line exponential を独立に読む必要はない。holomorphy と nonvanishing multiplier が cancellation を含めて処理する。
逆に、有限零点和の数値振る舞いだけから (22) の全 \(u\) 評価を得ることもできない。

## G7. Bounded / polynomial / tempered / L² を分ける

pointwise polynomial bound \(|A(u)|\le C(1+u)^d\)、\(u\ge0,d\ge0\) は (22) より強く、RH を含意する。
さらに critical zero \(\rho=1/2+i\gamma\) において (4) の pole order は \(m_\rho\)。
\(z=\epsilon+i\gamma\) とすると positive-halfline Laplace integral は \(O(\epsilon^{-d-1})\)、
negative-halfline contribution は entire だから
\[
 m_\rho\le d+1.                                             \tag{24}
\]
特に boundedness は全非自明零点の単純性も強制する。RH だけから boundedness や固定次数の polynomial bound を得たとは主張しない。

\(A\) の regular distribution が tempered である場合も RH が従う。実際 smooth cutoff \(\eta\) を
\(u\le-1\) で0、\(u\ge0\) で1と取ると、\(\eta A\) は右に support を持つ tempered distribution。
\(\langle\eta A,e^{-zu}\rangle\) は exponential を負側で smooth に切って Schwartz test にすれば
\(\Re z>0\) で holomorphic。\((1-\eta)A\) は (3) により entire Laplace transform を持つ。
従って再び (4) の noncancelled poles が RH を強制する。この議論は tempered distribution から pointwise polynomial bound を推測していない。
RH ⇒ temperedness はここでは得ていない。

一方、unweighted \(L^2(\mathbb R,du)\) は実際に不可能：
\[
 \boxed{A\notin L^2(\mathbb R).}                             \tag{25}
\]
証明は RH を仮定しない。仮に \(A\in L^2\) なら positive-halfline Cauchy–Schwarz から
\(\mathcal LA\) は \(\Re z>0\) で holomorphic、従って上と同様 RH が従う。
非自明零点は存在するので、その一つを \(\rho=1/2+i\gamma\) と取る。(3) と Cauchy–Schwarz により
\[
 |\mathcal LA(\epsilon+i\gamma)|
 \le \frac{\|A\|_{L^2(0,\infty)}}{\sqrt{2\epsilon}}+O_\gamma(1).
 \tag{26}
\]
しかし (4) の nonzero principal part は \(c\epsilon^{-m_\rho}(1+O(\epsilon))\)、\(m_\rho\ge1\)。
(26) と矛盾する。従ってこれは「RH 下で L² をまだ証明できない」という弱い結論ではない。
weighted L²、平均二乗密度、Besicovitch seminorm は異なる条件なので、この否定を移さない。

## G8. 既存 One-Prime Gaussian witness との関係

旧 `research/dyadic_arithmetic_reduction.md` §2 の Gaussian class は
\(g_*(t)=e^{-t^2}\in E\) と、算術商上の dual evaluations
\[
 \ell_\rho(T_2^n[g_*])=2^{n(\rho-1/2)}
             \sqrt\pi e^{(\rho-1/2)^2/4}\ne0
\]
を用いた。これは全零点を検出する **primal test vector と dual character** の組である。
今回の \(R\) は全 Möbius measure \(\sum\mu(n)\delta_{\log n}\) を Gaussian convolution した scalar observable。
normalized transform は \(K(z+1/2)/\zeta(z+1/2)\) であり、旧 witness の評価 \(K(\rho-1/2)\) とは異なる。
旧商の norm、dual eigencharacter、今回の scalar bound を同じものとして移さない。
Gaussian が zero-dependent input でない点は共通だが、(22) の必要な算術 estimate は今回も未証明である。

## G9. 一次資料の範囲と判定

- K. Soundararajan, [*Partial sums of the Möbius function*, arXiv:0705.0723v2](https://arxiv.org/pdf/0705.0723v2), §1 p.1, Eq.(1), Theorem 1：RH 下の Mertens upper bound。G6 では弱い \(x^{1/2+\varepsilon}\) だけを用いた。
- N. Ng, [*The distribution of the summatory function of the Möbius function*, author manuscript, 17 Jan 2004](https://www.cs.uleth.ca/~nathanng/RESEARCH/mobius2b.pdf), §1 pp.1–5、Lemma 3 p.12、Lemma 4 pp.13–14：cumulative kernel に \(1/s\) があること、明示式の RH/simple-zero 仮定を確認。強い good-height statement を無条件に輸入せず、G4 の弱い bound を直接証明した。重零点は (11) の一般 residue 公式で処理した。
- E. Hasanalizade, Q. Shen, P.-J. Wong, [*Counting zeros of the Riemann zeta function*](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf), JNT 235 (2022), Corollary 1.2, p.221, Eq.(1.5)：無条件 \(N(T)\) bound。G4 はその \(O(\log T)\) remainder だけを使う。
- N. Elkies, [author lecture note *The product formula for ξ(s) and ζ(s); vertical distribution of zeros*](https://people.math.harvard.edu/~elkies/M229.22/zeta2.pdf), pp.1–3, Eq.(1),(4),(6)：genus-1 product と zero count の規約を確認。この講義の \(\xi\) は poles 0,1 を残す完成関数で、こちらの entire \(\xi\) はその \(s(s-1)/2\) 倍。原発見論文を取得したとは記録しない。

**Decision:** 固定 Gaussian の global residue identity と fixed-left-line remainder は無条件に構成できる。
全 trivial zeros への無限左移動、common-amplitude quartet、unweighted L² を根拠に remainder を捨てる方法は停止。
求める (22) は RH 同値であり、Gaussian smoothing または正確な分解だけから得た新しい入力として採用しない。
個別 residue の極端な大きさを仮定せず、必要な grouping と未証明な全 \(u\) 評価を分けて保存する。

独立検算：DESTROYER が G4 の genus-1 product の finite part / tail と good-height 選択、
G7 の unweighted L² 不可能性を読み取り再導出して PASS。G4 の grouping は個別留数の絶対収束を意味しないという限定も確認した。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/dyadic_arithmetic_reduction.md`](../../dyadic_arithmetic_reduction.md)
