**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/phase4/notes/adelic_descent.md` · Original SHA-256: `19fe3c44441d08efa4b5c15cce8bdf51df67edd7f28f8e25909a4e51cf29368e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — adelic pairing の可閉性と positive-star の移植限界

2026-09-29。DESTROYER による限定監査。RH は OPEN。
Phase III の記録・主グラフは変更しない。新規性は主張しない。
ここで止めるのは指定された ambient Hilbert 空間からの正形式の移植であり、
算術的 cohomology／別の幾何的 polarization 全般ではない。

## 1. 判定と正確な候補

候補 AD：CCM の全零点を担う test quotient に正形式を与える際、周囲の自然な
weighted L² norm で bounded な比較を諦め、closable な非有界形式を使えばよい。

**判定：この指定 ambient norm と同じ arithmetic radical を保つ限り棄却。**
非零・非負・可閉性・ambient に稠密な null subspace は両立しない。
これは norm-continuity を仮定しない。以下の短い証明が今回の追加検査である。
正性を無条件に示したわけでも、CCM pairing が負であると示したわけでもない。

## 2. pairing と空間の指定

| 項目 | 今回固定する対象／義務 |
|---|---|
| 算術入力 | idèle class group (C_{\mathbb Q})、実際の adelic restriction |
| test domain | (E=\mathbf S(C_{\mathbb Q})^{\widehat{\mathbb Z}^{\times}})、全指数重み付き Schwartz topology |
| restriction image | (V_0=P_0V\subset E)。原点評価・積分が0の adelic Bruhat–Schwartz 関数からの像 |
| 商 | test topology における (E/\overline{V_0}^{\,E})。像が既に閉とは仮定しない |
| scalar pairing | (B(f,g)=\operatorname{Tr}\underline\vartheta_m(f\star g^\sharp)\)、第1変数線形 |
| star | (g^\sharp(u)=|u|^{-1}\overline{g(u^{-1})})。存在する involution と正性を区別 |
| ambient norm | (\|f\|_0^2=\int_{C_{\mathbb Q}}|f(u)|^2|u|d^\times u)。(H_0) は E のこの norm による completion |
| positive 根拠 | B の全 test 非負性は未供給。以下の lemma は「もし非負なら」という条件付き |
| 作用 | (T_af(u)=f(a^{-1}u))、正 modulus (a>0)、(W_a=a^{-1/2}T_a) |
| adjoint | (W_a) は ambient (H_0) で unitary。B を保存する代数式だけから quotient の Hilbert adjoint を得ない |
| 零点・重複度 | 元の nuclear-space trace は全非自明零点の自然重複度を数える。新 completion での保存は別義務 |
| trace/determinant | integrated test action の既知 trace と、新 Hilbert completion の Schatten trace／regularized determinant を同一視しない |
| 分類 | actual arithmetic の既知入力＋一般的な可閉形式 lemma。非有界化による修復への no-go |

