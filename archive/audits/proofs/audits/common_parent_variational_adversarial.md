**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/common_parent_variational_adversarial.md` · Original SHA-256: `947b7e83dc692b6b2e416ba48667cb32e1cdab847fa951a827ed16354cd1b943`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Common-parent variational comparison: independent adversarial tests

2026-09-30。RH OPEN。一般補題と synthetic 反例の限定監査。
以下の有限行列・移動質量・対角形式は actual Weil form や ζ の反例ではない。
新規性・一般的な変分法の不可能性は主張しない。旧ファイルは変更しない。
actual 行列・実験scriptの独立監査は、作成後の別段階である。

## V1. エネルギー差 / gap が正確に与えるもの

\(A\) は Hilbert 空間上の半有界自己共役作用素、最下点 \(e_0\) は単純固有値、
単位ground vectorを \(v\)、\(P=|v\rangle\langle v|\) とする。
\(\Delta=\inf\operatorname{Spec}(A|_{v^\perp})-e_0>0\)。
形式domain内の単位 \(w\) に対し
\[
 E=q_A(w)-e_0\ge\Delta\|(I-P)w\|^2,
 \qquad\eta=E/\Delta.
\tag{V1}
\]
従って \(\eta\to0\) なら、位相整合して
\[
 d^2:=\inf_{|c|=1}\|w-cv\|^2
 =2(1-|\langle v,w\rangle|)
 =\frac{2\|(I-P)w\|^2}{1+|\langle v,w\rangle|}
 \le2\eta.
\tag{V2}
\]
これは二次形式の定義域で成立し、残差の存在は必要ない。
\(E\to0\) 単独では不十分。\(\Delta\) が同時に消える場合の比を制御する。
一様に正のgapは便利だが必要条件ではない。

even sector内でこの補題を使った場合、得られるのは even groundへの接近である。
全空間のgroundもevenで単純だという ES には、odd sector との最下点比較等が別に必要。
共通の parity 対称性はその比較を供給しない。

## V2. 残差は domain と spectral identification を要する

残差を使うには \(w\in\operatorname{Dom}A\) を仮定する。
\(\mu=\langle Aw,w\rangle\)、\(r=(A-\mu)w\)、\(e_1=e_0+\Delta\) とおく。
\(\mu<e_1\) が分かっているとき
\[
 \|(I-P)w\|\le\frac{\|r\|}{e_1-\mu}.
\tag{V3}
\]
\((A-\mu)\) は \(v^\perp\) 上で少なくとも \(e_1-\mu\) 離れているためである。
また spectral theorem により
\[
 \|r\|^2
 =\langle(A-e_0)^2w,w\rangle-(\mu-e_0)^2
 \ge(\mu-e_0)(e_1-\mu),
\tag{V4}
\]
従って Temple型の \(\mu-e_0\le\|r\|^2/(e_1-\mu)\) が得られる。
\(w\in\operatorname{Dom}A^2\) は不要で、二乗項は \(\|(A-e_0)w\|^2\) と解釈する。

**誤用gate。** 任意の excited eigenvector も \((A-\mu)w=0\) である。
小残差だけでは、近い固有値がgroundであることを識別できない。
有限行列の残差 \(P_NAP_Nw-\mu w\) は、全作用素の残差に含まれる
\((I-P_N)Aw\) を計測しない。定義域を確認せず形式行列から全残差を作らない。

## V3. 小commutator・低energy・共通parityの有限反例

\[
 A=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&0\\0&0\end{pmatrix}
\]
は正、共通の内積、\([A,B]=0\)、両gap=1だが、groundは直交する。
parityを恒等作用とする同じeven sectorに埋め込める。
二つの基底を even compact smooth functions にすれば、同じ窓に支持され、
両者の実周波数Fourier tailはSchwartz型である。
共通局在と可換性は、同じgroundを選ぶことを保証しない。

さらに \(A_j=\operatorname{diag}(0,\delta_j)\)、\(\delta_j\downarrow0\)、\(w=e_2\)
なら energy excessは \(\delta_j\to0\)、Rayleigh残差は0だが、
groundとの距離は位相調整後も \(\sqrt2\)。ここでは \(E/\Delta=1\)。
絶対energyや絶対残差の小ささを(V1)の比と取り違えない。

## V4. 拡大窓で normalized Fourier 比較へ渡す十分評価

\(a=\log\lambda\)、\(f\in L^2[-a,a]\)、
\(\widehat f(z)=\int_{-a}^a f(t)e^{-izt}dt\) とする。
\(r>0\) について evaluation norm は
\[
 M_a(r)=\left(\frac{\sinh(2ar)}r\right)^{1/2},
 \qquad M_a(0)=\sqrt{2a},\qquad
 \sup_{|\Im z|\le r}|\widehat f(z)|\le M_a(r)\|f\|_2.
\tag{V5}
\]
even subspaceではより小さいnormも使えるが、指数次数 \(e^{ar}\) は残る。

単位trial \(w_a\) の normalized transform
\(G_w(z)=\widehat w_a(z)/\widehat w_a(z_*)\)、\(z_*=i/4\) が既知のproxyであると仮定する。
\(\kappa_a=|\widehat w_a(z_*)|>0\)、
\(d_a=\|v_a-w_a\|_2\) は位相を整合したground誤差とする。
\(d_aM_a(1/4)\le\kappa_a/2\) なら、任意compact \(K\) と
\(r\ge\sup_K|\Im z|\) に対し
\[
 \sup_K|G_v-G_w|
 \le\frac{2d_a}{\kappa_a}
 \left(M_a(r)+\sup_K|G_w|M_a(1/4)\right).
\tag{V6}
\]
証明は \(\widehat v=\widehat w+e\) とし
\[
 G_v-G_w=\frac{e(z)-G_w(z)e(z_*)}{\widehat v(z_*)}
\]
を使うだけである。規格化分母への誤差も同時に評価した。

従って \(G_w\) のcompact有界性が既知なら、全 \(0<r<1/2\) で
\[
 \frac{\sqrt{\eta_a}}{\kappa_a}
 \left(M_a(r)+M_a(1/4)\right)\longrightarrow0
\tag{V7}
\]
が(V1)から normalized Fourier比較を得る具体的十分条件。
単位trialに対する \(\kappa_a\) を使っており、未正規化proxyの値を混入しない。
\(\kappa_a\ge\kappa_0>0\) が別に分かる場合には
\[
 \eta_a\lambda^{2r}\longrightarrow0
 \quad\hbox{for every }1/4<r<1/2
\tag{V8}
\]
で十分。例えば \(\eta_a=O(\lambda^{-1})\) は満たす。
単なる \(\eta_a\to0\) とは異なる。
これは全ての誤差に対する norm-based 十分評価であり、特別な cancellationを持つ
actual誤差にも同じ率が必要だと断定するものではない。

Galerkinに投影したproxyを使う場合には、別の誤差がある。
単位 \(p\)、直交射影 \(P_N\)、\(\|P_Np\|>0\)、\(w=P_Np/\|P_Np\|\) に対し
\[
 \|w-p\|^2=2(1-\|P_Np\|)\le2\|(I-P_N)p\|^2.
\]
この投影誤差にも(V5)の窓依存損失を掛ける。
真のground対 projected proxy の比較、projected proxy対元のproxy、
元のproxy対 \(\mathscr X\) は三つの別の段階である。
高次数Fourier tailへ任意階微分の評価を適用するときは、周期境界のtrace一致も要る。

## V5. 分母が良好でも比 \(\eta\to0\) だけでは不足する厳密例

実・偶・非負 \(\phi\in C_c^\infty[-d,d]\)、\(\|\phi\|_2=1\)、\(\phi\ne0\) を固定する。
\(a>4d\)、\(b=a-d\)、\(\Phi(z)=\widehat\phi(z)\) とし
\[
 \psi_a(t)=\frac{\phi(t-b)+\phi(t+b)}{\sqrt2},\quad
 \varepsilon_a=e^{-3b/8},\quad
 v_a=\frac{\phi+\varepsilon_a\psi_a}{\sqrt{1+\varepsilon_a^2}}.
\tag{V9}
\]
支持は全て \([-a,a]\) 内。\(\phi,\psi_a\) は直交単位vector。
固定proxyを \(w_a=\phi\)、移動するgroundを \(v_a\) とする。
\(v_a\) は偶・非負・滑らか、\(\|v_a-\phi\|_2\to0\)。
実周波数では
\[
 \widehat\psi_a(x)=\sqrt2\cos(bx)\Phi(x),\qquad
 |\widehat v_a(x)|\le C|\Phi(x)|
\]
なので、窓に依存しない同じSchwartz envelopeを持つ。
これは strict band limitation を主張するものではない。

2次元 \(V_a=\operatorname{span}\{\phi,\psi_a\}\) 上で
\(A_a=I-P_{v_a}\)、\(B_a=I-P_\phi\) と定義する。
\(A_a\) のgapは1、trialのenergy/gap比は
\[
 \eta_a=\frac{\varepsilon_a^2}{1+\varepsilon_a^2}\longrightarrow0.
\]
さらに
\[
 \|[A_a,B_a]\|=\frac{\varepsilon_a}{1+\varepsilon_a^2}\to0,
 \qquad\|A_a-B_a\|=\frac{\varepsilon_a}{\sqrt{1+\varepsilon_a^2}}\to0.
\]
同じ正内積、共通even sector、同じ窓、同じFourier tail、uniform gapに加え、
作用素のnorm接近もある。しかし
\[
 \frac{\widehat v_a(z)}{\widehat v_a(z_*)}
 =\frac{\Phi(z)}{\Phi(z_*)}
 \frac{1+\sqrt2\varepsilon_a\cos(bz)}
      {1+\sqrt2\varepsilon_a\cos(bz_*)}.
\tag{V10}
\]
\(\widehat v_a(z_*)\to\Phi(i/4)>0\) で規格化は良好。
それでも \(z_1=3i/8\) で右辺は
\[
 \left(1+\frac1{\sqrt2}\right)\frac{\Phi(z_1)}{\Phi(z_*)}
 \ne\frac{\Phi(z_1)}{\Phi(z_*)}
\]
へ収束する。\(\Phi(iy)>0\) は \(\phi\ge0\) による。
小質量の対称な境界近傍成分が複素評価で増幅されるのが欠落項である。
この例は \(\eta_a\asymp e^{-3a/4}\) というpower decayまで持つ。
従って「比が0へ行く」ことを無条件に G* と同一視する推論は棄却する。
actual 誤差がより速く減衰、またはweighted normで小さい可能性は否定しない。
この synthetic \(v_a\) の変換は全実零点性を満たさない。
従って actual CCM の ES から従う追加の実零点定理まで保った反例ではない。
その特殊クラスの正規族・閉包定理から(V7)より弱い十分条件が得られる可能性を排除しない。

## V6. Γ / Mosco convergence でも無限遠へのground逃走は別問題

\(H=\ell^2(\mathbb N)\)、\(q(u)=\sum_{k\ge1}k|u_k|^2\) とし
\[
 q_j(u)=\sum_{k\ne j}k|u_k|^2,\qquad j\ge2.
\tag{V11}
\]
各形式は閉、対応作用素はcompact resolvent。
\(q_j\) の単位groundは \(e_j\)、ground値0、gap1である。
極限 \(q\) の単位groundは \(e_1\)、ground値1。

\(q_j\) は実際に Mosco convergence を満たす。
\(u_j\rightharpoonup u\) なら、固定 \(K\)、\(j>K\) について
\[
 q_j(u_j)\ge\sum_{k\le K}k|(u_j)_k|^2
 \longrightarrow\sum_{k\le K}k|u_k|^2;
\]
\(K\to\infty\) でliminf条件。
\(u\in\operatorname{Dom}q\) に対する固定回復列は
\(q_j(u)=q(u)-j|u_j|^2\to q(u)\)。domain外では回復limsup条件は自明。
それでも単位ground列 \(e_j\) は強収束部分列を持たず、単位球面上の最小値も収束しない。
各段階のcompact resolventとuniform gapは、族全体のequicoercivityではない。
正性やΓ収束を得た場合でも、どのtopologyでgroundの質量を保持するかを別に確認する。

## V7. actual計算を採用する前の限定チェック項目

1. 実装した \(Q_{\lambda,N}\) は actual Weil formの指定基底での同じ形式か。
   parity分割、内積、基底規格化、pole / archimedean / prime-power の係数を確認する。
2. trialは元のproxyか、投影後か、単位化後か。Rayleigh値とgapは同じ内積・同じsectorか。
3. 残差が有限行列内か全作用素か。後者ならdomainとhead外成分の誤差があるか。
4. \(E/\Delta\) の点検を、\(\sqrt{E/\Delta}\,M_a(r)/\kappa_a\) の点検へ渡しているか。
   未証明の \(\kappa_a\) 下界やtruegroundのnormalityを途中で仮定しない。
5. 有限数値は一般漸近評価ではない。誤差認証がなくても探索診断はできるが、
   『収束を証明した』『positive gapを全窓に得た』と記録しない。

**限定結論。** 共通の変分枠を正確に構成できても、必要な定量比較は自動ではない。
(V1)–(V4) は利用可能な一般補題、(V7) は明示的な十分条件。
(V9)–(V10) は ratio-to-zero だけからG*への移送を棄却する。
actual Weil/prolateについて(V7)を証明または反証した成果ではない。

## V8. Step31 script の限定読取監査

対象：`research/common_parent/experiments/rayleigh_probe.py` と `rayleigh_results.json`。
本担当は静的読取、旧独立Arb行列コードとの公式照合、表示結果の射程確認を行った。
原典全体の再監査・数値の独立再実行・全cutoffの区間認証とはしない。

**PASS：規約と構成。**

- \(L=\log c=2\log\lambda\)、\(V_j(t)=(-1)^je^{2\pi ijt/L}/\sqrt L\) に対し、
  係数は \(\int\overline{V_j(t)}k(t)dt\)。script の指数の負符号と中心移動は一致する。
- arch の \(S,C,X\)、\(K=\log\pi-\psi(1/4)-2\operatorname{atanh}(e^{-L/2})-2\arctan(e^{-L/2})\)
  は旧独立Arb組立てと同じ。\(\psi(1/4)=-\gamma-\pi/2-3\log2\) の代入も正しい。
- prime 非対角項の符号は、基底相関の偶化
  \([\sin(2\pi my/L)-\sin(2\pi ny/L)]/[\pi(n-m)]\) に負のvon Mangoldt係数を掛けたもの。
  対角では \(2(1-y/L)\cos(2\pi ny/L)\)。
- pole の \(\beta^2-mn\)、\(\beta=L/(4\pi)\) は
  \(2\Re(a_na_m)\)、\(a_n=2\sinh(L/4)/(\sqrt L(1/2+2\pi in/L))\) から再導出できる。
  real-even sectorだけでなく、指定基底のHermitian行列としての係数も整合する。
- orthonormal Legendreの \(y^2\) 行列は上側を余分に作ってから切るため、
  最終対角に必要な隣接成分を失っていない。\(c_{\rm prolate}=2\pi\lambda^2\)、
  even部分の固有mode indices \((0,2)\) は元の次数 \((0,4)\) に対応する。
- 通常Legendre係数への変換、積分比 \(h_4[0]/h_0[0]\)、
  mean-zeroの有限係数制約、\(x=\lambda y\) による \(1/\sqrt\lambda\) は一致する。
  この線形結合をprolateのgroundそのものと呼んでいない。
- raw \(k\) の対数反転対称性は強制していない。\(\lfloor\lambda/u\rfloor\) の
  breakpoints を分割してから Fourier投影している。
  even/odd sectorと複素係数のノルム処理も整合する。

**補助診断の修正：RESOLVED。** 初回読取の `relative_log_reflection_defect` は
\(|k(t)-k(-t)|^2\) の積分なのに、分割が \(k(t)\) のbreakpointsだけだった。
反転したbreakpointsも加えたunionを使うのが正確である。
main projection / Rayleigh値は \(k(t)\) だけを積分するため、この指摘の直接対象ではない。
rootへ通知後、`breaks + [-x for x in breaks]` のunionと再計算を確認した。
Gaussian quadratureの倍精度比較を厳密包含と扱ってはいない。

**数値の射程。** \(c=13,N=4\) の旧Arb行列midpointとの最大差は
表示結果で \(6.22\times10^{-14}\) 未満。
これは一致診断であり、新しい精度認証ではない。
`gap_resolved_in_float64=false` の行のground overlapやratioは、
浮動小数点の縮退subspaceの任意選択に影響されるため、近似の成否の証拠にしない。
`true` のflagもeps×normによる診断であって、求積・Ritz誤差を含む認証ではない。
同一数値固有分解から作った(V1)のassertは内部整合検査であり、actual gapの証明ではない。
\(c=2,N=4\) の約0.00212、\(c=3,N=4\) の約0.0000328というratioも有限診断に限定する。

読取snapshot SHA-256：

|対象|SHA-256|
|---|---|
|rayleigh_probe.py|`f6081ea013dd69fb03e96ada816325223565a97aece95b55b29e1083e8eacd74`|
|rayleigh_results.json|`9b8fe979a83cd5d857535f68fbb9822b7f839bb0cd199e431312690212f67f08`|

## V9. 自然な大域Weil形式の零空間と非一意性

root/literature提案を零点表示から独立に検算した。
中心化した \(z_\rho=(\rho-1/2)/i\)、Fourier規約 \(F_f(z)=\int f(t)e^{izt}dt\) に対し
\[
 Q(f,g)=\sum_\rho F_f(z_\rho)\overline{F_g(\overline{z_\rho})}
\tag{V12}
\]
を用いる。例えば全 \(m\ge0\) で
\(\int e^{|t|/2}|f^{(m)}(t)|dt<\infty\) を満たす滑らかなtest-spaceでは、
strip内の部分積分と \(N(T)=O(T\log T)\) により十分な次数で絶対収束する。
この位相でcompact cutoffを近似できるクラスについて、明示公式と一致する連続拡張を取る。
任意の \(L^2\) 関数へ定義したという主張ではない。

極限kernel \(k\) は両側super-exponentialで、\(F_k(z)=\mathscr X(z)/4\)。
従って全actual非自明零点で \(F_k(z_\rho)=0\) となり
\[
 Q(k,g)=0\quad\hbox{for every admissible }g
\tag{V13}
\]
がRHなしに項ごとに成立する。
翻訳は指数因子、微分は多項式因子を掛けるので同じradicalに入る。
\(k,k'',k^{(4)},\ldots\) は線形独立である。
線形関係をFourier変換すれば \(P(z^2)\mathscr X(z)=0\)、従って \(P=0\) だからである。

よって自然な大域形式が非負なら、正規化後の最小値0を実現するvectorは一意でない。
もし負のcompact方向があれば、値0の \(k\) はgroundでない。
「自然global functionalの一意なminimizerが \(k\)」という一般Γ極限案は、このままでは使えない。
追加制約による選択原理を全て否定する結論ではない。
またこのtest-space形式を、閉じた正の \(L^2\) quadratic formと無断に同一視しない。
global \(L^2\) closabilityは別義務である。

compact coreで \(e_0(a)=\inf\{Q(f,f):\|f\|_2=1,\ \operatorname{supp}f\subset[-a,a]\}\)
と定める。入れ子性により \(e_0(a)\) は非増加。
滑らかなcutoff \(k_a\to k\) を上記形式位相でも取り、単位化するとRayleigh値は0へ行く。
従って
\[
 \mathrm{RH}\ \Longleftrightarrow\ e_0(a)\longrightarrow0
\tag{V14}
\]
が、この定義のcompact-core Weil criterionとcutoff近似から従う。
順方向は \(Q\ge0\) とcutoffによる上界、逆方向は非増加列の極限0から
各 \(e_0(a)\ge0\)、従って全compact testで \(Q\ge0\) となることを使う。
この0への極限を新しい弱い算術入力として仮定してはいけない。
ここでの \(k_a\) は極限kernelの滑らかなcutoffであり、
actual prolate \(k_\lambda\) のenergy収束を証明したものではない。

## V10. 最終dictionary / Rayleigh報告 / 高精度診断の読取

対象は `research/common_variational_dictionary.md`、
`research/common_parent/notes/rayleigh_calculation.md`、
`high_precision_scores.py` と `high_precision_results.json`。
式・実装・scopeを読取確認した。高精度実験の独立再実行ではない。

**PASS。** dictionary は A の標準 \(L^2(dt)\) objective と、
determinant側の \(Q-e_0I\) 商内積を区別する。
Bの0/4 mixtureをconcentrationの制約最適解とする解釈は、\(\psi_2\) または
positive branchの \(\psi_8\) を使う停留式の矛盾により正しく棄却されている。
Sのkernelを無視しないpullbackは正確だが、元のAの再表現である。
CC既知のradicalを新しい唯一最小化元とせず、自然global形式での非一意性を保っている。

Rayleigh報告の \(p=P_Nk\)、\(c=\langle v_0,p\rangle\) について
\[
 \|cv_0-k\|_2\le\|p\|_2\sqrt\eta+\|(I-P_N)k\|_2
\]
は正しい。さらに同報告の
\(\sqrt{(\lambda^{2r}-1)/r}\) は \(\|e^{r|t|}\|_{L^2[-a,a]}\) であり、
(V5)より少し大きいが安全な評価。
\(0<r<1/2\) 全てでこの積が0へ行けば、既知のproxy値と \(z_*=i/4\) から
規格化分母も非零となり G* の比較部を得る。\(\eta\to0\) だけと同一視していない。
周期端点jumpを含む全変動 \(V_\lambda\) を使った
\[
 \|(I-P_N)k\|_2\le\frac{\sqrt{\log\lambda}}{\pi\sqrt N}V_\lambda
\]
も、\(|\langle V_j,k\rangle|\le\sqrt{2\log\lambda}V_\lambda/(2\pi|j|)\)
と \(\sum_{j>N}j^{-2}\le1/N\) により正しい。

**高精度の射程。** script は288bit Arb組立てのballを文字列midpointへ落とし、
75桁mpmathで固有分解する。trialもdouble係数の文字列表現を再正規化したもの。
従ってここでの極小gap・score・overlapは高精度診断であり、
**proxyだけでなく固有値/gap自体もinterval certificateではない**。
`eigenbasis_residual_max` はmidpoint行列の丸め計算内の残差で、
原行列ballを含む認証ではない。
有限行列の精度問題を診断上改善したことと、actual無限族の誤差を認証したことを分ける。

**通知した軽微な訂正：RESOLVED。** 初回読取の表 \(c=5,N=8\) の \(R_B\) が
\(5.60560\times10^{-13}\) となっていたが、JSON正本は
\(5.605280767840\ldots\times10^{-13}\)。表の対応値は
\(5.60528\times10^{-13}\) へ修正するようrootへ通知した。
最終の数値ノートとmainで修正済みであることを確認した。
これは定性判定・gap補題に影響しない。

読取snapshot：

|対象|SHA-256|
|---|---|
|common_variational_dictionary.md|`cc22aa8f2850d4e92192b688b7b638450f07934610f1bae2b058f7e91c5eda42`|
|rayleigh_calculation.md|`2762e656557b19bd4c3ace077c63b67cecd70ce9d99b30227da683248647bab0`|
|rayleigh_probe.py（breakpoint修正を確認）|`f6081ea013dd69fb03e96ada816325223565a97aece95b55b29e1083e8eacd74`|
|high_precision_scores.py|`a51ce206595b6e01becbbef203b13ce7c06e39898cc240dbf8790f087c75f60c`|
|high_precision_results.json|`72a7df15f842a816023d367dde13c1b5ad18d49cd6ead21f8d5598db5a780b5e`|

**総合判定：限定 PASS。** 共通parentの新定理、actual almost-minimizerの漸近、
gap比の極限、G* は得られていないという停止判断と整合する。

## V11. Main / candidate matrix / state の最終処分

`research/common_parent_variational_principle.md`、
`research/common_parent_candidate_matrix.md`、`research/common_parent_state.json` を全文読取した。
最終dictionaryのradicalの範囲、数値表の訂正、high-precision script/JSONの
midpoint非認証scopeの変更も確認した。計算は再実行していない。

**最終判定：PASS。blocking error は認めない。**

- 指定Bの非停留性は、通常のeven mean-zero concentration問題への限定反証。
  あらゆる未知の目的関数の不存在とはしていない。
- \(S_\lambda\) のkernelとcanonical pullbackを正確に区別し、
  objectiveの一致や \(\ker S_\lambda\) を保つdescentは別義務としている。
- 既知CCのglobal radicalは、pole条件を満たす全域Schwartz関数の算術和が対象。
  finite cutoffの \(S_\lambda h_\lambda\) が全てradicalに入ると拡張していない。
- 自然global形式の非一意性と、負方向がある場合のzero-energyの非最適性を分けている。
  閉じたglobal \(L^2\) 正形式を無断に仮定していない。
- \(\eta\to0\) の距離評価と、projection tail・増大窓を含む(V*)の十分評価を区別する。
  (V*)を必要最小条件とはしていない。ESはactual RH接続の別前件として残る。
- 数値は18件の倍精度診断、9件の高精度midpoint再評価。
  eigenvalue/gap/scoreもproxyもinterval認証ではないことがmain・note・script・JSON・stateで一致する。
- 大きな \(\eta\) を距離の下界とせず、固定Nの有限失敗を許容同時極限の反証にしない。
- Level1、共通parent未同定、G*未証明、RH OPEN、三系統で停止という結論は整合する。
  `B_exact_variational_problem_fixed` は付属 `B_scope` と合わせ、指定構成と
  通常の最適化との非同一性を固定した意味で読む。Bの新しい最適化原理の構築ではない。

最終snapshot SHA-256：

|対象|SHA-256|
|---|---|
|common_parent_variational_principle.md|`ddab318de9b3001d623b713c8459a6bf1e4c0bedcb0a1240e8db6b2a63f730e8`|
|common_parent_candidate_matrix.md|`416cf929f1be858b5e1d0502eeca3dee6349a148fe866d793c4e721f4b6723fb`|
|common_parent_state.json|`b0e3575ae929b73c9da5afd9d37040677e37f8d67e80ea737bd27667fd9b8080`|
|common_variational_dictionary.md|`16cc6d1d6ab7e9b5d96d7f0e0c6c8573dcef62a00e41a40b121ba71152f2d513`|
|rayleigh_calculation.md|`774d1a240a39482303220fb7a72a2b4f71cf227e35afb089dec9b260acc86b09`|
|high_precision_scores.py|`01fda43df351f0d40340eb1f3438a0deff9d687de867ef8f2c53aba95c8810f8`|
|high_precision_results.json|`6ef2c1945a04a5207c4f18f5a64f9b88741227e9bb2aff01a796f7f0e8391a84`|

追加の未解決訂正要求はない。今回の編集は本trackで新規作成した本auditのみ。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/common_parent/experiments/rayleigh_probe.py`](../../../../artifacts/research/common_parent/experiments/rayleigh_probe.py)
- [`research/common_parent/notes/rayleigh_calculation.md`](../../../reports/research/common_parent/notes/rayleigh_calculation.md)
- [`research/common_parent_candidate_matrix.md`](../../../reports/research/common_parent_candidate_matrix.md)
- [`research/common_parent_state.json`](../../../../data/source-records/research/common_parent_state.json)
- [`research/common_parent_variational_principle.md`](../../../reports/research/common_parent_variational_principle.md)
- [`research/common_variational_dictionary.md`](../../../reports/research/common_variational_dictionary.md)
