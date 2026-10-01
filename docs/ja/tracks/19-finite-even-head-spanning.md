# 19. 有限偶フーリエ空間：階数と条件数

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。偶L²巡回性に続く更新で、**Priority 2だけ**を完了した。次数を増やす漸近解析や全体の最低状態の捕捉は開始していない。

## 問いと正確な対象

実際のtheta核の微分を窓に制限して射影すると、固定有限偶フーリエ空間のどこまでを張るか。規約は $\widehat k(x)=\Xi(x)/4$、$\Xi(x)=\xi(1/2+ix)$、$R_af=1_{[-a,a]}f$。

$E_N^+$ の次元は $N+1$。窓の外で零にした正規直交基底は

$$b_0(t)=(2a)^{-1/2},\qquad b_n(t)=(-1)^na^{-1/2}\cos(\pi nt/a),\quad 1\le n\le N.$$

実際の列は $P_NR_ak^{(2j)}$。全実線のFourier標本は別の理想模型であり、実際の区間射影は $P_N(1-R_a)=0$ を満たす。この二つを混同すると裾の比較が成立しなくなる。

## 保存した補助結果

理想模型で $\omega_n=\pi n/a$、$t_n=\omega_n^2$ と置く。行列はXi重みの対角行列、Vandermonde行列 $(t_n^j)$、列の符号行列の積になる。$N+1$ 個のXi値のうち $r$ 個が非零なら、階数は正確に $\min(m+1,r)$。格子が零点に一致しなければ最小次数は $m=N$。

Xi格子零点は重複度に関係なく理想行列の一行を消す。周波数0の行は非零で、正負周波数の重複は偶部分への還元時に除いている。RH・単純零点は仮定しない。

実際の支持制限列には境界項が残る。$B_{nj}=\langle R_ak^{(2j)},b_n\rangle$ とすると

$$B_{nj}=-\omega_n^2B_{n,j-1}+d_nk^{(2j-1)}(a),\qquad d_0=\sqrt{2/a},\quad d_n=2/\sqrt a\ (n\ge1).$$

従って理想模型で零の行が実際にも零とは限らない。微分は支持制限の前に行う。切断した関数を微分すると境界分布が入り、別問題になる。

- **各固定 $a>0,N$** について、ある有限の初期微分列が実際の空間を正確に張る。巡回性と有限次元性による存在で、一般的な明示次数評価はない。
- **各固定 $N$** では、十分大きな $a$ で最小列 $m=N$ が張る。失敗し得る正の窓幅は有限集合だが、その場所・個数・空かどうかは未確定。
- 裾と最小特異値を比べる具体的不等式により、指定範囲で $m=N$ を認証する。浮動小数点行列式の非零性を階数証明としない。

Arb区間計算は、$a\in[1.499999,1.500001]$、$N=m=4$ と、$a\in[1.999999,2.000001]$、$N=m=6$ の各全域で完全階数を認証する。有限列の階数と元の座標の特異値下界の認証であり、**Weil正値性や物理Gram特異値の認証ではない**。

## 条件数は別の義務

Lagrange基底多項式から理想逆行列ノルムの上界 $L$、thetaの解析的裾評価から $\|E_{\mathrm{tail}}\|\le\tau$ を得る。$L\tau<1$ なら

$$\sigma_{\min}(B)\ge L^{-1}-\tau>0.$$

既知のVandermonde・離散直交多項式の道具を使っており、新しい一般定理とはしない。[参考文献](../references.md)を参照。

単項式から直交多項式への座標変更は張る空間を保つが、物理的写像を自動的に改善しない。係数ノルム、射影先のGram、全域または支持制限後のL² Gramを区別する。射影先のGramだけで正規化すると持ち上げ費用を隠し得る。

固定 $m=N$ で $a\to\infty$ のとき、元の最小特異値は $\Theta_N(a^{-2N-1/2})$、条件数は $\Theta_N(a^{2N})$。全域の物理Gramによる正規化でも小特異値の次数は消えない。正確な生成は一様安定性を意味しない。

高精度表は診断であり、物理Gramには有限のtheta和・積分切断を用いる。有限認証は別途記録したArb評価であって、浮動計算の一致から推測したものではない。

## 停止理由

固定空間の任意のベクトルは、偶最低状態を含め、十分長い**射影後**の微分列で表せる。これは代数的包含であって、最低状態の選択、係数制御、変化する最低状態と $k$ の比較ではない。

必要次数、物理的持ち上げ費用、形式ノルム誤差、固定次数階層の定数を同時極限で制御していない。**増大次数の選択、全体の偶最低状態、偶奇・ES、G*、RHは未解決。** この更新でPriority 3は開始していない。

## 原文と証拠

- [範囲を限定した主報告](../../../archive/reports/research/full_ground_capture/priority2/finite_even_head_spanning.md)
- [代数的階数と有限例外](../../../archive/reports/research/full_ground_capture/priority2/notes/algebraic_rank.md)
- [裾と条件数の証明](../../../archive/reports/research/full_ground_capture/priority2/notes/tail_conditioning.md)
- [文献・座標監査](../../../archive/reports/research/full_ground_capture/priority2/notes/conditioning_literature.md)
- [数値診断と限界](../../../archive/reports/research/full_ground_capture/priority2/notes/diagnostics.md)
- [区間認証コード](../../../artifacts/research/full_ground_capture/priority2/experiments/certify_tail_criterion.py)・[保存出力](../../../artifacts/research/full_ground_capture/priority2/experiments/tail_certificates.json)
- [独立した内部監査](../../../archive/audits/proofs/audits/full_ground_finite_head_adversarial.md)
- [当時の状態](../../../data/source-records/research/full_ground_capture/priority2/state.json)

監査は内部AIによるもので、外部査読やLean形式化ではない。新規性やRHが証明目前との含意は付けない。
