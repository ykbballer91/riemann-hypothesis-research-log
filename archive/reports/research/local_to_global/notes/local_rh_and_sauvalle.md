**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global/notes/local_rh_and_sauvalle.md` · Original SHA-256: `dfb86d165f6a581ec6d4361a29b25e8f89fcbfc965397cd7745adbe655d18eaf`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Local RH と Sauvalle の大域 weak Mellin：対象・証明・接着の限界

Track A／2026-09-30。RH は OPEN。既知の局所定理を一次資料で確認し、その大域公式を独立に計算する限定監査である。新規性・新しい大域零点拘束・原論文全体の再検証を主張しない。既存ファイルは変更していない。

## LA0. 結論と一次資料の固定

局所 RH は、Hermite 関数または非退化 second degree character の**局所 Mellin 変換**について成立する。標準の局所因子 \(\pi^{-s/2}\Gamma(s/2)\) と \((1-p^{-s})^{-1}\) 自体は零点を持たない。Sauvalle の大域公式には、局所計算後も \(\zeta(s)\) が乗法因子として残る。特に LA5 の具体例では

\[
\Xi_f(s)=e^{-\pi i s/4}C_2(s)\frac{2\xi(s)}{s(s-1)},\qquad
C_2(s)=2^{1-s}-1+e^{\pi i/4}(2^s-1). \tag{LA.1}
\]

\(C_2\) の零点はすべて \(\Re s=1/2\)。したがって \(0<\Re\rho<1,\ \Re\rho\ne1/2\) では

\[
\operatorname{ord}_\rho\Xi_f=\operatorname{ord}_\rho\xi
=\operatorname{ord}_\rho\zeta. \tag{LA.2}
\]

この明示的大域 weak Mellin の零点拘束は RH と同値であり、局所 RH の追加帰結として証明されたものではない。

今回固定した原文は次のとおり。

|資料|実際に読んだ版・範囲|一次リンク／SHA-256|
|---|---|---|
|Bump–Choi–Kurlberg–Vaaler, *A Local Riemann Hypothesis I*, Math. Z. 233 (2000), 1–19|著者公開の **PRELIMINARY VERSION**, running date 11–8–96, 19 PDF 頁。§1 Theorem 1 と二つの証明、pp.2–5。刊行版との逐語照合は未実施。|[著者 PDF](https://kurlberg.github.io/eprints/lrh1.pdf)；`247fc396b95a54b963906a3dcd257f317ebe538f579a7442ffbaa136e6a7ec95`|
|P. Kurlberg, *A Local Riemann Hypothesis II*, Math. Z. 233 (2000), 21–37|著者公開 25 PDF 頁版。§§1–4、Theorems 3–4、Appendix Lemmas 16–24 の証明を読了。§5 Theorem 5 の複素体反例機構も確認。以下の頁はこの著者版。|[著者 PDF](https://kurlberg.github.io/eprints/lrh2.pdf)；`4e14f06156c972a14a23816eb1f0321e0751f85664e062f00a935745dbb075a4`|
|B. Sauvalle, *On weak Mellin transforms, second degree characters and the Riemann hypothesis*, Acta Arith. 177.3 (2017), 219–275|**刊行原文**。Definition 3.1、Propositions 3.2–3.3, 3.6、§§3.8–3.9 の局所零点証明、§4 全体を確認。§5 の高次元一般化は本監査の対象外。|[刊行 PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/92045)／[DOI](https://doi.org/10.4064/aa8240-7-2016)；`b6d8234b4ebe8acc7e148baab3bfbacb3d95498d7152b5092eb7fed789430fb5`|

著者の[刊行一覧](https://kurlberg.github.io/publications.html)で I/II の書誌を確認した。Sauvalle の [arXiv:1502.02633v1](https://arxiv.org/abs/1502.02633v1) は 2015-02-09 投稿で、abstract は adèlic statement と RH の同値性を明記する。ここでの定理番号・頁は 2017 年刊行原文に固定し、arXiv v1 本文との版差照合を行ったとはしない。PDF は一時領域に取得し、上記ハッシュを確認した。

## LA1. 実 Hermite Mellin：何の零点を拘束するか

### LA1.1 規約と定数

physicists' Hermite polynomial と著者公開版 p.2 の関数を文字どおり

\[
H_n(x)=(-1)^ne^{x^2}\frac{d^n}{dx^n}e^{-x^2},\qquad
f_n(x)=2^{-n/2}H_n(\sqrt{2\pi}x)e^{-\pi x^2}
\]

とする。半直線 Mellin は

\[
M_n(s)=\int_0^\infty f_n(x)x^{s-1}\,dx.
\]

偶数 \(n\) では \(\Re s>0\)、奇数 \(n\) では \(\Re s>-1\) が通常積分の収束域。多項式 \(p_n\) を

\[
M_n(s)=
\begin{cases}
\pi^{-s/2}\Gamma(s/2)p_n(s),&n\text{ even},\\
\pi^{-(s+1)/2}\Gamma((s+1)/2)\sqrt{2\pi}\,p_n(s),&n\text{ odd}
\end{cases} \tag{LA.3}
\]

で定義する。\(\deg p_n=\lfloor n/2\rfloor\)。この定義では \(p_0=1/2,\ p_1=1/\sqrt2,\ p_2=s-1/2\)。Γ は零点を持たず、(LA.3) は meromorphic continuation を与える。Γ の極と \(p_n\) の零点を区別する。

**原文のスカラー規格化の注意。** 公開 preliminary p.2 は上記 \(2^{-n/2}\) を表示しながら、raising operator
\(R=\sqrt{2\pi}x-(2\pi)^{-1/2}d/dx\)
について \(f_{n+1}=Rf_n\) と表示する。画像でも確認したが、文字どおりには \(Rf_n=\sqrt2 f_{n+1}\) が正しい。例えば \(f_1=2\sqrt\pi x e^{-\pi x^2}\) に対し \(Rf_0=2\sqrt{2\pi}x e^{-\pi x^2}\)。したがってこの規約での隣接次数漸化式は

\[
p_{n+1}(s)=\frac1{\sqrt2}
\begin{cases}
p_n(s+1)+p_n(s-1),&n\text{ even},\\
s p_n(s+1)+(s-1)p_n(s-1),&n\text{ odd}.
\end{cases} \tag{LA.4}
\]

これは各次数の非零スカラーの問題で、零点や次の oscillator 同次方程式に影響しない。**刊行版にも同じ誤植があるとは未確認**である。

### LA1.2 正測度の所在：Mellin–Plancherel による直交

\(h(u)=e^{u/2}f(e^u)\) とおけば

\[
M_f(1/2+it)=\int_{\mathbb R}h(u)e^{itu}\,du,\qquad
\int_{\mathbb R}M_f(1/2+it)\overline{M_g(1/2+it)}dt
=2\pi\int_0^\infty f(x)\overline{g(x)}dx. \tag{LA.5}
\]

これはここで固定した Fourier 規約での正確な定数である。同じ parity の Hermite 関数は半直線上でも直交する。従って \(p_{2j}(1/2+it)\)、\(p_{2j+1}(1/2+it)\) は、それぞれ

\[
|\Gamma(1/4+it/2)|^2dt,\qquad
|\Gamma(3/4+it/2)|^2dt \tag{LA.6}
\]

に関する直交多項式族となる。位相を調整すれば実係数、多項式次数は \(j\)。各測度は正で全実線に支持を持ち、全 moment が有限である。次数 \(j\) の直交多項式が \(j\) 個未満の実符号変化しか持たなければ、その符号変化点の積で作った低次多項式との内積が非零になり、直交性と矛盾する。よって零点は実かつ単純。これが \(\Re s=1/2\) を与える。

ここで必要なのは **Mellin 画像が Γ×有限次数多項式で、同一 parity の全次数が同じ正測度で直交すること**である。単に入力関数が正、Fourier 自己双対、あるいは全体の \(L^2\) 内積が正というだけではこの議論にならない。原典：I, Theorem 1, first proof, p.3。

### LA1.3 strip を縮める補題の厳密な規約

oscillator の式

\[
\left(x^2-\frac1{4\pi^2}\frac{d^2}{dx^2}\right)f_n
=\frac{2n+1}{2\pi}f_n
\]

を最初は部分積分が正当な十分右側で Mellin 変換し、その後 meromorphic continuation すると

\[
M_n(s+2)-\frac{(s-1)(s-2)}{4\pi^2}M_n(s-2)
=\frac{2n+1}{2\pi}M_n(s).
\]

Γ の漸化式で (LA.3) を除くと、\(q(z)=p_n(z+1/2)\) に対して

\[
(2n+1)q(z)=(z+a)q(z+2)-(z-a)q(z-2),\quad
a=\begin{cases}1/2&n\text{ even},\\3/2&n\text{ odd}.
\end{cases} \tag{LA.7}
\]

**有限多項式補題。** 非零多項式 \(q\) の全零点が \(|\Re z|\le c\)、\(c>0\) にあり、\(a>0\) とする。右辺 \(r(z)\) の全零点は \(|\Re z|<c\) にある。

証明：\(\Re z\ge c\) なら \(|z+a|>|z-a|\)。各根 \(r_j\) に対し
\(|z+2-r_j|\ge|z-2-r_j|\) で、\(q(z+2)\ne0\)。後者の積と最初の厳密不等式から二項の絶対値は等しくならない。\(\Re z\le-c\) も逆向きに同様。境界 \(\Re z=c\) では根ごとの不等式は弱い場合があるが、先頭因子が厳密なので十分である。次数 \(d\) なら \(r\) の最高次係数は \((4d+2a)\) 倍であり \(r\not\equiv0\)。□

(LA.7) に対し \(c=\max_j|\Re r_j|>0\) と仮定すれば、同じ多項式の零点が境界に存在することと矛盾する。有限個の根、境界最大値の達成、同一関数を返す固有方程式が決定的である。\(\xi\) や無限 Euler 積にはこの有限多項式補題をそのまま適用できない。原典：I, second proof および無番号 Lemma, pp.3–5。

## LA2. Kurlberg II：p-adic の同じ点と異なる点

\(F\) は奇数剰余標数の nonarchimedean local field、\(\mathcal O\) は整数環、\(\mathfrak p=(\varpi)\)、\(q=|\mathcal O/\mathfrak p|\)、\(|\varpi|=q^{-1}\)。\(\mathcal S(F)\) は局所定数・compact support。\(\nu\) は unitary multiplicative character で、unramified twist を外して \(\nu(\varpi)=1\) とする。この twist は \(s\) の純虚平行移動なので実部を変えない。

Theorem 4 の「Hermite」は任意 Schwartz 関数ではなく、Weil 表現を

\[
H=\mathrm{SL}_2(\mathcal O)\cap\mathrm{SO}(x^2+y^2)
\]

へ制限した固有空間 \(V_\chi\) の元を指す。\(-1\) が平方の split case では \(\mathrm{SO}_2(F)\) 全体は compact でないため、この交差を落とせない。通常の正 \(L^2(F)\) 内積は Weil 表現不変だが、実 Hermite の微分方程式を p-adic に移植した証明ではない。

スケーリングと Fourier 固有性で \(f\in\mathcal S(\mathcal O,\mathfrak p^N)\) に還元する。lift 空間 \(\mathcal L=\mathcal S(\mathfrak p,\mathfrak p^{N-1})\) とその直交補空間 primitive に分ける。Theorem 3（p.12）は
\(f\mapsto Z_\nu(f)(s)=\int_{F^\times}f(x)\nu(x)|x|^s d^\times x\)
の \(V_\chi\cap\mathcal S(\mathcal O,\mathfrak p^N)\) 上の像が高々一次元であることを示す。anisotropic case では multiplicity-free 性、split case では有限単数群の正則表現と primitive 消滅補題を用いる。像が非零の場合に、Mellin 画像の零点を保ったまま real-valued 代表を選べる点が次の係数比較に必要である。

### LA2.1 primitive の計算を独立に整理

\(\psi\) の conductor が \(\mathfrak p^N\)、self-dual additive measure、\(\operatorname{vol}_{\times}(\mathcal O^\times)=1\) の規約では
\(C=q^{1-N/2}/(q-1)\)、\(d^\times x=C\,dx/|x|\)。Fourier 固有値を \(\lambda\) とすると \(|\lambda|=1\)。

unramified \(\nu=1\) の非自明 primitive（\(N\ge1\)）について Lemma 20 は

\[
Z_1(f)(s)=Cf(0)\left[\lambda-q^{N/2-1-(N-1)s}
+C^{-1}\frac{q^{-Ns}}{1-q^{-s}}\right]. \tag{LA.8}
\]

非零変換の零点では、\(y=q^{1/2-s}\)、\(r=q^{-1/2}\) として

\[
1=\left|y^{N-1}\frac{y-r}{1-ry}\right|. \tag{LA.9}
\]

\((y-r)/(1-ry)\) は単位円板の内・境界・外をそれぞれ保つ。\(N\ge1\) だから (LA.9) は \(|y|=1\)、従って \(\Re s=1/2\) を強制する。denominator の点は極として扱い、零点には数えない。ground の標準 \(1_{\mathcal O}\) は零点なしの Euler 因子を与える。

ramified \(\nu\) の level を \(0<M<N\) とすると Lemmas 17,22 は

\[
Z_\nu(f)(s)=A+Bq^{-(N-M)s},\qquad
|B|=q^{(N-M)/2}|A| \tag{LA.10}
\]

を与える。実代表では二つの単数積分が共役であり、Gauss 和の絶対値
\(q^{1-M/2}/(q-1)\) と \(C\) の比が上記係数になる。非零の場合、二項の絶対値を等置して \(\Re s=1/2\)。原文 Lemma 11 は同じ結論を functional equation と「零点は一本の垂直線上」によって証明する。lift 部分への帰納で Theorem 4 を得る。

**共有点**は臨界中心の Tate 対称性、特別な表現論的入力、有限の係数関係である。**異なる点**は、実数体の正測度直交と有限差分固有方程式に対し、p-adic では finite-level decomposition、Gauss 和、単位円の有理式を使うことである。通常の正内積の存在だけでは両証明を代替できない。\(p=2\) をこの Theorem 4 に含めない。さらに II, Theorem 5（pp.14–17）は複素体の対応する主張の失敗を示す。複素体では Mellin 像が一次元を超え、線形結合で任意点に零点を置ける。

## LA3. Sauvalle の局所 weak Mellin は別の関数クラス

\(F=\mathbb R\) または有限拡大を含む p-adic field とし、今回用いるクラスは

\[
f(x)=\psi(ax^2/2+bx),\qquad a\ne0.
\]

これは \(|f|=1\) の second degree character で、Hermite Schwartz 関数そのものではない。\(\varphi\in C_c^\infty(F^\times)\) に対し

\[
(\varphi\star f)(y)=\int_{F^\times}\varphi(x)f(x^{-1}y)d^\times x,
\quad
\operatorname{Mell}(\varphi\star f,s,\chi)
=\operatorname{Mell}(\varphi,s,\chi)\,\zeta_f(s,\chi). \tag{LA.11}
\]

Definition 3.1 と Propositions 3.2–3.3（pp.226–229）は smoothing 後が Schwartz であることから、\(\Re s>0\) でこの値を定義する。従って未収束の生の振動積分を通常の絶対収束積分として用いない。\(\chi\) は単数群上の unitary character を固定し、norm の純虚 twist は \(s\) に吸収する。変換が恒等的に零の場合は零点定理から除外する。

### LA3.1 実数体：Kummer 方程式の正積分

\(\psi_{\mathbb R}(x)=e^{-2\pi ix}\)、\(a>0\)、\(b\in\mathbb R\) とする。Propositions 3.13,3.15（pp.242–245）は

\[
\zeta_{a,b}(s)=e^{-\pi is/4}a^{-s/2}\pi^{-s/2}\Gamma(s/2)
{}_1F_1(s/2;1/2;\pi i b^2/a), \tag{LA.12}
\]

\[
\zeta_{a,b}(s,\operatorname{sgn})=-2\pi ib\,
e^{-\pi i(s+1)/4}a^{-(s+1)/2}\pi^{-(s+1)/2}\Gamma((s+1)/2)
{}_1F_1((s+1)/2;3/2;\pi i b^2/a). \tag{LA.13}
\]

特に \(b=0\) の sign sector は恒等的に零である。\(a<0\) は共役を用いて戻す。

Proposition 3.16 の核となる計算を記す。\(v>0\) とし
\({}_1F_1(u;v;it_0^2)=0\)、\(t_0>0\)。\(\alpha=v-1/2\) として

\[
Y(t)=t^\alpha e^{-it^2/2}{}_1F_1(u;v;it^2),\qquad
Y''=\left(\frac{\alpha^2-\alpha}{t^2}-t^2+2i(2u-v)\right)Y.
\]

\(W=Y\overline{Y'}-\overline Y Y'\) なら

\[
W'=-4i(2\Re u-v)|Y|^2,\qquad
0=W(t_0)-W(0)=-4i(2\Re u-v)\int_0^{t_0}|Y|^2dt. \tag{LA.14}
\]

\(|Y|^2=O(t^{2v-1})\) は積分可能、局所展開から \(W(0)=0\)。積分は厳密に正なので \(\Re u=v/2\)。虚引数の符号が逆でも共役で同じ結論。\(u=s/2,v=1/2\) または \(u=(s+1)/2,v=3/2\) を入れると Theorem 3.17（p.246）。Γ に零点がないことと合わせ、非零 weak Mellin の全零点は \(\Re s=1/2\) にある。

正性の所在は、仮定した Mellin 零点を Dirichlet endpoint にする**この局所 ODE の \(\int|Y|^2\)** である。adèle 全体について同じ境界問題や同じ ODE を供給する定理ではない。

### LA3.2 非アルキメデス体：valuation shell と unitary Weil index

Theorems 3.10（pp.235–238）と 3.11（pp.239–242）はこの second degree class に対して \(p=2\) も含む。Kurlberg II の奇数剰余標数という適用範囲とは異なる。

unramified の証明は \(\theta_f(y)=\int_{\mathcal O}f(yx)dx\) を用いる。\(a\) を平方スケーリングして \(|a|=q^d\) または \(q^{d-1}\) に正規化する。ここで \(q^d\) は different の norm。compact additive subgroup 上での character の積分は 0 またはその体積なので、片側は一つの ball の指示関数となる。もう片側を Weil index \(|\gamma_f|=1\) を伴う反転公式が決める。

具体的には \(|a|=q^d\)、non-ground case \(k\ge1\) では

\[
\operatorname{Mell}(\theta_f,s)
=q^{-d}\left(\frac{q^{-ks}}{1-q^{-s}}+
\gamma_f\frac{q^{k(s-1)}}{1-q^{s-1}}\right),\quad 0<\Re s<1.
\]

\(X=q^{s-1/2},r=q^{-1/2}\) として零点の多項式は

\[
\gamma_f X^{2k}-\gamma_f rX^{2k-1}-rX+1=0. \tag{LA.15}
\]

独立な確認として、これを \(\gamma_f X^{2k-1}(X-r)=-(1-rX)\) と書けば、LA2 と同じ円板の内外の絶対値比較から \(|X|=1\) が従う。原文は単位円上の符号変化を数える。\(|a|=q^{d-1}\) は反転で隣接する valuation がずれる場合で、同じ円周拘束になる。ground case の weak Mellin は Euler 因子の非零定数倍で、零点なし。

ramified case は Eq.(3.4) と character cancellation により、smoothing の支持が互いに反転する二つの shells に限られる。pp.241–242 の最終式は、非零定数を除いて

\[
q^{-ks}+\omega q^{-k-\delta/2}q^{(k+\delta)s},
\qquad |\omega|=1,\quad\delta\in\{0,1\}. \tag{LA.16}
\]

\(2k+\delta>0\) なら絶対値比較で \(\Re s=1/2\)。\(k=\delta=0\) は定数または恒等零として別扱いする。ここにも Euler 積全体の零点を扱う新しい正測度はない。

複素体へは一律に一般化しない。Sauvalle §3.10.2, Proposition 3.19（p.248）の \(\psi_{\mathbb C}(az^2/2)\) は、定数を除き \(\Gamma(s/2)/\Gamma(1-s/2)\) 型で正の偶数に零点を持つ。\(a|z|^2/2\) 型とは別クラスである。

## LA4. adèlic 接着で実際に証明される等式

Sauvalle §4.1 は factorizable な非退化 second degree character を扱う。\(\mathbb Q\) では各 completion の additive automorphism は scalar 型になり、この分解を使える。Definition 4.1、Proposition 4.2 は adèlic compact multiplicative test function による smoothing を定義し、Schwartz–Bruhat 関数になることを証明する。

**収束半平面が変わる。** Proposition 4.3（p.253）の大域 weak Mellin \(\Xi_f(s,\chi)\) の最初の定義域は \(\Re s>1\)。各局所の \(\Re s>0\) を全素点の積にそのまま引き継げない。Proposition 4.5 は Tate の大域 functional equation による meromorphic continuation を与える。以下は \(\mathbb Q,\chi=1\) を主例とし、一般 Hecke character の norm twist による極の平行移動を混同しない。

Theorem 4.6（pp.254–255）の証明は有限集合 \(S\supset T\) を取る。\(S\) は infinity、ramification、different、2、標準 smoothing にならない場所を含み、\(T\) は infinity と character の ramified places。\(v\notin S\) では

\[
\lambda(1_{\mathcal O_v^\times})f_v=1_{\mathcal O_v},\qquad
\zeta_{f_v}(s,\chi_v)=(1-\chi_v(\varpi_v)(N\mathfrak p_v)^{-s})^{-1}.
\]

従って最初 \(\Re s>1\) で

\[
\begin{aligned}
\Xi_f(s,\chi)
&=\prod_{v\in S}\zeta_{f_v}(s,\chi_v)
\prod_{v\notin S}(1-\chi_v(\varpi_v)(N\mathfrak p_v)^{-s})^{-1}\\
&=L(s,\chi)\prod_{v\in S}\zeta_{f_v}(s,\chi_v)
\prod_{v\in S\setminus T}(1-\chi_v(\varpi_v)(N\mathfrak p_v)^{-s}).
\end{aligned} \tag{LA.17}
\]

その後、等式全体を meromorphically continue する。これは無限積を critical strip で通常収束させた証明ではない。

原文 Theorem 4.6 は大域零点を非自明 Hecke 零点または局所零点として記述する。本監査で直接用いる範囲は \(0<\Re s<1\) と \(\mathbb Q\) の具体式 LA5 である。ここでは局所 weak Mellin の極がなく、有限 Euler 補正も非零なので、極・零点の相殺を曖昧にせず零点次数を比較できる。複素 places の local RH が失敗する一般 number field に「全局所零点は線上」を加えてはいけない。

## LA5. 接着を妨げる明示公式と、零点・極の区別

標準 global additive character と \(f(x)=\psi_{\mathbb A}(x^2/2)\)、\(\chi=1\) を固定する。Sauvalle Proposition 3.6（pp.231–232）、Proposition 3.13、および (LA.17) から

\[
\zeta_{f_\infty}(s)=e^{-\pi is/4}\pi^{-s/2}\Gamma(s/2),\quad
\zeta_{f_p}(s)=\frac1{1-p^{-s}}\ (p\ne2),\quad
\zeta_{f_2}(s)=\frac{C_2(s)}{1-2^{-s}}. \tag{LA.18}
\]

従って (LA.1) が厳密に得られる。

\(C_2\) の零点位置は局所定理を使わず検算できる。\(w=2^s,\eta=e^{\pi i/4}\) なら
\(w C_2=\eta w^2-(1+\eta)w+2\)。さらに
\(w=\sqrt2e^{-\pi i/8}v\) とすると

\[
v^2-\sqrt2\cos(\pi/8)v+1=0.
\]

中間係数の絶対値が 2 未満なので二根は \(|v|=1\)。従って \(|2^s|=\sqrt2\)、すなわち \(\Re s=1/2\)。\(C_2(0)=1\)、\(C_2(1)=e^{\pi i/4}\) である。

\(\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)=2\xi(s)/[s(s-1)]\) は 0,1 に極を持つ。局所 Euler 因子の \(s=2\pi i\mathbb Z/\log p\) にある極を、大域 continuation の全極と取り違えない。局所 Γ の負の偶数の極は \(\zeta\) の trivial zeros と相殺される。LA.1 はこれを済ませた completed expression であり、非自明零点について (LA.2) を与える。

したがって次は同値である：

1. RH。
2. この一つの具体的な \(\Xi_{\psi(x^2/2)}\) の全零点が \(\Re s=1/2\) にある。

第2条件は新たな弱い局所入力ではない。局所の正性・有限次数・Gauss 和は \(C_2\) の零点位置を決定するが、\(\xi\) 因子を除かない。

Hermite/Tate の通常 Schwartz 入力でも同じことが起きる。real place に偶 Hermite \(f_{2j}\)、finite places に \(1_{\mathbb Z_p}\) を置くと、(LA.3) の半直線規約に対し全 \(\mathbb R^\times\) 積分は二倍なので

\[
Z_{2j}(s)=2p_{2j}(s)\Lambda(s). \tag{LA.19}
\]

\(j=0\) は \(2p_0=1\) で標準完成ゼータ。\(j=1\) は \(2(s-1/2)\Lambda(s)\)。局所 RH が新しく保証するのはこの多項式因子の零点であり、\(\Lambda\) の臨界線外零点が仮に存在すれば (LA.19) にも同じ重複度で残る。II Introduction pp.2–3 が説明する「有限個の Hermite local factors の置換」の正確な範囲はこれである。

最後に、\(\sigma>1\) の標準 Euler 積は零点なしの因子の積として収束するが、critical strip の \(\zeta\) はその解析接続である。有限 Euler 積を掛けた Γ 因子は \(\Re s>0\) で零点なし。その列が critical strip 上で nonzero holomorphic limit へ局所一様収束する、と新たに仮定すれば Hurwitz は「極限も零点なし」を与える。これは大域零点を説明する機構にさえならない。局所因子の零点位置だけから、収束域外における continuation の零点位置を推定する段階が欠落している。

## LA6. 採否

|入力・提案|今回の判定|
|---|---|
|実 Hermite の Γ×直交多項式、正測度、shift-strip lemma|局所定理として採用可能。定数・有限次数・同一固有方程式を保持する。|
|Kurlberg の p-adic Hermite LRH|奇数剰余標数、指定 Weil eigenspace、非零 Mellin 画像の範囲で採用可能。|
|Sauvalle の second degree weak Mellin LRH|実数体と p-adic の指定クラスで採用可能。smoothing 定義、恒等零の除外、複素体での範囲制限が必要。|
|標準 unramified local factors の zero-freeness|既知だが大域零点拘束には空の情報。極と収束半平面を別に管理する。|
|有限 local correction × completed ζ の大域公式|厳密な接着公式として採用。大域ゼータ因子の零点問題を残すことを同時に明示する。|
|局所 LRH だけから adèlic LRH を結論|不成立の推論。具体式 (LA.1)–(LA.2) で不足が露出する。adèlic 零点拘束を追加仮定すると、この具体例ですでに RH 同値。|

**停止判断：局所側の未読条件を RH 非依存の大域 confinement として採用できる箇所は見つからなかった。** 本監査は局所の既知定理を否定せず、それらから大域 RH が証明されたとも扱わない。

独立読取監査：DESTROYER は LA1.3 の境界を含む strip 不等式・最高次係数、LA5 の二次式への代入・単位円根・零点次数等式・この固定 weak Mellin の RH 同値性を独立に確認し PASS とした。三論文全体の独立再監査を意味しない。
