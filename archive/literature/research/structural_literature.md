**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/structural_literature.md` · Original SHA-256: `27bf706846ff6c6f0692f4b7b0d13b2d1d51ddba87059950d2a9bb708ade8533`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 構造探索の数学文献台帳

確認日: 2026-09-29。対象: center_scale、accumulation_spectrum、variational_closure、prime_jump_obstruction の4ノート。21 statement records。既存主台帳との重複を許す。

各項目は charter の12フィールドを持つ。RH? は登録した使用statementがRHを前提とするかを示す。NOは未証明前件を認証する意味ではなく、RH同値定理・条件付き含意は Assumptions に明記する。原文照合と全文の独立証明検証は別であり、independently verified? は全件NO。査読不明をYESへ昇格しない。数学的prior artの引用だけを含み、着想元の物理添付・物理定数は証明出典に入れない。

## ST-Riemann1859

| Field | Value |
|---|---|
| Reference ID | ST-Riemann1859 |
| Title | Über die Anzahl der Primzahlen unter einer gegebenen Grösse |
| Authors | Bernhard Riemann; English translation by David R. Wilkins |
| Year | 1859 |
| URL | [一次資料](https://www.claymath.org/wp-content/uploads/2023/04/Wilkins-translation.pdf) |
| Claim used | center_scale: 完成関数の関数等式・中心化の根拠 |
| Exact theorem | 本文の完成関数と関数等式の導出（番号なし） |
| Assumptions | ξ の標準的完成。集合の対称性から各零点の固定性は従わない |
| RH? | NO |
| Peer-reviewed? | HISTORICAL_PUBLICATION |
| independently verified? | NO |
| Notes | 翻訳された原論文。現代の査読手続とは区別。対称性の反例はノート内の直接計算。 |

## ST-BerryKeating1999

| Field | Value |
|---|---|
| Reference ID | ST-BerryKeating1999 |
| Title | The Riemann Zeros and Eigenvalue Asymptotics |
| Authors | M. V. Berry; J. P. Keating |
| Year | 1999 |
| URL | [一次資料](https://epubs.siam.org/doi/abs/10.1137/S0036144598347497) |
| Claim used | center_scale: 裸の尺度作用とζ零点同定を区別する先行研究 |
| Exact theorem | Abstract の未知の Hermitian operator と XP 提案。証明定理として使用しない |
| Assumptions | 数学的なスペクトル対応の提案という範囲。統計の全主張を無条件として採用しない |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | SIAM Review 41, 236–266。数学的 prior art のみ。物理的定数・添付物理資料は証明入力に不使用。 |

## ST-RodgersTao2018

| Field | Value |
|---|---|
| Reference ID | ST-RodgersTao2018 |
| Title | The De Bruijn-Newman constant is non-negative |
| Authors | Brad Rodgers; Terence Tao |
| Year | 2018 |
| URL | [一次資料](https://arxiv.org/pdf/1801.05914v5) |
| Claim used | center_scale: 特定のtheta核の熱変形と一般の正偶核を区別 |
| Exact theorem | Introduction の H_t と Λ の定義; Theorem 1: Λ≥0; RH iff Λ≤0 |
| Assumptions | 論文で定義された特定の Φ と H_t。任意の非負偶核ではない |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | v5=2021-07-03、出版版に§8修正を加えた版とarXivが明記。反証法内での仮定と定理の無条件性を区別。全文再検証なし。 |

## ST-TwamleyMilburn2006

| Field | Value |
|---|---|
| Reference ID | ST-TwamleyMilburn2006 |
| Title | The Quantum Mellin transform |
| Authors | J. Twamley; G. J. Milburn |
| Year | 2006 |
| URL | [一次資料](https://arxiv.org/pdf/quant-ph/0702107v1) |
| Claim used | center_scale: log座標・半密度の数学的変換式の先行例 |
| Exact theorem | Equations (16), (25), (33)（ノート作成担当者の原文照合位置） |
| Assumptions | 半直線の L²(dx) と指定の log 座標。自己共役domainはノート内で別途設定 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | New J. Phys. 8, 328 (2006), DOI10.1088/1367-2630/8/12/328。arXiv投稿2007。数学的変換式の prior art のみ、実験・物理定数は不使用。 |

## ST-RVM2022

| Field | Value |
|---|---|
| Reference ID | ST-RVM2022 |
| Title | Counting zeros of the Riemann zeta function |
| Authors | Elchin Hasanalizade; Quanli Shen; Peng-Jie Wong |
| Year | 2022 |
| URL | [一次資料](https://arxiv.org/abs/2107.06506) |
| Claim used | center_scale: ζ零点計数と固定区間一次微分作用素の線形成長の差 |
| Exact theorem | Sections 1–2 の N(T) と Riemann–von Mangoldt 主項; 最適数値定数は使用しない |
| Assumptions | 全非自明零点を重複度込みで数える。臨界線上零点だけの計数ではない |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | J. Number Theory 235,219–241, DOI10.1016/j.jnt.2021.06.032。主台帳RVM2022と重複。 |

## ST-CC2021

| Field | Value |
|---|---|
| Reference ID | ST-CC2021 |
| Title | Weil positivity and trace formula, the archimedean place |
| Authors | Alain Connes; Caterina Consani |
| Year | 2021 |
| URL | [一次資料](https://alainconnes.org/wp-content/uploads/Selecta.pdf) |
| Claim used | center_scale / variational_closure: 尺度作用・半密度・Weil規約と局所結果の境界 |
| Exact theorem | Equations (5),(17), Appendix A, Appendix B; 限定domainのTheorem 1 |
| Assumptions | 全Weil明示公式と局所圧縮の補正を保持。Theorem1のsupport等の前件を外して全窓へ拡張しない |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | Selecta Math.27 (2021), DOI10.1007/s00029-021-00689-4。全素数・全supportの正値性を導く定理としては使用しない。 |

## ST-CC2023

| Field | Value |
|---|---|
| Reference ID | ST-CC2023 |
| Title | Spectral triples and ζ-cycles |
| Authors | Alain Connes; Caterina Consani |
| Year | 2023 |
| URL | [一次資料](https://ems.press/content/serial-article-files/44477?nt=1) |
| Claim used | prime_jump_obstruction / accumulation_spectrum: 素数平行移動の明示公式、局所形式coreの先行例 |
| Exact theorem | §2.1 (2.6)–(2.12), Proposition2.1; Proposition2.3（CCM2025 Prop3.4にも再掲） |
| Assumptions | 固定乗法窓、Haar測度、supportにより有限となる素数冪和。全実線作用素和の収束ではない |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | L’Enseignement Mathématique69,93–148, DOI10.4171/LEM/1049。prime jump の発散障害はノート内で独立導出。 |

## ST-Connes1998Local

| Field | Value |
|---|---|
| Reference ID | ST-Connes1998Local |
| Title | Trace formula in noncommutative geometry and the zeros of the Riemann zeta function |
| Authors | Alain Connes |
| Year | 1998 |
| URL | [一次資料](https://arxiv.org/pdf/math/9811068v1) |
| Claim used | center_scale / accumulation_spectrum: critical zerosのスペクトル実現と半局所trace |
| Exact theorem | III Theorem1 / Corollary2; VII Theorem4 |
| Assumptions | IIIはδ>1の重み付き商空間で既に臨界線上の零点のみ、重複度制限あり。VIIは無限素点を含む有限Sとcompact support Schwartz h |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | Selecta Math.5(1999),29–106, DOI10.1007/s000290050042。arXiv v1の番号。全零点捕捉・全表現unitaryとは主張しない。 |

## ST-Connes1998GlobalCriterion

| Field | Value |
|---|---|
| Reference ID | ST-Connes1998GlobalCriterion |
| Title | Trace formula in noncommutative geometry and the zeros of the Riemann zeta function — global criterion |
| Authors | Alain Connes |
| Year | 1998 |
| URL | [一次資料](https://arxiv.org/pdf/math/9811068v1) |
| Claim used | accumulation_spectrum: 大域traceの未証明箇所とRH同値の区別 |
| Exact theorem | VIII Theorem5; 数体対応の説明 pp.45–47 |
| Assumptions | Theorem5の明記された体は正標数。全Hecke L関数のRHと指定の大域trace公式の同値。数体では異なる近似射影の説明が必要 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | 同値定理の主張はRHを前提としない。大域trace公式の真を無条件入力にしていない。正標数の定理文を数体へそのまま引用しない。 |

## ST-CCM2025Core

| Field | Value |
|---|---|
| Reference ID | ST-CCM2025Core |
| Title | Zeta Spectral Triples — localized form and core |
| Authors | Alain Connes; Caterina Consani; Henri Moscovici |
| Year | 2025 |
| URL | [一次資料](https://arxiv.org/html/2511.22755v1) |
| Claim used | accumulation_spectrum: exact restrictionsの固定窓極限 |
| Exact theorem | Propositions3.3–3.4; Theorem3.6 |
| Assumptions | λ>1、L²([λ⁻¹,λ],du/u)、E=span(V_n)がform core、有限E_Nへの厳密制限 |
| RH? | NO |
| Peer-reviewed? | PUBLISHED_CHAPTER_REVIEW_UNCONFIRMED |
| independently verified? | NO |
| Notes | EMS公刊章 DOI10.4171/ELM/37/3。固定窓の最小値は有限制限最小値の極限。全NのPSDは別前件。 |

## ST-CCM2025Conditional

| Field | Value |
|---|---|
| Reference ID | ST-CCM2025Conditional |
| Title | Zeta Spectral Triples — finite selfadjoint construction and missing steps |
| Authors | Alain Connes; Caterina Consani; Henri Moscovici |
| Year | 2025 |
| URL | [一次資料](https://arxiv.org/html/2511.22755v1) |
| Claim used | accumulation_spectrum: 条件付き自己共役構成と未証明のζ同定 |
| Exact theorem | Theorem5.10; Section8 |
| Assumptions | 有限最低固有値ε_Nが単純、ξが偶、δ_Nξ=1。商計量はQW−ε_N I。全窓simple/evenと真の最低固有関数近似は§8の未完手順 |
| RH? | NO |
| Peer-reviewed? | PUBLISHED_CHAPTER_REVIEW_UNCONFIRMED |
| independently verified? | NO |
| Notes | RH仮定の定理ではないが、明示された条件付き。ε_Nを引いた正性は元形式のPSDを示さない。数値一致を全零点同定としない。 |

## ST-CvS2025

| Field | Value |
|---|---|
| Reference ID | ST-CvS2025 |
| Title | Quadratic Forms, Real Zeros and Echoes of the Spectral Action |
| Authors | Alain Connes; Walter D. van Suijlekom |
| Year | 2025 |
| URL | [一次資料](https://arxiv.org/html/2511.23257v1) |
| Claim used | accumulation_spectrum: 条件付き固定窓のFourier実零点定理 |
| Exact theorem | Theorem6.1（正確な定理文）; Proposition5.10 |
| Assumptions | 実分布Dから式(6)で三角多項式上の形式。半有界かつ本質的自己共役、最下点が孤立単純固有値、固有関数が区間反転で偶 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | Commun.Math.Phys.406:312, DOI10.1007/s00220-025-05493-1。operator coreの仮定を単なるform coreと置換しない。 |

## ST-Suzuki2026Local

| Field | Value |
|---|---|
| Reference ID | ST-Suzuki2026Local |
| Title | Weil’s quadratic form via the screw function — local statements |
| Authors | Masatoshi Suzuki |
| Year | 2026 |
| URL | [一次資料](https://arxiv.org/html/2606.09096v3) |
| Claim used | 全4ノートのWeil明示公式・局所Friedrichs実現・小窓正値性 |
| Exact theorem | §1.1; Theorem1.1; Theorem1.4; §2.4 |
| Assumptions | 固定a>0でB_a=D*G_aD、Friedrichs拡張。正値・最低固有値単純性の無条件結果は十分小さいaに限定 |
| RH? | NO |
| Peer-reviewed? | PREPRINT |
| independently verified? | NO |
| Notes | v3 2026-09-23。全窓正値性や§7のRH下heuristicは使用statementに含めない。 |

## ST-Suzuki2026Limit

| Field | Value |
|---|---|
| Reference ID | ST-Suzuki2026Limit |
| Title | Weil’s quadratic form via the screw function — conditional limit criterion |
| Authors | Masatoshi Suzuki |
| Year | 2026 |
| URL | [一次資料](https://arxiv.org/html/2606.09096v3) |
| Claim used | center_scale: 自己共役性以外に必要な全零点同定条件の具体例 |
| Exact theorem | Corollary1.6, equation(1.12) |
| Assumptions | 十分大きいaでλ(a)<λ_a, θ(a), 上半平面でanalyticなφ(a,z)を選び、e^φ Wがξ/(ξ+ξ′)へ上半平面compact上一様収束 |
| RH? | NO |
| Peer-reviewed? | PREPRINT |
| independently verified? | NO |
| Notes | 含意『極限条件⇒RH』はRHを仮定しない。ただし極限条件は未証明。旧版の全平面/z²ξ/ξ′と混在させない。 |

## ST-Burnol2004

| Field | Value |
|---|---|
| Reference ID | ST-Burnol2004 |
| Title | Two complete and minimal systems associated with the zeros of the Riemann zeta function |
| Authors | Jean-François Burnol |
| Year | 2004 |
| URL | [一次資料](https://arxiv.org/pdf/math/0203120v6) |
| Claim used | accumulation_spectrum: Sonine/Mellinの解析性・評価ベクトル・完全性の限界 |
| Exact theorem | Theorem2.1; Proposition2.2; Theorem3.1; Theorem7.7; Section8 |
| Assumptions | K_a: fとcosine変換が(0,a)で0、L_a:ともに定数。全複素評価点。零点は全非自明零点を重複度付きで使用 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | JTNB16,65–94, DOI10.5802/jtnb.434。一般Sonine関数は任意追加零点を許す。完全系・主要零点密度からRHは従わない。 |

## ST-NakamuraSuzuki2023Euler

| Field | Value |
|---|---|
| Reference ID | ST-NakamuraSuzuki2023Euler |
| Title | On infinitely divisible distributions related to the Riemann hypothesis — Euler distribution |
| Authors | Takashi Nakamura; Masatoshi Suzuki |
| Year | 2023 |
| URL | [一次資料](https://arxiv.org/pdf/2306.08317v1) |
| Claim used | accumulation_spectrum: ζ(σ+it)/ζ(σ)のcompound Poisson表示 |
| Exact theorem | Section1, Euler distribution representation following equation(1.7) |
| Assumptions | σ>1。Lévy測度Σ_{p,r}p^(−rσ)/r δ_(−rlogp)。この項目はTheorem1.2のRH下零点Lévy測度とは別 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | Statistics&Probability Letters, DOI10.1016/j.spl.2023.109889。σ↓1で弱収束が失われる説明はノート内の解析。 |

## ST-Nakamura2015Characteristic

| Field | Value |
|---|---|
| Reference ID | ST-Nakamura2015Characteristic |
| Title | A complete Riemann zeta distribution and the Riemann hypothesis — characteristic functions |
| Authors | Takashi Nakamura |
| Year | 2015 |
| URL | [一次資料](https://arxiv.org/pdf/1504.03438) |
| Claim used | accumulation_spectrum: 正測度表示自体ではRHに足りない例 |
| Exact theorem | Theorem1.1; proof Section2.1 |
| Assumptions | 全実σでΞ_σ(t)=ξ(σ−it)/ξ(σ)。完成ξを使用。裸ζとは異なる |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | Bernoulli21,604–617。PDFは出版物の電子再録。特性関数性と零点位置を区別。 |

## ST-Nakamura2015PretendedCriterion

| Field | Value |
|---|---|
| Reference ID | ST-Nakamura2015PretendedCriterion |
| Title | A complete Riemann zeta distribution and the Riemann hypothesis — pretended infinite divisibility criterion |
| Authors | Takashi Nakamura |
| Year | 2015 |
| URL | [一次資料](https://arxiv.org/pdf/1504.03438) |
| Claim used | accumulation_spectrum: 特性関数性より強い別条件がRH同値であること |
| Exact theorem | Theorem1.2; definition in Section1.3 |
| Assumptions | 全σ∈(1/2,1)でΞ_σがpretended-infinitely divisible。符号付きLévy測度を許し、通常のLévy可積分条件を課さないという同論文独自の定義 |
| RH? | NO |
| Peer-reviewed? | YES |
| independently verified? | NO |
| Notes | 同値命題自体はRH無仮定。RH⇒の明示測度表示を無条件に使用しない。通常のinfinitely divisibleと同一視禁止。Theorem1.4はσ>1でnot infinitely divisible but quasiと述べる。 |

## ST-PinchoverTintarev2004

| Field | Value |
|---|---|
| Reference ID | ST-PinchoverTintarev2004 |
| Title | A ground state alternative for singular Schrödinger operators |
| Authors | Yehuda Pinchover; Kyril Tintarev |
| Year | 2004 |
| URL | [一次資料](https://arxiv.org/pdf/math/0411658v1) |
| Claim used | variational_closure: ground-state identityの適用条件を検査 |
| Exact theorem | Lemma2.4, equation(2.6); Theorem1.4の非負性前件 |
| Assumptions | 指定の局所楕円作用素L=−div(A∇)+V。Lemma2.4は有界C¹領域D, Lψ=0, v∈H¹(D;R), vψ\|∂D=0。Theorem1.4は初めから形式非負 |
| RH? | NO |
| Peer-reviewed? | UNCONFIRMED_FOR_THIS_AUDIT |
| independently verified? | NO |
| Notes | arXiv header2004と本文date2018が異なる。今回は査読出版の確認を追加していない。一般Weil形式への移植・逆向きの正値性導出は禁止。 |

## ST-Groskin2026Tail

| Field | Value |
|---|---|
| Reference ID | ST-Groskin2026Tail |
| Title | A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form |
| Authors | Akiva Groskin |
| Year | 2026 |
| URL | [一次資料](https://arxiv.org/html/2607.02828v3) |
| Claim used | variational_closure: 特定有限行列のarchimedean cutoffと他の極限を分離 |
| Exact theorem | Theorem3.2; Corollary3.3（定義の照合用Theorem2.5） |
| Assumptions | 固定c>1,N、T>max(2πN/log(c),7)、指定の有限周波数行列。dictionaryは実偶ベクトル |
| RH? | NO |
| Peer-reviewed? | PREPRINT |
| independently verified? | NO |
| Notes | v3 2026-08-14。checkpoint02で辞書・tailの限定独立監査、版固定package39/39checksum確認、c13,N4の原著再実行と独立Arb直接積分を実施。論文全体・401次認証未再現のためverified欄はNOを維持。全c,N正値性・support単調性ではない。詳細proofs/audits/groskin-computation.md |

## ST-Zhu2026Window

| Field | Value |
|---|---|
| Reference ID | ST-Zhu2026Window |
| Title | Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law |
| Authors | Xuefeng Zhu |
| Year | 2026 |
| URL | [一次資料](https://arxiv.org/html/2608.24827v2) |
| Claim used | variational_closure: 有限blockと残りのcouplingを共に評価する設計の参考 |
| Exact theorem | Theorem1.2; Theorem6.2; Corollary6.3; Section7 withdrawal |
| Assumptions | 指定された固定窓の複素試験関数と認証誤差の前件。局所数値主張は独立再検証していない |
| RH? | NO |
| Peer-reviewed? | PREPRINT |
| independently verified? | NO |
| Notes | checkpoint03: v2原本の取得後も補足code/行列/factorの公開先未確認。一般entry boundにT/π欠落を厳密反証しtail/couplingは独立修復。原著L.8 head未認証。自作a=.5全mode認証は別ノートT090。全窓・RH主張に使用しない。 |

## 台帳の境界

- ノート内で直接証明された反例、平行移動恒等式、Schur判定、正値形式の商完備化は外部研究成果に帰属させていない。新規性も主張しない。
- prime_jump_obstruction が使う Euler の素数逆数和の発散は古典的入力だが、同ノートに原典URL・定理位置がない。この短時間台帳では未読の原典を補って閲読済みに見せず、原典追跡未了として残す。
- Plancherel、Hurwitz、閉形式論等の標準入力についても、ノートに指定されていない原典を捏造しない。四ノート中の主要な明示引用は収録したが、全標準定理の最初の原典を網羅する台帳ではない。
- Berry–Keating と Twamley–Milburn はノートが明示した数学的な対応・変換式の先行例としてのみ収録した。物理添付とは別資料であり、物理モデルをRHの証明前提としない。


## ST-DLMF25

- **id:** ST-DLMF25
- **title:** DLMF §25.11 Hurwitz Zeta Function
- **authors:** NIST Digital Library of Mathematical Functions
- **year:** 2026
- **url:** https://dlmf.nist.gov/25.11#E43
- **claim_used:** Euler境界の数値プローブに用いるEuler–Maclaurin近似
- **exact_theorem:** §25.11(iii), equation 25.11.43
- **assumptions:** 固定s、正の大きいa。実装N=1000、B2〜B8、binary64、区間保証なし
- **depends_on_RH:** NO
- **peer_reviewed:** OFFICIAL_REFERENCE
- **verified_independently:** NO
- **notes:** RHの解析入力でなく数値実装の参照。ζ(2)のsanity error約1.8e−15は他点の誤差証明ではない。

## ST-CeroneDragomir2009

- **id:** ST-CeroneDragomir2009
- **title:** Some convexity properties of Dirichlet series with positive terms
- **authors:** Pietro Cerone and Sever S. Dragomir
- **year:** 2009
- **url:** https://rgmia.org/papers/v8n4/IDSLCNew.pdf
- **claim_used:** 固定積imbalanceの正係数Dirichlet級数・対数凸性の既知性
- **exact_theorem:** 2005-10-25公開稿 §1 (1.5), §3 Proposition4, Remark5
- **assumptions:** 実パラメータで正係数級数が収束する範囲。零点への等号移行なし
- **depends_on_RH:** NO
- **peer_reviewed:** YES
- **verified_independently:** NO
- **notes:** Math.Nachr.282(2009),964–975。DOI10.1002/mana.200610783。該当公式のみ照合、全論文未検証。逆数凹性の結果は不採用。

## ST-Nielsen2022

- **id:** ST-Nielsen2022
- **title:** A note on some information-theoretic divergences between Zeta distributions
- **authors:** Frank Nielsen
- **year:** 2022
- **url:** https://arxiv.org/html/2104.10548v3
- **claim_used:** prime-power imbalance aggregateの半分が既知Bhattacharyya距離・Jensen差に一致
- **exact_theorem:** Table1; Theorem1直前のBhattacharyya coefficient and Jensen divergence
- **assumptions:** 両方のζ分布パラメータ>1。実確率分布。解析接続後には適用しない
- **depends_on_RH:** NO
- **peer_reviewed:** UNCONFIRMED_FOR_THIS_AUDIT
- **verified_independently:** NO
- **notes:** 一次公式をLITERATUREとrootが照合。全論文の正確性は未検証。直接代数で今回の特殊化を再導出。imbalance-prior-art.md参照。

## Support propagation の追加出典（2026-09-29）

詳細は [限定文献監査](../literature/notes/support-propagation-prior-art.md)、12項目の正規レコードは [JSON台帳](structural_sources.json) を参照。次の4件はすべて verified_independently=NO。RH無仮定の同値・条件付き定理を記録しても、その前件の成立を認証したことにはならない。

| Reference ID | 一次資料・使用箇所 | 読取範囲と適用限界 |
|---|---|---|
| ST-AndersonTrapp1975 | [Shorted Operators. II](https://epubs.siam.org/doi/10.1137/0128007)、Abstract | 査読公刊。出版社 abstract のみ、全文・定理番号未確認。定義は ambient operator の正値性を前提にする。 |
| ST-AlpayEtAl2010 | [arXiv:0912.4444v1](https://arxiv.org/pdf/0912.4444v1)、Thms 1.1–1.2、p.6 | 査読公刊。該当本文を閲読、全証明未検証。全区間可逆性が必要で、逆構成した accelerant と実際の Weil 核の同定は別義務。 |
| ST-Suzuki2021Canonical | [arXiv:1606.05726v3](https://arxiv.org/html/1606.05726v3)、Thms 2.1–2.4、Prop. 5.1 | 査読公刊、定理文は arXiv v3 に固定。該当本文閲読、全証明未検証。RH 同値条件は大域 determinant 非消滅と endpoint 極限の両方を含む。Prop. 5.1 の HB 前件を保持。 |
| ST-KreinLanger2014 | [出版社・DOI](https://link.springer.com/article/10.1007/s00020-013-2091-z)、Abstract | 査読公刊。出版社 abstract のみ、全文・個別定理条件未確認。正の延長の存在と算術的に指定された延長の一致を区別する。 |

この追記は先行研究と適用条件の記録であり、新規性や全 support の Weil 正値性を主張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/support-propagation-prior-art.md`](../literature/notes/support-propagation-prior-art.md)
- [`proofs/audits/groskin-computation.md`](../../audits/proofs/audits/groskin-computation.md)
- [`research/structural_sources.json`](structural_sources.json)
