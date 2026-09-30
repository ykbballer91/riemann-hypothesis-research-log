**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global/notes/spectral_approximants_and_exact_gap.md` · Original SHA-256: `1619fb9bab24a8637a1fe6549ed23871141cd0c895049dab8fe4b9506f87174b`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Finite-prime approximants と切断点の独立検算

2026-09-30。RH OPEN。既存ログ・主グラフを変更しない限定監査。

## 1. 使用版・変数

主資料は [CCM, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1)。
34頁PDFの §§3,5,7,8、特に Theorem 5.10 と「The missing steps」全節を照合した。
2026 EMS の書籍中の章としての掲載は
[出版社目次](https://ems.press/content/book-chapter-files/53351) で確認した。
出版社の章本文は取得できなかったため、以下の式番号・頁は固定した arXiv v1 のもの。
後続の [Connes 2026, §§6.1–6.6](https://arxiv.org/html/2602.04022v1)
も同じ二つの未解決点を明記する。新しい収束証明と読み替えない。

以下では
\[
 \mathscr X(z)=\xi(1/2+iz),\qquad
 \Omega=\{z:|\Im z|<1/2\},\quad z_*=i/4.
\]
RH は \(\mathscr X\) の全零点が実数であること。以前の
\(z=s-1/2\) とは座標が \(i\) 倍異なる。
\(\mathscr X(z_*)=\xi(1/4)>0\) はRHを使わない。
実数 \(0<s<1\) で \(\zeta(s)<0\)、\(s(s-1)<0\)、Gamma因子が正だからである。

## 2. 有限構成の実際の対象

\(\lambda>1,\ L=2\log\lambda,\ I_\lambda=[\lambda^{-1},\lambda]\)。
\[
 D_\lambda=-iu\partial_u,\quad
 \operatorname{Dom}D_\lambda=H^1_{\rm periodic}(I_\lambda,d^*u),
\qquad
 V_j(u)=L^{-1/2}e^{2\pi ij\log(\lambda u)/L}.
\]
\(E_N=\operatorname{span}\{V_j:|j|\le N\}\)。
有限行列 \(Q_{\lambda,N}\) は **actual Weil form のこの部分空間への制限**。
prime-power項は \(p^k\le\lambda^2\) に限られるが、Gamma・極項も初めから含む。
\(N\) は素数の個数ではなく Fourier/Galerkin 次数である。

\(\epsilon_{\lambda,N}=\min\operatorname{Spec}Q_{\lambda,N}\) とする。
必要条件 ES は、この固有値が単純で固有vector \(v_{\lambda,N}\) が
\(u\mapsto1/u\) に関して偶であること。
\[
 T_{\lambda,N}=Q_{\lambda,N}-\epsilon_{\lambda,N}I\ge0,\qquad
 \ker T_{\lambda,N}=\mathbb C v_{\lambda,N}.
\]
この正値性は有限行列の最小固有値を引いた結果であって、
\(Q_{\lambda,N}\ge0\) やRHの証明ではない。

Dirichlet vector \(\delta_N=L^{-1/2}\sum_{|j|\le N}V_j\) に対して
\(\delta_N(v)=1\) と規格化できることは、ES と特殊なrank-two commutatorから証明される。
\[
 D_{\lambda,N}=D_\lambda-|D_\lambda v\rangle\langle\delta_N|.
\]
自己共役性を主張する空間は元の全 \(L^2\) そのものではなく
\[
 (E_N/\mathbb Cv,\langle T_{\lambda,N}\,\cdot,\cdot\rangle)
       \oplus E_N^\perp
\]
である。有限商上の正内積と、未変更の無限 Dirac tail の直和。
したがって「有限prime operator」は有限次元行列だけでもない。

Theorem 5.10 の帰結（ES を仮定）：
\[
 d_{\lambda,N}(z):=\det_{\rm reg}(D_{\lambda,N}-z)
   =-i e^{-iz\log\lambda}\widehat v_{\lambda,N}(z),\qquad
 \widehat v(z)=\int_{I_\lambda}v(u)u^{-iz}\frac{du}{u}.
\tag{D}
\]
\(\widehat v\) は整関数で全零点が実数。有限商の特性多項式と
未変更tailのdeterminantの積による証明なので、零点の重複度も含む。
正則化の spectral cut は \((-1)^{-w}=e^{-i\pi w}\)。
phase因子を省略して raw determinant を直接 \(\mathscr X\) と比較してはいけない。

ES を全 \((\lambda,N)\) について無条件に証明した定理は、ここでは得ていない。
本文 §8 は連続窓 \(QW_\lambda\) の単純・偶最小固有関数も未解決とする。
finite-stage real-zero theorem は **条件付き定理として既知**、
すべての算術的入力について前提まで検証済みという主張は不可。

## 3. 安全な正規化

ES が成立する段階では \(\widehat v(z_*)\ne0\)。非実点であることだけを使う。
\(\widehat v(0)\ne0\) は偶性だけでは保証されないので、原点規格化を避ける。
\[
 F_{\lambda,N}(z)=\mathscr X(z_*)\,
 e^{i(z-z_*)\log\lambda}
 \frac{d_{\lambda,N}(z)}{d_{\lambda,N}(z_*)}
 =\mathscr X(z_*)\frac{\widehat v_{\lambda,N}(z)}
                         {\widehat v_{\lambda,N}(z_*)}.
\tag{N}
\]
これは整、実零点、偶、\(F_{\lambda,N}(z_*)=\mathscr X(z_*)\ne0\)。
定数一つ \(c_{\lambda,N}\) だけで raw determinant を補正するのは不十分で、
上の明示的な非消失phase因子も必要。

## 4. 収束することが既知の別の族

CCM (7.1)–(7.8) は
\[
 h(x)=\frac{\pi}{2}x^2(2\pi x^2-3)e^{-\pi x^2},\quad
 \mathcal E h(u)=u^{1/2}\sum_{m\ge1}h(mu)=k(u)
\]
と、prolate の \(h_{0,\lambda},h_{4,\lambda}\) の積分0の組合せ \(h_\lambda\)
（\([-\lambda,\lambda]\) 外は0）から
\[
 k_\lambda(u)=1_{I_\lambda}(u)\mathcal E h_\lambda(u)
\]
を構成する。Lemma 7.2 は適切なスカラー規格化で
\[
 \sup_{|x|\le\lambda}|h_\lambda(x)-h(x)|\le C\lambda^{-2}.
\tag{P}
\]
根拠は Meixner–Schäfke の固定次数 \(n=0,4\) の prolate/Hermite 漸近。
prolate Fourier concentration eigenvalue の \(1-\chi_n(\lambda)\) にも
指数的に小さい既知漸近がある。しかし \(\chi_n\) は Weil ground-state gap ではない。

### スカラーを再計算した結果

印刷された \(h,\mathcal E,\xi\) と \(d^*u=du/u\) を同時に採用すると、
\[
 \int_0^\infty h(x)x^{s-1}dx
  =\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2),
\quad
 \widehat k(z)=\frac14\xi(1/2-iz)=\frac14\mathscr X(z).
\tag{SC}
\]
初め \(\Re s>1\) で和・積分を交換し、以後は解析接続。
これは「\(\widehat k=\mathscr X\)」という印刷上の記述との定数差であり、
零点や収束戦略を損なわない。\(4h\) を使うか、下記の値規格化で完全に解消する。
HTMLとPDFの式を照合し、二担当が独立にGamma積分を検算した。

### Lemma 7.3 の収束評価を使用する際の補足

\(u\in I_\lambda\) では、有限和側にある項数は高々 \(\lambda/u\)。
ただし \(k\) 側には \(mu>\lambda\) のGaussian tailがあるので、正確には
\[
 |k_\lambda(u)-k(u)|
 \le C\lambda^{-1}u^{-1/2}
      +u^{1/2}\sum_{mu>\lambda}|h(mu)|.
\tag{T}
\]
後半を捨てた厳密不等式は使用しない。
\(\lambda\ge2\) で \(|h(x)|\le Cx^4e^{-\pi x^2}\) と積分比較により
後半のweighted Mellin積分は polynomial(\(\lambda\))\(e^{-\pi\lambda^2}\)。
また \(h\) は自己Fourier、\(h(0)=\int h=0\) なので Poisson により \(k(u)=k(1/u)\)。
窓外の \(k\) の積分も同様に小さい。
従って任意 \(0<r<1/2\) に対して
\[
 \sup_{|\Im z|\le r}
 |\widehat k_\lambda(z)-\mathscr X(z)/4|
 \le C_r\lambda^{-1/2+r}
       +C_r\lambda^{C_r}e^{-\pi\lambda^2}.
\tag{K}
\]
これは実部全体についての評価なので compact 収束より強い。
紙面の \(O(\lambda^{-1/2-\alpha})\) は
\(\alpha=\Re s=\Im z\) の片側評価。左右をまとめると (K)。
端点 \(r=1/2\) での収束をこの評価から主張しない。

\[
 G_\lambda(z)=\mathscr X(z_*)\frac{\widehat k_\lambda(z)}
                                      {\widehat k_\lambda(z_*)}
\tag{G}
\]
は十分大きい \(\lambda\) で定義でき、\(\Omega\) のcompact上
\(G_\lambda\to\mathscr X\)。
**この \(G_\lambda\) に全実零点を保証する定理は得られていない。**

## 5. THE EXACT BREAK を式にする

次の命題 G* は証明していない。未証明仮定として採用もしない。
既知成果が必要としている橋を、算術から既に定義された二つの族で指定しただけ。

**G*（正規化した真のground stateとprolate proxyの比較命題）**
ES が成立する \((\lambda_j,N_j)\)、\(\lambda_j\to\infty\) があり、
任意compact \(K\Subset\Omega\) について
\[
 \sup_{z\in K}
 \left|
 \frac{\widehat v_{\lambda_j,N_j}(z)}
      {\widehat v_{\lambda_j,N_j}(z_*)}
 -
 \frac{\widehat k_{\lambda_j}(z)}
      {\widehat k_{\lambda_j}(z_*)}
 \right|\longrightarrow0.
\tag{G*}
\]
ここで ES のcofinalな成立も命題の一部であり、既知扱いしない。
(K)+(G*) は \(F_{\lambda_j,N_j}\to\mathscr X\) を与える。
Hurwitz/Rouché の証明は [theorem stack](../../local_global_theorem_stack.md)。
逆にRHだけからこの特定の算術的ground stateの比較が従うとは分かっていない。
「新しいRH同値定理を証明した」という結論ではない。

一つの具体的な十分評価は
\[
 b_j=\widehat k_{\lambda_j}(z_*)/\widehat v_{\lambda_j,N_j}(z_*),
\quad
 \int_{I_{\lambda_j}}|b_jv_{\lambda_j,N_j}(u)-k_{\lambda_j}(u)|
        \max(u^r,u^{-r})\,\frac{du}{u}=o(1)
\tag{W_r}
\]
for every \(0<r<1/2\)。固定窓の無重み \(L^2\) 収束だけをこの評価と混同しない。

## 6. gap・残差・正規化を分ける

一般的な Rayleigh 原理では、単位trial \(w\)、単位ground \(v\)、
gap \(\Delta=e_1-e_0>0\) に対し
\[
 1-|\langle v,w\rangle|^2
 \le \frac{\langle Aw,w\rangle-e_0}{\Delta}.
\]
小さな Rayleigh 値それ自体では不足し、groundとの差とgapとの比が必要。
\(\Delta\ge c>0\) の一様下界は必要条件ではない。比が十分速く0へ行けばよい。
さらに \((W_r)\) へ移すと、
\[
 \|e^{r|t|}e(t)\|_{L^1(-\log\lambda,\log\lambda)}
 \le C_r\lambda^r\|e\|_2\quad(r>0)
\]
という窓依存損失と、\(\widehat v(z_*)\) の規格化のconditioningを払う。
原典の prolate concentration estimate は、この **Weil operator** の
Rayleigh差/gap/規格化比を一様に評価していない。

固定 \(\lambda\) の compact resolvent、trigonometric core、孤立単純groundが
確認できるなら通常のGalerkin収束は使えるが、\(\lambda\to\infty\) の一様推論ではない。
境界値 \(v(\lambda)=1\) の規格化には、単なる \(L^2\) 収束を超える制御が要る。
本稿の \(z_*\) 規格化はこの境界評価の問題を避けるが、(G*) 自体は解かない。

## 7. 必須の two-parameter 条件と UV

(D) の未変更tailは
\[
 \{\pi j/\log\lambda:|j|>N\}.
\]
従って非零compact一様極限を得る列には必ず
\[
 N_j/\log\lambda_j\longrightarrow\infty
\tag{UV}
\]
が必要。比が有界な部分列ではtail零点がある実区間に稠密となり、
極限がその区間で0、identity theoremにより恒等0になる。
これは二担当で検算した必要条件であって、十分条件ではない。
固定 \(N\) の高精度低零点一致を \(\lambda\to\infty\) の証明に転用できない。

最も簡単には actual \(N=0\) 制限の固有vectorは定数で、ES は自動。
\(a=\log\lambda\) とすると、値1に規格化した Fourier transform は
\[
 \frac{\sin(az)/z}{4\sinh(a/4)}.
\]
これは各段階で全実零点を持ち \(z_*=i/4\) で1。
しかし \(\lambda\to\infty\) で実軸上は全点で0へ行き、
\(z_*\) では1のまま。従って strip の正則な非零極限にはならない。
「finite real zeros＋一点規格化」だけで normal family が得られるという主張への
実際の低次数構成内の反例であり、RHや正しい同時極限への反例ではない。

各固定 \(\lambda,N\) のtail countingは線形成長であり、
Riemann–von Mangoldt の \(T\log T\) と全高さで一致しない。
UV prolate模型で漸近countingが合うことも、上の有限商の全零点同定にはならない。
任意固定compactへの収束が全て成立すればRHには十分なので、
不要に単一のgrowing-window rateを要求する必要はない。

## 8. 結論と再開条件

新しく監査できた実質的外部入力は (P)、(K)、正確なdeterminant公式 (D)、
条件付き実零点定理。単なる「収束すればRH」の言い換え以上に、
**比較対象・正規化・必要な窓依存精度**を指定できた。
ただし (D) の定理と §8 の二義務は旧 accumulation_spectrum.md §4 で既に採用済み。
今回未使用入力として数えるのは、明示的に追跡した (P)、(K) のproxy estimateであり、
既知gap自体を新しく発見したとは主張しない。
しかし実零点を保証する族について (G*) の評価は見つからない。
現在の限定監査はここで止める。第四の候補、未知の正値性の仮定、
主proof graphへのmergeは行わない。
再開の入口は actual Weil ground の ES と (G*) へ届く
独立な残差/gap/weighted-comparison estimate に限定する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/local_global_theorem_stack.md`](../../local_global_theorem_stack.md)
