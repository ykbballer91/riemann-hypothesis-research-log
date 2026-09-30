**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/full_ground_capture/cyclicity.md` · Original SHA-256: `52507e842fee06329585b2ecc46c9b91ab9619b619fbd4c163a5b2237103935e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Priority 1 — k の even L² cyclicity

2026-09-30。**RH は OPEN。K IS CYCLIC IN EVEN L2: PROVED.**

これは FULL-GROUND CAPTURE の Priority 1 だけの補助定理である。有限 Fourier head、conditioning、増大する微分次数、full ground、parity 比較には進まない。既存の研究ファイル・state・proof graph は変更しない。以下の結論の新規性は主張しない。

## 1. 結論と規約

既存の [核の規約 BR1](../rate_history/notes/boundary_rate_analysis.md) を固定する：

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi(x)=\xi(1/2+ix),\qquad
\widehat f(x)=\int_{\mathbb R}f(t)e^{-ixt}\,dt,
\quad \widehat k=\Xi/4.
\]

ここで \(\Xi\) は Fourier 周波数を変数とする標準 Xi 関数であり、\(\xi(1/2+z)\) という別の座標を使わない。\(k\) は実偶 Schwartz 関数で、実際の theta 表示は

\[
\theta(y)=\sum_{r\in\mathbb Z}e^{-\pi r^2y},\quad
\Psi(t)=e^{t/2}\theta(e^{2t}),\quad
k(t)=\frac18(D_t^2-1/4)\Psi(t).
\]

Poisson 恒等式による偶性と theta 級数の super-exponential tail から、全 \(k^{(r)}\) が Schwartz に属する。従って通常の部分積分で

\[
\widehat {k^{(2j)}}(x)=(-1)^j x^{2j}\Xi(x)/4.
\tag{1}
\]

**補助定理 CY1（無条件）**

\[
\boxed{\overline{\operatorname{span}_{\mathbb C}
\{k,k'',k^{(4)},\ldots\}}^{\,L^2(\mathbb R)}
=L^2_{\rm even}(\mathbb R).}
\tag{2}
\]

実 Hilbert 空間についても同じ結論が成立する。ここで cyclic とは、\(D^2\) の全多項式 orbit の **L² ノルム閉包** が偶部分空間を張る、という意味に限定する。

必要な weighted reduction は

\[
\overline{\mathbb C[x^2]}^{\,L^2(\mu)}=L^2_{\rm even}(\mu),
\qquad d\mu(x)=|\Xi(x)|^2dx
\tag{3}
\]

である。\(\mathbb C[x^2]\) が全 \(L^2(\mu)\) に稠密という命題は偽である。例えば非零の奇関数 \(x\in L^2(\mu)\) は全偶多項式に直交する。全 \(L^2(\mu)\) に稠密なのは全多項式 \(\mathbb C[x]\) である。

## 2. 全 moment と、cyclicity に十分な上界

\(c=\pi/2\) とおく。Gamma の鉛直方向の Stirling 展開から、\(x\to+\infty\) で

\[
\left|\Gamma(1/4+ix/2)\right|^2
=2\pi(x/2)^{-1/2}e^{-\pi x/2}(1+O(x^{-1})).
\]

また \(|s(s-1)|^2=(x^2+1/4)^2\) であるから、

\[
|\Xi(x)|^2
=\sqrt{\pi/2}\,x^{7/2}e^{-cx}
|\zeta(1/2+ix)|^2(1+O(x^{-1})).
\tag{4}
\]

