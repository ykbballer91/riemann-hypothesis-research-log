**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/scale_flow/notes/frobenius_mapping_torus.md` · Original SHA-256: `2604f0ccdbc3ad42b14adf725ea3ba415621f742298b351b6a65cd7647393fa1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 素数周期軌道の Frobenius mapping torus：一次本文監査

取得・照合日：2026-09-29。独立の continuous scale-flow track の Level 1 整理。既知の構成を採用する範囲を固定し、新発見・RH の進展とは扱わない。Phase III / IV の記録は変更しない。

## 一次資料と版

| ID | 著者・版固定資料 | 使用箇所（PDF の第 n 頁） | 確認範囲 |
|---|---|---|---|
| S16 | A. Connes–C. Consani, *Geometry of the scaling site*, [1603.03191v1](https://arxiv.org/pdf/1603.03191v1), 2016-03-10 | Lemma 5.1, p.21；Frobenius の区別は §5.2, pp.24–26 | \(C_p\) とその scaling action。個々の軌道の Riemann–Roch を全域 positivity と読まない。 |
| S24 | 同, *Knots, Primes and the adele class space*, [2401.08401v1](https://arxiv.org/pdf/2401.08401v1), 2024-01-16 | Theorem 1.1, p.2；§2, pp.4–5, Eq.(4) | 原著の無条件 mapping-torus 同定。 |
| S25 | 同, *Knots, primes and class field theory*, [2501.06560v1](https://arxiv.org/pdf/2501.06560v1), 2025-01-11 | Prop.3.4, pp.11–12, Eq.(7)；Thm.3.9, p.14；Fact 3.11 / Thm.3.12, pp.15–17；Prop.4.1 / Thm.4.2, pp.18–19；Prop.6.1, p.28 | 位相・作用・有限 abelian cover・向きを本文照合。全論文の独立証明検証ではない。 |

取得時点の S24 / S25 の arXiv 履歴は v1 のみ。ここでは arXiv 本文を一次資料として使用し、査読出版の有無は確認していない。「近年の構成」は上記の実在する定理を指し、未確認の最近の RH claim を含めない。

## 空間、軌道、持ち上げ

記号の衝突を避け、

\[
Y=\mathbb Q^\times\backslash\mathbb A_{\mathbb Q},\qquad
X=Y/\widehat{\mathbb Z}^{\times},\qquad \pi:Y\to X,
\]
\[
C_p\simeq\mathbb R_+^\times/p^{\mathbb Z},\qquad
H_p=\prod_{q\ne p}\mathbb Z_q^\times
\simeq\pi_1^{\mathrm{et}}(\operatorname{Spec}\mathbb Z_{(p)})^{\mathrm{ab}}
\]

とする。S16 Lemma 5.1 の点の記述では \(C_p\) は \(\mathbb Z[1/p]\) と順序群として同型な実数の部分群の族。\(u=\log\lambda\) における primitive period は \(L_p=\log p\)。S24 Theorem 1.1 / §2 により

\[
M_p:=\pi^{-1}(C_p)\simeq
(H_p\times\mathbb R)/\big((h,u)\sim(ph,u+L_p)\big). \tag{1}
\]

具体的代表元は \(a_p=0, a_q=h_q\in\mathbb Z_q^\times\ (q\ne p), a_\infty=e^u>0\)。この規格化を保つ有理数倍は正の \(p^{\mathbb Z}\) だけなので (1) が直接得られる。全 \(Y,X\) の難しい商位相と違い、\(M_p\) 自体はコンパクト Hausdorff な位相的 suspension である。局所的には \(H_p\times\) 区間で、無限 profinite fiber をもつ。離散 fiber の通常の covering space と同一視しない。

S24 における Frobenius は \(\overline{\mathbb F}_p\) 上の \(x\mapsto x^p\) という **arithmetic Galois Frobenius** の像。対応する cyclotomic action は \(\zeta_m\mapsto\zeta_m^p\), \(p\nmid m\)。特性 \(p\) の scheme の absolute Frobenius morphism、曲線の \(H^1\) 上の weight-one 作用、S16 の characteristic-one semiring 上の Frobenius は、この同定だけでは同じ作用にならない。

## 向き、帰還、monodromy、holonomy

以下は (1) からの独立な符号確認。

\[
\varphi_v[h,u]=[h,u+v],\qquad
\varphi_{L_p}[h,0]=[h,L_p]=[p^{-1}h,0]. \tag{2}
\]

したがって **増大する log-scale の帰還写像は \(h\mapsto p^{-1}h\)**。逆向き \(v\mapsto-v\) なら \(h\mapsto ph\)。S25 Prop.3.4 の証明 p.12 は deck generator を \((y,t)\mapsto(\phi(y),t+1)\) と定義し、\(\phi(h)=ph\) を monodromy と呼ぶ。この deck convention と、実際に選んだ正の時間での return map を区別すれば逆符号は明示的に管理できる。geometric Frobenius は arithmetic Frobenius の逆である。

fiber slice \(H_p\times\{0\}\) は suspension の topological transversal。これは bundle projection \(M_p\to C_p\) の全周にわたる連続 section とは違う。後者は存在しない：区間上の section の fiber 座標は連続性と全不連結性から一定となるが、端点で \(h=ph\) は不可能。

さらに \(p^k\ne1\) in \(H_p\) for every nonzero integer \(k\)。従って base の周期軌道 \(C_p\) の各点を full fiber へ持ち上げても、その scaling trajectory 自体は周期軌道にはならない。式 (2) の反復は holonomy pseudogroup / suspension return として解釈できるが、滑らかな実横断接束上の微分 \(D\varphi_{L_p}\) は供給されていない。S25 Prop.6.1 の semilocal homotopy quotient と codimension-one lamination は別の構成であり、それだけでこの不足を埋めない。

## 有限 abelian quotient の正確な範囲

S25 Thm.3.9 / 3.12：有限 abelian 拡大 \(L/\mathbb Q\)、\(G=\operatorname{Gal}(L/\mathbb Q)\)、class-field map \(\chi:\widehat{\mathbb Z}^{\times}\twoheadrightarrow G\) に対する associated cover を用いる。\(p\) が不分岐なら fiber は \(G\)、deck monodromy は \(\chi(p)=\operatorname{Frob}_p\)。分岐した \(p\) にはこの principal-\(G\)-bundle の主張をそのまま使えない。

独立な帰結：\(f_p=\operatorname{ord}(\operatorname{Frob}_p)\) とすると、各 lifted circle の長さは \(f_p\log p\)、個数は \(|G|/f_p\)。これらは \(p\) 上の素点に対応する。full \(H_p\) の suspension と有限 quotient の閉軌道を混同しない。

## prime powers、Euler logarithm、Gamma と poles

以下は通常の Euler 積からの等式であり、mapping torus 上の Fredholm determinant を構成したとの主張ではない。

\[
\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{e^{-skL_p}}k,\qquad
-\frac{\zeta'}{\zeta}(s)=\sum_p\sum_{k\ge1}L_p e^{-skL_p},
\qquad\Re s>1. \tag{3}
\]

この半平面では絶対・局所一様収束し、対数の枝は \(\Re s\to+\infty\) で 0 となるもの。primitive orbit の \(k\)-fold traversal は長さ \(k\log p\)、fiber 上では \(p^{\pm k}\) の反復。微分後の算術重みは **\(\log p\)** で、\(k\log p\) ではない。critical strip に同じ絶対収束表示を延長したとはいわない。

完成因子を明示すれば

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\xi(s)=\tfrac12s(s-1)\Lambda(s),
\]
\[
-\xi'/\xi(s)=\sum_{p,k\ge1}(\log p)p^{-ks}
+\tfrac12\log\pi-\tfrac12\psi(s/2)-1/s-1/(s-1),\quad\Re s>1. \tag{4}
\]

ここで \(\psi=\Gamma'/\Gamma\)。Gamma の archimedean 項と \(0,1\) の polar correction は prime circles の (3) だけにはない。零点側との exact trace formula には archimedean local distribution と pole subtraction を含む別の既知入力が必要。S25 の有限素点 mapping-torus 定理は、その正値性・trace-class 性・零点の全重複度を証明する定理ではない。

## 自然な正測度が証明する範囲

(1) から \(dm_{H_p}\,du/L_p\) が suspension 上の不変確率測度となる。従ってその \(L^2\) 上の Koopman flow は unitary。この直接確認は RH を仮定しないが、**ここに ζ の全零点を同定する定理はない**。Haar 正性を純性の不足の解決として流用できない。

また \(H_p\) の任意の互換な translation-invariant metric では \(h\mapsto ph\) は isometry。これは profinite fiber の距離に関する等長性であり、\(\Re\rho-1/2\) と等しい実 transverse Lyapunov exponent を得たことではない。もともと unitary な Koopman \(U_v\) を \(e^{-v/2}U_v\) に置き換えるとノルムは \(e^{-v/2}\) 倍になる。中心 \(1/2\) の規格化をする根拠・零点との同定は別途必要。

## 指定 functional-role fields

| Field | 判定 |
|---|---|
| Continuous flow | \(\varphi_v[h,u]=[h,u+v]\), scaling flow の実際の制限。 |
| Prime periodic orbit | base \(C_p\)。full lift の trajectory は一般に非周期。 |
| Orbit length | \(\log p\)（自然対数時間）。 |
| Prime-power iterates | \(k\log p\)、deck \(p^k\)、正時間 return \(p^{-k}\)。 |
| Frobenius relationship | arithmetic Galois Frobenius と deck monodromy。向き反転で return と一致。 |
| Normalized flow | 零点を担う空間での \(1/2\) 規格化は未供給。 |
| Candidate transverse exponent | profinite suspension に smooth-real exponent は未定義。 |
| Relation to Re(rho)-1/2 | 未証明。局所 orbit / finite-cover theorem の結論ではない。 |
| Invariant metric | Haar-\(L^2\) と profinite invariant metric は存在。必要な零点表現の metric とは未同定。 |
| Arithmetic source of metric | compact abelian group の Haar 測度。weight-one polarization ではない。 |
| Known prior art | S16 / S24 / S25 の上記の限定された定理。 |
| New content | なし。向きと適用域の監査、初等的帰結の確認。 |
| RH-equivalent assumption? | mapping torus 自体には不要。全零点の exact 表現に positive normalized invariant metric を追加すれば、まさに未解決の purity 義務を含む。 |
| Counterexample status | 上記の既知構成への反例なし。局所 Haar 正性からの RH 推論には零点同定がない。 |
| Decision | Level 1 の既知 input として保持。smooth transverse growth / 全零点対応 / 同じ空間での positive metric を既証明へ昇格させない。 |

独立検算は商の代表元、向き、有限 quotient の周期、Euler 微分、Haar 不変性に限定。既存論文の全定理を全面的に再証明したとは記録しない。
