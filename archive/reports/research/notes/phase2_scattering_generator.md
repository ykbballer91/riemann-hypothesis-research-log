**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase2_scattering_generator.md` · Original SHA-256: `583df90f6c03f1c648bcfa43f8ff54ee17fcd9df85cd6211071ee604a4206e29`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase II C — 算術的Laplacianから境界散乱を構成する

2026-09-29。内部導出後に一次文献で規約・既知性を照合した。
**判定:** actual Euler/Gammaを保つ生成子とexact boundary mapは構成できる。
しかしζ零点を生成するのは自己共役スペクトルではなく散乱の極である。
自然な自己共役cut-offへの置換は全ζ零点を落とす。RHは未証明。
新規性は主張しない。これはこの具体候補に対する判定である。

## 1. Candidate generator / Arithmetic input

\(X=\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H\)、
\(\mathscr H=L^2(X,dx\,dy/y^2)\)。
compact supportのsmooth automorphic関数のDirichlet形式
\[
q(f)=\int_X(|f_x|^2+|f_y|^2)\,dx\,dy
\]
を閉包し、そのFriedrichs作用素を \(G\) とする。
\(G\ge0\)、\(G=G^*\)、局所微分式は
\(-y^2(\partial_x^2+\partial_y^2)\)。この構成にRHは不要。
自己共役性は形式の定義から独立に供給され、零点から作用素をfitしていない。

算術入力は整数格子とprimitive pair \((c,d)\)。\(\Re s>1\) において
\[
E(z,s)=\frac12\sum_{(c,d)=1}\frac{y^s}{|cz+d|^{2s}}
\]
は局所一様絶対収束し、\(GE(\cdot,s)=s(1-s)E(\cdot,s)\) を
微分式として満たす。**この式はEがGのHilbert domainに属するとは言わない。**

## 2. Boundary data — exact constant term

\(\mathcal ZE(s)=\int_0^1E(x+iy,s)dx\) をcuspの零次Fourier係数とする。
\(c>0\) を固定し、\(d\bmod c\) のprimitive classと整数translateへ分ける。
\(\varphi_{\rm ar}(c)\) 個のclassごとに積分区間が実直線を覆うので
\[
\mathcal ZE(s)=y^s+y^{1-s}
 \left(\int_{\mathbb R}(1+v^2)^{-s}dv\right)
 \sum_{c\ge1}\frac{\varphi_{\rm ar}(c)}{c^{2s}}.
\]
積分は \(\sqrt\pi\Gamma(s-1/2)/\Gamma(s)\)。素数ごとの級数から
\[
\sum_{c\ge1}\varphi_{\rm ar}(c)c^{-2s}
=\prod_p\frac{1-p^{-2s}}{1-p^{1-2s}}
=\frac{\zeta(2s-1)}{\zeta(2s)}.
\]
すべての交換は \(\Re s>1\) の絶対収束内で行った。その後にmeromorphic continuationする。

Newman定数と混同しないよう、meromorphic completed zetaを
\(Z(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)\) と書く。
\(\xi(u)=u(u-1)Z(u)/2\)、\(Z(u)=Z(1-u)\)。
境界散乱係数は厳密に
\[
\boxed{\mathcal ZE(s)=y^s+\phi(s)y^{1-s},\qquad
\phi(s)=\frac{Z(2s-1)}{Z(2s)}.} \tag{C1}
\]
standard Gamma、全素数、整数primitive条件のいずれも変更していない。

散乱係数からζへの逆再構成もある。\(\Re u>1\) において
\[
r(u)=\frac{\Gamma((u+1)/2)}{\sqrt\pi\Gamma(u/2)}
\phi((u+1)/2)=\frac{\zeta(u)}{\zeta(u+1)},
\quad
\boxed{\zeta(u)=\prod_{j=0}^{\infty}r(u+j).} \tag{C2}
\]
有限積は \(\zeta(u)/\zeta(u+N)\) であり、後者の分母は局所一様に1へ収束する。
\(r(u+j)-1=O_K(2^{-j})\) により積も局所一様に収束する。
そのgermからの解析接続は一意。これが具体的な境界→全解析対象のmapである。
ただし再構成可能性から零点位置は従わない。

prime側との微分同定は \(\Re s>1\) で
\[
\frac{\phi'}{\phi}(s)=\psi(s-1/2)-\psi(s)
-2\sum_{n\ge2}\Lambda(n)(n-1)n^{-2s}. \tag{C3}
\]
この式を収束域外の非負energyとは解釈しない。

## 3. Evolution law / Why 1/2 appears

\(e^{-itG}\) はunitary evolutionを定める。cusp定数modeについて
\(v=\log y\)、\(h(v)=e^{-v/2}f(e^v)\) とおけば
\[
\int |f(y)|^2\frac{dy}{y^2}=\int|h(v)|^2dv,\qquad
G_{\rm cusp}\longleftrightarrow-\partial_v^2+1/4.
\]
したがってunitary channelは \(s=1/2+ir\) のoscillationを持つ。
1/2はこの幾何学的測度による半密度から出る。
\(\phi(s)\phi(1-s)=1\)、実構造と合わせてchannel上の \(|\phi|=1\) も成立する。

しかしζ変数は \(u=2s\)。ζの臨界線は散乱変数では \(\Re s=1/4\) であり、
unitary channel \(\Re s=1/2\) と同じ線ではない。規約の因子2を落としてはいけない。

## 4. 全零点との対応と自由度の所在

\(\rho=\beta+i\gamma\) を非自明ζ零点、重複度を \(m_\rho\) とする。
\(0<\beta<1\)、\(\gamma\ne0\)。実区間(0,1)で零点がないことは
alternating eta級数の正性と \(1-2^{1-s}<0\) からも分かる。

\(s_\rho=\rho/2\) で
\[
Z(2s_\rho-1)=Z(\rho-1)=Z(2-\rho)\ne0,
\]
最後は \(\Re(2-\rho)>1\) のEuler積の非消滅である。
従って \(\phi\) は \(s_\rho\) に次数 \(m_\rho\) の極を持つ。
逆に開strip \(0<\Re s<1/2\) の \(\phi\) の極はすべてこの形である。
分子の極は境界 \(s=1/2\) または外側 \(s=1\) にしかない。

これは**全零点・余剰なし・重複度・実部・虚部**を保つscalar scattering-divisor対応。
Gの全point spectrumとの対応ではない。cuspidal固有値など、Gには別のspectral dataがある。

続くLaplace parameterは
\[
\lambda_\rho=s_\rho(1-s_\rho),\qquad
\boxed{\Im\lambda_\rho=\frac{\gamma(1-\beta)}2\ne0.} \tag{C4}
\]
従って**どの非自明ζ零点もこの対応の下でGのL²固有値にならない**。
RHを仮定しても \(\Im\lambda_\rho=\gamma/4\ne0\)。
この不一致は数値ではなく、全零点に対する解析的な反証である。

多重極の場合は最高次の非零Laurent係数をresonant stateとして取ると、
そのcusp先頭項は非零定数倍の \(y^{1-\rho/2}\)。そのnormのintegrandは
\(y^{-\beta}dy\) で無限遠へ積分すると発散する。log座標の半密度では
\(e^{(1-\rho)v/2}\) となり、\((1-\beta)/2\) が増幅率として残る。
線外自由度 \(\beta-1/2\) はこの指数と散乱極の実部にあり、
自己共役Hilbert-domainの実固有値原理はここへ適用できない。

## 5. 自然なcut-off generatorへの修復を即時検査

自然な境界条件として、高さ \(a\ge1\) より上でcusp定数項を0にする閉形式を取ると、
別の正自己共役cut-off Laplacianが得られる。この構成の既知性は下記原論文で照合した。
この閉形式は元の全 \(\mathscr H\) 上の稠密形式ではない。
\(\mathscr H_a=\{f\in\mathscr H:\int_0^1f(x+iy)dx=0\ \text{for a.e. }y>a\}\)
という閉部分空間で、対応する \(H^1\) 形式domainを閉じてFriedrichs実現する。
対応するcompleted境界関数は
\[
D_a(s)=a^sZ(2s)+a^{1-s}Z(2s-1). \tag{C5}
\]
そのzeroを実スペクトルへ移す既知定理は**この和のzero**についてであり、ζ零点ではない。
実際、任意の \(a>0\) と任意の非自明 \(\rho\) に対して
\[
\boxed{D_a(\rho/2)=a^{1-\rho/2}Z(2-\rho)\ne0.} \tag{C6}
\]
全ζ零点が自然なcut-off determinantから除外される。finite-rankの数値近似ではない。

境界を無限へ送っても、次の局所一様な別の極限になる:
\[
a^{-s}D_a(s)\to Z(2s)\quad(1/2<\Re s<1),
\]
\[
a^{s-1}D_a(s)\to Z(2s-1)=Z(2-2s)
\quad(0<\Re s<1/2). \tag{C7}
\]
各compactで消える項は \(O_K(a^{-2\epsilon_K})\)。両極限はそれぞれのstripで零点を持たない。
したがってcut-off零点を \(\rho/2\) へ局所一様極限で持ってくる案も成立しない。
境界和から片方を代数的に引き去ればζを取り出せるが、引き算はspectral realityを保存しない。
それを任意countertermで補修する案は採用しない。

## 6. What forbids off-line states / hidden assumption

得られた構造で線外resonanceを禁止するものは**ない**。
\(\Re s_\rho=1/4\) を全ての算術的散乱極に要求すればRHと厳密に同値。
『自然な一定減衰率』『critical scattering sector』と名付けても独立入力にならない。
Gの自己共役性自体に循環はない。循環または誤りが入るのは、
散乱極をHilbert spectrumと同一視する段階、あるいは極の実部を別途固定する段階である。

## 7. Synthetic counterexample / arithmetic-specificity

generic unitary scatteringの反例はPhase Iに保存済みであり、新成果に数えない。
今回の決定的検査(C4),(C6)は**actual ζ/Gammaを保持したまま**成立する。
全Euler dataを保持して異なる零点の関数を作ることは解析接続の一意性と矛盾するため、
その意味でのsynthetic反例を作れたとは言わない。RHの反例も得ていない。

## 8. Known prior art / verification scope

- Werner Müller, *A Spectral Interpretation of the Zeros of the Constant Term of Certain
  Eisenstein Series*, 2007, [著者原稿](https://webdoc.sub.gwdg.de/ebook/serien/e/sfb611/331.pdf).
  §0 (0.1),(0.2), Theorem 0.1/0.2と§1のclosed form構成を照合。
  使用は境界係数とcut-off spectrumの区別。本文全体の独立検証ではない。
  中心s=1/2の表記に正規化依存の差があるので、本ノートはその点で定理を使用しない。
- Jeffrey C. Lagarias and Masatoshi Suzuki, *The Riemann hypothesis for certain integrals
  of Eisenstein series*, [arXiv:math/0412039](https://arxiv.org/abs/math/0412039),
  J. Number Theory 118 (2006), 98–122。
  cutoffで得る別関数のzero定理であり、Riemann ζのRH証明ではない。
- 本文係数の別照合: [Suzuki著者ノート](https://www.math.titech.ac.jp/top/~msuzuki/shizuoka_2004_2.pdf),
  (1)–(4)。こちらもs=1/2の除去可能特異点を他のentire規格化と区別する。

(C2),(C4),(C6),(C7)は本作業で上の定義から直接導出したが、新規性を主張しない。
コード `experiments/scripts/phase2_scattering_checks.py` は70桁の非認証診断。
FE、unitarity、(C2)のtelescoping、(C3)、既知の第1零点で(C4),(C6)の規約を点検した。
有限零点探索を全称証明には使っていない。出力にはproves_RH=falseを記録。

## 9. Exact missing lemma / Decision

**不足:** actual modular scatteringのすべてのnontrivial polesの実部を1/4へ固定する、
RHを前提にしない算術的rigidity。これは結論をそのまま書けばRH同値であり、
新しい易しい補題とは数えない。別の独立機構は得られていない。

**判定:** arithmetic construction Aと独立self-adjointness BはPASS。
scalar scatteringとしての完全対応はPASSだが、自己共役spectral realizationとしてのCはFAIL。
cut-offによる修復は(C6),(C7)で棄却。具体的なTrack Cは終了。
一般のboundary/scattering構成全ての不可能性を示したわけではない。

独立監査: LITERATURE担当が(C1)–(C4),(C6),(C7)の算術係数・Gamma比・
正常収束・重複度・parameter変換を独立検算。cut-offのHilbert空間と
多重極のLaurent係数を明示する修正を反映した。既知散乱理論全体の再証明ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/scripts/phase2_scattering_checks.py`](../../../../artifacts/experiments/scripts/phase2_scattering_checks.py)
