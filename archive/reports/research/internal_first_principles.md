**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/internal_first_principles.md` · Original SHA-256: `e6c6c9cfe050f9e2781bacd987ff6ee3fecacb600aa3f8038e0e77762234b140`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 内部構築を優先する探索 — 2026-09-29

**RH は未証明。外部の新しい proof claim を順番に監査する方針を中止する。**
最新のユーザー指示を優先し、実際の対象から恒等式・十分条件・反例を自分で組み立てる。
文献は具体的な候補の既知性・必要な定理条件を後で確かめる用途に限定する。
新しい定義や体系に、必要な正値性を公理として埋め込まない。
本巡は文献検索なし。独立導出であり、新規性の主張ではない。

## 1. 境界の平方から残差へ

実偶関数 \(\phi\) と必要な急減衰を仮定し、実数 \(a,b\) に対して

\[
K_\phi(a,b)=\frac12\int_{|(a+b)/2|}^{\infty}
y\phi(y+(a-b)/2)\phi(y-(a-b)/2)\,dy
\]

を直接調べる。\(\phi\) が偶なので積は \(y\) の偶関数であり、下限を
\((a+b)/2\) に換えても積分値は等しい。従って全実数 \(a,b\) で

\[
K_\phi(a,b)=\frac14\int_0^\infty(2t+a+b)\phi(t+a)\phi(t+b)\,dt. \tag{1}
\]

\(\beta>0\)、\(r_\beta(t)=\phi'(t)+\beta t\phi(t)\) と置く。
積の微分を積分するだけで

\[
\boxed{K_\phi(a,b)=\frac{\phi(a)\phi(b)}{4\beta}
 +\frac1{4\beta}\int_0^\infty
 [r_\beta(t+a)\phi(t+b)+\phi(t+a)r_\beta(t+b)]\,dt.} \tag{2}
\]

第一項は平方の核。第二項は交差項であり、点ごとの符号ではPSDは決まらない。
これは \(\phi\) の零点でも有効な式で、対数微分への除算を必要としない。
実際のリーマン核に対する \(K_\phi\succeq0\) 自体は既にRH同値と判定済み
（[Fourier 接続の記録](../../audits/proofs/audits/freedman-weyl-bridge-gate.md)）。
新しい入力を探す対象は (2) の残差の構造であり、PSDを仮定し直すことではない。

## 2. 限定された平方和と、その延長限界

\(G(t)=e^{-\beta t^2/2}\)、\(\phi(t)=A(1+\lambda t^2)G(t)\)、
\(A>0,\lambda\ge0\) なら、(2) の残差は厳密に

\[
R_\beta(a,b)=
\frac{A^2\lambda(\beta+\lambda)}{2\beta^3}G(a)G(b)
+\frac{A^2\lambda^2}{2\beta^2}[aG(a)][bG(b)]. \tag{3}
\]

従ってこの模型では平方和が得られる。導出は
\(q=(t+a)(t+b)\)、\((G(t+a)G(t+b))'=-\beta q'G(t+a)G(t+b)\)
による二回の部分積分。\(\lambda=0\) では残差が消える。

一般の \(\phi_\lambda=(1+\lambda t^2)\phi\) に対しても恒等式は作れる。
\(v=(a+b)/2,u=(a-b)/2,p(t)=1+\lambda t^2\) として

\[
J_m(a,b)=\frac12\int_{|v|}^\infty
y(y^2-v^2)^m\phi(y+u)\phi(y-u)\,dy
\]

なら

\[
K_{\phi_\lambda}=p(a)p(b)K_\phi+2\lambda J_1
+2\lambda^2abJ_1+\lambda^2J_2. \tag{4}
\]

しかし \(K_\phi\succeq0\Rightarrow J_1,J_2\succeq0\) はこの計算からは出ない。
一般のPSD核に対する尾積分はPSDを保存しない。これは (4) の保存命題自体の反証ではない。
次節の実核の障害があるため、このGaussian積の保存定理を主目的に拡張しない。

## 3. 正・強対数凹・増加scoreでも負になる厳密模型

\[
\phi_0(t)=e^{-t^2}p(t^2),\qquad
p(u)=1+\alpha u+bu^2,\quad \alpha=3/20,\ b=1/100.
\]

\(h(u)=-\phi_0'(\sqrt u)/(\sqrt u\phi_0(\sqrt u))\) を連続延長すると

\[
h(u)=2-2\frac{\alpha+2bu}{p(u)},\qquad
h'(u)=2\frac{(\alpha^2-2b)+2\alpha bu+2b^2u^2}{p(u)^2}>0.
\]

\(h(0)=17/10\) なので \((\log\phi_0)''\le-17/10\)。
入力は正・偶・整・急減衰で、Gaussianに対して規格化したscoreも正で厳密増加する。
それでも

\[
F_0(z)=\int_\mathbb R\phi_0(t)e^{izt}dt
=\frac{\sqrt\pi}{1600}e^{-z^2/4}(z^4-72z^2+1732)
\]

は非実零点を持つ。\(z^2\) の二次方程式の判別式は負。
さらに \(z=6+i\) では、\(P=z^4-72z^2+1732\) として
\(P=293-24i,P'=-72+284i\) より

\[
-\frac{\Im(F_0'/F_0)}{\Im z}=-\frac{76543}{172850}<0.
\]

Fourier接続の対角値も

\[
D_0(6+i,6+i)=-\frac{76543\pi e^{-35/2}}{20480000}<0.
\]

複素点を用いなくても、正半直線の5点で反証できる。
\(K_{\phi_0}(a,b)=e^{-a^2-b^2}\sum_{i,j=0}^4 C_{ij}a^ib^j\) の
奇数次数 \(1,3\) のブロックは

\[
\begin{pmatrix}29/40000&3/16000\\3/16000&1/40000\end{pmatrix},
\qquad \det=-109/6400000000.
\]

\(a_j=j\), \(c_j=e^{j^2}v_j\),
\(v=(-49/24,19/12,3,-43/12,25/24)\) なら
\(\sum_jv_jj^k=(0,1,0,-15/2,0)_k\)。従って

\[
\boxed{\sum_{i,j=1}^5c_ic_jK_{\phi_0}(i,j)=-109/160000.} \tag{5}
\]

連続核なのでDirac点評価は、十分小さい滑らかなbumpへの置換でも負のまま。
一般の符号付き試験関数に対するPSDの反証であり、非負試験関数だけの主張ではない。

### 位数1・超指数減衰への拡張

\[
\phi_\varepsilon(t)=\phi_0(t)e^{-\varepsilon(\cosh(2t)-1)},\quad\varepsilon>0.
\]

正・偶・整を保ち、
\((\log\phi_\varepsilon)''\le-17/10-4\varepsilon\cosh(2t)\)。
scoreの追加項 \(2\varepsilon\sinh(2t)/t\) は \(t>0\) で正・増加。
\(0<\phi_\varepsilon\le\phi_0\) により、(5) の各積分に優収束を適用できる。
従って十分小さい \(\varepsilon>0\) で同じ5点・同じ係数の負値が残る。
同じ優収束は \(F_\varepsilon\to F_0\) の複素コンパクト集合上の一様収束も与える。
\(F_0\) の非実零点の周りに小円を取れば、Rouchéの定理により
十分小さい正の \(\varepsilon\) で非実零点も残る。

Fourier変換 \(F_\varepsilon\) の最大modulusを \(M_\varepsilon(R)\) とすると
\(\cosh(2t)\ge e^{2|t|}/2\) から

\[
M_\varepsilon(R)\le\|\phi_0\|_1
\exp\{\varepsilon+(R/2)(\log(R/\varepsilon)-1)\}
\]

が \(R\ge\varepsilon\) で成立する。逆に \(R\ge1\) で \(F_\varepsilon(iR)>0\) の積分を
\(-t\in[\frac12\log R,\frac12\log R+1]\) に制限すると

\[
\log M_\varepsilon(R)\ge (R/2)\log R
-(\tfrac12\log R+1)^2-\varepsilon\cosh(\log R+2)+\varepsilon.
\]

従って \(\log M_\varepsilon(R)=(R/2)\log R+O_\varepsilon(R)\)。
**Fourier整関数の位数はちょうど1（有限指数型ではない）でも反例は残る。**
actual theta の算術、scoreの大域凸性、任意の追加構造まで否定したものではない。

## 4. 実際の核はGaussian実因子積の極限にも入らない

リーマン核を規格化して

\[
\Phi(t)=\sum_{n\ge1}(4\pi^2 n^4e^{9t/2}-6\pi n^2e^{5t/2})
 e^{-\pi n^2e^{2t}},\qquad t\ge0
\]

とする。偶延長を使う。まず固定 \(c\) に対して \(e^{ct^2}\Phi(t)\to0\)。
従って \(u=t^2\) における非負係数多項式の点ごとの極限にはならない。
より強く、\(c_N\) の発散を許す

\[
\Phi_N(t)=A_Ne^{-c_Nt^2}\prod_j(1+\lambda_{Nj}t^2),
\qquad A_N>0,\quad\lambda_{Nj}\ge0
\]

という**実一次因子の積**の全実軸での点ごとの閉包にも \(\Phi\) は入らない。
実際 \(H_N(u)=\log\Phi_N(\sqrt u)\) では

\[
H_N'''(u)=2\sum_j\frac{\lambda_{Nj}^3}{(1+\lambda_{Nj}u)^3}\ge0,
\qquad \Delta_h^3H_N(u)\ge0. \tag{6}
\]

正値関数への点ごとの収束だけで、四点の対数有限差分にも極限を通せる。
一方、実際のtheta展開の第一項と残りを分けると

\[
\log\Phi(t)=\log(4\pi^2)+(9/2)t-\pi e^{2t}+O(e^{-2t}).
\]

この漸近は \(t\) 微分3階まで有効。\(n\ge2\) の相対尾は3階微分まで
\(O(e^{6t}e^{-3\pi e^{2t}})\) であり、\(n=1\) の補正の微分は
\(O(e^{-2t})\)。従って \(H(u)=\log\Phi(\sqrt u),\ t=\sqrt u\) について

\[
H'''(u)=-\frac{\pi e^{2t}(4t^2-6t+3)}{4t^5}
+\frac{27}{16t^5}+O(e^{-2t}/t^3)<0
\]

が十分大きな \(u\) で成り立つ。\(\Delta_h^3 H(u)\) はこの導関数の
三重積分なので、大きな \(u\) で負となり (6) と矛盾。
微分の極限交換を仮定していない。任意の正係数多項式や別の保存変換の閉包まで
排除する定理ではない。

実核に対する小さい区間計算でも照合した。\(u=4,5,6,7\) の4点で
\(\Delta_1^3H(4)=-13.2185241442\ldots<0\) をArb192bitと解析尾で認証。
各点の \(X=\pi e^{2\sqrt u}>100\) に対し、\(n\ge2\) の相対尾は
\(64e^{-3X}\) 以下。これは \(n^4\) の隣接比が6未満、\(n^2\) の
隣接差が5以上である幾何級数評価から従う。対数差分の全誤差は
\(512e^{-300}<2.64\times10^{-128}\)。これは形状による構成の反証であり、
Weil窓や零点計算の拡大ではない。

## 5. 実際の算術和からの二つの直接構成

### 微分因子と正のflux

\(\theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}\)、
\(\Psi(t)=e^{t/2}\theta(e^{2t})\) とする。Poissonの変換則から \(\Psi\) は偶、
項別微分から \(\Phi=(\Psi''-\Psi/4)/2\)。従って

\[
U=2\cosh(t/2)-\Psi,\qquad (-D^2+1/4)U=2\Phi. \tag{7}
\]

\(U\sim e^{-|t|/2}\) なので、Fourier恒等式
\((z^2+1/4)\widehat U(z)=2\widehat\Phi(z)\) はまず
\(|\Im z|<1/2\) で成立する。外側の \(\widehat U\) は有理型接続として扱い、
全複素平面で元の積分が収束するとはしない。

\(t\ge0\)、\(x_n=\pi n^2e^{2t}\) で

\[
P=e^{t/2}U=1-2e^t\sum_{n\ge1}e^{-x_n},
\quad P'=2e^t\sum(2x_n-1)e^{-x_n}>0,
\]
\[
P''=2e^t\sum(-4x_n^2+8x_n-1)e^{-x_n}<0.
\]

\(x_n\ge\pi>3\) を使うだけで符号が決まる。
\(U(0)>0\) は \(\theta(1)<2\) から従うので、\(P\) は正・増加・凹で極限は1。
また \(W=(D+1/2)U=e^{-t/2}P'>0\)、\((-D+1/2)W=2\Phi\)。
これは実際の核に対する算術的な符号関係である。

しかし \(P\) をBernstein型、すなわち全高階の導関数が交代符号を持つものへ
強化する候補は失敗する。偶性と (7) から

\[
P'''(0)=U(0)/2-3\Phi(0)<-1/6<0. \tag{8}
\]

粗い厳密評価だけで十分：\(0<U(0)<1\) および
\(\Phi(0)>(4\pi^2-6\pi)e^{-\pi}>18/81=2/9\)
（\(3<\pi<4,e<3\) を使用）。Bernstein型なら \(P'''\ge0\) が必要。
従ってこの強化を終了。正の \(P'\) 単独をPSDや零点排除と同一視しない。

### 整数移動の和と差引項

\[
k(t)=e^{t/2}(4\pi^2e^{4t}-6\pi e^{2t})e^{-\pi e^{2t}},
\quad \Phi(t)=\sum_{n\ge1}n^{-1/2}k(t+\log n). \tag{9}
\]

半直線では (1) の右辺を、偶性を仮定せず \(K[f]\) と定義し、
\(H[f](a,b)=\int_0^\infty f(t+a)f(t+b)dt\) とする。
\(p_n=\log n,w_n=n^{-1/2}\) と置くと

\[
\boxed{K[\Phi](a,b)=\sum_{m,n}w_mw_n
\left\{K[k](a+p_m,b+p_n)-\frac{p_m+p_n}{4}H[k](a+p_m,b+p_n)\right\}.} \tag{10}
\]

\(s\ge0\) では
\(w_n|k(s+p_n)|\le Cn^4e^{-\pi n^2/2}e^{9s/2}e^{-(\pi/2)e^{2s}}\)。
\(\log n\) を掛けても総和可能であり、(10) の和・積分交換は絶対収束で正当化できる。
差引項は \(L\Phi(s)=\sum w_n\log n\,k(s+\log n)\) を使った
\(\frac14\int[L\Phi(t+a)\Phi(t+b)+\Phi(t+a)L\Phi(t+b)]dt\)。
点ごとに正でも、符号付き試験関数でのPSDとは異なる。

基底核のPSDを仮定しても、移動和からこの差引項を引けるという評価は得られない。
一般論は単一移動でも偽：\(g(t)=e^{-ct^2}\), \(f_p(t)=g(t+p)\), \(p>0\) に対し

\[
K[f_p](a,b)=\frac{f_p(a)f_p(b)}{8c}-\frac p2H[f_p](a,b).
\]

異なる二点で第一項を消す係数を取ると、移動Gaussianの線形独立性から
\(H\) の二次形式は厳密に正となり、全体は負となる。
**正の移動係数だけでPSDを移植する候補も終了。**
実際の算術和や \(k\) の反例ではなく、その和に固有の制御が必要という判定。

## 検証範囲と判定

- (2)、(3) は ROOT/BUILDER が独立導出。
- 四次模型は ROOT/BUILDER/DESTROYER が別々に係数を確認。5点の証人と複素点の証人も一致。
- 位数1の拡張は ROOT/DESTROYER、実核の三次差分障害は ROOT/LITERATURE が独立確認。
- (7)〜(8) は ROOT/LITERATURE、(9)〜(10) は ROOT/BUILDER が独立導出し、
  Fourier積分のstrip制限と差引項を保持した。
- [再現スクリプト](../../../artifacts/experiments/scripts/internal_kernel_checks.py) は有理数で(5)を検算。
  元積分の70桁求積も \(-0.00068125\) と誤差約 \(2.1\times10^{-58}\) で一致する。
  この求積は非認証であり、符号の根拠は有理数恒等式。
- 正・対数凹・増加scoreからPSDを出す候補と、上のGaussian実因子積による実核の構成は停止。
  **RHの反例ではなく、主証明グラフへの合流は0。**

実際のtheta算術和も直接調べたが、今回得たのは符号のある低階の微分関係と
差引項を含む恒等式まで。独立した全域の正値化機構は未達。
終了した形状条件・Gaussian積・単純移動・Bernstein強化を次巡に再開しない。
以後も内部構築を優先し、実際の算術量に対する新しい制御が現れた場合だけ次の候補とする。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/scripts/internal_kernel_checks.py`](../../../artifacts/experiments/scripts/internal_kernel_checks.py)
- [`proofs/audits/freedman-weyl-bridge-gate.md`](../../audits/proofs/audits/freedman-weyl-bridge-gate.md)
