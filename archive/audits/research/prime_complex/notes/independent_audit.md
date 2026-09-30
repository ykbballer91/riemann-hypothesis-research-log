**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_complex/notes/independent_audit.md` · Original SHA-256: `ce56a5a6b2b1dec88063b05bfcbadabddbd3c8063f519ca3ea9d854ed7f67389`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime complex：matching・homology・Hodge の独立監査

2026-09-30。旧ファイルは変更しない。RH は未解決。以下は prime complex の指定された機構だけを検査し、RH や Mertens の符号相殺一般に対する不可能性を主張しない。

**判定：** prime (2) の matching の unmatched faces は、odd squarefree (n\in(X/2,X]) に正確に対応する。その総数は reduced Betti 数の総和にも等しく、\(2X/\pi^2+O(\sqrt X)\)。従って acyclic Morse critical cells または通常の正定値 inner product による reduced Hodge kernel の**総次元**を平方根規模にする案は不可能。Mertens 関数はその偶奇の**差**であり、この相殺は否定も証明もされない。

独立に cone-collapse と chain basis を導出した後、既刊論文と照合した。上の homotopy・Betti formula 自体は既知であり、新規性はない。一次資料は [Björner, *A cell complex in number theory*, arXiv:1101.5704v1](https://arxiv.org/pdf/1101.5704v1)：p.2 Eq.(1.1)–(1.2) は Euler の符号、p.5 Theorem 3.1 は個々の Betti 数、pp.5–6 Theorem 3.4 は総和。後者にはここで必要なものより強い誤差評価がある。

## PC1. 複体と符号

実数 (X\ge2) に対し
\[
\Delta_X=\{\sigma_n=\{p:p\mid n\}: n\le X\text{ squarefree}\}
\]
と定義する。整数 (1) は empty face に対応し、augmented chain complex の次数は
\[
\deg\sigma_n=\omega(n)-1,
\quad \widetilde C_{-1}=\mathbb R\,[\varnothing].
\]
素数を増加順に orientation 付け、
\(\partial[p_1,\ldots,p_k]=\sum_{i=1}^k(-1)^{i-1}[p_1,\ldots,\widehat p_i,\ldots,p_k]\)
とする。特に \(\partial[p]=[\varnothing]\)。

\[
\widetilde\chi(\Delta_X)
=\sum_{n\le X\atop n\text{ sf}}(-1)^{\omega(n)-1}
=-\sum_{n\le X}\mu(n)=-M(X).                         \tag{PC1.1}
\]

従って homological degree による supertrace は \(-M(X)\)。cardinality \(\omega(n)\) を grading に採るなら全符号が一つ反転し、supertrace は (M(X))。この二つを混ぜない。普通の Euler characteristic は \(1-M(X)\) である。

## PC2. Toggle-(2) matching の acyclicity

odd squarefree (m\le X/2) を \(m\leftrightarrow2m\) と対にする。全ての even face は一意に対を持ち、unmatched は
\[
\mathcal C_X=\{n:X/2<n\le X,\ n\text{ odd squarefree}\}.   \tag{PC2.1}
\]
下向きの face-incidence arrows のうち matched edge だけを逆向きにすると、上向き arrow は (2) を追加するものだけ。各下向き arrow は odd prime を除き、その個数を厳密に減らす。(2) を除く arrow は全て matched なので、下向きには存在しない。従って有向 cycle はなく、matching は acyclic。

これは augmented matching であり、empty face と vertex (2) も対にしている。通常の nonaugmented discrete Morse convention ではこの一対を使わず、基点となる vertex (2) が追加の critical (0)-cell になる。reduced と ordinary の critical count の差 (1) を落とさない。

## PC3. 全 homology を捉えることの独立証明

### PC3.1. Cone collapse

\(A=\operatorname{star}_{\Delta_X}(2)\) は
\[
A=\{\sigma_m:m\le X/2,\ m\text{ odd sf}\}
\ \cup\ \{\sigma_{2m}:2m\le X,\ m\text{ odd sf}\}
\]
であり、vertex (2) を頂点とする nonempty contractible cone。

(A) の外の simplex は正確に (PC2.1) である。(n\in\mathcal C_X) の任意の proper face の積 (d) は、ある odd prime (p\ge3) を除くので
\(d\le n/3\le X/3<X/2\)。従って boundary 全体が (A) に入る。外の simplex 同士は inclusion を持たない。

finite CW subcomplex (A) の包含は cofibration。contractible な (A) を一点へ潰す quotient map は homotopy equivalence であり、各外 simplex はその boundary を基点へ潰される。従って
\[
\boxed{\Delta_X\simeq
\bigvee_{n\in\mathcal C_X}S^{\omega(n)-1}.}             \tag{PC3.1}
\]
degree (0) の場合は (S^0) を含む pointed wedge と読む。これは孤立した vertices も正しく数える。

### PC3.2. Augmented chain normal form と filtration

odd squarefree (n) に対し、無限 full simplex で
\[
b_n=[2,\sigma_n],\qquad z_n=\partial b_n
=\sigma_n-2*\partial\sigma_n
\]
を定義する。(z_n) の偶数 face の積は (2n/p<n)（(p\mid n\) は odd）。従って (n\le X) なら (z_n\in\widetilde C_*(\Delta_X)) であり、(b_n) 自体がまだ複体にない場合にも (z_n) は定義できる。

自然な odd basis \(\sigma_n\) を (z_n) に置き換え、even basis (b_n) は変えない。leading coefficient が (1)、他の項は全てより小さい積なので、これは **整数上でも unimodular な filtered basis change**。この基底では
\[
\partial b_n=z_n,\qquad\partial z_n=0.
\]
従って (n\le X/2) は二項 acyclic summand、(X/2<n\le X) は一項 homology summand となる。特に
\[
\widetilde\beta_k(\Delta_X)
=\#\{n\in\mathcal C_X:\omega(n)=k+1\}.                \tag{PC3.2}
\]
torsion はない。積 (X) による filtration の reduced barcode は、各 odd squarefree (n) について degree \(\omega(n)-1\) の interval \([n,2n)\)。(n=1) は degree (-1) の interval \([1,2)\) であり、今回 (X\ge2) では残らない。

この basis change は一般に orthogonal ではない。従って自然な simplex inner product の Laplacian の非零 spectrum が (0,1) だけになるとは言えない。chain isomorphism、barcode、kernel の次元と unitary spectral equivalence は別の statement である。

## PC4. 総 Betti 数の線形増大：初等的な全 (X) 証明

(A(Y)=\#\{n\le Y:n\text{ odd squarefree}\}\) とする。\(\mu^2(n)=\sum_{d^2\mid n}\mu(d)\) により
\[
A(Y)=\sum_{d\le\sqrt Y\atop d\text{ odd}}\mu(d)
 \left(\frac{Y}{2d^2}+O(1)\right).
\]
この有限和の誤差は (O(\sqrt Y))。無限級数への tail も (Y\sum_{d>\sqrt Y}d^{-2}=O(\sqrt Y)) なので
\[
A(Y)=\frac Y2\prod_{p\ne2}(1-p^{-2})+O(\sqrt Y)
=\frac{4Y}{\pi^2}+O(\sqrt Y).
\]
従って
\[
\boxed{B(X):=\sum_k\widetilde\beta_k(\Delta_X)
=A(X)-A(X/2)=\frac{2X}{\pi^2}+O(\sqrt X).}              \tag{PC4.1}
\]
この証明は PNT、RH、Mertens の符号相殺を使わない。

acyclic face matching が与える Morse chain complex は critical cells を基底に持ち、元の homology を保つ。従って各次数で critical cell 数は Betti 数以上、総数は (B(X)) 以上。toggle-(2) は reduced convention で等号を達成する。よって critical 総数 (O(X^{1/2+\epsilon})) を全 \(\epsilon>0\) について求める案は、例えば固定 \(0<\epsilon<1/2\) ですでに不可能である。

## PC5. 正定値 Hodge theory が与えるものと与えないもの

有限 augmented chain groups に任意の正定値 inner products を入れ、
\(\mathcal L=\partial\partial^*+\partial^*\partial\) と置く。
\[
\langle\mathcal L v,v\rangle=\|\partial v\|^2+\|\partial^*v\|^2\ge0,
\quad \ker\mathcal L_k\simeq\widetilde H_k(\Delta_X;\mathbb R).
\]
従って重みの選択にかかわらず
\[
\dim\ker\mathcal L=B(X)\sim2X/\pi^2.                  \tag{PC5.1}
\]
ordinary chain complex なら通常の (H_0) の基点分が加わり、総次元は (B(X)+1)。

homological grading で有限次元 heat supertrace は
\[
\operatorname{Str}(e^{-\tau\mathcal L})
=\sum_k(-1)^k\widetilde\beta_k(\Delta_X)
=-M(X)\quad(\tau\ge0).                               \tag{PC5.2}
\]
正の eigenvalues の parity pairing により supertrace では相殺する。一方 ordinary trace は
\(\operatorname{Tr}(e^{-\tau\mathcal L})\ge B(X)\) なので、正性による絶対値化だけでは平方根規模に届かない。

signed identity 自体は
\[
M(X)=\sum_{n\in\mathcal C_X}(-1)^{\omega(n)}.           \tag{PC5.3}
\]
odd squarefree の低い部分とその (2) 倍が相殺するという直接の Möbius identity と同じである。linear-sized な二つの parity subspaces の差を小さくする追加の算術評価を、Hodge 正性や dimension の小ささから得たことにはならない。別の nonlocal parity map の存在一般を否定する結論でもない。

## PC6. Acyclicity 不要の face-incidence matching 障害

さらに広い class として、face の prime insertion/removal edge だけを使う任意の matching を考える。cycle を許しても以下は変わらない。

prime (p\in(X/2,X]) の singleton face \(\{p\}\) は上方 coface を持たず、augmented Hasse diagram における唯一の隣接は empty face。empty face は高々一度しか対に使えない。従って
\[
\#\mathrm{unmatched}\ge\pi(X)-\pi(X/2)-1
\sim\frac{X}{2\log X}.                               \tag{PC6.1}
\]
最後の漸近だけは PNT を使う。一次参照の Björner Theorem 2.3(b), Remark 2.4(ii) も prime count をこの規約で採用している。nonaugmented matching なら右辺の (-1) は不要。

固定 \(\delta>0\) に対し \(X/(\log X)\) は (X^{1-\delta}) より大きくなるため、**any** face-incidence matching で unmatched 総数 (O(X^{1-\delta})) を達成することもできない。PC4 の線形下界は acyclicity を必要とするが、このより弱い下界には不要である。対象は incidence matching であり、任意の整数ペアリングや chain basis の非局所線形変換ではない。

## PC7. Large-prime decomposition の collision と recursion

(p>\sqrt X\) なら、(n\le X) はこの範囲の prime を高々一つしか含まない。しかし (n=pm\) から parent (m) への map は injective ではない。最小の例として (X=5) では faces \(\{3\},\{5\}\) が両方とも empty face を唯一の parent に持つ。各整数の large prime が一意であることは matching の衝突回避を意味しない。

topological decomposition 自体は正しい。small-prime core (K_0\) を (p\le\sqrt X\) だけを使う faces とすると
\[
\Delta_X=K_0\ \cup\!
\bigcup_{\sqrt X<p\le X}p*\Delta_{X/p}.
\]
各 base \(\Delta_{X/p}\) は (K_0) に入るが、これらは互いに重なり、empty face を必ず共有する。別々の cone の elementary cancellation を、共通 parent を再使用して simultaneous matching と呼ぶことはできない。

一般の prime (p) に対する deletion/link identity は
\[
\Delta_X=D_p(X)\cup p*D_p(X/p),\qquad
\widetilde\chi(\Delta_X)
=\widetilde\chi(D_p(X))-\widetilde\chi(D_p(X/p)),
\]
ただし (D_p(Y)) は (p\nmid n\) の faces だけの複体。これは
\[
M(X)=M_p(X)-M_p(X/p),\qquad
M_p(Y)=\sum_{n\le Y,\ p\nmid n}\mu(n)
\]
という既知の符号付き分割そのもの。cone が contractible という事実だけから、union の homology が小さいとは従わず、attachment と connecting maps が残る。

同様に unique large-prime factor による正確な数論的分割は
\[
M(X)=\sum_{n\le X\atop P^+(n)\le\sqrt X}\mu(n)
-\sum_{\sqrt X<p\le X}M(X/p),                          \tag{PC7.1}
\]
(n=1) は第一和に入れる。各 (X/p<\sqrt X) の寄与を Mertens 値として再投入するので、これだけで新しい cancellation bound を得たことにはならない。再帰式としての正しさと、符号を保持した定量制御は別の義務である。

## PC8. 終了判定と監査範囲

| 候補・statement | 判定 | 残る意味 |
|---|---|---|
| toggle-(2) の acyclicity と unmatched set | PASS | actual finite complex の厳密な構成 |
| 全 reduced Betti 数が unmatched count に一致 | PASS、既知 | wedge と integral filtered chain basis の双方で確認 |
| critical 総数・Hodge kernel 総次元の平方根化 | 不可能 | 総次元は \(2X/\pi^2+O(\sqrt X)\) |
| cycle を許す incidence matching の polynomial saving | 不可能 | singleton primes だけで \(\gg X/\log X\) |
| large prime の一意性から parent の injectivity | 偽 | (X=5\)、(3,5\mapsto1\) |
| cone/deletion identity だけで signed cancellation | 未供給 | exact identity は Mertens 型和を残す |
| nonlocal parity transfer 全般 | 今回の否定対象外 | 別の具体的 map と見積りが必要 |

本ファイルでは数値実験を実行していない。有限 enumeration が全 (X) の根拠なのではなく、PC3–PC7 の解析・代数証明が判定の根拠である。原論文の一部の既知結果との一致を確認したが、原論文全体の新規監査や最近の別論文への評価は行っていない。
