**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global_zero_confinement.md` · Original SHA-256: `3a49635eba861518f4ca21177c0983e013c0679bc466eab3b6b6a4fa0a85d816`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Local-to-global zero confinement / adelic gluing

2026-09-30。限定監査完了。**RH OPEN。達成 Level 1。**
既存研究・state・proof graphは変更せず、本トラックからmergeしない。

## 1. 結論

局所RHが成功する理由は、特別な算術的入力のMellin変換が、
正測度に関する直交多項式、または同等の局所的な零点拘束恒等式に帰着すること。
局所自己共役性だけが理由ではない。

有限段階のConnes構成では、**単純かつ偶なground stateという前件 ES**の下で、
そのFourier変換の全零点が実数になる。ESを必要な全段階で証明したわけではない。
一方、actual \(\xi\) への収束評価があるのは、別に構成されたprolate近似関数である。

したがって正確な切断点は、
**実零点性を持つ真のWeil ground stateと、\(\xi\) への収束が分かるprolate近似関数との、
正規化した複素変換の比較評価がないこと**である。以下で関数列・規格化・位相を固定する。
新しい全域零点評価を得たとは主張しない。

## 2. Local RH の proof-critical mechanism

### 実数体：Hermite → Mellin直交多項式

Bump–Choi–Kurlberg–Vaaler の指定Hermite関数のMellin変換は、
Gamma因子と有限多項式の積になる。同じparityのHermite関数の直交性を
Mellin-Plancherelで移すと、臨界線上で
\[
 |\Gamma(1/4+it/2)|^2\,dt
 \quad\text{または}\quad
 |\Gamma(3/4+it/2)|^2\,dt
\]
という正測度に対する多項式の直交性が得られる。
直交多項式の実単純零点定理が、Mellin変数で \(\Re s=1/2\) を与える。
oscillatorの自己共役性から任意の変換の零点実性が出るのではない。

別証明では、中心をずらした多項式 \(q\) に対する
\[
 r(z)=(z+a)q(z+2)-(z-a)q(z-2),\qquad a>0,
\]
のstrip縮小を用いる。零点が \(|\Re z|\le c,\ c>0\) にあれば、
左右の因子の絶対値比較により \(r\) の零点はより狭いstripに入る。
特定のMellin多項式がこの作用の固有多項式であることと、
有限個の零点について最大実部が達成されることが決定的である。
一般の整関数に同じ議論を無条件で移してはいけない。
[BCKV I, Theorem 1 の二証明](https://kurlberg.github.io/eprints/lrh1.pdf)。

### 非アルキメデス体：局所表現とunit-circle恒等式

Kurlberg II は、奇数剰余標数の局所体における特定のWeil表現vectorを扱う。
primitive unramified caseでは
\[
 y=q^{1/2-s},\quad r=q^{-1/2},\qquad
 1=\left|y^{N-1}\frac{y-r}{1-ry}\right|
\]
が零点条件から得られ、単位円の内外での厳密な絶対値比較により \(|y|=1\) が強制される。
ramified caseでは \(A+Bq^{-(N-M)s}\) とGauss和の
\(|B/A|=q^{(N-M)/2}\) が同じ線を与える。
任意のSchwartz関数についての主張ではない。
[Kurlberg II, Theorem 4 と Lemmas 20–22](https://kurlberg.github.io/eprints/lrh2.pdf)。

Sauvalle の非退化二次characterは別の対象であり、弱Mellin変換を要する。
実数の場合のKummer方程式のWronskian恒等式では、
正の積分 \(\int|Y|^2\) が複素parameterの実部を固定する。
非アルキメデスの場合はvaluation分解と局所Fourier/Weil indexが働き、\(p=2\) も含む。
共通点は「特別な局所入力＋exactな変換恒等式による絶対値拘束」。
全場所で同一の直交測度を用いる単一証明ではない。
[Sauvalle, published §§3–4](https://doi.org/10.4064/aa8240-7-2016)。

局所の適用範囲、shift-stripの境界検算、版ごとの規格化は
[局所担当ノート](local_to_global/notes/local_rh_and_sauvalle.md)に分離した。

## 3. Sauvalle の「どの一行」でglobal gapが現れるか

一般のglobal weak Mellin transformは、絶対収束域で
global \(L(s,\chi)\) と有限個のlocal correctionに分解される。
\(\mathbb Q\) の具体的な \(f(x)=\psi_{\mathbb A}(x^2/2)\) では
\[
 \Xi_f(s)=e^{-\pi is/4}C_2(s)\,
                 \frac{2\xi(s)}{s(s-1)},\qquad
 C_2(s)=2^{1-s}-1+e^{\pi i/4}(2^s-1).
\tag{S}
\]
有限補正 \(C_2\) の零点は全て \(\Re s=1/2\) にある。
従ってcritical stripの臨界線外では
\[
 \operatorname{ord}_\rho\Xi_f=\operatorname{ord}_\rho\zeta.
\]
この具体例のglobal confinementは既にRHと同値である。
失われたのは単なる「local constantの一様性」ではなく、
(S) に **未解決のglobal \(L\)-factorがそのまま残る**という事実である。
局所補正はその零点を取り除かない。
Euler積をcritical stripまで絶対収束する積として運ぶことはできない。
[Sauvalle, Theorem 4.6 と §4.4](https://doi.org/10.4064/aa8240-7-2016)。

## 4. Semilocal stability が保存するもの

CCM 2024 のSonin stabilityは、有限places集合 \(S\) に対する
bounded isomorphism \(\theta_S\) とFourier intertwiningである。
completed Mellin表示では
\[
 \upsilon_S\theta_S=\upsilon_\infty
\]
となり、対応する個別の整関数自体とその零点は保存される。
ただしnormは \(S\) に依存し、選ばれるground stateまで同一ではない。
Sonin条件は「関数とFourier変換がともに原点近傍で消える」であり、
「ともにcompact support」ではない。

ambient Mellin座標でのmultiplierは
\[
 m_S(t)=\prod_{p\in S_f}(1-p^{-1/2-it}),\qquad
 \|m_S^{-1}\|_\infty=\prod_{p\in S_f}(1-p^{-1/2})^{-1}.
\]
このinverse normは全素数へのexhaustionで発散する。
これはambient mapの結果であり、Sonin subspaceでの追加評価を反証してはいない。
空間同型だけからWeil positivity、ground gap、全零点実性は出ない。
[CCM 2024, §§4.6–4.8](https://arxiv.org/html/2310.18423v2#S4.SS6)。

## 5. 有限prime構成で既に証明されていること

以下は [CCM *Zeta Spectral Triples*, arXiv v1](https://arxiv.org/html/2511.22755v1)
の §5 と §8 を基準とする。2026年のEMS刊行物は書籍中の章であり、
正確な定理番号は固定arXiv版のものを用いる。

\(\lambda>1\)、\(I_\lambda=[\lambda^{-1},\lambda]\)、
\(E_N\) を次数 \(N\) 以下のlog-Fourier部分空間とする。
\(Q_{\lambda,N}\) はactual Weil formの制限で、有限prime powersだけでなく
Gamma・pole termsも含む。\(N\) は素数個数ではない。

**ES:** 最小固有値が単純で、対応する \(v_{\lambda,N}\) が反転について偶。

この条件の下で、有限商
\(E_N/\mathbb Cv_{\lambda,N}\) に \(Q_{\lambda,N}-\epsilon I\) の正内積が降り、
未変更のDirac tailと合わせた \(D_{\lambda,N}\) が自己共役になる。
元のWeil form自体の非負性を示したわけではない。
Theorem 5.10はexactに
\[
 d_{\lambda,N}(z):=\det_{\rm reg}(D_{\lambda,N}-z)
   =-i e^{-iz\log\lambda}\widehat v_{\lambda,N}(z),
\quad
 \widehat v(z)=\int_{I_\lambda}v(u)u^{-iz}\frac{du}{u}
\tag{D}
\]
を与える。従って \(\widehat v\) の全零点は実数である。

CvSの一般定理も、この結論を無条件の全算術構成へ拡張するものではない。
本質的自己共役性、孤立単純最小固有値、偶な固有関数を要する。
同論文の固定窓のcore近似評価は有効だが、全窓でのgapや規格化を制御しない。
[CvS, Theorem 6.1](https://arxiv.org/html/2511.23257v1#S6)。

## 6. 新しく使用できる外部estimateは存在する。ただし別の族

CCM §7ではprolate関数から \(h_\lambda\) を作り、
\[
 h(x)=\frac{\pi}{2}x^2(2\pi x^2-3)e^{-\pi x^2},\qquad
 k_\lambda(u)=1_{I_\lambda}(u)\,u^{1/2}
                            \sum_{m\ge1}h_\lambda(mu)
\]
を定義する。Lemma 7.2の固定次数prolate/Hermite近似は
\(\|h_\lambda-h\|_\infty=O(\lambda^{-2})\)。
Poisson summationとGaussian tailを追跡すると、任意 \(0<r<1/2\) に対し
\[
 \sup_{|\Im z|\le r}
 \left|\widehat k_\lambda(z)-\frac14\mathscr X(z)\right|
 \le C_r\lambda^{-1/2+r}
       +C_r\lambda^{C_r}e^{-\pi\lambda^2},
\qquad \mathscr X(z)=\xi(1/2+iz).
\tag{P}
\]
これは具体的な既知estimateであり、今回の外部入力として採用する。
印刷された \(h\) と \(du/u\) ではスカラーは \(\mathscr X/4\) となることを
Gamma積分で再検算した。値規格化でこの無害な定数差は解消する。
この再計算をRHへの新しいboundと数えない。

決定的な区別：

|族|実零点性|actual \(\mathscr X\) への収束|
|---|---|---|
|\(\widehat v_{\lambda,N}\)：真のWeil ground|ESの下で既知|未証明|
|\(\widehat k_\lambda\)：prolate近似関数|未証明|規格化後、strip内で既知|

二列の長所を同じ関数に属するように扱うことが、誤ったRH証明の一行になる。
原著 §8「The missing steps」と
[Connes 2026 §6.6](https://arxiv.org/html/2602.04022v1#S6.SS6)も、この比較を未解決としている。

## 7. Exact break proposition

座標を
\[
 \mathscr X(z)=\xi(1/2+iz),\quad
 \Omega=\{|\Im z|<1/2\},\quad z_*=i/4
\]
に固定する。非自明零点は無条件にこのstripに入り、
\(\mathscr X(z_*)=\xi(1/4)>0\)。
ESの下では \(\widehat v(z_*)\ne0\) なので
\[
 F_{\lambda,N}(z)=
 \mathscr X(z_*)e^{i(z-z_*)\log\lambda}
                 \frac{d_{\lambda,N}(z)}{d_{\lambda,N}(z_*)}
 =\mathscr X(z_*)\frac{\widehat v_{\lambda,N}(z)}
                         {\widehat v_{\lambda,N}(z_*)}
\]
は整、全実零点、非零の一点規格化を持つ。raw determinantに定数だけを
掛けるのではなく、(D)のphaseも取り除く。

**未証明の複合命題 G\*.**
\[
 \boxed{
 \begin{gathered}
 \exists(\lambda_j,N_j)\text{ satisfying ES},\quad\lambda_j\to\infty,\\
 \forall K\Subset\Omega:\quad
 \sup_{z\in K}\left|
 \frac{\widehat v_{\lambda_j,N_j}(z)}
      {\widehat v_{\lambda_j,N_j}(z_*)}
 -
 \frac{\widehat k_{\lambda_j}(z)}
      {\widehat k_{\lambda_j}(z_*)}
 \right|\longrightarrow0.
 \end{gathered}}
\tag{G*}
\]
ESのcofinalな成立と、比較estimateの両方を含む。
この二つを既知扱いして「残りはnormal familyだけ」とは結論しない。
RHからこの特定の比較命題への逆含意は証明していない。

(P)+(G*)なら \(F_{\lambda_j,N_j}\to\mathscr X\) が \(\Omega\) のcompact上で一様。
非実零点を囲む小円板にRouchéを適用すると、実零点しか持たない \(F\) に
非実零点が必要となり矛盾する。多重度も保存される。
全複素平面の収束より弱い、このstrip上の収束で十分である。
これは条件付き帰結であり、(G*)を証明したのではない。

## 8. 収束の検査を具体化した結果

1. 未変更tail \(\pi j/\log\lambda,\ |j|>N\) があるため、
   非零compact一様極限には \(N/\log\lambda\to\infty\) が必要。
   比が有界な部分列では実零点が有限区間に稠密化し、正則極限は恒等零になる。
2. actual \(N=0\) 構成は全段階でESを満たすが、\(a=\log\lambda\) として
   \[
   f_a(z)=\frac{\sin(az)/z}{4\sinh(a/4)}
   \]
   は \(f_a(i/4)=1\)、実軸上では0へ、\(z=2i/5\)では無限大へ向かう。
   全実零点と一点規格化だけでは正規族にならない。
3. 固定窓の \(L^2\) 近似から複素変換への移送には窓依存の
   \(\lambda^r\) 損失があり、規格化分母のconditioningも必要。
4. prolate集中固有値とWeil ground gapは異なる。
   trial stateのRayleigh差を真のgapで割る評価がなければ、ground近似は出ない。
5. norm-resolvent収束だけでもdeterminantに余分なGaussian因子が残り得る。
   tailのtrace/Schatten制御を独立に要する。

これは正しい同時極限への反証ではなく、弱い前提の誤用を排除する検査である。
数値実験は定数・identityの検算に限定し、零点一致やgrowth fitからRHを推測しなかった。

## 9. 過去trackとの重複とstrategy review

Phase III/IVの「算術的忠実性と正性を同一対象へ結べない」という障害は保持される。
特に [旧 accumulation_spectrum.md §4](notes/accumulation_spectrum.md) は既に
CCM Theorem 5.10、CvS Theorem 6.1、§8のsimple/evenとground近似の欠落を記録している。
この結論自体の再発見を新成果とは数えない。
今回の差分は、有限構成のexact determinant、条件付きreal-zero theorem、
今回式として詳しく取り込んだprolate近似関数への具体的収束評価を用いて、
不足する比較を正規化・strip・二変数経路付きの(G*)に固定したこと。
新しい作用素やcohomology、global metricは作っていない。

SauvalleとConnesのgapを同一の定理と呼ぶことはできない。
前者ではglobal \(L\)-factorがexactに残る。後者では二つの明示的な関数族の比較が欠ける。
共通するのは、localないしfiniteの零点拘束を、actual global関数へ忠実に渡す部分である。

Asano / Lee–Yang / stability-preserverとの比較からactual構成へのexact mapは得られない。
追加の2026年文献も確認したが、(G*)への無条件upper estimateは取得できなかった。
探索範囲と採用しなかった論拠は
[文献選別ノート](local_to_global/notes/search_scope_and_additional_inputs.md)に記載した。
網羅的な不存在証明とは主張しない。

**判定：** 3方向の限定監査は完了。Level 1。
新しい外部estimateはあり、真のground stateに対する新しい橋の証明はない。
同型の第四候補や数値規模拡大へ移らず、RH OPENのまま停止する。

## 10. 成果物と監査

- [定理stack](local_global_theorem_stack.md)
- [候補比較](local_global_candidate_matrix.md)
- [state](../../../data/source-records/research/local_global_state.json)
- [独立adversarial audit](../../audits/proofs/audits/local_global_zero_confinement_adversarial.md)
- [局所原典ノート](local_to_global/notes/local_rh_and_sauvalle.md)
- [Sonin / real-zero原典ノート](local_to_global/notes/semilocal_and_real_zero_theorems.md)
- [正規化・収束評価・切断点の計算](local_to_global/notes/spectral_approximants_and_exact_gap.md)
- [Hurwitzと収束反例の独立検算](local_to_global/notes/convergence_destroyer.md)
- [診断実験](../../../artifacts/research/local_to_global/experiments/check_normalization_and_tail.py)
- [実験結果](../../../artifacts/research/local_to_global/experiments/results.json)
- [既存343ファイル・HEAD・文書整合性の検査](../../../data/source-records/research/local_to_global/validation.json)
- [持ち帰り用のテキスト報告](local_to_global/completion_report.txt)

THE EXACT BREAK IS: ESを満たすcofinalなactual Weil ground-state列について、
(G*)の正規化したFourier変換の差が \(|\Im z|<1/2\) の各compact上で一様に0へ行く、
という比較定理が未証明である。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/audits/local_global_zero_confinement_adversarial.md`](../../audits/proofs/audits/local_global_zero_confinement_adversarial.md)
- [`research/local_global_candidate_matrix.md`](local_global_candidate_matrix.md)
- [`research/local_global_state.json`](../../../data/source-records/research/local_global_state.json)
- [`research/local_global_theorem_stack.md`](local_global_theorem_stack.md)
- [`research/local_to_global/completion_report.txt`](local_to_global/completion_report.txt)
- [`research/local_to_global/experiments/check_normalization_and_tail.py`](../../../artifacts/research/local_to_global/experiments/check_normalization_and_tail.py)
- [`research/local_to_global/experiments/results.json`](../../../artifacts/research/local_to_global/experiments/results.json)
- [`research/local_to_global/notes/convergence_destroyer.md`](local_to_global/notes/convergence_destroyer.md)
- [`research/local_to_global/notes/local_rh_and_sauvalle.md`](local_to_global/notes/local_rh_and_sauvalle.md)
- [`research/local_to_global/notes/search_scope_and_additional_inputs.md`](local_to_global/notes/search_scope_and_additional_inputs.md)
- [`research/local_to_global/notes/semilocal_and_real_zero_theorems.md`](local_to_global/notes/semilocal_and_real_zero_theorems.md)
- [`research/local_to_global/notes/spectral_approximants_and_exact_gap.md`](local_to_global/notes/spectral_approximants_and_exact_gap.md)
- [`research/local_to_global/validation.json`](../../../data/source-records/research/local_to_global/validation.json)
- [`research/notes/accumulation_spectrum.md`](notes/accumulation_spectrum.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_normalization_and_tail.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
