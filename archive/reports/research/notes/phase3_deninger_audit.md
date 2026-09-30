**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase3_deninger_audit.md` · Original SHA-256: `3adf3f3deefb07cddea84bf3f04b9539e9eab5e1bd9032822039d846772ac6b7`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase III — Deninger の幾何・作用・偏極を分離する限定監査

2026-09-29。一次資料の指定箇所を読み、局所構成、大域構造の予想、条件付き含意を区別した。
RH の証明は得ていない。Deninger の研究を「架空の作用素だけ」とも「大域コホモロジーが
既に完成」とも扱わない。ここでは新しい算術生成子を提案しない。

## 1. 有限体との比較の出発点

滑らかな射影幾何学的連結曲線 \(C/\mathbb F_q\) では、実在する
\(H^i_{\mathrm{et}}(C_{\overline{\mathbb F}_q},\mathbb Q_\ell)\) と Frobenius により

\[
 Z_C(T)=\frac{\det(1-TF\mid H^1)}{(1-T)(1-qT)},\qquad
 \#C(\mathbb F_{q^n})=1+q^n-\operatorname{Tr}(F^n\mid H^1)
\]

となる。Frobenius の規約はこの式に現れるものを固定する。
ここで cup product の非退化交代形式と \(F\) の倍率 \(q\) だけから、
\(|\alpha|=\sqrt q\) を結論してはいけない。

曲線の Jacobian を使う証明では、幾何学的な ample polarization が Rosati involution
\(a\mapsto a^\dagger\) を与え、\(\operatorname{Tr}(aa^\dagger)>0\) と
\(\pi^\dagger\pi=q\) を供給する。これにより Frobenius の複素根の絶対値が
\(\sqrt q\) と決まる。一般の \(\ell\)-adic cup pairing を最初から正定値複素内積と
呼ぶ議論ではない。

著者一次解説で確認した locator:
[Milne, Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf),
I §14 Theorem 14.3（本文 p.62）、II §1 Lemmas 1.2–1.3（pp.76–77）。
前者は ample divisor の交点数による正性、後者は
\(\pi^\dagger\pi=q\) と \(a^\dagger a=r\Rightarrow|\iota(a)|^2=r\) の機構。
この幾何学的正性の対応物が数体側での主要な未供給構造である。

## 2. 読んだ一次資料と版

1. Deninger, *Some Analogies Between Number Theory and Dynamical Systems on Foliated
   Spaces*, ICM 1998, pp.163–186:
   [原本](https://emis.de/ft/10155)。§3、特に Proposition 3.1、Theorem 3.4、pp.168–172、
   および pp.180–181 の動力系側との区別を確認。
2. Deninger, *On the Γ-Factors of Motives II*, Documenta Math. 6 (2001), 69–97:
   [原本](https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-06/05.pdf)。
   introduction、Corollary 3.1、Proposition 4.1、§5 の deformed-complex 構成を確認。
   introduction の定理番号予告ではなく、本文の §5／Theorems 5.1–5.4 を locator とする。
3. Deninger, *The Hilbert–Polya strategy and height pairings*, 2010,
   [arXiv:1001.1621](https://arxiv.org/abs/1001.1621),
   [著者PDF](https://www.uni-muenster.de/SFB878/publications/files/php7aMxKR3029.pdf)。
   §2 Conjecture 2、PDF pp.3–5 の trace/cup/Hodge-star を確認。
4. Deninger, *Dynamical systems for arithmetic schemes*,
   [arXiv:1807.06400v4](https://arxiv.org/pdf/1807.06400v4), 2024-02-07。
   119頁の全文監査ではなく、introduction pp.1–5、Proposition 4.5、§7 の topology、
   Theorem 7.10、§10 Definition 10.1 を確認。刊行版は Indagationes Math. 37 (2026),
   25–136。以下の細部は固定 v4 を根拠とする。
5. Deninger, *There is no “Weil-”cohomology theory with real coefficients for arithmetic
   curves*, [arXiv:2204.02714v2](https://arxiv.org/html/2204.02714v2), 2023-01-27。
   §2、とくに (2.1)–(2.12)、Theorem 2.13 を確認。旧 v1 の未確認 Assumption は
   v2 の定理では除去されているため、v1 の条件付き状態を現状として引用しない。

## 3. 大域構造で何が実在し、何がまだ要求なのか

以下の connectedness／\(H^0=\mathbb R\) の主張は、\(X_0\) が integral normal かつ
\(\operatorname{Spec}\mathbb Z\) 上 flat・finite type の場合に限定する。
今回の \(X_0=\operatorname{Spec}\mathbb Z\) はこの条件を満たす。

|項目|確認できた構成・定理|RHへ必要だが今回の資料では未供給のもの|
|---|---|---|
|基礎空間|2024 v4 は rational Witt vector sheaf の ringed space \(W_{\rm rat}(X_0)\) とその points から動力系を構成|完成数体ゼータの全 divisor を担う「真の」幾何との同定|
|topology|Galois quotient topology、Frobenius を逆にする inductive limit、正有理数作用による suspension が指定される|必要な解析・偏極を伴う適切な cohomology topology|
|functoriality|Witt 構成と Frobenius 作用は実在。admissible-character 部分への制限は Prop.4.5 の stable/functorial class と dominant morphism の条件を伴う|任意の算術操作に対する望ましい functorial cohomology／dualities 全体|
|実数作用|\(\mathcal X_0=\check X_0(\mathbb C)\times_{\mathbb Q_{>0}}\mathbb R_{>0}\)、\(\phi^t[x,u]=[x,e^tu]\) が実在|その作用の \(H^1\) generator の閉定義域とゼータ零点対応|
|閉点・周期軌道|閉点は長さ \(\log N(x)\) の周期軌道の compact packet に対応|一つの素数を一つの軌道と数える Euler 積／trace への寄与の厳密な処理|
|cohomology|§10 は葉に沿って locally constant な連続関数の層による \(H^\bullet_{\mathcal F}\) を定義し、\(H^0=\mathbb R\) を得る|その \(H^1\) が求める零点実現となること、正定値偏極、所要 trace/determinant|
|無限素点|2001年には局所 Gamma の層・flow 構成がある|2024年の global suspension には fixed point がなく、局所 Gamma を含む大域完成との接続|

この表の 2024 v4 に関する要約は、空間が「expected space の approximation」であるという
原論文自身の区別を保つ。Theorem 7.10 の分解は continuous bijection であり、一般には
homeomorphism ではない。有限次元の滑らかな manifold として置き換えない。
また「コホモロジーが一切定義されていない」とは言わない。
未証明なのは上表の必要な arithmetic identification と追加構造である。

2010 Conjecture 2 の別の記述では、全算術 scheme に対する複素 Fréchet 空間
\(H^\nu\)、実数作用、純固有値スペクトル、有限な代数的重複度、正則化行列式が
一つの予想として指定される。これは 2024 年の \(H^\bullet_{\mathcal F}\) に対して
それら全条件を証明した定理ではない。

## 4. trace・duality・determinant の論理を分ける

望まれる正則化行列式表示は

\[
 \widehat\zeta_X(s)=
 \prod_{\nu=0}^{2d}
 \det_\infty\!\left(\frac{s-\theta}{2\pi}\mid H^\nu\right)^{(-1)^{\nu+1}}.
\tag{P1}
\]

この式には固有値の総和を正則化できるための収束・解析接続も必要。
記号 \(\det_\infty\) を書くだけでは存在しない。
また交代積だけなら divisor は virtual な差であり、次数間の相殺を除く説明が要る。
\(\operatorname{Spec}\mathbb Z\) では \(H^0=\mathbb C\), \(\theta=0\)、
\(H^2=\mathbb C\), \(\theta=1\) と \(H^1\) の全零点・代数的重複度の同定が望まれる。
1998 p.168 は次数間 spectrum の分離を仮定してこの読取りを行っている。

別の義務が、算術 explicit formula を空間の dynamical Lefschetz trace として導くこと。
零点をあらかじめ並べた対角作用素なら spectral side を再現できるが、
それは素数側からの functorial construction ではない。
既知のゼータ正則化積や各局所 determinant は (P1) の大域幾何を単独では構成しない。

Poincaré 型の双線形 pairing は \(\rho\leftrightarrow d-\rho\) を与える。
それ自体は \(\rho\leftrightarrow d-\overline\rho\) の positive Hermitian 制約ではない。
この違いを埋める追加の Hodge-star と正性が次節の実質的入力である。

## 5. conformal pairing の機構を独立に計算する

以下は抽象的な条件付き計算であり、actual arithmetic cohomology の構成証明ではない。
共通の invariant domain 上に cup product、trace、反線形 \(*\) があり、

\[
 \operatorname{tr}\phi^t=e^{dt}\operatorname{tr},\qquad
 \phi^t(a\cup b)=\phi^ta\cup\phi^tb,\qquad
 \phi^t*=e^{t(d-\nu)}*\phi^t,
\]

かつ \(\langle f,g\rangle=\operatorname{tr}(f\cup *g)\) が正定値とする。
内積は第1変数線形とする。すると

\[
 \langle\phi^tf,\phi^tg\rangle
 =e^{-t(d-\nu)}\operatorname{tr}\phi^t(f\cup *g)
 =e^{\nu t}\langle f,g\rangle.
\tag{P2}
\]

微分が許されれば

\[
 \langle\theta f,g\rangle+\langle f,\theta g\rangle
 =\nu\langle f,g\rangle.
\tag{P3}
\]

固有ベクトル \(0\ne f\), \(\theta f=\rho f\) に対し
\((2\Re\rho-\nu)\|f\|^2=0\)。よって \(\Re\rho=\nu/2\)。
\(\nu=1\) が数体の臨界線 \(1/2\) を与える。
正定値性がなく \(\|f\|^2=0\) を許す場合、この結論は出ない。

有限な Jordan chain も (P3) と正性により消える。
\(K=\theta-\nu/2\)、\(Kf=i\gamma f\) に対し、
\(f=(K-i\gamma)g\) なら
\(\|f\|^2=\langle (K-i\gamma)g,f\rangle=0\) となるためである。
これは代数的重複度を1にする主張ではなく、Jordan block を排除する主張。

**domain の限定:** (P3) だけで無限次元作用素の skew-adjointness を断定しない。
固有値については上の計算で十分だが、全 spectrum／Stone theorem を使うには、
\(U_t=e^{-\nu t/2}\phi^t\) が Hilbert completion 上の strongly continuous unitary
group へ延長されることを確認する必要がある。
(P2)、全実数の group law、稠密な core 上で内積ノルムの continuity があれば
その延長は得られ、そこで generator の適切な閉包について
\(\theta^*=\nu-\theta\) となる。形式的 adjoint 等式とこの結論は区別する。

## 6. Gamma の正則化 determinant は実際に計算できる

局所実無限素点の最小モデルを独立に検算する。
\(\mathcal R_\infty=\mathbb C[e^{-2y}]\)、\(\theta=d/dy\) とすると
\(\theta e^{-2ny}=-2n e^{-2ny}\)。\(\Re s>0\) で spectral zeta は

\[
 \eta_s(w)=\sum_{n\ge0}\left(\frac{s+2n}{2\pi}\right)^{-w}
 =\pi^w\zeta_H(w,s/2).
\]

Hurwitz の値 \(\zeta_H(0,a)=1/2-a\)、
\(\zeta'_H(0,a)=\log\Gamma(a)-\tfrac12\log(2\pi)\) を用いると

\[
 \det_\infty\left(\frac{s-\theta}{2\pi}\right)
 =\sqrt2\,\frac{\pi^{s/2}}{\Gamma(s/2)},\qquad
 \det_\infty^{-1}=2^{-1/2}\pi^{-s/2}\Gamma(s/2).
\tag{P4}
\]

これは Deninger 1998 Proposition 3.1 の規格化と一致する。
2010 の \(\widehat\zeta=\pi^{-s/2}\Gamma(s/2)\zeta(s)\) とは定数 \(\sqrt2\) の違いがあり、
determinant 等式ではその定数を黙って落とさない。
零点位置についての違いはない。

さらに 2001 年の仕事は、この algebraic model にとどまらず、real-analytic な
Rees bundle、deformed relative de Rham complex、higher direct image modulo torsion
による局所幾何を与えている。Corollary 3.1／Proposition 4.1 は flow と固定点 fiber の
trace を同定し、§5 が幾何的構成を供給する。
**局所 Gamma の構成は成立した成果であるが、大域 \(H^1\) の偏極や算術零点対応を
証明したものではない。**

## 7. 実係数への素朴な移行は最新版の no-go に注意

2023 v2 Theorem 2.13 は、全数体について functorial な実係数理論を複素化し、
Artin-isotypic な中心一般化固有空間の重複度が Artin \(L\)-関数の中心零点次数に
一致する、という要求を否定する。
root number \(-1\) の symplectic 表現では中心零点次数が奇数となる一方、
実表現の複素化ではその型の複素表現は偶数重複度でしか現れないことが障害。

原論文はこのため twist のない real leafwise cohomology の単純な転用では不足し、
complex／quaternionic な target を残す。
\(\zeta\) 単独に対する任意の実 Hilbert 空間、全ての複素コホモロジー、RH自体を
否定する定理ではない。旧 v1 の条件付き証明を v2 に誤って適用しない。

## 8. 含意の方向と次の検査対象

確認できる方向は

\[
 \text{独立な算術 cohomology + 全 divisor の対応 + 正定値偏極 + (P2)}
 \Longrightarrow \mathrm{RH}.
\]

RH からこの全ての functorial geometry、site、trace、cycle class、偏極が構成できるという
逆向きは確認されていない。従って Deninger の全プログラムを「単なるRH同値」とは分類しない。
一方、既知の零点を基底ラベルにして作る抽象対角空間は、全プログラムの実現とは異なる。

**Exact missing structures:**

- actual arithmetic space 上の適切な（必要なら twisted）\(H^1\) と解析的 topology/domain。
- 素数 packet と無限素点を含む functorial trace／regularized determinant の同定。
- duality に加えて、cup・trace・反線形 star が作る正定値性の幾何学的証明。
- star と flow の conformal compatibility、および必要な Hilbert completion の連続性。

有限体での Rosati positivity に対応する第三の項を、単なる双対性・有効点数・
formal trace に弱めて済ませられるかが、次の bounded synthetic test の対象となる。
本ノート自体は新しい proof attempt や全窓計算を開始しない。
