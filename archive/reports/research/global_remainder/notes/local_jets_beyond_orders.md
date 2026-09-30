**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/global_remainder/notes/local_jets_beyond_orders.md` · Original SHA-256: `8f7586df35b4cb722391d433c49b407aad1071c18d0005b0448c870bf814cdec`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Track C: 有限 jets・解析 germ・全次数を超える剰余

2026-09-30。GLOBAL REMAINDER の独立限定ノート。旧 track は読取専用。本稿の構成・計算に新規性を主張しない。RH は OPEN。

**結論:** 有限個の局所係数、消失した Selberg–Delange（SD）漸近係数列、正則関数の全 Taylor 係数は異なるデータである。前二者から零点配置は決まらない。一方、正則 germ の全 Taylor 係数は解析接続を一意に決める。「同じ解析 germ なのに別の大域的 meromorphic continuation が存在する」という主張は採用できない。

## C1. Identity theorem による必須の訂正

同じ点 \(s_0\) の近傍で正則な \(F_1,F_2\) が、全 \(j\ge0\) について \(F_1^{(j)}(s_0)=F_2^{(j)}(s_0)\) を満たすなら、収束 Taylor 級数から近傍で \(F_1=F_2\)。さらに両者が同じ連結領域 \(D\) 上の一価 meromorphic functions なら、identity theorem により \(D\) 全体で一致する。極とその重複度も一致する。

これは接続の**一意性**であり、任意の germ に全平面への接続が存在すること、有限精度の係数から安定に全零点を計算できること、必要な縦方向評価が容易に得られることを保証しない。多価関数では continuation の経路・Riemann surface を指定する。本稿の \(\zeta,\xi,1/\zeta\) は既知の一価 meromorphic/entire functions を扱う。

従って正しい有限データの量化は
\[
 \forall N<\infty\quad \exists F_N\ne F:
       F_N^{(j)}(s_0)=F^{(j)}(s_0)\quad(0\le j\le N).
                                                               \tag{C1.1}
\]
\(\exists F_\infty\ne F\ \forall j\) への交換は不可能である。

## C2. 全 SD 係数の消失は Taylor germ の消失ではない

先行 [SD 監査ノート](../../weighted_prime_halfspace/notes/selberg_delange_endpoint.md) の記号を使う。算術パラメータを \(z\)、複素解析変数を \(s\) とする。
\[
 \sum_n\mu(n)^2z^{\omega(n)}n^{-s}=\zeta(s)^zG(s,z),\qquad
 B(s,z)=\frac{((s-1)\zeta(s))^zG(s,z)}s
       =\sum_{j\ge0}h_j(z)(s-1)^j.
\]
SD 係数は \(\lambda_j(z)=h_j(z)/\Gamma(z-j)\)。\(z=-1\) で \(G(s,-1)=1\) だが、
\[
 \frac1{\zeta(1+w)}=w-\gamma w^2+O(w^3),\qquad
 B(1+w,-1)=1-(1+\gamma)w+O(w^2).                    \tag{C2.1}
\]
従って \(h_0(-1)=1,\ h_1(-1)=-(1+\gamma)\) は非零である。それでも
\[
 \lambda_j(-1)=0\quad(j\ge0)
\]
となるのは \(1/\Gamma(-1-j)=0\) のため。全 Taylor 係数が零になったのではない。

この消失は既知である。de la Bretèche–Tenenbaum, *Remarks on the Selberg–Delange method*, 著者訂正版 p3 (1.9)–(1.10) 直後に非正整数の全係数消失が明記される。[一次 PDF](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf)

さらに端点だけへの射影で失われた情報は、全パラメータ族には残る。reciprocal Gamma の単純零点から直接
\[
 \lambda'_j(-1)=(-1)^{j+1}(j+1)!\,h_j(-1).           \tag{C2.2}
\]
全 \(j\) の**正確な**パラメータ微分が分かれば全 \(h_j(-1)\)、よって germ を回収できる。従って「端点の零形式級数だけでは足りない」を「全パラメータ族からでも原理的に不可能」に拡張しない。

## C3. 任意の有限 jet を保存する実・対称 entire 模型

ここだけ空間変数を \(w\) とし、\(\Xi_c(w)=\xi(1/2+w)\) と定義する。通常の \(\xi(1/2+it)\) という別の \(\Xi\) 規約と区別する。\(\Xi_c\) は実 entire・偶関数・位数 1、RH はその零点が虚軸上にあることに対応する。

任意の \(N\ge0\) を固定する。\(w_*=a+ib,\ ab\ne0,\ \Xi_c(w_*)\ne0\) を選び、
\[
 u_*=w_*^2,\qquad
 v_*=-\left(u_*-\frac14\right)^{-N-1},\qquad
 B_N=\frac{\Im v_*}{\Im u_*},\quad
 A_N=\Re v_*-B_N\Re u_*.
\]
\(\Im u_*=2ab\ne0\) なので \(A_N,B_N\) は実数として定義できる。そこで
\[
 Q_N(w)=1+\left(w^2-\frac14\right)^{N+1}(A_N+B_Nw^2),
 \qquad \Xi_N(w)=\Xi_c(w)Q_N(w).                     \tag{C3.1}
\]

これは次を直接満たす。

- \(Q_N\) は実係数の偶多項式、\(Q_N(w_*)=0\)。従って \(w_*,-w_*,\bar w_*,-\bar w_*\) が零点となる。
- \(\Xi_N-\Xi_c\) は \(w=\pm1/2\) で \(N+1\) 次以上消える。両点の全 \(0\le j\le N\) derivatives が一致する。
- 非零多項式を掛けても entire order は 1 のままで、実対称性と偶性を保存する。
- \(w_*\) は実際の零点を避けて選べる。例えば \(0<a<1/2\) の帯の中でも、離散零点集合の外にある \(b\ne0\) を選べる。

零点を単純にしたければ、括弧内に \(t(w^2-u_*)(w^2-\bar u_*)\) を加える。これは real-even と有限 jets と指定零点を保ち、指定点の導関数を非零係数で \(t\) に依存させるので、実数 \(t\) の高々一つの例外を避ければ quartet は単純になる。

**保存しないもの:** Euler 積、Dirichlet 係数、実際の prime/Gamma identity、成長の細かい正規化、追加零点がこの quartet だけであること、全零点が critical strip 内にあること。多項式に別の零点があってもよい。これは有限 jet・対称性・order だけの推論への反例であって、実際の \(\xi\) や RH の反例ではない。\(N\to\infty\) の収束・正規族性も主張しない。

## C4. 有限 jets を保存する meromorphic な極の模型

固定 \(1/2<\beta<1\) に対し
\[
 F_N(s)=\frac1{\zeta(s)}+\frac{(s-1)^{N+1}}{s-\beta}   \tag{C4.1}
\]
は \(s=1\) の \(N\)-jet を保存するが、\(s=\beta\) に極を持つ。\(\zeta(\beta)\ne0\)（実区間 \(0<\beta<1\) では \(\zeta(\beta)<0\)）なので追加項の非零 residue は打ち消されない。

reflection symmetry も保つ別模型は
\[
 H_N(s)=\xi(s)+
 \frac{[s(s-1)]^{N+1}}{(s-\beta)(s-(1-\beta))}.        \tag{C4.2}
\]
これは \(H_N(1-s)=H_N(s)\)、real symmetry、\(s=0,1\) の \(N\)-jets を保ち、\(\beta,1-\beta\) に非零の単純極を持つ。completed \(\xi\) の entire 性を保存する例ではなく、meromorphic 模型としての限定反例である。(C4.1) に functional equation は主張しない。

両模型とも actual Euler 因子を保存せず、普通の算術 Dirichlet 級数としての係数条件も供給しない。full analytic germ の一致ではないため identity theorem と矛盾しない。

## C5. 全次数を超える小ささと Borel の正しい範囲

\(\tau=1/\log X\)、\(R(\tau)=M(e^{1/\tau})e^{-1/\tau}\) と置く。既知の任意固定対数冪評価は
\[
 R(\tau)=O_K(\tau^K)\quad\text{for every fixed }K>0
 \quad(\tau\downarrow0)
\]
を与える。これは正の実軸上の全零**漸近**級数であり、\(\tau=0\) で正則な Taylor 級数ではない。そもそも未平滑化した \(M(e^{1/\tau})\) は平方自由整数を跨ぐ点で跳ぶので、sectorial analytic function として Watson 型定理へ代入できない。

一般模型 \(e^{-d/\tau}\), \(d>0\) も全係数零の漸近級数を持つが非零である。unnormalized では \(X e^{-d\log X}=X^{1-d}\)。\(0<d<1/2\) の模型は平方根より大きくても、対数冪展開の全係数は零のままである。これは actual Möbius coefficients を保存しない限定反例。

実際の Perron integrand の局所留数も同じ境界を示す。非自明零点 \(\rho\) が単純なら
\[
 \operatorname{Res}_{s=\rho}\frac{X^s}{s\zeta(s)}
       =\frac{X^\rho}{\rho\zeta'(\rho)}.              \tag{C5.1}
\]
重複度 \(m\) なら \(X^\rho\) に \(\log X\) の高々 \(m-1\) 次多項式が掛かる。これらを \(X\) で割ると
\(\tau^{-k}e^{-(1-\rho)/\tau}\) であり、任意の \(\Re\rho<1\) について対数冪を全て超えて小さい。従って零 SD 級数は \(\Re\rho=1/2\) と \(1/2<\Re\rho<1\) を区別しない。(C5.1) は局所 residue identity であり、無条件の全零点和表示・その収束・輪郭残差の消失を主張していない。

形式級数 \(\widetilde R=0\) の通常の Borel transform は厳密に 0、その Laplace sum も 0。そこから非零の \(R\) や Stokes constants を自動復元することはできない。別の sector、方程式、成長・境界条件、非零の別形式族等を与えるなら話は変わるが、今回それを \(\zeta\) に構築したとは主張しない。Borel 法一般の不可能性でもない。

## C6. 二重スケーリングでは実際の和まで何を証明できるか

\[
 L=\log X,\quad \ell=\log L,\quad
 z_X=-1+\delta_X,\quad \delta_X=c/\ell .
\]
ここでは \(c\) は有界な実数。先行ノートの局所係数計算だけを使うのではなく、Granville–Koukoulopoulos, Theorem 1, (1.2)–(1.5) の**複素パラメータに一様な加法剰余**を使う。[刊行版一次 PDF, pp2–3](https://dms.umontreal.ca/~koukoulo/documents/publications/LSD.pdf)

\(|z|\le2\)、majorant \(|\mu^2z^\omega|\le\tau_2\)、\(A=9/2\)、\(J=4\) とする。素数平均の仮定は既知の PNT の固定対数冪誤差から一様に成立し、
\[
 S_z(X)=XL^{z-1}\sum_{j=0}^4\lambda_j(z)L^{-j}
                         +O(XL^{-7/2})              \tag{C6.1}
\]
を得る。各 \(\lambda_j\) は端点近傍で正則で \(\lambda_j(-1)=0\)、\(\lambda_0(-1+\delta)=-\delta+O(\delta^2)\)。従って任意の固定 \(C>0\) に対し、\(|c|\le C\) で一様に
\[
 S_{-1+c/\ell}(X)
 =XL^{-2}e^c\left[-\frac c\ell+
 O_C\left(\frac{c^2}{\ell^2}+\frac{|c|}{L\ell}\right)\right]
 +O_C(XL^{-7/2}),                                    \tag{C6.2}
\]
すなわち
\[
 \frac{L^2\ell}{X}S_{-1+c/\ell}(X)
 =-ce^c+O_C\left(\frac{c^2}{\ell}
                   +\frac{|c|}{L}+\ell L^{-3/2}\right). \tag{C6.3}
\]
固定 \(c\ne0\) なら主項が支配する。\(c=0\) も含め normalized limit は一様に \(-ce^c\) へ収束し、その点の極限は 0 である。よって「二つの極限が必ず交換不能」とは言えない。端点で主項が零になるため、この規模より小さい \(M(X)\) の平方根評価を取り出せないことが残る。

なお (C6.1) の remainder は複素近傍で正則かつ一様なので、固定小円上の Cauchy estimate によって微分できる。これに限っては
\[
 S'_z(X)\big|_{z=-1}
   =-\sum_{n\le X}\mu(n)\omega(n)
   =-X/L^2+O(X/L^3)                                  \tag{C6.4}
\]
も正当な既知 SD 枠組みの帰結となる。これは「局所係数だけを微分したから実和も微分できる」という省略とは異なる。端点値 \(M(X)\) の強化ではない。

有限 \(X\) の \(S_z(X)\) は正確な有限多項式である。先行記録の \(X=30\) では \(S_z=1+10z+7z^2+z^3\)、\(S_{-1}=-3,\ S'_{-1}=-1\)。この小規模値を (C6.2) の証明や非可換極限の証拠には使わない。

## C7. 一次文献と適用条件

以下は定理の該当箇所を確認した範囲であり、各論文全証明の独立検証ではない。

1. **Mellin mapping:** Flajolet–Gourdon–Dumas, *Mellin transforms and asymptotics: harmonic sums*, TCS 144 (1995), 3–58。Theorem 3（印刷 pp16–17）は漸近項から Mellin 極への direct mapping。Theorem 4（pp19–21）は continuation strip、境界の正則性、有限個の極と一様な \(O(|s|^{-r}),r>1\) の減衰を仮定する converse mapping。p21 は flat addition と「正確な復元には縦積分の消失が必要」を明記。Corollary 1（p23）の無限極への拡張にも避極高さでの評価が必要。[一次 PDF](https://specfun.inria.fr/dumas/Publications/FlGoDu95.pdf)。[公式訂正](https://algo.inria.fr/flajolet/Publications/mellin-harm-corr.pdf) p1 は Theorem 4 の対数冪を \(k-1\) へ修正している。本稿は修正後を使う。
2. **Watson/Borel:** Gillam–Gurarii, *On a Watson-like Uniqueness Theorem and Gevrey Expansions*, arXiv:math/0508425v1 (2005-08-23)。pp1–3 の (1)–(6) は、一様 factorial remainder と開き \(>\pi\) の sector における一意性、および狭い sector での非零 flat example を比較する。Watson reconstruction の記述は pp14–15、(56)–(59) に追加解析条件と Laplace 表現がある。[指定版一次 PDF](https://arxiv.org/pdf/math/0508425v1)。これらの sectorial hypotheses を actual Mertens remainder に証明したわけではない。
3. **Darboux/transfer:** Flajolet–Odlyzko, *Singularity analysis of generating functions*, SIAM J. Discrete Math. 3 (1990), 216–240。Theorem 1（pp220–221）は indented disk での解析接続と局所 \(O((1-w)^\alpha)\) を使い、Taylor 係数を \(O(n^{-\alpha-1})\) に移す。§5（p234）, (5.2) の Darboux lemma は円周上 \(C^k\) 正則性から \(o(n^{-k})\)。[一次 PDF](https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf)。必要な境界 regularity を有限 jets や消失した SD 係数列で置き換えることはできない。本稿はこれを actual \(\mu\) の評価として適用していない。

actual 算術への有効な Mellin 恒等式は、例えば \(w\in C_c^\infty(0,\infty)\)、\(c>1\) に対して
\[
 \sum_{n\ge1}\mu(n)w(n/X)
 =\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
             \frac{\widehat w(s)X^s}{\zeta(s)}\,ds,
 \qquad \widehat w(s)=\int_0^\infty w(u)u^{s-1}du.     \tag{C7.1}
\]
この初期線での交換は絶対収束、\(\widehat w\) の縦方向急減衰から正当化できる。左への移動には \(1/\zeta\) の極・避極輪郭・成長を扱う独立評価が必要であり、Mellin mapping の一般論だけでは供給されない。未平滑化 \(M\) は不連続なので、Theorem 4 の連続関数仮定へ直接入れない。

**採否:** finite-jet countermodels と (C6.2) は限定的な厳密整理として採用。same-full-germ countermodel、零形式級数からの非零 Borel 復元、未証明 resurgence、有限多項式からの平方根 remainder、一般的な解析法の universal no-go は採用しない。必要なのは actual 算術の大域評価であり、その新しい評価は今回得ていない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/weighted_prime_halfspace/notes/selberg_delange_endpoint.md`](../../weighted_prime_halfspace/notes/selberg_delange_endpoint.md)
