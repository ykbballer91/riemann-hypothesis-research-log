**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_complex/notes/matching_persistence.md` · Original SHA-256: `7f87a06502ceeac40dec47e149cada47256b7d18fd48fd4195ab86d1757d19ec`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime complex：toggle 2、完全 matching、exact persistence

2026-09-30。独立の有限鎖計算。既存ファイルは変更しない。RH は OPEN。shifted complex と Betti 数の公式は既知であり、本ノートの barcode 表示についても新規性を主張しない。

**結論。** 素数2を toggle する matching は acyclic かつ reduced の意味で perfect。odd squarefree \(n\) ごとに、degree \(\omega(n)-1\) の区間 \([n,2n)\) がちょうど一つある。これは各時点の Betti 数だけの一致ではなく、整数係数の filtered chain basis による直接分解である。\(n=1\) は augmented degree \(-1\) の例外を表す。

## MP1. 複体と augmentation の規約

\(X\ge1\) に対し
\[
 \Delta_X=\{S:\ S\text{ は素数の有限集合},\ w(S):=\prod_{p\in S}p\le X\},
 \qquad w(\varnothing)=1.
\]
これは squarefree integers \(n\le X\) を faces とする有限複体。\(S\) の次元は \(|S|-1\)。以下の \(C_*(\Delta_X;\mathbb Z)\) は **augmented** simplicial chain complex であり、\(C_{-1}=\mathbb Z[\varnothing]\)、\(\partial[p]=[\varnothing]\)、\(\partial[\varnothing]=0\) とする。頂点は増加順に向きを付ける。通常の reduced homology とこの鎖複体の homology を同定する。

\(1\le X<2\) では \(\Delta_X=\{\varnothing\}\)。幾何的実現は空、\(\widetilde H_{-1}=\mathbb Z\)、他は0である。\(X\ge2\) では頂点2があり、\(\widetilde H_{-1}=0\)。\(X<1\) まで filtration を拡張するなら void complex と zero chain complex を採用すれば以下の \([1,2)\) と整合する。逆に \(X<1\) でも空 face を強制的に含める規約なら、その degree \(-1\) bar の出生端だけが変更される。本ノートの基本パラメータは \(X\ge1\) である。

係数を field に制限する必要はない。鎖の基底変換は整数上で行い、最後に任意の係数へ移せる。

## MP2. 素数 insertion matching と2の役割

固定素数 \(p\) に対し、\(p\notin S\) かつ \(p\,w(S)\le X\) の組
\[
 S\longleftrightarrow S\cup\{p\}
\]
を match する。Hasse graph の matched edge を上向き、他を下向きに orient すると acyclic である。実際、上向きの一歩は \(p\) を追加する。その後 \(p\) を削除する edge は必ず matched edge なので下向きには通れず、ほかの頂点を削除する下向きの道しか残らない。従って上向き edge を含む有向閉路はない。上向き edge を含まない閉路も次元が減少するため不可能。

\(p=2\) の unmatched faces は正確に
\[
 \mathcal U_X=\{S_n:n\text{ odd squarefree},\ X/2<n\le X\}.
 \tag{1}
\]
ここで \(S_n\) は \(n\) の素因数集合、\(S_1=\varnothing\)。全ての even squarefree face はその2を削除した face と match される。

通常の非空 face poset で Morse matching を定義する場合は \(\varnothing\leftrightarrow\{2\}\) を除く。この場合、\(X\ge2\) では基点を表す critical vertex \(\{2\}\) が一つ余分に残る。従って「critical count = total **reduced** Betti」は augmented matching の記述であり、ordinary CW の critical count にはその一個を加える。

**任意の素数で perfect になるわけではない。** \(p=3,X=10\) では matched pairs は \(\varnothing\leftrightarrow\{3\}\) と \(\{2\}\leftrightarrow\{2,3\}\)。critical faces は \(\{5\},\{7\},\{2,5\}\) の三個だが、複体は edges \(\{2,3\},\{2,5\}\) の木と孤立点7なので total reduced Betti は1。critical differential が消える根拠に acyclicity だけを使ってはならない。

## MP3. 整数係数の filtered chain basis

odd squarefree \(n=p_1\cdots p_k\)、\(3\le p_1<\cdots<p_k\) に対し、全素数 simplex の formal chains として
\[
 \sigma_n=[p_1,\ldots,p_k],\quad
 b_n=[2,p_1,\ldots,p_k],\quad
 z_n:=\partial b_n=\sigma_n-[2]*\partial\sigma_n.
 \tag{2}
\]
\([2]*\) は2を先頭に追加する cone operation。\(n=1\) では \(\sigma_1=z_1=[\varnothing]\)、\(b_1=[2]\)。常に
\[
 \partial b_n=z_n,\qquad \partial z_n=0.
 \tag{3}
\]
\(b_n\) がまだ \(\Delta_X\) に属さないときも、(2) は大きな formal simplex の boundary として定義してよい。\(z_n\) の全項が \(\Delta_X\) 内にあるかを次で検査する。

\(z_n\) の odd term \(\sigma_n\) の weight は \(n\)。他の各項は \([2]*\sigma_{n/p_j}\) で weight
\[
 2n/p_j\le 2n/3<n.
 \tag{4}
\]
従って \(z_n\) の filtration birth は正確に \(n\)、\(b_n\) の birth は \(2n\)。各 \(X\) における鎖の基底は
\[
 \boxed{\{z_n:n\text{ odd squarefree},\ n\le X\}
       \ \cup\ \{b_n:n\text{ odd squarefree},\ 2n\le X\}.}
 \tag{5}
\]
degree はそれぞれ \(\omega(n)-1\)、\(\omega(n)\)。

**基底である証明。** 古い odd simplex \(\sigma_n\) を、その係数が1で残る \(z_n\) に置換する。差に現れるのは変更しない even basis vectors \(b_{n/p_j}\) だけであり、(4) により同じ filtration stage に存在する。逆変換は \(\sigma_n=z_n+[2]*\partial\sigma_n\) で与えられる。従って整数係数の可逆変換であり、両方向とも filtration を保つ。全 \(X\) で同じ vector を用いるので inclusion とも整合する。

この証明は単なる Morse inequalities ではない。filtered chain complex 全体を、odd squarefree \(n\) ごとの二項複体
\[
 \mathbb Z b_n\xrightarrow{\ 1\ }\mathbb Z z_n
 \quad\text{（births }2n,n\text{）}
 \tag{6}
\]
の直和へ明示的に分解している。

## MP4. Homology basis、barcode、inclusion の正確な作用

各時点で (6) を切ると、\(n\le X<2n\) のときだけ \(z_n\) の homology class が残る。従って
\[
 \boxed{\widetilde H_d(\Delta_X;\mathbb Z)
   =\bigoplus_{\substack{n\ {m odd\ squarefree}\\X/2<n\le X\\\omega(n)=d+1}}
             \mathbb Z[z_n].}
 \tag{7}
\]
特に torsion はない。critical count は degree ごとに reduced Betti 数と一致する。

任意の field \(\Bbbk\) 上の reduced persistence module は
\[
 \boxed{\widetilde H_d(\Delta_\bullet;\Bbbk)
       \cong\bigoplus_{\substack{n\ {m odd\ squarefree}\\\omega(n)=d+1}}
                         \Bbbk_{[n,2n)}.}
 \tag{8}
\]
同じ表示は interval module の係数を \(\mathbb Z\) とした直接分解としても成立する。出生端は含み、消滅端は含まない。\(X\le Y\) の inclusion は surviving label \(n\) を同じ \([z_n]\) に送り、\(Y\ge2n\) なら \(\partial b_n\) として0に送る。したがって
\[
 \operatorname{rank}(\widetilde H_d(\Delta_X)\to\widetilde H_d(\Delta_Y))
 =\#\{n\text{ odd squarefree}:Y/2<n\le X,\ \omega(n)=d+1\}.
 \tag{9}
\]

最小例は次の通り。

| \(n\) | cycle | degree | reduced interval |
|---:|---|---:|---|
| 1 | \([\varnothing]\) | \(-1\) | \([1,2)\) |
| 3 | \([3]-[2]\) | 0 | \([3,6)\) |
| 5 | \([5]-[2]\) | 0 | \([5,10)\) |
| 7 | \([7]-[2]\) | 0 | \([7,14)\) |
| 15 | \([3,5]-[2,5]+[2,3]\) | 1 | \([15,30)\) |

ordinary \(H_0\) を使うなら、頂点2により出生する一本の永続区間 \([2,\infty)\) が追加される。reduced と ordinary の barcode を混同しない。

## MP5. Wedge of spheres の直接証明と shifted 性

\(X\ge2\) とする。\(A_X=\operatorname{star}_{\Delta_X}(2)\) は、odd faces \(w(S)\le X/2\) の複体に頂点2を cone したものなので nonempty contractible subcomplex。

\(A_X\) の外の simplices は (1) の critical faces に一致する。その任意の proper face の weight は、取り除いたある素数 \(p\ge3\) に対して高々 \(n/p\le n/3\le X/3<X/2\) なので boundary 全体が \(A_X\) に入る。また外の二つの faces は包含関係を持たない。よって \(A_X\) を一点へ潰すと
\[
 |\Delta_X|/|A_X|
 \cong\bigvee_{\substack{n\ {m odd\ squarefree}\\X/2<n\le X}}
                    S^{\omega(n)-1}.
 \tag{10}
\]
有限 CW subcomplex の inclusion は cofibration であり、nonempty contractible subcomplex を潰す quotient map は homotopy equivalence。この標準補題は contraction の homotopy extension から従う。従って (10) は \(\Delta_X\) の homotopy type を与える。次元0では孤立頂点と基点の対を \(S^0\) と読み、球が一つもなければ wedge は一点とする。\(X<2\) の空の実現にはこの collapse の議論を適用しない。

shifted 性も直接分かる。face 内の素数 \(q\) を、face 内にない小さい素数 \(p<q\) に置換すると weight が減るため、再び face になる。ただし (10) の証明は一般の shifted-complex theorem を仮定せず、この2-cone の構造を使った。

## MP6. 全ての bar が短くても、homology は線形に増える

augmented chain homotopy を
\[
 h\sigma=\begin{cases}[2]*\sigma,&2\notin\sigma,\\0,&2\in\sigma\end{cases}
 :C_d(\Delta_X)\longrightarrow C_{d+1}(\Delta_{2X})
\]
と置く。empty face にも \(h[\varnothing]=[2]\) とする。(2) の符号で直接計算すると
\[
 \partial h+h\partial=\iota_{X,2X}.
 \tag{11}
\]
従って \(\Delta_X\to\Delta_{2X}\) は全ての reduced homology 上で0。幾何的にもその像は \(\Delta_{2X}\) の \(\operatorname{star}(2)\) に含まれる。対数パラメータ \(u=\log X\) では全ての reduced bar の長さは正確に \(\log2\)。

それでも \(X\ge2\) における total reduced Betti number は
\[
 B(X)=\#\{n\text{ odd squarefree}:X/2<n\le X\}
       =\frac{2X}{\pi^2}+O(\sqrt X).
 \tag{12}
\]
この粗い漸近式は初等的に証明できる。\(\mu^2(m)=\sum_{d^2\mid m}\mu(d)\) を odd \(m\le Y\) で和を取ると
\[
 \#\{m\le Y:m\text{ odd squarefree}\}
 =\frac Y2\sum_{d\ {m odd}}\frac{\mu(d)}{d^2}+O(\sqrt Y)
 =\frac{4Y}{\pi^2}+O(\sqrt Y).
\]
有限和から無限和への tail は \(O(Y/\sqrt Y)\)、odd multiple の counting error は \(O(\sqrt Y)\)。Euler product の値は \(\prod_{p>2}(1-p^{-2})=8/\pi^2\)。\(Y=X,X/2\) の差が (12) である。

また実数または複素数係数の各有限 augmented total chain space に任意の正定値 inner product を入れ、実際の simplicial boundary を \(d=\partial\)、その adjoint を \(d^*\) とする。\(D_X=d+d^*\) は self-adjoint で
\[
 \|D_Xv\|^2=\|dv\|^2+\|d^*v\|^2,\qquad
 \dim\ker D_X=\dim(\ker d/\operatorname{im}d)=B(X).
 \tag{13}
\]
最初の式は \(d^2=0\) による。有限次元 Hodge decomposition で harmonic representative が一意に存在するため第二式が従う。従って metric の変更はこの kernel dimension を減らさない。これは向き付き boundary の \(d+d^*\) についての主張であり、別に定義する unsigned prime-shift operator と同一視しない。

(11) の短寿命と (12)–(13) の線形成長が同時に成立する。従って「persistence が有限だから未消去 homology や harmonic kernel も小さい」という推論は、この actual arithmetic complex 自体によって否定される。何か別の norm を使った具体的 cancellation estimate の可否まで否定したわけではない。

## MP7. Möbius 符号、既知性、停止点

matching された \(n,2n\) の Möbius 符号は相殺するので、全 \(X\ge1\) で
\[
 M(X)=\sum_{m\le X}\mu(m)
     =\sum_{\substack{n\ {m odd\ squarefree}\\X/2<n\le X}}\mu(n)
     =-\widetilde\chi(\Delta_X).
 \tag{14}
\]
\(X\ge2\) では \(M(X)=-\sum_{d\ge0}(-1)^d\widetilde\beta_d\)。\(1\le X<2\) では degree \(-1\) の contribution を含める必要がある。Betti 数は非負でも、(14) は次元の parity による signed sum である。barcode を完全に記述しただけでは、この和の平方根規模の cancellation は得られない。

一次資料の限定照合：Anders Björner, [*A cell complex in number theory*, arXiv:1101.5704v1](https://arxiv.org/html/1101.5704v1), §1 (1.1)–(1.2) が Euler–Mertens 関係、Theorem 2.1 が shifted complex の wedge と Betti 公式、Theorem 3.1 / (3.1) が本ノートと同一の squarefree complex の shifted 性と odd-interval count を与える。これらの fixed-stage 結果は既知。本ノートは (2)–(6) から inclusion-compatible な interval decomposition を直接示したが、先行研究全体を調査していないため persistence 表示の新規性も主張しない。既知の Mertens/RH 同値条件を新しい入力とは扱わない。

**独立監査。** DESTROYER が MP3 の filtration-preserving basis、\(n=1\) の augmented exception、MP5 の contractible star quotient を独立検算し PASS。これは他の spectral / arithmetic bridge の検証を意味しない。

**Decision:** exact matching、homotopy type、整数係数 homology basis、barcode、doubling inclusion の null homotopy を保持する。これらは計算可能な構造であるが、Möbius parity cancellation や actual ζ zero spectrum の正値実現を供給していない。RH は OPEN。
