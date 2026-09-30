**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/scale_flow/notes/padic_transverse_audit.md` · Original SHA-256: `24f5964a68173aa6724b90aed4710aeb5576b1cad54fad1361fa997a18a807a7`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# p-adic 横断作用の追加監査

2026-09-29。結論：literal な「actual arithmetic flow には幾何的横断作用・成長が一切ない」は誤り。vanishing-\(p\) stratum の算術 normal model では正時間の valued exponent は厳密に \(+1\)。ただし、滑らかな実横断微分や ζ の全零点の \(\Re\rho-1/2\) との同定を得たわけではない。既知構造の限定監査であり、新規性・RH の距離短縮を主張しない。

## 一次本文の scope

Connes–Consani, *Knots, primes and class field theory*, [arXiv:2501.06560v1 PDF](https://arxiv.org/pdf/2501.06560v1), 2025-01-11。Introduction p.3 の “Isotropy Subgroup” / “Explicit Formulas” 段落は、\(K_v^\times\) の transverse space \(K_v\) への作用と、その kernel の局所 diagonal trace

\[
\int_{K_v}\delta(x-\lambda x)\,dx=|1-\lambda|_v^{-1}
\]

を明記する。これは導入の既知構造の説明で、RH や正値性を証明する numbered theorem ではない。同頁は商 \(Y_K\) の singular topology にも注意する。以下はこの説明と Prop.3.4（pp.11–12、Eq.(7)）の規格化に対する直接検算。[版固定 HTML の該当節](https://arxiv.org/html/2501.06560v1#S1)。

## 1. \(p\)-成分を動かす正確なモデル

\[
H_p=\prod_{q\ne p}\mathbb Z_q^\times,\quad L=\log p,\quad
N_p=\mathbb Q_p\times H_p\times\mathbb R.
\]

\(n=(z,h,u)\) を adele
\[
j(n)_p=z,\qquad j(n)_q=h_q\ (q\ne p),\qquad
j(n)_\infty=e^u
\]
で表す。二つのこの形の adele が有理数倍なら、その比は正で全 \(q\ne p\) において unit、従って \(p^m\)。よって

\[
E_p=N_p/\mathbb Z,\qquad
(z,h,u)\sim(pz,ph,u+L)                                      \tag{1}
\]

から \(Y=\mathbb Q^\times\backslash\mathbb A_\mathbb Q\) への写像は **連続かつ集合として単射**。\(u\) の translation により \(\mathbb Z\)-作用は自由・proper なので、\(E_p\) 自身は locally compact Hausdorff。\(z=0\) の zero section は既知の \(M_p=\pi^{-1}(C_p)\)。\(E_p\to M_p\) は transition scalar \(p\) の一次元 \(\mathbb Q_p\)-vector bundle として定義できる。

これは vanishing-\(p\) idele-class orbit に沿う arithmetic normal model。全 adele 商の smooth normal bundle や開近傍 chart と宣言する必要はない。

## 2. 帰還 germ と指数

実 scaling は \(\varphi_v[z,h,u]=[z,h,u+v]\)。slice \(u=0\) で一周後に代表元を戻すと

\[
R(z,h)=(p^{-1}z,p^{-1}h),\qquad
R^k(z,h)=(p^{-k}z,p^{-k}h).                                 \tag{2}
\]

従って
\[
|p^{-k}z|_p=p^k|z|_p,\qquad
\frac{\log(|p^{-k}z|_p/|z|_p)}{kL}=1\quad(z\ne0).             \tag{3}
\]

逆時間では \(-1\)。\(R\) は全 \(\mathbb Q_p\times H_p\) の homeomorphism。固定した小 ball \(B_r(0)\) に戻り続ける主張ではない：\(k\) 回の出力を \(B_r\) に入れる入力域は \(B_{r/p^k}\)。従って bounded chart での反復と germ の区別も明示できる。

full lift では \(h\) も移るため、(2) は「同一の lifted periodic point を固定する Poincaré map」ではない。閉じた base orbit \(C_p\) を回る suspension return / holonomy between fibers である。\(H_p\) 内の移動は不変距離に関して等長でも、追加した \(z\)-方向は拡大する。先の mapping-torus note の fiber 内の等長性と矛盾しない。

より intrinsic な直接確認として、

\[
\mathcal N([z,h,u])=e^u|z|_p,\qquad
\mathcal N(\varphi_v e)=e^v\mathcal N(e)                      \tag{4}
\]

は (1) の deck transformation に不変な、連続で正の fiber norm（zero vector を除く）。\(e^{u+L}|pz|_p=e^u|z|_p\) による。従って全時間の normal growth も \(+1\)。compact base \(M_p\) 上で正の連続因子だけ異なる fiber norm に替えても、その因子の上・下界があるので漸近指数は同じ。単に非有界な frame 変更から捏造した指数ではない。

## 3. 商位相の限界：このモデルは ambient chart ではない

\(H_p\) は全ての他素点で unit という条件を課すため、\(j(N_p)\) は adele 空間の開集合ではない。それだけで embedding の否定にはならないが、実際に (1) の単射は ambient \(Y\) の部分空間への topological embedding ではない。次の独立な CRT 検算で確認できる。

固定した \(z\ne0,\ h\in H_p\) を取る。\(M_j\) を \(p\) 以外の最初の \(j\) 個の素数の \(j\) 乗の積とする。十分大きい \(k_j\) を取り、CRT により正整数 \(a_j\) を
\[
a_j\equiv1\pmod{p^j},\qquad
a_j\equiv p^{k_j}\pmod{M_j},\qquad
|a_j-p^{k_j}|\le p^jM_j
\]
と選ぶ。\(p^{k_j}>j p^jM_j\) とすれば \(r_j=a_j/p^{k_j}\to1\) in \(\mathbb R\) and in every \(\mathbb Q_q,\ q\ne p\)、また \(a_j\to1\) in \(\mathbb Q_p\)。

\(b_j=j(p^{k_j}z,h,0)\) とおくと、adele topology で
\[
b_j\longrightarrow j(0,h,0),\qquad
r_j b_j\longrightarrow j(z,h,0).
\]
後者の restricted-product 条件も満たす：\(r_j\) の分母は \(p\) の冪だけなので、全 \(q\ne p\) で \(r_jh_q\in\mathbb Z_q\)。商では \(b_j\) と \(r_jb_j\) は同じ点なので、この列は \(Y\) 内で二つの異なる点に収束する。一方 \(E_p\) は Hausdorff で、列の極限は zero-section の点だけ。従って (4) の norm を ambient quotient topology の連続な距離・norm とみなすことはできない。

この点は p-adic action/groupoid の normal cocycle を否定しない。許される主張は「actual adelic representatives とその算術 transition から得る normal model / local transverse action」であり、「全 \(Y\) の通常の manifold chart」ではない。

## 4. local trace と half-density

加法 Haar 測度 \(dx\) を固定する。 \(\lambda\ne1\) なら change of variables だけで
\[
\int_{\mathbb Q_p}\delta((1-\lambda)x)\,dx
 =|1-\lambda|_p^{-1}.                                      \tag{5}
\]

これは Schwartz kernel の distributional diagonal evaluation。\(L^2(\mathbb Q_p)\) 上の非コンパクト dilation operator が trace class という主張ではない。特に \(\lambda=1\) はこの式の適用外で、全 explicit formula には distribution の正規化・正則化を別に保持する。

unitary half-density normalization
\[
(U_\lambda f)(x)=|\lambda|_p^{1/2}f(\lambda x)
\]
を用いると、同じ局所量は
\[
\frac{|\lambda|_p^{1/2}}{|1-\lambda|_p}
 =p^{-k/2}\qquad(\lambda=p^k\text{ または }p^{-k},\ k\ge1).  \tag{6}
\]

ここでは \(1/2\) は Haar-Jacobian の平方根として独立に現れる。しかし (6) は全零点の実部 \(1/2\) を示さず、Gamma・pole terms、global arithmetic quotient、zero multiplicity、positivity の不足も解決しない。局所の scalar multiplier \(p^{-1}\) と Galois Frobenius の fiber translation は、同じ規格化から現れる別の作用である。

## 判定

- **PASS:** actual \(p\)-adic transverse scalar action、return (2)、normal valued exponent \(+1\)、reverse exponent \(-1\)、局所 kernel 因子 (5)、half-density 因子 (6)。
- **REJECT:** literal「幾何的横断作用・成長がない」。\(H_p\) fiber 内だけの計算から全 normal 方向を除外できない。
- **限定:** この model の算術的実在性と ambient quotient の chart / topology は別。full lift 上の周期点を固定する smooth-real Poincaré differential とは呼ばない。
- **OPEN / NOT SUPPLIED:** \(\alpha=\Re\rho-1/2\) をこの normal growth と exact に同定する zero-bearing representation、そこに必要な invariant positive metric / purity。既知の局所式を RH-equivalent global input の証明に昇格させない。

編集は本ノートのみ。Phase III / IV と既存 mapping-torus note は変更していない。
