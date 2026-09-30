**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma/notes/fourier_bridge.md` · Original SHA-256: `44c89ca7a8f8e1697b73525cd84de55e2f0cbd23390ded4c968df84b6a5e9427`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Arithmetic Comma：torus coefficient と Fourier–Mellin の exact bridge

2026-09-30。有限素数集合から actual Möbius 和への正規化を直接計算する。既存ファイルは変更しない。**Level 1: exact bridge** と **未証明の cancellation estimate** を分ける。新規性・RH の進展は主張せず、RH は OPEN。

## FB1. Signed subset measure と sharp cutoff

異なる素数の有限集合 \(P=\{p_1,\ldots,p_k\}\) を固定する。
\[
 \mathcal N_P=\{n_\kappa=\prod_{j=1}^k p_j^{\kappa_j}:
                         \kappa\in\{0,1\}^k\},\quad
 \mu(n_\kappa)=(-1)^{|\kappa|},\quad Q_P=\prod_{p\in P}p.
\]
empty subset は \(n=1\)、\(\log n=0\)、符号 \(+1\)。signed measure と右連続な cutoff を
\[
 \nu_P=\mathop{*}_{p\in P}(\delta_0-\delta_{\log p})
      =\sum_{n\in\mathcal N_P}\mu(n)\delta_{\log n},\qquad
 A_P(L)=\nu_P(( -\infty,L])
       =\sum_{\substack{n\in\mathcal N_P\\n\le e^L}}\mu(n)
 \tag{1}
\]
と定める。総変動は \(\|\nu_P\|_{TV}=2^k\)。\(P\ne\varnothing\) なら総質量は0なので \(e^L\ge Q_P\) では \(A_P(L)=0\)。この有限の全 subset 相殺を、素数集合が変化する \(M(X)\) の評価と混同しない。

## FB2. Normalized Haar coefficient extraction

\(\mathbb T^k\) 上の Haar measure を
\(dm=(2\pi)^{-k}d\theta_1\cdots d\theta_k\)、\(z_j=e^{i\theta_j}\) と固定する。
\[
 B_P(z)=\prod_{j=1}^k(1-z_j)
       =\sum_{n\in\mathcal N_P}\mu(n)z^{\kappa(n)},\qquad
 C_{P,X}(z)=\sum_{\substack{n\in\mathcal N_P\\n\le X}}z^{\kappa(n)}.
\]
monomials の直交性 \(\int z^\alpha\overline{z^\beta}dm=\mathbf1_{\alpha=\beta}\) から
\[
 \boxed{A_P(\log X)=\int_{\mathbb T^k}B_P(z)\overline{C_{P,X}(z)}dm(z).}
 \tag{2}
\]
追加の \(2^k\) は掛からない。\(2^{-k}A_P\) は各 subset に確率 \(2^{-k}\) を与えた別の signed average である。

一般の複素係数 \(w_n\) に対して
\[
 C_w(z)=\sum_{n\in\mathcal N_P}\overline{w_n}z^{\kappa(n)}
 \quad\Longrightarrow\quad
 \int B_P\overline{C_w}\,dm=\sum_{n\in\mathcal N_P}\mu(n)w_n.
 \tag{3}
\]
複素 cutoff のときもこの conjugation を保持する。

一方、\(N_P(X)=\#\{n\in\mathcal N_P:n\le X\}\) とすれば
\[
 \|B_P\|_2^2=2^k,\quad\|C_{P,X}\|_2^2=N_P(X),\quad
 |A_P(\log X)|\le2^{k/2}\sqrt{N_P(X)}.
 \tag{4}
\]
これは恒等式に付随する Cauchy–Schwarz bound であり、一般に自明な \(|A_P|\le N_P\) より弱い。正の Haar measure があることだけでは Möbius cancellation を得ない。

## FB3. Prime-log flow と有限時間の費用

\(z(t)=(p_1^{-it},\ldots,p_k^{-it})\) と置く。\(\sum_j a_j\log p_j=0\)、\(a_j\in\mathbb Z\) は素因数分解の一意性から全 \(a_j=0\) を強制する。従って非定数 character の時間平均は
\[
 \frac1T\int_0^T e^{-it\omega}dt
     =\frac{1-e^{-iT\omega}}{iT\omega}\longrightarrow0
       \quad(\omega\ne0).
\]
有限 trig polynomial の各項に適用して、深い ergodic theorem を使わず
\[
 A_P(\log X)=\lim_{T\to\infty}\frac1T\int_0^T
                      B_P(z(t))\overline{C_{P,X}(z(t))}dt.
 \tag{5}
\]
ただし \(B_P\) **単独**の平均は1であって \(A_P\) ではない。cutoff polynomial が必要である。

有限時間の exact expansion は、\(a\in\mathcal N_P\)、\(b\in\mathcal N_P\cap[1,X]\) の \(a=b\) を diagonal とし、残りを \(\log(a/b)\) の周波数とする。従って error は
\[
 |E_T|\le\frac2T
   \sum_{\substack{a\in\mathcal N_P,\ b\in\mathcal N_P\cap[1,X]\\a\ne b}}
                    \frac1{|\log(a/b)|}.
 \tag{6}
\]
異なる正整数 \(a,b\le Q_P\) には \(|\log(a/b)|\ge1/Q_P\)。よって例えば
\[
 |E_T|\le \frac{2Q_P(2^k-1)N_P(X)}{T}.
\]
この粗い bound は \(P,X\) とともに悪化する。fixed finite torus の equidistribution から、\(P\) が増大する cutoff 問題の一様な rate は出ない。ここでの周波数差は実数 \(\log(a/b)\) そのものであり、単位を固定しない「\(2\pi\) に近い」という議論で置換しない。

## FB4. Compact smooth cutoff の Fourier inversion

\[
 \widehat\phi(t)=\int_{\mathbb R}\phi(v)e^{-itv}dv,\qquad
 \phi(v)=\frac1{2\pi}\int_{\mathbb R}\widehat\phi(t)e^{itv}dt,
 \qquad \phi\in C_c^\infty(\mathbb R).
\]
\(S_{P,\phi}(L)=(\nu_P*\phi)(L)\) とすると
\[
 \boxed{S_{P,\phi}(L)=\sum_{n\in\mathcal N_P}\mu(n)\phi(L-\log n)
 =\frac1{2\pi}\int_{\mathbb R}\widehat\phi(t)e^{itL}
                        \prod_{p\in P}(1-p^{-it})dt.}
 \tag{7}
\]
有限和と absolutely convergent Fourier integral の交換なので無条件。\(w_n=\phi(L-\log n)\) を (3) に代入すれば同じ量を torus coefficient としても表せる。

無減衰の全素数 Euler product を実軸 \(it\) で収束すると仮定してはいけない。(7) の有限積には問題がなくても、それを \(1/\zeta(it)\) に置換する根拠にはならない。

## FB5. 全素数への actual arithmetic extension と no-tail 条件

\(P_y=\{p:p\le y\}\) とする。\(y\ge X\) なら
\[
 \boxed{A_{P_y}(\log X)=M(X):=\sum_{n\le X}\mu(n).}
 \tag{8}
\]
理由は \(n\le X\) の全素因数が \(X\) 以下であり、non-squarefree terms の \(\mu\) は0だから。\(\max P\ge X\) だけでは足りず、必要な全素数を含む条件である。

\(\operatorname{supp}\phi\subset[\alpha,\beta]\) なら \(\phi(L-\log n)\ne0\) は \(n\le e^{L-\alpha}\) を含意する。従って \(y\ge e^{L-\alpha}\) で
\[
 S_{P_y,\phi}(L)=\sum_{n\ge1}\mu(n)\phi(L-\log n)
 \tag{9}
\]
は exact。ここには tail estimate 自体が不要である。右辺も各 \(L\) では有限和。

全実線上の transform へ移すときは \(\sigma>1\) で減衰させる。
\[
 \nu_\sigma=\sum_{n\ge1}\mu(n)n^{-\sigma}\delta_{\log n},\qquad
 \|\nu_\sigma\|_{TV}=\sum_{n\ge1}\frac{\mu(n)^2}{n^\sigma}
                      =\frac{\zeta(\sigma)}{\zeta(2\sigma)}<\infty.
\]
absolutely convergent Euler product から、全実数 \(t\) に対して
\[
 \widehat\nu_\sigma(t)
  =\sum_{n\ge1}\mu(n)n^{-\sigma-it}
  =\prod_p(1-p^{-\sigma-it})=\frac1{\zeta(\sigma+it)}.
 \tag{10}
\]
\(g_\sigma(v)=e^{-\sigma v}\phi(v)\) とすれば
\[
 \boxed{\sum_{n\ge1}\mu(n)\phi(L-\log n)
 =\frac{e^{\sigma L}}{2\pi}\int_{\mathbb R}
    \frac{\widehat g_\sigma(t)e^{itL}}{\zeta(\sigma+it)}dt.}
 \tag{11}
\]
\(\phi(L-\log n)=e^{\sigma L}n^{-\sigma}g_\sigma(L-\log n)\) が係数の確認となる。\(\widehat g_\sigma\in L^1\) と \(\|\nu_\sigma\|_{TV}<\infty\) が Fubini を正当化する。

有限積を (10) に収束させる際も、絶対収束半平面では uniform in \(t\)。例えば差の係数は全て \(n>y\) にあるので \(y\ge1\) に対しその絶対値は \(\sum_{n>y}n^{-\sigma}\) 以下。これは (8)–(9) の exact support argument とは別の、transform 側の収束である。

## FB6. Step smoothing、Perron、unsmoothing の費用

固定 \(\eta\in C_c^\infty([-1,1])\) に \(\eta\ge0\)、\(\int\eta=1\) を課す。\(0<h\le1\)、\(\eta_h(v)=h^{-1}\eta(v/h)\)、\(H_h(v)=\int_{-\infty}^v\eta_h(w)dw\) として
\[
 M_h(X)=\sum_{n\ge1}\mu(n)H_h(\log X-\log n)
        =\int\eta_h(v)M(Xe^{-v})dv.
 \tag{12}
\]
\(H_h\) 自体は compact support ではないが、\(v\le-h\) で0、\(v\ge h\) で1。従って (12) に寄与する \(n\) は \(n\le Xe^h\)。\(y\ge Xe^h\) なら finite \(P_y\) と full arithmetic の平滑和は exact に一致する。Gaussian mollifier のように compact support がない場合には、この no-tail 結論を使わない。

sharp cutoff との差は \(Xe^{-h}\le n\le Xe^h\) でしか生じず、一項の差は高々1なので
\[
 \boxed{|M_h(X)-M(X)|
       \le\#(\mathbb N\cap[Xe^{-h},Xe^h])
       \le 2X\sinh h+1=O(hX+1).}
 \tag{13}
\]
同じ評価は finite \(P\) にも成立する。\(\eta\) が符号付きなら、その \(L^1\) norm を考慮せずこの係数1を使ってはいけない。

\(s=\sigma+it\)、\(\sigma>1\) として
\[
 \mathcal E_h(s)=\int\eta_h(v)e^{-sv}dv,\qquad
 \int H_h(v)e^{-sv}dv=\frac{\mathcal E_h(s)}s.
\]
後式は integration by parts。従って絶対収束する smoothed Perron formula は
\[
 \boxed{M_h(X)=\frac1{2\pi}\int_{\mathbb R}
       \frac{X^{\sigma+it}\mathcal E_h(\sigma+it)}
            {(\sigma+it)\zeta(\sigma+it)}dt.}
 \tag{14}
\]
固定 \(h>0\) では \(\mathcal E_h(\sigma+it)\) が任意冪で減衰する。\(h\to0\) でその定数が一様とは主張しない。

sharp Perron の endpoint も確認する。\(f_\sigma(v)=e^{-\sigma v}\mathbf1_{v\ge0}\) とすれば \(f_\sigma\in L^1\cap BV\)、\(\widehat f_\sigma(t)=(\sigma+it)^{-1}\)。\(\nu_\sigma*f_\sigma=e^{-\sigma L}M(e^L)\) も \(L^1\cap BV\) なので、symmetric Fourier inversion の左右平均公式より
\[
 \lim_{T\to\infty}\frac1{2\pi i}
     \int_{\sigma-iT}^{\sigma+iT}\frac{X^s}{s\zeta(s)}ds
 =M^*(X):=\sum_{n<X}\mu(n)+\tfrac12\mathbf1_{X\in\mathbb N}\mu(X).
 \tag{15}
\]
noninteger \(X\) では \(M^*(X)=M(X)\)。integer cutoff の右連続値を得るには \(\mu(X)/2\) を加える。finite \(P\) も同じ convention。対称な mollifier で \(h\downarrow0\) とした場合も jump では左右平均へ収束する。これは (13) の \(+1\) と整合する。

## FB7. 二素数・三素数の exact toy

\(P=\{2,3\}\) なら
\[
 \nu_P=\delta_0-\delta_{\log2}-\delta_{\log3}+\delta_{\log6},\quad
 B_P=1-z_2-z_3+z_2z_3.
\]
\(X=e^L\) における \(A_P\) は

| \(X\) の区間 | \((0,1)\) | \([1,2)\) | \([2,3)\) | \([3,6)\) | \([6,\infty)\) |
|---|---:|---:|---:|---:|---:|
| \(A_{\{2,3\}}(\log X)\) | 0 | 1 | 0 | -1 | 0 |

\(P=\{2,3,5\}\) なら八項は
\[
 \nu_P=\delta_0-\delta_{\log2}-\delta_{\log3}-\delta_{\log5}
       +\delta_{\log6}+\delta_{\log10}+\delta_{\log15}-\delta_{\log30}.
\]

| \(X\) の区間 | \((0,1)\) | \([1,2)\) | \([2,3)\) | \([3,5)\) | \([5,6)\) | \([6,10)\) | \([10,15)\) | \([15,30)\) | \([30,\infty)\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(A_{\{2,3,5\}}(\log X)\) | 0 | 1 | 0 | -1 | -2 | -1 | 0 | 1 | 0 |

例えば \(X=7\) ではこの finite 値は \(-1\) だが actual \(M(7)=-2\)。省いた素数7の項が原因であり、(8) の十分条件を満たしていない。完全な cutoff support を含むことと、有限 Euler product の全項相殺を区別する。

## FB8. Hardy/Bohr の範囲と RH を隠す移項

無減衰の \(\mu(n)\) は square summable でない。従って formal \(\prod_p(1-z_p)\) 自体を \(H^2(\mathbb T^\infty)\) の vector として採用できない。Bohr lift の \(H^2\) において、減衰係数 \(\mu(n)n^{-\sigma}\) は \(\sigma>1/2\) で square summable：
\[
 \sum_n\mu(n)^2n^{-2\sigma}=\frac{\zeta(2\sigma)}{\zeta(4\sigma)}<\infty.
\]
従って torus \(L^2\) vector の存在は無条件である。しかし、これだけで指定 character \(z_p=1\) や指定 orbit \(z_p=p^{-it}\) における pointwise value を得ない。boundary point evaluation は \(H^2\) norm では非連続で、例えば異なる \(N\) 個の monomials の和を \(\sqrt N\) で割ると norm1、identity character での値は \(\sqrt N\)。Haar-a.e. の結果を固定 arithmetic orbit の値へ昇格させない。

通常の \(H^2\) point-evaluation estimate を追加変数 \(w\) に適用すると
\[
 \left|\sum_n\mu(n)n^{-\sigma}n^{-w}\right|
 \le\left(\frac{\zeta(2\sigma)}{\zeta(4\sigma)}\right)^{1/2}
          \zeta(2\Re w)^{1/2},\qquad\Re w>1/2.
\]
これは追加の半平面 \(\Re w>1/2\) を要し、特に \(w=0\) や \(w=it\) の値を与えない。\(\sigma>1/2\) と合わせた保証領域は \(\Re(\sigma+w)>1\) 内にある。この一般的 \(H^2\) bound から reciprocal zeta の critical-strip pointwise control を取り出してはいけない。

なお、有限 cutoff polynomial との coefficient pairing まで失われるわけではない。\(B_\sigma\) を上記 \(L^2\) vector、\(C_{\sigma,X}=\sum_{n\le X,\,\mu(n)^2=1}n^\sigma z^{\kappa(n)}\) とすれば \(\int B_\sigma\overline{C_{\sigma,X}}dm=M(X)\) は exact。しかし Cauchy–Schwarz は \(|M(X)|\le\|B_\sigma\|_2(\sum_{n\le X}n^{2\sigma})^{1/2}=O_\sigma(X^{\sigma+1/2})\) しか与えず、\(\sigma>1/2\) では自明な \(O(X)\) を改善しない。exact coefficient bridge と改善された estimate は別である。

(14)–(15) の積分線を \(\Re s=1/2+\varepsilon\) まで動かすには、\(1/\zeta\) の poles、水平辺、無限遠、\(h\)-依存を処理する必要がある。非自明零点は \(1/\zeta\) の poles になる。\(s=1\) の \(\zeta\) の pole は逆数の zero であり、これと混同しない。strip 内の移動で全ての residue を消し、全 \(\varepsilon>0\) で zero-free と仮定するなら RH 同値の入力を持ち込んでいる。

また (13) を平方根規模にするには例えば \(h\lesssim X^{-1/2+\varepsilon}\) を要し、その縮む幅に対して (14) の estimate を一様化する追加仕事が残る。fixed \(P\) の equidistribution、fixed \(h\) の Fourier inversion、\(\sigma>1\) の absolute convergence のどれも、この一様 cancellation estimate を供給しない。

## FB9. 一次出典・独立確認・判定

- Hedenmalm–Lindqvist–Seip, [*A Hilbert space of Dirichlet series and systems of dilated functions in L²(0,1)*, math/9512211v1](https://arxiv.org/html/math/9512211v1), §2.2 (2-5) が prime coordinates の Bohr lift、同節の normalized Haar / Hardy model、§4.1 (4-1) が prime-log Kronecker flow の平均を扱う。author preprint の本文を照合した。原 Bohr 1913 論文全体を再監査したという意味ではない。
- Hardy–Riesz, *The General Theory of Dirichlet’s Series* (1915) の原本文取得は今回の web endpoint で完了しなかった。その Perron theorem を読了済みとして引用せず、(15) は本ノートの \(L^1\cap BV\) Fourier inversion による導出を使った。
- DESTROYER が (11) の減衰・Fourier 符号、非負 compact mollifier の下での (13)、sharp \(y\ge X\) / smooth \(y\ge Xe^h\) の no-tail 条件を独立に検算し PASS。signed mollifier と非compact smoothing の例外も確認された。

**Decision:** (2), (5), (7), (8)–(15) は actual arithmetic coefficients を保持した Level 1 の exact bridge として保存する。新しい一様 cancellation estimate は得ていない。有限トーラスの正測度、近接周波数、平滑化、解析接続を RH の代用品にしない。RH は OPEN。
