# 18. 偶数階微分族の巡回性

**STATUS: RIEMANN HYPOTHESIS OPEN**

記録日：2026-09-30。17トラックの公開棚卸し後の更新で、**Priority 1だけ**を完了した。原文のディレクトリ名にある「全体の最低状態の捕捉」は、この更新で証明した定理名ではない。

## 着想と検査

固定有限次元の選択定理の前に、微分族の合併がすべての偶な平方可積分関数へ届くかという基本問題がある。稠密性は近似の資源だが、増大する族の一様速度は与えない。

実際の規格化は

$$\widehat{k}(x)=\int_{\mathbb R}k(t)e^{-ixt}dt=\Xi(x)/4,\qquad \Xi(x)=\xi(1/2+ix).$$

正測度 $d\mu(x)=|\Xi(x)|^2dx$ を調べた。標準的なGamma減衰と無条件のゼータ評価から、指数 $\pi/2$ 未満のすべての指数モーメントが有限になる。Xiは非零整関数なので実零点集合の測度は0。RHも単純零点も不要である。

## 得られた補助定理

$$\boxed{\overline{\mathrm{span}_{\mathbb C}\lbrace k^{(2j)}:j\ge0\rbrace}^{L^2(\mathbb R)}=L^2_{\mathrm{even}}(\mathbb R).}$$

実偶L²での実線形包についても成立する。Carleman条件によるL²(μ)の多項式稠密性、偶対称化、全射等長写像 $h\mapsto\Xi h$、Plancherelから従う。別証明は解析的Fourier変換と一意性を使う。どちらもXiの一様有界な逆数では割らない。

$y=x^2$ への変数変換では、Stieltjes条件は $m_{2n}^{-1/(2n)}$ を使う。$m_{4n}$ を使う別のHamburger条件と取り違えない。補足のモーメント漸近は稠密性の証明に不要である。

## 未証明の範囲と停止理由

L²稠密性は、Weil形式領域の稠密性や形式核、一様近似評価、安定な係数、試行族の外側の固有値差を与えない。支持・Fourier解像・微分次数の極限交換も正当化しない。未証明のL²連続性・可閉性でradical恒等式を拡張してはならない。

**全体の最低状態の捕捉、増大するmの一様評価、ES、G*、RHは未解決。** この更新ではPriority 2以降を行っていない。定性的稠密性から必要な定量的・形式位相的制御へ進むには別の議論が必要であり、ここで停止した。

巡回性は、範囲を限定した内部AI監査を伴う書面上の補助証明である。既知のモーメント・Fourier原理を適用し、新規性は主張しない。外部査読やLean形式化は行っていない。

## 原文と証拠

- [主証明](../../../archive/reports/research/full_ground_capture/cyclicity.md)
- [モーメントの出典と別の直接証明](../../../archive/reports/research/full_ground_capture/notes/moment_problem_sources.md)
- [補足のモーメント漸近](../../../archive/reports/research/full_ground_capture/notes/moment_asymptotic.md)
- [内部監査](../../../archive/audits/proofs/audits/full_ground_cyclicity_adversarial.md)
- [当時の状態](../../../data/source-records/research/full_ground_capture/state.json)

[履歴](../timeline.md) · [再現手順](../reproducibility.md) · [参考文献](../references.md)

後の[Priority 2更新](19-finite-even-head-spanning.md)は固定有限空間の階数・条件数を扱う。この巡回性更新の当時の証明範囲を変更しない。
