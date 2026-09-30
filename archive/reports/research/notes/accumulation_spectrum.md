**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/accumulation_spectrum.md` · Original SHA-256: `ec58731301fff14f9efef0cab39852ef5a1e784e15c963496c44304c8f26139c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# C「累積からスペクトルへ」・E「有限から無限へ」の一次文献監査

調査日: 2026-09-29（JST）。対象は数学的な構造だけである。元の着想資料に含まれる物理的説明・物理定数は導入しない。主 theorem graph は変更しない。本ノートは新しい RH 証明を宣言するものではない。

**判定:** 素数冪の平行移動、Mellin 変換、有限 Weil 行列、自己共役作用素という各構造には明確な先行研究がある。有限行列を同一形式の厳密な制限にすることは必要な整合性を与えるが、それだけでは十分でない。適切な core と**全次数**の正値性まで証明すれば固定窓の正値性に進める。しかし**全窓**の Weil 正値性は RH と同値であり、その前件を新しく証明する仕事は残る。

## 1. 調査範囲・根拠の区分

一次資料の原文で式、定理の前件、結論を照合した。査読誌への掲載と本監査による証明の独立再検証は別である。ここで「原文確認」は定理文・該当証明箇所の読解であり、論文全体の独立証明でも計算の再現でもない。

