**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_complex_matching_matrix.md` · Original SHA-256: `33cb3e69934c6c1603311b4a3f82aff99975d2fdb265d75deaa4e21e99fa9e38`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime complex matching matrix

2026-09-30。RH OPEN。最大3つの主要構成を検査し、kill condition により終了。

| ID | 候補 | 実際の pairing / map | 未対応構造 | 独立な評価 | 結論 |
|---|---|---|---|---|---|
| PC-A | smallest-prime insertion、discrete Morse | odd m<=X/2 と2mを対にする | odd squarefree n∈(X/2,X] | 2X/pi²+O(sqrt X)、全 reduced Betti 数に一致 | Stage A/B。acyclic critical 総数の Stage C は不可能 |
| PC-B | large-prime、hyperbola、recursive cone gluing | p>sqrt X の face pmをparent mへ送る候補 | 共通parentへの衝突、singleton primes | any incidence matching に未対応>=pi(X)-pi(X/2)-1 | Stage D/Eは不可能。再帰式だけでは符号制御なし |
| PC-C | persistence、Hodge、spectral parity | d+d* の positive modes は偶奇で exact に対 | harmonic zero modes | kernel 総次元=全 reduced Betti数=Theta(X) | small-kernel 原理は反証。index は残った Mertens 符号和 |

## PC-A：どこまで positive result か

Arithmetic input: prime factor sets、product cutoff、最小素数2。
Matching: m<->2m、m odd squarefree、2m<=X。
Involution: matched domain では成立。全 even squarefree face が一意に対を持つ。
Acyclicity: 上向きは2の追加だけ。2の削除は逆向き edge なので閉路なし。
Boundary: U_X=(X/2,X] の odd squarefree faces。
Homotopy: star(2) collapse により各 residual face が一つの sphere。
Chain model: odd n ごとの z_n=boundary[2,sigma_n]、b_n=[2,sigma_n]。
Quantitative content: residual count は independently defined だが Theta(X)。
Independent of RH: 全て無条件。squarefree density の初等証明は PNT も不要。
Known prior art: Björner 1101.5704v1 Thms.2.1,3.1,3.4。
Novelty: 主張しない。barcode表示も初出未調査。
Kill reason: matching は reduced Betti 下界を既に達成し、通常の Morse cancellation に
よる critical 数の追加削減はできない。

naive smallest-admissible toggle は X=5 の {3}->empty->{2} で involution に失敗。
固定p=3のmatchingはacyclicでもperfectとは限らず、X=10でcritical3、Betti総数1。
単に「素数を一個追加すれば符号が変わる」ことと admissible matching を区別する。

## PC-B：平方根閾値が現れても小残差にならない理由

Arithmetic input: p>sqrt X は n<=X に高々一個。
Exact decomposition: small-prime core に cones p*Delta_{X/p} を貼り合わせる。
Important distinction: parent m<sqrt X が少なくても、同じmへ多数のpが集まる。
X=5 のp=3,5は両方m=1を使用しようとする。

Strong falsification: p∈(X/2,X] は singleton で上方 coface がない。その唯一の
augmented incidence neighbor はempty。任意の matching がemptyを一回しか使えないので、
未対応数>=pi(X)-pi(X/2)-1~X/(2log X)。acyclicityは不要。
固定delta>0でO(X^(1-delta))は不可能。これはnonlocal arithmetic pairingには適用しない。

Recursive link: D_p(X/p) はpを除く複体で、一般に full Delta_{X/p} ではない。
Euler recurrence: M(X)=M_p(X)-M_p(X/p)。新しい cancellation estimate は含まない。
Local divisor identity: 個別の simplex では完全相殺するが、global unionではfacesが重複。
weighted identity sum mu(d)floor(X/d)=1 と unweighted M を取り違えない。

Kill reason: sqrt X個のparentsだけを数えるとattachment multiplicityを失う。
shared basesを互いに独立なconesとして相殺する方法は不正。

## PC-C：persistence/index が保持するもの

Filtered chain basis: integer unimodular、各odd sf nのbarは[n,2n)、degree omega(n)-1。
Doubling map: cone homotopyにより reduced homology上0。
Boundary size: 全barsのlog寿命がlog2でも、同時に生きるbarがTheta(X)個。
Natural metric: oriented simplicesをorthonormal、degreeごと正定値を許す。
Operator: actual boundary d による D=d+d*、L=D²。
Exact spectral pairing: lambda>0 で D/sqrt(lambda) が偶奇のL-eigenspacesを同型にする。
Kernel: finite Hodge theoremにより total reduced Betti数。metricで小さくできない。
Index sign: cardinality gradingならM、homological degree gradingなら−M。

Kill reason: positive/nonzero modes の pairing は一般の finite complex にもある。
線形個のkernelの偶奇差を小さくする算術評価は供給しない。
homology基底を任意に順位でpairして残差を|M|にする案は、独立なboundを与えないので
同じ候補の tautology gate で棄却。第4の探索ルートとして続けない。

## Synthetic / fidelity matrix

| Test model | 何を検査したか | 結果 |
|---|---|---|
| actual squarefree integers | exact boundary ranks、M、critical、barcode | 整数・有理数で一致 |
| all integers via prime sets | 2と4が同じface、mu値は異なる | 元のMöbius modelとして不適合 |
| finite actual prime set | 全積までcutoffを上げるとfull simplex | reduced homologyとsigned sumは0。有限から無限への一様boundは出ない |
| modified multiplicative weights | min-vertex matchingとcone structure | 同じ構造が成立し、RH固有性を保証しない |
| seeded prime-weight perturbations | 素数ラベルのweightだけを変えた有限complex | exactmatchingは依然成立。actual arithmeticは保持されない |
| equal weights、孤立vertices | 8頂点、各weight4、cutoff4 | signed residual=−7。generic topologyだけで小さなindexは強制されない |
| prime-pair graph flag completion | X=15のtriangle | 本来ない30のfaceを加えるため失格 |

## Stage と終了時点

Stage A: YES、natural parity pairingを具体的に構成。既知構造の再確認。
Stage B: YES、unmatched set と完全homology/persistenceを明示。
Stage C: NO、このacyclic residualはTheta(X)なのでo(X)ではない。
Stage D: NO、face-incidence matching全体でもsingleton obstructionがある。
Stage E: NO、平方根相殺もRHも未証明。

best_unmatched_bound_exponent=1.0 はactual explicitmatchingの残余総数について。
Mertensの符号付き差の最良既知指数、あるいは未知のnonlocal方法の限界という意味ではない。

**Strategy review:** 線形critical/kernel障害と共有parent障害に到達したため終了。
以前のdyadic boundを改善する新しい算術入力は0。旧graphへのmergeは0。
