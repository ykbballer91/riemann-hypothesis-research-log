**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/spiral_scale_flow.md` · Original SHA-256: `30a2f9c64ed69b22d1f20823175aeffe9f13562116e52e326ebbf6d12cef8118`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Spiral / scale-flow / global invariant 独立探索

2026-09-29、checkpoint05。RHはOPEN。物理的主張・numerologyを前提にせず、
ユーザー指定の尺度変換・双対性・保存量・exact restrictionsを数学として検査する。
fixed-window brute-force拡大は停止したまま。

**到達点:** 自然なglobal保存形式は既に存在する。しかし不定符号を許し、
線外零点を禁止する新しい独立機構にはならない。以下は証明候補の選別記録である。
新規性、RHの証明、主証明グラフへの合流を主張しない。

## 1. 最も具体的な global object と保存則

`D=C_c∞(R)`、`F_f(z)=∫f(x)e^(izx)dx`、
`z_rho=(rho−1/2)/i` と置く。RHを仮定せず、零点を多重度込みで並べる。
臨界帯内の一様Fourier減衰と標準の零点計数から

\[
Af=(F_f(z_\rho))_\rho\in\ell^2.
\]

共役パラメータ `z_rho↔bar z_rho` を交換する自己共役unitary involutionをJとする。
Weilの零点側は正確に

\[
\mathcal Q(f,g)=\langle Af,JAg\rangle,
\qquad Q_W(f)=\mathcal Q(f,f).
\]

これはtest-space上の `A*JA` 表示であり、L²上の閉作用素の積と主張しない。
各有限supportのsmooth testへの制限は、この同じglobal sesquilinear formのexact restriction。
固定窓の閉形式は、その局所form-domainへの既知の閉拡張である。
無限構造を先に置くという方向は厳密に実行できるが、global positivityは別問題である。

さらに `T_a f(x)=f(x−a)` とすると

\[
F_{T_af}(z)=e^{iaz}F_f(z),\quad
\boxed{\mathcal Q(T_af,T_ag)=\mathcal Q(f,g).}
\]

零点側の二つの指数が相殺し、算術側でも全てが相関に依存するため成立する。
**これは実際のWeil形式に由来する無条件の保存則**である。
ところが、線外のペアでも相殺は同じである。sample空間の対角flowはJを保存しても、
正の通常normを保存するとは限らない。

`mathcal Q≥0` はWeil基準によりRH同値。`J≥0 on A(D)` を追加しても同じ義務が残る。
Jの正部分だけを「relevant subspace」と定義しても、全testの像がそこに入る証明がなければ
元の問題を取り替えてしまう。通常のglobal L²でclosed positive factorizationを要求する
候補には、既存のsampling/closability反例もある。
[構成・domain・収束](../../audits/proofs/audits/spiral-scale-reduction.md)、
[独立反証](../../audits/proofs/audits/spiral-scale-adversarial.md)。

## 2. Dilationと1/2の正確な役割

`Wf(v)=e^(v/2)f(e^v)` は `L²(R_+,dx)→L²(R,dv)` のunitary写像。

\[
(U_uf)(x)=e^{u/2}f(e^u x),\quad
WU_uW^{-1}g(v)=g(v+u),\quad
H=-i(x\partial_x+1/2),\quad U_u=e^{iuH}.
\]

Hは `W^{-1}H¹(R)` をdomainとする自己共役生成子で、`C_c∞(R_+)` がcore。
`x^(-1/2+it)` は固有値tのgeneralized eigenfunctionでありL²固有ベクトルではない。
裸のHのスペクトルは連続な実数全体で、ζの離散零点列を選ばない。
測度を `dx/x` にすれば同じ構造の係数は0になるので、1/2は指定したdxの半密度規約に対応する。

`s=1/2+alpha+it` の正規化characterは `exp(−alpha u−itu)`。
これが全実uで一定normを持つ条件はalpha=0と同値。
全ζ零点にその条件を課すだけなら、RHの表記を圧縮しただけである。
`s↦1−s` 自体の点固定集合はs=1/2のみで、critical line全体の反射固定集合は
`s↦1−bar s` の方である。

正定値保存normを持つflowの非零Hilbert modeなら増幅率は0、という一般機構は正しい。
しかしすべてのζ零点をそのmodeとして同定する未証明の段階を飛ばせない。
unitaryな散乱の複素resonanceは、自己共役生成子の実スペクトルと別物である。
[位相・可逆性の監査](../../audits/proofs/audits/spiral-scale-topology.md)。

## 3. 精密化した候補と判定

各行の主張は、反例のある一般含意と、追加仮定つきの正しい補助命題を区別する。

|ID|精密な候補|RHとの関係・検査結果|判定|
|---|---|---|---|
|SF1|全ζ零点の正規化characterが全uで有界／一定norm|alpha=0と各点で同値。恒等式を直接導出|RH再表現として棄却|
|SF2|裸の自己共役dilation Hのスペクトルがζ零点を全て実現|Hは既知の連続スペクトル。離散同定なし|不成立／Hilbert–Pólya義務が残る|
|SF3|双対な可逆flow、det・flux・Wronskianの保存がradial driftを禁止|双曲型2×2 groupが保存しながら増幅減衰する|解析・有限反例で棄却|
|SF4|正定値norm保存、または双方向contractivityが実際のmodeのdriftを禁止|一般定理として正しい。全零点のmode同定が未証明|補助原理のみ、RH入力不採用|
|SF5|global Weil objectのexact restrictionsと保存量からglobal positivity|global A*JAとtranslation invarianceは成立。Jは不定になり得る|保存則だけの強制を棄却|
|SF6|unitary scattering・保存spectral measureがresonanceを実軸へ拘束|Blaschke因子は実軸でunitaryだが非実poleを持つ|解析反例で棄却|
|SF7|exact recursion/log-periodicity/self-dualityが臨界線を強制|geometric string由来の双対積にRe s=1/3,2/3のzero列|解析・数値反例で棄却|
|SF8|fractal-string inverse spectral性から新しいRH入力を得る|Lapidus–Maierの全D≠1/2の条件は既知のRH同値|再発見として棄却|
|SF9|winding/index/critical-line phaseの保存が線外quartetを禁止|偶実多項式quartetはcritical lineで正、閉輪郭は矛盾なく4個を数える|解析・数値反例で棄却|
|SF10|prime-power phase ensembleの実周波数がzero spectrumを実にする|明示公式は既知。収束域外の正energy解釈なし、複素zeroを許す|新しい禁止機構なし|
|SF11|可逆性やentropy-like単調性だけでneutralityを得る|一方向contractiveなら減衰を許す。両方向保存と全zero対応が別途必要|独立算術構造なし|
|SF12|Q_WをHessian/energy/spectral normと呼べば非負|S(f)=Q_W(f)/2のHessian表示は自動だが凸性を含まない。正norm表示はRH同値|同値・恒等的再表現として棄却|

## 4. 数学的反例の核

**保存しても増幅する:** `diag(e^(−alpha u),e^(alpha u))` はdet=1で、
`J=[[0,1],[1,0]]` に関するenergyとsymplectic formを保存する。
正定値の保存計量という条件はここにはない。

**位相が変わらなくても線外零点がある:**
`P(z)=((z−a)²+b²)((z+a)²+b²)` の零点は `±a±ib` だが、
`P(it)=(a²+b²−t²)²+4a²t²>0`。

**自己相似と双対性を同時に満たす:** 長さ8^(-j)、多重度2^jのgeometric factorから

\[
F(s)=(1-2\,8^{-s})(1-2\,8^{-(1-s)})
=3/2-\sqrt2\cosh((s-1/2)\log8)
\]

を作る。双対・実構造・log-periodicityを持ち、zeroはRe s=1/3,2/3。
一方critical lineでは `F≥3/2−sqrt2>0`。

反例の成立はfactorization・行列恒等式・厳密不等式で証明し、数値の零包含を等号の証明としない。
これらはζのEuler積・全明示公式を共有する関数ではないので、RH反例ではない。
数値反証の対象は以上の具体的な含意であり、未定義の抽象作用素の「探索成功」を数値から主張しない。

## 5. 既知研究との対応と未解決前件

Berry–Keatingのdilation、Connesのtrace/absorption/resonance、Burnolのdilation/scattering、
Suzuki・de Branges・Kreinのcanonical systemは、この探索座標の先行研究である。
unitarity、causality、全区間可逆性、endpoint同定、RH同値条件をそれぞれ分ける。
文献の版・正確な定理と確認範囲は
[spiral-scale-prior-art.md](../../literature/literature/notes/spiral-scale-prior-art.md) に記録する。

Lapidus–Maierでは、固定Dの逆スペクトル命題はRe s=Dのζ零点の不存在と対応する。
D=1/2が特別なのは、その線には零点が存在することが既知で逆問題が失敗するため。
全D≠1/2の成功がRHに対応し、自己相似から臨界線を導く証明ではない。
原著の誤差条件と後年の強化版を混同しない。

canonical systemのWronskian・transfer determinantは通常の保存則であり、
正のHamiltonianの全域構成やζとの同定を自動的に与えない。
resolvent恒等式や散乱位相の不変量も、定義する作用素とboundary条件を先に固定する必要がある。
既存support-flow監査で未解決だった全域義務を、そのまま前提に採用しない。

## 6. 検証手続・終了理由

- BUILDER: generator/core、sample map、J-pairing、exact restrictions、保存則、global L²の限界。
- DESTROYER: synthetic quartet、有限保存flow、scattering、自己相似の反例、別担当の導出監査。
- ROOT: 固定集合・位相・argument principle・自己相似factor・prime級数の収束の再構成。
- LITERATURE: 一次研究の条件をstatement単位で照合。新規性・検索の網羅性は主張しない。

**本トラックの一般的な証明候補は終了・棄却。主証明グラフへの新規合流は0。**
成功条件A〜Dのいずれも満たさない。自然なglobal invariantと不定global objectはあるが、
線外を排除する独立の正性・mode同定・算術評価が欠けている。
対称性、純回転、保存、fractalという語への改名や有限窓計算でこの欠落を補わない。
新しい算術構造が別に提示された場合の可能性まで否定した結論ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/spiral-scale-prior-art.md`](../../literature/literature/notes/spiral-scale-prior-art.md)
- [`proofs/audits/spiral-scale-adversarial.md`](../../audits/proofs/audits/spiral-scale-adversarial.md)
- [`proofs/audits/spiral-scale-reduction.md`](../../audits/proofs/audits/spiral-scale-reduction.md)
- [`proofs/audits/spiral-scale-topology.md`](../../audits/proofs/audits/spiral-scale-topology.md)
