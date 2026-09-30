**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_variational_dictionary.md` · Original SHA-256: `16cc6d1d6ab7e9b5d96d7f0e0c6c8573dcef62a00e41a40b121ba71152f2d513`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Common-parent variational dictionary

2026-09-30。RH OPEN。既存ファイルは読取専用。
本稿の \(A\) はWeil ground、\(B\) は指定されたprolate proxyを表す。
記号 \(B\) と区別するため算術和写像を \(S_\lambda\) と書く。

## 1. A の exact objective

\[
 a=\log\lambda,\quad L=2a,\quad
 Y_\lambda=L^2([-a,a],dt),\quad
 V_j(t)=L^{-1/2}e^{2\pi ij(t+a)/L},\quad
 E_N=\operatorname{span}\{V_j:|j|\le N\}.
\]
全関数は区間外で0とする。\(V_j\) は周期基底だが、その零延長の
convolutionにprime/Gamma/poleのWeil distributionを作用させる。
周期convolutionへ置換しない。

\[
 Q_{\lambda,N}=(Q_W(V_m,V_n))_{m,n=-N}^N,\qquad
 e_0=\min_{\|v\|_2=1,\ v\in E_N}Q_W(v,v).
\tag{A1}
\]
標準内積は \(dt=du/u\)。本比較に使うnormはこの内積であり、
determinant構成の \(Q-e_0I\) による商内積とは異なる。
固有方程式は \(Q_{\lambda,N}v=e_0v\)。
ESは \(e_0\) が単純で、\(Jv(t)=v(-t)=v(t)\) であること。
reflectionとQが可換でも、global groundが偶という結論は自動ではない。

自然なprime-side表示は
\[
 Q_W(f,f)=\int_{\mathbb R}|\widehat f(t)|^2
       \frac{h_\Gamma(t)}{2\pi}\,dt
 +2\Re\!\left(\widehat f(i/2)\overline{\widehat f(-i/2)}\right)
 -2\sum_{p^k\le\lambda^2}\frac{\log p}{p^{k/2}}
                       \Re(f^**f)(k\log p),
\tag{A2}
\]
\[
 h_\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi,\qquad
 \widehat f(z)=\int f(t)e^{-izt}dt.
\]
Gamma multiplier、rank-two pole term、prime shiftsを含む符号付きの形式。
これを無条件に非負leakageと呼ばない。
[CCM, §§3–5](https://arxiv.org/html/2511.22755v1)。

## 2. Prolateの最適化と、指定Bの構成は同じではない

additive空間 \(X_\lambda=L^2([-\lambda,\lambda],dx)\) で、
\(\mathcal Fh(\xi)=\int h(x)e^{2\pi ix\xi}dx\) とする。
\(P_\lambda=1_{[-\lambda,\lambda]}\)、\(\widehat P_\lambda=\mathcal F^{-1}P_\lambda\mathcal F\)。
\[
 C_\lambda=P_\lambda\widehat P_\lambda P_\lambda,\qquad
 J_{\rm leak}(h)=\|(I-P_\lambda)\mathcal Fh\|_2^2
               =\|h\|_2^2-\langle h,C_\lambda h\rangle.
\tag{B1}
\]
単位normでleakage最小、同値にconcentration最大のvectorは \(\psi_{0,\lambda}\)。
高次mode \(\psi_{j,\lambda}\) は先行modeへの直交制約下のmin–max解。
\[
 PW_\lambda=-\partial_x((\lambda^2-x^2)\partial_x)+(2\pi\lambda x)^2,
\qquad PW_\lambda\psi_j=\theta_j\psi_j,\quad
 C_\lambda\psi_j=\kappa_j\psi_j.
\tag{B2}
\]
regular endpoint realizationを使う。Dirichlet端点値0を勝手に課さない。
\(x=\lambda y\) で \(PW_\lambda=-\partial_y((1-y^2)\partial_y)+c^2y^2\)、
\(c=2\pi\lambda^2\)。\(\kappa_j\) はconcentration eigenvalueであり、
\(\theta_j\) やWeilの \(e_j\) と同じではない。

指定proxyのseedは
\[
 I_j=\int_{-\lambda}^{\lambda}\psi_{j,\lambda}(x)dx,\qquad
 h_\lambda\ \propto\ \psi_{4,\lambda}-(I_4/I_0)\psi_{0,\lambda}.
\tag{B3}
\]
各 \(\psi_j\) の任意の非零スカラー正規化は、このdirectionを変えない。
\(\int h_\lambda=0\) はexactだが、\(h_\lambda\) はPWやCの固有vectorではない。
2次元span内のmean-zero条件で方向を選んだものであって、
全mean-zero空間のconcentration最適解ではない。

後者の非同一性はLagrange式から直接検査できる。
もし \(h_\lambda\) がeven mean-zero空間のconcentration stationary pointなら
\[
 C_\lambda h_\lambda=\kappa h_\lambda+\eta\,1.
\]
\(\psi_{2,\lambda}\) 成分を取ると \(\eta I_2=0\)、\(I_2\ne0\) なので \(\eta=0\)。
すると \(\kappa_0\ne\kappa_4\) の二つの非零成分に同じ固有値を要求し矛盾。
Fourier-positive branchだけに制限しても \(\psi_8\) で同じ検査ができる。
これらの局所固有関数の性質と原典の規約は
[B担当ノート](common_parent/notes/B_variational_and_equations.md)に記載。

## 3. B をAへ入れるcanonical map

\[
 (S_\lambda h)(u)=\sqrt u\sum_{1\le m\le\lambda/u}h(mu),
 \quad u\in[\lambda^{-1},\lambda],\qquad
 k_\lambda=S_\lambda h_\lambda.
\tag{B4}
\]
seedは偶なので正半直線の値だけで計算する。
log座標の \(k_\lambda(e^t)\) と、additive seedの \(h_\lambda(x)\) を混同しない。
\(k_\lambda\) が有限 \(\lambda\) でlog反転に関して偶とは限らない。
finite Fourier eigenvaluesの異なる0/4 mixtureを、
全実線Fourier不変関数として扱ってはいけない。

有限Weil行列へ代入する際は、既存の直交射影だけを使う：
\[
 p_{\lambda,N}=P_N[k_\lambda(e^t)],\qquad
 b_{\lambda,N}=\frac{p_{\lambda,N}}{\|p_{\lambda,N}\|_2},
 \quad p_{\lambda,N}\ne0.
\tag{B5}
\]
計算ではraw proxyを使い、偶化・zero位置を用いた補正・新内積を加えない。
zero extension由来の内部jump \(t=\log(\lambda/m)\) と端点を積分で処理する。

## 4. 一枚のobjective比較

|項目|Weil ground A|prolate最適化と指定proxy B|
|---|---|---|
|目的量|\(Q_W(f,f)\) の最小化|各modeはconcentration min–max。指定Bは0/4 mean-zero mixtureの算術像|
|場所・norm|\([-a,a]\), \(dt=du/u\)|seedは \([-\lambda,\lambda]\), \(dx\)。算術像では \(du/u\)|
|制約|\(f\in E_N,\ \|f\|_2=1\)|各modeは先行modeと直交。seed mixtureはspanとmean-zeroで選択|
|境界|周期Fourier基底の零延長|regular prolate endpoint、値0ではない|
|Euler式|\(Q_{\lambda,N}v=e_0v\)|各 \(\psi_j\): PW/C固有式。mixtureは同じ1固有値式を満たさない|
|算術|実際の全 \(p^k\le\lambda^2\)、Gamma、pole|seed最適化にprimesなし。後段 \(S_\lambda\) の整数和が算術入力|
|localization|log support、非局所prime shifts|additive space/frequency leakage|
|対称性|reflection可換。ESは別義務|seed additive-even。像のlog-evenは有限段階で自動でない|
|親を同一視するための不足|BのWeil energy excessとfull gap|算術像にconcentration最適性を運ぶ恒等式がない|

## 5. 自然なpullbackは書けるが、common parentの発見ではない

正半直線上 \(X_\lambda^+=L^2((0,\lambda),dx)\) を使うと、
\(S_\lambda:X_\lambda^+\to Y_\lambda\) はboundedかつonto。
ただし \((0,\lambda^{-1})\) にsupportを持つ関数はkernelへ落ちる。
\[
 G_\lambda=S_\lambda^*S_\lambda\ne I,\qquad
 \mathcal J_A(h)=\frac{Q_W(S_\lambda h,S_\lambda h)}
                       {\langle h,G_\lambda h\rangle}.
\]
pullback Euler式は弱形式で
\[
 S_\lambda^*Q_WS_\lambda h=\mu G_\lambda h,
\]
finite版なら \(S_\lambda\) を \(P_NS_\lambda\) に置く。
これはAを別座標で書いただけで、Bの選択を導いていない。
新しい算術metricを発明したものでもない。

実際、kernel内の非零smooth mean-zero \(h\) に対し、pullback energyと
\(\|S_\lambda h\|^2\) は0だが \(J_{\rm leak}(h)>0\)。
従って自然な全source空間上で
\[
 Q_W(S_\lambda h,S_\lambda h)
       =\alpha_\lambda J_{\rm leak}(h)+\beta_\lambda\|S_\lambda h\|^2
 \quad(\alpha_\lambda\ne0)
\]
という単純な同一視は偽。
追加のconstraintや非自明な誤差項を含む全ての未知parentの不存在を証明したわけではない。

## 6. 原典のtrace connectionと、本問のvector energyは別

Connesのtrace formulaはcutoff projections、scalingの積分作用、Weil distributionを結ぶ。
しかしtrace identityから、指定trial vectorのRayleigh値やground-state orderが同じとは言えない。
CCの公刊 *Spectral triples and ζ-cycles* §3は、
算術和像がWeil formのradicalに入ることを既に記録している。
ここでの像は \(f(0)=\int f=0\) を満たす全域Schwartz関数の算術和であり、
有限切断 \(S_\lambda h_\lambda\) 全体をradicalと主張するものではない。
これがproxyの小energyを考える既知の動機であり、concentrationのunique minimumと
Weilのunique minimumの同一化定理ではない。
[公刊原典 pp.118–120](https://ems.press/content/serial-article-files/44477)。

## 7. Type I–IV の分類

|Type|候補|判定|
|---|---|---|
|I 同じminimizer|Bも通常concentrationの制約付き最小解|上述KKTで指定解釈はFALSE。A/B共通の別目的量は未取得|
|II 同じparent・別座標|\(S_\lambda\) pullback|exactだが非等長・kernelあり。Aの再表現以上にはならない|
|III 双対variational principle|Fourier/Mellinによるprimal/dual同一化|trace/変換の対応は既知。objectiveとconstraintのdual identityは未取得|
|IV 共通limit・unique minimizer|global Weil formをlimitとする|自然なextended formには無限次元radical。正性があっても最小解は非一意|

**NO COMMON PARENT IDENTIFIED.**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/common_parent/notes/B_variational_and_equations.md`](common_parent/notes/B_variational_and_equations.md)
