**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/weighted_prime_halfspace/notes/selberg_delange_endpoint.md` · Original SHA-256: `dde9518432397b127609fab6de0f4af633f01b22e75f7070dae60df678c782fa`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Selberg–Delange の平方自由パリティ端点

記録日: 2026-09-30。対象は \(\mu^2(n)z^{\omega(n)}\) の算術和。一次資料の該当定理と下記の直接計算だけを確認した限定監査であり、論文全体の独立再証明・新規性・RH の進展は主張しない。旧 track のファイルは変更しない。

**判定:** \(z=-1\) では局所漸近展開の全係数が厳密に消える。しかし有限 \(X\) の和は Mertens 和そのもので、必要な相殺は剰余に全て残る。「bulk の漸近係数が消える」から、有限和の境界局在・低次元化・固定冪節約は導けない。

## 1. 正しい算術族と積の領域

\[
 f_z(n)=\mu(n)^2z^{\omega(n)},\qquad
 S_z(X)=\sum_{n\le X}f_z(n),\qquad z^0=1.
\]

平方自由性から、\(\Re s>1\) で絶対収束する直接の恒等式は

\[
 F(s,z)=\sum_{n\ge1}\frac{f_z(n)}{n^s}
 =\prod_p(1+zp^{-s})=\zeta(s)^zG(s,z),\qquad
 G(s,z)=\prod_p(1+zp^{-s})(1-p^{-s})^z.                 \tag{SD1}
\]

\((1-p^{-s})^z=\exp(z\log(1-p^{-s}))\) は \(\Re s>0\) で通常の冪級数による対数を選ぶ。\(|z|\le R,\ \Re s\ge1/2+\eta\) では各大素数因子が \(1+O_{R,\eta}(p^{-2\Re s})\)。有限個の小素数因子を残せば、\(G\) は \(\Re s>1/2\) に局所一様に収束する正則積であり、\(z\) にも正則である。因子の零点は許すので、ここで \(\log G\) の大域的存在を仮定しない。\(\zeta(s)^z\) の表示は零点を横断する大域的一価表示ではない。

特に因子ごとに
\[
 G(s,-1)=\prod_p\frac{1-p^{-s}}{1-p^{-s}}=1,\quad
 F(s,-1)=\frac1{\zeta(s)},\quad S_{-1}(X)=M(X).         \tag{SD2}
\]

これは \(\sum z^{\omega(n)}\) と異なる。後者の素数因子は
\[
 1+z\sum_{\nu\ge1}p^{-\nu s}
 =\frac{1+(z-1)p^{-s}}{1-p^{-s}}.
\]
\(z=-1\) でも平方を除かず、係数は \((-1)^{\omega(n)}\) である。\(\mu\) や \((-1)^{\Omega(n)}\) と置き換えてはいけない。

## 2. 局所係数の直接計算

\(Z(s)=(s-1)\zeta(s)\) は \(s=1\) の十分小さい円板で正則・非零、\(Z(1)=1\)。そこで
\[
 B(s,z)=\frac{Z(s)^zG(s,z)}s
       =\sum_{j\ge0}h_j(z)(s-1)^j,\qquad
 \lambda_j(z)=\frac{h_j(z)}{\Gamma(z-j)}.              \tag{SD3}
\]

Perron 核の局所項は \(X e^{w\log X}w^{j-z}h_j(z)\,dw\)。Hankel 積分の reciprocal-Gamma 因子から
\[
 X(\log X)^{z-1}\sum_{j=0}^J
             \frac{\lambda_j(z)}{(\log X)^j}         \tag{SD4}
\]
という形になる。この説明だけでは Perron 積分の残りを評価していないため、剰余には次節の定理を別に使う。

\(h_j(-1)\) は有限で、\(1/\Gamma(-1-j)=0\) なので \(\lambda_j(-1)=0\) は全 \(j\ge0\) で厳密。これは既知であり、de la Bretèche–Tenenbaum, *Remarks on the Selberg–Delange method*, 著者訂正版 PDF p3、(1.9)–(1.10) 直後も非正整数の場合の全係数消失を明記する。同頁 Theorem 1.2 は複素指数を許す。[著者 PDF](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf)

同論文は Acta Arith. 200.4 (2021), 349–369。参照した著者 PDF は出版版への小修正ありと明記され、arXiv v1 と同一と仮定していない。版履歴は [arXiv:2010.12929](https://arxiv.org/abs/2010.12929)。

## 3. 使用できる定理・一様性・剰余

**固定 \(A\) の確実な適用。** 上記 Theorem 1.2 は \(J=\lceil A-1\rceil\)、\(f\in\mathcal F(r,\sigma_0)\)、素数上の差 \(g(p)=f(p)-\varrho\) に (1.2) を仮定し、剰余
\[
 O\!\left(\frac{X(\log_3X)^\beta}
                 {(\log X)^{A+1-r}}\right)            \tag{SD5}
\]
を与える。\(\mu\) では \(\varrho=-1,r=1,1/2<\sigma_0<1\) を選ぶ。差 \(g(p)=0\)、高素数冪係数 \(f(p^\nu)=0\ (\nu\ge2)\)、\(\sum_p p^{-2\sigma_0}<\infty\)、および \(\sum_{v<p\le w}1/p\le\log(\log w/\log v)+O(1)\) だから (1.11) も満たす。任意の固定 \(A>0\) が許されるので
\[
  \forall K>0\quad M(X)=O_K\!\left(X(\log X)^{-K}\right). \tag{SD6}
\]
ただし (SD5) の \(\beta\)・定数はパラメータに依存する。\(A=A(X)\) として定数依存を無視してはいけない。

**複素 \(z\) の有界集合上の加法誤差。** Granville–Koukoulopoulos, *Beyond the LSD method for the partial sums of multiplicative functions*, Theorem 1、(1.2)–(1.5)、PDF pp2–3 は、\(|f|\le\tau_k\) と
\(\sum_{p\le x}f(p)\log p=\alpha x+O(x/\log^A x)\)
を仮定する。\(J\) は \(A\) 未満の最大整数で、誤差は
\[
 O\!\left(X(\log X)^{k-1-A}
                 (\log\log X)^{\mathbf1_{A=J+1}}\right). \tag{SD7}
\]
定数は \(k,A\) と素数平均の定数だけに依存する。[刊行版著者 PDF](https://dms.umontreal.ca/~koukoulo/documents/publications/LSD.pdf)、[DOI](https://doi.org/10.1007/s11139-018-0119-3)

ここへの適用は直接確認できる。\(|z|\le R\) で固定 \(k\ge\max(1,R)\) とすれば、平方自由数上 \(|f_z(n)|\le k^{\omega(n)}=\tau_k(n)\)、他では \(f_z=0\)。素数平均は \(z\vartheta(x)\) で、既知の無条件 PNT の任意固定対数冪誤差を使えば、その定数も \(|z|\le R\) に一様。従って (SD7) は \(z=-1\) を含む一様な**絶対誤差**であり、\(\lambda_0(z)\) による割り算をした相対誤差の一様性ではない。

**PNT 型の subpower も固定冪節約とは異なる。** Chang–Martin, arXiv:1908.00035v2, Appendix A, Definitions A.4/A.6, Theorem A.13 と証明（印刷 pp16–17,22–23）は零点自由領域型の解析接続・成長条件と非負 majorant を使う一様 SD 定理である。[指定版 PDF](https://arxiv.org/pdf/1908.00035v2)

本族では固定 \(0<c_0<2/11,\delta_0=1\) を選べば、領域 \(\sigma\ge1-c_0/(1+\log^+|t|)\) で \(G(s,z)\) は有界。majorant \(f_R=\mu^2R^\omega\) の積にも同じ評価があるため type \(T(z,R;c_0,1,M_R)\) が成立する。同定理の証明の \(\Phi'(x)\) からの誤差表示を、固定パラメータを定数に吸収して用いると
\[
 \left|S_z(X)-X L^{z-1}\sum_{j=0}^N\lambda_j(z)L^{-j}\right|
 \ll_R X L^{\Re z-1}\Gamma(N+R+2)(C_R/L)^{N+1}
          +X L^{R/2}e^{-c_R\sqrt L},\quad L=\log X,    \tag{SD8}
\]
\(R\ge1\)、十分大きい \(X\)、全整数 \(N\ge0\)。ここでは Lemma A.11（印刷 p19）の \(\Phi'(X)\) の評価と、Theorem A.13 の証明中（p23）の \(S_z(X)-\Phi'(X)\) の表示を用い、定理本文の \(R_N\) の PDF テキスト抽出をそのまま転記していない。\(z=-1,\ N=\lfloor\varepsilon_R L\rfloor\) と十分小さい固定 \(\varepsilon_R>0\) を取り Stirling 評価を使えば、既知の規模 \(M(X)\ll X e^{-c\sqrt{\log X}}\) を回収できる。この補足も局所係数だけの結論ではない。

\(e^{-c\sqrt{\log X}}=X^{-c/\sqrt{\log X}}\) の指数は 0 に近づく。従って (SD6) やこの補足を \(O(X^{1-\delta})\)（固定 \(\delta>0\)）へ強化してはいけない。

重要な provenance: de la Bretèche–Tenenbaum p3 末尾は、証明が \(\tau_\varrho\) の既存 SD 展開に強く依存すると説明する。\(\tau_{-1}=\mu\) なので、既知定理を使うことは有効でも「全係数消失から独立な新 PNT/RH 機構を得た」とは言えない。これは RH 仮定の循環とは別の、既知入力の再使用である。

## 4. 端点近傍で相対主項が不安定になる理由

直接の局所正則性から
\[
 \lambda_0(-1+\varepsilon)
 =\frac{G(1,-1+\varepsilon)}{\Gamma(-1+\varepsilon)}
 =-\varepsilon+O(\varepsilon^2).
\]
従って局所先頭項だけは
\[
 X(\log X)^{-2}e^{\varepsilon\log\log X}
                  [-\varepsilon+O(\varepsilon^2)].   \tag{SD9}
\]
\(\varepsilon=\varepsilon(X)\to0\) で主項が絶対誤差以下にもなり得る。これは局所係数の Taylor 計算であり、この式だけを有限和 \(S_z(X)\) の微分公式・一様な相対漸近式とはしない。

また (SD4) の全係数消失は、有限 \(X\) で整数格子の「bulk」が正確に打ち消されて boundary だけになる恒等分解を与えない。剰余の支持・次元・幾何的局在は何も証明していない。

## 5. Erdős–Kac / Sathe–Selberg と \(\pi\) 周波数

標準化 \((\omega-\log\log X)/\sqrt{\log\log X}\) の CLT は固定 Fourier 周波数 \(u\) を扱う。元のパリティ周波数 \(\pi\) は \(u_X=\pi\sqrt{\log\log X}\to\infty\) に対応するため、弱収束を代入するだけでは制御されない。局所個数 \(N_k(X)\) の相対近似を得ても、\(\sum_k(-1)^kN_k(X)\) の誤差は別途必要であり、中心領域の大きい正項の近似から強い相殺は自動ではない。

ただし「全ての強化分布定理が \(\pi\) を除外する」は誤り。Kowalski–Nikeghbali, *Mod-Poisson convergence in probability and number theory*, 著者 PDF §4, (4.1)–(4.2), pp7–8 は all-integer \(\omega(n)-1\) について一様 mod-Poisson 収束を述べ、\(u=\pi\) で \(\sum_{n\le X}(-1)^{\omega(n)}=o(X/\log^2X)\) を明記する。これは平方自由版の \(M(X)\) ではなく、しかも固定冪節約ではない。[著者 PDF](https://people.math.ethz.ch/~kowalski/mod-poisson.pdf)、[arXiv 版履歴](https://arxiv.org/abs/0905.0318)

今回 Sathe–Selberg の全ての \(k\)-一様範囲を再監査したとは主張しない。採用に必要なのは、対象が平方自由版であること、および交代和に許される絶対誤差を明記した評価である。

## 6. 大域的欠落と採否

\(1/\zeta(s)=(s-1)/Z(s)\) は \(s=1\) で正則な単純零点を持つ。一方、\(\zeta\) の零点 \(\rho\) が重複度 \(m\) なら \(1/\zeta\) はそこで位数 \(m\) の極を持つ。\(G(s,-1)=1\) はこれを消さない。Perron 輪郭を大域的に左へ移すには、これらの極と縦方向の成長の制御が残る。

例えば \(M(X)=O(X^{1-\delta})\) なら部分積分
\[
 \frac1{\zeta(s)}=s\int_1^\infty M(x)x^{-s-1}\,dx
\]
が \(\Re s>1-\delta\) で正則になり、同半平面は零点自由となる。固定 \(0<\delta<1/2\) の節約を即 RH 同値とは呼ばない。全 \(\epsilon>0\) に対する \(M(X)=O_\epsilon(X^{1/2+\epsilon})\) は古典的 RH 同値条件である。逆向きに必要な Littlewood 型入力の一次 locator は、先行 dyadic 監査でも確認した [Báez-Duarte, arXiv:math/0202141v2, §2.1](https://arxiv.org/html/math/0202141v2#S2.SS1)。

限定的 synthetic check もできる。固定 \(1/2<\beta<1\) と \(c_\beta=\zeta(2-\beta)/\zeta(2)\) に対し
\[
 D_\beta(s)=\zeta(s+1-\beta)-c_\beta\zeta(s+1),\qquad D_\beta(1)=0
\]
は \(s=1\) で正則だが、係数 \(a_n=n^{\beta-1}-c_\beta/n\) は
\[
 \sum_{n\le X}a_n=X^\beta/\beta-c_\beta\log X+O_\beta(1).
\]
これは積分比較で直接確認でき、\(s=\beta\) の極が残る。「局所正則零点だけなら剰余も平方根以下」という一般推論への反例である。Euler 因子・乗法性・実際の \(\zeta\) 算術を保存しておらず、RH への反例とはしない。

**Keep:** 正しい平方自由 Euler 積、全局所係数消失、固定対数冪評価、端点近傍の絶対／相対誤差の区別。**Kill:** これらだけを根拠とする低次元 remainder・固定冪節約・RH 証明。追加すべき独立入力は \(s=1\) の局所 Taylor 情報ではなく、Mertens 相殺または同等の大域的解析評価である。RH は OPEN。
