**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase2_newman_generator.md` · Original SHA-256: `cea0253e3baa7572a54e2049ae6067faa75d3bf7ca710d584e459ca68574d540`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# PHASE II / Track A — actual Newman heat generator

2026-09-29。第一原理で構成した後に一次文献と規約を照合した限定検査。
**生成子・算術的な時間原点・Gaussian compactification は厳密に構成できる。
その構造から有限時刻の全零点を実軸へ強制する機構は得られない。RH は OPEN。**
新規性は主張しない。主グラフ・状態ファイルは変更しない。

## Candidate generator

この repo の固定された標準核を

\[
\Phi(u)=\sum_{n\ge1}
(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})e^{-\pi n^2e^{2u}}
\quad(u\ge0),\qquad \Phi(-u)=\Phi(u)
\tag{A1}
\]

とする。Poisson 恒等式により偶延長は滑らかで、実際の整数和と一致する。
\(u\ge0\) では各項が正であり、\(\Phi>0\)。すべての導関数は両端で
double exponential に減衰する。Fourier 規約と時間変形を

\[
H_\tau(z)=\int_{\mathbb R}e^{\tau u^2}\Phi(u)e^{izu}\,du,
\qquad H_0(z)=\Xi(z)=\xi(1/2+iz)
\tag{A2}
\]

と固定する。\(\tau\) と \(z\) が任意の複素 compact にあるとき、積分と任意階の
両変数微分は共通の可積分関数で支配される。従って \(H\) は二変数で entire。

\(L^2(du)\) の掛け算作用素 \(M f=u^2f\) は正自己共役で、
\(D(M)=\{f:u^2f\in L^2\}\)。unitary Fourier 変換
\((2\pi)^{-1/2}\int f(u)e^{izu}du\) では
\(M\leftrightarrow-\partial_z^2\)、後者の domain は \(H^2(\mathbb R)\) である。
\(\Phi\in\bigcap_{a>0}D(e^{aM})\) なので、この特定の初期値の軌道は全実時間で合法。
ただし \(e^{\tau M}\) は \(\tau>0\) で \(L^2\) 全体上の有界作用素ではない。
全空間の可逆な unitary group を構成したという意味でもない。

生成子が自己共役であることは、その作用素のスペクトルが実という主張であり、
特定ベクトルの Fourier 変換 \(H_\tau(z)\) の零点が実という主張ではない。

## Arithmetic input

算術入力は (A1) の**全整数 Gaussian 和と所定の完成操作そのもの**である。
有限素数近似、変形した Mellin 因子、任意の counterterm は入れない。
\(\tau=0\) のみで (A2) の標準 \(\xi\) 同定を用いる。
\(\tau\ne0\) に同じ Euler 積や同じ Gamma 因子が残るとは仮定しない。

具体的に、\(n=1\) 項と残りを分けると

\[
\log\Phi(u)=-\pi e^{2u}+\frac92u+\log(4\pi^2)+O(e^{-2u})
\quad(u\to+\infty).
\tag{A3}
\]

第一項内の補正は \(1-3e^{-2u}/(2\pi)\)、\(n\ge2\) の相対尾は
\(O(e^{-3\pi e^{2u}})\) である。例えば \(n^2-1\ge3+(n-2)\) として
多項式係数を幾何級数で支配すれば、この尾評価は直接得られる。

ここから次の、零点を仮定しない算術的な「時計」の補題が得られる。

**Arithmetic clock lemma.** \(\Phi_a(u)=e^{au^2}\Phi(u)\)、\(a\in\mathbb R\) なら

\[
\boxed{\lim_{u\to\infty}
\frac{\log\Phi_a(u)+\pi e^{2u}-(9/2)u-\log(4\pi^2)}{u^2}=a.}
\tag{A4}
\]

従って標準 Gaussian の全整数和の漸近条件を保つこの時間移動は \(a=0\) のみ。
時間原点は実際の算術データで固定できる。ただしこの極限値0と零点の実軸性との
間にはまだ不等式も含意もない。(A4) を RH の弱い代替仮説とは呼ばない。

## Boundary data

初期データは \(H_0=\Xi\) の全関数、同値に (A1) の全核である。
一つの生成子へまとめても、この無限自由度の初期データは消えない。
対称性・正核・有限個のモーメントは、初期データの代わりにはならない。

全実 \(\tau\) で

\[
H_\tau(-z)=H_\tau(z),\qquad
H_\tau(\overline z)=\overline{H_\tau(z)},\qquad
H_\tau(iy)>0\quad(y\in\mathbb R).
\tag{A5}
\]

最後は正核に対する cosh 積分であり、**純虚軸上の零点を除く**だけである。
\(x\pm iy\)、\(x\ne0\) の quartet は許される。
また実軸 Fourier 反転から
\(\int_{\mathbb R}H_\tau(x)dx=2\pi\Phi(0)\) が保存される。
これは符号を持つ関数の積分保存で、零点の位置を制約する正ノルム保存ではない。

既存ノートの Gaussian convolution
\(F_\sigma(z)=e^{-\sigma z^2}F(z)\) と本変形は異なる。
前者は既存の零点を全て保存するが、後者では零点は動く。
例えば \(\partial_\tau H_\tau(0)=\int u^2e^{\tau u^2}\Phi(u)du>0\) なので、
本変形を \(e^{-\tau z^2}H_0(z)\) と取り違えることはできない。
比較先: [既存の heat multiplier 反例](../selfdual_theta_boundary.md#5-正の増分があっても零点を除去しない例)。

## Evolution law

積分を微分すると、符号を含めて

\[
\boxed{\partial_\tau H_\tau=-\partial_z^2 H_\tau.}
\tag{A6}
\]

これは \(\tau\) 増加方向では backward heat equation。
実軸上では \(\frac d{d\tau}\|H_\tau\|_2^2=2\|H_\tau'\|_2^2\ge0\)。
その正のエネルギー恒等式も零点実軸性を主張していない。

正規化を \(Z_\tau=H_\tau(0)>0\)、
\(\rho_\tau(u)=e^{\tau u^2}\Phi(u)/Z_\tau\)、
\(m_2(\tau)=\int u^2\rho_\tau du\) とすると

\[
\partial_\tau\rho_\tau=(u^2-m_2)\rho_\tau,\quad
m_2'(\tau)=\operatorname{Var}_{\rho_\tau}(u^2)>0,
\quad
\partial_\tau(H_\tau/Z_\tau)
=-\partial_z^2(H_\tau/Z_\tau)-m_2(H_\tau/Z_\tau).
\tag{A7}
\]

確率密度の正性と moment の単調性は厳密だが、cosine 積分の符号を固定しない。
単純零点の局所枝 \(z(\tau)\) には implicit function theorem から
\(z'=H_\tau''(z)/H_\tau'(z)\) が成り立つ。
最初から全枝を実数列として index するには実零点性が必要であり、それを
\(\tau=0\) まで無条件に仮定して運動方程式を使わない。

### 非 RH 補題：negative-time compactification の定量形

\(T>0\)、\(\Phi_0=\Phi(0)>0\) として

\[
\mathcal C_T(z)=\frac{\sqrt T\,H_{-T}(\sqrt T z)}{\sqrt\pi\Phi_0}
\]

と置く。これは時間と周波数の明示的な拡大だけであり、任意の補正項を足さない。
任意の \(R<\infty\) について

\[
\boxed{
\mathcal C_T(z)=e^{-z^2/4}
\left[1+\frac{\Phi''(0)}{2\Phi_0T}
\left(\frac12-\frac{z^2}4\right)\right]+O_R(T^{-2}),
\qquad |z|\le R.
}
\tag{A8}
\]

**証明.** \(x=\sqrt T u\) と置換する。偶性と Taylor の積分剰余により

\[
\left|\Phi(x/\sqrt T)-\Phi_0-\frac{\Phi''(0)x^2}{2T}\right|
\le\frac{\|\Phi^{(4)}\|_\infty |x|^4}{24T^2}.
\]

これを \(e^{-x^2}e^{izx}\) に掛けて積分する。誤差定数は明示的に

\[
\frac{\|\Phi^{(4)}\|_\infty}{24\sqrt\pi\Phi_0}
\int_{\mathbb R}|x|^4e^{-x^2+R|x|}dx
\]

以下である。Gaussian Fourier 積分とその二階微分から (A8) を得る。
\(z\) 微分を何回行っても同じ議論が使える。□

従って \(H_{-T}(\sqrt Tz)/H_{-T}(0)\) は

\[
e^{-z^2/4}\left[1-\frac{\Phi''(0)z^2}{8\Phi_0T}\right]+O_R(T^{-2}).
\tag{A9}
\]

極限は全平面で零点のない Gaussian である。そのため各固定 \(R\) について
十分大きい \(T\) では \(H_{-T}\) は \(|z|\le R\sqrt T\) に零点を持たない。
存在する零点の列は \(|z_T|/\sqrt T\to\infty\) と逃げる。
\(r=(1+T)^{-1}\) とすれば \(r=0\) は局所一様位相で連続な compactified 境界に
なるが、この位相は逃げる零点を捨てる。\(r=0\) を越える時間変数の正則延長は主張しない。
(A8) は無条件の解析補題であり、RH同値ではない。

## Why 1/2

\(s=1/2+iz\) は標準の完成関数の対称性 \(\xi(s)=\xi(1-s)\) を
\(z\mapsto-z\) にする座標である。\(z\) が実であることと \(\Re s=1/2\) が一致する。
熱生成子 \(-\partial_z^2\) 自体が数値 \(1/2\) を算出するわけではない。
また「空間の中心 \(1/2\)」と「熱時間 \(\tau=0\)」は別の概念である。
前者は関数等式、後者は (A1)/(A4) の標準算術データで固定される。

## What forbids off-line

この構成の中で新たに得られた排除則は (A5) の純虚零点排除だけである。
一般の非実 quartet の排除は得られていない。
正生成子、正密度、moment 単調性、even symmetry、保存積分、Gaussian 境界は
いずれもその排除則を含まない。

全実零点性を既知としている時刻から**時間を増加する方向**への保存定理はあるが、
それを時間0へ逆向きに使用できない。以下の既知入力と明示模型で方向を検査する。

## Known prior art

構成 (A1)–(A9) の後に、一次論文
[Rodgers–Tao, arXiv:1801.05914v3 (2020-03-06), §1, (1)–(4), Theorem 1.1](https://arxiv.org/html/1801.05914v3)
を照合した。そこでは半直線 cosine 変換を使うので、規約は

\[
H_t^{\mathrm{RT}}(z)=\frac18 H_{t/4}(z/2),\qquad
\Lambda_{\mathrm{repo}}=\Lambda_{\mathrm{RT}}/4.
\tag{A10}
\]

同論文 §1 の de Bruijn/Newman 定理の記述と Theorem 1.1 を**既知入力**として使うと

\[
\exists\lambda\in[0,1/8]:\quad
H_\tau\text{ の全零点が実}\iff\tau\ge\lambda.
\tag{A11}
\]

上界 \(1/8\) は古典的な保守的上界の換算であり、最新・最良上界の主張ではない。
閾値の存在と非負性をこのノートで再証明したのではない。
\(\tau<0\) の各時刻には非実零点があるという (A11) と、(A8) の Gaussian 極限が
**実際の算術核に対して同時に成立**する。従って、この compactified 境界から
有限時刻の零点実軸性を逆伝播する一般的推論は実例により成立しない。

零点運動も同論文 (5), §4 に既知の体系がある。
本ノートでは実零点列の存在を必要としない単純零点の局所式だけを独立導出した。
この生成子・熱変形を新しい理論と呼ばず、(A4)/(A8) の記述についても優先権を主張しない。

## RH-equivalent hidden assumption

\(\tau_{\mathrm{arith}}=0\)、\(\lambda\)（全実零点性の閾値）、
\(\tau_{\mathrm{ref}}=1/8\)（既知の安全時刻）を区別する。

- \(\lambda\le0\) は RH と同値。(A11) を合わせれば \(\lambda=0\) が同値。
- 「全ての \(\tau>0\) で実零点のみ」も同値である。逆向きは
  \(H_\tau\to H_0\) の局所一様収束と Hurwitz で従い、順向きは既知の保存定理。
- 「0が臨界時間である」は (A4) の算術的な時間原点の特定からは出ない。
- \(\tau_{\mathrm{ref}}\) から0までの全高さ・全零点の逆向き非衝突を
  無条件の安定性原理として置けば、未証明の核心を仮定したことになる。
- 無限零点系の cutoff・renormalization は、その必要な uniform bound を
  自動的には供給しない。有限高さでの継続と全高さの継続を分ける。

以上を新公理・弱い closure 仮説として採用しない。

## Synthetic counterexample

正の偶原子測度
\(\mu_c=c\delta_0+(\delta_1+\delta_{-1})/2\)、\(c>0\) に対して

\[
F_\tau(z)=\int e^{\tau u^2}e^{izu}d\mu_c(u)=c+e^\tau\cos z
\]

は同じ (A6) と対称性を満たし、各時間で正測度から作られる。
その全零点が実であるための必要十分条件は

\[
\boxed{\tau\ge\log c.}
\tag{A12}
\]

実際、\(\tau<\log c\) では
\(z=(2k+1)\pi\pm i\operatorname{arcosh}(ce^{-\tau})\)。
\(\tau=\log c\) では実二重零点、より大きい時刻では実単純零点のみ。
従って生成子・対称性・正測度だけでは閾値を0に固定できない。
これは有限原子測度の模型であり、actual theta kernel の反例ではない。

滑らかさだけを追加しても排除できないことも確認できる。
\(\psi(u)=C\exp(-\cosh(2u))\)、\(\int\psi=1\) として
\(\phi_c(u)=c\psi(u)+(\psi(u-1)+\psi(u+1))/2\) と置く。
正・偶・smooth・double-exponential decay を持ち、全時間の熱変形が存在する。
時間0での変換は \(\widehat\psi(z)(c+\cos z)\) なので、\(c>1\) なら
明示的な非実零点を持つ。原子模型の正確な閾値 (A12) までこの平滑模型へ移してはいない。

さらに実際の核を \(\Phi_a=e^{au^2}\Phi\) とずらすと
\(H^{(a)}_\tau=H_{\tau+a}\)、閾値は \(\lambda-a\) となる。
generic な解析条件は保たれるが (A4) の算術的な時計は変わる。
例えば \(a=-1\) なら時間0に非実零点があることが (A11) から既知。
これも標準の算術的初期値を保持した RH 反例ではない。

## Exact missing lemma

必要なのは (A1) の算術初期値を用いて、**全高さを一様に制御しながら、
既知の実零点時刻から0へ戻せる評価**である。
その結論を単に「\(\lambda\le0\)」と述べるなら RH 同値であり、補助入力にはならない。

有界 Jordan 領域の rectifiable な境界 \(\Gamma\) については、非 RH な次の局所補題は直ちに成立する。
\(\tau_0\in\mathbb R\)、\(m=\min_\Gamma|H_{\tau_0}|>0\)、
\(R=\max_\Gamma|\Im z|\) とし、\(\delta>0\) に対して

\[
M=\int_{\mathbb R}u^2e^{(\tau_0+\delta)u^2}\Phi(u)e^{R|u|}du<\infty.
\]

\(|\tau-\tau_0|<\min(\delta,m/M)\) なら
\(|H_\tau-H_{\tau_0}|<m\) on \(\Gamma\) なので Rouché により内部の零点数は保存される。
これは有限局所継続の正確な条件であり、実零点性そのものを保存する定理ではない。
高さを無限にした際の \(m/M\) の下界も与えない。

本限定検査では、この局所条件を全高さ・時間0まで接続する独立な算術的下界は得られなかった。
生成子一個への整理だけではその不足を解消しない。

## Decision

**KEEP（補助構成）:** 規約・domain・PDE、算術時計 (A4)、正規化式 (A7)、
定量 compactification (A8)/(A9)、有限 contour 継続は厳密で RH を仮定しない。

**REJECT（推論）:** 正生成子や正核からの実零点性、時間原点の指定からの
Newman 閾値0、Gaussian compactification からの逆伝播。
最後の推論は既知入力 (A11) と actual 算術核の (A8) の組合せでも否定される。

**STOP（この限定候補）:** 独立な全高さの算術評価は未取得。
\(\lambda=0\) の言い換えを新しい generator/closure 公理として採用しない。
RH の証明も反証もなく、固定窓認証の拡大や新しい有限零点表の生成は実施していない。

独立検算: DESTROYER が (A8)/(A9) の Gaussian moment と係数、(A12) の閾値・重零点を
別に検算した。これはノート全体や既知入力 (A11) の独立再証明を意味しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/selfdual_theta_boundary.md`](../selfdual_theta_boundary.md)
