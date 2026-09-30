**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/desogus-pivot-cancellation-stress.md` · Original SHA-256: `fe236b0039ed6a02005dc2c1f17953187c4dff398f086fcf582544a19ad0e268`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus: small-pivot cancellation の固定 forcing 検査

2026-09-29、DESTROYER。対象は [2609.20367v2](https://arxiv.org/html/2609.20367v2) の Lemma 6.28、Corollary 6.29、harmonic-graph / root-residual identities、Lemma 6.60–6.61。原文 TeX の2774–2940、2630–2770、4455–4512行を再読した。

**判定:** $h=\mathscr A^{\rm cut}x$ の形式的な分子因子だけでは、固定 target reserve から追加の第二 debit $D$ を一様に支払えない。以下は正の pivot、停留条件、固定 forcing、同一 target vector を保つ厳密族。
**単一 debit の $Q-D\ge0$ 自体は否定しない。実 Weil の反例でも RH の反例でもない。**

## 1. 正の one-defect 族と固定 forcing

$|L|=|R|=1$、$a_-=a_+=1$、$I=J=1$ とし、$0<\varepsilon<1$ に対して

$$
\beta=\frac{1-\varepsilon}{2-\varepsilon},\qquad
A_\varepsilon=I_2-\beta
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

これは Lemma 6.28 の unit-length constant-profile sector である。旧 scalar block は
$1-\beta=1/(2-\varepsilon)\ge1/2$。全 $A_\varepsilon$ の固有値は
$1$ と $\delta=1-2\beta=\varepsilon/(2-\varepsilon)>0$。
この族には負の pre-short pivot を使う抜け道はない。

固定 forcing $g=(0,1)$ に対する解は厳密に

$$
x=A_\varepsilon^{-1}g
=\left(\frac{1-\varepsilon}{\varepsilon},\frac1\varepsilon\right).
$$

第一成分の forcing は0なので、旧成分は正確な harmonic response。
左を Schur 消去すると

$$
\gamma^c=\frac{\beta}{1-\beta}=1-\varepsilon,\qquad
\Pi^{\rm phys}=1-\gamma^c=\varepsilon,\qquad
h=1.
$$

右成分は constant profile、$\theta_+=x_+=1/\varepsilon$、
$\widehat h_0=h=1=\Pi^{\rm phys}\theta_+$。従って

$$
\boxed{D=\frac{|\widehat h_0|^2}{\Pi^{\rm phys}}=\frac1\varepsilon.}
$$

分子に形式的な因子 $\Pi$ があっても、解 $\theta_+$ 自体が $\Pi^{-1}$ の速さで増大している。

## 2. $Q-D$ は正しく相殺するが、第二 $D$ は残る

Lemma 6.61 の記号に合わせると

$$
E=|x_+|^2=\varepsilon^{-2},\quad u=1,\quad
c=\gamma^cJ=1-\varepsilon,\quad
Q=E(1-cu)=\varepsilon^{-1}.
$$

従って

$$
Q-D=0=E(1-u),\qquad
\boxed{Q-2D=-\varepsilon^{-1}\longrightarrow-\infty.}
$$

**$Q-D\ge0$ のために $D$ の一様有界性は不要。** この恒等式は族の全点で正しく成立している。
反証対象は、既存の二枝の計算で不足した第二 $D$ を、形式的な分子相殺だけで有限 target reserve に収めるという修復候補である。

## 3. target amplitude を1に固定した同一停留ベクトル

外部 target coordinate を $t$、任意の固定 reserve を $R_*>0$ とし、

$$
\mathcal F_\varepsilon(x,t)
=x^*A_\varepsilon x
-2\Re(\bar t\,x_+)+R_*|t|^2.
$$

$t=1$ を固定した唯一の source minimizer は §1 の同じ $x$。
source Hessian $A_\varepsilon$ は正であり、旧成分を先に消去しても結果は同じ。
その最小値は

$$
\boxed{\inf_x\mathcal F_\varepsilon(x,1)=R_*-\varepsilon^{-1}.}
$$

従って target coordinate の正規化、source stationarity、same-vector bookkeeping は、必要な response bound を自動的には供給しない。
Lemma 6.60 の「ground coordinate one」は全 harmonic vector の Hilbert norm を1にする条件ではない。
仮に全 vector を後から norm 1 にしても、debit と target reserve は同じ二乗因子で縮むので、その比 $D/(R_*|t|^2)=1/(R_*\varepsilon)$ は改善しない。

## 4. 正の core と正確な rank-one root identities も保てる

同じ族を $0<r<1/2$、$\beta=2r^2$、
$s=(r,r)^T$、$\delta=1-4r^2$、
$\varepsilon=\delta/(1-\beta)$ で parametrise する。
旧 core を $C=I_2$、旧 full operator を $A=C-2ss^T=A_\varepsilon$ と置く。
新 target の polar component も正の定数1とし、

$$
C_{\rm new}=
\begin{pmatrix}I_2&b\\b^T&R_*+2\end{pmatrix},
\quad b=2s-e_+,\quad
A_{\rm new}=C_{\rm new}-2(s,1)(s,1)^T.
$$

すると $A_{\rm new}$ は §3 の quadratic form の行列である。
$\|b\|^2=8r^2-4r+1\le1$ なので core Schur complement は

$$
S=R_*+2-\|b\|^2=R_*+1+4r-8r^2\ge R_*+1>0.
$$

core は $r\uparrow1/2$ を含めて一様に正。旧 $A$ も各 $r<1/2$ で正。
root-residual identity の各量は

$$
\eta=1-b^TC^{-1}s=\delta+r,\qquad
\zeta=1-(-e_+)^TA^{-1}s=1+\frac r\delta,\qquad
\eta=\delta\zeta.
$$

しかし $\zeta$ は発散し、$\eta\to1/2$ は消えない。正確な rooted Schur formula も

$$
T=S-\frac2\delta\eta^2=R_*-\varepsilon^{-1}
$$

を与える。従って $\eta=\delta\zeta$ という因数分解だけから小さい root loss は導けない。
これは別の模型を量産したものではなく、§1–3 の同じ forced family に core / polar の辞書を加えたもの。

## 5. 原文への適用範囲と残る必要条件

固定した有界 $x$ に対する $\Pi|\theta|^2$ の連続極限と、固定 forcing に対して $x=A^{-1}g$ を解き直す極限は異なる。後者への適用には解の増大を追跡する必要がある。
一般の Lemma 6.28 の normalization では

$$
\widehat h_0=\frac{\Pi}{\sqrt{|R|}}\theta,\qquad
D=\frac{\Pi}{|R|}|\theta|^2.
$$

target amplitude $t$ に対し $D\le C|t|^2$ を欲しければ、例えば

$$
|\widehat h_0(t)|^2\le C\Pi|t|^2
\quad\text{または}\quad
\Pi|\theta(t)|^2\le C|R|\,|t|^2
$$

のような **actual response estimate** が必要である。row identity 単独はこれを含まない。
reserve 自体が $\Pi^{-1}$ の速さで増える場合や、actual arithmetic forcing が $\sqrt\Pi$ 以上の速さで減る場合は、この族による否定の対象外である。

原文の exact harmonic graph $H_kf=(-A_k^{-1}B_{A,k}f,f)$ と $F_k^\#=H_kf_k^\natural$ は same-target stationary vector を指定するが、単独では $A_k^{-1}B_{A,k}f$ の一様 bound ではない。
現実の folded coordinates と固定 target forcing の写像がまだ未指定である以上、本族を実 Weil の counterexample に昇格しない。

**停止判定:** 「pure numerator cancellation が追加の第二 $D$ の一様支払いを保証する」という generic repair は棄却。単一-charge identity は維持。actual arithmetic response / reserve の未証明の橋は残る。

独立 exact sanity check は $r=7/16,15/32,31/64$、$R_*=2$ に対し Python Fraction で行った。順に $D=79/30,287/62,1087/126$、
$T=-19/30,-163/62,-835/126$、stationarity と $\eta=\delta\zeta$ の等号を有理数として確認した。一般の反証根拠は上の恒等式と $\varepsilon\downarrow0$ の解析である。

ROOTも別の短いFraction計算で同じ3点のstationarity、正pivot、core Schur下界、root identity、Tを独立確認した。
