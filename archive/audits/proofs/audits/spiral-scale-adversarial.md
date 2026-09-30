**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/spiral-scale-adversarial.md` · Original SHA-256: `e5cd62e562e5c872f009eaf3de3614a9fd6db2f90449f08f807d203590cb98e4`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Spiral / scale-flow の独立 DESTROYER 監査

2026-09-29。RH は OPEN。新規の零点排除定理は得ていない。以下の finite flow、entire function、scattering model は ζ/RH の反例ではなく、指定された一般推論の反例である。固定窓の拡張や数値改善は行わない。

対象は追加指示の multiplicative scaling、log-coordinate、self-duality、conservation、unitarity、reversibility、winding、self-similarity。物理的時間・numerology を前提にしない。

## 1. 精密命題と判定

| 候補 | 精密化 | 判定 |
|---|---|---|
| Spiral translation | 全 ζ 零点で $e^{-(\rho-1/2)u}$ の modulus が一定 | RH の言い換え |
| Self-duality | 零点集合が $s\mapsto1-s,\bar s$ で不変なら各点は中心線上 | FALSE: quartet |
| Conservation | determinant、symplectic form、不定 energy の保存が radial drift を排除 | FALSE: 第3節 |
| Reversibility | group と time-reversal involution の存在が drift を排除 | FALSE: 第3節 |
| Positive norm | 正定値 Hilbert norm を保存する group の実在 eigenmode は neutral | TRUE: 第2節。ζ mode の同定は未証明 |
| Scattering unitarity | 実 spectral parameter で unitary なら continuation の pole も実 | FALSE: 第4節 |
| Winding | 対称な family の winding 保存は軸外 quartet を排除 | FALSE: 第5節 |
| Self-similarity | exact scaling と self-duality は中心線性を強制 | FALSE: 第6節 |
| Global conserved Weil form | translation-invariant な global form なら非負 | FALSE inference: 保存と正値性は別、第7節 |

$z=s-1/2$ とすると holomorphic duality は $z\mapsto-z$ で、fixed set は $\{0\}$。
real-type symmetry と合成した $z\mapsto-\bar z$ の fixed set が imaginary axis である。
二つの対称性による **集合の不変性** と、各零点が反線形 involution の fixed point であることを区別する。

## 2. 正定値ノルムから得られる、本当に正しい機構

**命題 U。** 正定値 Hilbert 空間上の unitary group $T_u$ と非零ベクトル $v$ が

$$
T_uv=e^{-(\alpha+it)u}v\qquad(u\in\mathbb R)
$$

を満たすなら $\alpha=0$。
実際 $\|v\|^2=\|T_uv\|^2=e^{-2\alpha u}\|v\|^2$。

両方向に一様有界な group でも同じ結論。片方向だけの contractivity は $\alpha\ge0$ しか与えず、逆方向も同じ正定値空間で contractive なら isometry となる。逆写像が存在するという reversibility だけでは足りない。

問題はゼータ零点をこの命題の $v$ に同定するところにある。
$U_uf(x)=e^{u/2}f(e^ux)$ は $L^2(\mathbb R_+,dx)$ 上で unitary だが、
$x^{-1/2+it}$ は Hilbert 空間の元ではない:

$$
\int_0^\infty |x^{-1/2+it}|^2dx=\int_0^\infty\frac{dx}{x}=\infty.
$$

さらに実 $\alpha$ のどの値についても $x^{-1/2-\alpha-it}$ は同じ空間には入らない。正規化後の $e^{-\alpha u-itu}$ は test-distribution としては存在し、$\alpha\ne0$ では片端で指数増大するため tempered distribution ではない。「ζ resonance は tempered なこの種の mode」との同定まで証明しなければ、この差を零点排除に使えない。

任意の Hilbert 空間・operator を選んで、全零点に命題 U の mode を与えるという裸の存在命題は RH と同値になる。RH が真なら零点を index とする $\ell^2$ 上の diagonal unitary group を作れるからである。独立した自然な構成・domain・mode identification を伴わない Hilbert–Pólya の言い換えは採用しない。

## 3. 自然な保存量と reversibility を同時に満たす drift

まず

$$
D_u=\begin{pmatrix}e^{\alpha u}&0\\0&e^{-\alpha u}\end{pmatrix},\qquad\alpha\ne0
$$

は determinant $1$、symplectic form $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$、
不定二次形式 $G=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ を保存する。
swap involution $C$ により $CD_uC=D_{-u}$。
従って volume、Wronskian、symplectic pairing、不定 energy、reversibility は全て radial drift と共存する。

phase rotation も加えられる。$R_{\tau u}$ を実2次元 rotation とし、

$$
M_u=\operatorname{diag}(e^{\alpha u}R_{\tau u},
                        e^{-\alpha u}R_{\tau u}).
$$

これは実4次元の one-parameter group で、

$$
J_4=\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
G_4=\begin{pmatrix}0&I\\I&0\end{pmatrix}
$$

を保存し $\det M_u=1$。$S=\operatorname{diag}(1,-1)$ と
$C_4=\begin{pmatrix}0&S\\S&0\end{pmatrix}$ に対して
$C_4M_uC_4=M_{-u}$。generator の eigenvalues は $\pm\alpha\pm i\tau$。
正定値の conserved metric ではなく signature $(2,2)$ の energy である点が本質。

再現 script では

$$
R=\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix},
\qquad M=\operatorname{diag}(2R,R/2)
$$

の全 identity を有理数で検証した。$v=(1,0,1,0)$ の $G_4$ energy は全 iterate で $2$、Euclidean norm squared は $4^k+4^{-k}$。回転係数は有理演算のために選んだもので、特別な数論的意味を与えない。

$M^THM=H$ を満たす正定値 $H$ は存在しない。modulus $2$ の eigenvector を複素化した正定値 norm に入れると、norm preservation と矛盾する。したがって「保存量がある」から「保存量が正定値」への飛躍が致命的である。

## 4. Unitary scattering と complex resonance の両立

### 4.1 実軸で unitary な明示的 meromorphic function

$$
S(z)=\frac{(z-i)^2-4}{(z+i)^2-4}
=\frac{(z-2-i)(z+2-i)}{(z-2+i)(z+2+i)}.
$$

実 $t$ では numerator と denominator が conjugate なので $|S(t)|=1$。
upper half-plane では analytic かつ contractive。しかし $z=\pm2-i$ に相殺されない pole がある。
$S(-z)=S(z)^{-1}$ という reciprocal symmetry も満たす。
これは実軸 unitarity・analytic contractivity・reciprocity だけによる pole 排除の反例。
この特定の rational function を ζ の scattering matrix と同定してはいない。

実際の self-adjoint scattering にも同じ区別がある。$g>0$ の delta potential は
$H^1(\mathbb R)$ 上の閉非負形式
$\int|f'|^2+g|f(0)|^2$ から self-adjoint operator を持ち、
連続条件と derivative jump $f'(0+)-f'(0-)=gf(0)$ から

$$
r(k)=\frac g{2ik-g},\qquad t(k)=\frac{2ik}{2ik-g}
$$

を得る。実 $k\ne0$ で scattering matrix は unitary、even channel は
$(k-ig/2)/(k+ig/2)$ で、continuation は $-ig/2$ に pole を持つ。
これは negative imaginary axis 上の virtual-state pole と呼ぶべき例であり、Hilbert 空間の非実 eigenvalue ではない。

関連する標準的な区別は [Dyatlov–Zworski, Mathematical Theory of Scattering Resonances, §2.4](https://math.mit.edu/~dyatlov/res/res_final.pdf) にある。今回の反例の符号・pole は上の式から直接導出した。文献検索で real-axis unitarity の所在を確認したが、同書全体を再監査したとは主張しない。

### 4.2 Unitary dilation の compression は減衰 mode を持ち得る

$L^2(\mathbb R)$ 上の unitary group $(U_uf)(x)=f(x+u)$ を
$L^2(0,\infty)$ へ compression すると、$u\ge0$ で

$$
(T_uf)(x)=f(x+u)
$$

という contractive semigroup を得る。
$f(x)=\sqrt{2\kappa}\,e^{-(\kappa+i\omega)x}$、$\kappa>0$ は正規化された実在の Hilbert vector で、
$T_uf=e^{-(\kappa+i\omega)u}f$。
全実線の group は unitary でも compression の decay rate は非零である。
generator は半直線上の derivative、domain は $H^1(0,\infty)$ であり、全実線の self-adjoint translation generator と同じ domain ではない。

従って「全系が unitary」「圧縮系の resonance」「全系の Hilbert eigenmode」を交換してはいけない。

## 5. Winding と synthetic off-line quartet

$$
P_a(z)=((z-a)^2+1)((z+a)^2+1),\qquad 0\le a\le1/4.
$$

偶・実型で、零点は $\pm a\pm i$。$a=0$ では imaginary axis 上の double zeros、$a>0$ では off-axis quartet。
$|z|=2$ 上に零点はなく、全 $a$ で巻き数は $4$。
従って parameter 変形で winding が保存されても、零点は軸から離れ得る。
中心線上では

$$
P_a(it)=(a^2+1-t^2)^2+4a^2t^2>0\qquad(a>0).
$$

critical-line phase の変化がなくても、off-line zeros は存在する。order 1 が必要なら $\cosh(z)P_a(z)$ を用いれば quartet は残る。これは完成 ζ の代用品として全ての算術構造を再現したという意味ではない。

$\xi(1/2+it)$ が real であることは functional equation と real-type symmetry から従う。line 上の位相だけでは line 外の零点を数えられない。Argument principle は閉 contour 内の総数を数えるが、その数だけでは零点の実部を特定しない。line count と全 count の同一性を仮定するなら必要な零点排除を仮定したことになる。

## 6. Exact self-similarity と self-duality の併用も不十分

ROOT 提案の自然な geometric string を独立検算した。multiplicity $2^j$、length $8^{-j}$ の geometry は

$$
\zeta_{\mathcal L}(s)=\sum_{j\ge0}2^j8^{-js}
=\frac1{1-2\cdot8^{-s}},\qquad \Re s>1/3.
$$

長さの総和は $4/3$ で有限。continuation の complex dimensions は
$1/3+2\pi i k/\log8$。self-dual entire factor は

$$
\begin{aligned}
F(s)&=(1-2\cdot8^{-s})(1-2\cdot8^{-(1-s)})\\
&=\frac32-\sqrt2\cosh((s-1/2)\log8).
\end{aligned}
$$

$F(1-s)=F(s)$、real type、order 1、imaginary period $2\pi/\log8$ を持ち、零点は

$$
\Re s=1/3\quad\text{または}\quad2/3.
$$

それでも
$F(1/2+it)=3/2-\sqrt2\cos(t\log8)\ge3/2-\sqrt2>0$。
これは exact self-similarity、dual pairing、line phase の同時存在から中心線性を導く候補を反証する。$\zeta_{\mathcal L}$ の pole と Riemann ζ の零点は同じ対象ではない。

[Herichi–Lapidus, arXiv:1210.0882v3](https://arxiv.org/abs/1210.0882v3) は spectral operator の quasi-invertibility と指定垂直線上の ζ zero-free 条件の同値性を明記する。この種の全 $c\ne1/2$ の inverse spectral criterion は RH reformulation であり、self-similarity 単独の零点排除とは異なる。今回の geometric model は初等幾何級数からの独立反例で、新規性を主張しない。

## 7. 自然な global Weil conservation は実在するが、符号を与えない

非自明零点 $\rho=\beta+i\gamma$ に $z_\rho=\gamma-i(\beta-1/2)$ を対応させ、

$$
F_f(z)=\int f(x)e^{izx}dx,\qquad
Q_W(f,g)=\sum_\rho F_f(z_\rho)\overline{F_g(\bar z_\rho)}
$$

という既存規約を使う。$f,g\in C_c^\infty(\mathbb R)$ では strip 内の急減衰と $N(T)=O(T\log T)$ により絶対収束する。

$T_af(x)=f(x-a)$ なら

$$
F_{T_af}(z)=e^{iaz}F_f(z),\qquad
e^{iaz}\overline{e^{ia\bar z}}=1.
$$

従って **off-line zero を仮定しても**
$Q_W(T_af,T_ag)=Q_W(f,g)$。
これは人工的に imbalance の零集合を定義した量ではなく、既存 Weil 形式そのものの自然な保存則である。しかし正値性は従わない。

sample map $\mathcal A f=(F_f(z_\rho))_\rho$ はこの test space から $\ell^2$ へ入る。
零点の対称性により $z_\rho\leftrightarrow\bar z_\rho$ の添字交換 $J$ があり、$J=J^*=J^{-1}$。

$$
Q_W(f,f)=\langle\mathcal Af,J\mathcal Af\rangle.
$$

translation は sample space で
$D_a=\operatorname{diag}(e^{iaz_\rho})$ と intertwine し、
$D_a^*JD_a=J$。strip 幅から $\|D_a\|\le e^{|a|/2}$。
off-line pair がある場合、$D_a$ は ordinary $\ell^2$ norm の unitary group とは限らない。
pair の $J$ は $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ で、不定形式を保存するだけである。

有限 pair model では $(1,-1)$ の $J$ energy は $-2$ で、複素指数を掛けてもそのまま保存される。これを実際の ζ sampling range の負方向と同一視してはいけない。一方、その実際の range 上で常に $J$ が非負という主張は Weil positivity そのものであり、RH 同値である。

$J$ の positive eigenspace に勝手に projection すれば別の形式を作るだけになる。この部分空間が canonical/relevant であり、test functions の像を含み、scale evolution で不変で、同じ explicit formula を再現することを独立に示す必要がある。
また test-space 上の $\mathcal A$ の定義から、global $L^2$ 上の有界性・closability・自己共役 realization は自動でない。既存の [variational_closure.md](../../../reports/research/notes/variational_closure.md) の domain 監査を維持する。

## 8. 再現と採用基準

[spiral_scale_checks.py](../../../../artifacts/experiments/scripts/spiral_scale_checks.py) と
[spiral-scale-checks.json](../../../../artifacts/experiments/results/spiral-scale-checks.json) を保存した。
有理行列の全恒等式、rational scattering pole の非相殺、real-axis modulus を exact arithmetic で確認。Arb/ACB 192 bit で self-similar model の正の一様下界、代表零点の enclosure、symbolic identity との整合、indefinite pair の保存を確認した。零点で ball が0を含むこと自体を零点存在証明には使わず、存在は上の指数恒等式から証明する。

quartet winding の2048点計算は float diagnostic に限る。厳密な巻き数は明示された4根と boundary exclusion から従う。全 check は PASS。ζ の新しい零点計算や有限窓 certificate は含まない。

採用可能な新規 mechanism は、正定値性、mode 同定、domain、収束、trace/explicit formula との一致を **独立に**供給する必要がある。保存・対称・unitary・self-similar という語だけの候補と、RH 同値条件への再命名は反証または同値性判定で停止する。本稿の一般候補から主証明 graph への新規合流はない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/spiral-scale-checks.json`](../../../../artifacts/experiments/results/spiral-scale-checks.json)
- [`experiments/scripts/spiral_scale_checks.py`](../../../../artifacts/experiments/scripts/spiral_scale_checks.py)
- [`research/notes/variational_closure.md`](../../../reports/research/notes/variational_closure.md)
