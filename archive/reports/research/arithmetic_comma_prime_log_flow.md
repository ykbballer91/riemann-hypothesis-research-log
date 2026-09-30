**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma_prime_log_flow.md` · Original SHA-256: `cf0830431a7077ffa3e3dbf0afd0567b88487a1ff7d8f1f6f9304fffb4cd6595`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma / Prime-log Kronecker Dephasing

2026-09-30。RH は **OPEN**。既存 Phase I–IV、Scale Flow、One-Prime、Dyadic、Prime Complex の成果・状態・主証明グラフは変更しない。

**終了判定：Level 1（既知の exact bridge の固定）まで。** 三つの主要経路を検査したが、素数対数の非共鳴から Möbius 和の新しい定量評価を導く独立な矢印は得られなかった。特に「位相分布・時間平均・分散から恒等位相の和を制御する」一般則には、同じ素数対数と同じ cutoff を保持した明示反例がある。これは RH の反例でも、全ての位相法の不可能性定理でもない。

## 1. 基礎対象と適用範囲

有限素数集合 \(P\)、\(L=\log X\)、\(\lambda_p=\log p\) に対し
\[
\nu_P=*_{p\in P}(\delta_0-\delta_{\lambda_p}),\quad
A_P(L)=\sum_{S\subset P,\,\sum_{p\in S}\lambda_p\le L}(-1)^{|S|}.
\]
全素数の対象は局所有限な signed measure
\[
\nu=\sum_{n\ge1}\mu(n)\delta_{\log n},\qquad
M(e^L)=\nu(({-\infty},L]).
\]
その Laplace transform の絶対収束は \(\Re s>1\) で
\[
\int e^{-su}d\nu(u)=\frac1{\zeta(s)}=\prod_p(1-p^{-s}).
\]
解析接続は、この signed measure の絶対収束領域の拡大を意味しない。形式的な無減衰 Bohr 積 \(\prod_p(1-z_p)\) 自体を無限トーラス \(H^2\) の元とはしない。

有限の Bohr 対応は \(n=\prod p^{\kappa_p}\leftrightarrow z^\kappa\)。squarefree support では \(\kappa_p\in\{0,1\}\)、係数は \(\mu(n)=(-1)^{|\kappa|}\)。vertical translation は \(z_p(t)=p^{-it}\)。素因数分解の一意性から非零整数ベクトル \(m\) に \(\sum m_p\log p\ne0\)。非定数 character の時間平均を直接積分すれば、固定有限次元の continuous Kronecker flow の等分布が従う。これは mixing ではない。

一次資料：Hedenmalm–Lindqvist–Seip [math/9512211v1](https://arxiv.org/html/math/9512211v1)、§2.2、§4.1。これは既知の Bohr/Hardy–Dirichlet 構造であり、新規成果ではない。

## 2. Track A：cutoff を保つ exact bridge

正規化 Haar measure (dm) に対して
\[
B_P(z)=\prod_{p\in P}(1-z_p),\qquad
C_{P,X}(z)=\sum_{n\le X,\ n\text{ squarefree},\ p\mid n\Rightarrow p\in P}z^{\kappa(n)}
\]
と置くと
\[
\boxed{A_P(\log X)=\int B_P(z)\overline{C_{P,X}(z)}\,dm(z).} \tag{A1}
\]
追加の \(2^{|P|}\) は不要。weighted half-space の形は \(C_{P,X}\) にそのまま残る。全素数 \(p\le X\) を含めれば \(A_P(\log X)=M(X)\) であり、係数側の omitted tail は零である。一方、必要な素数を省いて積だけを小さくしても actual Mertens 和にはならない。

また \(\widehat\phi(t)=\int\phi(v)e^{-itv}dv\)、\(\phi\in C_c^\infty(\mathbb R)\) なら
\[
(\nu_P*\phi)(L)=\frac1{2\pi}\int\widehat\phi(t)e^{itL}
                    \prod_{p\in P}(1-p^{-it})\,dt.          \tag{A2}
\]

全素数では \(\sigma>1\)、\(g_\sigma(v)=e^{-\sigma v}\phi(v)\) として
\[
\sum_n\mu(n)\phi(L-\log n)
=\frac{e^{\sigma L}}{2\pi}\int
\frac{\widehat g_\sigma(t)e^{itL}}{\zeta(\sigma+it)}\,dt.     \tag{A3}
\]
絶対収束と Fubini により無条件。有限積を \(\Re s=0\) で無限 Euler 積へ置き換える操作はしない。

非負、質量1、台 ([-h,h]) の mollifier で step cutoff を平滑化した \(M_h(X)\) について
\[
|M_h(X)-M(X)|\le 2X\sinh h+1.                              \tag{A4}
\]
平方根級に戻すには縮む \(h\lesssim X^{-1/2+\varepsilon}\) に対する一様な積分評価が必要。対応する Fourier の周波数幅・微分定数も追跡しなければならない。fixed smoothing の評価だけでは足りない。Perron の整数 endpoint は半跳躍となり、右連続な (M(X)) との差 \(\mu(X)/2\) も明記した。

**不足する部分。** (A1) は二つの因子の相関であって、\(B_P\) 単独の時間平均ではない。その単独平均は1。Cauchy–Schwarz は一般に自明界を改善しない。(A3) の contour を \(\Re s=1/2+\varepsilon\) へ移し、零点に由来する residues を捨てる案は未証明の zero-free 条件を使う。相関自体に平方根 bound を置くだけなら Mertens 問題の再表現である。

証明・endpoint・no-tail・\(H^2\) の範囲は [Fourier bridge note](arithmetic_comma/notes/fourier_bridge.md) に保存。

## 3. Track B：非共鳴の実際の効力と反例

異なる正整数 \(a,b\) について
\[
|\log(a/b)|\ge\frac1{\max(a,b)}.
\]
actual cutoff の \(a,b\le X\) なら (1/X)。一般の整数係数 \(|m_p|\le H\) では
\[
0<|\sum m_p\log p|,\qquad
|\sum m_p\log p|\ge\exp(-H\sum_{p\in P}\log p).             \tag{B1}
\]
Matveev の原典 §2 Corollary 2.3 は固定素数集合について \(H\) の polynomial lower bound を与えるが、指数に次元依存定数と \(\prod\log p\) が入り、増大する素数集合で一様な固定指数にはならない。[Matveev II (2000)](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=314&what=fullteng)。

これらは character/time-average の誤差に使える。しかし粗い gap bound が要求する大きい「十分時間」を、必要な return time の下界と誤認してはならない。actual cutoff の比較では強い (1/X) bound を使える。

### 3.1. 位相の向き

\[
|B_P(z(t))|=\prod_{p\in P}2|\sin(t\log p/2)|.
\]
全位相が0に近い return はこの full product を**抑制**する。全位相が \(\pi\) に近い時は**増幅**する。各座標の誤差が \(\eta<\pi\) なら、それぞれ \(\eta^{|P|}\) 以下、\([2\cos(\eta/2)]^{|P|}\) 以上。fixed dimension の両 box の時間密度は Haar mass \((\eta/\pi)^{|P|}\)。稀な box でも振幅は大きくなり得る。

\(\int|B_P|^2dm=2^{|P|}\)、\(\int|B_P|dm=(4/\pi)^{|P|}\)。後者の定数は円周積分から直接出るもので、着想源の論文や物理的数値は使っていない。確率正規化して \(2^{-|P|}\) を掛けるなら、元の整数和へ戻す倍率を失ってはならない。

### 3.2. 同じ分布でも固定位相では違う：主要な反証

\(\mathcal A_X=\{n\le X:\mu(n)^2=1\}\) とし
\[
C_X(z)=\sum_{n\in\mathcal A_X}z^{\kappa(n)},\quad
F_X(z)=\sum_{n\in\mathcal A_X}\mu(n)z^{\kappa(n)}.
\]
すると厳密に
\[
\boxed{F_X(z)=C_X(-z).}                                    \tag{B2}
\]
Haar 平行移動により、両者の複素値の分布は完全一致する。全モーメント、全 \(L^q\) norm、fixed \(X\) の極限時間分布も同じ。一方
\[
F_X(1)=M(X),\qquad C_X(1)=|\mathcal A_X|\sim6X/\pi^2.       \tag{B3}
\]
これは素数対数も cutoff geometry も変えていない反例である。従って時間 RMS が平方根規模であること、さらに全分布を知ることさえ、恒等位相の相殺を強制しない。固定した reconstruction kernel との**相関**は別であり、その追加情報を利用する可能性までは否定しない。

また actual Möbius polynomial 自体について
\[
\sup_{t\ge t_0}|\sum_{n\le X}\mu(n)n^{-it}|=|\mathcal A_X|
\quad(t_0\ge0).                                          \tag{B4}
\]
全座標 (-1) に近づく dense orbit と三角不等式による。全時間一様の平方根 bound は成り立たないが、\(t=0\) の Mertens bound の否定ではない。

### 3.3. all commas の定義と高次共鳴

cutoff、符号、multiplicity を保つ signed gap distribution を
\[
\mathcal D_X=\sum_{a,b\in\mathcal A_X}\mu(a)\mu(b)
                     \delta_{\log a-\log b}
\]
と構成した。Fourier transform は \(|F_X(z(t))|^2\)。必要なら \((\log a,\log b)\) 上の元の二変数測度により境界位置を個別に保持できる。sinc kernel との積分が有限時間平均を正確に与えるが、その符号付き積分を小さくする新評価は得られない。

高次モーメントでは \(2\cdot15=3\cdot10\) のような multiplicative resonance が存在する。素因数指数を合算すれば同じベクトルなので、prime-log independence と矛盾しない。高次モーメントを増やすだけでは (B2) の同分布障害は消えない。

詳しい直接証明は [phase statistics gate](arithmetic_comma/notes/phase_statistics_gate.md)、独立監査と Matveev の適用範囲は [nonresonance audit](../../audits/research/arithmetic_comma/notes/nonresonance_audit.md)。

## 4. Track C：pretentious formulation

一般の multiplicative \(|f|\le1\) に使える Halász–Montgomery–Tenenbaum の形を原典の掲載版で確認した。完全乗法的な関数だけの定理を \(\mu\) に流用しない。
\[
m_\mu(X,T)=\min_{|t|\le2T}\sum_{p\le X}\frac{1+\cos(t\log p)}p,
\quad
\frac{|M(X)|}X\ll(1+m_\mu)e^{-m_\mu}+T^{-1/2}.              \tag{C1}
\]
固定 \(t\) での距離と、増大する全窓の minimum は違う。全 \(t\) について
\[
0\le m_\mu\le2\sum_{p\le X}p^{-1}=2\log\log X+O(1).
\]
そのため比較関数 \((1+m)e^{-m}\) 自体をこの公式内で最小化しても、得られる規模はせいぜい log-power であり、固定 \(X^{-\delta}\) ではない。これは actual (|M(X)|) の下界ではなく、**この black box の出力の限界**。

全座標が \(\pi\) に近い位相は \(\mu(p)=-1\) に近く、距離を小さくする。この向きも B の積の振幅と整合する。character twists の分離は一つの例外候補まで自動排除するものではなく、conductor と高さの量化が別途必要。

一次資料：Granville–Soundararajan [Decay of Mean Values of Multiplicative Functions (2003)](https://doi.org/10.4153/CJM-2003-047-0)、p.1192 Eq.(1.2) と同頁 theorem；[Pretentious Multiplicative Functions and an Inequality for the Zeta-Function (2008)](https://dms.umontreal.ca/~andrew/PDF/Norm.pdf)、pp.209–211。詳しくは [pretentious audit](../../audits/research/arithmetic_comma/notes/pretentious_audit.md)。

## 5. 二素数・有限素数・数値反証

\(P=\{2,3\}\) の squarefree 状態は (1,2,3,6) の4個だけ。cutoff を通過する和は (1,0,-1,0)。\(\{2,3,5\}\) では birth products (1,2,3,5,6,10,15,30) に対する累積和が (1,0,-1,-2,-1,0,1,0)。

大きな係数 \(m\log2-n\log3\) の近似共鳴は存在するが、それは元の Boolean 模型に新しい squarefree 状態を追加しない。fixed finite primes で \(X\) を増やし続ければ最後は総和0になるだけであり、RH の漸近問題は再現しない。

[実験コード](../../../artifacts/research/arithmetic_comma/experiments/check_phase_bridge.py) と [結果](../../../artifacts/research/arithmetic_comma/experiments/results.json) を保存した。subset enumeration、6件の整数演算による Haar モーメント検算、product identity の60桁数値照合、二素数の近似 return、有限時間 sinc 積分、2・3素数で計40,000点の診断 sampling を実施した。全 assertion は通過。sampling を連続時間の厳密な census や RH の証拠にはしない。

例：\(X=100\) では \(M(X)=1\)、squarefree count は61。符号付き・全正符号の両模型で二次 Haar moment は61、四次は11229と完全一致する。恒等位相での値は1と61。これは asymptotic fit ではなく、B2 を小さい入力で検算するもの。

\(P=\{p:50<p\le100\}\) という actual-prime subsystem は empty と10個の singletons しか cutoff100を満たさず、和は (-9)。ログが非共鳴でも cutoff の幾何が偏りを残す。これは全 (M(100)) とは違う対象であると明示した。

## 6. 既存トラックへの接続と禁止した近道

Prime Complex の線形規模の残存状態を減らす方法へは戻らなかった。今回は状態を保った位相の相関を検査した。小素数だけへ切り詰め、残りを絶対値で捨てる案では、例えば ((X/2,X]) の素数の寄与だけでも多数残る。sieve の上界からその符号付き相殺は出ない。

\(H^2\) では減衰した Möbius 係数が \(\sigma>1/2\) で square summable になるが、恒等 boundary character の評価は非連続。有限 cutoff 空間でも、その point evaluation norm は正確に \(\sqrt{|\mathcal A_X|}\) で、RMS の平方根を相殺して自明界へ戻す。以前の「弱い completion で必要な評価を失う」問題がここでも現れる。

高次相関、Gowers 型量、Chowla 型予想を新仮定として持ち込まない。もし必要な定量相関を仮定するだけなら問題の移し替えである。imaginary phase drift と \(Re\rho-1/2\) の radial drift を直接結びつける新 identity は得られなかった。

新しい \(M(X)=O(X^\theta)\) を得ていないため、Dyadic の既存 \(2^{(\theta-1/2)n}\) への指数改善はなし。本トラック単独の最良固定指数は自明界の \(\theta=1\)。これは既存の PNT 級・zero-free-region 型の評価を否定する値ではない。以前の Dyadic ファイルは一切変更しない。

## 7. Strategy review と終了理由

| 主要試行 | 無条件に保存したもの | 新しい bound が止まる場所 | 判定 |
|---|---|---|---|
| A Fourier/discrepancy | exact Haar/Fourier/Perron bridge、unsmoothing 費用 | kernel と符号積の算術的相関 | bridge 保存、RH route 終了 |
| B quantitative nonresonance | gap 下界、有限時間 identity、位相法則反例 | marginal law が恒等位相情報を失う | distribution-only 案を反証、route 終了 |
| C pretentious | 一般 multiplicative の Halász、距離の正確な符号 | 距離は \(O(\log\log X)\)、black box は log scale | route 終了 |

三試行で、独立な相関評価は追加されなかった。別名の第4候補へは進まない。**主証明グラフへ統合しない。** 新しい再開条件は、actual cutoff kernel との相関を既知算術から無条件に抑える具体的な identity または estimate が提示されること。単にその相関へ平方根 bound を置くことは再開条件を満たさない。

本トラックの成果は exactness と failure mechanism の切り分けである。RH の新しい同値条件を成果として数えず、RH は未解決のままとする。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/arithmetic_comma/experiments/check_phase_bridge.py`](../../../artifacts/research/arithmetic_comma/experiments/check_phase_bridge.py)
- [`research/arithmetic_comma/experiments/results.json`](../../../artifacts/research/arithmetic_comma/experiments/results.json)
- [`research/arithmetic_comma/notes/fourier_bridge.md`](arithmetic_comma/notes/fourier_bridge.md)
- [`research/arithmetic_comma/notes/nonresonance_audit.md`](../../audits/research/arithmetic_comma/notes/nonresonance_audit.md)
- [`research/arithmetic_comma/notes/phase_statistics_gate.md`](arithmetic_comma/notes/phase_statistics_gate.md)
- [`research/arithmetic_comma/notes/pretentious_audit.md`](../../audits/research/arithmetic_comma/notes/pretentious_audit.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_phase_bridge.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/results.json` — SOURCE REFERENCE NOT INCLUDED
