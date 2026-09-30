**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/local_global_zero_confinement_adversarial.md` · Original SHA-256: `3674251579b8a19b71bfae82470b832a1e3c5702b7079c66d30ded066bc17116`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Local-to-global zero confinement: independent final audit

2026-09-30。担当 DESTROYER。RH OPEN。新規数学結果の優先権を主張しない。
今回の作成対象はこの新規ファイルのみ。既存ノート・旧state・主proof graphは変更していない。

## 1. 監査対象と実施範囲

対象は以下の現行ノートと統合表である。

- [spectral approximants / exact gap](../../../reports/research/local_to_global/notes/spectral_approximants_and_exact_gap.md)：全文読取と指定式の独立再計算。
- [local RH / Sauvalle](../../../reports/research/local_to_global/notes/local_rh_and_sauvalle.md)：読取。特に LA1.3 の境界不等式、LA5 の単位円代入・零点次数・RH同値を独立検算。
- [theorem stack](../../../reports/research/local_global_theorem_stack.md)：全文読取、Hurwitz・規格化・量化を監査。
- [candidate matrix](../../../reports/research/local_global_candidate_matrix.md)：全文読取、採否・旧trackとの区別を監査。
- 自担当の [convergence destroyer](../../../reports/research/local_to_global/notes/convergence_destroyer.md)：一般反例と actual 固定head検査の詳細。
- 最終追加の [主報告](../../../reports/research/local_to_global_zero_confinement.md)、
  [state JSON](../../../../data/source-records/research/local_global_state.json)、
  [完了報告](../../../reports/research/local_to_global/completion_report.txt)：全文読取。
  既監査の式との整合、成功範囲、ES・比較の未証明性、反例の射程を照合した。
  この追加レビューを、全引用原典の再読や数値実験の独立再実行とは扱わない。

原典確認は限定的である。CCM arXiv:2511.22755v1 の Theorem5.10、Lemma5.9、
§§7–8、Borcea–Brändén の指定 stability/Lee–Yang 定理、Bornemann の determinant 連続性評価、
Śliwiński arXiv:2601.12133v1 の対象定義と Theorem3.1 を該当箇所で確認した。
local RH I/II・Sauvalle・Sonin・CvS の全原典を本担当が再読したとはしない。
それらの原典照合の範囲は各専門担当ノートの記録に依拠し、以下では計算の独立検算と区別する。

判定語の意味：

|判定|意味|
|---|---|
|PASS|明示された限定範囲で、式・論理を独立確認した。論文全体の認証ではない。|
|CONDITIONAL|引用定理または標準定理の前件を維持した含意として妥当。前件の actual 成立とは別。|
|OPEN|必要な actual 評価または構成を今回得ていない。偽と断定していない。|
|REJECT|指定された短絡推論を採用しない。一般反例・対象不一致・未供給の橋を理由として区別する。|

## 2. 判定表

|対象|判定|限定・根拠|
|---|---|---|
|ES を前件とする CCM 実零点定理と determinant identity|CONDITIONAL|最小固有値が単純、ground vector が偶。有限商＋無限tailの正則化determinantである。|
|必要な cofinal 経路で ES が成立|OPEN|有限数値・prolate の even-simple 性を actual Weil ground へ移していない。|
|ground族とprolate proxy族の区別|PASS|前者の実零点性と後者の算術的収束を、同一対象の性質として合算していない。|
|prolate→Hermite estimate|CONDITIONAL|原典の指定次数・規格化で引用採用。元の prolate 漸近定理全体を本担当が再証明したものではない。|
|表示された h の Mellin transform の factor 1/4|PASS|Gamma積分を独立計算。値規格化で解消される技術的定数修正。|
|proxyのGaussian tailを加えた収束評価|PASS（引用sup estimateを前件）|省略された nu>λ の項を指数的に小さい尾として加えれば整合する。|
|正規化 actual ground と proxy の compact 比較 G*|OPEN|具体的な残差/gap/weighted comparison は未供給。|
|N/logλ→∞ の必要性|PASS|未変更格子零点の稠密化と恒等定理。十分条件ではない。|
|actual N=0 の非正規族性|PASS|一点規格化後にも strip 内で指数的に発散する点が存在。|
|Hurwitz/Rouché による strip 内の接続|CONDITIONAL|actual ground族の複素compact一様収束と非零極限を前件とすれば、RHへ届く。|
|norm-resolventだけからtarget determinant収束|REJECT|高域の多数の固有値が非消失Gaussian因子を残す厳密例がある。|
|Sauvalleの具体式におけるoff-line multiplicity保存|PASS（表示された大域公式を前件）|C₂の零点位置を独立計算。局所補正がζの線外零点を除去しない。|
|local RHだけからglobal confinement|REJECT|局所・大域の対象が違い、具体式にはcompleted ζが残る。局所定理自体は棄却しない。|
|一様gapの正下界が不可欠という主張|REJECT|必要なのは残差/gap と窓依存損失の総合評価。一様gapは便利な十分入力にすぎない。|
|3方向の限定監査 Level1、RH OPEN という統合分類|PASS|新しいactual global arithmetic bridgeを証明したという記述はない。|

## 3. ES、正規化、収束対象

\(\mathscr X(z)=\xi(1/2+iz)\)、\(S=\{|\Im z|<1/2\}\)、\(z_*=i/4\) とする。
\(\mathscr X(z_*)=\xi(1/4)>0\) はRHによらない。
CCM の exact identity を \(\Delta_{\lambda,N}\) と書けば
\[
 \Delta_{\lambda,N}(z)=-i e^{-iz\log\lambda}\widehat v_{\lambda,N}(z),
\quad
 e^{i(z-z_*)\log\lambda}
 \frac{\Delta_{\lambda,N}(z)}{\Delta_{\lambda,N}(z_*)}
 =\frac{\widehat v_{\lambda,N}(z)}{\widehat v_{\lambda,N}(z_*)}.
\]
ES のもとで右辺分母は非零。偶性だけから \(\widehat v(0)\ne0\) とは言えない。
また raw determinant は定数倍だけでなく、表示された非消失phaseも補正する。
この演算は零点を保存するが、actual \(\mathscr X\) への収束を証明するものではない。

印刷された
\(h(x)=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2}\) について
\[
 \mathcal Mh(s)=\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2),\qquad
 \widehat{\mathcal Eh}(z)=\mathscr X(z)/4.
\]
従って値規格化した proxy の極限は正しく \(\mathscr X/\mathscr X(z_*)\) になる。
これは修復可能なスカラー差であり、原論文全体の反証にはしない。
真の ground transform と proxy transform が同じ極限を持つ評価 G* は、なお別の未解決入力。
ESを満たす列の存在も G* の複合命題内に明示して残す。

## 4. 二変数経路と正規族性の量化

tail零点は \(\pi k/\log\lambda\), \(|k|>N\)。
\(\lambda_j\to\infty\)、\(N_j/\log\lambda_j\le C\) の部分列があるなら、
任意 \(x>\pi C\) に tail零点が近付く。
非零compact一様極限はこの実区間上で全て0になり、恒等定理に反する。
したがって \(N_j/\log\lambda_j\to\infty\) は必要。

actual \(N=0\) では1次元制限のgroundは定数でESを満たし、\(a=\log\lambda\) として
\[
 f_a(z)=\frac{\sin(az)/z}{4\sinh(a/4)},\qquad f_a(i/4)=1.
\]
実軸の各固定点では \(f_a\to0\) だが
\[
 f_a(2i/5)=\frac58\frac{\sinh(2a/5)}{\sinh(a/4)}\longrightarrow+\infty.
\]
全零点実数・偶・一点規格化は複素stripの正規族性を含意しない。
この反例は fixed-head 経路だけを棄却し、適切な cofinal 経路の可能性は残す。

**量化の訂正：RESOLVED。** 初回読取で theorem stack の C-actual 行にあった
「全窓について normal family / OPEN」という表現は、全 \((\lambda,N)\) 族と
読むと上の \(N=0\) 例に反するため訂正を依頼した。
最終差分では「ESを満たす適切な cofinal 経路上」の評価を OPEN とし、
全パラメータ族の normality を FALSE と明記していることを独立に確認した。
完了報告も同じ二つを区別している。この指摘に未解決の修正要求は残っていない。

## 5. Hurwitz と determinant の独立検査

全actual零点が無条件に \(S\) 内にあるため、全平面での収束は不要。
仮の非実零点を囲む小円板を \(S\setminus\mathbb R\) に取り、境界上の
\(\min|\mathscr X|>0\) と compact一様収束から Rouché を使えば、
近似にも同じ正の個数の非実零点が必要になり矛盾する。
多重零点も含む。有限格子の値、実軸だけの収束、leading countingだけでは代替できない。

norm-resolvent と determinant の区別には、\(Ae_k=ke_k\) on \(\ell^2\) を用いた。
\(A_j\) は \(j<k\le j+j^2\) の固有値のみ \(j\) へ変更する。
\[
 \|(A_j-i)^{-1}-(A-i)^{-1}\|\le2/j,
\quad
 \det(I-z^2A_j^{-2})
 \longrightarrow e^{-z^2}\frac{\sin\pi z}{\pi z}.
\]
target \(\det(I-z^2A^{-2})=\sin(\pi z)/(\pi z)\) と違う。
各固定低固有値の一致、原点での値1も満たす。
\(\|A_j^{-2}-A^{-2}\|_1=1-O(1/j)\) が高域の欠けた評価を示す。
これは actual CCM の反例ではなく、一般的な determinant同定の短絡だけへの反例。
trace-norm収束等を追加すれば正の連続性定理は使える。

## 6. Sauvalle と local shift-strip の独立計算

LA1.3 の多項式補題では、\(\Re z\ge c>0\)、\(|\Re r_j|\le c\) から
\[
 |z+2-r_j|^2-|z-2-r_j|^2=8\Re(z-r_j)\ge0,
\quad |z+a|^2-|z-a|^2=4a\Re z>0.
\]
先頭因子が境界でも厳密性を与える。最高次係数 \(4d+2a\) も正しい。
有限次数・最大零点実部の達成・同じ多項式を返す差分固有方程式が前提である。
actual \(\xi\) に同じ式が成立するとは扱っていない。

Sauvalle の担当ノートの具体式は
\[
 \Xi_f(s)=e^{-\pi is/4}C_2(s)\frac{2\xi(s)}{s(s-1)},\qquad
 C_2(s)=2^{1-s}-1+e^{\pi i/4}(2^s-1).
\]
\(w=2^s,\eta=e^{\pi i/4}\) として
\(wC_2=\eta w^2-(1+\eta)w+2\)。
\(w=\sqrt2e^{-\pi i/8}v\) の代入で
\(2[v^2-\sqrt2\cos(\pi/8)v+1]\) となり、両根は単位円上。
従って \(C_2\) の全零点は \(\Re s=1/2\)。
線外の非自明 \(\rho\) では他因子に零点・極がなく
\[
 \operatorname{ord}_\rho\Xi_f=\operatorname{ord}_\rho\xi
 =\operatorname{ord}_\rho\zeta.
\]
この固定 \(\Xi_f\) の全零点拘束はRHと同値であって、独立な弱い局所入力ではない。
local RH・Tate接着公式そのものを棄却していない。

## 7. 保存検査と独立性

`research/local_to_global/preservation_baseline.json` の343個の SHA-256 を
本担当が read-only Python で全件再計算した。
**checked=343、changed=0、missing=0**（本監査作成直前のsnapshot）。
旧ファイル保存の検査であり、新ノートの数学的正しさの証明ではない。
逆に数学的PASSが旧ファイル保存を自動的に保証するわけでもない。

読取snapshotのハッシュは以下。rootによる今回新規ノートの後続修正は別snapshotとなる。

|対象|SHA-256|
|---|---|
|spectral_approximants_and_exact_gap.md|`85bbf79309ea9a4583161dd2a9f0151cb6071ae70b1a70bcdae252f515552b52`|
|local_rh_and_sauvalle.md|`dfb86d165f6a581ec6d4361a29b25e8f89fcbfc965397cd7745adbe655d18eaf`|
|local_global_theorem_stack.md|`5fedb88350517a9a624364cfae31c2309896e4fa9b70409fa010b5a2789fc93e`|
|local_global_candidate_matrix.md|`dd087ae746db8960c1ce20e919bd5b019d9edc86a51bd49932189408bb2c70cc`|

**総合判定：指定された一般論と個別計算は限定 PASS、actual 接続は CONDITIONAL / OPEN。**
root の Level1・新しいglobal arithmetic bridge未達・RH OPEN という結論は妥当。
本監査の反例からRH、CCMの条件付き定理、局所RH定理、原論文全体の偽は導かない。

## 8. 最終3成果物への追加レビュー

主報告・state・完了報告は、(i) ES が未証明、(ii) 実零点族と収束族は別、
(iii) 値規格化した G* は未証明、(iv) 条件付き Hurwitz 接続のみ完成、
(v) 新規性を主張しない既知入力の採用、(vi) Level1・RH OPEN、の各点で一致する。
state JSON の構文も確認した。`new_external_input_found=true` は既知成果を今回採用した意味で、
新定理や新しいglobal bridgeの証明という意味ではないことが明記されている。

追加レビューは **PASS：重大な過大主張・対象の混同・成果物間の矛盾を認めなかった**。
CCM の条件付き定理を無条件へ強めず、Sauvalle の零点次数一致をRH解決とせず、
固定 \(N=0\) や一般作用素の反例を全ての許容極限経路への不可能性へ広げていない。
trace/Schatten制御への言及は determinant連続性を使う経路の入力として読み、
同じノートが示す直接の weighted Fourier比較を禁止する必要条件とは読まない。

最終読取snapshot（前節の初回snapshotとは区別）：

|対象|SHA-256|
|---|---|
|local_global_theorem_stack.md（量化修正後）|`20ecc6491f31f4ce26bab5f4d988dca557aa00891558ecddac8d93f767bf5d21`|
|local_to_global_zero_confinement.md|`c03f9001c9082a2e49feeba78453320c8aef71ce1e7e379c7245145fc032420e`|
|local_global_state.json|`c29395763e79acae653d02c5f3dae90b266a00ed4117fc9d7dc7e934e865711c`|
|local_to_global/completion_report.txt|`1426f8246662291dc23146f1c2817b34a43bf5a2d4441ac57330b33631454fea`|

最終全体のHEAD・リンク・保存基準の再照合はrootの別検証である。
本担当が独立に実施した保存検査は前節の343件snapshotであり、責任範囲を混ぜない。

## 9. 重複監査と量化の限定差分レビュー

最終レビュー後の指定差分だけを追加読取した。旧
`research/notes/accumulation_spectrum.md` §4 は read-only で参照し、
CCM Theorem5.10、CvS Theorem6.1、CCM §8 の二つのmissing stepsが
既に記録されていることを本担当も確認した。
今回の main・state・matrix・report・root note は、それらを未使用の新入力や
新発見と数えないよう限定している。**重複・優先権の限定は PASS。**

`new_external_input_found=true` の現在の射程は、旧§4で式として追跡されなかった
CCM Lemmas7.2–7.3 の prolate/Hermite と proxy変換の具体的estimateである。
これは既知文献の今回の追加利用を示すにとどまり、新定理・新しいRH入力・
研究全体で未曾有の結果という意味ではない。
この確認は指定旧§4との比較であり、全旧文書をもう一度検索したという主張ではない。
以前のsnapshotでより広く読めた表現については、この最終限定を優先する。

root note の \((W_r)\) は `for every \(0<r<1/2\)` へ明確化された。
\(C_r\lambda^r\|e\|_2\) を用いる条件と整合し、\(r=0\) の定数を
無断で同一視しない。この変更は比較命題の証明を追加したものではない。
RH OPEN、G* OPEN、達成Level1という数学的判定は変わらない。

限定差分レビュー後のsnapshot：

|対象|SHA-256|
|---|---|
|local_to_global_zero_confinement.md|`3a49635eba861518f4ca21177c0983e013c0679bc466eab3b6b6a4fa0a85d816`|
|local_global_state.json|`4ba6b5027bf8aec5b923ef60f86fd42f9cd3b756285bc8ec2c1a7c5c875b38e0`|
|local_global_candidate_matrix.md|`b8cfc07a522237455a99e4b943cc9871b3494002fab95fcc78ec46afde908248`|
|local_to_global/completion_report.txt|`b10ca2c90c58a2424d2b780931d41efff2c9b64a045f6fd1ecc90ce804840cba`|
|local_to_global/notes/spectral_approximants_and_exact_gap.md|`1619fb9bab24a8637a1fe6549ed23871141cd0c895049dab8fe4b9506f87174b`|
|旧 notes/accumulation_spectrum.md（参照のみ）|`ec58731301fff14f9efef0cab39852ef5a1e784e15c963496c44304c8f26139c`|

本担当の編集は今回新規の本audit末尾への追記のみ。追加の未解決訂正要求はない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/local_global_candidate_matrix.md`](../../../reports/research/local_global_candidate_matrix.md)
- [`research/local_global_state.json`](../../../../data/source-records/research/local_global_state.json)
- [`research/local_global_theorem_stack.md`](../../../reports/research/local_global_theorem_stack.md)
- [`research/local_to_global/completion_report.txt`](../../../reports/research/local_to_global/completion_report.txt)
- [`research/local_to_global/notes/convergence_destroyer.md`](../../../reports/research/local_to_global/notes/convergence_destroyer.md)
- [`research/local_to_global/notes/local_rh_and_sauvalle.md`](../../../reports/research/local_to_global/notes/local_rh_and_sauvalle.md)
- [`research/local_to_global/notes/spectral_approximants_and_exact_gap.md`](../../../reports/research/local_to_global/notes/spectral_approximants_and_exact_gap.md)
- [`research/local_to_global_zero_confinement.md`](../../../reports/research/local_to_global_zero_confinement.md)
- [`research/notes/accumulation_spectrum.md`](../../../reports/research/notes/accumulation_spectrum.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/local_to_global/preservation_baseline.json` — SOURCE REFERENCE NOT INCLUDED