これは \(|\zeta|^2\) を定数とみなす点wise 同値漸近ではない。Gamma/pole-removal factor に関する乗法誤差であり、zeta の零点でも式は整合する。出典は [DLMF §5.11、特に (5.11.9)](https://dlmf.nist.gov/5.11#E9)。

必要な zeta 上界は極めて粗くてよい。\(\Re s>0,\ s\ne1\) の Euler summation 表示

\[
\zeta(s)=\frac{s}{s-1}-s\int_1^\infty\{y\}y^{-s-1}\,dy
\tag{5}
\]

は、まず \(\Re s>1\) で \(s\int_1^\infty\lfloor y\rfloor y^{-s-1}dy\) を分解し、残りの絶対収束積分で延長して得られる。\(\Re s=1/2\) で積分の絶対値は 2 以下なので、無条件に

\[
|\zeta(1/2+ix)|\le C(1+|x|).
\]

したがって全実数で

\[
|\Xi(x)|^2\le C(1+|x|)^{11/2}e^{-c|x|}.
\tag{6}
\]

特に、任意の \(0<b<c\) について

\[
\int_{\mathbb R}e^{b|x|}\,d\mu(x)<\infty.
\tag{7}
\]

全絶対 moment が有限である。\(m_r=\int x^r\,d\mu\) とすると \(m_{2n+1}=0\)、\(m_{2n}>0\) であり、固定定数 \(C_0,C_1\) により

\[
m_{2n}\le C_0+C_1\frac{\Gamma(2n+13/2)}{c^{\,2n+13/2}}.
\tag{8}
\]

Stirling によって右辺の \(2n\) 乗根は \((2n/(ce))(1+o(1))\)。従って十分大きな \(n\) で

\[
m_{2n}^{-1/(2n)}\ge \frac{c e}{4n},
\qquad
\boxed{\sum_{n\ge1}m_{2n}^{-1/(2n)}=\infty.}
\tag{9}
\]

定数 \(1/4\) は余裕を持たせたもので、最適化不要。これで Hamburger Carleman 条件は証明済みである。**Stirling と初等的 zeta 上界だけで足り、RH・零点位置・平均二乗の精密評価は使わない。**

## 3. moment の精密漸近（本体の証明とは独立の追加評価）

上界と同値漸近を区別するため、精密式の追加入力を明記する。古典的な無条件平均二乗公式を

\[
\int_0^T|\zeta(1/2+it)|^2dt
=T\log(T/(2\pi))+(2\gamma-1)T+E(T),
\quad E(T)=O_\delta(T^{1/3+\delta})
\tag{10}
\]

とする。十分小さい固定 \(\delta>0\) の評価は [Simonič–Starichkova, arXiv:2105.06821v3](https://arxiv.org/abs/2105.06821v3) の無条件結果であり、RH の仮定ではない。

\(v=2n+9/2\)、\(\psi=\Gamma'/\Gamma\) とすると

\[
\boxed{
m_{2n}=\frac{\sqrt{2\pi}\,\Gamma(v)}{(\pi/2)^v}
\left[\psi(v)+2\gamma-\log(\pi^2)+o(1)\right].}
\tag{11}
\]

従って、より簡単には

\[
m_{2n}\sim
\sqrt{2\pi}\,\Gamma(2n+9/2)(2/\pi)^{2n+9/2}\log n,
\qquad
m_{2n}^{-1/(2n)}\sim\frac{\pi e}{4n}.
\tag{12}
\]

導出の要点：\(w_v(t)=t^{v-1}e^{-ct}\)、\(Z_v=\Gamma(v)c^{-v}\) として (10) を部分積分する。主項の密度は \(\log(t/(2\pi))+2\gamma\)。Gamma 分布平均により

\[
Z_v^{-1}\int_0^\infty w_v(t)(\log(t/(2\pi))+2\gamma)dt
=\psi(v)-\log c-\log(2\pi)+2\gamma.
\]

\(\alpha=1/3+\delta<1/2\) を固定すれば、誤差は

\[
Z_v^{-1}\left|\int_0^\infty E(t)w'_v(t)dt\right|
\ll \left(\mathbb E T^{2\alpha}\right)^{1/2}
\left(\mathbb E\left((v-1)/T-c\right)^2\right)^{1/2}
\ll v^{\alpha-1/2}=o(1),
\]

ここで \(T\) は shape \(v\)、rate \(c\) の Gamma 分布で、後者の二乗平均は厳密に \(c^2/(v-2)\)。小さい \(t\) の有限区間は \(Z_v\) に比べて無視できる。(4) の \(O(t^{-1})\) は同じ平均評価を \(v-1\) に適用して \(O(v^{-1}\log v)\) となる。最後に正負の実軸の係数 \(2\sqrt{\pi/2}=\sqrt{2\pi}\) を掛ける。

詳細と原典の定理番号は [moment 専用ノート](notes/moment_asymptotic.md) に記録する。**(11) は Stirling 単独の帰結ではない。cyclicity は (8)–(9) だけで既に十分である。**

## 4. Hamburger determinacy と多項式稠密性

有限正 Borel 測度 \(\mu\) は全 moment を持ち、(9) を満たす。従って Hamburger moment problem は determinate、すなわち全 moment を共有する正 Borel 測度は一意である。さらに

\[
\overline{\mathbb C[x]}^{\,L^2(\mu)}=L^2(\mu).
\tag{13}
\]

適用する一次資料は [de Jeu, arXiv:math/0111019v2, Theorem 2.3, p.5](https://arxiv.org/pdf/math/0111019v2)。必要なら \(\mu/\mu(\mathbb R)\) に規格化するが、Carleman 発散と稠密性は変わらない。Carleman の determinacy だけを density と読み替えず、density を含む定理を使っている。

本件では稠密性を次の短い議論でも直接証明できる。\(h\in L^2(\mu)\) が全多項式に直交するとし、\(d\nu=\overline h\,d\mu\) とおく。Cauchy–Schwarz と (7) により、任意の \(0<b<c\) で

\[
H(z)=\int_{\mathbb R}e^{izx}\,d\nu(x)
\]

は \(|\Im z|<b/2\) で正則である。より狭い strip 上の各導関数は指数 moment によって優収束で正当化できる。直交性は全 \(H^{(r)}(0)=0\) を与えるので、identity theorem により \(H\equiv0\)。有限複素測度の Fourier 変換の一意性から \(\nu=0\)、従って \(h=0\) \(\mu\)-a.e.。これが (13) の直接証明である。

## 5. 偶 sector と x² への pushforward

\(\mu\) は偶測度であるから

\[
P_+h(x)=\tfrac12(h(x)+h(-x))
\]

は \(L^2(\mu)\) 上の直交射影。偶関数を近似する全多項式列に \(P_+\) を適用すると、誤差を増やさず偶多項式列になる。従って (3) が従う。

\(y=x^2\) へ移すなら

\[
d\nu_+(y)=\frac{|\Xi(\sqrt y)|^2}{\sqrt y}\,dy\quad(y>0),
\qquad \int_0^\infty y^n d\nu_+(y)=m_{2n}.
\tag{14}
\]

原点の表示上の特異性は可積分で、原点に atom はない。\(h(y)\mapsto h(x^2)\) は \(L^2(\nu_+)\) と \(L^2_{\rm even}(\mu)\) の等長同型である。よって \(\nu_+\) でも全多項式は稠密。

この測度の Stieltjes Carleman 条件は

\[
\sum_{n\ge1}\left(\int y^n d\nu_+\right)^{-1/(2n)}
=\sum_{n\ge1}m_{2n}^{-1/(2n)}=\infty.
\]

ここに誤って Hamburger 型の \(m_{4n}^{-1/(2n)}\) を入れない。後者の和の収束は、Stieltjes determinacy や polynomial density の反証にはならない。

## 6. weighted density を k の cyclicity へ戻す

\(\Xi\) は非零 entire 関数である。例えば \(\xi(2)>0\) なので恒等的な零関数ではない。したがって実軸上の零点集合は離散、Lebesgue 測度ゼロである。ここで全複素零点が実軸にあるとは一切仮定していない。

写像

\[
U:L^2(\mu)\longrightarrow L^2(dx),\quad Uh=\Xi h
\tag{15}
\]

は \(\|Uh\|_2^2=\int|h|^2d\mu\) により等長。さらに任意の \(g\in L^2(dx)\) に対して、\(\Xi\ne0\) の所で \(h=g/\Xi\)、零点で任意に 0 と定義すれば

\[
\int|h|^2d\mu=\int|g|^2dx,
\qquad Uh=g\quad\text{a.e.}
\]

なので **onto** である。\(1/\Xi\) が通常の unweighted L² multiplier として有界である必要はない。扱っている二つのノルムが異なることが重要である。\(\Xi\) の偶性から偶部分空間も相互に写す。

(3) と (15) により \(\{x^{2j}\Xi(x)\}_{j\ge0}\) の線形 span は \(L^2_{\rm even}(dx)\) に稠密。(1) と Plancherel により (2) が従う。非 unitary Fourier 規約に伴う全体係数 \(\sqrt{2\pi}\) および \(1/4\) は閉包を変えない。実関数の主張は近似列の実部を取ればよい。

## 7. RH independence と主張の境界

| 論点 | 結論 |
|---|---|
| 全 moment | (6) により無条件に有限 |
| Carleman divergence | (8)–(9)、粗い上界だけで成立 |
| Hamburger determinacy | 成立 |
| 全多項式の full weighted L² density | 成立 |
| 偶多項式の even weighted L² density | 成立 |
| 偶多項式の full weighted L² density | 偽。奇 sector を含まない |
| even derivatives の even physical L² cyclicity | PROVED |
| RH・単純零点・零点位置の入力 | なし |
| moment 精密式の追加入力 | 無条件の zeta 平均二乗定理のみ |
| 有限 head の rank / 最小特異値 | 未着手 |
| \(m=m(a,N)\to\infty\) の定量制御 | 未着手 |
| parameter-dependent full ground の捕捉 | 未証明・今回の結論に含めない |
| even/odd ground 比較・G*・RH | 未証明 |

この定理は、任意の **固定された** 偶 L² 関数を有限微分結合で任意精度まで近似できることを述べる。必要次数・係数・conditioning の一様評価は与えない。変化する ground state への定量近似、Weil form norm での core 性、複素 Fourier strip 上の収束は出ない。

global Weil radical の既知の元が L² に稠密になることも、Weil form が L² 連続であることを意味しない。従って「dense radical だから form が全域ゼロ」「dense だから full ground capture」という推論は行わない。

## 8. 第一報の六問への回答

1. **moment asymptotic**：(11)–(12)。特に \(m_{2n}^{-1/(2n)}\sim\pi e/(4n)\)。全 moment は有限。
2. **Carleman**：成立し、調和級数型で発散する。証明本体は精密漸近不要。
3. **polynomial density**：全多項式は \(L^2(\mu)\) に稠密。
4. **even density**：偶多項式だけで偶 sector を稠密に張る。full sector ではない。
5. **k の cyclicity**：\(\overline{\operatorname{span}\{k^{(2j)}\}}=L^2_{\rm even}(\mathbb R)\) を証明。
6. **RH 使用の有無**：使用なし。RH は OPEN のまま。

**K IS CYCLIC IN EVEN L2: PROVED.**

Priority 1 の第一報としてここで区切る。既存 state/proof graph へ自動 merge せず、finite-head spanning 以降はこの報告では実行しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/full_ground_capture/notes/moment_asymptotic.md`](notes/moment_asymptotic.md)
- [`research/rate_history/notes/boundary_rate_analysis.md`](../rate_history/notes/boundary_rate_analysis.md)
