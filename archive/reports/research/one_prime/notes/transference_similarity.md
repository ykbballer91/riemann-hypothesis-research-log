**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/one_prime/notes/transference_similarity.md` · Original SHA-256: `3256a46995fc3e15d0f9b9d258cf923ad34b0d705118680304f4bcdc27189981`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# One-Prime Return：intertwiner・similarity・dilation の独立監査

2026-09-29。対象は新規 one-prime track のみ。既存ファイル、Phase III/IV、state、主グラフは変更していない。以下は関数解析上の既知補題と明示的な反例の再検算であり、新規性、RH の証明、RH の反例を主張しない。

**結論。** 全零点の非零連続指標を局所 unitary 表現から引き戻せれば、一つの return で零点の実部を制御できる。surjectivity は不要で、dense range は十分。しかしその intertwiner は算術的に構成されていない。literal な profinite Haar return からの引き戻しは、絶対値だけでなく eigenvalue の torsion 条件も課す。dense intertwiner から global operator norm の一様有界性へ進む一般則は偽。similarity theorem は既に得られた二側一様有界性を正内積に変換する定理であり、その有界性を供給するものではない。unitary dilation はさらに別の関係である。

## TS1. Forward transference の最小条件

\(H\) を Hilbert 空間、\(U:H\to H\) を unitary、\(X\) を Hausdorff 位相線形空間、\(T:X\to X\) を線形作用素とする。線形 map \(J:H\to X\) と非零線形汎関数 \(\ell\) が
\[
JU=TJ,\qquad \ell\circ T=\lambda\ell
\]
を満たすとする。必要な条件は **\(f=\ell\circ J\) が非零かつ \(H\) 上 bounded** である。このとき
\[
f\circ U=\lambda f,\qquad
\|f\|=\|f\circ U\|=|\lambda|\|f\|
\]
なので \(|\lambda|=1\)。ここでは \(U\) の onto 性を使う。単なる一方向 isometry では同じ norm 等式は保証されない。

\(J\) と \(\ell\) が連続なら boundedness が従う。さらに \(J(H)\) が \(X\) で dense なら、\(\ell\ne0\) の連続性から \(\ell J\ne0\)。従って **dense continuous intertwiner は十分、surjective でも injective でもある必要はない**。逆に dense は最小条件ではなく、各対象指標が image を消さないことだけで足りる。

この一つの指標については \(X\) の norm、\(T\) の全 spectrum、\(T\) の operator-norm power bound、実時間への \(C_0\) 拡張はいずれも不要。domain を制限する場合は \(J(H)\) 上で合成が定義され、上の intertwining が成立することを省略できない。

算術的規約を
\[
\ell_\rho\circ T_p=p^{\rho-1/2}\ell_\rho,\qquad p>1
\]
と固定し、全零点について上の条件を証明すれば \(p^{\Re\rho-1/2}=1\)、従って \(\Re\rho=1/2\)。これは正しい条件付き帰結であるが、その全零点を保持する \(J\) の存在は未供給である。

## TS2. Literal Haar return はさらに torsion を要求する

actual local fiber は
\[
H_2=\prod_{q\ne2}\mathbb Z_q^\times,\qquad
\mathcal H_2=L^2(H_2,dh),\qquad (U_2F)(h)=F(2^{-1}h).
\]
\(H_2\) は profinite abelian なので、その連続指標 \(\chi\) は有限像を持つ。指標は完全正規直交系で、
\[
U_2\chi=\chi(2)^{-1}\chi.
\]
従って \(U_2\) は pure point の spectral measure を持ち、各 eigenvalue は root of unity である。「位相的 spectrum の全点が torsion」という意味ではない。固有値集合の閉包には非 torsion の点も入り得る。

bounded nonzero \(f=\ell_\rho J\) が \(fU_2=\lambda_\rho f\) を満たすとき、完全性より \(f(\chi)\ne0\) の指標が少なくとも一つある。その指標に式を適用して
\[
\lambda_\rho=\chi(2)^{-1}.
\]
従って literal な全零点 transfer は
\[
\Re\rho=\tfrac12,\qquad
\frac{\Im\rho\log2}{2\pi}\in\mathbb Q
\]
を同時に要求する。後者の rationality を実際の零点について証明したとも、否定したとも言わない。RH だけからこの stronger fidelity 条件が従うとは未確認である。\(p=2\) を他の一素数へ替えても同じ論理になる。

local mapping torus の全 suspension \(L^2\) を使い、その一周 return を取る場合にも eigenvalue は \(e^{i\omega L}=\chi(p)^{-1}\) で同じ制約が残る。異なる source representation へ変更するなら、算術的選択と full-zero fidelity を新たに証明する必要がある。

## TS3. Dense bounded intertwiner は global power boundedness を与えない

次は synthetic な exact counterexample で、actual adelic quotient の反例ではない。source の eigenvalues さえ全て roots of unity にできる。

\(H=X=\bigoplus_{j\ge2}\mathbb C^2\) を通常の Hilbert 直和とし、
\[
\eta_j=e^{2\pi i/2^j},\quad \delta_j=|\eta_j-1|>0,
\]
\[
U_j=\begin{pmatrix}1&0\\0&\eta_j\end{pmatrix},\quad
J_j=\begin{pmatrix}\delta_j&1\\0&\delta_j\end{pmatrix},\quad
T_j=\begin{pmatrix}1&(\eta_j-1)/\delta_j\\0&\eta_j\end{pmatrix}.
\]
直接乗算で \(J_jU_j=T_jJ_j\)。\(U=\bigoplus U_j\) は unitary、\(J=\bigoplus J_j\) は bounded かつ injective。各有限 block は invertible なので range は全ての有限 support vector を含み dense である。\(\delta_j\to0\) なので全空間で bounded below ではない。

\(T=\bigoplus T_j\) と \(T^{-1}\) は bounded である。実際、各 diagonal は modulus 1、各 off-diagonal は modulus 1 なのでそれぞれの norm は \(\le2\)。全整数 \(n\) に対して
\[
T_j^n=\begin{pmatrix}
1&(\eta_j^n-1)/\delta_j\\0&\eta_j^n
\end{pmatrix}.
\]
幾何和から \(|\eta_j^n-1|/|\eta_j-1|\le|n|\)。固定 \(n\) で \(j\to\infty\) とすればこの比は \(|n|\) に収束する。従って
\[
|n|\le\|T^n\|\le1+|n|\qquad(n\ne0).
\]
ゆえに bounded injective dense intertwiner \(JU=TJ\) が存在しても、\(T\) は二側 power bounded ではない。これは TS1 と矛盾しない。TS1 は bounded eigenfunctionals の eigenvalue を制限し、全 operator norm を制限していない。

surjective bounded \(J:H\to X\) かつ Banach \(X\) なら事情が異なる。open mapping theorem による bounded-cost lifting と \(T^nJ=JU^n\) から一様 operator bound が出る。dense と onto を置き換えると、この lifting bound が失われる。

## TS4. Reverse map の injectivity だけでは増大を移せない

向きを逆にして \(J:X\to H\), \(JT=UJ\) とする。\(J\) が bounded injective でも
\(\|Tx\|_X\) を \(\|UJx\|_H\) から上に制御する norm 下界はない。

明示例：\(a>0\) を固定し、
\[
X=\ell^2(\mathbb Z,e^{2a|k|}),\quad H=\ell^2(\mathbb Z),
\quad (Tx)_k=x_{k-1},\quad (Uy)_k=y_{k-1}.
\]
包含 \(J:X\hookrightarrow H\) は bounded injective dense で \(JT=UJ\)。\(U\) は unitary だが
\[
\|T^n\|=e^{a|n|},\qquad \|T^ne_0\|_X=e^{a|n|}.
\]
さらに \(e^{-a}<|\lambda|<e^a\) なら
\[
\ell_\lambda(x)=\sum_{k\in\mathbb Z}\lambda^k x_k
\]
は \(X\) 上 bounded で、\(\ell_\lambda T=\lambda\ell_\lambda\)。unit circle 外の bounded characters も存在する。この functional は逆向きの包含だけでは \(H\) の bounded functional に移らない。

十分な修復は \(\|Jx\|_H\ge c\|x\|_X\) という bounded-below 条件である。そのとき \(JT^n=U^nJ\) により \(\|T^n\|\le\|J\|/c\)。mere injectivity はこの条件を含まない。

## TS5. Sz.-Nagy / Day–Dixmier similarity の正確な入力

Hilbert 空間の bounded invertible \(T\) について
\[
\sup_{n\in\mathbb Z}\|T^n\|<\infty
\quad\Longleftrightarrow\quad
T\text{ is similar to a unitary operator}.
\]
一次本文は [Sz.-Nagy, 1947, Theorem I, p.152; proof §3, pp.155–156](https://acta.bibl.u-szeged.hu/38563/1/math_011_fasc_003.pdf)。同 Theorem II は全実数の一パラメータ群版。PDF は雑誌 fascicle 全体で、p.152 は PDF index 25。OCR の \(\pm\) が落ちる箇所があるが、proof は \(T^{-n}\) による norm 下界を明示する。

入力と結論を独立に再構成する。\(M=\sup_{n\in\mathbb Z}\|T^n\|\) とすると
\(M^{-1}\|v\|\le\|T^nv\|\le M\|v\|\)。整数上の translation-invariant mean \(m\) を用いて
\[
q(v,w)=m_n\langle T^nv,T^nw\rangle
\]
と置けば \(M^{-2}\|v\|^2\le q(v,v)\le M^2\|v\|^2\)、\(q(Tv,Tw)=q(v,w)\)。対応する正可逆 bounded operator \(G\) は
\[
M^{-2}I\le G\le M^2I,\qquad T^*GT=G.
\]
\(S=G^{1/2}\) により \(STS^{-1}\) が unitary。逆向きは similarity の条件数による \(\|T^n\|\le\|S\|\|S^{-1}\|\)。したがって theorem の適用には、同じ空間・同じ norm で正負全ての powers の一様有界性が既に必要である。

amenable group への版は [Dixmier, 1950, §5 Theorem 6, pp.221–222](https://acta.bibl.u-szeged.hu/13605/1/math_012_pars_a_213-227.pdf) の一次本文を確認した。右不変 mean と strongly continuous uniformly bounded Hilbert representation が仮定。離散 \(\mathbb Z\) では連続性の追加義務はない。

[Day, *Means for the Bounded Functions and Ergodicity of the Bounded Representations of Semi-Groups*, Trans. AMS 69 (1950), 276–291](https://www.jstor.org/stable/1990358) は一次書誌を確認したが、本巡では本文の theorem 番号を照合できていない。Day の本文まで読了したとは記録しない。今回使う定理の exact statement と証明入力は上記 Sz.-Nagy と Dixmier の原文および直接証明で照合済み。

**Banach 版を Hilbert 版にすり替えない。** 二側一様有界な Banach 表現なら
\[
\|x\|_{\rm inv}=\sup_{n\in\mathbb Z}\|T^nx\|
\]
は等価な不変 norm になる。この norm が inner product から来るとは限らない。Dixmier 同 pp.221–222 はこの相違も明記する。例えば \(\ell^1\) 上の恒等表現は既に isometric だが、非反射的な \(\ell^1\) を等価 norm で Hilbert 空間にすることはできない。

## TS6. Subexponential / polynomial の取り違え

\[
T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
T^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}\quad(n\in\mathbb Z)
\]
は二側 subexponential で \(\|T^n\|=O(1+|n|)\) だが一様有界でなく、unitary と similar ではない。よって subexponential bound から Sz.-Nagy の正計量を自動的には得られない。

ただし bounded eigenfunctional について \(\ell T=\lambda\ell\) なら、二側 subexponential operator bound だけでも \(|\lambda|=1\) が従う。正 powers から \(|\lambda|\le1\)、負 powers から \(|\lambda|\ge1\)。この弱い character 結論と similarity を分ける必要がある。正 powers だけの bound では一般には片側の不等式しか出ない。

operator theory の **polynomially bounded operator** は、全多項式 \(p\) に共通の \(C\) があって
\[
\|p(T)\|\le C\sup_{|z|\le1}|p(z)|
\]
という意味である。\(p(z)=z^n\) を取れば一側 power boundedness を含む。従って \(\|T^n\|=O(n^d)\) という polynomial **power growth** と全く別。上の Jordan 例は後者を満たすが前者を満たさない。

## TS7. Unitary dilation は inverse powers を制御しない

[Sz.-Nagy, *Sur les contractions de l'espace de Hilbert*, Theorem I, p.88](https://real.mtak.hu/212287/1/math_015_087-092.pdf) を一次本文で確認した。contraction \(T\) に対し、より大きい Hilbert 空間の unitary \(U\) と圧縮 \(P\) があり
\[
T^n=P U^n|_H,\qquad (T^*)^n=P U^{-n}|_H\quad(n\ge0).
\]
**負の側は \(T^{-n}\) でなく \((T^*)^n\)**。原文末尾の受理日は 1953-06-30、標準書誌は Acta Sci. Math. 15 (1953), 87–92。archive metadata の 1954 表示とは区別する。

明示例：\(T=rI\) on \(\mathbb C\), \(0<r<1\)。\(T\) は invertible contraction だが \(\|T^{-n}\|=r^{-n}\)。円上の Poisson 確率測度
\[
d\mu_r(e^{it})=\frac{1-r^2}{|1-re^{it}|^2}\frac{dt}{2\pi}
\]
と \(U=M_z\) on \(L^2(\mu_r)\)、定数関数への圧縮を取れば、Fourier moments から
\[
P U^n|_{\mathbb C}=r^{|n|}I\quad(n\in\mathbb Z).
\]
正 powers は \(T^n\)、負 powers は \((T^*)^{|n|}\) になり、\(T^{-n}\) ではない。

さらにこの \(P:L^2(\mu_r)\to\mathbb C\) は bounded onto でも、TS1 の \(PU=TP\) を満たさない。\(f(z)=z^{-1}\) なら \(PUf=1\)、\(TPf=r^2\)。dilation の圧縮等式を global intertwining に読み替えるのが誤用の最小点である。

## TS8. Product formula / hyperbolicity は early kill

既存の一般障害を新成果として数えない。\(D=\operatorname{diag}(c,c^{-1})\), \(c>1\), は determinant 1、symplectic pairing、swap による time reversal を保つが \(\|D^n\|=c^{|n|}\)。正内積 \(G>0\) で \(D^*GD=G\) とすると第一 diagonal 成分に \(c^2G_{11}=G_{11}\) が必要になり不可能である。

product formula の \(|p|_\infty|p|_p=p\,p^{-1}=1\) は局所的な伸長・収縮を相殺する scalar 関係であり、各成分や直和の正 norm の一様有界性を与えない。局所 monodromy の実在、全零点が残る map、正 norm の control は別の入力である。

## TS9. 採用・棄却と残る具体的義務

| 候補 | 判定 | 必要な未供給入力 / 最小障害 |
|---|---|---|
| forward \(JU=TJ\) と全零点の非零 bounded pullback | 条件付き PASS | actual arithmetic \(J\) と全零点保持が未構成 |
| continuous dense range だけを各 character に使う | PASS | \(\ell_\rho\) の target topology での連続性が必要 |
| literal local profinite Haar source から全零点へ移す | 保留 / 強い fidelity 条件 | 各 multiplier が torsion であることまで要求する |
| dense bounded intertwiner から global power bound | REJECT | TS3 の純点 torsion source の exact counterexample |
| reverse injective map から global norm bound | REJECT | TS4、bounded-below 条件がない |
| 二側 uniformly bounded Hilbert 表現から正不変内積 | 既知 PASS | power bound 自体を算術から証明する必要がある |
| subexponential を unitary similarity と同一視 | REJECT | Jordan block、ただし character 実部の結論には使える |
| unitary dilation から逆時間 bound / exact intertwiner | REJECT | scalar contraction の Poisson dilation |
| product formula・dual symmetry から no-growth | REJECT | hyperbolic diagonal model |

本監査は、零点の実部を制御するだけなら full operator similarity より弱い指標別条件で足りることを確定した。他方、その条件を満たす local-to-global arithmetic map は作っていない。source の局所正性を述べ直すこと、similarity theorem の名前を付けること、dilation を追加することでは、この欠けた map と boundedness は供給されない。
