**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/scale_flow/notes/independent_audit.md` · Original SHA-256: `d6c6550d5f8abfceb6dff40db400e1389a69e4b580d2f6463dec2765ceb91ace`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Scale-flow 独立監査：SG3、SG5 と局所 Haar spectrum

監査日：2026-09-29。対象は新規 `research/scale_flow` のみ。Phase III/IV の文書・状態は変更していない。

対象：`notes/spectral_growth.md` の SG3、SG5、SG6、および `notes/frobenius_mapping_torus.md` の局所 torus 規約。既知補題を独立に検算した記録であり、新規性・RH の証明を主張しない。

**判定：SG3 と SG5 は PASS。局所 Haar モードの表示と完全性も PASS。** ただし「指標が有限像」の根拠には compact abelian だけでなく **profinite** を使う。また、以下の完全固有関数系は compact resolvent を与えない。局所 Haar 表現と全零点を保持する算術表現との同定は未供給である。

## IA1. SG3：正形式の完備化と全零点の保持

仮定を省略せず記す。複素線形空間 (E) に全実時間の群 (W_u)、半正定値 Hermitian form (q) があり、
\[
q(W_uv,W_uw)=q(v,w),\qquad
q(W_uv-v,W_uv-v)\longrightarrow0\quad(u\to0).
\]
各非自明零点 \(\rho\) に非零の線形汎関数 \(\ell_\rho\) があり、
\[
\ell_\rho(W_uv)=e^{(\rho-1/2)u}\ell_\rho(v),\qquad
|\ell_\rho(v)|\le C_\rho\sqrt{q(v,v)}.
\]
このとき radical \(N_q=\{v:q(v,v)=0\}\) は不変で、\(E/N_q\) の Hilbert 完備化に \(W_u\) は unitary として延長する。onto 性は \(W_{-u}\) の存在による。core 上の連続性と isometry により延長は強連続である。

汎関数は radical を消し、完備化上でも非零かつ有界である。\(\alpha=\Re\rho-1/2\) とすると、unitary による前合成は双対 norm を保存するので
\[
\|\ell_\rho\|=\|\ell_\rho\circ W_u\|
 =e^{\alpha u}\|\ell_\rho\|.
\]
従って \(\alpha=0\)。零点ごとの \(C_\rho\) は一様でなくてよい。

厳密な範囲は次の通り。

- 実部ゼロという帰結だけなら強連続性は不要。強連続性は閉 generator と Stone の定理に必要である。この区別は現ノートに反映済み。
- 得られる generator \(G\) は \(G^*=-G\)。\(\Theta=G+\tfrac12I\) なら同じ domain で \(\Theta^*=I-\Theta\)。元の形式微分作用素との一致・core 性は別途必要。
- 全ての零点が少なくとも一つの非零 bounded functional として残れば、実部の結論には足りる。逆に「Hilbert spectrum の全てが零点である」、全 multiplicity の trace 保存、generalized eigenvector の保存まではこの補題から出ない。
- 既存 test-space の全零点汎関数が、選んだ新しい norm に有界であることは自動でない。正性だけ、形式 adjoint 関係だけ、critical-line 零点だけの保持を代入できない。

従ってこれは正しい条件付き補題であるが、必要な算術 Hilbert norm を構成した結果ではない。

## IA2. SG5：一周期の unitary return

同じ Hilbert 空間・同じ norm 上の \(C_0\) 群 \(W_u\) に対して、ある \(L>0\) の \(W_L\) が unitary とする。局所有界性により
\[
M=\sup_{0\le r\le L}\|W_r\|<\infty.
\]
全ての \(u\in\mathbb R\) を \(u=nL+r\), \(n\in\mathbb Z\), \(0\le r<L\) と書く。\(W_L^n\) が正負の整数 \(n\) とも unitary なので \(\|W_u\|\le M\)。逆時間も用いて
\[
M^{-1}\|v\|\le\|W_uv\|\le M\|v\|.
\]
非零 \(v\) の指数は両時間方向でゼロである。

平均内積
\[
\langle v,w\rangle_{\rm av}
 =\frac1L\int_0^L\langle W_tv,W_tw\rangle\,dt
\]
は正定値で、\(M^{-2}\|v\|^2\le\|v\|_{\rm av}^2\le M^2\|v\|^2\)。被積分関数が \(L\)-periodic であるため、任意時間の \(W_u\) に不変である。等価 norm なので完備性と強連続性も維持される。

元の norm 自体が全時刻で不変とは限らない。ノートの \(S R_{2\pi u/L}S^{-1}\) は正しい反例。同じ空間・同じ norm で \(W_{\log2},W_{\log3}\) が unitary なら、稠密な加法部分群と強連続性により全時刻 unitary となる。しかし、異なる素数の異なる局所 fiber の return operator はこの仮定を満たしたことにならない。

周期 cocycle の記述も、周期系の基本解という仮定の下で正しい。\(X(t+L)=X(t)M\) と \(M^*G_0M=G_0\) から、\(G(t)=X(t)^{-*}G_0X(t)^{-1}\) は periodic。無限次元では逆作用素の有界性と一様 coercivity が別途必要である。

## IA3. 局所 torus の規約と測度

算術的同定は既知の一次資料を採用する。Connes–Consani の [2024 年版 Theorem 1.1](https://arxiv.org/html/2401.08401v1) と [2025 年版 Proposition 3.4、Theorems 3.9・3.12](https://arxiv.org/html/2501.06560v1) が局所 mapping torus と abelian Galois 解釈の入力である。ここでその算術同定全体を再証明したとはしない。以下の Haar spectral 計算は表示された torus から直接導く。

固定素数 \(p\) について
\[
H_p=\prod_{q\ne p}\mathbb Z_q^\times,\quad L=\log p,\quad
M_p=(H_p\times\mathbb R)/((h,u)\sim(ph,u+L)),
\qquad \phi_v[h,u]=[h,u+v].
\]
\(p\) は各 \(\mathbb Z_q^\times\), \(q\ne p\), の単元である。正規化 Haar 測度 \(dh\) と \(du/L\) を基本領域 \(0\le u<L\) に使う。gluing の \(h\mapsto ph\) が Haar を保存するので、これは \(\phi_v\)-不変の確率測度を与える。

forward-pullback の規約
\[
(K_vF)(m)=F(\phi_v m)
\]
を採用する。このとき \(K_v\) は \(L^2(M_p)\) 上の強連続 unitary 群。逆向き Koopman 規約を採れば、以下の周波数の符号が全て反転するだけである。

正時間 \(L\) の return は \([h,L]=[p^{-1}h,0]\)。従って断面上で \(K_L\) は \(F(h)\mapsto F(p^{-1}h)\)。算術 Frobenius を \(p\) と記す deck 方向との違いは、既存ノートで明示された向きの選択と整合する。

## IA4. 指標、周波数、完全性

\(H_p\) は compact metrizable **profinite abelian** group である。連続指標 \(\chi:H_p\to S^1\) は有限像を持つ。例えば \(S^1\) の十分小さい弧は非自明部分群を含まない。連続性と profinite 性により、その逆像に含まれる開部分群を取れるので、\(\ker\chi\) は開、従って有限指数である。

この議論の profinite 仮定は必要である。一般の compact abelian group の指標が有限像とは限らない（\(S^1\) の恒等指標）。本件の具体的 \(H_p\) では有限像の結論は正しい。

\(\theta_\chi=\arg\chi(p)\in[-\pi,\pi)\) とし、
\[
\omega_{\chi,n}=\frac{2\pi n-\theta_\chi}{L},\qquad
\Phi_{\chi,n}(h,u)=\chi(h)e^{i\omega_{\chi,n}u},
\quad n\in\mathbb Z.
\]
すると
\[
\Phi_{\chi,n}(ph,u+L)
 =\chi(p)e^{i\omega_{\chi,n}L}\Phi_{\chi,n}(h,u)
 =\Phi_{\chi,n}(h,u).
\]
従って mode は torus に降下し、\(K_v\Phi_{\chi,n}=e^{i\omega_{\chi,n}v}\Phi_{\chi,n}\)。全周波数は実数である。特に \(e^{i\omega L}=\chi(p)^{-1}\) は IA3 の return と一致する。

**全局所 \(L^2\) における完全性。** \(H_p\) の指標は \(L^2(H_p,dh)\) の完全正規直交系である。これは compact abelian Fourier 理論、または指標による点の分離と Stone–Weierstrass から従う。基本領域で
\[
L^2(M_p)\simeq L^2(H_p\times[0,L),dh\,du/L)
 \simeq\bigoplus_{\chi\in\widehat H_p}L^2([0,L),du/L).
\]
各 \(\chi\) 成分において \(e^{-i\theta_\chi u/L}\) の乗算は unitary であり、通常の Fourier basis \(e^{2\pi inu/L}\) を上の quasi-periodic basis に移す。従って全 \((\chi,n)\) の mode は完全正規直交系である。raw \(L^2\) では端点は零測度であり、境界値の条件を全代表元へ課す必要はない。境界条件は generator の domain や連続代表元を述べる際に現れる。

\(K_v=e^{ivA_p}\) と置くと、
\[
D(A_p)=\left\{\sum_{\chi,n}c_{\chi,n}\Phi_{\chi,n}:
 \sum_{\chi,n}\omega_{\chi,n}^2|c_{\chi,n}|^2<\infty\right\},
\qquad A_p\Phi_{\chi,n}=\omega_{\chi,n}\Phi_{\chi,n}.
\]
これは自己共役で、固有関数系は完全。ただし作用素の spectrum は周波数集合の閉包であり、固有値が全て孤立して有限重複度という主張ではない。

特に **compact resolvent ではない**。\(\widehat H_p\) は無限集合で、各 \(\chi\) の \(n=0\) mode は \(|\omega_{\chi,0}|\le\pi/L\) を満たす。従って有界周波数帯に無限個の直交固有ベクトルがある。\((A_p-i)^{-1}\) のそれらの像は一様にゼロから離れた norm を持つ直交列なので、compact ではない。完全固有関数系の存在を compact resolvent やリーマン零点型の固有値計数と混同できない。

## IA5. 正性・重さ・全零点への射程

定数 mode \(\chi=1,n=0\) は周波数ゼロで存在する。既存の unitary 群を形式的に
\[
\widetilde K_v=e^{-v/2}K_v
\]
へ変えると \(\|\widetilde K_v\|=e^{-v/2}\)。非零時刻では unitary でなく、生成作用素は \(iA_p-\tfrac12I\)。算術零点表現で用いる半密度正規化を、既に weight 0 の局所 Haar 表現へそのまま適用してよい理由はない。

この独立計算が与えたのは、既知の実局所 mapping torus 上の Haar 表現と、その全局所 \(L^2\) の spectral decomposition である。有限体曲線の polarized \(H^1\) の weight 1 純性ではない。幾何学的な横断 Lyapunov exponent のゼロもここからは述べていない。

局所 \(L^2(M_p)\) の完全性と、\(\zeta\) の全零点を保持する global quotient の完全性は別の命題である。必要なのは同じ正 Hilbert 空間における全零点の非零 bounded functional、群との intertwining、定義域、Gamma と極項、要求する場合は multiplicity/trace の一致である。今回それらを構成していない。

**監査結論。** 既知 SG3/SG5 の適用条件は正しく分離されている。局所周波数の降下条件・符号・Haar 正性・完全性は直接証明できる。追加すべき限定は、有限像には profinite 性を用いること、および局所 generator は compact resolvent を持たないこと。局所 unitary return を全零点空間へ移す未証明の比較は残り、今回の計算は RH に新しい結論を与えない。

## IA6. 追加監査：p-adic normal model と half-density trace

追加対象は親から提示された次の具体式である。
\[
E_p=(\mathbb Q_p\times H_p\times\mathbb R)/
 ((z,h,u)\sim(pz,ph,u+L)),\qquad L=\log p.
\]
零断面は \(M_p\)。この rational-action quotient model の上で
\[
N([z,h,u])=e^u|z|_p
\]
は well-defined である。実際、任意 \(m\in\mathbb Z\) に対し
\[
e^{u+mL}|p^m z|_p=e^up^m p^{-m}|z|_p=e^u|z|_p.
\]
各 fiber でこれは \(\mathbb Q_p\) の ultrametric norm の正スカラー倍である。lifted flow を
\(\phi_v[z,h,u]=[z,h,u+v]\) と取ると
\[
N(\phi_v[z,h,u])=e^vN([z,h,u]).
\]
したがって \(z\ne0\) の valued normal growth exponent は正確に \(+1\)。正時間一周を断面へ戻すと \(z\mapsto p^{-1}z\) であり、\(|p^{-1}z|_p=p|z|_p\)、\(\log p/L=1\) とも一致する。

**範囲の限定。** これは明示した quotient model での厳密計算である。\(E_p\) が full adèle class space \(Y\) の滑らかな normal bundle、あるいは全零点の表現であるとは証明していない。さらに、下記 IA7 の通り、この代表元からの単射は topological embedding ですらなく、ambient open chart ではない。従って「この自然な rational-action normal model まで含めて全ての transverse growth が禁止される」という literal な命題は反証されるが、未定義の full \(Y\) の微分幾何学を補ったとはしない。特に、この \(+1\) は \(\Re\rho-\tfrac12\) ではなく、RH に対する反例ではない。局所 Koopman の正不変内積と normal cocycle の norm growth は異なる対象である。

half-density の係数も独立に一致する。\(\mathbb Q_p\) の加法 Haar 測度 \(dz\) に対して
\[
(U_\lambda f)(z)=|\lambda|_p^{1/2}f(\lambda z),
\qquad \lambda\in\mathbb Q_p^\times
\]
は \(L^2(\mathbb Q_p,dz)\) 上 unitary。\(\lambda\ne1\) の kernel の diagonal における distributional integral は
\[
\int_{\mathbb Q_p}|\lambda|_p^{1/2}
       \delta_0((1-\lambda)z)\,dz
 =\frac{|\lambda|_p^{1/2}}{|1-\lambda|_p}.
\]
\(\lambda=p^k\), \(k\ge1\), なら分母は \(1\)、分子は \(p^{-k/2}\)。\(\lambda=p^{-k}\) なら分母は \(p^k\)、分子は \(p^{k/2}\)。いずれも \(p^{-k/2}\) を得る。

これは通常の Hilbert trace ではない。\(U_\lambda\) は無限次元 Hilbert 空間上の unitary で compact でなく、trace-class でもない。\(\lambda=1\) は固定点退化によりこの式の対象外。また、この一つの local fixed-point coefficient と全 explicit formula の global trace identity は別であり、\(\log p\)、他の場所、Gamma、極項、正規化の gluing をこの計算だけから供給したとはしない。

追加判定：提示された norm と half-density の二式は **PASS**。幾何学的 normal growth の全面禁止と、全零点 spectral character の \(\alpha=0\) という未解決の禁止命題は、結論として分岐させる必要がある。

## IA7. 完成した p-adic ノートの CRT 非 embedding 証明

追加読取対象：`notes/padic_transverse_audit.md` 全体、特に §3。**PASS**。算術代表元
\[
j(z,h,u)_p=z,\quad j(z,h,u)_q=h_q\ (q\ne p),\quad
j(z,h,u)_\infty=e^u
\]
の map は連続である。二つの代表元を結ぶ有理数は正で、全 \(q\ne p\) で単元だから \(p^m\)。従って \(E_p\to Y\) は集合として単射。\(u\) 方向の平行移動により deck 作用は proper で、\(E_p\) は Hausdorff である。

固定 \(z\ne0,h\in H_p\) に対して、\(M_j\) を \(p\) 以外の最初の \(j\) 素数の \(j\) 乗の積とする。CRT の二条件
\[
a_j\equiv1\pmod{p^j},\qquad
a_j\equiv p^{k_j}\pmod{M_j}
\]
は互いに素な法なので解を持つ。\(p^{k_j}>j p^jM_j\) と取り、法 \(p^jM_j\) の解を \(p^{k_j}\) の距離 \(\le p^jM_j\) に選べるので、\(a_j>0\) かつ \(r_j=a_j/p^{k_j}\to1\) in \(\mathbb R\)。各固定 \(q\ne p\) に対し十分大きい \(j\) では \(r_j-1\in q^j\mathbb Z_q\)、また \(a_j\to1\) in \(\mathbb Q_p\)。

\(b_j=j(p^{k_j}z,h,0)\) とすると
\[
b_j\longrightarrow j(0,h,0),\qquad
r_jb_j\longrightarrow j(z,h,0)
\]
は **adele topology** で成立する。後者では \(r_j\) の分母が \(p\) の冪だけであるため、全 \(q\ne p\) で \(r_jh_q\in\mathbb Z_q\)。従って各成分の収束だけでなく、restricted product の一様な integrality 条件も満たす。\(p\)-成分は \(a_jz\to z\)、実成分は \(r_j\to1\) である。

商 \(Y\) で \(b_j,r_jb_j\) は同じ点である。その点列が image 内の相異なる二点へ収束する一方、\(E_p\) 内では Hausdorff 性により同じ現象は起きない。従って連続単射 \(E_p\to Y\) は **topological embedding ではない**。実際、\(\mathcal N([p^{k_j}z,h,0])=p^{-k_j}|z|_p\to0\) に対し、第二の image 極限の norm は \(|z|_p>0\) なので、\(\mathcal N\) は image の ambient subspace topology に関して連続にはならない。

この確認により、単なる「embedding 未証明」より強い限定が得られる。許されるのは actual adelic representatives と算術 transition に基づく normal groupoid model の記述であり、通常の ambient manifold chart やその global metric への移行ではない。原典の local transverse action の説明、有限場所の distributional trace、全零点の正 Hilbert 表現は依然別の段階である。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/scale_flow` — SOURCE REFERENCE NOT INCLUDED
