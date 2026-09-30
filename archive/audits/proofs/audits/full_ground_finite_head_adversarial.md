**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `proofs/audits/full_ground_finite_head_adversarial.md`; original SHA-256: `bbc8b202d83c210cc2aaf1f178c55d8a194e338e55877fe974650410dacd0f90`. Publication formatting does not constitute a new mathematical audit.

---

# Priority 2 — finite even Fourier head 独立監査

2026-09-30。**STATUS: RIEMANN HYPOTHESIS OPEN.**

**判定：PASS WITH EXPLICIT SCOPE。** 以下で特定した2件の記述上の修正は反映済み。
Priority 2 の通常の有限 head の rank と conditioning に限る。新規性、Weil positivity、
Priority 3/4、growing-order の一様制御、full ground capture、G*、RH の証明を認める判定ではない。
内部 AI-agent による独立読取・計算監査であり、外部査読・形式証明ではない。

## 1. 監査対象と方法

対象は `research/full_ground_capture/priority2/` の次の新規成果物。

- `notes/algebraic_rank.md`：AR1–AR7。
- `notes/conditioning_literature.md`：有限次元の直接計算と原典の適用範囲。
- `notes/tail_conditioning.md`：TC0–TC6。
- `notes/diagnostics.md`。
- `experiments/finite_head_probe.py`、`certify_tail_criterion.py`、`validate_diagnostics.py`。
- `experiments/probe_85.json`、`probe_115.json`、`tail_certificates.json`、`diagnostic_validation.json`。

既存の cyclicity と Fourier 規約を読み取り、符号・規格化・量化を独立に導出した。
今回この監査者が Gautschi 等の全原論文を再読したとは主張しない。原典調査担当の
locator と採用条件を確認し、今回使う cardinal 係数・ノルム不等式は直接再導出した。
新規の確率的 sampling 定理は actual fixed grid へ適用していない。

認証コードは `main()` を実行せず import し、320 bit で2つの窓区間と1つの不成立例を
再計算した。bytecode 書込みを無効化し、原稿・既存成果物・実験 JSON は変更していない。
これは別精度の独立実行であり、別の interval library や別実装による二重認証ではない。
85/115桁の実験全体は再実行せず、コード読取と保存値の独立比較を行った。

## 2. 射影・標本・偶 sector — PASS

零延長した cosine head の射影を使う限り

\[
P_NR_a=P_N,\qquad P_N(1-R_a)=0.
\]

従って「切断前の \(P_Nf\)」を全線 Fourier 標本の意味で使うことはできない。
TC0 は全線標本写像 \(S_{a,N}\) を別に定義し、

\[
B_{\cdot j}=S_{a,N}(R_af_j)
=S_{a,N}f_j-S_{a,N}((1-R_a)f_j)
\]

としている。この修正は正しい。対象関数の積分は絶対収束するが、\(S_{a,N}\) は
全 global \(L^2\) 上の有界射影ではない。

偶 head の正規直交基底は

\[
b_0=(2a)^{-1/2},\qquad
b_n=(-1)^n a^{-1/2}\cos(\pi nt/a),\quad1\le n\le N
\]

であり、次元は \(N+1\)。\(+n,-n\) を二重に数えない。
ideal 行列は相異なる \(q_n=-(\pi n/a)^2\) の Vandermonde と対角 Xi 因子の積なので

