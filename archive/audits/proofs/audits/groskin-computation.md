**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/groskin-computation.md` · Original SHA-256: `4be1c1e3d47e244bc9ee8c56b2e548d545c7086814a9f443c2acd622cb626969`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Groskin有限系の独立区間演算 — 2026-09-29

判定: **c=13, N=4 の指定された9次正方行列について正定値を認証**。
RHはOPEN。全c,Nの正値性、全零点の実性、原論文の401次計算は認証していない。
本文の規約問題は [辞書監査](groskin-dictionary.md)、tailの解析条件は
[tail監査](groskin-tail.md)、取得物の版固定は
[取得監査](../../../literature/literature/notes/groskin-certificate-audit.md) に分離する。

## 何を独立に計算したか

L=log c, w_n=2πn/L, r(x)=e^(−x/2)/(1−e^(−2x)) として、

\[
S_n=\int_0^L r(x)\sin(w_nx)dx,\quad
C_n=\int_0^L r(x)(\cos(w_nx)-1)dx,\quad
X_n=\int_0^L xr(x)\cos(w_nx)dx.
\]

原著者の特殊関数・幾何級数実装をimportせず、上記3積分をArbの認証求積で計算した。
原点の可除特異点は sinc を使い、

\[
b(z)=\frac{e^{z/2}}{2\operatorname{sinc}(iz)}=zr(z),
\]

被積分関数をそれぞれ $w_nb(z)\operatorname{sinc}(w_nz)$、
$-w_n^2zb(z)\operatorname{sinc}(w_nz/2)^2/2$、$b(z)\cos(w_nz)$ とする。
これらはmeromorphicであり、極を含むballのdivisionは非有限値を返す。
したがって複素求積のanalytic flagを無条件に無視してよい種類の関数である。
sinc(0)=1はライブラリが可除特異点として扱う。
[python-flint公式仕様](https://python-flint.readthedocs.io/en/latest/acb.html#acb.integral)
に従う。求積許容値に達したことを仮定せず、返却された有限ball自体を使う。

a=e^(−L/2)として

\[
K=\log\pi-\psi(1/4)-2\operatorname{atanh}(a)-2\arctan(a).
\]

これは $\int_L^\infty r(x)dx=\operatorname{atanh}(a)+\arctan(a)$ と
[digamma積分表示](https://dlmf.nist.gov/5.9#E16) から得る。
原著コードの kappa(L)+J(L) と等しい。例えば
$\psi(1/4)=-\gamma-\pi/2-3\log2$、U=1/aを代入し、
atan(U)+atan(a)=π/2 と実対数の加法則で確認できる。

arch行列は

\[
A_{nn}=-K-2C_n+2X_n/L,\qquad
A_{mn}=\frac{S_m-S_n}{\pi(m-n)}\quad(m\ne n),\quad S_{-n}=-S_n.
\]

素数冪項は有限のΛ(q)/√q和、pole項はβ=L/(4π)を使った

\[
P_{mn}=\frac{L(\sqrt c+1/\sqrt c-2)}{2\pi^2}
\frac{\beta^2-mn}{(m^2+\beta^2)(n^2+\beta^2)}.
\]

両者は辞書監査の直接積分・divided differenceと同じ規約である。
偶sectorのWeil形式同定と、全指数行列の数値正定値判定の範囲を区別する。
全行列が正なら、特に指定された等長埋込みによる偶sectorも正。

## 原著閉形式との解析照合

r(x)=Σ_(k≥0)e^(−c_k x), c_k=2k+1/2 と展開し、
0から∞までのLaplace積分をdigamma/trigammaの級数と比較すると、

\[
S_n=\tfrac12\Im\psi(1/4+iw_n/2)-w_nG_S,
\quad C_n=-\tfrac12\Re(\psi(1/4+iw_n/2)-\psi(1/4))+G_C,
\]
\[
X_n=\tfrac14\Re\psi'(1/4+iw_n/2)-LG_1-G_2.
\]

$G_S,G_C,G_1,G_2$ はそれぞれ e^(−c_kL) に
$1/(c_k^2+w_n^2)$、$w_n^2/[c_k(c_k^2+w_n^2)]$、
$c_k/(c_k^2+w_n^2)$、$(c_k^2-w_n^2)/(c_k^2+w_n^2)^2$ を掛けた和。
Lから∞の尾で w_nL=2πn を使用する。この導出が原著の閉形式を正当化し、
数値一致だけを恒等式の証明には使わない。

原著 `_geom_sums` は k>2まで計算し、残りを各和について
$4e^{-c_{k+1}L}/(1-e^{-2L})$ のballで覆う。
残りでは c_j≥8.5。4係数の絶対値は順に
$1/c_j^2,1/c_j,1/c_j,1/c_j^2$ 以下なので、この余剰係数4は安全。
この判定は c>1 が前提。実行CLIには一般の無効入力の検証がないため、指定入力以外へ無条件に拡張しない。

## 再実行と認証内容

環境: python-flint 0.9.0、mpmath 1.4.1。前者はArb/FLINTの区間演算を使用。
依存固定は `experiments/requirements-cert.txt`。

```sh
python3 -m venv .venv-cert
.venv-cert/bin/python -m pip install -r experiments/requirements-cert.txt
.venv-cert/bin/python experiments/scripts/groskin_independent_certificate.py
.venv-cert/bin/python experiments/scripts/groskin_compare_assemblies.py
```

最後の比較だけは版固定した原著コードの取得を要する。独立認証の実行は原著コード不要。

独立プログラムは192bitで81成分を組み立て、区間LDLを行う。
9個のpivotがすべて厳密に正。最小pivotは約7.8717192833×10^(−10)、
そのball半径は1.82×10^(−34)以下。**pivotを最小固有値と呼んではならない。**
全行列ball、全pivot、L因子をJSONに保存し、10進出力から再読込した行列でも正定値判定を再現。
区間LDLが包含するのは、解析的公式で定義した厳密行列の実LDL。
途中で0をまたぐpivotなら失敗して停止し、精度不足を負固有値と誤認しない。

原著arXiv v3のコードは全文静的確認後、c13,N4,384bitで再実行した。
原著selftestは既定c13,N8,300bitを使い、mpmathとの1e−60相対agreementでPASS。
これはball包含証明ではない。独立比較では c13,N=0,1,4 の計91成分すべてで、
原著384bit ballが直接求積192bit ballに包含され、Kの2表現も一致した。

さらに h_+(7) は
0.107179671275616465180782590044777210112891725273899511810777
を中心とする半径7.52×10^(−58)以下のballに入り、0<h_+(7)<0.1072を認証。
有理数のみで得る別の粗い認証はtail監査にある。

結果:

- `experiments/results/groskin-c13-n4-independent.json`: 独立組立て・全pivot。
- `experiments/results/groskin-c13-n4-author-rerun.json`: 原著コード再実行の要約。
- `experiments/results/groskin-assembly-comparison.json`: 境界N0/N1を含む照合。

Arb実装、ランタイム、解析的規約の監査を信頼基盤とする数値証明であり、Lean証明ではない。
高次N=200の原著出力を再現したとは記録しない。
本結果は1つの有限窓に関する既知構成の再現であり、全窓の一様制御・RH・新規性を主張しない。

独立監査: DESTROYER が S/CC/XC、K、非対角の符号、pole係数、analytic flag、
LDL判定の射程を別途再導出してPASS。一般入力の素数列挙について指摘された
浮動平方根は整数 `math.isqrt` に変更し、指定入力を再実行した。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/requirements-cert.txt`](../../../reports/experiments/requirements-cert.txt)
- [`experiments/results/groskin-assembly-comparison.json`](../../../../artifacts/experiments/results/groskin-assembly-comparison.json)
- [`experiments/results/groskin-c13-n4-author-rerun.json`](../../../../artifacts/experiments/results/groskin-c13-n4-author-rerun.json)
- [`experiments/results/groskin-c13-n4-independent.json`](../../../../artifacts/experiments/results/groskin-c13-n4-independent.json)
- [`experiments/scripts/groskin_compare_assemblies.py`](../../../../artifacts/experiments/scripts/groskin_compare_assemblies.py)
- [`experiments/scripts/groskin_independent_certificate.py`](../../../../artifacts/experiments/scripts/groskin_independent_certificate.py)
- [`literature/notes/groskin-certificate-audit.md`](../../../literature/literature/notes/groskin-certificate-audit.md)
- [`proofs/audits/groskin-dictionary.md`](groskin-dictionary.md)
- [`proofs/audits/groskin-tail.md`](groskin-tail.md)
