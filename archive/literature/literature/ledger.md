**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/ledger.md` · Original SHA-256: `dfc66b0415dc7ca30388e88a9847cfeceb5b24c3ccb711da8d90634063b8177a`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Literature Ledger

確認日: 2026-09-29。NO の独立検証欄は原文未確認を意味するとは限らず、定理の完全な独立再証明・計算再現をしていないという意味。原文の確認箇所は各項目に記す。PREPRINT は使用した版の区分であり、別途出版済みでないことの断定ではない。

## CMI

- **Reference ID:** CMI
- **Title:** Riemann Hypothesis: official problem page
- **Authors:** Clay Mathematics Institute
- **Year:** 2026
- **URL/DOI/arXiv:** https://www.claymath.org/millennium/riemann-hypothesis/
- **Claim used:** RHの公式な未解決状態と定義
- **Exact theorem:** Unsolved / Riemann Hypothesis
- **Assumptions:** 非自明零点。数値確認は定義を置き換えない
- **Depends on RH?:** NO
- **Peer-reviewed?:** NO
- **Verified independently?:** NO
- **Notes:** 2026-09-29閲覧。研究論文ではない。

## RVM2022

- **Reference ID:** RVM2022
- **Title:** Counting zeros of the Riemann zeta function
- **Authors:** Elchin Hasanalizade and Quanli Shen and Peng-Jie Wong
- **Year:** 2022
- **URL/DOI/arXiv:** https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf
- **Claim used:** 零点計数 O(T log(T+2))
- **Exact theorem:** Sections 1–2, N_Q(T); 最適数値定数は使用しない
- **Assumptions:** 全非自明零点を重複度込みで数える
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** J. Number Theory 235, 219–241; DOI 10.1016/j.jnt.2021.06.032。BUILDERが原文照合。

## Weil1952

- **Reference ID:** Weil1952
- **Title:** Sur les formules explicites de la theorie des nombres premiers
- **Authors:** Andre Weil
- **Year:** 1952
- **URL/DOI/arXiv:** https://cds.cern.ch/record/471308
- **Claim used:** Weil判定法の原典追跡
- **Exact theorem:** 原版の定理番号未照合。現代C_c∞版はSuzuki2023で照合
- **Assumptions:** 原典のテスト空間は逐条未確認
- **Depends on RH?:** NO
- **Peer-reviewed?:** NO
- **Verified independently?:** NO
- **Notes:** Lund supplement pp.252–265。書誌確認のみ。定理細部の根拠に単独使用しない。

## Suzuki2023

- **Reference ID:** Suzuki2023
- **Title:** Aspects of the screw function corresponding to the Riemann zeta function
- **Authors:** Masatoshi Suzuki
- **Year:** 2023
- **URL/DOI/arXiv:** https://arxiv.org/pdf/2206.03682v4
- **Claim used:** Weil基準の正確なC_c∞版
- **Exact theorem:** Section 3.2, equations (3.3)–(3.5)
- **Assumptions:** 全complex compactly supported smooth test functions; multiplicities
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** J. Lond. Math. Soc. 108, 1448–1487。PDF版はVersion of May 31, 2023（arXivヘッダ30 May 2023）。HTMLの2026本文Dateは参照せず版固定PDFを採用。

## Suzuki2025

- **Reference ID:** Suzuki2025
- **Title:** On the Hilbert space derived from the Weil distribution
- **Authors:** Masatoshi Suzuki
- **Year:** 2025
- **URL/DOI/arXiv:** https://doi.org/10.4153/S0008414X25101739
- **Claim used:** 定義とWeil判定法の規約照合
- **Exact theorem:** Section 1 (1.1),(1.2); Section 3.1 (3.3)
- **Assumptions:** 定義は無条件。Theorem 1.1のHilbert空間同型はRH仮定
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** RHを仮定するTheorem 1.1を無条件依存に採用しない。

## Li1997

- **Reference ID:** Li1997
- **Title:** The positivity of a sequence of numbers and the Riemann hypothesis
- **Authors:** Xian-Jin Li
- **Year:** 1997
- **URL/DOI/arXiv:** https://doi.org/10.1006/jnth.1997.2137
- **Claim used:** Li criterionのルート比較
- **Exact theorem:** λ_n≥0 for every nとRHの同値。全文の定理番号未照合
- **Assumptions:** ξから定義された全係数。有限個の計算は不足
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** 出版社abstract照合のみ。主証明依存に採用しない。

## BaezDuarte2002

- **Reference ID:** BaezDuarte2002
- **Title:** A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis
- **Authors:** Luis Baez-Duarte
- **Year:** 2002
- **URL/DOI/arXiv:** https://arxiv.org/pdf/math/0202141v2
- **Claim used:** 離散化されたL²近似基準
- **Exact theorem:** Theorem 1.1: χ_(0,1)∈closure span{fractional_part(1/(ax)): a∈N} iff RH
- **Assumptions:** H=L²(0,∞); closure in its norm
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 原稿v2本文確認。自然Möbius部分和のa.e.収束とH収束を区別。

## ConreyLi1998

- **Reference ID:** ConreyLi1998
- **Title:** A note on some positivity conditions related to zeta- and L-functions
- **Authors:** J. Brian Conrey and Xian-Jin Li
- **Year:** 1998
- **URL/DOI/arXiv:** https://arxiv.org/pdf/math/9812166v1
- **Claim used:** de Branges正値条件の障害調査
- **Exact theorem:** 本文の条件と適用例を調査用に確認。今回その定理を使用しない
- **Assumptions:** 特定のHilbert空間の正値条件。全de Branges手法の不可能性とは異なる
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** arXiv版を固定。出版版メタデータの再確認は保留。

## Connes1998

- **Reference ID:** Connes1998
- **Title:** Trace formula in noncommutative geometry and the zeros of the Riemann zeta function
- **Authors:** Alain Connes
- **Year:** 1998
- **URL/DOI/arXiv:** https://arxiv.org/abs/math/9811068v1
- **Claim used:** Hilbert–Pólya / trace formulaのルート比較
- **Exact theorem:** abstractのspectral interpretationとtrace formulaへのreduction
- **Assumptions:** 全trace formulaの成立を未証明条件として残す
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 本文88頁の全面監査なし。推論の依存に採用しない。

## PRZZ2018

- **Reference ID:** PRZZ2018
- **Title:** More than five-twelfths of the zeros of zeta are on the critical line
- **Authors:** Kyle Pratt and Nicolas Robles and Alexandru Zaharescu and Dirk Zeindler
- **Year:** 2018
- **URL/DOI/arXiv:** https://arxiv.org/abs/1802.10521
- **Claim used:** mollifier経路の過去の到達点
- **Exact theorem:** 要旨の無条件割合改善。全文定理番号未照合
- **Assumptions:** 全零点を重複度込みで数えた漸近割合
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 最新記録という主張はしない。

## GuthMaynard2024

- **Reference ID:** GuthMaynard2024
- **Title:** New large value estimates for Dirichlet polynomials
- **Authors:** Larry Guth and James Maynard
- **Year:** 2024
- **URL/DOI/arXiv:** https://arxiv.org/abs/2405.20552
- **Claim used:** zero-density経路の進展
- **Exact theorem:** 要旨: N(σ,T)≤T^(30(1−σ)/13+o(1))。精密σ域は未監査
- **Assumptions:** 主定理を使用しないため、未確認の一様域は主張しない
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 原稿要旨確認。2026出版情報は今回依存に不要。零点ゼロ個は従わない。

## Lamzouri2026

- **Reference ID:** Lamzouri2026
- **Title:** A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line
- **Authors:** Youness Lamzouri
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/html/2609.02882v1
- **Claim used:** 核最適化問題の出所と限定的barrier
- **Exact theorem:** Theorem 1.1; Proposition 2.1; Lemma 3.2; Remark 3.4
- **Assumptions:** Theorem 1.1は無条件の主張。核側はη real even, smooth, support(-1/2,1/2), ∫η²=1
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 解析数論部分全体は独立未検証。kernel最適化だけを別途初等証明。

## Wang2026

- **Reference ID:** Wang2026
- **Title:** Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals
- **Authors:** Biao Wang
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/html/2609.07918v1
- **Claim used:** 2026-09 の新着結果を把握
- **Exact theorem:** Theorem 1.1, equations (1.7),(1.8)
- **Assumptions:** fixed 0<θ<1, H=T^θ; liminf割合
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 原文の主張を確認。独立検証未済で主定理の依存にはしない。

## Deligne1974

- **Reference ID:** Deligne1974
- **Title:** La conjecture de Weil I
- **Authors:** Pierre Deligne
- **Year:** 1974
- **URL/DOI/arXiv:** https://numdam.org/articles/10.1007/BF02684373/
- **Claim used:** 有限体上のRHとの類推範囲
- **Exact theorem:** 有限体上の幾何学的Weil予想。本文定理番号は本探索で未照合
- **Assumptions:** 有限体上の対象。数体のζへの対応構成を含まない
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** Publ. Math. IHES 43, 273–307。今回ζへの推論に使用しない。

## Montgomery1973

- **Reference ID:** Montgomery1973
- **Title:** The pair correlation of zeros of the zeta function
- **Authors:** H. L. Montgomery
- **Year:** 1973
- **URL/DOI/arXiv:** https://www-personal.umich.edu/~hlm/paircor1.pdf
- **Claim used:** random matrix関連と仮定検査
- **Exact theorem:** Section I, Theorem / opening sentence
- **Assumptions:** RHを論文全体で仮定
- **Depends on RH?:** YES
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** Proc. Sympos. Pure Math. 24,181–193。最近の無条件版と混同しない。

## CarrilloEtAl2019

- **Reference ID:** CarrilloEtAl2019
- **Title:** Nonlinear aggregation-diffusion equations: radial symmetry and long time asymptotics
- **Authors:** J. A. Carrillo and S. Hittmeir and B. Volzone and Y. Yao
- **Year:** 2019
- **URL/DOI/arXiv:** https://doi.org/10.1007/s00222-019-00898-x
- **Claim used:** 全実線密度エネルギーの先行研究照合
- **Exact theorem:** Section 3, Theorems 3.7 and 3.10
- **Assumptions:** d=1,m=2,M=1,W=2(|x|−1)へ特殊化。有限一次moment。核条件はノートで照合
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** 汎関数は今回のE−1と一致。cosineは既存Euler–Lagrangeから導出できる。原文に同定数が印刷されるとまでは主張しない。

## Tschukin2017

- **Reference ID:** Tschukin2017
- **Title:** Concepts of modeling surface energy anisotropy in phase-field approaches
- **Authors:** Tschukin and Silberzahn and Selzer and Amos and Schneider and Nestler
- **Year:** 2017
- **URL/DOI/arXiv:** https://doi.org/10.1186/s40517-017-0077-9
- **Claim used:** CDFエネルギーと既知sine profileの照合
- **Exact theorem:** Isotropic phase-field model, equations (6) and (7)
- **Assumptions:** double-obstacle potential, ε=2√2/π, γ=π/(2√2), φ=Fに特殊化
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:** 既知のprofileとの一致。CDF平方剰余の最古の原典としては指定しない。

## DLMF59

- **Reference ID:** DLMF59
- **Title:** DLMF 5.9 Integral Representations
- **Authors:** NIST Digital Library of Mathematical Functions
- **Year:** 2026
- **URL/DOI/arXiv:** https://dlmf.nist.gov/5.9#E16
- **Claim used:** 独立有限行列のarchimedean積分とdigammaの規約
- **Exact theorem:** 5.9.16; 5.7.6との部分分数照合
- **Assumptions:** Re(z)>0でのdigamma積分。区間L>0と整数frequencyに特殊化
- **Depends on RH?:** NO
- **Peer-reviewed?:** OFFICIAL_REFERENCE
- **Verified independently?:** NO
- **Notes:** groskin-computation.mdの解析導出で使用。DLMFの全章を独立再証明したという意味ではない。

## PythonFlint09

- **Reference ID:** PythonFlint09
- **Title:** acb: complex numbers, python-flint 0.9.0 documentation
- **Authors:** python-flint developers
- **Year:** 2026
- **URL/DOI/arXiv:** https://python-flint.readthedocs.io/en/latest/acb.html#acb.integral
- **Claim used:** Arb認証求積のanalytic flagと返却ballの仕様
- **Exact theorem:** acb.integral; acb.sinc; digamma/polygamma API
- **Assumptions:** meromorphic integrandは極を含む場合nonfinite ball。有限返却ballを区間LDLへ渡す
- **Depends on RH?:** NO
- **Peer-reviewed?:** OFFICIAL_DOCUMENTATION
- **Verified independently?:** NO
- **Notes:** 原著のpython-flint0.8.0と今回0.9.0を区別。小例独立再現で実使用。ライブラリ内部の形式検証は未実施。

## DLMF1054

- **Reference ID:** DLMF1054
- **Title:** DLMF 10.54 Spherical Bessel Integral Representations
- **Authors:** NIST Digital Library of Mathematical Functions
- **Year:** 2026
- **URL/DOI/arXiv:** https://dlmf.nist.gov/10.54
- **Claim used:** Legendre Fourier規格化と無限tailの上界
- **Exact theorem:** 10.54.1 and 10.54.2; power series 10.53.1
- **Assumptions:** nは非負整数。complex引数にはPoisson表示、実引数には絶対値1のcosを使用
- **Depends on RH?:** NO
- **Peer-reviewed?:** OFFICIAL_REFERENCE
- **Verified independently?:** NO
- **Notes:** 固定窓の独立certificateで使用。tailのn!・double factorial・Fourier位相を別途監査。

## CC2021

- **Reference ID:** CC2021
- **Title:** Weil positivity and trace formula, the archimedean place
- **Authors:** Alain Connes and Caterina Consani
- **Year:** 2021
- **URL/DOI/arXiv:** https://link.springer.com/article/10.1007/s00029-021-00689-4
- **Claim used:** 限定domainを維持して引用可
- **Exact theorem:** Theorem 1; Theorem 11
- **Assumptions:** g in C_c^infinity(R_+^*), support [2^(-1/2),2^(1/2)], transform vanishes at i/2 and 0 for Theorem 1
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:**  今回未実施、第三者の独立計算再現は未調査

## CC2023

- **Reference ID:** CC2023
- **Title:** Spectral triples and zeta-cycles
- **Authors:** Alain Connes and Caterina Consani
- **Year:** 2023
- **URL/DOI/arXiv:** https://ems.press/journals/lem/articles/11033001
- **Claim used:** localized form/coreの先行文献
- **Exact theorem:** Section 2; Proposition 2.3 as restated in CCM2025 Proposition 3.4
- **Assumptions:** abstractのみ確認、主定理に不使用
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:**  今回未実施

## CvS2025

- **Reference ID:** CvS2025
- **Title:** Quadratic Forms, Real Zeros and Echoes of the Spectral Action
- **Authors:** Alain Connes and Walter D. van Suijlekom
- **Year:** 2025
- **URL/DOI/arXiv:** https://arxiv.org/html/2511.23257v1
- **Claim used:** 条件付き固定窓無限次元定理。全窓仮定やxi同定を結論に加えない
- **Exact theorem:** Theorem 1.2 (informal overview); Theorem 6.1 (precise); Proposition 5.10
- **Assumptions:** real distribution on [0,L], quadratic form (6) on trigonometric polynomials; lower-bounded essentially self-adjoint operator; simple isolated lowest eigenvalue with reflection-even eigenfunction
- **Depends on RH?:** NO
- **Peer-reviewed?:** YES
- **Verified independently?:** NO
- **Notes:**  今回逐行再構成は未実施

## CCM2025

- **Reference ID:** CCM2025
- **Title:** Zeta Spectral Triples
- **Authors:** Alain Connes and Caterina Consani and Henri Moscovici
- **Year:** 2025
- **URL/DOI/arXiv:** https://arxiv.org/html/2511.22755v1
- **Claim used:** core・下有界性・条件付き有限作用素。global positivityには未使用
- **Exact theorem:** Propositions 3.3 and 3.4; Theorem 3.6; Theorem 5.10; Section 8
- **Assumptions:** QW_lambda on L2([lambda^-1,lambda],du/u), form core E=span(V_n); finite theorem uses E_N and simple-even ground-state assumptions
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:**  今回未実施。本文の数値実験は著者によるもの

## Suzuki2026v3

- **Reference ID:** Suzuki2026v3
- **Title:** Weil's quadratic form via the screw function
- **Authors:** Masatoshi Suzuki
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/abs/2606.09096
- **Claim used:** 局所・構成定理は検証候補。極限仮説を採用しない
- **Exact theorem:** Theorems 1.1, 1.3, 1.4, 1.5; Corollary 1.2; Corollary 1.6 (conditional limit)
- **Assumptions:** B_a=D*G_aD on H_0^1(-a,a); G_a on mean-zero L2; small-a positivity only; shifted space uses lambda<lambda_a
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** v3 Corollary 1.6は上半平面compact上一様収束とxi/(xi+xi')。旧版のz^2 xi/xi'・全平面compactと異なる 定理仮定を本文確認、完全な独立証明監査は未実施 Corollary 1.6はRHでなく未証明の極限条件に依存。Section 7のRH下heuristicは独立項目に分離。

## Groskin2026v3

- **Reference ID:** Groskin2026v3
- **Title:** A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form
- **Authors:** Akiva Groskin
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/abs/2607.02828
- **Claim used:** 有限辞書・archimedean tailの条件を独立監査。c13,N4のみArb認証再現。全c,N正値性ではない
- **Exact theorem:** Theorem 2.5; Theorem 3.2; Corollary 3.3
- **Assumptions:** fixed c>1,N; dictionary real-even vectors; tail theorem C^{[-N,N]}, T>max(2pi N/log(c),7)
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:**  2026-09-29限定監査: Theorem2.5実偶辞書とTheorem3.2主要tailを再導出。Lemma2.1係数2とCor3.3左端に修正注意。原著c13,N4再実行と独立Arb直接積分9次正定値認証が一致。原著401次証明書・論文全体の検証は未済。詳細proofs/audits/groskin-{dictionary,tail,computation}.md

## Zhu2026v2

- **Reference ID:** Zhu2026v2
- **Title:** Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau-Widom decay law
- **Authors:** Xuefeng Zhu
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/abs/2608.24827
- **Claim used:** 正しい有限還元の独立再導出に使用。原著L.8 head・simple-even主張は依存採用保留。
- **Exact theorem:** Theorem 1.2; Theorem 6.2; Corollary 6.3; Section 7 (withdrawal)
- **Assumptions:** positivity claimed for complex f supported in [-0.8,0.8]; corresponding autocorrelation support [-1.6,1.6]
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** Section 7 explicitly retracts an earlier L=1.19 positivity certificate claim due to wrong-direction prime-comb bound v2 PDF/TeX取得。§17のcode/matrix/factor/checksum一式の公開先を確認できず原著head未再現。一般entry boundを厳密反証、正しい係数でL.8 tail/couplingのみ独立修復。別のa=.5 fixed-window certificateは自作Arbで認証しT090に分離。 Theorem 1.3はRHを仮定するためこのNO分類から除外し、独立項目に分離。

## KimEtAl2026v2

- **Reference ID:** KimEtAl2026v2
- **Title:** A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion
- **Authors:** Taebong Kim and Youngsik Hong and Minsik Kim and Sunyoung Choi and Jaewon Jang and Junghoon Shin and Minseo Kim
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/abs/2607.24830
- **Claim used:** 探索の参考のみ、主定理依存には使用しない
- **Exact theorem:** 本文定理は未監査
- **Assumptions:** abstractのみ確認、主定理に不使用
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:**  書誌・abstractだけ確認。本文定理監査・計算再現なし

## Zhu2026Conditional

- **Reference ID:** Zhu2026Conditional
- **Title:** Weil positivity in compact windows: conditional claim only
- **Authors:** Xuefeng Zhu
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/html/2608.24827v2
- **Claim used:** 仮定検査のみ。依存不採用
- **Exact theorem:** Theorem 1.3
- **Assumptions:** RHを仮定
- **Depends on RH?:** YES
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 同一論文の固定窓主張とは区別。

## Suzuki2026Heuristic

- **Reference ID:** Suzuki2026Heuristic
- **Title:** Weil quadratic form: heuristic discussion only
- **Authors:** Masatoshi Suzuki
- **Year:** 2026
- **URL/DOI/arXiv:** https://arxiv.org/html/2606.09096v3
- **Claim used:** 仮定検査のみ。依存不採用
- **Exact theorem:** Section 7
- **Assumptions:** RH下のheuristic
- **Depends on RH?:** YES
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** 無条件の作用素構成定理とは区別。

## CCLM2014

- **Reference ID:** CCLM2014
- **Title:** Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function
- **Authors:** Emanuel Carneiro and Vorrapan Chandee and Friedrich Littmann and Micah B. Milinovich
- **Year:** 2014
- **URL/DOI/arXiv:** https://arxiv.org/pdf/1406.5462v1
- **Claim used:** 既知kernel最適化の先行結果
- **Exact theorem:** Section 3.5, Corollary 14
- **Assumptions:** Fourier support制限を持つextremal problem。zero correlation側のRH仮定と区別
- **Depends on RH?:** NO
- **Peer-reviewed?:** PREPRINT
- **Verified independently?:** NO
- **Notes:** BUILDERとDESTROYERが原文照合。最適化部分のみ関連。


## MRT2019

- **id:** MRT2019
- **title:** Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges
- **authors:** Kaisa Matomaki and Maksym Radziwill and Terence Tao
- **year:** 2019
- **url:** https://arxiv.org/html/1707.01315v3
- **claim_used:** prime-power joint-symbolへの既存無条件cancellation評価の適用限界
- **exact_theorem:** Section 2.4, (29), Lemmas 2.6–2.7 and following application to Lambda
- **assumptions:** 固定saving exponentと十分大きい固定Bprime。log^Bprime(x)<=|t|<=x^Bprime。定数・閾値の依存を保持
- **depends_on_RH:** NO
- **peer_reviewed:** YES
- **verified_independently:** NO
- **notes:** Proc. Lond. Math. Soc.118 (2019),284–350; DOI10.1112/plms.12181。主張の一次資料照合のみ。全証明未再構成。詳細joint-symbol-prior-art.md。
