**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/lemmas/finite_to_infinite.md` · Original SHA-256: `d0bdfa65e79a65c5a7ddfd9747ed53b15805c45e4b63c24692c7881516544006`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定支持での Weil 形式の連続性と有限 Gram 行列

作成日: 2026-09-29。担当: BUILDER / SYMBOLIC ANALYST。
状態: 以下の補題は `PROVED`（既知の初等解析的帰結を本リポジトリ内で証明）。新規性は主張しない。
全ての有限行列の正値性という仮定は `EQUIVALENT-TO-RH / OPEN` のままである。

記号は `weil_conventions.md` に従う。以下は RH を仮定しない。

## F0. 空間と既知入力

\[
\mathcal D_L=\{f\in C_c^\infty(\mathbb R;\mathbb C):
                      \operatorname{supp}f\subset[-L,L]\},\quad L>0,
\]

\[
p_m(f)=\max_{0\le j\le m}\|f^{(j)}\|_\infty,\quad m=0,1,2,\ldots
\]

とする。この半ノルム列で \(\mathcal D_L\) に Fréchet 位相を入れる。
収束とは支持がこの一つの区間に収まり、全ての階数の導関数が一様収束することである。
異なる \(L\) を同時に動かす極限は、ここで扱う固定支持の収束とは異なる。

唯一の零点計数入力は

\[
N_*(T):=\#\{\rho\in Z:|\Im\rho|\le T\}
\le C_0(T+1)\log(T+2)\quad(T\ge0) \tag{9}
\]

となる定数 \(C_0\) が存在するという無条件の古典的評価である。多重度を数える。
Riemann–von Mangoldt の零点計数公式の弱い帰結であり、臨界線上の零点だけの計数ではない。
一次研究文献として Hasanalizade–Shen–Wong, *Counting zeros of the Riemann zeta function*, J. Number Theory 235 (2022), 219–241, DOI 10.1016/j.jnt.2021.06.032, §1 と §2 の \(N_{\mathbb Q}(T)\) を照合した。
本稿は同論文の数値定数の最適性や高精度な誤差係数を必要としない。
[著者公開の出版版](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf)

## F1. 固定帯での一様減衰

**命題.** 各 \(L>0\)、整数 \(m\ge0\) に対して

\[
|F_f(u+iv)|\le A_{L,m}\,p_m(f)(1+|u|)^{-m}
\quad (f\in\mathcal D_L,\ u\in\mathbb R,\ |v|\le1/2), \tag{10}
\]

が成り立つ。例えば \(A_{L,m}=2^{m+1}Le^{L/2}\) と取れる。

**証明.** まず \(|e^{i(u+iv)x}|=e^{-vx}\le e^{L/2}\) なので
\(|F_f(u+iv)|\le2Le^{L/2}p_0(f)\) である。
\(|u|\ge1\) なら \(z=u+iv\ne0\) であり、\(m\) 回部分積分すると

\[
F_f(z)=(-1)^m(iz)^{-m}\int f^{(m)}(x)e^{izx}dx.
\]

全ての境界項は消える。\(f\) と全ての導関数は区間外でゼロであり、端点にも連続だからである。
従って \(|F_f(z)|\le2Le^{L/2}p_m(f)|u|^{-m}\)。
\(|u|\ge1\) では \(|u|^{-m}\le2^m(1+|u|)^{-m}\)、\(|u|\le1\) では \(1\le2^m(1+|u|)^{-m}\) を使えば (10) となる。∎

## F2. 絶対収束、tail 評価、Hermitian 性

**命題.** 任意の整数 \(m\ge1\) に対し

\[
S_m=\sum_{\rho\in Z}(1+|\gamma|)^{-2m}<\infty.
\]

\(T\ge2\) に対して、\(m\) と (9) の定数だけに依存する \(B_m\) が存在し

\[
S_m(T):=\sum_{|\gamma|>T}(1+|\gamma|)^{-2m}
\le B_m T^{1-2m}\log(T+2). \tag{11}
\]

従って \(f,g\in\mathcal D_L\) について、

\[
Q(f,g)=\sum_{\rho\in Z}F_f(z_\rho)\overline{F_g(\bar z_\rho)}
\]

は無条件に絶対収束し、

\[
|Q(f,g)|\le A_{L,m}^2 S_m p_m(f)p_m(g), \tag{12}
\]

\[
|Q(f,g)-Q_T(f,g)|
\le A_{L,m}^2 S_m(T)p_m(f)p_m(g),\quad
Q_T(f,g)=\sum_{|\gamma|\le T}F_f(z_\rho)\overline{F_g(\bar z_\rho)}. \tag{13}
\]

**証明.** \(2^kT<|\gamma|\le2^{k+1}T\) に分割する。各区間の寄与は

\[
(2^kT)^{-2m}N_*(2^{k+1}T)
\le C_1 T^{1-2m}2^{(1-2m)k}
                   \{\log(T+2)+(k+1)\log2\}
\]

で抑えられる。\(m\ge1\) なら \(\sum_{k\ge0}(k+1)2^{(1-2m)k}\) は収束するので (11) が得られる。
\(|\gamma|\le2\) の零点は有限個であるから \(S_m<\infty\) も従う。
\(z_\rho\) と \(\bar z_\rho\) はともに (10) の帯にあり実部は \(\gamma\) である。
各項の絶対値に (10) を二度適用して和を取れば (12) と (13) が得られる。∎

\(m=1\) だけでも十分である。各 \(p_m\)-有界集合上で零点和は一様に絶対収束する。
ゆえに零点列の並べ替えと共役は合法であり、`weil_conventions.md` (7) による Hermitian 性が成立する。
\(|\gamma|\le T\) は \(\rho\mapsto1-\bar\rho\) で不変なので、\(Q_T\) も Hermitian である。
ここで \(Q_T\ge0\) や tail の正符号は主張していない。

## F3. 必要な連続性と極限交換

**命題.** \(f_n\to f\)、\(g_n\to g\) が一つの \(\mathcal D_L\) で成り立つとき、

\[
Q(f_n,g_n)\longrightarrow Q(f,g). \tag{14}
\]

実際には \(p_1(f_n-f)\to0\)、\(p_1(g_n-g)\to0\) だけでよい。

**証明.** \(C_L=A_{L,1}^2S_1\) と置く。第1変数に線形、第2変数に共役線形であるため

\[
\begin{aligned}
|Q(f_n,g_n)-Q(f,g)|
&\le |Q(f_n-f,g_n)|+|Q(f,g_n-g)|\\
&\le C_L\{p_1(f_n-f)p_1(g_n)+p_1(f)p_1(g_n-g)\}.
\end{aligned}
\]

収束する \(g_n\) の \(p_1(g_n)\) は有界なので右辺はゼロに収束する。∎

これは数値 \(Q(f_n,g_n)\) の収束を示す補題である。
作用素の強収束、ノルム収束、resolvent 収束、trace norm 収束は必要としないし、結論もしない。
\(L\to\infty\) に関する一様評価も結論しない。明示定数には \(e^{L/2}\) が含まれる。

## F4. 固定支持内の明示的な可算稠密族

\(\eta\in\mathcal D_1\) を実数値・非負で \(\int\eta=1\) となる固定関数とする。
例として、\(|x|<1\) では \(C\exp(-1/(1-x^2))\)、それ以外ではゼロとし、\(C\) で積分を1に正規化する。
\(L\in\mathbb N_{\ge1}\) ごとに

\[
\mathcal B_L=
\left\{b_{a,\epsilon}(x)=\epsilon^{-1}\eta((x-a)/\epsilon):
a\in\mathbb Q,\ \epsilon\in\mathbb Q_{>0},\ |a|+\epsilon<L\right\}
\]

を任意の順序で \((\phi_{L,j})_{j\ge1}\) と列挙する。

**命題.** \(\operatorname{span}_{\mathbb C}\mathcal B_L\) は \(\mathcal D_L\) の Fréchet 位相で稠密である。
線形独立性は必要ない。

**証明.** 任意の \(f\in\mathcal D_L\)、階数 \(m\)、許容誤差 \(\tau>0\) を固定する。

1. \(0<\delta<1/2\) に対し \(f_\delta(x)=f(x/(1-\delta))\) とする。
   支持は \([-L(1-\delta),L(1-\delta)]\) に収まる。
   各 \(j\le m\) に対し \(f_\delta^{(j)}(x)=(1-\delta)^{-j}f^{(j)}(x/(1-\delta))\) である。
   導関数の一様連続性とコンパクト台により \(p_m(f_\delta-f)\to0\)。
   \(p_m(f_\delta-f)<\tau/3\) となる \(\delta\) を選ぶ。
2. 有理数 \(0<\epsilon<\delta L/2\) を十分小さく取る。
   \(f_\delta*\eta_\epsilon\) とその \(j\le m\) 階導関数は、対応する \(f_\delta^{(j)}\) に一様収束する。
   これは \(\int\eta=1\) と \(f_\delta^{(j)}\) の一様連続性から、積分内の差を評価すれば得られる。
   従って \(p_m(f_\delta*\eta_\epsilon-f_\delta)<\tau/3\) とできる。
3. \(L(1-\delta)<R<L-\epsilon\) となる有理数 \(R\) を取る。
   \(\int_{-R}^R f_\delta(t)\eta_\epsilon(x-t)dt\) を有理分点・有理標本点の Riemann 和で近似する。
   \(x\in[-L,L]\)、\(t\in[-R,R]\)、\(j\le m\) について
   \(f_\delta(t)\eta_\epsilon^{(j)}(x-t)\) は一様連続なので、有限和は全ての \(j\le m\) で一様近似できる。
   各項は \(f_\delta(a_k)\Delta t_k\,b_{a_k,\epsilon}(x)\) であり、\(|a_k|+\epsilon<L\) だから \(\mathcal B_L\) の複素線形結合である。
   \(p_m\) 誤差を \(\tau/3\) 未満にする。

三角不等式により近似誤差は \(\tau\) 未満となる。
\(m=n\)、\(\tau=1/n\) を順に適用すれば、全ての半ノルムで \(f\) に収束する線形結合の列を得る。∎

## F5. 有限 Gram 正値性から全テストへの橋

\[
V_{L,N}=\operatorname{span}_{\mathbb C}
\{\phi_{L,1},\ldots,\phi_{L,N}\},\qquad
(M_{L,N})_{jk}=Q(\phi_{L,k},\phi_{L,j})
\]

と定める。添字の順序を逆にしている理由は、\(Q\) が第1変数に線形だからである。
\(f=\sum_{j=1}^Nc_j\phi_{L,j}\) に対し

\[
Q(f,f)=c^*M_{L,N}c. \tag{15}
\]

**定理.** 以下は同値である。

1. \(\forall L\in\mathbb N_{\ge1}\ \forall N\in\mathbb N_{\ge1},\ M_{L,N}\succeq0\)。
2. \(\forall L\in\mathbb N_{\ge1}\ \forall f\in\mathcal D_L,\ Q(f,f)\ge0\)。
3. \(\forall f\in C_c^\infty(\mathbb R;\mathbb C),\ Q(f,f)\ge0\)。

従って既知の Weil 判定法 W1 を用いれば、これらはすべて RH と同値である。

**証明.** 1 を仮定する。\(L\) と \(f\in\mathcal D_L\) を固定し、F4 で
\(f_n\in\bigcup_N V_{L,N}\)、\(f_n\to f\) を選ぶ。
各 \(f_n\) はある有限個の \(\phi_{L,j}\) の線形結合であり、それらの最大添字を \(N_n\) とすれば
\(Q(f_n,f_n)\ge0\) が (15) から従う。
F3 によって \(Q(f_n,f_n)\to Q(f,f)\)、非負実数集合の閉性から \(Q(f,f)\ge0\) である。これが 2。
各コンパクト台はある整数 \(L\) の \([-L,L]\) に収まるので 2 は 3 を含意する。
3 から 1 は (15) を任意の \(c\in\mathbb C^N\) に適用すれば得られる。∎

**論理状態.** 橋の定理は無条件に証明した。
しかし仮定1の全称命題は証明していない。
それは RH と同値であり、「残りは有限行列だから自動的に正」と解釈してはならない。
この同値化自体を新しい RH 進展とは数えない。

## F6. 有限個の確認と零点打切りの限界

有限個の行列の PSD から F5 の全称命題は出ない。
具体的に、任意の \(N_0\) について \(\ell^2(\mathbb N)\) 上の有界 Hermitian 形式

\[
q(x)=\sum_{j=1}^{N_0}|x_j|^2-|x_{N_0+1}|^2
\]

は、\(\operatorname{span}\{e_1,\ldots,e_N\}\) の全ての \(N\le N_0\) で PSD だが、
\(q(e_{N_0+1})=-1\) である。
これは RH の反例ではなく、「任意に多いが有限個の確認で十分」という一般的推論への反例である。

零点打切り行列 \((M_{L,N}(T))_{jk}=Q_T(\phi_{L,k},\phi_{L,j})\) にも注意を要する。
全零点を多重度込みで \(|\gamma|\le T\) まで漏れなく含めた場合、F2 と Cauchy–Schwarz により

\[
\|M_{L,N}-M_{L,N}(T)\|_{\rm op}
\le E_{L,N}(T)
:=A_{L,1}^2 S_1(T)\sum_{j=1}^N p_1(\phi_{L,j})^2. \tag{16}
\]

実際、単位ベクトル \(c\) に対応する \(f=\sum c_j\phi_{L,j}\) について
\(p_1(f)^2\le\sum_jp_1(\phi_{L,j})^2\) であり、(13) と Hermitian 行列の Rayleigh 商表示を使う。

従って

\[
\lambda_{\min}(M_{L,N}(T))\ge E_{L,N}(T)
\quad\Longrightarrow\quad M_{L,N}\succeq0. \tag{17}
\]

打切り行列が単に PSD というだけでは (17) の誤差余裕は保証されない。
数値計算を用いる場合は、零点の網羅性、各行列要素の丸め誤差、tail の明示上界、固有値下界をすべて保証する必要がある。
臨界線上の既知零点のみを選んだ \(\sum |F_f(\gamma)|^2\) は自動的に正だが、未確認零点を含む本来の \(Q\) と等しいという証明にはならない。
式 (17) を有限個の \(L,N\) について保証しても F5 の全称命題は未解決である。

## F7. 残った核心と依存関係

\[
\begin{array}{c}
\text{零点の帯・対称性・計数 (KNOWN)}\\
\Downarrow\\
\text{F1--F3: 絶対収束と固定支持連続性 (PROVED)}\\
\quad+\quad\text{F4: 可算族の稠密性 (PROVED)}\\
\Downarrow\\
\text{F5: 全有限 Gram PSD と全テスト正値性の同値 (PROVED)}\\
\quad+\quad\text{W1: Weil 判定法 (KNOWN)}\\
\Downarrow\\
\boxed{[\forall L,N,\ M_{L,N}\succeq0]\iff\mathrm{RH}}
\end{array}
\]

本稿が閉じたのは、正しい領域と位相の下での有限→無限の解析的接続である。
未解決の算術的主張 \(\forall L,N,\ M_{L,N}\succeq0\) は閉じていない。
新しい非循環的な正値性機構、または全称命題を含意する既知で独立な構造が必要である。
