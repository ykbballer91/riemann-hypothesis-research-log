**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/destroyer-initial.md` · Original SHA-256: `6dc204245360d4714a03252bce3b19324c66d8be5aab96f0d96b294f84b4683c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 独立監査: 固定 support の Weil 形式と有限 Gram 橋渡し

日付: 2026-09-29。役割: DESTROYER。BUILDER の証明本文を読まず、親エージェントが提示した命題だけから検算した初回監査。

判定: **限定した橋渡し命題は条件を明記すれば成立する。RH の正値性を新しく証明していない。** 原論文での Weil criterion の正確な許容クラスとの一致は LITERATURE AUDITOR の検証対象として残す。

## 検査対象の定義

\[
D_L=\{f\in C_c^\infty(\mathbb R):\operatorname{supp}f\subset[-L,L]\},\qquad
p_m(f)=\max_{0\le j\le m}\|f^{(j)}\|_\infty.
\]
L は固定正数。整数 L に限定しても全 \(C_c^\infty\) を覆う。
\[
\rho=\beta+i\gamma,\quad z_\rho=-i(\rho-1/2)=\gamma-i(\beta-1/2),\qquad
F_f(z)=\int f(x)e^{izx}\,dx.
\]
\[
Q(f,g)=\sum_\rho F_f(z_\rho)\overline{F_g(\overline{z_\rho})}.
\]
零点は重複度込みで数え、全非自明零点を含める。\(0<\beta<1\) と零点数評価は無条件の既知結果として使用する。有限計算では代替できない。

## 1. 減衰評価と境界項: PASS

\(z=u+iv\)、\(|v|\le1/2\) とする。\(f\) は端点を含めた全実線上で smooth かつ台が \([-L,L]\) に含まれるため、端点で全導関数がゼロとなり、部分積分の境界項は消える。

\(|u|\ge1\) なら m 回の部分積分から
\[
|F_f(u+iv)|\le |u|^{-m}\int_{-L}^L
\left|\frac{d^m}{dx^m}(f(x)e^{-vx})\right|dx
\le2Le^{L/2}(3/2)^m p_m(f)|u|^{-m}.
\]
\(|u|\le1\) には直接の積分評価を使う。従って全 u で有効な明示的定数の一例は
\[
|F_f(u+iv)|\le C_{L,m}p_m(f)(1+|u|)^{-m},\quad
C_{L,m}=2Le^{L/2}3^m.
\]
L=0 は \(D_0=\{0\}\) として別扱いすればよい。m=0 の減衰評価自体は有効だが、以下の零点和には不十分。

## 2. 零点和・tail・連続性: PASS (m≥1)