\[
\operatorname{rank}A_m=\min(m+1,\#\{0\le n\le N:\Xi(\pi n/a)\ne0\}).
\]

\(n=0\) は \(\Xi(0)>0\)。同じ grid hit の零点重複度を複数の失われた行と数えない。
微分列は \((-x^2)^j\Xi(x)\) であって Xi の jet 標本ではない。
ideal の零行から actual の零行は従わず、有限精度の grid hit を exact equality としない。

## 3. Actual recurrence と finite-prefix 定理 — PASS

偶 \(f\) に対し \(b'_n(\pm a)=0\)、\(b_n''=q_nb_n\) なので

\[
\int_{-a}^a f''b_n=q_n\int_{-a}^a fb_n+2f'(a)b_n(a).
\]

\(b_n(a)=a^{-1/2}\) for \(n\ge1\) であることが shifted phase の役割である。
従って AR8 の

\[
B_{nj}=q_nB_{n,j-1}+d_nk^{(2j-1)}(a),\quad
d_0=\sqrt{2/a},\quad d_n=2/\sqrt a
\]

は正確。\(R_aD^{2j}k\) と、端点分布を含む \(D^{2j}(R_ak)\) の区別も保持されている。

CY1 と有界全射 \(T=P_NR_a\) により、各固定 \((a,N)\) で有限 initial prefix が
head を exact に張る。有限次元性を使うこの結論は正しいが、必要次数の明示上界を
供給するものではない。AR4 の Gaussian-polynomial 模型は、cyclicity 単独から
一律の初期次数を導く推論だけを否定し、actual 正値 theta 核の反例とはしていない。

## 4. 固定 N の大窓と有限例外 — PASS

\(m=N\) を固定すると

\[
A_N=a^{-1/2}D(a)W\operatorname{diag}(1,a^{-2},\ldots,a^{-2N}),
\quad D(a)\longrightarrow D_\infty\text{ invertible}.
\]

固定 Vandermonde \(W\) の可逆性による下界と最終列による上界から
\(\sigma_{\min}(A_N)=\Theta_N(a^{-2N-1/2})\)。
actual tail はこれより小さく、AR17 の eventual full rank が従う。

AR18 の determinant 定数も確認した。row phase の符号は
\((-1)^{N(N+1)/2}\)、負 nodes の Vandermonde の符号も同じで相殺する。
したがって

\[
\det B_N(a)\sim
\frac{(\Xi(0)/4)^{N+1}}{\sqrt2}
\pi^{N(N+1)}\prod_{0\le r<s\le N}(s^2-r^2)
\,a^{-(N+1)(N+1/2)}.
\]

\(B(a)=\sqrt a\,C(a)\) とした \(C_{nj}\) は固定区間上の
\(\eta_n\int_{-1}^1k^{(2j)}(ax)\cos(\pi nx)dx\)。
theta 級数は \(|\Im t|<\pi/4\) の compact 上で holomorphic であり、\(C\) は
\(a=0\) を含む strip へ解析的に延長する。大きい正 \(a\) で determinant が非零なので
恒等的零ではない。零点の内部集積、0への集積、大窓での零点を全て排除できるため、
各固定 \(N\) の actual 最小 prefix の退化窓は有限集合である。

これは ideal grid-hit 集合の主張ではない。例外の位置・個数・空集合性や、\(N\) に
一様な閾値は得ていない。さらに

\[
\sigma_{\max}(B)=\Theta_N(a^{-1/2}),\qquad
\kappa_2(B)=\Theta_N(a^{2N})
\]

なので、eventual exact rank を大窓で一様な良条件性へ昇格していない点は適切である。

## 5. Tail majorant と interval certificate — PASS

\(y=\pi q^2e^{2t}\) への変数変換で
\(e^{t/2}=\pi^{-1/4}q^{-1/2}y^{1/4}\)、\(2dt=dy/y\)。
従って TC3 の \(\Gamma(\ell+1/4,q^2Y)\) と係数は正しい。
\(Y\ge4m+4\)、\(\ell\le2m+2\) は incomplete-Gamma の
\(\Gamma(\nu,x)\le2x^{\nu-1}e^{-x}\) の前件を満たす。
さらに \(\log q\le(q^2-1)/2\) で多項式因子を吸収し、TC4 の幾何級数上界を得る。

行の norm 係数の平方和は \(1/(2a)+N/a\) なので TC5 の \(\tau\) も正しい。
非負 nodes の Lagrange cardinal 多項式の係数絶対値和は
\(\beta_n=\prod_{r\ne n}(1+t_r)/|t_n-t_r|\)。
逆行列の column \(\ell^2\) norm を \(\ell^1\) norm で抑えることで
\(\|A^{-1}\|_2\le L\)、従って
\(L\tau<1\Rightarrow\sigma_{\min}(B)\ge L^{-1}-\tau>0\) が従う。
Xi 対角因子・原点の規格化を落としていない。

320-bit 再実行で得た包含は次の通り。

| 対象 | \(L\tau\) の包含 | \(L^{-1}-\tau\) の包含 | 判定 |
|---|---|---|---|
| \(a\in[1.499999,1.500001],\ N=m=4\) | \([4.527\cdot10^{-7}\ \pm8.21\cdot10^{-11}]\) | \([0.05172\ \pm3.42\cdot10^{-6}]\) | full rank 認証 |
| \(a\in[1.999999,2.000001],\ N=m=6\) | \([7.13\cdot10^{-40}\ \pm4.05\cdot10^{-43}]\) | \([0.034071\ \pm8.59\cdot10^{-7}]\) | full rank 認証 |
| \(a=1,\ N=m=2\) | 約 \(1.1278838405\) | 負の下界 | 十分条件不成立、rank は未判定 |

前二行は原稿の \(L\tau<4.529\cdot10^{-7},7.135\cdot10^{-40}\) および
raw 最小特異値 \(>0.0517,0.0340\) を確かに支持する。
Arb の入力 ball が窓区間全体を含み、acb completed-zeta の実部を含む区間を用いている。
Xi の実性は既知の実対称性によるもので、単に数値虚部が0を含むことだけで証明していない。
zero table、SVD、浮動 determinant は certificate に使っていない。
この証明のソフトウェア上の信頼基盤は python-flint/Arb/acb と記載した解析的不等式である。

## 6. Physical Gram と fixed-head 極限 — PASS

head Gram \(B^*B\)、global Gram、support Gram は正しく区別されている。
head Gram での whitening は射影後の norm に関する恒等式であり、切断前の lift cost を
評価しない。global/support Gram は解析性と \(p(x^2)\Xi(x)=0\) の議論で正定値。

\(G=LL^*\) に対する実験の \(B(L^*)^{-1}\) は \(BG^{-1/2}\) と同じ特異値を持つ。
全ての関数と実装行列は実数なので、コードの transpose は conjugate transpose と一致する。

TC12–13 の

\[
B_mG_m^{-1}B_m^*=T\Pi_mT^*,\qquad
0\le T\Pi_mT^*\uparrow I
\]

は固定有限 head で operator norm 収束する。\(0<\epsilon<1\) に対する右逆 norm の
存在評価は正しい。窓を固定して次数を増やすこの定性的事実と、次数を固定して窓を
増やす TC11 を取り違えていない。

補足の攻撃結果：非零 Xi 標本での ideal 評価は、global \(L^2\) ノルムについて
微分多項式 span 全体上で非有界である。もし偶多項式の一点評価が \(L^2(|\Xi|^2dx)\)
で有界なら、Riesz 表現による絶対連続測度が対称 atomic measure と全 moment を共有する。
指数 moment による Fourier 解析接続・一意性から両測度が等しくなり矛盾する。
従って fixed-column tail が小さいことを、増加する全微分空間で一様に小さい operator
誤差へ置き換えられない。この限定的障害は actual fixed-head 定理を否定しない。

## 7. 数値診断の範囲と修正履歴

`finite_head_probe.py` の incomplete-Gamma base tail、端点漸化式、独立の区間求積、
Cholesky 向き、cosine 規格化は整合する。
16項 theta と \([-4,4]\) の global Gram は有限打切りで、区間認証されていない。
精度・求積次数を変えた一致は SVD の exact rank 証明ではない。
保存した grid-hit 例も exact hit や actual rank の認証ではないと明示されている。

保存 JSON の7ケースを独立に照合した。35桁に丸めた raw 値の比較は相対 \(10^{-30}\)
以内、physical 最小特異値の最大相対差は約 \(1.139\cdot10^{-22}\) で、記載した
\(10^{-19}\) 以内を満たす。115桁実行で記録した二経路係数残差は全て \(10^{-95}\) 以下。
これは保存された浮動計算の整合性検査であって、真値の包含誤差ではない。

修正済み事項：

1. TC5 の右逆評価の前件を単なる \(\epsilon>0\) から \(0<\epsilon<1\) へ修正。
2. 35桁保存値からは裏付けられない「raw repeat agreement \(<10^{-65}\)」を削除。
   \(<10^{-30}\) の serialized-value 比較へ弱め、求積残差が115桁実行の値であることも明記。

両修正を再読し、**RESOLVED** とする。現監査対象に blocking mathematical error は残らない。

## 8. 停止境界

PASS は有限偶 head の rank・明示的十分条件・2つの小窓区間の認証に限定する。
特定条件の失敗から rank loss は結論しない。次数・head・窓を同時に増やす定量評価、
全 Weil 行列の ground、parity 比較、energy convergence、ES、G*、RH は今回未取得。
Priority 3/4 を開始したものではない。既存研究ファイルと公開用コピーは本監査では変更していない。

## 9. 監査済み snapshot

本監査自身を除く SHA-256。以下は Priority 2 ディレクトリからの相対 path。

| Path | SHA-256 |
|---|---|
| `notes/algebraic_rank.md` | `a7b88f62d53d9c7a8ed92c97cd74a0bc750fdc2167f8ae3b64f1e2192c0bc95a` |
| `notes/conditioning_literature.md` | `8ee50f66fa18cc433b6508507afd975c36f969148e5ada4b9cfd517ddcaf0a51` |
| `notes/tail_conditioning.md` | `d1ebde4f59a381a6bdaefb76fe89e2e23355b4421a85b1e2d1225eaa63c73fe8` |
| `notes/diagnostics.md` | `889566b20bc655d60037e86b6d8f7bcb61259ed6eff2e0e4de938d75d330ec1e` |
| `experiments/finite_head_probe.py` | `3a958083eea64a993cb3c23188b32c23bacd03536de3f6469b34b49a0c49251c` |
| `experiments/certify_tail_criterion.py` | `fee1b9b6f7fae6598c2e567e876ad792d70a8ab2277eb05098a31ef823a75c3e` |
| `experiments/validate_diagnostics.py` | `ee6de8bb5ff8bc793e74e3e97a3187950ceefaa4985c03853efef108778ee24c` |
| `experiments/probe_85.json` | `8b19c1b6b00f12df574296e5656acc2925b26562291bdc7f5037e072a7485f17` |
| `experiments/probe_115.json` | `0b8b279869452de4a24831f58be5efc4d0d4776a0c0011013e53073515bcc581` |
| `experiments/tail_certificates.json` | `afd934e9e37d121c92920410e4ee763ac373284b0bee1b735f84461bfa43dcc6` |
| `experiments/diagnostic_validation.json` | `667afe205a6baac6cda5bba95d49198f4c5241dd3972df90e5a44f241d9c0d79` |

## 10. 最終主文・state の追加読取監査

`finite_even_head_spanning.md` 全体と `state.json` を追加確認し、PASS とする。主文 F の ground に関する yes は、各固定 head の **射影済み** hierarchy への代数的包含だけを意味する。global radical 所属性、ground の選択、係数の小ささ、cofinal uniform capture を主張していない。state の `independent_audit=PASS_WITH_EXPLICIT_SCOPE` と各 OPEN/未開始 field は主文と整合する。

320-bit 入力 ball が二つの exact-decimal 端点を含むことも包含比較で確認した。最終原稿の hash を以下に固定し、Priority 2 で停止する。Priority 3/4 は開始しない。

| Path | SHA-256 |
|---|---|
| `research/full_ground_capture/priority2/finite_even_head_spanning.md` | `b5af4c2a73f0388a401b99533191258ec5f47a4744ed71c71ce3b7b3a3dc60e5` |
| `research/full_ground_capture/priority2/state.json` | `788e093efb38c5dda549cd027893e40c7464fd0a1c2615627ae8565f1109d81c` |
