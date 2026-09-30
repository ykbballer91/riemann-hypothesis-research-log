**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/desogus-source-dependency.md` · Original SHA-256: `d1a5116960c8782828c21044aab816b9ab47a6053955609fd29b6753947bad32`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Desogus 2609.20367v2 — 一次資料・依存関係・証明書境界

2026-09-29。LITERATURE 担当。**UNVERIFIED EXTERNAL PROOF CLAIM**。主対象は [v2 HTML](https://arxiv.org/html/2609.20367v2) / [v2 PDF](https://arxiv.org/pdf/2609.20367v2)（2026-09-20、69頁）、比較対象は [v1](https://arxiv.org/html/2609.20367v1)（2026-09-17）。査読済みとの根拠は確認していない。全体を skim して依存を抽出したが、全文の独立再証明ではない。著者の証明・PASS・independent という表記を、本プロジェクトの独立検証 YES に移さない。

原資料 hash は root の provenance（原資料参照・公開版未収録: `research/desogus_source_provenance.json`） を参照。番号付き全90項目は [dependency JSON](../../../reports/research/desogus_dependency.json)。75件が theorem/lemma/proposition/corollary、残りは定義・注記・audit・計算証明書。各項目に型、TeX label/行、著者証明の存在、独立検証 NO を分けた。引用参照から生成した辺と、監査者が選別した88本の主要依存辺も分離した。これは形式化済みの完全証明グラフではない。

## 1. 最短の主経路と重点 cut 候補

著者の最終経路は、厳密な局所作用素 → 真の source routing/common cut → inherited response/fold の同一形式への配置 → 全整数の算術余裕 → 帰納 → 全 compact support の奇関数 Weil 正値性 → RH、である。式(63)の局所作用素と、その後に用いる Cauchy–Carleman/collar 形式の完全な一致が前提。

具体的には、6.62（帰納 base）と8.5（帰納 step）から8.6、1.3/1.4による零延長から任意 support、7.1と1.2から8.7/0.1へ進む。8.5の証明は6.53、8.1、6.57、8.2、6.49、8.3、8.4、6.55を組み合わせる。

以下は**表示された MASTER 経路に関する候補単一前提 cut**。別証明不存在や厳密な graph-theoretic 最小性までは認証していない。主結論自身を cut と数える自明な分類は避けた。

| 候補 | 必須の仕事 | 独立監査で残る義務 |
|---|---|---|
| Theorem 1.2 | real odd core で十分という判定 | 変換・conjugation・全 support の量化・零点 tail |
| Proposition 5.3 | 元の Weil 形式と collar model の完全同定 | off-diagonal kernelだけでなく diagonal/killing、domain、closure |
| Corollary 6.29 | 真の harmonic vector の folded operator が6.28の one-defect operator である同定 | 定義した forcing の恒等式から arithmetic forcing の同定へ飛躍しない |
| Theorem 6.53 | ground と transverse に同じエネルギーを二重配賦しない共通 short | 真の source slots/gauge に lower form が同時成立するか |
| Certificate 6.62 | \(a=\frac12\log7\) の無限次元帰納 base | 保存された7×7行列と full operator の間の尾・coupling・正規化 |
| Lemma 8.1 | inherited response の同一 reduced metric への配置 | \(P^{ex}>0\)、stationarity、実際の forcing と comparator debit |
| Certificate 8.3 | 全整数 \(k\ge7\) の aligned scalar margin | finite sweep と \(W_k\)・variance の解析 tail の接合 |
| Lemma 8.4 | common-cut と fold の同じ quadratic contribution への同定 | 二つの arm が同じ target block/coupling を持つ根拠、scalar debit の数 |

**Gate I の位置に注意。** v2 TeX 内で thm:gate1/cor:gate1 の明示参照を全検索すると、2.1→2.3→Audit 2.4で終わる。8.5–8.7の最終経路からの明示依存はない。Audit 2.4も scalar hybrid shell と真の operator pivot を区別する。従って2.1に反例が出ればその命題は破れるが、それだけで最終 MASTER 経路の必須前提が破れたとまでは判定しない。根拠なく Gate I の大規模再計算を最優先にしない。

**閉包の位置にも注意。** compact smooth odd core の各 test に対する非負性が得られれば1.2を直接使える。したがって7.1の global closed-domain extension の不備だけでは、compact-core 経路も破れたとは限らない。

## 2. 既存障害との対応

元の障害は [support flow](../../../audits/proofs/audits/support-propagation-flow-renormalization.md) と [敵対監査](../../../audits/proofs/audits/support-propagation-adversarial.md) にある。

| OUR BARRIER / WHY GENERIC METHOD FAILS | DESOGUS CLAIMED REPAIR / EXACT LOCATOR | ASSUMPTIONS・判定 |
|---|---|---|
| \(A>0,C>0\) でも \(C-B^*A^{-1}B<0\) は可能 | 6.27の exact harmonic graph、8.5の全k coercivity | 8.5を独立に導く必要。Schur identityそのものは新しい正値性を与えない。UNKNOWN |
| gapが小さいと absolute coupling bound は不足 | 6.28の forcing にも defect factor が入る cancellation、6.29/8.4で実際の行へ接続 | 6.28は \(\Pi^{phys}>0\) の条件を持つ。零点への連続性は negative pivot の排除ではない。UNKNOWN |
| 別々に source short した余裕を足すと二重使用し得る | 6.51の \(\mathfrak b=\mathfrak l_0+\mathfrak r\)、6.52、6.53の単一common-complement short | common extension、等長で互いに素な真の source slots が必要。モデル内の予算と真の Weil realization を別に確認。UNKNOWN |
| unitary/gauge 変更だけでは真の form の正値性は増えない | 5.3 full-form transport、6.32 split-unitary short、8.4 | 対角項を含む exact equality が必要。形式名を与えるだけでは十分でない。UNKNOWN |
| 新しい prime translation の差分は一般に不定 | 3.1–3.3で prime-power branches を保ち、6.49、6.55、8.3で negative debit を支払う | 全kで成り立つ量的比較なら回避し得る。固定窓や単なる正のarch tailで置換しない。UNKNOWN |
| finite matrix positive でも infinite tail/coupling が残る | 6.23の真の Schur criterion、6.24、6.62とAppendix A3 | \(QCQ\ge\gamma Q>0\)、\(B=QCP\)、polar vectorを含むPが必要。保存行列の正値性だけでは不足。UNKNOWN |
| 無限次元で \(A>0\) と bounded invertibility は同値でない | 6.1/6.27で \(C_k^{-1},A_k^{-1}\) と最小化を使用 | compact resolvent/gap、cross operator、form domain、inverse rangeを確認。UNKNOWN |

この担当では上記 repair を独立再現していない（全て NO）。UNKNOWN は「偽」と同義ではない。root/Destroyer の反証結果があれば、別監査の結論を明示して統合する。

## 3. Restricted odd criterion は外部の未記載定理ではない

[v2 §1 Theorem 1.2](https://arxiv.org/html/2609.20367v2#S1.Thmtheorem2) に証明が書かれている。量化は全実数値奇関数 \(f\in C_c^\infty(\mathbb R)\)。support 上限を固定しない。中心化 \(F(z)=\int f(y)e^{zy}\,dy,\ \lambda=\rho-\frac12\) の規約で
\[
\mathcal W[f]=\sum_\lambda F(\lambda)\overline{F(-\bar\lambda)}
=-\sum_\lambda F(\lambda)^2.
\]
RH下では各項が非負。逆向きは、実偶 bump の変換 \(\Psi\)、高さT以下の非対象 orbitを消す実偶多項式 \(P_T\)、補間用 \(R_M=a_M+b_Mz^2\) を使い、
\[
F_M(z)=zP_T(z)R_M(z)\Psi(z)^M,\qquad F_M(\lambda_0)=1
\]
を作る。対象 quartet の寄与は負、他の有限 orbit は零、残りの絶対和は \(O(q^{2(M-M_0)})\to0,\ q<1\)。test の support はMとともに増え得る。この点を固定窓の criterion と取り違えない。

既知の入力は explicit formula、零点の対称性、閉帯内の bump transform の一様急減衰、\(N(T)=O(T\log T)\)。この部分の書式上は RHを逆向きの前提にしていない。証明全体の独立検証は NOだが、外部 restricted-odd theorem の欠落という分類は不適切。Weil1952、Guinand1948、Titchmarsh1986等は一般 explicit-formula lineageとして列挙され、1.2固有の外部定理番号は記載されない。

## 4. 外部算術依存の正確な locator

Desogus Lemma3.4、6.42、6.54、8.3の解析tailで使う二つの不等式は、[Dusart, 1002.0442](https://arxiv.org/pdf/1002.0442) の原文で確認した。

- Proposition 3.2: \(x>0\) で \(\psi(x)-\vartheta(x)<1.00007\sqrt x+1.78x^{1/3}\)。
- Theorem 5.2 の表: \(k=2,\eta_2=0.2,x_2=3594641\) の \(|\vartheta(x)-x|<\eta_2 x/\log^2x\)。PDFテキスト抽出では「>」と「≥」が混ざるため、厳密な左端記号は原PDF表示で再照合するか、finite rangeへ左端を含める。

これは RH を仮定する Schoenfeld の \(\sqrt x\log^2x\) 型評価ではない。必要な二式は Dusart の**無条件**命題に存在する。原論文の計算全体の独立検証は NO。Desogus が [7],[17] とまとめて引用すること自体を hidden RH と判定しない。

Feshbach1958、Schur1911、Ando1979、Anderson–Trapp1975は一般 shorting/Schur calculus の出典であり、真の arithmetic coupling の一様支配を供給するものではない。Carleman/Rosenblum/Yafaev、MPFR/Arb/Rumpの引用も、モデルと元のWeil operatorの同定を代替しない。

## 5. v1→v2の確認範囲

両版HTMLの番号付き90項目を照合。数式番号だけの変化を数学的変更と数えない。重要な変更は以下。

- 2.2: \(Y\mapsto m_Y^{(k)}\) の piecewise \(C^1\)・局所絶対連続と整数端点の扱い。
- 2.3: midpoint-shellの導出とsmall-cell条件。
- 6.49: exact mismatch debit と lower-model debit の大小を明記。
- 8.1: inherited line の metric normalization と actual response の定義を明記。
- 8.3: aligned forcing \(W_k\) の解析tailの導出を拡充。
- 8.4: whitened row、two-arm square completion、target diagonalを一回だけ置く説明を拡充。

v2で説明が増えたことは正しさの独立保証ではない。特に8.4の「二つのarmが同じ block/coupling」という actual-operator statement を検証する必要は残る。

## 6. 補足資料・hash・実行境界

arXiv abstractのリンクは [Zenodo DOI 10.5281/zenodo.22864087](https://doi.org/10.5281/zenodo.22864087)。Web readerでは取得失敗したが、公開 [Zenodo API](https://zenodo.org/api/records/22864087) を保存して確認できた。

- record version: 2.0.0、publication date: 2026-09-20、metadata modified: 2026-09-22。
- license: MIT。arXiv:2609.20367v2 への isSupplementTo が明示される。concept DOI は10.5281/zenodo.22799712。
- [公開ZIPのdownload URL](https://zenodo.org/api/records/22864087/files/The_Three_Gates_Supplementary_V2.zip/content)。
- 保存: literature/source_cache/desogus-The_Three_Gates_Supplementary_V2.zip。
- 2,171,846 bytes、213 members、展開サイズ3,236,562 bytes。
- SHA256: c46356c7961dba2651a22000564652779f6153eb8ecfcd8250208dd8a95106d1。
- MD5: b8578e91c83162299b09a1fa39bfde7f。APIの公開MD5と一致。
- ZIP内のSHA256SUMSの185ファイルをzip bytesから再計算し、全て一致、missing/mismatchなし。これは完全性検査であって数学的証明書検証ではない。
- この担当は ZIP の読取とハッシュ計算のみ。著者プログラムは実行していない。

| proof-critical対象 | ZIP内相対パス | 実際の範囲 |
|---|---|---|
| 全体の索引 | CERTIFICATE_LEDGER.md / REPRODUCIBILITY.md / run_core_verification.sh | 作者の実行指示・対象の列挙 |
| 6.62 base | Y7_base/y7_frozen_certificate.json / verify_y7_frozen_certificate_exact.py | 保存された7×7 interval familyの有理数Gershgorin等 |
| 6.42 AWGC | arithmetic/awgc/awgc_interval_verifier.cpp | finite \(k\le3594641\) |
| 6.54 | master/fresh_mertens_log_bound.cpp | finite Mertens/log |
| 6.55 | master/master_safe_cut_interval_verifier.cpp | finite \(7\le k\le4999\) |
| 8.3 | master/master_aligned_safe_interval_verifier.cpp | finite aligned scalar envelope |
| 第二tail stream | independent_checks/tail/tail_cleanroom_cert.cpp | 作者が提供する別実装による十分tail比較 |
| Gate-II監査 | independent_checks/gateII/GATEII_FULL_COMB_SCALARIZATION_AUDIT_2026-09-19.md | full-prime-comb scalarization という特定攻撃だけの監査 |

小さな重要ファイルのSHA256:

- verify_y7_frozen_certificate_exact.py: 9a6c524149e373f14f8afbd9695345f3969699fbb9972f5b3a07fcec3384d5ac
- master_aligned_safe_interval_verifier.cpp: 7568e249538bd8b4cc075f305dc96cf07fe2448b2a3545eba87987abaee6b13a
- master_safe_cut_interval_verifier.cpp: 2fc74ff3f672194a2d0c7a9798f96f86dc586e8333a2e82ff41dfe12af2cea30

再現命令は REPRODUCIBILITY.md にあり、厳格C++ flagsは -O2 -std=c++17 -fno-fast-math -ffp-contract=off -frounding-math。例えば aligned verifier をcompile後、引数3594641で実行する。現担当での未実行を作者ログのPASSで置換しない。

### 静的に見つかった証明書の限界

1. Y7_base/HISTORICAL_INPUT_LEDGER.md は、terminal producer が参照する12直接入力のうち結果ファイル以外の11 transient inputs が配布されていないと明示する。保存行列を検査するだけなら不要でも、元のoperator→interval matrixの完全再生成には別 stream の全誤差保証を検査する必要がある。
2. Y7_end_to_end/scripts/exact_ldl_direct_relative.py は NumPy 配列を対称化し17桁decimal化してからFraction LDLを行う。その正値性は保存された丸め行列について厳密である。元の無限次元operatorやproducerの丸め誤差を含む interval family の証明と同義ではない。README自体も corroborating route と区別する。
3. master_safe_cut_interval_verifier.cpp の cost 上界計算は、概略 \(term=up(num/up(n\,L_{lo}))\)。分母を上へ丸める向きは商の**下**方向であり、外側の一回の up が全誤差を補償する別証明は静的読取では見つからない。\(d_0=0.422785L\) のdecimal定数の外向き包含も明示されない。これは数値余裕が負という反証ではなく、claimed rigorous upper bound の実装保証に関する検査点。独立Arb/有理数実装で修復可能か調べる。
4. 同梱 Gate-II audit は、2026-09-16の別TeX名とSHA256 48ecf5a8b9d28944cd7c822c258e806b901fb89b777df20ef10ceacbd22e57f7 を対象とする。現在v2 TeXのhashとは異なる。さらに文書は full-comb scalarization だけの監査で、全定理の再証明ではないと明記。外部第三者の承認や本プロジェクト独立検証とみなさない。

## 7. 直近30日の限定frontier確認

2026-09-29取得。対象期間は2026-08-30〜09-29、arXivのRH/Weil/canonical/spectral関連検索と一次abstractの照合。全新着を列挙した網羅監視ではない。

| 一次資料 | 分類・今回の確認限界 |
|---|---|
| [Desogus2609.20367](https://arxiv.org/abs/2609.20367), Sep17/20 | DIRECT proof claim。本ノートの優先対象 |
| [Caceres2609.28529v1](https://arxiv.org/abs/2609.28529v1), Sep22 | DIRECT proof claim。Dirichlet discrepancyの漸近balanceからRHを主張。abstractのみ、未監査。journal referenceがあるだけで妥当性を承認しない |
| [Silva2609.25564v1](https://arxiv.org/abs/2609.25564v1), Sep22 | finite Rodriguez–Villegas approximantsの局所一様収束を主張。abstractのみ。有限零点locationやRHを自動補完しない |
| [Kazin–Kadyrov2609.29898v1](https://arxiv.org/abs/2609.29898v1), Sep24 | tempered xiのoff-axis zerosによる別予想の反例。ζそのもののRH反証ではない。abstractのみ |
| [Mishra–Sarkar2609.26787v1](https://arxiv.org/abs/2609.26787v1), Sep22 | Robin型finite arithmetic expressionの全n不等式とRHの同値性を主張。有限計算で全nを認証したという意味ではない。abstractのみ |

これらの存在は確認したが、Desogusの核心監査を中断して全件全文へ広げない。新規性・RH解決を主張しない。

## 8. 番号付き全項目の分類索引

以下は本文中の項目存在と型の索引。new analytic theorem は「この論文で扱う解析命題」という作業分類であり、新規性や正しさの判定ではない。全行の独立検証は NO。詳細の証明存在フィールドと引用参照はJSONに保存。


| 番号 | 原文項目 | 型 | 著者証明の存在 |
|---|---|---|---|
| 0.1 | Theorem 0.1 (Main theorem). | 解析, 同値判定 | YES_PROOF_TEXT_PRESENT_IN_SECTION_7 |
| 1.1 | Theorem 1.1 (Weil positivity criterion). | 一般既知代数, 外部引用, 同値判定 | EXTERNAL_RESULT_STATED |
| 1.2 | Theorem 1.2 (Restricted odd Weil criterion). | 同値判定, 解析 | YES_PROOF_TEXT_PRESENT |
| 1.3 | Lemma 1.3 (Exterior-harmonic cancellation). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 1.4 | Lemma 1.4 (Cofinal-support reduction). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 2.1 | Theorem 2.1 (Global cellular covariance theorem). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 2.2 | Lemma 2.2 (Uniform derivative tail). | 解析, 極限/帰納 | YES_PROOF_TEXT_PRESENT |
| 2.3 | Corollary 2.3 (Gate I: midpoint shell). | 解析 | YES_PROOF_TEXT_PRESENT |
| 2.4 | Audit statement 2.4 (Scope of Gate I). | 範囲注記 | NOT_APPLICABLE |
| 3.1 | Lemma 3.1 (Exact full-space unit-cell decomposition). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 3.2 | Lemma 3.2 (Divisor partial-isometry square). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 3.3 | Lemma 3.3 (True affine translation identity). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 3.4 | Lemma 3.4 (Unconditional Chebyshev capacity). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 4.1 | Lemma 4.1 (Feshbach reserve and primal target diagonal). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 4.2 | Lemma 4.2 (OSPR inequality). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 4.3 | Lemma 4.3 (Analytic one-defect inequality). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 5.1 | Lemma 5.1 (Cauchy–Carleman kernel transport). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 5.2 | Lemma 5.2 (Exact cancellation of the regular gamma kernel). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 5.3 | Proposition 5.3 (Transport of the complete quadratic form). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.1 | Lemma 6.1 (Root-lift and associative shorting). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.2 | Lemma 6.2 (Variational formula for the true rooted load). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.3 | Lemma 6.3 (Polar moment identity). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.4 | Lemma 6.4 (Ground–reflection representation of the polar vector). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.5 | Remark 6.5. | 範囲注記 | NOT_APPLICABLE |
| 6.6 | Lemma 6.6 (Source/target ground-line invariance). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.7 | Lemma 6.7 (Exact root-adapted fibre normalization). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.8 | Lemma 6.8 (Exact endpoint Möbius nesting). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.9 | Lemma 6.9 (Edge-local gauge covariance). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.10 | Audit statement 6.10 (What edge-local covariance does not prove). | 範囲注記 | NOT_APPLICABLE |
| 6.11 | Audit statement 6.11 (Compatibility limit of the root-adapted normalization). | 範囲注記 | NOT_APPLICABLE |
| 6.12 | Lemma 6.12 (Exact common-cell unitary and true ground profile). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.13 | Lemma 6.13 (DFT-compatible mean/mean-zero splitting). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.14 | Corollary 6.14 (Familywise DFT-compatible ground splitting). | 解析, 作用素/domain | ASSERTED_OR_DEFERRED |
| 6.15 | Audit statement 6.15 (Scope of the common-residue splitting). | 範囲注記 | NOT_APPLICABLE |
| 6.16 | Lemma 6.16 (Fixed-target branch gauge). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.17 | Lemma 6.17 (Two-source mean-zero interaction). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.18 | Analytic certificate 6.18 (Parent/source mean capacity). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.19 | Corollary 6.19 (Weighted Laplacian on the source means). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.20 | Theorem 6.20 (Coherent multi-source capacity). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.21 | Corollary 6.21 (Source-resolved transverse Feshbach bound). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.22 | Audit statement 6.22 (What CMC closes, and what it does not). | 範囲注記 | NOT_APPLICABLE |
| 6.23 | Lemma 6.23 (True-core finite Schur criterion). | 同値判定, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.24 | Corollary 6.24 (True-core endpoint Krylov–Radau criterion). | 同値判定, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.25 | Remark 6.25 (Already proved tail mechanism). | 範囲注記 | NOT_APPLICABLE |
| 6.26 | Lemma 6.26 (Sherman–Morrison root residual). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.27 | Lemma 6.27 (Exact full-operator harmonic graph). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.28 | Lemma 6.28 (Exact post-short scalar cancellation). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.29 | Corollary 6.29 (FOLD-FORCING on the full-operator harmonic graph). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.30 | Lemma 6.30 (Sharp true-ground rotation of the one-defect bound). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.31 | Lemma 6.31 (Shorting covariance under a split unitary). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.32 | Corollary 6.32 (Exact physical/arithmetic short intertwining). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.33 | Lemma 6.33 (Exact true-metric nested Schur identity). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.34 | Lemma 6.34 (Exact Green representation of the residual ground scalar). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.35 | Definition 6.35 (Exact Green-root condition). | 同値判定 | NOT_APPLICABLE |
| 6.36 | Theorem 6.36 (Exact one-step Green-root closure). | 同値判定, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.37 | Lemma 6.37 (Second Sherman–Morrison reduction to one vector). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.38 | Lemma 6.38 (Hyperbolic-sine terminal scalar inequality). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.39 | Corollary 6.39 (Exponential two-scale form). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.40 | Remark 6.40 (Equivalent monotonicity formulation). | 範囲注記 | NOT_APPLICABLE |
| 6.41 | Audit statement 6.41 (Scope of the terminal scalar closure). | 範囲注記 | NOT_APPLICABLE |
| 6.42 | Proposition 6.42 (Arithmetic weighted-ground certificate). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 6.43 | Certified finite computation 6.43 (Finite AWGC interval run). | 計算支援, 有限計算, 区間証明書 | CLAIMED_CERTIFICATE_APPENDIX_A |
| 6.44 | Theorem 6.44 (AWGC operator lift). | 解析, 作用素/domain | DEFERRED_TO_COROLLARY_6.49 |
| 6.45 | Corollary 6.45 (Arithmetic mismatch reserve). | 解析, 作用素/domain | ASSERTED_OR_DEFERRED |
| 6.46 | Lemma 6.46 (Exact inherited-ground two-scale surplus). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.47 | Theorem 6.47 (MASTER double-load scalar budget). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 6.48 | Lemma 6.48 (Exact short of the one-defect lower form). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.49 | Corollary 6.49 (Uniform mismatch gap and operator AWGC lift). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.50 | Lemma 6.50 (Universal pair-deficit capacity). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 6.51 | Lemma 6.51 (Exact baseline/residual split of the one-cell form). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.52 | Theorem 6.52 (Residual coherent capacity with free source means). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.53 | Theorem 6.53 (Simultaneous ground/transverse common-cut lower form). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.54 | Lemma 6.54 (Independent logarithmic endpoint bound). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 6.55 | Theorem 6.55 (Safe transverse reserve for MASTER). | 計算支援, 区間証明書, 解析 | YES_PROOF_TEXT_PRESENT |
| 6.56 | Lemma 6.56 (Rational parent estimate). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.57 | Lemma 6.57 (Sharp MASTER mixed block). | 解析 | YES_PROOF_TEXT_PRESENT |
| 6.58 | Lemma 6.58 (True inherited-line surplus). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.59 | Lemma 6.59 (Mixed inherited–mismatch block). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.60 | Lemma 6.60 (Harmonic-vector identification). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.61 | Lemma 6.61 (Fold remainder on the identified harmonic vector). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 6.62 | Certified finite computation 6.62 (Arithmetic base at Y=7Y=7). | 計算支援, 有限計算, 区間証明書 | CLAIMED_CERTIFICATE_APPENDIX_A3 |
| 7.1 | Lemma 7.1 (Odd-channel compatibility and closure). | 閉包, 極限/帰納, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 8.1 | Lemma 8.1 (Exact inherited-response placement). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 8.2 | Lemma 8.2 (Homogeneous aligned-forcing penalty on the exact parent block). | 一般既知代数, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 8.3 | Certified finite computation 8.3 (Aligned MASTER scalar margin). | 計算支援, 有限計算, 区間証明書 | CLAIMED_CERTIFICATE |
| 8.4 | Lemma 8.4 (Exact common-cut/fold intertwining (MASTER-P3)). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 8.5 | Theorem 8.5 (MASTER coercivity on the exact harmonic graph). | 解析, 作用素/domain | YES_PROOF_TEXT_PRESENT |
| 8.6 | Corollary 8.6 (Gate II induction). | 解析, 極限/帰納 | YES_PROOF_TEXT_PRESENT |
| 8.7 | Theorem 8.7 (Odd Weil positivity and the Riemann hypothesis). | 解析, 同値判定 | YES_PROOF_TEXT_PRESENT |
| 8.8 | Remark 8.8 (Closure of the MASTER dependencies). | 範囲注記 | NOT_APPLICABLE |

## 9. 独立数学監査からの追記（同日、上の棚卸し後）

この節は担当者別の独立監査を統合する。初期90項目の NO は文献担当の棚卸し時点を保持し、JSONの audit_findings に検証範囲付き結果を別記した。

- [Gate III監査](../../../audits/proofs/audits/desogus-gate3.md): Theorem1.2は独立再導出YES。1.3のsmooth-core cancellation、1.4と8.6のcofinal-support含意は条件付きYES。7.1のradius independenceも条件付きYES。通常global L²でのclosureはFAILEDだがcompact-core経路に不要。原文にLemma1.5はないため、番号を推測追加していない。
- [Gate II監査](../../../audits/proofs/audits/desogus-gate2.md): 6.48のlocal rank short、6.53のone-cell共通予算はモデル内でYES。8.1/8.2のscalar algebraはYES。実際のWeil operatorへのplacementはNO。
- 6.29→8.4→8.5には proof-critical GAP。6.28の恒等式だけではpositive physical pivotを供給しない。また8.4の表示された二armを消去するとdebitは2D、8.5へ渡す非負残差はQ−D。原文と同じQ,Dなら追加のDが残る。この不足を3担当が独立確認した。実Weilの負方向やRH反証を意味しない。
- [root計算・修復監査](../../../audits/proofs/audits/desogus-computation-and-repair.md): 印刷された7×7 interval familyのFraction正値性はYES、operator assemblyはNO。9個の選択kでのArb scalar値はYES、全kはNO。
- [safe-cut修復結果](../../../../artifacts/experiments/results/desogus-safe-cut-repair.json): 元C++の丸め疑義に対し、独立192bit Arbで全4993件（7≤k≤4999）を認証。最小下界はk=7で1.5202196525197510393。有限componentは修復済み。解析tailとactual-operator bridgeの欠落を閉じたとは扱わない。

最短の残り課題は、同じ算術的Weil作用素に対するfoldの正確なdebit ledgerと未使用reserveを導出すること。有限数値の精度改善だけでは、この論理cutは縮まらない。RHはOPEN。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/desogus-safe-cut-repair.json`](../../../../artifacts/experiments/results/desogus-safe-cut-repair.json)
- [`proofs/audits/desogus-computation-and-repair.md`](../../../audits/proofs/audits/desogus-computation-and-repair.md)
- [`proofs/audits/desogus-gate2.md`](../../../audits/proofs/audits/desogus-gate2.md)
- [`proofs/audits/desogus-gate3.md`](../../../audits/proofs/audits/desogus-gate3.md)
- [`proofs/audits/support-propagation-adversarial.md`](../../../audits/proofs/audits/support-propagation-adversarial.md)
- [`proofs/audits/support-propagation-flow-renormalization.md`](../../../audits/proofs/audits/support-propagation-flow-renormalization.md)
- [`research/desogus_dependency.json`](../../../reports/research/desogus_dependency.json)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/desogus-The_Three_Gates_Supplementary_V2.zip` — SOURCE REFERENCE NOT INCLUDED
- `research/desogus_source_provenance.json` — SOURCE REFERENCE NOT INCLUDED
