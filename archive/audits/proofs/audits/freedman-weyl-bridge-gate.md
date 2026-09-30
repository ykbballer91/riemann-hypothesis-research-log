**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/freedman-weyl-bridge-gate.md` · Original SHA-256: `7261304b2d1f61d099afe4722ac74d22f33d9491f77999637344a3aefe556204`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Freedman v1 — Fourier接続と収縮性の gate

2026-09-29。候補分類 ENABLING。**全域正値性の入力として不採用。RH未証明。**
原著はRH完全証明を主張していない。以下は Eq.(6), Appendix C–C.1 の限定監査で、
102頁全体または内部数値certificateの独立検証ではない。

一次資料: [Freedman, arXiv:2606.29555v1](https://arxiv.org/html/2606.29555v1)。
固定HTML: `literature/source_cache/freedman-2606.29555v1.html`。
SHA256 `90697240319ea6149c7723baabc9a5b5c5ee2332e8f68c8b6397df1d71ff68c3`。
本文Theorem 2.2・§16・Appendix Aは元の核への移行を未完とし、
Appendix C後半は収縮性・移行・全パラメータ範囲を閉じたとしている。両記述を混同しない。
後者の収縮性は PROVED-IN-PAPER=YES-ARGUMENT-PRESENT、
INDEPENDENTLY-VERIFIED=NO-PROOF-CRITICAL-GAP。

## 独立に確認した接続恒等式

実偶関数 \(\Phi\) は任意の指数より速く減衰するとし、
\(F(z)=\int_{\mathbb R}\Phi(t)e^{izt}dt\)、\(E_\nu(z)=F(z+i\nu)\) と置く。
原著 Eq.(6) の核は
\[
K_\nu(a,b)=\frac12\int_{|(a+b)/2|}^{\infty}
y\cosh(2\nu y)\Phi(y+(a-b)/2)\Phi(y-(a-b)/2)\,dy.
\]
de Branges型核は、正値性を仮定せず代数的に
\[
\mathcal B_\nu(w,z)=
\frac{E_\nu(z)\overline{E_\nu(w)}-E_\nu^\#(z)\overline{E_\nu^\#(w)}}
 {2\pi i(\bar w-z)}
\]
と定義する。\(\mathcal D_L(w,z)=\iint e^{iza-i\bar w b}L(a,b)\,da\,db\) とすると
\[
\boxed{\mathcal D_{K_\nu}=\frac\pi4\partial_\nu\mathcal B_\nu},\qquad
\boxed{\mathcal B_\omega=\frac4\pi\int_0^\omega\mathcal D_{K_\nu}\,d\nu}.
\tag{F}
\]
これは零点配置を使わない。単位的Fourier規約なら第一式の係数は \(1/8\)。

導出: \(H_\nu\) を上の核の \(y\cosh(2\nu y)\) を \(\sinh(2\nu y)\) に置換したものとする。
\(q=z-\bar w,p=z+\bar w\) と置き
\[
I=\int_{\mathbb R}\int_0^\infty \sinh(2\nu y)\sin(qy)e^{ipu}
\Phi(y+u)\Phi(y-u)\,dy\,du.
\]
\(a=x+u,b=x-u\) のJacobianは2なので \(\mathcal D_H=2I/q\)。
一方 \(t=y+u,s=y-u\) と実偶性から \(\mathcal B\) の分子は \(-8iI\)、
分母は \(-2\pi iq\)。よって \(\mathcal D_H=(\pi/2)\mathcal B\)。
\(\partial_\nu H=2K_\nu\)、\(\mathcal B_0=0\) から(F)を得る。\(q=0\) は可除極限。

超指数減衰は複素 \(z,w,\nu\) のコンパクト集合上で積分・微分の絶対一様収束を与える。
特に \(y\ge|x|\) で \(\max(|y+u|,|y-u|)=y+|u|\) を使える。
核がPSDなら、切断した指数関数で二次形式を評価してから支配収束を使うことで
\(\mathcal D_K\) もPSD。従って全 \(0\le\nu\le\omega\) の元の核のPSDは
\(\mathcal B_\omega\) のPSDを含意する。未同定の商形式のPSDではこの前件を満たさない。
単一の \(\omega\) に対するPSDを、その区間全体へ拡張する主張でもない。

ROOT/BUILDERが別々に導出し、DESTROYERも係数・共役・可除点を確認。
Gaussian \(\Phi(t)=e^{-t^2}\) を用い、80桁mpmathで独立な一変数積分と
\(F(z)=\sqrt\pi e^{-z^2/4}\) の \(\nu\) 微分を比較した。
\((z,w,\nu)=(.3+.4i,-.7+.6i,.2),( .4i,.4i,.49)\) の絶対誤差は
\(5.28\cdot10^{-82},1.06\cdot10^{-81}\) 未満。非認証sanity checkであり証明根拠は上の解析。

## 中心の正値性は既にRH同値

\(F=\Xi\)（正の定数倍を含む）では(F)の \(\nu=0\) は
\[
\mathcal D_{K_0}(w,z)=
\frac{F(z)F'(\bar w)-F'(z)F(\bar w)}{4(z-\bar w)}.
\tag{P}
\]
\(m=-F'/F\) と書けばこれは \(F(z)\overline{F(w)}/4\) を掛けたPick核。
もし上半平面に次数 \(r\ge1\) の零点 \(z_0\) があれば、
\(z=z_0-i\varepsilon\) で \(F'/F=ir/\varepsilon+O(1)\) となり、
\[
\mathcal D_{K_0}(z,z)=\frac{|F(z)|^2}{4\Im z}\Im m(z)<0
\]
を与える。従って \(K_0\) のPSDは、多重零点を含めてRHを強制する。

逆にRHの下では、order1のHadamard積から
\[
\mathcal D_{K_0}(w,z)=\frac14\sum_{r\in Z(F)}m_r
\frac{F(z)}{z-r}\overline{\frac{F(w)}{w-r}}
\]
というPSD Gram和を得る。和は相異なる実零点を取り、重複度は \(m_r\)。
可除点では延長し、tailは \(\sum m_r/(1+r^2)<\infty\) で局所一様に収束する。
実軸でのFourier逆変換はSchwartz試験関数の正値性を保ち、連続核への集中試験で
\(K_0\) のPSDへ戻る。したがって中心核の全域PSDはRH同値であり、弱い入力ではない。
\(\nu_j\downarrow0\) の列だけでも全核PSDを仮定すれば、連続性と有限Gram正錐の閉性により同じ結論。

注意: 一般の \(\mathcal B_\omega\) のPSDだけから厳密なHermite–Biehler条件を結論してはならない。
\(E,E^\#\) の共通非実因子は核のPSDと両立する。(P)の対角符号論法はその問題を回避している。
例えば固定 \(\omega>0\) と \(F(z)=(z^2+\omega^2)(z^2+9\omega^2)\) では、
\(E_\omega(z)=G(z)(z+4i\omega)\), \(G(z)=z(z^2+4\omega^2)\) だから
\(\mathcal B_\omega=(4\omega/\pi)G(z)\overline{G(w)}\) はPSDだが、共通零点 \(2i\omega\) がある。
この反例は多項式であり、Riemann核への反例ではない。

対角の条件 \(4\mathcal D_{K_0}(z,z)\ge0\) は、
[Csordas–Escassut (2005), Theorem2.3, Eq.(2.4), p.334](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf)
の複素Laguerre基準 \(y^{-1}\Im\{-F'(z)\overline{F(z)}\}\ge0\) に正確に一致する。
同定理のstrip/growthクラスはRiemann \(\Xi\) を含む。一次PDF本文と画像を照合済み。
近接する既知研究には [Suzuki 1204.1827v2, Proposition1.2](https://arxiv.org/html/1204.1827v2)、
[Sondow–Dumitrescu, Theorem1/Corollary1](https://arxiv.org/pdf/1005.1104)、
[Csordas 1309.0055v2, Theorems3.7/4.6](https://arxiv.org/html/1309.0055v2) もある。
inner/Hermite–Biehler・単調性・theta積核による既知の零点基準と区別する。
(F)の完全一致する先行掲載は限定検索で未確認だが、標準積分の帰結なので新規性を主張しない。

## Appendix C の最小cut: 定常性は収縮性を与えない

原文は完備化後の \(Q(f_x,h)=0\)（\(h\in\ker R\)）と
\(|\kappa(s,u)|\le1\) から \(\|CKE\|\le1\) を結論している。
しかし持ち上げ \(E\) のノルム制御は導出されていない。

以下は、この一般推論への厳密反例。\(f=(x,n)\in\mathbb R^2\) に対して
\[
Uf=(x,-x/2,n),\quad C(v_1,v_2,v_3)=((v_1+v_2)/\sqrt2,v_3),
\quad K=\operatorname{diag}(1/2,-1/2,0).
\]
\(G_+=CU,G_-=CKU,Rf=x\) とすると
\[
G_+f=(x/(2\sqrt2),n),\quad G_-f=(3x/(4\sqrt2),0),\quad
Q(f)=\|G_+f\|^2-\|G_-f\|^2=n^2-5x^2/32.
\]
\(Q\) は \(\ker R\) 上で正、各fiberの唯一の最小化元は \(f_x=(x,0)\)、
\(Q(f_x,h)=0\) も成立する。有限次元なので完備化・連続性・稠密性に問題はない。
それでも \(\|C\|=1,\|K\|=1/2\) に対し、Green plus imageでの右逆
\(E(g,0)=(2\sqrt2g,-\sqrt2g,0)\) は
\[
CE=I,\quad \|E\|=\sqrt{10},\quad CKE(g,0)=(3g/2,0),\quad
\boxed{\|CKE\|=3/2>1}.
\]
対角値は実際の形 \(\kappa=(1-r)/(1+r)\) の \(r=1/3,3,1\) に対応する。
ROOT/BUILDER独立確認、\(-5/32\) と \(9/4\) は有理数演算でも照合。
actual \(\Phi\) の負方向を得たとはしない。

未供給の入力は、actual Green lift \(Lf_x\) に対する
\(\|C M_\kappa Lf_x\|^2\le\|CLf_x\|^2\) を強制する独立な算術評価。
これを単に仮定すると、まさに残っていた \(M\le P\) の再命名になる。
結論: 接続の恒等式は確認したが、正値性のcritical gapは未修復。
中心核のPSDを弱い仮定として採用するルートは終了。finite certificateの拡大は行わない。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/freedman-2606.29555v1.html` — SOURCE REFERENCE NOT INCLUDED
