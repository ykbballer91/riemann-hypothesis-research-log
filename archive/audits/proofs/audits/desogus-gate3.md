**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/desogus-gate3.md` · Original SHA-256: `73a82b9e72556245f4215d7e00105a3250dac8204cf9af8e52cee7482e609def`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus 2609.20367v2 — Gate III 独立敵対監査

2026-09-29。担当 DESTROYER。対象は [v2, 20 September 2026](https://arxiv.org/html/2609.20367v2)、比較は [v1](https://arxiv.org/html/2609.20367v1)。状態は **UNVERIFIED EXTERNAL PROOF CLAIM**。本稿は全論文・Gate II・計算証明を検証したものではない。RH は OPEN。

## 0. 判定と最小 cut

Gate III から致命的な数学的 cut は現時点で得られない。restricted odd criterion と cofinal-support 移行は独立に再証明できる。局所 operator の domain 表記は補足を要するが修復可能。

一方、Lemma 7.1 の「global closed explicit-formula form への closure」は Hilbert 空間を指定しておらず、通常の global $L^2_{\rm odd}(\mathbb R)$ の意味では自身の positivity 仮定の下でも成立しない。しかし **この closure は RH の結論に不要**。compact real-odd core の非負性だけで Theorem 1.2 に進める。従ってこの問題を外部証明全体の致命的反証と扱ってはいけない。

追加依頼で Gate II の一部を独立確認した結果、§7 に **Lemma 8.4 の二枝短縮 $2D$ と、Theorem 8.5 が用いる残差 $Q-D$ の不整合**を記録した。これは原文表示のままでは通らない具体的な bridge であり、Gate III の条件付き成立とは区別する。

| ノード（v2） | PROVED-IN-PAPER | 独立再証明 | 状態・依存 |
|---|---|---|---|
| Theorem 1.2 restricted odd criterion | YES | YES | VALIDATED、標準 explicit formula を入力 |
| Lemma 1.3 exterior-harmonic cancellation | YES | YES | VALIDATED on smooth core |
| (18), (19) zero-extension equality | YES | YES as forms | VALIDATED、operator 記法は domain 補足 |
| Lemma 1.4 cofinal support | YES | YES conditional | VALIDATED conditional on unbounded endpoint positivity |
| Corollary 8.6 integer→arbitrary support の部分 | YES | YES conditional | Gate II の各 endpoint の成立自体は NO |
| Lemma 7.1 radius independence/core positivity | YES | YES conditional | VALIDATED、closure 不要 |
| Lemma 7.1 global Hilbert closure | ASSERTED | FAILED in global $L^2$ interpretation | GAP / NOT ACTUALLY NEEDED |
| Certificate 6.62 の基点 | CLAIMED CERTIFICATE | NO here | 別担当の計算監査対象 |
| Lemma 6.28 scalar cancellation | YES | YES with its sign hypothesis | FOLD-FORCING 単独では pivot の符号を供給しない、§7.1 |
| Lemma 8.4 two-arm short → MASTER-P3b の使用 | YES | FAILED AS WRITTEN | 同じ $Q,D$ に対して実際の短縮は $2D$、§7.2 |
| Theorem 8.5 induction step | YES | NO | §7 の bridge を直す追加 estimate / normalization が必要 |

以下の YES は数値サンプルでなく、各命題の再導出を意味する。無条件に全 endpoint が正であるという結論は含まない。

## 1. Theorem 1.2: odd 制限でも本当に十分か

論文の centered bilateral Laplace 規約を使用する:

$$
\lambda=\rho-1/2,\quad F(z)=\int_{\mathbb R}f(y)e^{zy}dy,\quad
\mathcal W[f]=\sum_\lambda F(\lambda)\overline{F(-\bar\lambda)}.
$$

real odd $f$ では $F(-z)=-F(z)$、$F(\bar z)=\overline{F(z)}$。
従って各 summand は $-F(\lambda)^2$。RH 下では $F(i\gamma)$ は purely imaginary なので summand は非負。符号と conjugation は正しい。

逆向きの isolation construction を独立に再導出した。

1. $\Re\lambda_0\ne0$ を持つ零点を仮定する。real even bump $\psi$ を原点近傍へ狭めれば、その Laplace transform $\Psi(\lambda_0)$ は非零にできる。実定数倍で modulus を1にする。
2. compact support smoothness により、閉 strip $|\Re z|\le1/2$ 上で $\Psi$ は imaginary direction に任意べきで減衰する。したがって target より高い $T$ と $0<q<1$ を固定し、$|\Im z|\ge T$ で $|\Psi(z)|\le q$ とできる。
3. 高さ $T$ 未満の有限個の non-target symmetry orbits を零化する real even polynomial $P_T$ を作る。target orbit では非零に保てる。
4. $\lambda_0^2=u+iv,\ v\ne0$ の場合、$w_M=(\lambda_0P_T(\lambda_0)\Psi(\lambda_0)^M)^{-1}$ として
   $b_M=\Im w_M/v,\ a_M=\Re w_M-u b_M$ と取れば、
   $R_M(z)=a_M+b_Mz^2$ が所要の正規化を与える。
   $|w_M|$ は一定なので両係数は一様有界。
   $\lambda_0$ が非零実数の退化 case は real constant だけで足りる。
5. $F_M(z)=zP_T(z)R_M(z)\Psi(z)^M$ は real odd smooth compact test の Laplace transform。
   Laplace transform の derivative には負号が付くが、全体の real coefficient に吸収でき、存在や oddness を変えない。
6. $P_T,R_M$ の degree は $M$ に依存しない。固定 $M_0$ に対する rapid decay と $N(T)=O(T\log T)$ から

$$
\sum_{|\Im\lambda|\ge T}|F_M(\lambda)|^2
\le C_Tq^{2(M-M_0)}\longrightarrow0.
$$

target quartet では値は $1,1,-1,-1$、寄与は multiplicity 込みで $-4m$。non-target low zeros は零、high zeros の寄与の絶対値は上の二乗和で抑えられる。従って十分大きい $M$ で $\mathcal W[f_M]<0$。

**検査結果:** 全 support の odd criterion として正しい。test の support は convolution power と共に増えるため、単一固定窓だけで RH が得られるとは言えない。論文はここでその誤量化をしていない。symmetry だけを根拠にした generic quartet 排除ではなく、全 odd test への positivity が必要である。

## 2. Zero extension の係数・prime endpoint・polar profile

$f\in C_c^\infty(-a,a)$、$a<b$ に対し、内外二本の strip を直接積分すると

$$
\mathfrak H_b[Ef]-\mathfrak H_a[f]
=\frac12\int_{-a}^{a}|f(x)|^2
\left\{\int_a^b\frac{dy}{y-x}
+\int_{-b}^{-a}\frac{dy}{x-y}\right\}dx
=\frac12\int|f(x)|^2\log\frac{b^2-x^2}{a^2-x^2}\,dx.
$$

$V_a^{\rm ph}(x)=-\frac12\log(a^2-x^2)$ の変化が正確に打ち消す。係数 $1/4$ の double form、二つの向き、最後の $1/2$ は整合している。

追加した prime translation は長さ $\log n\ge2a$ なので旧 support の自己相関は零。等号 $\log n=2a$ でも overlap は測度零であり、strict threshold の境界に残差は出ない。
regular gamma kernel は物理座標で同じ function of $|x-y|$、polar profile は $\sinh(y/2)$ の literal restriction なので両者も不変。rescaled profile $\sqrt a\sinh(ax/2)$ を異なる $a$ 間で同一視してはいけないが、§1.1 はこの区別をしている。

従って、正しい form domain 上で

$$
q_b(Ef,Eg)=q_a(f,g)
$$

が成立する。これは新しい方向の cross block が零であること、あるいは zero-extended old form との差が PSD であることを意味しない。以前の prime-3 mixed-term 反例とは矛盾しない。

## 3. Eq. (61) と fixed-support domain の補足

固定 $a$ の正しい form domain は

$$
\mathcal V_a=\left\{f\in L^2_{\rm odd}(-a,a):
\int_{\mathbb R}\log(2+|t|)|\mathcal F(Ef)(t)|^2dt<\infty\right\}.
$$

標準 archimedean multiplier $h(t)=\Re\psi(1/4+it/2)-\log\pi$ は下に有界で
$h(t)=\log(2+|t|)+O(1)$。固定 support の prime term は有限個の bounded translations、polar は bounded rank one。従って局所形式は closed semibounded で、form norm は上の log norm と同値。

論文の archimedean constant も独立に照合できる。
$k(r)=e^{-r/2}/(1-e^{-2r})$、$\rho(r)=k(r)-1/(2r)$ とすると

$$
h(t)-h(0)=2\int_0^\infty k(r)(1-\cos tr)\,dr.
$$

また

$$
\int_\varepsilon^\infty k(r)\,dr
=\operatorname{atanh}(e^{-\varepsilon/2})
+\arctan(e^{-\varepsilon/2})
=-\frac12\log\varepsilon+\log2+\frac\pi4+o(1).
$$

$h(0)=-\gamma-\pi/2-3\log2-\log\pi$ と合わせると scalar は
$-\gamma-\log(2\pi)$。rescaling 後の $-\log a$、endpoint potential、regular kernel の負号を含め (61) と一致する。この local normalization には今回反例を得ていない。

smooth odd compact core の form density は、まず support をわずかに縮める dilation、続いて real even mollifier による convolution で得られる。log weight での dilation continuity と dominated convergence を用いる。正値性を仮定する必要はない。

**表記上の修正:** Lemma 1.4 の全 $f\in\mathcal H_a$ に対する $\langle f,A_af\rangle$ は、unbounded operator の通常の bracket としては定義されない。$\mathcal V_a$ 上の closed form として読むか、operator domain に制限する必要がある。この修正は結論を弱めない。

literal operator compression を要求する場合も修復できる。sharp support projections は log form domain を保存する（既存の [dyadic proof](support-propagation-adversarial.md) 第7節）。inner/shell の singular cross kernel は境界付近で $1/(2(u+v))+O(1)$、Carleman estimate により bounded。残りの prime・regular・polar cross terms も固定 support では bounded。そのため closed form は domain の直和上で bounded cross perturbation を持ち、operator domain の block decomposition が得られる。少なくとも Gate III の結論には form equality だけで十分。

局所 form embedding は compact。high-frequency mass は log weight から一様に消え、finite-band restriction は Hilbert–Schmidt。従って固定 $a$ の operator は compact resolvent を持つ。この事実により、実際の局所 operator について strict positivity と kernel の不在が確立すれば、qualitative な positive gap も得られる。一般の無限次元 block matrix の反例をここへそのまま転用しない。

## 4. Integer endpoint → arbitrary support: 一様性の追加仮定は不要

§6.13 は arithmetic endpoint を明示的に

$$
a_k=\frac12\log k,\qquad Y=k
$$

と固定する。Certificate 6.62 の $Y=7$ も $a_7=\frac12\log7$。
§1 の dyadic diagnostics の $a_k=\frac12\log(2^k)$ とは別の indexing である。記号の再使用は注意を要するが、最終 induction で physical radius を $k$ そのものと誤解する必要はない。

全整数 $N\ge7$ に $q_{a_N}\ge0$ が本当に証明されたなら、任意の有限 $a$ と任意の $f\in\mathcal V_a$ に対し、$N>e^{2a}$ を一つ選べば

$$
q_a(f)=q_{a_N}(Ef)\ge0.
$$

これが Lemma 1.4 / Corollary 8.6 の必要部分の全証明。$N$ に一様な spectral gap、$N\to\infty$ の limit exchange、support の微分可能性は必要ない。一方 **全整数 $N$** の前件は必要で、有限計算や各 positive window の局所延長だけでは足りない。

したがって、この箇所は generic propagation の障害を勝手に回避していない。回避したとの核心的主張は前段の Theorem 8.5 の all-step induction にあり、その数学的内容と base certificate を別途監査しなければならない。

## 5. Lemma 7.1: global $L^2$ closure は別問題で、不要

radius independence と compact odd core 上の positivity は第2・4節から成立する。
その後の global closure は空間・norm を指定していない。local closedness や exact compatibility だけから global $L^2$ closability は従わない。

さらに本件では、同 lemma の全局所 positivity 仮定から Theorem 1.2 により RH が従ったとすると、global $L^2_{\rm odd}(\mathbb R)$ 上の Weil form は **closable ではない**。

独立な検査: positive zero height $\gamma_0$ を一つ選び、real even $\phi\in C_c^\infty$、$\int\phi=1$ とする。

$$
f_R(x)=R^{-1}\phi(x/R)\sin(\gamma_0x).
$$

各 $f_R$ は real odd smooth compact test で、$\|f_R\|_2^2=O(R^{-1})\to0$。
$\Phi(t)=\int\phi(x)e^{itx}dx$ と書けば

$$
\widehat f_R(t)=
\frac{\Phi(R(t+\gamma_0))-\Phi(R(t-\gamma_0))}{2i}.
$$

RH 下の Weil form は零点高度での Fourier sampling の二乗和である。
sampling vector は $\gamma_0$ で $i/2$、$-\gamma_0$ で $-i/2$、他で0となる非零 vector へ $\ell^2$ 収束する。証明は各点の極限、Schwartz decay、zero-counting bound による summable domination。multiplicity を含めても同じ。
従って

$$
Q_W(f_R-f_S)\longrightarrow0,\qquad
Q_W(f_R)\longrightarrow m(\gamma_0)/2>0,\qquad
f_R\longrightarrow0\ \text{in }L^2.
$$

これは closability criterion に反する。したがって通常の global $L^2$ closure と解釈した追加主張は、著者自身の positivity 仮定の下で維持できない。他の topology を意図するなら、その空間・注入・completion を別途定義する必要がある。

**分類: GAP, NOT ACTUALLY NEEDED / 削除による修復可能。**
RH の議論は

$$
\text{all integer endpoint positivity}
\Longrightarrow \text{all real odd compact tests positive}
\xRightarrow{\text{Theorem 1.2}}\mathrm{RH}
$$

で完結する。global Hilbert closure の句を丸ごと削除してもよい。
この欠落を理由に Theorem 8.5 が偽だとか、RH が偽だとは結論しない。

## 6. Exact differential audit と版差

**OUR BARRIER:** exact nested restrictions、local closedness、各小ステップの可能性だけでは全 support の非負性は得られない。

**WHY GENERIC METHOD FAILS:** 相互作用の Schur cost と消える gap。対数 multiplier の countermodel でも各正窓は局所延長できるが有限 critical radius で止まる。

**DESOGUS CLAIMED REPAIR:** Certificate 6.62 と Theorem 8.5 の全 arithmetic step に対する strict harmonic-graph positivity。Gate III 自体が新しい arithmetic estimate を追加しているわけではない。

**EXACT THEOREM / LEMMA:** Theorem 8.5 → Corollary 8.6 → Lemma 1.4 / compression (18) → Theorem 1.2。Lemma 7.1 の closure 部分は bypass できる。

**ASSUMPTIONS:** 同一の真の localized Weil form、全 step、正しい common-cut/forcing/tail budget、valid base certificate。これら Gate II の仮定を今回は証明していない。

**IS THE REPAIR ACTUALLY SUFFICIENT?:** 本当にその operator について全 step の positivity が成立するなら YES。論文中で実際に成立したかはここでは UNKNOWN。

**INDEPENDENTLY REPRODUCED?:** 最後の compact-core bridge YES。新規 arithmetic induction NO。

**STATUS:** CONDITIONAL、主な最小 cut 候補は Gate II に残る。global closure の問題は修復可能で主 cut ではない。

v1 と v2 の Theorem 1.2 の isolation proof、Lemma 1.3 の cancellation、Lemma 1.4、Lemma 7.1 の closure 文は同じ数学的構造である。v2 の Gate I regularity、MASTER common-cut、aligned forcing の修正を無視して v1 の別の gap を v2 に一般化していない。今回 YES とした Gate III の項目も、その改訂 Gate II の correctness を保証しない。

## 7. 追加の独立 cross-check: Gate II の scalar short と二枝の debit

親担当・BUILDER から指定された2点を、v2 の原文 TeX と別実行の有理数計算で確認した。参照は [Desogus v2, Lemmas 6.28–6.29, 6.61, 8.4 and Theorem 8.5](https://arxiv.org/html/2609.20367v2)。ここでの有限例は **論文内の一般的な代数推論を検査する例であり、実 Weil form の負方向でも RH の反例でもない**。

### 7.1 FOLD-FORCING は pivot の符号を供給しない

Lemma 6.28 は $1-\beta I>0$ の旧 block を仮定するが、scalar debit の不等式には別に $\Pi^{\rm phys}>0$ を明記している。Corollary 6.29 が与える $g=\mathscr A^{\rm pre}x$ は、その追加の符号を含まない。

両区間の長さを1、$a_-=a_+=1$、$I=J=1$ とし、

$$
\beta=\frac34,\qquad
\mathscr A^{\rm pre}=
\begin{pmatrix}1/4&-3/4\\-3/4&1/4\end{pmatrix},
\qquad x=(3,1).
$$

旧 block は $1/4>0$、$g=\mathscr A^{\rm pre}x=(0,-2)$ なので旧座標はまさに harmonic response である。しかし

$$
\gamma^c=3,\qquad
\Pi^{\rm phys}=Q=-2,\qquad
\widehat h_0=-2,\qquad
D=\frac{|\widehat h_0|^2}{\Pi^{\rm phys}}=-2.
$$

形式恒等式 $Q-D=0=E(1-u)$ は成立する。これは **負の denominator に対する signed quotient の cancellation** であって、正 block を変分消去した debit の議論にはならない。$\Pi<0$ の自由 scalar を最小化すれば infimum は $-\infty$ である。$\Pi\downarrow0$ の連続拡張も、$\Pi<0$ を正値として使う根拠にはならない。

**独立判定:** Lemma 6.28 自体の条件付き代数は YES。Corollary 6.29 の row identity から $\Pi>0$ を得る推論は FAILED。実 Weil における $\beta_k,a_{k,\pm}$ の特殊な定義から別に符号が証明されているかは、この例だけでは決着しない。

### 7.2 同じ定義の $D$ に対して二枝は $2D$ を消費する

Lemma 8.4 の (207)–(208) の表示にそのまま従えば、固定した $x$ に対する二枝部分は

$$
\Phi(x,t_+,t_-)
=Q[x]+\mathfrak B|\gamma|^2
+\langle Pt_+,t_+\rangle+\langle Pt_-,t_-\rangle
+2\Re\langle bx,t_+\rangle+2\Re\langle bx,t_-\rangle.
$$

$P\succ0$ により厳密に

$$
\inf_{t_+,t_-}\Phi
=Q[x]+\mathfrak B|\gamma|^2-2\|P^{-1/2}bx\|^2
=Q[x]+\mathfrak B|\gamma|^2-2D.
$$

これは原文 (209)–(212) の平方完成とも一致する。対称・反対称座標に移れば、結合は $\sqrt2 b$ であり同じ $2D$ になる。一方、MASTER-P3b と Theorem 8.5 の proof が非負として捨てる部分は $Q-D$ である。原文は $Q$ を scalar short 前の同じ contribution、$D$ を one-arm debit と定義しているので、表示のままでは追加の $D$ が残る。

最小の厳密例は $Q[x]=x^2,P=b=1$。$x=1,t_+=t_-=-1$ に対して

$$
Q-D=0,\qquad
\Phi(1,-1,-1)-\mathfrak B|\gamma|^2=-1.
$$

positive-pivot の one-defect model とも整合する数値を選べる:

$$
\beta=\frac14,\quad
x=(1/3,1),\quad
g=(0,2/3),\quad
\Pi^{\rm phys}=Q=D=\frac23.
$$

このとき旧 block $3/4>0$、$\Pi^{\rm phys}>0$、$Q-D=0$ であるが、同じ $Q,D$ を持つ二枝 block $P=b=2/3$ の短縮は $Q-2D=-2/3$。従って **pivot sign の追加だけでは、二倍の不足は修復されない**。

もちろん $\mathfrak B|\gamma|^2$ など別項が実際の Weil form 全体を救う可能性は残る。その場合は不足分 $D$ を支払う新しい estimate、または $Q,D$・枝の Hilbert norm・fold identity の修正を明示する必要がある。ここから実際の Weil form が負だとは結論しない。

**独立判定:** (207)–(212) の二枝平方完成 YES。表示された同じ $Q,D$ でその消去を $Q-D\ge0$ だけにより nonnegative remainder と扱う bridge は FAILED AS WRITTEN。Theorem 8.5 の positivity conclusion を独立確認できない具体的な cut である。枝に未表示の制約があるなら、その制約下の二枝表示そのものを作り直して確認する必要がある。

### 7.3 再現計算

以下は Python 標準ライブラリの Fraction のみを用い、丸め誤差がない。

~~~python
from fractions import Fraction as F
for beta in (F(3, 4), F(1, 4)):
    gamma = beta / (1 - beta)
    xm, xp = beta / (1 - beta), F(1)
    g = (xm - beta * (xm + xp), xp - beta * (xm + xp))
    pi = Q = 1 - gamma
    h = g[1] + gamma * g[0]
    D = h * h / pi
    print(beta, 1-beta, (xm, xp), g, pi, Q, D, Q-D, Q-2*D)
~~~

実行結果は順に

~~~text
beta=3/4: old=1/4, x=(3,1), g=(0,-2), Pi=Q=D=-2, Q-D=0, Q-2D=2
beta=1/4: old=3/4, x=(1/3,1), g=(0,2/3), Pi=Q=D=2/3, Q-D=0, Q-2D=-2/3
~~~

## 8. 有限 scalar repair の read-only 監査

root が独立作成した [desogus_safe_cut_repair.py](../../../../artifacts/experiments/scripts/desogus_safe_cut_repair.py) と [結果 JSON](../../../../artifacts/experiments/results/desogus-safe-cut-repair.json) を読み、Theorem 6.55 の safe-transverse scalar

$$
\frac12+\log(1/w_k)-
\sum_{\substack{n=p^\ell\le k\\n\nmid k}}
\frac{(\log p)^2/n}{1/2+\log(w_{\lfloor k/n\rfloor}/w_k)-d_0},
\quad d_0=0.422785,\quad w_j=\log(1+1/j)
$$

との一致を確認した。整数の sieve / quotient block partition / prime-power divisor removal は正確であり、Arb の各正の denominator と全4993個の gap に対する確定比較は一様下界 $1.5202196525$ を証明する。positive log ball の二乗は、この環境で問題のある zero-crossing ball の二乗に該当しない。

別の256-bit Arb 実行では、SPF・prefix sums を使わず trial division と prime-power branch ごとの直接加算を行った。$k=7,8,33,4998,4999$ の5点すべてで公開 JSON interval との overlap と上記下界を確認した。全4993点の別再実行を行ったと主張しない。script の hash と結果内の source hash の一致も確認した。

~~~text
script SHA256:
5a8a0e4bb782200b4cb0670262055e419093adb06a4b1a6c29f8648666e71eab
results SHA256:
5cb77d4967b16a836de16381b1716a0f8fdcacaf1a2a5865c3ab6f2f558ff18d
~~~

**判定: 有限 scalar repair は YES。** JSON の minimum_at は lower endpoint の最小位置の記録である。厳密な actual-gap argmin まで主張するなら、他の lower endpoint が $k=7$ の upper endpoint を超えることを別に確認すべきだが、一様正値性の assert には影響しない。$k\ge5000$ の解析 tail、common-cut operator identification、§7 の bridge はこの計算で修復されない。

## 9. Compact resolvent による scope 検査

追加の bounded attack として、Lemma 6.28 / Corollary 6.29 の one-defect operator が、真の infinite-dimensional shell Schur operator 全体と unitary に同定されているかを検査した。
**結論は scope fork。full-space の onto unitary 同定なら不可能だが、原文がその強い同定を主張しているとは確認できない。この攻撃を論文の確定反証へ昇格しない。**

### 9.1 真の finite-support shell Schur は compact resolvent を持つ

固定 support 上の localized Weil form の domain は log Fourier weight により制御される。form-unit ball の Fourier tail は

$$
\int_{|t|>R}|\widehat f(t)|^2dt
\le \frac{C}{\log(2+R)}
$$

と一様に小さくなり、固定 support から有限 Fourier band への作用素は Hilbert–Schmidt。従って form-domain の $L^2$ 埋込みは compact である。prime translations と polar/gamma の bounded perturbations はこの性質を変えない。

old/shell の sharp cut を行った対角形式の shell 側 $D$ にも同じ議論が適用できる。old/new cross $B$ は bounded: endpoint singularity は Carleman kernel $1/(x+y)$ 型、他は bounded finite-window terms。
旧 block $A\ge cI>0$ を仮定すれば $A^{-1}$ は bounded かつ compact であり、

$$
T=D-B^*A^{-1}B
$$

は $D$ の bounded compact perturbation。resolvent identity により $T$ は compact resolvent を持つ。この結論に $T\ge0$ は不要。

### 9.2 非原子的な全 $L^2$ 上の multiplication-minus-rank-one は異なる

$\Omega=L_k\sqcup R_k$ を正の有限 Lebesgue measure の非原子的空間、$a$ を実 measurable、有限 a.e. とする。
自己共役 multiplication operator $M_a$ の resolvent は

$$
(M_a-i)^{-1}=M_{1/(a-i)}
$$

であり compact ではない。実際、ある $M<\infty$ に対して $E=\{|a|\le M\}$ は正測度。$E$ 内の互いに素な正測度集合に支えを持つ normalized indicators $f_n$ を取れば、resolvent images も互いに直交し

$$
\|(M_a-i)^{-1}f_n\|_2\ge(M^2+1)^{-1/2}.
$$

従って compactness に必要な収束部分列を持たない。
さらに $K=\beta|1_\Omega\rangle\langle1_\Omega|$ は bounded rank one。
$(M_a-K-i)^{-1}-(M_a-i)^{-1}$ は finite rank なので、rank-one perturbation も compact resolvent にはできない。$a$ が端点で発散しても、この正測度集合の議論は残る。

ゆえに、真の shell space 全体から onto unitary $V$ を用いた

$$
VT V^*=M_{a_{k,+}}-\gamma_k^c|1_{R_k}\rangle\langle1_{R_k}|
$$

という **全無限次元空間での operator equality** は、右辺を上記の literal nonatomic $L^2(R_k)$ 上に解釈する限り不可能。同じ障害は full pre-short operator を Lemma 6.28 の $\mathscr A_k^{\rm pre}$ と onto unitary に同定する解釈にも適用する。

### 9.3 原文の scope を過大に読まない

v2 TeX の該当箇所を再読した:

- Lemma 6.16 は fixed-target ground を $P=|1\rangle\langle1|$ としており、この profile ground は1次元。
- Corollary 6.29（TeX 2913–2940）は complementary coordinates を固定して forcing 側へ移し、残る folded ground channel に one-defect row を置く。
- Lemma 6.60（TeX 4455–4478）は真の $T_k$ を $\mathcal K_k^\perp\oplus\mathbb C\mathfrak e_k$ に分け、normalized Schur minimizer を比較する。
- Lemma 8.4（TeX 4816–4829, 4876–4879）は resulting folded ground component と、その ground contribution の同定を述べる。

以上から **全 shell $L^2$ への onto map は明記されていない**。有限個の source-ground coordinates、1次元 final ground、または一つの harmonic vector 上の energy contribution を意図しているなら、9.2 の spectral obstruction は適用できない。finite-dimensional compression や、一つの vector における row equality は full resolvent の同定ではない。

ただしその限定的読みによって §7 や BUILDER の DG10 の未証明 energy dictionary が自動的に埋まるわけでもない。
必要なのは、$x_{k,\pm}$ の実際の range、Hilbert norm と domain、retained coordinates への map、残りの二次 energy を保持した exact identity である。
本監査ではその新しい identity は得られなかった。

**停止判定: full-space reading は数学的に排除、actual claimed ground-channel reading には本攻撃だけでは不適用。既存の critical unknown はそのまま残す。**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/desogus-safe-cut-repair.json`](../../../../artifacts/experiments/results/desogus-safe-cut-repair.json)
- [`experiments/scripts/desogus_safe_cut_repair.py`](../../../../artifacts/experiments/scripts/desogus_safe_cut_repair.py)
- [`proofs/audits/support-propagation-adversarial.md`](support-propagation-adversarial.md)
