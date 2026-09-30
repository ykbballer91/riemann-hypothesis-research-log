**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/global_remainder_beyond_all_orders.md` · Original SHA-256: `ab1ac806bc8752e8afbc9cbcbb98ec14e19fb5dba07d33616c90c9fd48df9a11`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Global Remainder / Beyond-All-Orders

2026-09-30。独立トラック。RH は OPEN。以前の全ファイル・state・proof graph は変更せず、本成果を自動 merge しない。

## 判定

三つの主要試行を実施し、strategy review の上で本探索を終了する。Gaussian 平滑化の厳密な変換、留数と残余積分、完成関数の左右の積分路、局所展開の消失とパラメータ依存を固定した。しかし、実際の Möbius 算術から正規化剰余の subexponential growth を独立に導く入力は得られなかった。

**成功レベルは保守的に Level 0。** 本トラック内で新たに記録した厳密な反例・制約はあるが、既知の変換論・複素解析からの帰結であり、文献上新しい no-go theorem や新しい RH-independent な算術評価と認定しない。新しい零点実部上界はない。

特に次の四点が今回の判別結果である。

1. 全次数で消えるのは Selberg–Delange の漸近係数であり、解析 germ の Taylor 係数ではない。
2. Gaussian の全零点非消失性は既存 One-Prime witness と共通する。非消失性だけでは成長率を制御しない。
3. 正しい右側の逆変換の temperedness は十分条件だが、中央線で別の tempered inverse を定義する操作にはこの意味がない。
4. この faithful な剰余に L² 可積分性を要求すると強すぎる。既知の臨界線零点だけで L² は否定される。

導出の詳細は [Gaussian ノート](global_remainder/notes/gaussian_global_decomposition.md)、[双側変換ノート](global_remainder/notes/completed_two_sided.md)、[局所展開ノート](global_remainder/notes/local_jets_beyond_orders.md)。判定表は [候補比較](global_remainder_candidates.md)、独立監査は [adversarial audit](../../audits/proofs/audits/global_remainder_adversarial.md)。

## 1. 局所消失を正確に固定する

\[
 S_z(X)=\sum_{n\le X}\mu(n)^2z^{\omega(n)},\qquad
 F(s,z)=\zeta(s)^zG(s,z),\qquad G(s,-1)=1.
\]

したがって \(F(s,-1)=1/\zeta(s)\)、\(S_{-1}(X)=M(X)\)。\(s=1\) の近傍で

\[
 H(s,z)=\frac{((s-1)\zeta(s))^zG(s,z)}s
       =\sum_{j\ge0}h_j(z)(s-1)^j
\]

と書く規約では、局所漸近係数は

\[
 \lambda_j(z)=\frac{h_j(z)}{\Gamma(z-j)},\qquad
 \lambda_j(-1)=0\quad(j\ge0).                              \tag{1}
\]

これは負整数パラメータで Hankel 積分が正則な局所項を消すことに対応する。\(1/\zeta(s)=(s-1)+O((s-1)^2)\) は非零の解析関数である。実際 \(h_0(-1)=1\) であり、局所情報そのものがゼロになったわけではない。非正整数における係数消失は既知である。[de la Bretèche–Tenenbaum, pp.2–3, (1.9)–(1.10)](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf)

本稿で beyond all orders と呼ぶのは (1) のみ。remainder の指数的小ささ、resurgence、Borel summability、Stokes 定数の存在を含まない。

## 2. 任意有限 jet と全解析 germ の no-go を分ける

対称座標 \(z=s-\tfrac12\) を使う。任意の有限 \(N\ge0\)、\(z_*=a+i\gamma\)、\(0<a<\tfrac12,\gamma>0\) に対し（新しい零点の挿入には \(\Xi(z_*)\ne0\) も選ぶ）、

\[
 Q_N(z)=1+(z^2-\tfrac14)^{N+1}(A+Bz^2)
\]

の実数 \(A,B\) を、\(w=z_*^2\) として

\[
 A+Bw=-(w-\tfrac14)^{-N-1}
\]

から一意に決められる。すると \(Q_N\) は偶・実係数、\(Q_N(z_*)=0\)、かつ \(Q_N-1\) は \(z=\pm\tfrac12\) で次数 \(N+1\) 以上の零点を持つ。

\[
 \widetilde\Xi_N(z)=\Xi(z)Q_N(z)
\]

は偶性、実対称性、entire order 1 を保持し、指定した軸外 quartet を追加する。\(s=0,1\) で任意に指定した有限次数まで元の完成関数の jet が一致する。元の Gamma/pole prefactor で戻せば \(\widetilde\zeta_N(s)=\zeta(s)Q_N(s-\tfrac12)\) となり、\(1/\widetilde\zeta_N-1/\zeta=O((s-1)^{N+2})\)。Euler product と実際の Möbius 係数は保持しないため、これは actual zeta の反例ではない。

**同じ全 Taylor jet を持つ異なる正則 germ は作れない。** 一致定理により、同じ連結領域上の一価 meromorphic continuation も一致する。「任意の N ごとに別の模型を作れる」と「一つの異なる模型が全 N で同じ jet を持つ」は異なる。今回の全ゼロ列 (1) は germ そのものではなく、情報を消す asymptotic readout である。

この模型は局所係数消失・対称性・有限位数だけから軸外極を排除する推論を否定する。既知解析原理を超える新規性は主張しない。

## 3. Track A：算術的 Gaussian observable

\[
 \phi(v)=e^{-v^2},\quad
 R(u)=\sum_{n\ge1}\mu(n)\phi(u-\log n),\quad
 A(u)=e^{-u/2}R(u),\quad K(s)=\sqrt\pi e^{s^2/4}.
\]

固定 \(u\) では絶対収束する。例えば \(\log n>2|u|+2\) では Gaussian が任意の \(n^{-B}\) より速く減衰する。compact \(u\) 上の任意階微分も同様に一様収束する。実際 \(R\) は複素 \(u\) の entire function でもある。

絶対 Fubini が正当な領域は最初に \(\Re s>1\) とする：

\[
 \int_\mathbb R R(u)e^{-su}\,du
 =K(s)\sum_{n\ge1}\mu(n)n^{-s}
 =\frac{K(s)}{\zeta(s)}.                                  \tag{2}
\]

変数 \(v=u-\log n\) により符号は \(n^{-s}\)。絶対値の交換は
\(\sqrt\pi e^{\sigma^2/4}\sum|\mu(n)|n^{-\sigma}<\infty\)
で確認する。正規化後は

\[
 \mathcal L A(z)=\frac{K(z+\tfrac12)}{\zeta(z+\tfrac12)}
 \quad(\Re z>\tfrac12).                                   \tag{3}
\]

Euler product の絶対収束を critical strip まで延長していない。

### 3.1 完全な積分路恒等式

\(c>1\)、\(a<0\) は負の偶整数でないものに固定し、

\[
 V_{b,T}(u)=\frac1{2\pi i}\int_{b-iT}^{b+iT}
              \frac{K(s)e^{su}}{\zeta(s)}\,ds .
\]

高さ \(T\) は零点を通らない。上辺を \(c+iT\to a+iT\)、下辺を \(a-iT\to c-iT\) とし、\(J_T(u)=(2\pi i)^{-1}(\int_{\rm top}+\int_{\rm bottom})K(s)e^{su}/\zeta(s)\,ds\) と書くと

\[
 V_{c,T}(u)=V_{a,T}(u)+
 \sum_{\substack{a<\Re r<c\\|\Im r|<T}}
 \operatorname{Res}_{s=r}\frac{K(s)e^{su}}{\zeta(s)}
 -J_T(u).                                                 \tag{4}
\]

これは有限高さの完全恒等式。\(R=V_{c,T}+\) 右縦線の tail であり、その tail には

\[
 |R(u)-V_{c,T}(u)|
 \le e^{cu+c^2/4}\frac{\zeta(c)}{\zeta(2c)}
       \operatorname{erfc}(T/2)                            \tag{5}
\]

という明示上界がある。水平辺を黙って捨てない。

標準的な零点計数と \(\xi\) の Hadamard product により、固定幅 \(a\le\sigma\le c\) で
\(|1/\zeta(\sigma\pm iT_j)|\le\exp(C T_j\log^2T_j)\)
となる good heights \(T_j\to\infty\) を選べる。Gaussian が優越するので \(J_{T_j}\to0\)。従って (4) は

\[
 R(u)=V_a(u)
 +\lim_{j\to\infty}\sum_{|\Im\rho|<T_j}
      e^{\rho u}P_\rho(u)
 +\sum_{a<-2k<0}\frac{K(-2k)e^{-2ku}}{\zeta'(-2k)}          \tag{6}
\]

へ進む。非自明零点和は **good-height ごとの grouped sum**、compact な実 \(u\) 上で一様収束する。個々の留数の絶対収束は仮定しない。\(V_a\) は絶対収束する残余積分で
\(|V_a(u)|\le C_a e^{au}\)。
高さ列と評価の証明は Gaussian ノートに記した。既知の Mellin/留数機構の適用であり、新しい explicit formula と主張しない。

\(s=1\) は \(1/\zeta\) の零点、\(s=0\) は正則点なので、ここにはそれらの留数はない。局在した Gaussian の式には累積 Perron kernel の \(1/s\) がないため、単純零点の係数は \(K(\rho)/\zeta'(\rho)\) であり **\(1/\rho\) を付けない**。

### 3.2 多重零点と反射 quartet

\[
 \frac{K(s)}{\zeta(s)}
 =\sum_{j=1}^{m}b_{\rho,-j}(s-\rho)^{-j}+\text{regular}
\]

なら

\[
 P_\rho(u)=\sum_{j=1}^m b_{\rho,-j}\frac{u^{j-1}}{(j-1)!},
\quad \deg P_\rho=m-1,\quad
 [u^{m-1}]P_\rho=\frac{mK(\rho)}{\zeta^{(m)}(\rho)}\ne0.     \tag{7}
\]

単純零点 \(\rho=\tfrac12+a+i\gamma\) の quartet が (6) の正規化に与える寄与は

\[
 2\Re\left(e^{i\gamma u}
       (c_\rho e^{au}+c_{1-\bar\rho}e^{-au})\right),
 \qquad c_r=K(r)/\zeta'(r).                                \tag{8}
\]

実対称性は共役係数を与えるが、二つの \(c\) を同一にはしない。一般には単独の \(\cosh(au)\) envelope ではなく、\(\cosh\) と \(\sinh\) の係数付き和になる。多重度がある場合は (7) の多項式も残る。

軸外モードを他のモードが全体として消せるかは、振動和の点ごとの下界でなく (3) の極で判定する。非消失 kernel はその極を残す。もし全体が後述の subexponential bound を満たせば、その Laplace transform が正則になるため、極との矛盾が出る。右端零点が存在して最大を取ること、最大実部零点が一つだけ支配することを仮定しない。

### 3.3 無限左移動は失敗する

固定 \(u\) に対し、自明零点の個別留数は

\[
 \log\left|\frac{K(-2k)e^{-2ku}}{\zeta'(-2k)}\right|
 =k^2-2k\log k+O_u(k)\longrightarrow+\infty .
\]

Gaussian は縦には減衰するが実方向には増大する。したがって全自明零点の通常の無限留数級数は項がゼロにさえ収束せず、\(a\to-\infty\) で残余を捨てる操作は不可。有限 \(a\) の (6) が正当な形である。

## 4. 成長条件：同値・十分・不可能を区別する

\(u\to-\infty\) では \(A(u)=O(e^{-u^2-u/2})\)。無条件の絶対値評価で正側に得られるのは \(A(u)=O(e^{u/2})\) 程度であり、subexponential ではない。

**定理（既知同値性のこの observable への適用）**

\[
 {\rm RH}
 \Longleftrightarrow
 \forall\epsilon>0,\quad A(u)=O_\epsilon(e^{\epsilon u})
 \quad(u\to+\infty).                                     \tag{9}
\]

右から左：負側の急減衰と正側の評価により (3) が \(\Re z>0\) で正則。非消失 numerator により \(\Re\rho>\tfrac12\) の零点を排除し、反射で RH。
左から右：RH の既知帰結 \(M(x)=O_\epsilon(x^{1/2+\epsilon})\) を (2) の Stieltjes 和へ部分積分すると、Gaussian 積分によって \(R(u)=O_\epsilon(e^{(1/2+\epsilon)u})\)。詳細は Gaussian ノート。

| 仮定する正側の性質 | 極に対する帰結 | この探索での判定 |
|---|---|---|
| 全 \(\epsilon>0\) の subexponential bound | 右半平面の極なし | (9)、RH 同値。独立には得ていない |
| bounded | RH に加えて軸上極次数 \(\le1\) | 零点単純性も要求。RH から導いていない |
| \(O((1+u)^d)\) | RH、軸上極次数 \(m\le d+1\) | 追加の一様制御。RH 同値とはしない |
| regular distribution として tempered | RH、極次数の一様有限上限 | 十分条件。逆含意は未証明 |
| \(L^2(\mathbb R)\) | 軸上の極さえ持てない | actual observable では不可能 |

最後の行は明示的な no-go である。\(A\in L^2\) なら、負側は急減衰なので、既知の臨界線零点の ordinate \(\gamma\) に対し

\[
 |\mathcal L A(\epsilon+i\gamma)|
 \le\|A_+\|_2(2\epsilon)^{-1/2}+O(1).
\]

一方 (3) はその点で次数 \(m\ge1\) の極を持ち、\(\epsilon^{-m}\) で発散する。この二つは両立しない。RH、零点単純性、留数和の絶対収束は不要。L² を global stability の目標に据えるのは誤りである。

### 4.1 One-Prime との重複

| 項目 | 既存 One-Prime | 本トラック |
|---|---|---|
| Gaussian | \(g_*(t)=e^{-t^2}\) | \(\phi(u-\log n)\) |
| 非消失変換 | \(\sqrt\pi e^{(\rho-1/2)^2/4}\) | \(K(\rho)\ne0\) |
| 算術対象 | 既存 zero-bearing quotient と評価汎関数 | 実際の \(\mu(n)\) の convolution |
| 零点検出 | return character \(2^{\rho-1/2}\) | reciprocal zeta の極 \(\rho-1/2\) |
| 必要な追加入力 | forward subexponential return | forward subexponential scalar remainder |
| 独立な入力の取得 | 未取得 | 未取得 |

同一の関数・空間ではないが、非消失 Gaussian と指数成長の排除という機構は共通。scalar smoothing が忠実な zero detection を与えることを新しい解決と数えない。過去の quotient topology を変更していない。

## 5. Track B：完成関数と左右の積分路

\[
 \Xi(z)=\xi(\tfrac12+z),\quad E(z)=e^{z^2},\quad
 H_c(u)=\frac1{2\pi i}\int_{\Re z=c}
                    \frac{E(z)}{\Xi(z)}e^{zu}\,dz,\quad c>\tfrac12 .
\]

Gamma の reciprocal は縦方向に \(e^{\pi|t|/4}\) 程度の増大を持つが \(e^{-t^2}\) が優越し、積分は絶対収束する。\(z=\pm\tfrac12\) は完成関数の逆数の極ではない。\(c>\tfrac12\) の間では同じ \(H\) であり、負側は任意指数より速く減衰する。

偶性から正しく出る式は

\[
 H_{-c}(u)=H_c(-u),
\]

であって \(H_c\) の偶性ではない。実際の右側 \(H\) が偶なら、負側の任意指数減衰が正側へ移って \(L^2\) となり、同じ極の議論と矛盾する。従ってこの faithful \(H\) 自体は無条件に非偶。左右の差には横断する全零点の留数が入る。有限高さで水平辺を含める恒等式は双側変換ノートに記した。単純 quartet の係数は
\(4\Re(r_a\sinh(au))\)、\(r_a=E(a)/\Xi'(a)\)。

実際の算術表現もある。定義

\[
 A_\infty(z)=
 \frac{2e^{z^2}\pi^{z/2+1/4}}
 {(z^2-1/4)\Gamma(z/2+1/4)}
\]

とその右側 inverse \(a_c\) を用いて

\[
 H(u)=\sum_{n\ge1}\mu(n)n^{-1/2}a_c(u-\log n).             \tag{10}
\]

固定 \(c>\tfrac12\) では絶対収束する。しかし絶対値評価は \(O_c(e^{cu})\) まで。Gamma、finite primes、pole cancellation を全て含めても、正側の Möbius cancellation を独立に改善していない。

この同じ右側 \(H\) が tempered なら、正半軸 smooth cutoff と負側急減衰から Laplace transform を \(\Re z>0\) へ正則に延ばせて RH が出る。ただし temperedness は零点多重度の一様上限も要求するので、RH 同値とは認定しない。

### 5.1 積分路を変えただけの偽解決

\(a>0\)、\(G(z)=e^{z^2}/(z^2-a^2)\) は偶・実 meromorphic。\(g(u)=(2\sqrt\pi)^{-1}e^{-u^2/4}\) とすると

\[
 H_{\rm central}=g*\left(-\frac{e^{-a|u|}}{2a}\right),\quad
 H_{\rm right}=g*\left(\mathbf1_{u\ge0}\frac{\sinh(au)}a\right).
\]

前者は Schwartz で、後者は正側に指数増大し、

\[
 H_{\rm right}(u)-H_{\rm central}(u)
       =\frac{e^{a^2+au}}{2a}.                             \tag{11}
\]

同じ meromorphic formula でも bilateral Laplace の収束域が違う。中央線の temperedness は軸外極を排除しない。複素 quartet と任意多重度を持つ偶・実有理模型にも同じ反例が成立する。

actual arithmetic が指定する右側 inverse を保ったまま bound を証明する義務が残る。単なる Fourier/PV 定義、対称化、phase quotient、completed という名称からは出ない。Track B はこの未取得入力で停止。

## 6. Track C：局所消失、germ、パラメータ遷移

局所逆変換の全係数がゼロなら、**そのゼロ formal series 単独**の通常の Borel transform もゼロである。非零の \(M(X)\) をそこから一意に回復するには追加の大域情報が必要。実際の大域 singularities は (2) に見えるが、これを定理なしに Stokes data と呼ばない。

通常の Mellin contour asymptotics は singularity と asymptotic terms を対応させる。ただし pole を跨いだ留数はそれだけで Borel-plane singularity や resurgent alien derivative ではない。今回適用可能な、RH-independent に singularity positions を拘束する resurgence theorem は確認できなかった。

パラメータ族を捨てなければ局所情報は戻る：

\[
 \lambda'_j(-1)=(-1)^{j+1}(j+1)!\,h_j(-1).                \tag{12}
\]

従って全 \(j\) の exact parameter derivatives は全局所 germ を回収し得る。「端点の全ゼロ列からは無理」と「全パラメータ族を与えても原理的に無理」は別である。既知 germ の解析接続の一意性は、零点位置の有効な評価を供給するという意味ではない。

\(\ell=\log\log X\)、\(\delta=c/\ell\) とすると、複素パラメータ一様な既知の Selberg–Delange 型定理から、有界 \(c\) 上で

\[
 \frac{(\log X)^2\log\log X}{X}\,
 S_{-1+c/\log\log X}(X)\longrightarrow -c e^c            \tag{13}
\]

が一様に従う。\(c=0\) も含む。導出では additive remainder を維持し、消える main term で割らない。[Granville–Koukoulopoulos, Theorem 1](https://dms.umontreal.ca/~koukoulo/documents/publications/LSD.pdf)

これは genuine な境界層の尺度を与えるが、端点の微小な \(M(X)\) の平方根評価は与えない。「極限が非可換」と曖昧には主張しない。正規化した (13) はむしろ端点まで一様である。同じ定理の複素一様性と Cauchy 評価により

\[
 \left.\partial_z S_z(X)\right|_{z=-1}
 =-\frac{X}{(\log X)^2}+O\!\left(\frac{X}{(\log X)^3}\right)
\]

も得られるが、値 \(S_{-1}=M\) の未評価剰余とパラメータ微分は別。これらは既知定理の帰結であり、独立な新しい算術的拘束として採用しない。

## 7. 反証・計算・停止理由

新しい実験は [code](../../../artifacts/research/global_remainder/experiments/check_global_remainder.py) と [results](../../../artifacts/research/global_remainder/experiments/results.json) に保存した。

- actual Möbius Gaussian 和と右側逆変換：3 点、級数 tail と縦線 tail の明示上界を照合。
- 有限矩形：\(a=-3,c=1.5,T=16,u=1\)。非自明零点最初の共役対、自明零点 \(-2\)、左右縦線、水平辺を全て保持。
- 同じ Gaussian の中央線／右側逆変換：6 点、(11) と反射差を検算。
- 非実軸外 quartet \(\pm0.2\pm i\) の模型：4 点、右半平面留数和と積分路の差を検算。
- 有限 jet 模型：5 次数、係数を有理数で exact に構成して指定 quartet の根を確認。
- reciprocal Gamma の端点微分：7 例。
- \(S_z(X)\) の有限多項式：3 cutoffs、端点と近傍値。漸近 fit は行わない。

数値積分は 50 桁浮動小数の診断であり、interval certificate ではない。数学的証明は有限積分路と解析評価に置く。数値で単純零点の留数を使った箇所はその検算に限定し、一般定理は多重零点を許す。有限範囲の小ささは RH の証拠にしない。

**Strategy review:** A は exact decomposition と既知 subexponential 同値性、B は faithful inverse の未証明成長条件、C は局所情報消失と既知一様漸近の限界へ戻った。三つとも「actual Möbius coefficients が大域の指数増大を禁じる」独立の証明を得ていない。同型の第4候補を続けない。

残る最小の要求は (2) または (10) の actual arithmetic representation に対する RH-independent な正側評価である。これを subexponential と仮定すれば問題を移しただけになる。既存トラックの停止理由を再命名して採用しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/global_remainder_adversarial.md`](../../audits/proofs/audits/global_remainder_adversarial.md)
- [`research/global_remainder/experiments/check_global_remainder.py`](../../../artifacts/research/global_remainder/experiments/check_global_remainder.py)
- [`research/global_remainder/experiments/results.json`](../../../artifacts/research/global_remainder/experiments/results.json)
- [`research/global_remainder/notes/completed_two_sided.md`](global_remainder/notes/completed_two_sided.md)
- [`research/global_remainder/notes/gaussian_global_decomposition.md`](global_remainder/notes/gaussian_global_decomposition.md)
- [`research/global_remainder/notes/local_jets_beyond_orders.md`](global_remainder/notes/local_jets_beyond_orders.md)
- [`research/global_remainder_candidates.md`](global_remainder_candidates.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_global_remainder.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