\(N_*(T)=\#\{\rho:|\gamma|\le T\}=O(T\log(T+2))\) を T≥2 について用いる。低い高さの有限個の零点を分離すれば
\[
S_m=\sum_\rho(1+|\gamma|)^{-2m}<\infty\quad(m\ge1)
\]
であり、二進区間 \(2^kT<|\gamma|\le2^{k+1}T\) の和を取ることで
\[
\sum_{|\gamma|>T}(1+|\gamma|)^{-2m}
\ll_m T^{1-2m}\log(T+2)\quad(T\ge2)
\]
を得る。したがって
\[
|Q(f,g)|\le C_{L,m}^2S_m p_m(f)p_m(g)
\]
かつ同じ係数の tail 版が成立する。m=1 でも指数は −2 で収束する。この点で m≥2 を要求する必要はない。

全和の絶対収束は、零点の添字の反射による並べ替えを正当化する。固定 support 以外で定数 \(C_{L,m}\) を一様と呼んではならない。

## 3. 共役方向・Hermitian 性: PASS

\(\rho\mapsto1-\overline\rho\) に対応して \(z_\rho\mapsto\overline{z_\rho}\) となる。零点多重集合がこの写像で不変なため、絶対収束を使う添字交換により
\[
\overline{Q(g,f)}=Q(f,g).
\]
各項の \(\overline{F_g(\bar z)}\) を \(\overline{F_g(z)}\) に置き換えるのは不可。その置換は軸上性を暗黙に仮定する。

## 4. Gram convention: 修正を要求

この定義の Q は第1変数で線形、第2変数で反線形である。従って
\[
G_{jk}=Q(\phi_j,\phi_k)
\quad\Longrightarrow\quad
Q\left(\sum_jc_j\phi_j,\sum_kc_k\phi_k\right)=c^T G\bar c.
\]
通常の \(c^*Mc\) に一致させるなら
\[
M_{jk}=Q(\phi_k,\phi_j)
\]
と定義すべき。G の PSD と M の PSD は同値だが、二次形式の恒等式には転置が必要。規約を明記せず \(Q(f,f)=c^*Gc\) と書く証明は式として誤り。

## 5. 密度から正値性への延長: PASS (同じ位相での密度が条件)

各固定 L に対して、有限線形結合の和が \(D_L\) で \(p_m\)-稠密な列 \(\phi_{L,j}\) を持つことを仮定する。全 N で Gram PSD なら、その有限線形結合で Q が非負。f を \(p_m\) で近似する \(f_n\) を取ると
\[
|Q(f_n,f_n)-Q(f,f)|
\le C_{L,m}^2S_m p_m(f_n-f)\bigl(p_m(f_n)+p_m(f)\bigr)\to0.
\]
従って \(Q(f,f)\ge0\)。固定 support の Fréchet 位相で稠密であればこの条件は満たされる。**単に \(L^2\)-稠密という記述では不十分**。反例 F01 を参照。

任意の compact support はある整数 L の窓に入る。従って L→∞ における作用素極限や一様な tail 評価を追加で主張する必要はない。\(\forall L\in\mathbb N_{>0}\) と \(\forall N\) の量化はいずれも省略できない。

## 6. 論理評価: 正値性の核心は残る

この橋渡しは、全許容関数の正値性を、無限個の有限 Gram 行列の PSD に正しく還元する。有限個の行列の計算、または各固定 N で確認範囲を拡大したという実験は、全 L,N の PSD の証明に代わらない。

零点和を有限高さで切って作る行列は元の Gram 行列とは異なる。切断誤差の**絶対値評価**は差分行列の PSD を意味しない。特に最小固有値が誤差より小さい場合、近似行列の PSD だけから正確な行列の PSD は従わない。厳密な誤差を spectral margin と比較できた個々の行列だけが認証対象となる。

**監査で棄却したもの:** 境界項無視、共役方向の置換、L²密度による未証明延長、Gram 添字規約の誤用、量化の有限化、tail の絶対値評価を正値増分に取り違えること。

**生存したもの:** 固定 support・正確な Fourier 規約・無条件零点数評価・適切な密度・全サイズ量化の下での連続性と有限→無限橋渡し。

**初回時点で未監査:** Weil criterion の原典での試験関数クラスと本定義の一致、BUILDER の最終本文、形式化コード。本文と現代文献に対する追跡監査を以下に記録する。

## 7. BUILDER 本文の追跡監査

初回の独立導出を保存した後、`proofs/lemmas/finite_to_infinite.md` F0–F7 と `proofs/lemmas/weil_conventions.md` を閲読した。

- **F1 PASS:** 本文の定数 \(A_{L,m}=2^{m+1}Le^{L/2}\) は本監査の定数より鋭いが正しい。本文は \(f(x)e^{-vx}\) を実振動に対して微分する代わりに、複素数 \(iz\) で直接部分積分し \(|z|\ge|u|\) を使っているためである。
- **F2–F3 PASS:** m=1 での収束、二進分割による tail、固定 support の \(p_1\) 連続性を確認した。
- **F4 PASS:** 関数の support の縮小、mollifier による近似、有理標本点の Riemann 和という三段階は、各 \(p_m\) で正しく機能する。support に正の余裕があるため、すべての bump が厳密に \((-L,L)\) に入る。関数族は基底である必要はない。
- **F5 PASS:** Gram 行列の添字が転置され、\(Q(f,f)=c^*Mc\) が正しくなっている。全 L,N の量化が保存され、RH 同値の未解決仮定を残している。
- **F6 PASS:** Hermitian 行列の Rayleigh 商と \(p_1(\sum c_j\phi_j)\le\|c\|_2(\sum p_1(\phi_j)^2)^{1/2}\) から operator norm の tail 上界が従う。最小固有値と誤差の比較方向も正しい。右辺の定数を単なる big-O から実用的な数値上界として取り出したとは主張していない。
- **変換規約 PASS:** Fourier の共役反転、Mellin の \(t^{-1/2}\) 因子、乗法畳み込み、\(s\mapsto1-\bar s\) の対応を直接代入で確認した。

明示公式の算術側は、[Suzuki, arXiv:2606.09096v3, §1.1](https://arxiv.org/html/2606.09096v3) と独立に照合し、\(\log(4\pi)+\gamma_E\) の定数および積分 kernel の規約が一致することを確認した。原点でのキャンセルと無限遠の可積分性も本文どおりである。このプレプリントの後段の予想は使用していない。

許容関数クラスについては、[Suzuki, arXiv:2206.03682v4, §3.2 (3.3)–(3.5)](https://arxiv.org/html/2206.03682v4) で \(C_c^\infty(\mathbb R)\) 上の判定法と共役反転規約を確認した。これは現代の研究論文での定式化の照合であり、Weil 1952 原版全文を独立に監査したという意味ではない。閲読時の HTML では版ヘッダが 2023-05-30、本文の Date が 2026-08-24 と併記されていたため、出版版と各 arXiv 版の日付を区別して書誌を固定する必要がある。

追記: LITERATURE AUDITOR は [固定 v4 PDF](https://arxiv.org/pdf/2206.03682v4) の p.1 で本文日付 2023-05-31、版ヘッダ 2023-05-30 を確認し、p.10 の §3.2 に同じ判定法を確認したと報告した。この書誌差には固定 PDF を優先する。

**追跡判定:** 上記局所解析・規約・有限→無限橋渡しは PASS。正値性核心は OPEN。形式化コードと Weil 原版全文は未監査のまま。

## 8. 固定支持の核最適化 barrier の独立監査

対象: `proofs/lemmas/kernel_optimization_barrier.md` K0–K6。
本文の閲読前に平均ゼロ primitive の恒等式と cosine 臨界点を独立に導出し、その後本文の式・定義域・正規化と照合した。

**判定: PASS (記載された変分問題と、同一の二次モーメント式に限定)。RH 全般の不可能性定理ではない。**

### 平均ゼロ条件と境界項

\(I=[-1/2,1/2]\)、\(\int_Ih=0\)、\(H(x)=\int_{-1/2}^xh\) とする。\(h\in L^2\subset L^1\) より H は絶対連続、両端でゼロ。\(V(x)=\int_I|x-y|h(y)dy\) に対して \(V'=2H\) が成立する。従って
\[
\int_I\int_I|x-y|h(x)h(y)dxdy
=\int_IH'V=-2\int_IH^2.
\]
境界項を消す理由は平均ゼロ条件であり、一般の質量1の f にそのまま同じ恒等式を適用してはいけない。本文は h=f−f0 にのみ適用しており正しい。

\(t=x+1/2\) とおき、H を \(\mathbf1_{[-1/2,x]}-t\) と h の内積として評価すれば
\[
\|H\|_2^2\le\left(\int_0^1t(1-t)dt\right)\|h\|_2^2
=\frac16\|h\|_2^2.
\]
従って本文の \(\mathcal C(h)\ge(2/3)\|h\|_2^2\) は正しい。係数の最適性は必要ない。

### cosine 解・正規化・gap

\(a=1/\sqrt2\)、\(f_0(x)=\cos(\sqrt2x)/(\sqrt2\sin a)\) は質量1であり、\(f_0''+2f_0=0\)。\(T=I+\int|x-y|\) の作用は \(Tf_0\) を affine にし、偶性が傾きをゼロにする。端点での評価により
\[
Tf_0=C_{\rm MT}=\frac12+\frac{\cot a}{\sqrt2}.
\]
従って質量1の任意の実 L² 関数について交差項は消え、
\[
\mathcal C(f)-C_{\rm MT}=\mathcal C(f-f_0)
\ge\frac23\|f-f_0\|_2^2.
\]
非負・偶という制限を一旦外した大きなクラスで正しい下界を得ているので、元の小さい核クラスに対する下界も成立する。唯一性は L² における a.e. の意味。

### 最小値と infimum の区別

f0 は端点でゼロでないため、そのゼロ延長を compact smooth な最小化関数と呼べない。本文は cutoff を施した平方根を \(\eta_\delta\) として正規化し、\(f_\delta=\eta_\delta^2\to f_0\) を L² で示す。この手順で小さいクラスの infimum が一致する。T は有界なのでこの L² 収束で十分であり、前節の Weil 形式で必要だった \(p_1\) 収束と混同していない。δ に一様な導関数評価を仮定していない点も適切。

### 文献の二次モーメントとの対応

実偶 f、P=f*f に対し \(P(0)=\|f\|_2^2\) であり、Fubini と反射で
\[
2\int_0^1\alpha P(\alpha)d\alpha
=\int_I\int_I|x-y|f(x)f(y)dxdy.
\]
従って変分問題と文献の定数は同じ。Fourier の \(2\pi\) は変分核自体の追加係数にはならない。

[Lamzouri v1](https://arxiv.org/html/2609.02882v1) の Lemma 3.2、Remark 3.4、Theorem 1.1 の末尾を独立に閲読し、定数と下界 \(2-C_\eta\) の対応、および固定 cutoff の後に高さを無限へ送る順序を確認した。重み除去で固定 P と固定 P'' に別々に公式を適用するため、T に依存する試験関数に一様性を仮定する必要はない。ここでは pair-correlation 入力定理全体を再証明していない。

[Carneiro–Chandee–Littmann–Milinovich v1, Corollary 14](https://arxiv.org/html/1406.5462v1) の純解析的下界と定数を独立に照合した。R=K² については、三角形 kernel の Fourier 対応と Plancherel から \(M(K^2)=\mathcal C(f)-1\)。当該純解析不等式と、同論文の零点への応用での RH 仮定を区別した。

### 結論の量化

核変更だけで同じ下界式の右辺を最大化する値は \(2-C_{\rm MT}=0.6725007\ldots\) であり、\(C_{\rm MT}\ge5/4>1\) から100%にはならない。この値は**実際の臨界線零点の割合の上限ではない**。支持、モーメント、零点情報、最後の不等式を変える手法を排除しない。この限定を本文が明記しているため、方法の barrier としての結論は適切である。

**未検証のもの:** Lamzouri の pair-correlation 入力の全証明、引用先の Lean 証明群の依存関係。この監査の PASS はこれらの全体監査を意味しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`proofs/lemmas/finite_to_infinite.md`](../../../reports/proofs/lemmas/finite_to_infinite.md)
- [`proofs/lemmas/kernel_optimization_barrier.md`](../../../reports/proofs/lemmas/kernel_optimization_barrier.md)
- [`proofs/lemmas/weil_conventions.md`](../../../reports/proofs/lemmas/weil_conventions.md)
