**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global/notes/convergence_destroyer.md` · Original SHA-256: `3d769fe51fe15ca748d936731b08495aa01ad4e6330b523c1c13ed8a0f00c017`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Local-to-global convergence: independent adversarial audit

2026-09-30。限定 Track C。RH OPEN。以下の一般反例は ζ の反例ではない。
新規性は主張しない。既存ファイル・主 proof graph は変更しない。

## C1. 実際に十分な解析条件

\[
\mathscr X(z)=\xi(1/2+iz),\qquad
S=\{z:|\Im z|<1/2\},\qquad z_*=i/4.
\]
\(\mathscr X(z_*)=\xi(1/4)>0\) で、\(\mathscr X\) の全零点は無条件に
\(S\) 内にある。したがって全平面での近似を要求する必要はない。

**十分条件。** \(F_j\) は \(S\) で正則、非実零点を持たず、
\(F_j\to\mathscr X\) が \(S\) の複素 compact 上一様なら RH。
証明は \(S\cap\{\Im z>0\}\) と下半分に Hurwitz を適用するだけである。
極限が恒等0でないことは既知の \(\mathscr X(z_*)\ne0\) による。
列全体でなく部分列で十分。各 compact が最終的に正則な定義域に含まれる設定でもよい。

より局所的には、仮の非実零点を囲む閉円板 \(D\Subset S\setminus\mathbb R\)
で、\(\mathscr X\ne0\) on \(\partial D\)、かつある十分大きな段階で
\[
 |F_j-\mathscr X|<|\mathscr X|\quad\hbox{on }\partial D
\]
があれば Rouché により矛盾する。零点の重複度も数える。
これを全ての仮の非実零点に使えることが必要で、有限個の円板の数値検査では足りない。
「最弱の収束位相」を一意に定義したのではなく、証明に必要な局所条件を指定した。

Vitali を使う別の十分条件は、複素領域での局所有界性と、内部に集積点を持つ集合上の
点収束である。実軸上の一致だけから複素局所有界性を省略しない。
Fourier 表現 \(F_j(z)=\int f_j(t)e^{izt}dt\) があるときは、例えば
\[
 \int_{\mathbb R}|f_j(t)-f(t)|e^{r|t|}dt\longrightarrow0
 \quad(0<r<1/2)
\tag{C1}
\]
が閉部分帯全体での一様収束を与える。これは actual kernel に対して証明すべき評価である。

## C2. 正規化・実軸のみ・逃走の区別

各段階が非零でも \(F_j(z)=j^{-1}\cos z\to0\) は起こる。
Hurwitz の恒等0の例外を除くには、既知の非零値での正規化などが要る。
一方 \(1-z^2/j^2\to1\) は零点が無限遠へ逃げる例であり、Hurwitz と矛盾しない。

実軸上だけの局所一様収束については、実偶多項式 \(p_j\) を
\[
 \sup_{|x|\le j}|p_j(x)-\log(1+x^2)|\le1/j
\]
となるよう Weierstrass 近似と偶対称化で選ぶ。
\(f_j(z)=\exp(p_j(z)-p_j(0))\) は実偶・整・零点なし・\(f_j(0)=1\) だが、
実軸上で局所一様に \(1+x^2\) へ収束する。その解析接続は \(\pm i\) に零点を持つ。
従って複素領域の正規族条件は本質的である。
この例は次数・増大度の一様制御を持たない。実零点多項式の特殊な閉包定理を否定していない。

さらに
\[
 (1-z^2/j^2)^{j^2}\longrightarrow e^{-z^2}
\tag{C2}
\]
は全零点が逃げても、その累積が非消失因子を残す例である。
各近似の order が0でも極限の order は2になる。
各段階で order \(\le1\) という情報だけは一様な増大度評価ではない。

## C3. 偶 canonical product の必要な tail 管理

零点0を別処理し、正の実零点を重複度込みで \(\gamma_{j,k}\) とする。
正規化された偶 order \(\le1\) 関数について paired product
\(\prod_k(1-z^2/\gamma_{j,k}^2)\) を比較するなら、有限 head の収束のほかに
\[
 \lim_{R\to\infty}\sup_j
 \sum_{\gamma_{j,k}>R}\gamma_{j,k}^{-2}=0
\tag{C3}
\]
は便利な十分 tail 条件である。\(|z|\le r,\ R\ge2r\) なら解析的対数の枝を0で固定して
\[
 \left|\sum_{\gamma_{j,k}>R}\log(1-z^2/\gamma_{j,k}^2)\right|
 \le 2r^2\sum_{\gamma_{j,k}>R}\gamma_{j,k}^{-2}.
\]
一様な counting bound \(N_j(T)\le C T\log(T+2)\) があれば部分積分で右辺 tail は
\(O_r(\log(R+2)/R)\)。actual \(\mathscr X\) の counting bound だけを近似族へ流用しない。

全零点を重複度付きで target に対応させる入力は別に必要である。
主要 counting 漸近や低零点の一致は、有限個の余分な非実 quartet を検出しない。
例えば \(\cos z\) に
\[
 P(z)=\frac{((z-1)^2+1/16)((z+1)^2+1/16)}{(17/16)^2}
\]
を掛けると、実偶 order1 と主要 counting は保たれ、非実 quartet が4個追加される。
これは actual Euler/Gamma を保った模型ではない。counting だけを使う推論への検査である。

## C4. Resolvent と determinant は同じ収束問題ではない

まず共通 Hilbert 空間、または指定した unitary identification が必要である。
段階ごとに違う内積で自己共役というだけでは、共通の resolvent 収束を定義していない。

強 resolvent のみでは、\(A_j=I-|e_j\rangle\langle e_j|\) on \(\ell^2\) が反例になる。
\(A_j\to I\) strongly だが、\(0\in\operatorname{Spec}A_j\) は全段階に存在して極限にはない。
固有vector が弱く0へ逃げる。norm-resolvent 収束について同じ反例を主張しない。
norm-resolvent は通常の共通空間の仮定下で、孤立有限重複度固有値の射影・重複度を制御する。

**しかし norm-resolvent でも determinant tail は別入力である。**
\(Ae_k=ke_k\) とし、\(A_j\) は \(j<k\le j+j^2\) の固有値だけを \(j\) に変更する。
全作用素は自己共役、compact resolvent、定義域は \(\operatorname{Dom}A\)。
\[
 \|(A_j-i)^{-1}-(A-i)^{-1}\|\le2/j\longrightarrow0.
\]
各 \(A_j^{-2}\) は trace class で
\[
 \begin{split}
 D(z)&=\det(I-z^2A^{-2})=\frac{\sin\pi z}{\pi z},\\
 D_j(z)&=D(z)\,
 \frac{(1-z^2/j^2)^{j^2}}
 {\prod_{k=j+1}^{j+j^2}(1-z^2/k^2)}
 \longrightarrow e^{-z^2}D(z).
 \end{split}
\tag{C4}
\]
商の表示は可除点を延長して整関数として読む。
分母は compact 上1へ収束する。全固定低固有値は最終的に一致し、\(D_j(0)=D(0)=1\)。
それでも target determinant とは一致しない。
実際 \(\|A_j^{-2}-A^{-2}\|_1=1-O(1/j)\) で trace norm 収束はない。
この例は非実零点を作らない。非消失因子・正規化の誤同定だけを反証する。

正の結果も区別する。trace-class holomorphic family \(K_j(z)\) が
compact 上 trace norm で \(K(z)\) に収束すれば Fredholm determinant も収束する。
[Bornemann, §4 (4.1), §5](https://arxiv.org/pdf/0804.2543) の標準評価は
\[
 |\det(I+A)-\det(I+B)|
 \le\|A-B\|_1\exp(1+\max(\|A\|_1,\|B\|_1)).
\]
固定 trace-class \(K\) の増大 Galerkin 射影はこの十分条件を満たす。
移動する \(K_j\)、Schatten 正則化 determinant、zeta-regularized determinant に
無条件で同じ推論を移さない。とくに actual spectral determinant と \(\mathscr X\) の
正確な同定がなお必要。ここでは同論文の訂正対象 Lemma4.1 の強い特殊評価は使わない。

## C5. Actual CCM 族の規格化と二変数経路

一次資料：[Connes–Consani–Moscovici, arXiv:2511.22755v1,
Theorem5.10 と §§7–8](https://arxiv.org/html/2511.22755v1)。
有限 head の最小固有値が単純で ground vector が偶である条件を ES と呼ぶ。
定理の作用素は有限商と未変更の無限 tail の直和であり、普通の有限行列だけではない。
その exact identity を使うと
\[
 \Delta_{\lambda,N}(z)=-i e^{-iz\log\lambda}\widehat v_{\lambda,N}(z),
\quad
 e^{i(z-z_*)\log\lambda}
 \frac{\Delta_{\lambda,N}(z)}{\Delta_{\lambda,N}(z_*)}
 =\frac{\widehat v_{\lambda,N}(z)}{\widehat v_{\lambda,N}(z_*)}.
\tag{C5}
\]
ES のもとでは全零点が実数なので分母は非零。
\(z_*=0\) での非消失は偶性・単純 ground だけから保証されない。
\(z_*=i/4\) は target strip 内でもあり安全。
定数倍だけでなく表示した非消失 phase 因子を補正する。

印刷された
\(h(x)=\frac\pi2x^2(2\pi x^2-3)e^{-\pi x^2}\) に対して独立に積分すると
\[
 \int_0^\infty h(x)x^{s-1}dx
 =\frac{s(s-1)}8\pi^{-s/2}\Gamma(s/2).
\]
従って \(\mathcal Eh(u)=\sqrt u\sum_{m\ge1}h(mu)\) の変換は
\(\widehat k(z)=\xi(1/2-iz)/4=\mathscr X(z)/4\)。
これは scalar の修正であり、値規格化で消える。戦略全体の反証にはしない。
Lemma7.3 の表示評価には \(mu>\lambda\) の Gaussian tail を加える必要があるが、
root note の exponentially small tail 補足は整合する。

**独立検算した必要経路条件。** \(a_j=\log\lambda_j\to\infty\) とする。
Lemma5.9 の sine 表示、または未変更 tail より
\(\pi k/a_j\), \(|k|>N_j\) は全て \(\widehat v_{\lambda_j,N_j}\) の零点。
非消失因子で補正しても零点は残る。もし \(N_j/a_j\le C\) の部分列があれば、
任意の \(x>\pi C\) に対して \(k_j\sim xa_j/\pi>N_j\)、
\(\pi k_j/a_j\to x\)。compact 一様極限 \(F\) は \(F(x)=0\) となる。
恒等定理により \(F\equiv0\)。ゆえに非零極限には
\[
 N_j/\log\lambda_j\longrightarrow\infty
\tag{C6}
\]
が必要。十分条件ではない。固定 \(N\) の精密な有限表はこの必要条件を代替しない。

root 提案の **actual \(N=0\) 検査** も独立 PASS：1次元 Weil 制限の ground は定数で ES。
\(a=\log\lambda\) として値規格化した transform は
\[
 f_a(z)=\frac{\sin(az)/z}{4\sinh(a/4)}.
\tag{C7}
\]
全零点は実数、\(f_a(i/4)=1\)。しかし任意の固定実 \(x\) で \(f_a(x)\to0\)
（\(x=0\) は分子を \(a\) と延長）、一方 \(f_a(2i/5)\to+\infty\)。
従ってこの経路は \(S\) 内で局所有界でない。
actual 有限族でも「偶・実零点・非実1点の値固定」だけでは正規族にならない。
これは許容される cofinal 経路全般を反証しない。

## C6. 残る actual gate と root note の読取判定

現在の具体的十分命題は、ES を満たす cofinal な \((\lambda_j,N_j)\) が存在し、
正規化した真の ground transform と prolate proxy transform の差が
\(S\) の各 compact 上0へ行くことである。既知の proxy 収束と C1 がその後を閉じる。
ES の存在とこの比較評価を別々の義務として残す。
RH からその特定の ground-state 比較が逆に従うとは証明していない。
論文 §8 も二つの未証明入力を明記する。

`spectral_approximants_and_exact_gap.md` §§1–8 を読取監査した。
phase、\(1/4\)、\(z_*\)、weighted Mellin tail、残差/gap 比、(C6) の区分は PASS。
\(\|e^{r|t|}e\|_1\le C_r\lambda^r\|e\|_2\) は \(r>0\) で正しい。
\(r=0\) なら \(\sqrt{2\log\lambda}\) を別に持つので、その端点へ同じ定数を流用しない。
一様な正の spectral gap は必要条件ではなく、残差/gap と窓依存損失の総合評価が必要。

追加文献 [Śliwiński, arXiv:2601.12133v1,
Definition2.4 / Theorem3.1](https://arxiv.org/html/2601.12133v1) は convergence 入力として採用不可。
CCM の有限商＋無限 tail を普通の \(2N+1\) 次元 compression と同定している。
有限行列で \([X,D]=iI\) は trace を取るだけで不可能。
周期微分作用素でも位置の乗算が周期定義域を保たない。
さらに状態内分散の下界から、別に指定した ζ 零点との平均距離の下界は出ない。
これらは表示された証明の切断点であり、その数値表や全ての将来の error bound の否定ではない。

## C7. Stability / Lee–Yang は exact dictionary がある場合のみ

[Borcea–Brändén I, Theorems1.1–1.2](https://arxiv.org/pdf/0809.0401) は
多項式の stability を保つ線形写像を、その symbol 等で判定する。
使用には actual な \(T_j\)、stable seed、該当 symbol の安定性、target への収束が必要。
「素数ごとの操作」という呼称だけはこれらの代わりにならない。

[Borcea–Brändén II, §8 Theorem8.1](https://arxiv.org/pdf/0809.3087) の
ferromagnetic Ising 型 Lee–Yang 条件も、正の coupling と外場の対応が前提。
actual \(\mathscr X\) への変数回転・スカラー・有限体積 partition function・複素極限を
全て同定して初めて C1 と接続する。ここではその辞書を構成していない。
局所 positivity、実軸データ、counting、自己共役性を一つにまとめて
「全零点を保持する極限がある」と読み替えない。

**判定。** Hurwitz 側は完成した一般原理。actual ES と正規化 ground/proxy 比較は未解決。
必要経路 (C6) と actual 固定head検査 (C7) は確認済みだが、独立な収束評価を供給しない。