既知入力の locator は [CCM07 v1](https://arxiv.org/html/math/0703392)
Definition 4.10、Definition 4.14、Theorem 4.16、(4.47)、(6.9)、Proposition 6.4。
特に同命題 (2)/(6.12) は、任意の f に V の元を加えて (\|f+v\|_0) を任意に小さくできるとする。
その証明は先行する Connes 論文の \(\delta=0\) 全射性を引用する。
今回はこの入力を採用し、その全射性証明を再証明したとはしない。

コンパクト単位群への平均 (P_0f(u)=\int_{\widehat{\mathbb Z}^{\times}}f(ku)dk)
には Haar 確率測度を使う。これは \(\|\cdot\|_0\) の収縮で、restriction と可換。
したがって E 上でも \(\overline{V_0}^{H_0}=H_0\)。この一つの norm の稠密性を
強い test topology での稠密性と混同しない。

## 3. dense-null-subspace lemma：非有界・可閉でも消失する

**命題 AD1.** H を Hilbert 空間、D を稠密な線形部分空間とする。
q:D×D→C は非負 Hermitian sesquilinear form とし、q[x]=q(x,x) と書く。
N⊂D は H に稠密な線形部分空間で、全 n∈N に q[n]=0 とする。
q が H に関して closable なら q≡0。
q が closed なら、さらに D=H である。

可閉性は次の条件で判定する：x_j∈D が H で0へ収束し、
q[x_j−x_k]→0 なら q[x_j]→0。
非負性による Cauchy–Schwarz から q(n,x)=0（n∈N,x∈D）。
x∈D を固定し、n_j∈N を \(\|x-n_j\|_H\to0\) となるよう取る。
y_j=x−n_j とすると

\[
 y_j\to0\text{ in }H,\qquad q[y_j-y_k]=0,\qquad q[y_j]=q[x].
\]

可閉性は q[x]=0 を強制する。x は任意だから q≡0。
その closure は全 H 上の零形式である。既に closed なら
form norm \((\|x\|_H^2+q[x])^{1/2}\) は H norm と等しく、D は稠密かつ完備なので D=H。□

**必要な限定。** q の正性と N⊂D は仮定である。
単に不定 pairing の radical が稠密という情報から「closed quadratic form」を論じない。
D を小さくして arithmetic relations N を除く案は、本命題の仮定を外すが、
元の全 test quotient を扱う修復にはならない。非負 q を含む closed extension も不可能：
その restriction は可閉であるため同じ議論を受ける。

**AD2：CCM への適用。** 原 pairing は V_0 を radical に含む。
従って、もし B が非負かつ非零なら、B は (H_0) に関して非可閉である。
特に RH を仮定して B の非負性を得ても、ambient (H_0) 上の可閉性は回復しない。
閉形式の第一表現定理を用いて (B[f]=\|A^{1/2}f\|_0^2\) と置く修復は使えない。
これは B 自身の正性を否定する結果ではなく、正性とこの completion の組合せの障害である。

## 4. Hilbert module／調和代表への写像でも同じ境界

K を Hilbert 空間、あるいは Hilbert C*-module とし、
R:D⊂H_0→K を線形写像、(R(V_0)=0) とする。
R の graph が可閉、すなわち x_j→0、Rx_j→y なら y=0 と仮定する。
任意の x∈D に対し v_j→x、v_j∈V_0 と取れば
x−v_j→0 かつ R(x−v_j)=Rx。従って Rx=0。
これは対象側の completeness と graph の可閉性だけを用いる。

よって、非零な「算術 class の調和代表」への写像 R を作り

\[
 B(f,g)=\langle Rf,Rg\rangle_K
\]

とする場合、R はこの ambient norm に関して可閉ではあり得ない。
Hilbert-module という名称はこの障害を除かない。
C*-値正形式についても、分離する各 state による scalarization が全て
H_0 可閉なら AD1 により全 scalarization が0、従って元の正形式も0となる。
module 正性だけから scalarization の可閉性は仮定しない。

この結論は実在する葉層の Hodge projection を否定しない。
そこで exact forms の閉包と調和部分が分離していることと、
ここで arithmetic V_0 が H_0 全体に稠密であることは異なる。
双方を結ぶ比較写像が同じ Hilbert topology で可閉、という追加要求が止まる。

## 5. topology を変えれば何が回避でき、何が残るか

「核型 norm」という単一の性質は指定にならない。
nuclear Fréchet topology、seminorm の族、Hilbert completion を区別する必要がある。
E の強い topology に連続な形式でも、H_0 に関して可閉とは限らない。

この区別を actual Mellin 座標で計算する。
t=log u、g(t)=e^{t/2}f(e^t) とすると

\[
 \|f\|_0^2=\|g\|_{L^2(dt)}^2,\qquad
 \widehat f(s)=\int_\mathbb R g(t)e^{(s-1/2)t}dt.
\]

k>0 に対し (H_k=L^2(\mathbb R,e^{2k|t|}dt)) を使えば、
|Re s−1/2|<k の各 Mellin 評価は連続になる。実際

\[
 |\widehat f(s)|^2\leq\|g\|_{H_k}^2
 \int_\mathbb R e^{2(\Re s-1/2)t-2k|t|}dt
 =\frac{k}{k^2-(\Re s-1/2)^2}\|g\|_{H_k}^2.
\]

有限階 Mellin derivatives も積分に |t|^{2j} を入れた同じ評価で連続となる。
k>1/2 なら通常の全非自明零点の位置を含む。
restriction 像を消す Mellin 評価をこの空間に移せば、その非零な連続 functional は
Hilbert 閉包商にも残る。従って、強い norm への変更は「全ての商が0」という障害を
実際に回避し得る。ただしこの計算だけから全 quotient の同定や重複度保存を主張しない。

代価は作用との整合である。正規化した W_{e^r} は g(t)↦g(t−r) となり、

\[
 \|W_{e^r}g\|_{H_k}\leq e^{k|r|}\|g\|_{H_k}.
\]

この作用は strongly continuous な bounded group だが、この重みでは一般に unitary
ではない。正の商 norm の存在だけで問題は終わらない。
もし零点 ρ における非零な連続 functional L_ρ が商に残れば

\[
 L_\rho(W_{e^r}f)=e^{(\rho-1/2)r}L_\rho(f).
\]

同じ商作用を unitary にする新しい norm が L_ρ の連続性を保つなら、
双対作用の等長性から |e^{(ρ−1/2)r}|=1 が必要。
強い norm は mode を保持できるが、望む unitarity を算術から導いたことにはならない。

新しい completion に最低限必要なのは次である。

- 元の arithmetic quotient からの写像と正確な kernel。余分な null directions を作らないこと。
- 全実 scaling の作用、共通 domain、正 star との compatibility。
- 全非自明零点の回収と余分な spectral modes の排除。
- multiplicity を weighted scalar evaluation と eigenspace dimension で混同しないこと。
  trace の (m_\rho|\widehat f(\rho)|^2) は m_ρ 個の独立 vector の構成ではない。
  仮に元の表現に Jordan chains があれば、unitary completion への忠実な移行はそれも説明する必要がある。
- integrated trace、全有限素点、無限素点、極0,1、determinant の正規化の一致。

これらの義務を伴わない「E/V を正内積で完成する」は修復として採用しない。

### 有限 local algebra による multiplicity gate

この小模型は、actual CCM の各 local module が次の形だと証明したものではない。
その同定を追加で主張する修復に対する synthetic／conditional gate である。

\(A=\mathbb C[\epsilon]/(\epsilon^m)\)、\(m>1\)、
\(a=\sum_{j=0}^{m-1}a_j\epsilon^j\) とする。乗算作用 M_a は三角行列であり

\[
 \operatorname{Tr}M_a=m a_0,\qquad
 \operatorname{Tr}(M_aM_b)=m a_0b_0.
\]

\(a^\sharp=\sum_j(-1)^j\overline{a_j}\epsilon^j\) は反線形 involution。
従って

\[
 B_A(a,b)=\operatorname{Tr}(M_aM_{b^\sharp})=m a_0\overline{b_0}
\]

は非負で、radical は厳密に \((\epsilon)\)。positive radical quotient は1次元に落ちる。
元の m 次元表現の trace の係数 m は、1次元空間の通常の operator trace からは
回復しない。norm を m 倍しても、1次元の恒等作用の trace は1のままである。

さらに \(\rho=1/2+i\gamma\)、\(\Theta=\rho I+M_\epsilon\) とすると
この形式的 sharp では \(\Theta^\sharp=1-\Theta\) が成立する。
しかし A 全体に正定値内積を入れて同じ等式を Hilbert adjoint として成立させることは
できない。もしできれば \(M_\epsilon\) は skew-adjoint、従って normal かつ
diagonalizable であり、nilpotent なので0となる。実際は m>1 で非零である。
零点が臨界線上という位置条件だけでも、忠実な Jordan representation の
unitary 化は得られない。これを actual 零点の単純性や CCM の欠陥の証明とは扱わない。

## 6. Deninger の positive-star はどこまで具体的か

一次資料 [Deninger–Singhof, math/0204111v1](https://arxiv.org/pdf/math/0204111v1)
§4 pp.10–14 は、閉多様体上の Kähler–Riemann 葉層について調和代表と reduced
leafwise cohomology を同定し、正内積を構成する。これは予想だけではない。
Prop.4.6 は dense leaf、葉正則 map、(f^*[\omega]=q[\omega]\) の条件下で
cohomology の正内積を (q^n) 倍する作用を得る。
今回はその内積保存式を採用し、任意 endomorphism の Hilbert completion 上での
全射性まで自動的に足さない。全実数の可逆 flow があれば、その点は別に検査できる。

一方 [Deninger 2010, §2, Conjecture 2 と pp.4–5](https://www.uni-muenster.de/IVV5MI/wwwmath/sfb878/publications/files/php7aMxKR3029.pdf)
では、数体の全零点を担う cohomology、反線形 star の正性、flow との整合は
必要な算術構造として記述される。上の葉層を Spec Z の generator と同定する定理ではない。
2024 v4 の実際の算術動力空間・層 cohomology も、この全ての正性と determinant
同定を証明したものとはされていない。固定版の locator と到達範囲は
[Phase III の限定監査](../../notes/phase3_deninger_audit.md) §3–6 に記録済み。

**twist の追加にも条件がある。**
[Álvarez López–Kordyukov の Corrigendum](https://doi.org/10.1112/S0010437X26102930)
（online 2026-04-22）の修正 Corollary C は、flat Riemannian coefficient bundle の
frame bundle に持ち上げた葉層も Riemannian であることを要求する。
trivial coefficients の Hodge 定理は影響を受けない。
「算術上必要な twist を入れても正 star が自動的に移る」という一般化は採用しない。

独立な幾何と同定が与えられた場合の計算自体は明快である。

\[
 (x,y)=\operatorname{tr}(x\cup *y)>0,\quad
 \operatorname{tr}\phi^t=e^{dt}\operatorname{tr},\quad
 \phi^t*=e^{(d-\nu)t}*\phi^t
 \quad\Longrightarrow\quad
 (\phi^tx,\phi^ty)=e^{\nu t}(x,y).
\]

共通微分 domain 上では
\((\theta x,y)+(x,\theta y)=\nu(x,y)\)。
非零固有vector は Re ρ=ν/2 を満たす。
全 spectrum を扱うには (e^{-\nu t/2}\phi^t) の強連続 unitary group への延長を別途確認する。
正 definite でない pairing や形式的な adjoint 記号だけではこの結論は出ない。

## 7. 有限体・数体の機能対応と normalization

| 機能 | 有限体曲線の既知入力 | 数体で今回残る義務 |
|---|---|---|
| cohomology | 真の曲線／Jacobian と functorial な H¹ | 既存 cyclic quotient と正幾何の比較 |
| 正性 | ample polarization による Rosati 正性 | 双対性ではなく正 star の構成 |
| 作用 | Frobenius、\(\pi^\dagger\pi=q\) | actual scaling と正 star、domain の整合 |
| trace | 全閉点・全 iterate の trace formula | 素数側の既知 nuclear trace と新 Hilbert trace の一致 |
| multiplicity | characteristic polynomial の重複度 | completion が mode／jet／trace multiplicity をどう保持するか |

有限素点の Euler 因子を替えず、無限素点を省略せず、完成関数
\(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) の極0,1を区別する。
全体 \(\xi(s)=s(s-1)\Lambda(s)/2\) と \(\Lambda\) は同じ determinant ではない。
既知の local tower \(\Theta_\infty e_n=-2ne_n\) では
\(\det_\zeta((s-\Theta_\infty)/(2\pi))=\sqrt2/\Gamma_\mathbb R(s)\)。
この定数を含む局所 Gamma 構成と、全 global H¹ の正性を取り違えない。
この段落は既存規約の保持であり、新しい接着構成ではない。

## 8. positivity の分類と停止点

| 候補 | 分類 | 判定 |
|---|---|---|
| (H_0) の norm をそのまま商へ | actual 既知命題の帰結 | 商が0 |
| 同じ (H_0) における非零 positive closable form | AD1＋actual dense radical | 不可能 |
| 同じ (H_0) からの可閉な harmonic/Hilbert-module map | graph lemma | arithmetic radical を消すなら零写像 |
| stronger test topology／別 Hilbert norm | no-go の仮定を回避可能 | 全 mode、作用、trace、重複度の比較が未供給 |
| 既存 trace pairing の全 test 正性 | 既知 Weil criterion | 新しい正性入力にはならない |
| 幾何的 leafwise positive star | 指定された幾何上の実定理 | actual ζ generator との同定を別途要する |
| full arithmetic positive-star program | 幾何・同定・正性を含む条件付き十分条件 | RH から全プログラムへの逆含意は未確認 |

限定監査はここで停止する。非有界化だけによる修復は排除できたが、
異なる topology／独立な算術偏極の不可能性は証明していない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/notes/phase3_deninger_audit.md`](../../notes/phase3_deninger_audit.md)
