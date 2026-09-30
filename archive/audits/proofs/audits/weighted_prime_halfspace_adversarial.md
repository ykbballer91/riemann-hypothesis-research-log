**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/weighted_prime_halfspace_adversarial.md` · Original SHA-256: `733b6c0cbd49260ce82b42bb5680ffb9546bf64b86e374fecd7e2f81183f848f`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Weighted Prime Half-space — adversarial audit

2026-09-30。RH OPEN。新しい proof-critical identity は得ていないため Lean formalization は実施しない。数値結果は構造の検算・反証専用。

## 1. 監査の分担と独立性

BUILDER は Track A の有限差分・sharp downset bound・文献照合を担当。
LITERATURE は優先 Track B の平方自由 Euler product、Selberg–Delange endpoint、剰余定理を担当。
DESTROYER は Track C の Gibbs readout と sieve parity を担当。
ROOT は actual arithmetic を保つ統合、実験コード、候補採否を担当した。

DESTROYER は Track A の downset bound と independent perturbation を別に検算し、Track B の原典・剰余・synthetic Dirichlet series も独立監査した。LITERATURE は Track C の Gibbs identity、saddle 存在条件、非Gaussian極限、saddle への極限移行、無限 parity の定義域を独立監査した。いずれも stated scope で PASS。

これらは記載した定理・補題・仮定の確認であり、引用論文全体の独立再証明ではない。

## 2. Arithmetic fidelity

- 全候補の主対象は \(\mu(n)^2z^{\omega(n)}\)。\(z=-1\) は \(\mu(n)\)。
- 全整数版 \(z^{\omega(n)}\) の Euler factor は異なる。Liouville \((-1)^{\Omega(n)}\) も別。
- actual cutoff は \(\sum\epsilon_p\log p\le\log X\) のまま。rectangular cutoff への置換なし。
- comparison weights や synthetic Dirichlet series は論理的含意を反証するためだけに使用し、actual ζ の代用品にはしていない。
- 旧 topology、zero-bearing quotient、Gamma factor、proof graph、各 state は一切変更しない。

## 3. Track A の destroyer gates

| Gate | Exact check | Decision |
|---|---|---|
| translation の符号 | \(J(u)=1_{u\ge0}\) には \(I-\tau_{+\log p}\)、\(H_L(0)\) には \(I-\tau_{-\log p}\) | 正しい符号に固定 |
| 境界なら小さい | support は \([0,\vartheta(X)]\)、全変動 \(2^{\pi(X)}\) | narrow-boundary inference 棄却 |
| 正の spline | 目的量は \(D^{m-1}B\)、\(B\ge0\) とは別 | positivity shortcut 棄却 |
| smoothness | \(h^{-m}\|\psi^{(m-1)}\|_\infty\prod\log p\) が残る | fixed-order estimate 流用なし |
| universal threshold bound | \({m-1\choose\lfloor(m-1)/2\rfloor}\)、equal-weight で sharp | 正規化だけの利得を棄却 |
| independence / distinct sums | 閾値 margin 内で Q-independent perturbation が extremum を保つ | 非共鳴だけの改善を反証 |
| Littlewood–Offord | unsigned shell と interval の長さ・endpoint を保持 | signed arithmetic bound と混同なし |
| noise / martingale | \(\rho^{-m}\) の復元、最後の difference に全 parity coefficient | 無料の減衰・順序独立標本化を棄却 |
| prime block | parent の \(\pi(X/r)-\pi(Y)\) を保持 | multiplicity の削除なし |

Downset proof の細部：\(q_j=a_j/\binom mj\) は非増加、\(p_j=q_j-q_{j+1}\ge0\)。最後の \(j=m\) の交代和は0なので、残る convex mass は \(q_0-q_m\le1\)。常に \(q_0\) と等しいとはしていない。empty downset、full cube、\(m=1\) も含む。\(m=0\) は別に扱う。

Irrational extremizer は actual primes の counterexample ではない。一般定理だけを強化する提案への反例である。

## 4. Track B の destroyer gates

### 全係数消失の範囲

\(G(s,-1)=1\) は因子ごとの exact identity。
\(\lambda_j(-1)=h_j(-1)/\Gamma(-1-j)=0\) は全局所漸近係数についての statement。

ここから次を推論しない：

- \(M(X)=0\)。
- finite Boolean bulk の exact pairing。
- remainder の支持が境界だけになる。
- remainder が低次元になる。
- remainder が平方根規模になる。

例えば \(S_{-1}(100)=1\) であり、局所係数が0でも有限和は0でない。

### 剰余定理の量化

de la Bretèche–Tenenbaum の Theorem 1.2 に \(\mu,\varrho=-1,r=1,\sigma_0>1/2\) を入れる条件を確認。任意の固定 \(K\) の \(O_K(X/\log^KX)\) は得られるが、定数を無視した \(K(X)\) は使わない。

補足の \(Xe^{-c\sqrt{\log X}}\) 型評価も、Chang–Martin v2 Lemma A.11 と Theorem A.13 の証明 p.23 を別担当が照合。これは既知の零点自由領域を含む定理を利用した再取得であり、今回の独立な cancellation mechanism ではない。

有界複素 \(z\) 集合での加法誤差と、零になる先頭係数で割った相対誤差を区別。全係数が消えるから error constant まで0とはしていない。

### Local zero synthetic test

\[
D_\beta(s)=\zeta(s+1-\beta)
-c_\beta\zeta(s+1),\quad c_\beta=\zeta(2-\beta)/\zeta(2),
\quad 1/2<\beta<1.
\]
\(D_\beta(1)=0\)、局所正則だが、係数和は \(X^\beta/\beta-c_\beta\log X+O_\beta(1)\)。第一項は積分比較または Euler summation、第二項は harmonic sum による。

Euler product と multiplicativity は保持しない。従って RH の反例ではなく、局所的主項消失から小さい大域 remainder を推論する一般則だけを反証する。

### 分布定理

通常 CLT の fixed normalized frequency に \(\pi\sqrt{\log\log X}\) を代入しない。一方、強化された mod-Poisson theorem が \(\pi\) を扱う場合もあるため、「πを扱う定理はない」とも言わない。対象の squarefree 条件と絶対誤差の scale をそれぞれ検査した。

## 5. Track C の destroyer gates

有限 Gibbs formula は全実 \(\sigma\) で exact。ただし \(\mathbb E(\chi G)\) を \(\mathbb E\chi\,\mathbb EG\) に置き換えない。\(X=3,\sigma=1\) の有理反例では復元値の符号が逆になる。

有限 saddle は \(0<L<\vartheta(X)\) のとき一意。positive saddle は \(L<\vartheta(X)/2\) のときに限る。全 \(X\ge2\) に positive solution があるとはしていない。

非Gaussian極限は分散だけから推論せず、Laplace transform を直接導いた。saddle への移行は次で定量化できる：
\[
d_X=(\sigma_X-1)L\to0,\quad u_p=\log p/L,\quad
q_p(d)=\frac1{1+pe^{du_p}}.
\]
\(|d|\le1\) なら \(|\partial_dq_p|\le e\,u_p/p\)。よって
\[
|q_p(d_X)-q_p(0)|\le e|d_X|u_p/p.
\]
Laplace 対数の差は \(O_t(|d_X|\sum u_p^2/p)=O_t(|d_X|)\to0\)、normalized variance の差も \(O(|d_X|)\to0\)。したがって transform の極限自体を移せる。

Lindeberg の \(3/4\) は指定した大素数区間からの寄与であり、全 Lindeberg sum の厳密な極限値と主張していない。

無限系では \(\sigma>1\) に selected primes が almost surely 有限。全実 \(\sigma\le1\) では無限個で、通常の parity が定義できない。有限 parity expectation が0へ収束する statement は全負の \(\sigma\) へ広げられない点も検査した。

## 6. Sieve parity の主張範囲

有限 divisor-sum upper/lower bound を \(1\pm\lambda(n)\ge0\) で重み付ける不等式を、signed error \(E_\lambda\) を残して証明した。local densities のみを使う情報の限界を示すが、任意 sieve level でその error が小さいとは仮定しない。

\(\mu^2\pm\mu\) の leading divisor density が同じという模型は各固定 \(d\) の statement。全ての exact divisor sums、増大する level での総誤差、追加の bilinear information まで識別不能とはしていない。

Tao 2015 の broad parity barrier には informal な範囲があることも記載。全 Selberg/β-sieve theorem の最適定数を再監査したとは主張せず、今回使う divisor-information obstruction に限定する。

## 7. 実験の役割

整数算術：Möbius sieve、prime recursion、全 downsets 次元1〜4、equal-weight rank formula 次元1〜20、720 permutations、pivotal shells、大素数 multiplicity、\(\omega\) 別個数。

有理数算術：\(z=-1+\delta\) の有限多項式値、\(\sigma=1\) の有限 Gibbs/covariance identity。

80桁 numerical diagnostics：重み perturbation、saddle values、inverse-Gamma の実装確認。対数・平方根による comparison は区間保証ではない。一般の irrational perturbation theorem、reciprocal-Gamma zero、saddle の存在・極限は別の解析的証明による。

Random continuous weights は有限精度の擬似乱数サンプルであり、分布定理の実験的証明には使わない。growth fit なし。

LITERATURE の独立実験監査も PASS。元のスクリプトを import・再実行せず、trial division、Fraction、principal-ideal unions による別実装で、recurrence 203段階、downsets の件数3・6・20・168、720順列、pivotal shell 10件、大素数分割1389項、tilt 3件、\(\omega\) 多項式4件・有理端点値20件を照合した。binary64 による重み模型7件・saddle 6件の別再計算も一致し、最大差 \(4.44\times10^{-16}\)。これは数値診断の照合であり区間保証ではない。

## 8. 最終 decision

三試行を終了。今回の独立な新評価はなく、Level 0、RH OPEN。
全ての可能な arithmetic threshold methods への不可能性定理は主張しない。
prior files の hash preservation、required files、state consistency、code と JSON、local links は別の validation に保存する。
