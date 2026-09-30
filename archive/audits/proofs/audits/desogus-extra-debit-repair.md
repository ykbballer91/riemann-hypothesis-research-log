**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/desogus-extra-debit-repair.md` · Original SHA-256: `b92d091f01850bcb7aef5436550587e90c7dba79e602ddd5e37008741d0135a5`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus: literal 2D を残した追加debitの修復条件

2026-09-29。出発状態はcommit `0763006` の未修復RL-k。
対象は [Desogus v2](https://arxiv.org/html/2609.20367v2)、Lemmas 8.1–8.2、Certificate 8.3、Lemma 8.4、Theorem 8.5、およびroot/harmonic identities。
**結論: target予算で第二のDを払うことは原理的には可能。ただし必要なactual amplitude / pivot upper boundは本文から得られず、今回の修復は未完。**
既存の二arm監査を再実行するのでなく、その係数2を受け入れた修復の最小追加条件を以下に示す。

## ED1. 同じvector上の修正された予算式

`F=H_k f`、`f=γ e_k+q`、`q⊥e_k` とする。以下では、先行するsame-form transport、parent損失の配置、domain整合が正当に成立することを**条件付きで**認める。
これら自体の未修復事項を、新しい不等式で証明済みにしない。

親の損失を支払った後の、独立に指定されたground予算は

\[
g_k=\frac12+\log k-
 \frac{439}{250\log2}\sum_mV_{k,m}-\frac52W_k.
\]

実際のdirect target diagonal `B_k=1/2+log(1/w_k)`、`w_k=log(1+1/k)` を残せば、
さらに未使用な明示量 `τ_k=−log(kw_k)>0` があり、保守的に使えるground予算は `ḡ_k=g_k+τ_k`。
`0<τ_k<w_k` は `x/(1+x)<log(1+x)<x` から従う。この微小余裕もDとの比較を自動的には与えない。
χ、Wの同じ支出をもう一度reserveとして加算しない。

foldの記号を、target振幅γとの混同を避けて

\[
c_k^{\rm F}=\gamma_k^cJ_k<1,\quad
\Theta_k(f)=\int_{R_k}x_{k,+}(f),\quad
E_k(f)=\int_{R_k}a_{k,+}|x_{k,+}(f)|^2
\]

とする。ここでは `Pi_k^phys>0` を仮定する。
正しいone-arm debitとweighted varianceは

\[
D_k[f]=\frac{1-c_k^{\rm F}}{J_k}|\Theta_k(f)|^2,
\qquad
V_k[f]=E_k(f)-\frac{|\Theta_k(f)|^2}{J_k}\ge0.
\]

最後の不等式はweighted Cauchy–Schwarz。
`Q_k=V_k+D_k` なので、literal二armをshortした残りは **`Q_k−2D_k=V_k−D_k`** である。
従って、parent支払い後の真に未使用なtransverse下界を `R_k^⊥[f]` と書ける場合、修正された十分なledgerは

\[
\boxed{q_{k+1}[H_kf]\ge
 \bar g_k|\gamma|^2+R_k^\perp[f]+V_k[f]-D_k[f].}       \tag{ED1}
\]

これは先行ledgerへの条件付き修正式であって、実Weilについて新たに証明した下界ではない。
Theorem 8.5は `R_k^⊥` に非負性・strictnessを付して導入するが、その独立した閉形式の完全な式を表示していない。
実装可能な修復では、使うtransverse formも前段のcutから指定する必要がある。

## ED2. 必要な追加不等式と、成功する具体的な十分条件

ED1だけで非負性を得る最小の追加比較は

\[
\boxed{D_k[f]\le\bar g_k|\gamma(f)|^2+R_k^\perp[f]+V_k[f]
 \quad\text{for every admissible }f.}                    \tag{ED2}
\]

strict induction用には、例えば独立な定数 `d_k<g_k`、`0≤η_k<1` で

\[
\boxed{D_k[f]\le d_k|\gamma(f)|^2
       +\eta_k R_k^\perp[f]+V_k[f]}                     \tag{ED3}
\]

を証明すればよい。するとED1から `(g_k−d_k)|γ|²+(1−η_k)R_k^⊥[f]` が残る。
ED2/3の右辺は既存の予算と明示varianceであり、`q_actual+D` を新reserveと定義したものではない。

**特に短い修復条件。** 実際に `x_(k,+)(f)=L_k f` と同定でき、`||L_k||≤1` なら、通常のL² Cauchy–Schwarzから

\[
D_k[f]\le
 \frac{|R_k|(1-c_k^{\rm F})}{J_k}\|x_{k,+}\|^2
=\Pi_k^{\rm phys}\|x_{k,+}\|^2
\le\Pi_k^{\rm phys}\|f\|^2.                            \tag{ED4}
\]

さらに先行cutから `R_k^⊥[f]≥σ_k||q||²` が独立に得られ、

\[
\boxed{0<\Pi_k^{\rm phys}<\min(g_k,\sigma_k)}           \tag{ED5}
\]

を証明できれば、第二のDはgroundとtransverseの残予算で完全に払える。
つまり係数2だけを理由に修復不可能とは結論できない。
ここで `σ_k=B_k−widehat σ_k>0` を使うには、Theorem 6.55のscalar量が実target transverse normへliftする同定も要る。

しかし、最初のtransportがunitary/block diagonalであることだけでは、全source/complement short後のfolded ground mapがED4のcontractionであるとはまだ言えない。
`Pi_phys` の正値性に加え、今回は**上界**も必要。
one-cell lower modelのpivotが小さいことを、このactual pivotの上界として使えない。
lower-form比較から得るSchur比較は下向きの下界であり、必要な上界と方向が逆である。

## ED3. 実target振幅・横成分への最小の定量化

folded momentが線形であるとき

\[
\ell_k(f):=\sqrt{(1-c_k^{\rm F})/J_k}\,\Theta_k(f),
\qquad D_k[f]=|\ell_k(f)|^2.
\]

ED2の右辺を、そこで指定されたformから `M_k[f]=ḡ_k|γ|²+R_k^⊥[f]+V_k[f]` と置く。
ED2の正確な内容は `sup_(f≠0)|ell_k(f)|²/M_k[f]≤1` である。
Mのform domain上でこのfunctionalが有界か、そしてそのdual normが1以下かを証明する必要がある。
これは不足量の明示であり、supが小さいと仮定して問題を解いたことにはしない。

より実装しやすいが強い条件として、`R_k^⊥≥σ_k||q||²`、`ell_k(f)=a_k γ+<b_k,q>` がL²で成立すると仮定する。
任意の正数d、ηについて

\[
D_k[f]\le d|\gamma|^2+\eta\sigma_k\|q\|^2\quad(\forall f)
\quad\Longleftrightarrow\quad
\boxed{\frac{|a_k|^2}{d}+\frac{\|b_k\|^2}{\eta\sigma_k}\le1.} \tag{ED6}
\]

重み付きdirect-sum normでの線形functionalのnormを計算しただけで、全mixed termも含む。
ここで必要性も含む同値は、全 `γ⊕q` 空間またはそこに稠密な許容coreについての量化を前提とする。
許容ベクトルをさらに制限するなら、表示条件は十分条件としてのみ使う。
従って、`0<η<1` と `d<g_k` を満たすED6を証明すれば、Vを一切消費せず修復できる。
固定ηで `||b_k||²<ησ_k` の場合の最小dは

\[
d_{\min}=\frac{|a_k|^2}{1-\|b_k\|^2/(\eta\sigma_k)}.
\]

実際のa、bを計算せず、parentのχやWをここへ代入する根拠はない。
それらはすでに親の損失を支払う別のsource vectorの量である。

## ED4. old gap と residual はどこに残るか

`A_k≥λ_k I>0`、actual old–new couplingを `B_(A,k)` とする。
folded momentのambient functionalがL²で `Theta(F)=<v_old,F_old>+<v_new,F_new>` と明示できる場合、harmonic identityから正確に

\[
\Theta_k(f)=\Theta_{\rm ambient}(H_kf)=\langle r_k,f\rangle,
\qquad r_k=v_{\rm new}-B_{A,k}^*A_k^{-1}v_{\rm old}.       \tag{ED7}
\]

従ってED6に必要なのは `sqrt((1−cF)/J) r_k` のground射影とtransverse射影である。
たとえば有界Bの場合の保守的評価は

\[
\|r_k\|\le\|v_{\rm new}\|
 +\frac{\|B_{A,k}\|\,\|v_{\rm old}\|}{\lambda_k}.        \tag{ED8}
\]

もしactual辞書が `v_old=0` を示せばこのold-gap費用は消えるが、それをrow equationだけから仮定してはならない。
functionalがL²で連続でない場合にはED7/8を使わず、ED3のform-dual条件へ戻る。

本文の独立に正しいroot identitiesも、必要な上界を供給しない。
`zeta=t−B_A* A^(-1)s`、`eta=delta zeta` は等式であり、`zeta` の大きさを抑えない。
例えば同じvectorに対するCauchy–Schwarzで得るのは

\[
\sqrt{2\delta_k}|\langle\zeta_k,f\rangle|
\le\sqrt{2\delta_k}|\langle t_k,f\rangle|
 +\sqrt{1-\delta_k}\,\|A_k^{-1/2}B_{A,k}f\|.
\]

ここに残るold response energyも無料のreserveではない。
また、このtrue polar residualとfolded debitのfunctionalを同一視するには別の辞書が必要である。

## ED5. 本文から得られたもの、得られなかったもの、量化

- Lemma 8.1はstationary rowと同じmetricでのsurplus分解を与えるが、responseのtarget振幅に対する上界ではない。
- Lemma 8.2はそのsurplusを3/5と2/5に分け、mixedとaligned forcingに使用する。残った任意のresponseに使える同量の正予算は宣言できない。
- Certificate 8.3はg_kのscalar正値性を扱い、`Theta_k(f)`、`Pi_phys`、old gap、ED6のa/bを含まない。
- `g=A_pre x`、`h=A_cut x_+`、`eta=delta zeta` からはED2–ED6は出ない。必要なactual amplitude / pivot upper boundの式は該当箇所に見つからなかった。

固定したkで、actual kernelからED4/5またはED6を証明できれば、それは検証可能な追加の算術評価になり得る。
一方 **全k** でED3を、base・正pivot・先行ledgerとともに仮定すれば、inductionとcofinalityを通じてRHを供給する。
それを無条件の新入力として採用しない。
この特定のlower budgetに対するED2/3がRHから逆に従うことは未証明であり、RH同値とは判定しない。

区別すべき既存のexact条件は
`(2/delta_k)|<eta_k,f>|²≤<f,S_k f>`（全f）で、これは単に `T_k≥0` の書換え。
このactual positivityを全endpointで要求する非負版は、圧縮とrestricted Weil criterionによりRHの内容へ戻る。
この書換えを新しい制御原理と呼ばない。

**停止判定:** 第二のDを払う最小の不足は、実際のfolded ground responseを実target amplitudeと既存transverse予算で抑えるED2/3、またはそれを具体化するED4/5・ED6である。
現状の原文からその独立証明は得られず、未修復。新規固定窓certificateやscalar再走査は行っていない。

## ED6. Contraction候補の本文照合と既知の作用素定理

literal old/new splitでは `P_new(U_old⊕U_new)H_k f=U_new f` なので新成分のnormは保存される。
しかし `||H_k f||²=||f||²+||A_k^(-1)B_(A,k)f||²` で、harmonic graph全体はcontractionではない。
Lemma 8.4はx_+をresulting folded ground componentと呼ぶが、これが新成分の直交射影であること、
射影・metric・a_+・βの実kernel辞書は未指定。従ってED4の仮定を本文のunitarityだけから採用できない。
この限定照合を終え、同じmissing dictionaryを周回する修復探索は停止する。

[Douglas (1966), Theorem 1](https://galaxy.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf)
によれば有界作用素の場合、`B B*≤c A` と `B=A^(1/2)D, ||D||²≤c` は同値である。
各pivotにおける値域包含だけでなく、使える予算以下のcを独立に示す必要がある。
[Griesemer–Hasler (2008), §2, conditions (b)–(c), Theorem 1](https://pnp.mathematik.uni-stuttgart.de/iadm/Griesemer/GriHas.pdf)
も消去側の有界逆・応答の有界性を前提とし、thresholdに向かう一様評価を自動供給しない。
これらは既知の正確な定理であり、ζ固有の新入力には数えない。

ED1–ED8の代数は別担当が独立確認。実作用素へのliftはNOのまま。

## ED7. Polar-free core の全窓正値性を弱い前提にはできない

実奇compact smooth core上で `A_a=C_a−2|s_ph><s_ph|`、`s_ph(y)=sinh(y/2)` とする。
このとき **全aについてC_a≥0 ⇔ RH**。単一窓の命題ではない。
RH⇒A_a≥0⇒C_a≥0はWeil基準から従う。逆向きでは線外零点λ₀を仮定し、
[Gate III §1](desogus-gate3.md)の分離testのLaplace transformを

\[
F_M(z)=z(z^2-1/4)P_T(z)R_M(z)\Psi(z)^M
\]

とする。λ₀≠±1/2なのでR_Mを再正規化でき、target quartetの負寄与を維持する。
追加次数2は固定のため、同じ高零点tailの抑制も保つ。一方F_M(±1/2)=0より
`<s_ph,f_M>=0`、従って十分大きなMでは `C_a[f_M]=A_a[f_M]=W[f_M]<0`。
これは既存criterionの直接拡張で、ROOTとDESTROYERが独立確認した。

既知の有限消失条件付きWeil criterionは
[Connes–Consani, arXiv:2006.13771v1, Appendix C, Proposition C.1, p.51, (155)](https://arxiv.org/pdf/2006.13771v1)。
同命題はMellin transformの零点を、非自明零点と交わらず0,1を含む有限集合に指定する。
実奇制約も同時に保持できる部分は上記分離構成で確認した。新規性は主張しない。
任意のfinite-rank補正へ一般化せず、通常global L²上の有界性・閉形式も主張しない。
「まず全窓C≥0を既知の正性から得る」という独立入力のない迂回はRH同値として棄却する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/desogus-gate3.md`](desogus-gate3.md)
