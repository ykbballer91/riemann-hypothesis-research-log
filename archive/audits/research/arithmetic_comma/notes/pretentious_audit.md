**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma/notes/pretentious_audit.md` · Original SHA-256: `a5a972975e8d762cdbafbbfb46456ae183c49604f6e4e694f3a3ac2e9012e28a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma：pretentious distance の限定監査

2026-09-30。主対象は \(\mu\) の非加重部分和。Bohr / Hardy–Dirichlet の別担当資料へは立ち入らない。旧ファイルは変更しない。新規性も RH の進展も主張しない。

## 1. 固定した一次資料

**GS03.** Andrew Granville and K. Soundararajan, *Decay of Mean Values of Multiplicative Functions*, Canadian Journal of Mathematics **55**(6) (2003), 1191–1230, DOI [10.4153/CJM-2003-047-0](https://doi.org/10.4153/CJM-2003-047-0), [掲載 PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9BE47DD2587F7A1078B1D9219B5B3F82/S0008414X00031552a.pdf/decay-of-mean-values-of-multiplicative-functions.pdf)。

使用箇所は §1, p.1192, Eq.(1.2) と番号なし Halász–Montgomery–Tenenbaum theorem。\(f\) は multiplicative、全整数で \(|f(n)|\le1\)、\(x\ge3,\ T\ge1\)。完全乗法的である必要はない。原文の \(2T\) 規約のまま
\[
m_f(x,T)=\min_{|t|\le2T}\sum_{p\le x}
\frac{1-\Re(f(p)p^{-it})}{p}
\]
と置くと、絶対定数で
\[
\frac1x\left|\sum_{n\le x}f(n)\right|
\ll (1+m_f(x,T))e^{-m_f(x,T)}+T^{-1/2}.                 \tag{H}
\]
同頁 Theorem 1 は prime-power Euler factors を保持した別の explicit bound。p.1193 Corollary 1 は completely multiplicative と一般 multiplicative の定数を分けており、前者だけを \(\mu\) へ流用しない。ここで採用するのは一般形 (H)。Halasz の原始論文自体の全文は今回未照合。

**GS08.** Andrew Granville and Kannan Soundararajan, *Pretentious Multiplicative Functions and an Inequality for the Zeta-Function*, CRM Proceedings and Lecture Notes **46** (2008), 205–211, [著者公開の掲載体裁 PDF](https://dms.umontreal.ca/~andrew/PDF/Norm.pdf)。

p.209 の番号なし定義が
\[
\mathbb D(f,g;x)^2=\sum_{p\le x}\frac{1-\Re(f(p)\overline{g(p)})}{p}.
\tag{D}
\]
p.206 は (H) を再掲、pp.210–211 Propositions 6–7 は character / \(n^{it}\) twist の距離の分離を扱う。p.208 Proposition 1 の infinite prime-power logarithmic norm は **completely multiplicative** を仮定するので、\(\mu\) にそのまま適用する根拠にはしない。

以上は該当定理の本文・仮定・符号の照合。論文全体の証明を独立再検証したという意味ではない。GS03 は掲載版を使用。GS08 は著者公開掲載体裁を使用し、別途の査読履歴までは確認していない。以下の代入・積の恒等式・scale obstruction は今回の直接検算。

## 2. \(\mu\) の適用範囲と量化

\(\mu\) は乗法的だが \(\mu(p^2)=0\ne\mu(p)^2\) なので完全乗法的ではない。(H) の一般形には適合する。
\[
\mathbb D(\mu,n^{it};x)^2
=\sum_{p\le x}\frac{1+\cos(t\log p)}p,\qquad
m_\mu(x,T)=\min_{|t|\le2T}\mathbb D(\mu,n^{it};x)^2 .
\tag{1}
\]
従って \(t\log p\approx\pi\bmod2\pi\) は \(\mu(p)=-1\) と \(p^{it}\) の一致に近く、距離を **小さく**する。\(t\log p\approx0\) は距離への寄与を \(2/p\) に近づける。

固定した \(t=t_0\) の距離の下界から、\(m_\mu(x,T)\) の下界は出ない。向きは \(m_\mu(x,T)\le\mathbb D(\mu,n^{it_0};x)^2\)。とくに \(t=0\) で大きい距離を示しても、別の \(t\) が minimum を取る可能性は残る。

全固定 \(t\) についての非模倣という qualitative condition と、\(x\) とともに大きくなる \(|t|\le2T(x)\) の **一様定量下界**も区別する。有限 prime set の位相計算や有限 \(t\)-grid は後者の代用にならない。原文の \(2T\) を \(T\) と書き直すことは可能だが、その際は範囲と error の定数を同時に変更する。

## 3. 非加重積と重み付き Euler 積の符号

有限 prime set \(p\le y\) の非加重積を
\[
P_y(t)=\prod_{p\le y}(1-e^{-it\log p})
\]
とすると
\[
|1-e^{-i\theta}|^2=2-2\cos\theta .
\tag{2}
\]
したがって \(\theta\approx0\) は因子を抑え、\(\theta\approx\pi\) は因子を最大の \(2\) に近づける。この方向は (1) と整合する。「\(\pi\) に近いから Möbius cancellation が強い」と読むのは逆である。

さらに \(P_y(t)\) は
\[
\sum_{d\mid\prod_{p\le y}p}\mu(d)d^{-it}
\]
であり、全 subset products を含む。積が \(y\) を越える整数も含むため \(\sum_{n\le y}\mu(n)n^{-it}\) とは別物。実部ゼロの無限 Euler 積としても今回定義しない。

(H) に近い prime-weighted 積は
\[
Q_x(t)=\prod_{p\le x}(1-p^{-1-it}).
\]
\(H_x=\sum_{p\le x}1/p\) と置き、対数を絶対収束する prime-power 展開で計算すると、一様な \(O(1)\) で
\[
\begin{aligned}
\log|Q_x(t)|
&=-\sum_{p\le x}\sum_{k\ge1}\frac{\cos(kt\log p)}{k p^k}\\
&=-\sum_{p\le x}\frac{\cos(t\log p)}p+O(1)
=H_x-\mathbb D(\mu,n^{it};x)^2+O(1).
\end{aligned}                                                     \tag{3}
\]
つまり \(|Q_x(t)|/\log x\asymp\exp(-\mathbb D^2)\)。ここで \(H_x=\log\log x+O(1)\) を使った。距離が小さい位相では正規化 Euler 積が大きい方向である。

\(\mu(p^k)=0\) for \(k\ge2\) でも、**対数**には (3) の全 prime powers が現れる。これは矛盾ではない。一般 multiplicative の Euler factor は \(1+\sum_{k\ge1}f(p^k)p^{-ks}\)、\(\mu\) の場合は \(1-p^{-s}\)。\(\mu(p^k)=(-1)^k\) と置き換えると Liouville 関数という別対象になる。

## 4. Halász の black box が固定べき savings を出さない理由

非負性と \(\cos\le1\) だけで、全 \(t,T\) について
\[
0\le m_\mu(x,T)\le2H_x=2\log\log x+O(1).                \tag{4}
\]
\(A(u)=(1+u)e^{-u}\) は \(u\ge0\) で単調減少。従って
\[
A(m_\mu(x,T))\ge A(2H_x)
\asymp\frac{\log\log x}{(\log x)^2}.                    \tag{5}
\]
これは (H) の **比較関数の到達可能な最小 scale** の下界であり、実際の \(|M(x)|/x\) の下界ではない。実際の Möbius 和はこの一般評価より小さくてもよい。

仮に \(m_\mu\ge c\log\log x-O(1)\) を一様に得ても、(H) が与えるのは \(O((\log\log x)(\log x)^{-c}+T^{-1/2})\)。固定 \(\delta>0\) に対する \(x^{-\delta}\) へこの式だけで到達するには、第一項に \(m_\mu\gtrsim\delta\log x\) が必要だが (4) と両立しない。error 項だけを小さくするなら \(T\gtrsim x^{2\delta}\) が必要となり、しかも第一項の問題は解消しない。

従って PNT の \(M(x)=o(x)\)、固定した log-power saving、位相の定性的非共鳴を \(M(x)=O(x^{1-\delta})\) と読み替えない。固定 log-power はすべての固定正 \(\delta\) の power saving より弱い。(4)–(5) は一般 Halász black box の限界であり、追加の算術構造を使う別証明への no-go theorem ではない。

## 5. Character twists を混同しない

Dirichlet character \(\chi\bmod q\) に対して
\[
\mathbb D(\mu,\chi(n)n^{it};x)^2
=\sum_{p\le x}\frac{1+\Re(\overline{\chi(p)}p^{-it})}p
=\mathbb D(\mu\overline\chi,n^{it};x)^2.                 \tag{6}
\]
\(p\mid q\) では \(\chi(p)=0\) なので寄与は \(1/p\)。\(\mu\overline\chi\) も一般乗法的かつ絶対値 \(\le1\) で (H) を適用できる。untwisted \(M(x)\) の (H) に必要なのは \(n^{it}\) との比較であり、算術級数や全 twists の評価を求めるなら conductor・高さの範囲を別に明示する必要がある。

GS08 Propositions 6–7 の character 間の分離は「複数の異なる character に同時に近づきにくい」という statement。一つの例外候補まで自動的に排除する評価でも、全 conductor での RH/GRH 級一様 bound でもない。

**Decision:** (1)–(6) の規約・適用域・scale obstruction を保持する。有限位相積の抑制を cutoff Möbius 和の cancellation へ移す定理、または fixed-power saving を与える追加算術入力は得られていない。距離を必要以上の \(\asymp\log x\) まで大きくすると仮定する案は (4) で不可能。既知の pretentious framework の範囲を越える新入力は未提示で、RH は OPEN。限定文献監査はここで終了。
