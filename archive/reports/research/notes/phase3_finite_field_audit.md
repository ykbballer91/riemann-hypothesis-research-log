**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase3_finite_field_audit.md` · Original SHA-256: `8e3f7cca88485cfad511c99bed17f3aee194d2ea873e9202ac8fca0cb6dc2007`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase III — 有限体 RH の依存関係監査

日付: 2026-09-29。担当: BUILDER。既知定理の構造抽出であり、新規性・数体 RH の証明を主張しない。曲線の Rosati 証明と Deligne の一般次元の証明を区別する。以下の「独立性」は各入力が他の記載入力から自動的には得られない、または当該証明がどの既知結果を別入力として使うかという意味であり、公理論的独立性の主張ではない。

## 1. 規約と結論の位置


有限体を \(\mathbf F_q\)、\(\ell\ne\operatorname{char}\mathbf F_q\)、\(X=X_0\times\overline{\mathbf F}_q\) とする。\(F^*\) は \(q\)-乗 Frobenius **射の pullback** とする。これは étale cohomology 上では算術 Galois Frobenius の逆に対応する（Deligne [D], §1.15）。Tate module の Frobenius 射と、その pullback の特性多項式は同じである。射、Galois 作用、dual vector space の三つの意味の「Frobenius」を混同しない。

有限次元性と Grothendieck–Lefschetz により

\[
N_r=\#X_0(\mathbf F_{q^r})
=\sum_i(-1)^i\operatorname{Tr}(F^{*r}\mid H_c^i(X,\mathbf Q_\ell)),\qquad
Z(X_0,T)=\prod_i\det(1-TF^*\mid H_c^i)^{(-1)^{i+1}}. \tag{1}
\]

これは点の Euler 積とスペクトルを**同じ算術対象の上で**結ぶ。式 (1) だけから各固有値の絶対値は得られない。[G, Thm 5.1] が一般の constructible sheaf の determinant formula、[D, (1.5.1), (1.5.4), (1.14.3)] が本監査の規約を直接与える。[G] の当時の基礎付けに関する留保を現在の未証明条件と扱わず、[D, §2.14] が示す SGA 4/5 の基礎定理を既知入力とする。

滑らかな射影 \(X_0\) の目標は

\[
\forall i\ \forall\alpha\in\operatorname{Spec}(F^*|H^i)
\ \forall\iota:\mathbf Q(\alpha)\hookrightarrow\mathbf C,
\qquad |\iota(\alpha)|=q^{i/2}. \tag{2}
\]

[D, Thm 1.6] は smooth **projective** と明記される。一般の smooth proper への拡張は §5 で別に説明する。Poincaré duality は \(\alpha\leftrightarrow q^d/\alpha\) を与えるが、複素共役 \(\bar\alpha\) との一致や正定値性を単独では与えない。

## 2. 曲線: 同じ Jacobian 上の偏極・Frobenius・正値性

\(C_0/\mathbf F_q\) を滑らかな射影幾何学的連結曲線、\(J=\operatorname{Jac}(C_0)\) とする。\(H^1(C)\simeq H^1(J)\) は Frobenius と可換であり、

\[
Z(C_0,T)=\frac{\det(1-TF^*|H^1(C))}{(1-T)(1-qT)}.
\]

\(\mathbf F_q\) 上の偏極 \(\lambda:J\to J^\vee\) から
\(x^\dagger=\lambda^{-1}x^\vee\lambda\) を定める。幾何学から来る入力を分離すると次の二つである。

* **正値性:** \(D=\operatorname{End}_{\mathbf F_q}^0(J)\) 上の Rosati trace pairing は正定値。適切な通常の trace \(\tau\) に対して \(\tau(xx^\dagger)>0\) for \(x\ne0\)。
* **算術随伴恒等式:** \(\pi^\dagger\pi=\pi\pi^\dagger=q\cdot1\)。ここで \(\pi\) はこの \(J\) の \(q\)-Frobenius 射。

前者は ample polarization の正値性の定理であり、「\(\dagger\) は adjoint という名前だから正」という定義ではない。後者は Frobenius–Verschiebung の \(FV=VF=[q]\)、dual Frobenius と Verschiebung の関係、\(\lambda\) が \(\mathbf F_q\) 上で定義されることから得る。具体的に \(\pi_{J^\vee}\lambda=\lambda\pi\) と \(\pi^\vee\pi_{J^\vee}=[q]\) を代入すればよい。[O, Props 3.3–3.4, §3.5] はこの分離を明示する。Prop 3.4 は simple の場合を述べるが、この Frobenius–Verschiebung 計算は任意の polarized abelian variety に適用できる。

ここから先は次の有限次元線形代数で足りる。\(D_\mathbf R=D\otimes\mathbf R\) に

\[
(x,y)=\tau(xy^\dagger)
\]

を入れる。trace の循環性から左乗法 \(L_\pi\) の随伴は \(L_{\pi^\dagger}\)。従って

\[
L_\pi^*L_\pi=qI,\qquad \|L_\pi x\|^2=q\|x\|^2. \tag{3}
\]

複素化後の固有ベクトル \(v\ne0\) について \(|\alpha|^2\|v\|^2=q\|v\|^2\) なので \(|\alpha|=\sqrt q\)。左正則表現は忠実であり、\(p(L_\pi)=0\iff p(\pi)=0\)（逆方向は \(1\in D\) に作用させる）。Tate module 上の endomorphism 作用も忠実なので、その最小多項式は同じである。このため (3) の制約は点数を与える \(H^1\) の全固有値・全複素共役に届く。Tate module の忠実性と整数係数特性多項式は [K, Thm 6.0.4, Cor 6.0.5] も参照。

### 2.1 弱められる条件と弱められない条件

この最終線形代数には全 endomorphism algebra の正値性よりも、\(\pi,\pi^\dagger\) を含む忠実な有限次元表現上の正定値内積と (3) だけで足りる。しかし、その内積を固有値を知った後で選ぶことは算術入力を構築したことにならない。半正定値なら nullspace に隠れた固有値を排除できないので、零点を担う商への忠実性も必要である。

数体への最重要の輸送対象は「ある正の空間」の存在ではなく、**素数側と零点側を忠実に同定した同じ空間上で、算術作用と正の adjoint が両立すること**である。

### 2.2 双対性・随伴スケーリングだけの検査模型

\[
F=\begin{pmatrix}0&-9\\1&7\end{pmatrix},\quad
H=\begin{pmatrix}2&7\\7&18\end{pmatrix}
\quad\Longrightarrow\quad F^{\mathsf T}HF=9H,
\qquad \det H=-13.
\]

このとき \(\alpha_\pm=(7\pm\sqrt{13})/2\)、\(\alpha_+\alpha_-=9\) だが \(|\alpha_\pm|\ne3\)。\(H\)-adjoint について \(F^\dagger F=9I\) は正確に成り立つ。失われているのは \(H>0\) である。正定値 \(H_+\) が同じ恒等式を満たすなら、実固有ベクトルに評価して直ちに矛盾する。

これは有限行列・形式的 zeta データの模型である。実在する曲線、Jacobian、有限型スキーム、étale cohomology を構成した例ではない。別途点数候補や Euler 積係数の非負整数性を検証しても、それらが実際の幾何学的 realization を供給することにはならない。

## 3. 一般次元: Deligne の実際の purity 機構

一般次元の [D] を「正の偏極があるので全固有値が円上」と要約するのは不正確である。原論文の骨格は

\[
\text{Lefschetz pencil / vanishing cycles}
\Rightarrow\text{大きい symplectic monodromy + 局所有理性}
\Rightarrow\text{偶数 tensor の係数非負性 + 極の位置}
\Rightarrow\text{purity}
\]

であり、さらに \(X^k\) を用いて残った定数誤差を消す。

### 3.1 基本評価の算術的正値性を再導出

\(U_0\subset\mathbf P^1_{\mathbf F_q}\) と lisse sheaf \(\mathcal F_0\) について [D, Thm 3.2] の入力を置く。

\[
\mathcal F_0\otimes\mathcal F_0\longrightarrow\mathbf Q_\ell(-\beta)
\text{ は非退化 alternating},\qquad
\rho(\pi_1(U))\text{ は Sp の }\ell\text{-adic 開部分群}, \tag{4}
\]

かつ全閉点 \(x\) の局所特性多項式が \(\mathbf Q[T]\) に属する。閉点の次数を \(d_x\)、\(q_x=q^{d_x}\) とする。任意の \(k\ge1\) について

\[
\operatorname{Tr}(F_x^r|\mathcal F^{\otimes2k})
=\bigl(\operatorname{Tr}(F_x^r|\mathcal F)\bigr)^{2k}\ge0. \tag{5}
\]

有理性がここで実数としての符号を確保する。局所 Euler 因子の logarithm は

\[
\log L_{x,k}(T)=\sum_{r\ge1}
\frac{\bigl(\operatorname{Tr}(F_x^r|\mathcal F)\bigr)^{2k}}rT^{rd_x},
\]

したがって \(L_{x,k}\) 自体も非負係数で、定数項は 1。Euler 積 \(L_k=\prod_xL_{x,k}\) の係数は各因子の係数以上だから、各局所収束半径は全体の収束半径以上である。これは Hilbert 空間の正値性を仮定する箇所ではなく、**同じ局所算術 trace の偶数冪**から得られる正値性である。

一方、symplectic invariant theory と \(H_c^2\) の coinvariant 記述により

\[
H_c^2(U,\mathcal F^{\otimes2k})\simeq
\mathbf Q_\ell(-k\beta-1)^{N_k},\qquad H_c^0=0,
\]

なので trace formula は

\[
L_k(T)=\frac{\det(1-TF^*|H_c^1(U,\mathcal F^{\otimes2k}))}
{(1-q^{k\beta+1}T)^{N_k}}. \tag{6}
\]

を与える。分子による cancellation はあり得るが、\(|T|<q^{-k\beta-1}\) の新たな極は生じないので必要な下界には支障がない。局所固有値 \(\alpha\) は \(\mathcal F^{\otimes2k}\) に \(\alpha^{2k}\) を与え、その局所逆 determinant の極の絶対値は \(|\alpha|^{-2k/d_x}\)。従って

\[
q^{-k\beta-1}\le |\alpha|^{-2k/d_x}
\quad\Rightarrow\quad
|\alpha|\le q_x^{\beta/2+1/(2k)}.
\]

\(k\to\infty\) と (4) の双対 \(q_x^\beta/\alpha\) により \(|\alpha|=q_x^{\beta/2}\)。これが [D, Lemmas 3.3–3.6, §3.7] の Rankin 型 tensor amplification の核である。ここでは大きい monodromy の役割は (6) の**極の予算**を制限することであり、任意の正の Euler 積だけでは代用できない。

この証明段階で開部分群条件は、「全ての \(2k\) について tensor coinvariants が必要な Tate 型である」という条件まで弱められる。局所有理性も、選んだ複素実現で (5) の実数性・非負性を直接供給する条件に弱められる。ただし全複素共役の結論には各共役について対応する条件が要る。単に係数が複素代数的というだけでは (5) は不成立である。

### 3.2 この入力が幾何学から出る箇所

Lefschetz pencil の vanishing-cycle 空間 \(E\) から radical を除いた
\(E/(E\cap E^\perp)\) を使う。odd fibre dimension では非退化 alternating pairing を持つ。Picard–Lefschetz transvection と既約性が大きい monodromy を与えるのが [D, §§5.7–5.11, Thm 5.10]。局所特性多項式の有理性を供給するのが [D, Thm 6.2]。後者を全次数の purity から既に得た事実として先取りしてはいけない。

弱 Lefschetz、Poincaré duality、Leray、vanishing-cycle の分解、上の基本評価を用い、[D, Lemma 7.1] は even dimension \(d\) の middle cohomology に

\[
q^{d/2-1/2}\le|\alpha|\le q^{d/2+1/2} \tag{7}
\]

を得る。任意の \(X\) の middle eigenvalue \(\alpha\) に対し、Künneth により \(\alpha^k\) が \(H^{kd}(X^k)\) に現れる。even \(k\) で (7) を適用して \(k\) 乗根を取ると誤差は \(1/(2k)\)。これが [D, §7.3] の二度目の amplification である。他の次数は弱 Lefschetz と duality によって処理する。

**非入力:** hard Lefschetz をこの証明の既知入力に数えない。[D, §7.1, 印刷 p.300] はその時点でまだ hard Lefschetz を証明していないための分解を行っている。standard conjectures、全次数の Hodge 型 positivity、全 étale cohomology 上の正定値 Rosati 内積を前提にもしていない。交代 cup pairing は実 Hilbert 内積ではない。

## 4. 抽出した入力一覧と数体側の状態

`EXACT` は同じ主張・役割が実際に存在、`PARTIAL` は一部の算術・解析対応だけ存在、`CONJECTURAL` は対応構想はあるが必要な同定が未証明、`ABSENT` はこの研究で必要対象・機構が与えられていない、を意味する。`ABSENT` は存在不可能という定理ではない。表の数体欄は **ζ_Q の global zeros の実現**について判定する。別の既知 motive の局所 Frobenius の純性を転用した判定ではない。

| ID | 入力・役割 | 弱化可能性 | 独立性・出典 | 数体側 |
|---|---|---|---|---|
| FF-A | 有限次元 \(H_c^i\) と算術 Frobenius が同じ \(X\) から生じる | 最終線形代数には忠実な必要部分だけでよい | 対称多項式からは幾何学を作れない。[D §§1.3–1.5] | **ABSENT**: 同様の有限次元対象。global zeros の無限集合には異なる枠組みが必要 |
| FF-T | 点の Euler 積 = trace = determinant、式 (1) | 適切な trace identity と全 spectrum の忠実性で代替可能 | 正値性を含まない。[G Thm 5.1; D (1.5.4)] | **PARTIAL**: 明示公式はあるが正の Hilbert trace realization は未証明 |
| FF-D | duality と Tate twist による reciprocal pairing | 対象固有値の reciprocal closure で足りる | 複素共役・正値性とは別。[D §2.3] | **PARTIAL**: ξ の関数等式は exact、正の adjoint までは与えない |
| C-R | \(H^1(C)=H^1(J)\) と忠実な endomorphism/Tate realization | 全 algebra でなく Frobenius 生成部分でもよい | スペクトル模型の命名では代替不可。[O §3; K 6.0.4] | **ABSENT**: primes と global zeros を担う共通 Jacobian 型対象 |
| C-P | Rosati trace の正定値性 | 忠実な作用空間の正定値性まで弱化可 | ample polarization からの幾何定理。[O 3.3] | **CONJECTURAL**: 必要な算術 realization と両立する正値性 |
| C-F | 同じ polarization で \(\pi^\dagger\pi=q\) | 同じ表現上の scaled isometry で足りる | Frobenius–Verschiebung と base-field compatibility。[O 3.4] | **ABSENT**: 数体零点の作用に対する算術由来の対応恒等式 |
| D-L | pencil、弱 Lefschetz、Leray、vanishing cycles による還元 | 対象に適した幾何的還元でもよい | hard Lefschetz や purity の仮定ではない。[D §§5,7.1] | **ABSENT**: ζ_Q に対する該当 family と vanishing cycles |
| D-M | 大きい monodromy が tensor coinvariants を Tate 型に固定 | 必要な tensor invariants と極の bound だけでよい | 開 Sp は transvection から証明。[D 5.10, 3.7] | **ABSENT**: 同じ算術対象の全 tensor 極の支配 |
| D-Q | 全局所特性多項式の有理性 | 全共役で必要 trace が実ならよい | purity の結論から前借りしない。[D 6.2] | **PARTIAL**: 個々の有理 Euler 因子はあるが対象 family がない |
| D-E | 偶数 tensor の trace 非負性と係数 domination | 必要な全偶数冪での domination | D-Q と tensor identity から導出、単独の追加仮説ではない。[D 3.3–3.6] | **PARTIAL**: 元の Euler 積の係数非負性だけでは (6) を供給しない |
| D-B | \(H_c^2\) coinvariants により (6) の極が制限される | \(k\beta+O(1)\) 型の十分強い極 bound でもよい | D-M、trace、curve duality に依存。[D 2.10, 3.7] | **ABSENT**: 高い tensor でも損失が有界な極の評価 |
| D-K | \(X^k\) と Künneth で \(\alpha^k\) を実現 | 同じ次数増幅を保つ functor でもよい | (7) が全積対象で使えることが必要。[D 7.3] | **ABSENT**: 誤差を消せる算術 realization の閉じた積体系 |

表は必要十分の唯一の公理系ではない。曲線の C 系列と一般次元の D 系列は別証明経路であり、全てを一度に仮定する必要はない。C-P と C-F を同じ対象で実現することと、D-M/D-B の tensor 極支配を得ることは、同じ名前の「positivity」で一括できない。

Phase III統合時の対応補足：上表のABSENTは、有限体のpolarized realizationと同じ役割を
全て満たす対象についてである。CCMのcyclic quotientには実在する算術的全零点traceがある。
またC-Fの形式的類似 H(T_af,T_ag)=aH(f,g) もその算術形式で無条件に成立する。
不足するのは、それを正のHilbert adjointの恒等式として使える独立なpolarization。
従って「算術cohomologyも相似則も一切ない」とは読まない。統合した最新のstatusは
`../finite_field_dependency_spine.md` のFF1–FF6と `../number_field_gap_matrix.md` を優先する。

## 5. smooth proper の範囲と 1974 年の証明範囲

smooth proper \(X_0/\mathbf F_q\) の幾何学的連結成分を扱う。de Jong [A, Thm 4.1, Remark 4.2] により smooth projective \(Y_0\) から generically finite proper alteration \(f:Y_0\to X_0\) を取れる（必要なら有限体を有限拡大する）。proper な \(X_0\) の場合、alteration source は proper であるから、同定理の projective compactification 内で既に閉かつ開となり、projective に取れる。有限体は perfect なので regular source は smooth である。

同じ次元の smooth proper 間で Poincaré duality による pushforward と projection formula から

\[
f_*f^*=(\deg f)I
\]

が成り立つ。\(\mathbf Q_\ell\) では \(\deg f\ne0\) は可逆なので、\(H^i(X)\) は \(H^i(Y)\) の Frobenius-stable direct summand。従って (2) が移る。基礎体を \(\mathbf F_{q^r}\) に拡大した場合も \(|\alpha^r|=(q^r)^{i/2}\) から元の結論を得る。これは既知の **後年の拡張経路**であり、de Jong の1996年の定理を Deligne1974年の入力へ遡及させない。

追加入力 `P-A`: smooth projective alteration と degree push–pull。役割は projective→proper、弱化は同次数での Frobenius-equivariant injection で十分、独立性は alteration という別幾何定理、数体 global-zero analogue は **ABSENT**。singular / nonproper 全般について各 \(H_c^i\) が純 weight \(i\) だとは主張しない。

## 6. 数体移植で最初に欠けるもの

\(\zeta_{\mathbf Q}(s)=\prod_p(1-p^{-s})^{-1}\) は \(h^0(\operatorname{Spec}\mathbf Q)\) の weight-zero trivial motive の global \(L\)-function として扱える。各 unramified local Frobenius は \(1\) に作用する。この局所実現と weight-zero purity は **EXACT**。しかし ζ の非自明な **global zeros** はその一次元局所作用の固有値ではない。「各素数の局所 purity は既知」から global RH は従わない。

有限体の曲線では、global zeta の分子を担う実際の \(H^1\) があり、\(q\) の冪による全点数が一つの Frobenius の反復 trace である。\(\operatorname{Spec}\mathbf Z\) の次元が1という観察は、その \(H^1\)、正の偏極、全素数を同じ作用の反復として扱う構造を作らない。全素数の \(\log p\) を単一の固定 \(\log q\) の整数倍として置換することもできない。

したがって次の不足を分離しておく。

1. **算術的実現:** 全素数・Archimedean 項・極と、全非自明零点の重複度を同じ trace/determinant に忠実に実現する対象と作用。
2. **正の構造との両立:** その同じ対象の算術作用に対する正定値 adjoint と、中心 weight を強制する scaling/duality 恒等式。
3. **無限次元の解析:** determinant の正則化、operator/form domain、nullspace、閉包、trace identity のテスト空間を失わずにつなぐこと。

零点から対角自己共役作用素を作る案は、off-line 零点を最初から捨てるか、実スペクトルの同定で RH を仮定していないかを監査する必要がある。Weil positivity や全面的 Herglotz 性を不足2の無条件な「入力」と呼び換えることもしない。本ノートはこの三点のいずれも数体に対して構築していない。

この整理は既存の非 Hilbert な算術商・distribution trace realization が存在しないという主張ではない。Connes–Consani–Marcolli の actual zero quotient を選ぶ比較は別ノートの担当範囲であり、そこで既に得られる arithmetic trace は保持して不足を縮小すべきである。特定の quotient 上の positivity criterion が RH 同値であることと、Deninger 型の幾何学・functoriality・domain まで含む全構想が RH と同値であることも区別する。後者の逆含意は本監査からは得られない。

**判定:** 有限体から採用するのは、算術 trace realization と正値性を同じ対象で結ぶ必要、および Deligne の具体的 tensor/pole 機構の区別である。新しい RH 入力は0。次の限定候補を選ぶなら、単独の一般正値性よりも、素数に由来する共通の polarized arithmetic realization の具体的定義が先である。

## 7. 出典と確認範囲

* **[D] 一次原論文:** P. Deligne, *La conjecture de Weil I*, Publ. Math. IHÉS **43** (1974), 273–307, [Numdam 本文](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf), [DOI](https://doi.org/10.1007/BF02684373)。重点確認: §§1–3, 5–7、特に Thm 3.2, Lemmas 3.3–3.6, §3.7, Thms 5.10/6.2, Lemma 7.1, §7.3。数式 OCR に加え印刷284–285頁をローカル PDF rendering で画像確認。取得 PDF SHA256: `8392b345d4854e6dc55fb42cfc0b616d941935983723627237239a87348f42e5`。一時取得先 `[local machine path omitted]` は恒久的 source-cache ではない。
* **[G] 一次原報告:** A. Grothendieck, *Formule de Lefschetz et rationalité des fonctions L*, Séminaire Bourbaki, exp.279（講演1964年12月、刊行1966）, 41–55, [本文](https://www.numdam.org/item/SB_1964-1966__9__41_0.pdf), Thm 5.1、§§3–6。[D §2.14] の SGA 4/5 基礎付けと合わせて読む。
* **[O] 著者による専門講義章:** F. Oort, *Abelian varieties over finite fields*, [本文](https://math.nyu.edu/~tschinke/books/finite-fields/final/05_oort.pdf), §3, Props 3.3–3.4。Rosati positivity の幾何学的定理を本監査で再証明したのではなく、そこで明示された既知入力として採用。
* **[K] 著者講義:** K. S. Kedlaya, *RH for abelian varieties*, [Chapter 6](https://kskedlaya.org/weil-cohom/chapter-6.html), Thm 6.0.4, Cor 6.0.5。上記の曲線線形代数と忠実性の照合用。
* **[A] 一次原論文:** A. J. de Jong, *Smoothness, semi-stability and alterations*, Publ. Math. IHÉS **83** (1996), 51–93, [本文](https://www.numdam.org/item/PMIHES_1996__83__51_0.pdf), Thm 4.1, Remark 4.2。

ここでの監査は依存関係・規約・該当証明機構の確認であり、SGA 全巻、Rosati positivity の元証明、Deligne の全補題、alterations 全証明を新たに形式検証したという意味ではない。
