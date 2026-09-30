**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic_reduction_candidates.md` · Original SHA-256: `ed66d8cfeccd3519a7a24e49e5e9c85d9cc625bff89fcddd332e66827b00d827`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Dyadic reduction：候補比較と終了判定

2026-09-30。固定 E/W、T_2、p_N、q_N。RH OPEN。
探索の単位は以下の 3 major mechanisms。結果の出なかったものを新名称で再開しない。

| ID | 算術的入力と exact identity | 成立する範囲 | 定量的帰結 | 判定 |
|---|---|---|---|---|
| D1 | diagonal Q^times の reindexing、2-adic 格子、odd/even split | 実際の summation range 内 | local Haar 正規化は保持。ただし一般 class の評価なし | 一般 reduction として終了 |
| D2 | Poisson、Fourier と inversion、固定 dyadic interval | Poisson は pole-free range で exact | compact representatives の変更は W∩Cc∞={0} により不可 | exact compact folding は反証 |
| D3 | 全整数 Möbius inverse、cutoff、mean correction | **全 g∈E**、actual w_n∈V⊂W | p_1(R_n)<=C 2^{n/2}(1+n)p_4(g) | explicit construction と Level 3 を保存。準指数 endpoint は RH 同値として終了 |

## D1 — Rational / 2-adic / telescoping

Candidate: diagonal rational multiplication を使い dyadic shift を恒等関係へ落とす。
Arithmetic source: Q^times にわたる summation、全 places の product formula。
Exact identity: Sigma R_{2^n,diagonal} eta=Sigma eta。
Obstruction: T_2^n は real-only idele の半密度作用。diagonal 作用と違い、有限側へ移すと
2^{-n}Z_2 の格子と 2^{-n/2} が残る。

Odd shell identity は Theta_f(x/2^n)=Theta_f(x)+sum_{j=1}^n O_f(x/2^j)。
同じ pole-free f の場合に各項は range にあり、商では零を別の零で表現している。
任意 g に拡張した (I-2^{-1/2}T_2^{-1})g∈W は
ell_rho にかけると (1-2^{-rho})ell_rho(g) となり、一般には非零なので偽。

無限 odd 展開の残差 2^{-J/2}phi_f(t+Jlog2) は pointwise と bare L² では消えるが、
非零 phi_f なら p_N は少なくとも 2^{(N-1/2)J}poly(J) で増える。
これを E/W 上の発散とは言わない。各残差自体は W なので商では 0。

Decision: 有限の exact dictionary を保存。全商に対する fold としては不採用。
2-adic wavelet / martingale の名称を付けても、同じ range 内計算だけなら新候補にしない。
有限 filter を P(T_2)E⊂W に強めると、下記 D2 の compact test が直ちに反証する。

## D2 — Poisson inversion / compact fundamental region

Candidate: positive translate を Fourier/inversion で negative translate に交換し、
代表元を [0,log2) または固定 compact interval に戻す。
Exact identity: phi_f(t)=phi_Ff(-t)、J_ref T^n=T^{-n}J_ref。
Obstruction: reflection 自体は商上の恒等作用でも norm contraction でもない。

Stronger no-go: W∩Cc∞(R)={0}。proof は全零点 jets、Jensen、無条件 Riemann–von
Mangoldt。従って compact g,h に g-h∈W なら g=h。遠方 compact bump を別の compact
interval へ exact に折ることはできない。台の幅が log2 より小さい bump はさらに、
全 E を W に送る非零 Laurent polynomial P(T_2) の不存在を示す。

Decision: compact exact folding は終了。noncompact tail / approximate representative は
反証の対象外なので、D3 をこの no-go で捨てない。

## D3 — Möbius inverse / cutoff / canonical pole conditions

Candidate: 右側の算術和を完全に逆に解き、既存の pole conditions を満たすように
原点近くで cutoff と一つの integral correction を施す。

Arithmetic input: 全整数 mu、恒等式 sum_{d|r}mu(d)=delta_{r,1}、Poisson。
Boundary data: f(0)=0、integral f=0 を満たす even real Schwartz function。
Actual relation: eta=f tensor product_p 1_Zp の summation。そのため finite places、
real place、二つの極条件は最初から同じ test の中にある。
Topology: 元の E、closure W、元の p_1 と p_4。新しい completion は作らない。
Zero retention: 全 ell_rho と j<m_rho の jets はそのまま。projection による消去なし。

Explicit construction: [証明](dyadic/notes/explicit_mobius_reduction.md) の (1)–(4)。
Exact support: R_n=0 on t>=0、左は非compact tail。
Unconditional rate: 2^{n/2}(1+n)、source seminorm p_4。
Arithmetic source of gain: exact Möbius inversion + pole-free Poisson の left-tail bound。
What remains: cutoff inverse の振幅と integral correction の global cancellation。

Conditional theorem: |M(X)|<=K_theta X^theta, 0<theta<1 なら
p_1(R_n)<=C_theta K_theta 2^{(theta-1/2)n}p_4(g)。
すべての theta>1/2 の Mertens bound は RH 同値。
同じ固定 algorithm の全 epsilon 準指数 bound も RH 同値であることを双方向に確認。
従って RH-independent cancellation を得たと報告しない。

Prior art: Meyer v1 §5.3 Lemmas 5.3–5.4 の inverse Euler operator/cutoff が近い。
Müntz/co-Poisson と Báez-Duarte の全整数 dilation も関連。
特定 seminorm bound の literal な既出・初出は未確定。新規性の主張なし。

Decision: 無条件の identity と c=1/2 bound を保存。endpoint を新しい証明入力として
採用する候補は終了。c=1/2 の最適性や全 reduction の不可能性は未証明。

## 要求事項ごとの到達範囲

| 要求 | 結果 |
|---|---|
| forward-only sufficiency | 完全確認。反射以外の inverse-time bound 不要 |
| T_2 W=W、negative direction も | adèlic test と E homeomorphism から確認 |
| explicit w_n、n=1..4、recurrence | D3 で全 g に構成。D1 の Gaussian range 例も別途確認 |
| compact fundamental-domain representative | compact 入力に対する非自明な exact fold は不可 |
| noncompact tail | 左半直線に support を制限、全 E seminorm は有限 |
| prime-power telescoping | D1 は range 内。D3 には actual compact archimedean shell corrections |
| R_n の全 epsilon bound | 未証明。固定構成の statement は RH 同値 |
| cyclic / functional-specific weakening | Gaussian 一つが全零点を検出。成長評価は依然未解決 |
| p=2 only と full arithmetic の差 | return は p=2、relation の Möbius inverse は全整数を使用 |
| dyadic-only Báez-Duarte density | 3 つの区間の exact 計算で反証。現商には適用しない |
| larger dual unit ball の算術記述 | 未構成。Hahn–Banach で難所を隠さない |
| full q_1 operator spectral radius | 未評価。p_4→p_1 の結果との混同なし |
| new independent proof-critical bridge | なし。graph merge 0 |

**Strategy review / final decision:** 三つの主要機構を評価した後に終了。
Level 3 は本課題の定義どおり「固定 c<1 を実際に証明した」という限定的達成。
RH 解決への新しい算術入力が得られたという success level ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/dyadic/notes/explicit_mobius_reduction.md`](dyadic/notes/explicit_mobius_reduction.md)