| ID | 一次資料・固定した版 | 公刊状況と今回の確認範囲 |
|---|---|---|
| S1 | Masatoshi Suzuki, *Weil’s quadratic form via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), 2026-09-23 | プレプリント。§1.1 の明示公式と試験関数域を原文確認。§7 のヒューリスティックを無条件定理として使用しない。 |
| S2 | Alain Connes, *Trace formula in noncommutative Geometry and the zeros of the Riemann zeta function*, [arXiv:math/9811068v1 PDF](https://arxiv.org/pdf/math/9811068v1), 1998-11-10 | 査読誌 Selecta Math. 5 (1999), 29–106、DOI [10.1007/s000290050042](https://doi.org/10.1007/s000290050042)。[著者の公刊記録](https://alainconnes.org/publications/)で書誌確認。以下の節・定理番号は arXiv v1 に固定。III.1、VII.4、VIII.5、VIII の数体への説明を照合。 |
| S3 | Connes–Consani–Moscovici, *Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1), 2025-11-27 | [EMS の公刊章](https://ems.press/books/elm/323/6477), DOI [10.4171/ELM/37/3](https://doi.org/10.4171/ELM/37/3)。章の存在は確認したが個別査読手続は未確認。以下は v1 の式・定理番号。 |
| S4 | Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, [arXiv:2511.23257v1](https://arxiv.org/html/2511.23257v1) | 査読誌 [Commun. Math. Phys. 406, 312 (2025)](https://link.springer.com/article/10.1007/s00220-025-05493-1), DOI 10.1007/s00220-025-05493-1。正確な使用条件は v1 Theorem 6.1 を参照。 |
| S5 | Jean-François Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, [arXiv:math/0203120v6 PDF](https://arxiv.org/pdf/math/0203120v6), 2004-02-24 | 査読誌 [J. Théor. Nombres Bordeaux 16 (2004), 65–94](https://jtnb.centre-mersenne.org/item/JTNB_2004__16_1_65_0/), DOI 10.5802/jtnb.434。§§1–3、Theorem 7.7、§8 を照合。 |
| S6 | Connes–Consani, *Spectral triples and ζ-cycles* | 査読誌 [L’Enseignement Mathématique 69 (2023), 93–148](https://ems.press/journals/lem/articles/11033001), DOI 10.4171/LEM/1049。[公刊 PDF](https://content.ems.press/assets/public/full-texts/serials/lem/69/1/11033001/online/10.4171-lem-1049.pdf)。本監査では公刊情報・概要と S3 が Prop. 2.3 を引用する位置を確認。全証明の再監査はしていない。 |
| S7 | Takashi Nakamura–Masatoshi Suzuki, *On infinitely divisible distributions related to the Riemann hypothesis*, [arXiv:2306.08317v1 PDF](https://arxiv.org/pdf/2306.08317v1) | 査読誌 Statistics & Probability Letters、公刊 DOI [10.1016/j.spl.2023.109889](https://doi.org/10.1016/j.spl.2023.109889)。§1 の Euler compound Poisson 表示、Theorems 1.1–1.2 を原文確認。 |
| S8 | Takashi Nakamura, *A complete Riemann zeta distribution and the Riemann hypothesis*, [電子公刊再録 PDF, arXiv:1504.03438](https://arxiv.org/pdf/1504.03438) | 査読誌 Bernoulli 21 (2015), 604–617。PDF 表紙の再録表示、Theorems 1.1–1.2 と §2.1 を確認。 |

検索は上記論文、arXiv の固定版、出版社・著者の一次資料に限定した。二次解説の断定は採用していない。網羅的な新規性調査ではないため、「類似構造を見つけた」と「全ての先行例を列挙した」は区別する。

## 2. C1: 素数冪の累積を対称平行移動へ写す

### 正確に成立する式

第一変数線形の内積を採り、

\[
 \langle f,g\rangle=\int_{\mathbb R}f(x)\overline{g(x)}\,dx,
 \qquad (\tau_a f)(x)=f(x-a),\qquad \widetilde f(x)=\overline{f(-x)}
\]

とする。\(f\in C_c^\infty(\mathbb R)\)、\(h=f*\widetilde f\) に対し

\[
 h(a)=\langle f,\tau_a f\rangle,
 \qquad h(a)+h(-a)=\langle(\tau_a+\tau_{-a})f,f\rangle.
\]

S1 §1.1 の無条件の Weil 明示公式をこの記号で書けば

\[
\begin{aligned}
 Q_W(f)&=W(f*\widetilde f),\\
 W(h)&=\int_{\mathbb R}h(x)(e^{x/2}+e^{-x/2})\,dx\\
 &\quad-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                  \bigl(h(\log n)+h(-\log n)\bigr)\\
 &\quad-(\log(4\pi)+\gamma_E)h(0)
 -\int_0^\infty\{h(x)+h(-x)-2e^{-x/2}h(0)\}
                         \frac{e^{x/2}}{e^x-e^{-x}}\,dx.
\end{aligned}
\]

したがって算術部分は厳密に

\[
 -\sum_{p^k}\frac{\log p}{p^{k/2}}
   \langle(\tau_{k\log p}+\tau_{-k\log p})f,f\rangle
\]

である。\(\operatorname{supp}f\subset[-L,L]\) なら寄与するのは \(p^k\le e^{2L}\) だけ。この有限性は試験関数の自己相関の support による。全 \(L^2(\mathbb R)\) 上の無限作用素級数が作用素ノルム収束するという主張ではない。[S1 §1.1](https://arxiv.org/html/2606.09096v3#S1.SS1) と [S3 (3.19)–(3.20)](https://arxiv.org/html/2511.22755v1#S3.SS1) に対応する。

### 何が新しく必要か

平行移動 \(\tau_a\) はユニタリ、\(\tau_a+\tau_{-a}\) は自己共役だが正作用素ではない。Fourier 側の乗数 \(2\cos(at)\) は符号を変える。したがって「素数冪の和を作用素にできた」から Weil 正値性は出ない。極項・無限素点の項を含む**全体**の符号制御が必要である。

また \(F_f(z)=\int f(x)e^{izx}\,dx\)、\(z_\rho=(\rho-1/2)/i\) と置くと、零点側の正しい積は

\[
 Q_W(f)=\sum_\rho F_f(z_\rho)\overline{F_f(\overline{z_\rho})}.
\]

一般には \(|F_f(z_\rho)|^2\) ではない。後者へ置換するには \(z_\rho\in\mathbb R\)、すなわち対象零点の臨界線上性が必要になる。この置換を無条件に使う方法は循環する。

**精度:** 試験関数域での厳密な恒等式。**先行性:** Weil 明示公式の作用素表示そのものに先行例がある。**RH より易しいか:** 表示の構築は易しいが、全試験関数の符号制御は RH 同値。**反証・棄却法:** 候補式の素数冪係数、極項、無限素点項を照合し、一つでも欠落すれば同一形式ではない。候補の PSD 主張には、誤差を含めても負である Rayleigh 商を一つ示せば反例となる。

### 補足: Euler 積の正の確率測度を臨界線まで延長できるか

\(\sigma>1\) では既知の厳密な構成がある。

\[
 Z_\sigma(t)=\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
 =\sum_{n\ge1}\frac{n^{-\sigma}}{\zeta(\sigma)}e^{-it\log n}
 =\exp\!\left(\sum_{p,r\ge1}\frac{p^{-r\sigma}}r
                   (e^{-itr\log p}-1)\right).
\]

これは正の確率測度の特性関数で、Lévy 測度は
\(\sum_{p,r}p^{-r\sigma}r^{-1}\delta_{-r\log p}\)。[S7 §1](https://arxiv.org/pdf/2306.08317v1) に同じ表示がある。

しかし \(\sigma\downarrow1\) ですでに、\(t=0\) では \(Z_\sigma(0)=1\)、固定 \(t\ne0\) では \(Z_\sigma(t)\to0\) となる。極限は原点で不連続なので、確率測度の弱極限を与えない。正規化に使った正の級数 \(\sum n^{-\sigma}\) も \(\sigma\le1\) では発散する。したがって解析接続された商へ同じ正測度を引き継ぐことはできない。

さらに強い注意として、S8 Theorem 1.1 は完成関数の商 \(\xi(\sigma-it)/\xi(\sigma)\) が**全ての実 \(\sigma\)** で特性関数になることを無条件に証明している。正測度表示自体は既にあり、それでも RH は従わない。同論文 Theorem 1.2 の RH 同値条件は、すべての 1/2<σ<1 における **pretended-infinitely divisible** 性であり、単なる特性関数性でも通常の infinitely divisible 性でもない。これは signed measure を許す同論文独自の定義（§1.2）。Theorem 1.4 は σ>1 でも通常の infinitely divisible 性を否定し、quasi-infinitely divisible 性を述べる。[S8 Theorems 1.1–1.4](https://arxiv.org/pdf/1504.03438)

この候補の精度・先行性は高いが、RH より易しい新しい十分条件は得ていない。棄却試験は正規化測度の有限性、極限の原点連続性、正定値性と零点位置の混同の三点である。

## 3. C2: Connes の trace formula と零点のスペクトル実現

S2 ではイデール類群の作用とアデール上の和

\[
 E(f)(g)=|g|^{1/2}\sum_{q\in k^*}f(qg)
\]

から商空間を作る。III.1 の重みパラメータ \(\delta>1\) を持つ実現では、生成作用素 \(D_\chi\) のスペクトルは**既に実部が \(1/2\) である零点**に対応する。重複度も \(\delta\) に依存して切られる。重み付き表現全体はユニタリとは限らず、純虚スペクトルだけから歪自己共役性を結論してはいけない。[S2 III.1–Corollary 2](https://arxiv.org/pdf/math/9811068v1)

有限集合 \(S\) の素点を使う VII.4 の trace formula は、コンパクト support の Schwartz 関数 \(h\) に対し

\[
 \operatorname{Tr}(R_\Lambda U(h))
 =2h(1)\log'\Lambda
 +\sum_{v\in S}\int_{k_v^*}'\frac{h(u^{-1})}{|1-u|}\,d^*u+o(1).
\]

ここで \(R_\Lambda=\widehat P_\Lambda P_\Lambda\)、局所主値積分の正規化は加法指標に依存する。\(R_\Lambda\) を無断で直交射影や正作用素に置換できない。[S2 VII.4](https://arxiv.org/pdf/math/9811068v1)

大域版は別の射影・極限の問題である。VIII.5 の**定理文は正標数**の大域体を仮定し、大域 trace formula と全 Hecke L 関数の RH の同値性を述べる。数体については VIII 後半、PDF pp.45–47 の近似射影による対応説明を区別して読む。数体で関数と Fourier 変換の両方に厳密な有限 support を課すと非零関数が消えるため、正標数の射影定義をそのまま移植できない。

この監査での帰結は次の通りである。

- 半局所公式が全ての有限 \(S\) について成立しても、それだけで大域射影の trace の極限が同じになるわけではない。空間・射影・正規化が変わるため、有限和であることとは別に比較定理が要る。
- 純虚スペクトルの実現が臨界線上の零点だけを選んでいても矛盾しない。全零点の捕捉を別に証明する必要がある。
- 原文の非臨界零点の「resonance」としての扱いは、非臨界零点の不存在証明ではない。
- trace が等しいという主張には、試験関数域、正則化、極・自明零点・重複度を含む等式を要求する。零点数の主要項や低い零点の一致だけでは足りない。

**精度:** 半局所 trace formula と限定されたスペクトル同定は定理。**先行性:** 本候補の数学的骨格は少なくとも S2 に既出。**RH より易しいか:** 大域 trace 同定の核心を証明せず省略すると RH 同値の難所を隠す。**棄却法:** 定理が捕捉する零点集合を確認し、全零点ではない場合はその段階で RH への接続を棄却する。有限 \(S\) の公式と大域射影の極限を混同する箇所も検出可能である。

## 4. C3: 有限 Weil 形式から自己共役作用素を作る既知の定理

S3 では \(\lambda>1\) ごとに \(L^2([\lambda^{-1},\lambda],du/u)\) 上の Weil 形式を考える。\(E_N\) は指定の対数座標 Fourier 基底 \(V_k\), \(|k|\le N\), の span であり、\(QW_\lambda^N\) はその**厳密な制限**である。Prop. 3.3–3.4 は半有界閉形式と form core を与える。

\[
 \inf_{\|f\|=1}QW_\lambda(f)
 =\lim_{N\to\infty}\lambda_{\min}(QW_\lambda^N),
 \qquad\lambda_{\min}(QW_\lambda^{N+1})\le
              \lambda_{\min}(QW_\lambda^N).
\]

Theorem 5.10 は最小固有値 \(\epsilon_N\) が単純、固有ベクトル \(\xi\) が偶、\(\delta_N(\xi)=1\) という条件で、商空間 \(E_N/\mathbb C\xi\) に

\[
 QW_\lambda^N-\epsilon_N\langle\cdot,\cdot\rangle
\]

の計量を入れて自己共役作用素を作り、その正則化行列式を \(\widehat\xi\) と結ぶ。**最小固有値を引いた形式の正値性は、元の \(\epsilon_N\ge0\) を証明しない。**

S3 §8 は、全窓にわたる最小固有値の単純性・偶性と、提案された近似関数 \(k_\lambda\) が真の最小固有関数を十分正確に近似することを、残る手順として明記している。[S3 Prop. 3.4, Theorem 5.10, §8](https://arxiv.org/html/2511.22755v1)

固定窓の無限次元化については S4 Theorem 6.1 が既にある。実分布から指定の畳み込み型二次形式を作り、三角多項式上の作用素が半有界かつ**本質的自己共役**、最下点が**孤立した単純固有値**、その固有関数が区間反転に関して偶であると仮定すると、固有関数の Fourier 変換は実零点のみを持つ。証明は三角多項式の **operator core** と固有ベクトル近似を使う。単に閉形式があることを、この本質的自己共役性の前件と同一視しない。[S4 Theorem 6.1](https://arxiv.org/html/2511.23257v1#S6)

**精度:** 条件付きの厳密な実零点・自己共役性定理。**先行性:** 有限次元から固定窓の無限次元へ移す骨格は既存。**RH より易しいか:** simple/even 条件単独は RH と同値とは確認されていないが、さらに全 ζ 零点への正しい極限同定を加えると RH を導く。難しさの低下は未証明。**棄却法:** 奇最小固有関数、縮退、孤立性の喪失、必要な operator core の不成立を探す。低い実零点の数値一致のみで全 ζ 零点への収束としない。

## 5. C4: Burnol の Sonine 空間・Mellin 変換

S5 の正規化は

\[
 \mathcal F_+f(u)=2\int_0^\infty\cos(2\pi tu)f(t)\,dt,
 \quad\widehat f(s)=\int_0^\infty f(t)t^{-s}\,dt,
 \quad M(f)(s)=\pi^{-s/2}\Gamma(s/2)\widehat f(s).
\]

\(K_a\subset L^2(0,\infty;dt)\) は \(f\) と \(\mathcal F_+f\) がともに \((0,a)\) で消える空間、\(L_a\) はともに定数である拡張空間。Theorem 2.1 と Proposition 2.2 は完成 Mellin 変換の解析性と評価汎関数の連続性を与える。後者には \(0,1\) の極を許す。評価ベクトルは**任意の複素評価点**に存在する。

Theorem 3.1 は全非自明 ζ 零点（重複度を含む）に対応する評価ベクトルが \(L_a\) で完全となる条件 \(a\ge1\)、極小となる条件 \(a\le1\) を述べる。これは RH を仮定した零点選別ではない。[S5 §§2–3](https://arxiv.org/pdf/math/0203120v6)

したがって「零点を Hilbert 空間のベクトルにできた」「完全系を得た」は「その零点が自己共役作用素の固有値である」と異なる。S5 §8 は一般の Sonine 関数には任意に選んだ零点を追加でき、全てが RH 型の零点制約を満たすわけではないと明示する。Theorem 7.7 の零点密度主要項が ζ と似ることも零点の線上性を決めない。

**精度:** Mellin/評価ベクトル/完全性は正確な定理。**先行性:** S5 とそこで明示される de Branges 理論に既出。**RH より易しいか:** 空間構築は完了しているが、ζ を特定の実零点型構造関数へ同定する新条件が必要。**棄却法:** ζ 以外の Sonine 関数にも同じ論法が適用され、任意の非実スペクトル点を許してしまわないか確認する。この一般クラスで成立しない結論を ζ に移すには、ζ 固有の追加前件を特定する。

## 6. E: exact restrictions で十分になる条件と、十分でない条件

以下は文献の主張を誇張しないための本ノート独自の論理整理である。新しい RH の入力ではない。

### 6.1 正しい十分条件

固定 \(L\) に対し、同じ Hermitian 形式 \(q_L\) の定義域内に

\[
 V_{L,1}\subset V_{L,2}\subset\cdots,
 \qquad M_{L,N}=q_L|_{V_{L,N}}
\]

を置く。次のいずれかがあればよい。

1. \(\bigcup_N V_{L,N}\) が閉半有界形式 \(q_L\) の **form core** であり、全 \(N\) について \(M_{L,N}\succeq0\) を証明する。
2. \(q_L\) が試験関数位相で連続、\(\bigcup_N V_{L,N}\) がその位相で稠密であり、全 \(N\) について同じ正値性を証明する。

すると各 \(f\) に対する近似 \(f_j\) から \(q_L(f)=\lim_jq_L(f_j)\ge0\) が従う。S3 Prop. 3.4 は 1 の具体例。本リポジトリの `proofs/lemmas/finite_to_infinite.md` は 2 の試験関数版を対象にしている。形式の連続性と稠密性を所与にした後の移行は標準的である。

全 support を覆う \(L=1,2,\ldots\) についてこれを証明すれば

\[
 (\forall L\in\mathbb N)(\forall N\in\mathbb N)\ M_{L,N}\succeq0
 \Longleftrightarrow
 (\forall f\in C_c^\infty(\mathbb R))\ Q_W(f)\ge0
 \Longleftrightarrow \mathrm{RH}.
\]

適切な core があるという前提での同値である。定性的な正値性だけなら、全窓に一様な正の固有値間隙や \(L\) に一様な近似速度までは不要。しかし有限回の計算から無限に多い前件を取り出すことはできない。

### 6.2 Hilbert 空間で稠密というだけでは不足する

明示的な対照例を \(H=L^2(-1,1)\)、定義域 \(H^1(-1,1)\) 上で

\[
 q(f)=\int_{-1}^1|f'(x)|^2\,dx-|f(0)|^2
\]

とする。例えば \(|f(0)|^2\le2\|f\|_2^2+\tfrac12\|f'\|_2^2\) は \(|x|\le1/2\) 上で基本定理と Cauchy–Schwarz を適用して平均すれば得られる。従って \(q+3\|\cdot\|_2^2\) のノルムは \(H^1\) ノルムと同値であり、これは半有界閉形式である。\(E=C_c^\infty((-1,0)\cup(0,1))\) は \(H\) で稠密で、\(q|_E\ge0\)。その可算稠密生成系の有限 span を用いれば全有限制限は PSD になる。それでも定数関数 \(1\in H^1(-1,1)\) に対して \(q(1)=-1\)。\(E\) は form core ではない。

この例は「厳密な制限」「nested」「\(L^2\) 稠密」を全て満たす設計でも、必要な位相を取り違えると失敗することを示す。閉形式の下半連続性だけでは、稠密部分空間上の非負性を外側へ移す向きの不等式は得られない。

### 6.3 有限個の PSD と全次数の PSD の差

\(\ell^2\) 上で \(q(x)=\sum_{j\ne N_0+1}|x_j|^2-|x_{N_0+1}|^2\) とすれば、最初の \(N_0\) 個の標準基底への全制限は正定値だが、次の制限は負方向を持つ。有限に多くの既知 PSD から、未知の次元への自動延長はない。

厳密制限の最小固有値は次数とともに**下がる**。したがって計算済みの正の最小固有値は無限形式の最下点に対する上界であって、非負下界ではない。有限計算を証明にするなら残りの方向を抑える独立の解析評価が要る。

また \(\|M-\widetilde M\|\le\varepsilon\) の保証があるときだけ

\[
 \lambda_{\min}(\widetilde M)-\varepsilon
 \le\lambda_{\min}(M)
 \le\lambda_{\min}(\widetilde M)+\varepsilon
\]

を証明書として使える。下界非負ならその有限行列の PSD、上界負ならその有限行列の負方向を証明できる。いずれも全窓・全次数を自動的に含まない。

### 6.4 異なる三つの極限を分離する

| 極限 | 解決すべき内容 | それだけで解決しないもの |
|---|---|---|
| 同一窓で次数 \(N\to\infty\) | 厳密制限・core・必要に応じて固有関数の収束 | 窓外の試験関数、ζ との同一性 |
| 窓 \(L\to\infty\) または \(\lambda\to\infty\) | 全試験関数の被覆、あるいは変動する空間・計量・作用素の比較 | 別の窓で得た数値一致の一般化 |
| 素点・積分・零点の数値 cutoff の除去 | その cutoff に固有の、符号またはノルムの厳密な tail 評価 | 次元・窓の未計算部分の PSD |

三者を単一の「十分大きくする」で済ませない。有限次数・有限窓での自己共役性があり、実零点の entire functions \(H_{L,N}\) が作れたとしても、ζ に対応する非零関数 \(\Xi(z)\) への**複素領域で局所一様な収束**（非零の正規化・全零点・重複度の扱いを含む）が別に必要である。適切な収束が証明されれば Hurwitz の定理を使えるが、実軸上の低い零点の一致はこの前件を代替しない。

## 7. 探索候補の判定表

| 候補 | 精密化できる部分 | 既出性 | 残る前件と RH との関係 | 具体的な失敗検出 |
|---|---|---|---|---|
| C1 素数冪の平行移動和 | 試験関数上の Weil 明示公式と厳密同値 | S1、S3、従来の明示公式 | 全体の非負性は RH 同値 | 欠けた極項・無限素点項、誤係数、非実零点の積を絶対値平方へ変える循環 |
| C2 大域 trace 同定 | 半局所公式、臨界零点の実現 | S2 | 全零点を捕捉する大域極限は本質的難所 | 臨界零点のみの定理を全零点と読むこと、射影の無断交換 |
| C3 最小固有関数の実零点 | simple/even 等の条件下の定理 | S3、S4 | 全窓で条件成立＋ζ への極限同定。より易しいという証拠なし | 縮退・奇性・core 不成立、最小値を引いた形式と元形式の混同 |
| C4 Sonine/Mellin | 評価ベクトル・完全系・変換恒等式 | S5 | ζ 固有の実零点型構造関数との同定 | 同じ仮定を満たす一般 Sonine 関数の追加零点 |
| E exact restrictions | 正しい位相の core＋全次数 PSD なら移行可能 | S3 Prop. 3.4、標準形式論 | 全窓・全次数 PSD は RH 同値 | \(L^2\) 稠密のみの対照例、有限チェックの後で現れる負方向 |

採用できるのは、既知の恒等式・定理を誤差なく土台として使い、**未証明の前件を明示した候補**までである。この調査から主 theorem graph に追加できる新しい無条件の大域正値性命題は得られていない。

## 8. 保留中の Groskin 調査との境界

ユーザー追加探索のため arXiv:2607.02828v3 の専用監査は中断した。既存 `literature/notes/weil-frontier.md` の記載を超えて、公開コードの所在・区間演算証明書の再現は確認していない。本ノートは Groskin の数値証明書を検証済み入力として用いない。専用 `groskin-certificate-audit.md` は中断時点で新規作成していない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/weil-frontier.md`](../../../literature/literature/notes/weil-frontier.md)
- [`proofs/lemmas/finite_to_infinite.md`](../../proofs/lemmas/finite_to_infinite.md)
