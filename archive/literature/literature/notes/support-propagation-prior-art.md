**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/support-propagation-prior-art.md` · Original SHA-256: `e3f4029f9b34132035666028288eebb4a509ab837c98380e542158fed0b2a756`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Support 拡大・Schur 補元・canonical flow の先行研究監査

調査日: 2026-09-29 (JST)。root の support propagation 方針への限定調査。対象は下記一次論文の該当 statement と条件であり、網羅調査・全証明の独立検証ではない。物理資料は使わない。RH、新規な拡大定理、counterterm の一意性を証明したとは扱わない。先行する固定窓の比較は [別ノート](window-four-fifths-comparison.md) に保存済み。

## 1. Schur 補元は正しい検査式だが、旧窓の正値性だけでは閉じない

有界 Hermitian block \(M=\begin{pmatrix}A&B\\B^*&D\end{pmatrix}\)、\(A\ge\alpha I>0\) なら、平方完成で

\[
 q_M(x,y)=\langle A(x+A^{-1}By),x+A^{-1}By\rangle
 +\langle (D-B^*A^{-1}B)y,y\rangle . \tag{S}
\]

従って \(M\ge0\iff D-B^*A^{-1}B\ge0\)。これは本ノートで直接確認できる代数恒等式であり、新しい RH 入力ではない。新 shell の \(D\) と cross block \(B\) を実際の Weil form から固定した後に、右辺の残余を評価しなければならない。\(A>0\) と \(D>0\) だけでも不足する。\(A\ge0\) に緩めた場合、単に \(A^{-1}\) を擬似逆行列と書き換えず、range 条件・還元解の有界性を別に処理する必要がある。

**先行資料:** W. N. Anderson, Jr. / G. E. Trapp, *Shorted Operators. II*, SIAM J. Appl. Math. 28 (1975), 60–71, [DOI 10.1137/0128007](https://epubs.siam.org/doi/10.1137/0128007)。出版社 abstract の定義は、既に **positive な \(M\)** と閉部分空間 \(\mathcal S\) に対する \(0\le X\le M, \operatorname{Ran}X\subset\mathcal S\) の最大化である。正の ambient operator を仮定して shorted operator を作り、その存在から ambient positivity を導く使用は循環する。今回全文の定理番号は未照合のため捏造しない。査読公刊 **YES**、全文独立検証 **NO**。

Weil の元の閉形式は一般に非有界である。\(L^2\) の窓・shell 分割をそのまま作用素 block とするには、form domain が分割で保たれるか、cross form が制御されるかを証明する。smooth な有限族での (S) と、全閉形式上の (S) は区別する。

## 2. Krein accelerant: 逆作用素が全区間で存在することが入力

D. Alpay, I. Gohberg, M. A. Kaashoek, L. Lerer, A. L. Sakhnovich, *Krein systems and canonical systems on a finite interval: accelerants with a jump discontinuity at the origin and continuous potentials*, [arXiv:0912.4444v1](https://arxiv.org/pdf/0912.4444v1), IEOT 68 (2010), 115–150, [出版社・DOI 10.1007/s00020-010-1803-x](https://link.springer.com/article/10.1007/s00020-010-1803-x)。査読公刊 **YES**、全証明独立検証 **NO**。

**Theorem 1.1, equations (1.1)–(1.2):** Hermitian 行列核 \(k(-x)=k(x)^*\)、\([-T,T]\) 上連続（原点の jump を許す）を用い、

\[
 (T_\tau f)(x)=f(x)-\int_0^\tau k(x-s)f(s)\,ds,
 \quad 0<\tau\le T,
\]

を **各 \(\tau\)** で可逆と仮定する。resolvent 核は

\[
 \gamma_\tau(x,y)-\int_0^\tau k(x-s)\gamma_\tau(s,y)\,ds=k(x-y).
\]

これから Krein system が得られる。**本文 p.6、(2.10) 直前**は、この全区間可逆性と \(T_T\) の strict positivity の同値を明記する。

**Theorem 1.2, (1.10)–(1.13):** 連続な Dirac-type canonical potential \(v\) を先に与える逆問題では、上の全区間可逆性を持つ accelerant が一意に存在し、\(v(\tau)=-i\gamma_\tau(\tau,0)\)。しかし、任意の連続 \(v\) から作った \(k\) が算術的に指定された Weil 核と一致するとは述べない。

従って resolvent/Volterra flow を導入すること自体は先行手法である。今回の欠落は、実際の算術核を accelerant として扱えること、または構成後の核の厳密な同定である。単なる小区間の可逆性から全区間可逆性への延長則は、この定理にはない。

## 3. Suzuki の Fredholm canonical system と RH 同値条件

**2026 年の screw-form 論文と区別する。** ここで直接該当するのは Masatoshi Suzuki, *Hamiltonians arising from L-functions in the Selberg class*, [arXiv:1606.05726v3](https://arxiv.org/html/1606.05726v3)（v3: 2020-10-01）、公刊書誌 JFA 281 (2021), 109116, [DOI 10.1016/j.jfa.2021.109116](https://doi.org/10.1016/j.jfa.2021.109116)。公刊論文であるが今回 publisher 本文取得は失敗し、定理番号は明示した arXiv v3 に固定する。全証明独立検証 **NO**。

以下は \(\zeta\) に限定（一般定理は \(\mathcal S_{\mathbb R}\)、次数 \(d_L\)）。\(E(z)=\xi(1/2+\omega-iz)^\nu, \omega>0, \nu\in\mathbb Z_{>0},\ \nu\omega>1\)。\(\Theta=E^\sharp/E\) の逆 Fourier 核 \(K\) は causal で、

\[
 K[t]f(x)=\mathbf1_{x<t}\int_{-\infty}^{t}K(x+y)f(y)\,dy,
 \qquad
 \gamma(t)=\left(\frac{\det(I+K[t])}{\det(I-K[t])}\right)^2,
 \quad H(t)=\operatorname{diag}(\gamma^{-1},\gamma).
\]

**Theorems 2.1–2.2:** ある \(\tau>0\) までは \(\pm1\notin\operatorname{spec}K[t]\)、上の Hamiltonian と初期値 \(A(0,z)-iB(0,z)=E(z)\) を持つ canonical system を無条件構成する。**§3 (K1)–(K5)** は Fourier 表示、核の成長・因果性・局所微分正則性に加え、このスペクトル条件を明記する。**Proposition 5.1** の全 \(t\ge0\) に対する \(\|K[t]\|<1\) は、§5.1 冒頭の \(E\in\overline{\mathbb{HB}}\) を引き継ぐ。これを無条件の全域推定として引用しない。

**Theorem 2.4** の \(\zeta\) への特殊化は正確に、RH と次の族の存在との同値である。

\[
 \omega_n\downarrow0,\quad \nu_n\omega_n>1,\quad
 \det(I\pm K^{\omega_n,\nu_n}[t])\ne0\ (\forall t\ge0),
\]
\[
 \lim_{t\to\infty}J^{\omega_n,\nu_n}(t;z,z)=0
 \quad(\forall z\in\mathbb C_+),\qquad
 J(t;z,w)=\frac{\overline{A(t,z)}B(t,w)-A(t,w)\overline{B(t,z)}}{\pi(w-\bar z)}.
\]

**監査判断:** determinant の非消滅と endpoint 条件の両方を落とせない。ratio の平方は定義できる範囲で正になるが、その事実は大域構成を保証しない。またこの \(K[t]\) は \(\Theta\) の Hankel kernel であり、Weil form の窓作用素をそのまま block 表記したものではない。両者を同一視するには別の恒等式が必要である。

参考として、この論文の canonical equation の符号では \(r=B/A\) が定義できる chart 上で

\[
 r'=-z\gamma^{-1}-z\gamma r^2
\]

と直接計算できる。Riccati への書換えは上の存在条件を除かない。\(A=0\) による chart の極と、\(I\pm K[t]\) の非可逆化を混同しない。

## 4. Suzuki 2026 の非局所作用素は shift と極限条件を伴う

Masatoshi Suzuki, *Weil’s quadratic form via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), 2026-09-23。査読公刊確認 **NO**、全証明独立検証 **NO**。Theorem 1.1 は局所 Weil form の Friedrichs realization、Theorem 1.3 は下端 \(\lambda_a\) の連続性であり、拡大による非負性保存定理ではない。

**§6 と §8.3:** \(\lambda<\lambda_a\) を取り \(T_a=A_a-\lambda I>0\) で Hilbert norm を構成する。従って補助微分作用素の自己共役拡張を得ても、shift 前の \(A_a\ge0\) は従わない。

**Corollary 1.6, (1.12):** 十分大きな各 \(a\) について \(\lambda(a)<\lambda_a,\theta(a)\) と上半平面で解析的な \(\phi(a,z)\) を選び、

\[
 e^{\phi(a,z)}W(a,\theta;z)\longrightarrow
 \frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)}
\]

が上半平面の各 compact 上で一様に成立すれば RH。**この極限は未証明条件**。直後の説明と §7 は \(A_a>0\) 下の heuristic を区別し、全ての十分大きな \(a\) で \(\lambda=0\) を許すこと自体が Weil criterion により RH 同値であると述べる。kernel の連続性だけで無条件の canonical propagation を得たとは引用できない。

## 5. Groskin の正の archimedean flow は support flow ではない

Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, [arXiv:2607.02828v3](https://arxiv.org/html/2607.02828v3)。査読確認 **NO**、全証明独立検証 **NO**。一次 TeX と [取得・計算状況](groskin-certificate-audit.md) を参照。

**Theorem 2.5:** 固定 \(c>1,N\ge0\) と実偶 vector の exact Guinand–Weil dictionary。RH を仮定せず、零点側の \(z\) は複素数を許す。これはすべての Weil test functions の正値性定理ではない。

ここで \(h_+(T)=\Re\psi(1/4+iT/2)-\log\pi\)。

**Theorem 3.2:** \(L=\log c,\rho=2\pi/L,I_N=\{-N,\ldots,N\}\)、\(T_2>T_1>\max(\rho N,7)\) で

\[
 Q_{\rm arch,T_2}-Q_{\rm arch,T_1}
 =\frac1{\pi^2}\int_{T_1}^{T_2}\frac{h_+(T)\sin^2(LT/2)}\rho
 (p_Tp_T^{\mathsf t}+q_Tq_T^{\mathsf t})\,dT,
 \quad p_T(n)=\frac1{T/\rho-n},\quad q_T(n)=\frac1{T/\rho+n}.
\]

固定 \((c,N)\) の full complex finite frequency space 上で正定値増分、自然順序で strict total positivity。**Corollary 3.3** の tail は \(0\prec Q_\infty-Q_T\preceq B_T I\)。いずれも周波数 cutoff \(T\) を動かす条件であり、\(c\) を動かす主張ではない。

**監査判断:** \(c\) を拡大すると \(L,\rho\)、test-function 辞書、新 prime terms が変わる。同じ \(c\) でも \(N\to\infty\) を固定 \(T\) で取れば \(T>\rho N\) が破れる。この定理の Cauchy–Stieltjes 表現だけから、新 shell の cross term と整合した一意 counterterm は得られない。定理の範囲では、必要なのは各 support 間の正確な埋込み、元の全 source との一致、Schur residual の下界を別に証明することである。

## 6. 延長の「存在」と算術的に指定された延長を分ける

M. G. Krein / H. Langer, *Continuation of Hermitian Positive Definite Functions and Related Questions*, IEOT 78 (2014), 1–69, [出版社・DOI 10.1007/s00020-013-2091-z](https://link.springer.com/article/10.1007/s00020-013-2091-z)。今回は出版社 abstract と書誌のみ確認。canonical systems/strings と正定値関数の延長問題を結ぶ先行文献として挙げる。個別定理の条件は未照合であり、Weil 核への適用済みとはしない。査読公刊 **YES**、独立検証 **NO**。

存在定理が「ある正の延長」を与えても、それが次の素数冪の source を持つ所定の延長であるとは限らない。この論理上の差は、追加項を調整して Schur residual を正にした場合にも残る。正値性を得た補助形式から元の Weil form に戻す恒等式・不等式が必要である。

## 7. この調査から採用できるもの・未解決事項

| 手法 | 既知の有効部分 | 今回別に要るもの |
|---|---|---|
| Schur / shorting | block 消去・最小化 | 算術的 \(D-B^*A^{-1}B\ge0\)、domain 条件 |
| Krein resolvent | accelerant から canonical system | 実核の全区間可逆性、または逆構成との同定 |
| Suzuki Fredholm family | 局所構成、正確な RH 同値式 | 大域 determinant 非消滅と endpoint 極限 |
| Suzuki 2026 | shift 後の Hilbert space・自己共役拡張 | shift を外す正値性または未証明の複素局所一様極限 |
| Groskin tail order | 固定 \((c,N)\) で正の周波数増分 | support 間の整合と新 arithmetic cross term の制御 |

共通の \(C_c^\infty\) Weil form を exact restrictions として扱い、support が無限大へ増す各窓全体で PSD を証明できれば、各 compact test はいずれかの窓に入り RH が従う。この場合は「有限個の計算の極限交換」よりも、**全段階の拡大則を無条件証明すること**が中心義務になる。全窓 PSD は既知の Weil criterion そのものである。今回確認した文献には、この義務を旧窓 PSD のみから自動的に解消する定理は見つからなかった。この結論は記載した検索・読取範囲に限定する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`literature/notes/groskin-certificate-audit.md`](groskin-certificate-audit.md)
- [`literature/notes/window-four-fifths-comparison.md`](window-four-fifths-comparison.md)
