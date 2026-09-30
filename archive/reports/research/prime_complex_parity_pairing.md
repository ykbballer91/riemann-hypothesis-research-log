**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_complex_parity_pairing.md` · Original SHA-256: `bfd37bf8a70051af4f11665c9d2b089dba787ae7ef18dfe0fe4ddeeb0f36fd4e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime Complex Parity Pairing / Topological Cancellation

2026-09-30。独立探索完了。RH は **OPEN**。既存 Phase I–IV、Continuous Scale Flow、
One-Prime Return、Dyadic Reduction のファイル・state・proof graph は変更しない。

**結論：自然な明示的 parity pairing は存在する。しかし、その未対応部分は線形規模で、
この複体の homology 自体がその線形個数を必要とする。** Stage A/B を達成・再確認した。
Morse critical cells または Hodge kernel の総数を小さくするルートは反証された。
非局所的な算術 pairing 全般、Mertens の符号相殺、RH を反証したわけではない。

主要な fixed-stage 結果は既知である。[Björner, 1101.5704v1, Eqs.(1.1)–(1.2),
Thms.2.1, 3.1, 3.4](https://arxiv.org/html/1101.5704v1) と一致することを確認した。
以下は直接の構成・反証と、その証明上の意味を固定する記録。新規性を主張しない。

## 1. 複体・符号・次数

\[
 \Delta_X=\{S:S\text{ is a finite prime set},\ \prod_{p\in S}p\le X\},
 \quad X\ge1,\quad\prod\varnothing=1.
\]
squarefree n の face を sigma_n、omega(n)=|sigma_n| と書く。empty face n=1 を含む。
augmented chain degree は omega(n)-1、境界は増加順の素数に通常の交代符号を付ける。
特に boundary[p]=[empty]。この規約で
\[
 M(X)=-\widetilde\chi(\Delta_X)
     =-\sum_{k\ge-1}(-1)^k\widetilde\beta_k(\Delta_X).        \tag{1}
\]
X>=2 では degree -1 の homology は 0。ordinary Euler は 1-M(X) である。
parity を homological degree でなく face cardinality omega に取れば index の符号が
反転し、M 自身になる。偶数「次数」と偶数「素因数個数」を混ぜない。

Knill の squarefree 整数の divisibility graph の clique complex は、nonempty faces
の order complex、すなわち本複体の barycentric subdivision。
[Knill, 1608.06877v1, §§1.1, 3.4](https://arxiv.org/pdf/1608.06877v1) と対応する。
素数だけを頂点にして pq<=X を辺とする graph の flag completion は別物。
X=15 で辺 6,10,15 はあっても face {2,3,5} の積30は許されず、flag completion は
元の1-cycleを誤って埋める。

## 2. 第一候補：素数2の挿入／除去

奇 squarefree m<=X/2 について
\[
                 \sigma_m\longleftrightarrow\sigma_{2m}      \tag{2}
\]
と対応させる。互いに一意、cutoff を保ち、parity が反転する。matched Hasse edge を
上向きにすると、上向き移動は2の追加だけ。追加後は2を除く edge を下向きには
通れず、他の下向き移動では odd vertices が減るので cycle はない。

未対応部分は独立に明示できる：
\[
 \boxed{\mathcal U_X=
 \{n:X/2<n\le X,\ n\text{ odd squarefree}\}.}                \tag{3}
\]
従って exact bulk cancellation はある：
\[
                 M(X)=\sum_{n\in\mathcal U_X}(-1)^{\omega(n)}.\tag{4}
\]
これは |M(X)| 個を恣意的に残した定義ではない。しかし |U_X| は小さくない。

### 同じ homology を保つ限り、これ以上 critical 数は減らない

A_X=star(2) は contractible cone。外にある face は正確に U_X。
その proper face は odd prime q>=3 を少なくとも一つ除くので積が n/q<=X/3<X/2。
従って全境界が A_X 内に入る。A_X を一点に潰すと
\[
 \Delta_X\simeq\bigvee_{n\in\mathcal U_X}S^{\omega(n)-1},
 \qquad
 \widetilde\beta_k=\#\{n\in\mathcal U_X:\omega(n)=k+1\}.      \tag{5}
\]
通常の nonaugmented Morse convention では基点 {2} が追加の critical 0-cell であり、
critical 総数は 1+|U_X|。以下の数は reduced/augmented のもの。

odd squarefree 計数 Q_odd(Y) には、mu²(m)=sum_{d²|m}mu(d) と絶対収束 Euler product から
\[
 Q_{\rm odd}(Y)=\frac Y2\prod_{p>2}(1-p^{-2})+O(\sqrt Y)
               =\frac{4Y}{\pi^2}+O(\sqrt Y).
\]
よって RH、PNT、Mertens の符号相殺を使わず
\[
 \boxed{|\mathcal U_X|=\sum_k\widetilde\beta_k
                  =\frac{2X}{\pi^2}+O(\sqrt X).}             \tag{6}
\]
Björner はより強い既知の誤差評価も述べるが、ここでは初等的な (6) だけで十分。
全 squarefree faces は約6X/pi²、そのうち約4X/pi²が対になり、約2X/pi²が残る。
固定比率の bulk cancellation であり、near-perfect な o(X) cancellation ではない。
log 座標の境界幅が log2 と固定でも、その中の face 数は線形に増える。

Morse inequalities により任意の acyclic matching の critical 数は Betti 数以上。
(2) は既に各次数で最小値を達成している。
**同じ複体の acyclic Morse matching による Stage C=o(X) は不可能。**

「smallest admissible prime を毎回選ぶ」naive rule は involution ですらない。
X=5 で {3}→empty→{2}。使用済みの face を管理しない rule を matching と呼べない。

## 3. 鎖レベルの完全分解と persistence

odd squarefree n=p_1...p_r に対して、全素数 simplex 内で
\[
 b_n=[2,p_1,\ldots,p_r],\qquad
 z_n=\partial b_n=\sigma_n-[2]*\partial\sigma_n.              \tag{7}
\]
b_n が cutoff 外でも、z_n の他の項の積は 2n/p_i<n なので、z_n は時刻 n に既に存在。
b_n は時刻2nに入る。全段階で、odd simplex basis を z_n に置換し even basis b_n を
残す操作は整数係数の filtered unimodular basis change である。新基底では
\[
                    \partial b_n=z_n,\qquad\partial z_n=0.   \tag{8}
\]
従ってこれは単なる Euler characteristic でなく、実際の二項鎖複体への直和分解。
各時点で common acyclic part P と未対応の偶奇 homology 部分を明示するが、残余総数は (6)。

reduced persistence barcode は厳密に
\[
 \boxed{[n,2n),\quad\text{degree }\omega(n)-1,
           \quad n\text{ odd squarefree}.}                   \tag{9}
\]
n=1 は degree -1 の [1,2)。ordinary H_0 なら [2,infinity) が別に一本加わる。
全 log-persistence length は log2。それでも、時刻Xで生きている interval は |U_X| 個。

cone homotopy h sigma=[2]*sigma（2を含むときは0）は
\[
 h:C_*(\Delta_X)\to C_{*+1}(\Delta_{2X}),\qquad
 \partial h+h\partial=\iota_{X,2X}.                          \tag{10}
\]
従って doubling inclusion の reduced homology map は零。
「全クラスが finite persistence で消えるから、その時点の kernel が小さい」は
(6)、(9)、(10) により actual complex 自身で反証される。極限の infinite simplex が
contractible でも、有限 cutoff の残差を一様に制御しない。

通常の inclusion に関する nonzero homological stability もここからは出ない。
いずれ全 reduced class は死に、固定次数の Betti 数も最終的に一定になるのではない。
prime の積を保つ自然な全 symmetric-group action も指定されておらず、通常の
representation stability theorem を自動適用する根拠はない。

## 4. 第二候補：large prime、hyperbola、recursive boundary

p>sqrt X の prime は n<=X に高々一個なので、n=pm と分離すると m<sqrt X。
この平方根閾値は積の不等式から自然に現れる。しかし m を parent とする map は
多対一。X=5 で 3 と5は共に1へ送られ、一つの empty face を二度 match できない。

さらに cycle を許す **任意の face-incidence matching** に対しても、p∈(X/2,X] の
singleton {p} は上方 coface を持たず、唯一の隣接が empty face。そのため
\[
 \#\mathrm{unmatched}\ge\pi(X)-\pi(X/2)-1
                      \sim\frac{X}{2\log X}.                \tag{11}
\]
漸近の部分だけは既知のPNTを使う。有限Xの不等式は純粋に組合せ的。
従って acyclicity を外しても、prime insertion/removal だけでは固定 delta>0 の
O(X^{1-delta}) を得られず、Stage D/E は不可能。非局所な parity pairing 全般の
反証ではない。

### 再帰的なコピーは正確に存在するが、parent は共有される

D_p(Y) を p を含まない faces の複体とすると
\[
 \Delta_X=D_p(X)\cup p*D_p(X/p),\qquad
 D_p(X)\cap(p*D_p(X/p))=D_p(X/p).                            \tag{12}
\]
link は D_p(X/p) であり、p を含む face を除かず単純に Delta_{X/p} と書いてはいけない。
reduced Euler の式は M(X)=M_p(X)-M_p(X/p) に一致し、追加の評価を生まない。

large primes p>sqrt X だけでは、bases Delta_{X/p} はすべて small-prime core に入るので
\[
 \Delta_X=K_{\le\sqrt X}\cup
                 \bigcup_{\sqrt X<p\le X}p*\Delta_{X/p}.
\]
各 cone は contractible だが、bases が互いに重なる。small parents の個数が
O(sqrt X) であることは、attachments と multiplicities がその個数で制御されることを
意味しない。m=1 だけでも約 X/log X 個の large-prime faces が集まる。
Euler 側には
\[
 M(X)=\sum_{n\le X,\,P^+(n)\le\sqrt X}\mu(n)
                         -\sum_{\sqrt X<p\le X}M(X/p)        \tag{13}
\]
が残る。これは exact decomposition であり、新しい小残差の証明ではない。

### local divisor cancellation は破れていない

各 n>1 の squarefree divisors は P(n) の full Boolean simplex を作り、
sum_{d|n}mu(d)=(1-1)^{omega(n)}=0。n<=X ならその全 divisors も <=X である。
したがって global cutoff が個別の divisor identity を破るわけではない。
異なる n の divisor simplexes が重なり、一つの face を多重に数えることが問題。
実際、局所恒等式を全部足すと
\[
 1=\sum_{d\le X}\mu(d)\lfloor X/d\rfloor,
 \quad
 M(X)=1-\sum_{d\le X/2}\mu(d)(\lfloor X/d\rfloor-1).         \tag{14}
\]
unweighted sum に戻すとこの multiplicity が残る。これを boundary defect と呼ぶだけで
Mertens 相殺を証明したことにはならない。Buchstab / largest-prime 分割も同様。

## 5. 第三候補：natural Hodge / spectral parity pairing

各 oriented simplex を orthonormal とする有限 augmented chain space で、d=boundary、
D=d+d*、L=D²=dd*+d*d とする。cardinality parity omega を +/- grading に使えば D は
odd self-adjoint、L の positive eigenspaces は D/sqrt(lambda) により偶奇で一対一になる。
これは exact な spectral pairing であり、物理的仮定は不要。

しかし Hodge theorem と (5) から
\[
 \boxed{\dim\ker D=\dim\ker L=\sum_k\widetilde\beta_k
                         =2X/\pi^2+O(\sqrt X).}             \tag{15}
\]
各次数の任意の正定値内積へ変えてもこの次元は不変。整数基底 (7) の変換は一般に
unitary ではなく、自然な Laplacian の全 spectrum が0と1になるとは主張しない。

cardinality grading なら
\[
 \operatorname{ind}(D_+)=M(X),\qquad
 \operatorname{Str}(e^{-\tau L})=M(X),\qquad
 \operatorname{Tr}(e^{-\tau L})\ge|\mathcal U_X|.              \tag{16}
\]
homological-degree grading では最初の二つの符号が反転する。
非零 modes を全て相殺しても、線形個の zero modes 間の符号相殺がそのまま残る。
positivity や短い persistence からその差を小さくすることはできていない。

任意の非局所 odd map を新しく許す場合、finite-dimensional index はその map の内容に
よらず dim C_+-dim C_-=M(X)。さらに残余の正・負基底を順番に対応させれば未対応数は
|M(X)| にできるが、それは独立な boundary bound ではなく、禁止された再記述である。
そのような map を新しい arithmetic mechanism として採用しない。

## 6. Exact experiments と synthetic gate

[check_complex.py](../../../artifacts/research/prime_complex/experiments/check_complex.py) と
[results.json](../../../artifacts/research/prime_complex/experiments/results.json) に保存した。

- X<=10000 の限定標本で、squarefree faces、matching、critical locations、parity、
  largest prime、birth/death を整数で列挙。大きな X への growth fit はしていない。
- X=1,2,3,5,10,15,30,60,100,210 の boundary ranks を有理数演算で独立計算。
  Hodge kernel も小例で exact に確認。Betti 公式と全件一致。
- 標準の F_2 boundary-matrix persistence reduction を cutoff1000で実行し、204本の
  completed intervals が正確に [n,2n) と一致。整数係数の証明は別に与えた。
- X=15 では acyclic toggle matching の未対応数3に対し、最大 incidence matching は1。
  後者は cycle を持つ。acyclic と任意 matching の障害を混同しない具体例。
- modified/equal multiplicative vertex weights、有限素数集合で同じ min-vertex 構成が
  成立することを確認。構造のかなりの部分は primes 固有ではない。
- 全整数を prime sets に写すと2と4が同じ集合になり、mu(2)=-1、mu(4)=0 を区別できない。
  squarefree の仮定を外して同じ複体を使うことはできない。

例として X=1000 では未対応200（mu=+1が101、mu=-1が99）、M=2。
X=10000では未対応2029、M=-23。有限の差が小さいことを一般の評価へ昇格しない。

## 7. Dyadic Reduction への戻りと最終判定

今回、独立に得られた absolute bound は |M(X)|<=|U_X|=O(X)、指数theta=1だけ。
以前の theta<1 を前提とする conditional estimate に theta=1 を代入してはいけない。
その端点では integral F_a の絶対可積分性が保証されず、以前の無条件評価
p_1(R_n(g))<=C2^{n/2}(1+n)p_4(g) が残る。指数改善は **0**。
新しい Mertens bound、square-root cancellation、RH-independent bridge は得ていない。

明示的 matching（第一候補）、large-prime / recursive assembly（第二候補）、
persistence / Hodge spectral pairing（第三候補）を評価した。linear critical count と
kernel count の kill condition に達し、strategy review を経て終了。別名の第4候補は
続けない。一般の未知の非局所算術 pairing まで不可能とは断定しない。

詳細な [独立監査](../../audits/research/prime_complex/notes/independent_audit.md)、
[鎖分解・persistence 証明](prime_complex/notes/matching_persistence.md)、
[文献照合](prime_complex/notes/literature.md)、
[候補比較](prime_complex_matching_matrix.md)、
[機械可読 state](../../../data/source-records/research/prime_complex_state.json)、
[持ち帰り用テキスト報告](prime_complex/completion_report.txt) を参照。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/prime_complex/completion_report.txt`](prime_complex/completion_report.txt)
- [`research/prime_complex/experiments/check_complex.py`](../../../artifacts/research/prime_complex/experiments/check_complex.py)
- [`research/prime_complex/experiments/results.json`](../../../artifacts/research/prime_complex/experiments/results.json)
- [`research/prime_complex/notes/independent_audit.md`](../../audits/research/prime_complex/notes/independent_audit.md)
- [`research/prime_complex/notes/literature.md`](prime_complex/notes/literature.md)
- [`research/prime_complex/notes/matching_persistence.md`](prime_complex/notes/matching_persistence.md)
- [`research/prime_complex_matching_matrix.md`](prime_complex_matching_matrix.md)
- [`research/prime_complex_state.json`](../../../data/source-records/research/prime_complex_state.json)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_complex.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
