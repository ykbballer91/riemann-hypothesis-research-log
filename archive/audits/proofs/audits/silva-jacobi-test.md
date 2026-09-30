**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/silva-jacobi-test.md` · Original SHA-256: `1fc2e5f64d7b14c79b6f8a0426197a3728d6cddd00194855a269cd496372db43`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Silva actual theta 列: E≤6 の固定 Jacobi 候補を棄却

2026-09-29。**CERTIFIED NEGATIVE RESULT FOR THIS OPERATOR CANDIDATE ONLY。**
実theta profileから得るmonic列 `p0,p1,p2,p3` は三項漸化式を満たさない。
これはRHの反証でも、Silvaの近似定理の否定でもない。

原典: [Silva, arXiv:2609.25564v1](https://arxiv.org/html/2609.25564v1)、(8)、(16)–(17)。
実装は [silva_jacobi_certificate.py](../../../../artifacts/experiments/scripts/silva_jacobi_certificate.py)、
全区間・係数辞書・hashは [silva-jacobi-certificate.json](../../../../artifacts/experiments/results/silva-jacobi-certificate.json)。
著者コードは実行・importしていない。

## J1. 棄却する具体的候補

`z=s−1/2, u=z²` とし、E=2nに対して `Z_(2n)(1/2+z)` をuの多項式と読む。
その最高次係数で割ったmonic多項式を `p_n(u)` とする。
`p0=1` はmonic定数の規約である。原典が定義するEは正の偶数で、
E=0における `j/E` を計算するのでなく、任意の非零定数のmonic正規化を初項とする。

候補は、**この同じ変数u・この同じ次数順序の列が、固定Jacobi行列Jの先頭n×n主小行列の特性多項式になる**ことである。
Jacobi行列の対角を `α_n`、隣接要素を実 `b_n≠0` とすると、最後の行のdeterminant展開により必ず

\[
p_{n+1}(u)=(u-\alpha_n)p_n(u)-\beta_n p_{n-1}(u),
\qquad \beta_n=b_n^2>0
\]

となる。この必要条件は有限行列の恒等式だけであり、無限作用素のdomainやFavard定理の十分方向に依存しない。
ここでpositiveとは正の直交化・正の隣接係数に関する条件であり、Jそのものを正作用素と仮定していない。

## J2. 一意な三項係数と残差

\[
p_1=u+a,\qquad p_2=u^2+bu+c,\qquad p_3=u^3+du^2+eu+f.
\]

u²とuの係数を比較すると、候補の係数は一意に

\[
\alpha_2=b-d,\qquad \beta_2=c-\alpha_2b-e
\]

で決まる。残る定数係数は

\[
\boxed{p_3=(u-\alpha_2)p_2-\beta_2p_1+\gamma p_0,
\qquad \gamma=f+\alpha_2c+\beta_2a.}
\]

従ってこの候補の必要条件は `γ=0`。係数の正値性だけではこれを代用できない。
一つ前の段階は `α1=a−b, β1=−α1 a−c` により常に形式上合わせられるので、
E=6で初めて追加の独立した残差を検査する。

## J3. 少数sampleからの厳密係数化

Pの対称性を使い、必要なsampleは `x=0,1/6,1/4,1/3,1/2` の5点だけ。
各項

\[
(-1)^j\binom EjP(j/E)\frac1{E!}
 \prod_{k=0}^{E-1}(E-j-k-1/2-z)
\]

をFractionによる有理多項式として展開し、jとE−jを**区間演算の前に**合わせた。
すべての奇数次係数が有理数として0であることをassertした。
E=6の係数辞書は、列が `1,u,u²,u³` の順で

| sample | 1 | u | u² | u³ |
|---|---:|---:|---:|---:|
| P(0) | 231/512 | 12139/5760 | 101/288 | 1/360 |
| P(1/6) | 63/256 | −739/960 | −41/48 | −1/60 |
| P(1/3) | 105/512 | −341/384 | 25/96 | 1/24 |
| P(1/2) | 25/256 | −259/576 | 35/144 | −1/36 |

E=4の係数は既存の閉形式辞書とも別に照合し、区間のoverlapを確認した。
最高次係数が正であることをE=2,4,6すべてで認証してからmonic化した。

積分はpython-flint 0.9.0のArb/ACB、192 bits。既に監査した
[E4 certificate](../../../../artifacts/experiments/scripts/silva_degree_four_certificate.py)と同じtheta kernel、
`n≤4, 0≤v≤2` を使う。全sampleを通じて分母 `1+4x(1−x)sinh²(v/2)≥1` なので、
同じ解析的誤差上界が適用できる。省いたn項の一様上界は約 `1.12286×10^(−30)`、
v>2の一様上界は約 `1.21957×10^(−70)`。それらをArbの半径へ加えた。
ACB quadratureの有限性と虚部の0包含も確認した。`P(0)=1/2` を数値入力に強制せず、積分区間がその値を含むことを確認した。

## J4. 認証結果

多項式の概形は次の通り（表示は近似、証明に用いる全区間はJSONに保存）。

\[
\begin{aligned}
p_1(u)&\simeq u+87.27109322136,\\
p_2(u)&\simeq u^2+765.74622545931u+44283.5829143382,\\
p_3(u)&\simeq u^3+2792.78729601947u^2
 +793098.737482920u+41230898.3375644.
\end{aligned}
\]

認証された残差は

\[
\gamma\in
[21578447.7300319429859648640601801972932585691
 \ \pm\ 3.52\times10^{-15}].
\]

特にプログラムは粗い有理境界でも

\[
\boxed{21578447.73<\gamma<21578447.74}
\]

をassertした。これは丸め誤差やquadrature/tail誤差で0へ動く値ではない。
なお `β1≈14927.68360>0, β2≈803383.89406>0` も区間で確認した。
失敗は隣接係数の符号でなく、独立な定数残差 `γ≠0` にある。

実行:

```sh
.venv-cert/bin/python experiments/scripts/silva_jacobi_certificate.py
```

原文HTMLは数学入力ではない。cacheがあれば固定されたexpected hashとの一致をassertし、
cacheがなければexpected hashだけを記録して計算を継続する。原文・著者コードを配布物へ含める必要はない。

### 独立監査

DESTROYERはscriptをimportせず、beta積分のrising-factorial表現を
`s=1/2+k, u=k²` で評価し、有理Vandermonde補間でE=2,4,6の全係数rowを再構成した。
JSONの辞書との完全一致を確認したうえで、保存されたsample enclosureを入力とする別の256-bit計算により
`γ≈21578447.73003194`、半径 `3.55×10^(−15)`、`γ>21000000` と既存区間とのoverlapを確認した。
この監査では積分自体の再実行はしていない。kernel/tailの検証は前段のE4監査を使用している。
ROOTもmonic係数比較とγ式を読んで整合を確認した。
後続の変更は粗い区間・βの追加assertとcache-optionalなprovenance処理であり、積分・係数・γの計算式は同じである。

## J5. 射程と停止

実際のSilva列が、そのまま固定Jacobi作用素の主小行列の特性多項式列になる候補は、E≤6で棄却された。
次数ごとの非零定数倍はmonic化で消えるため、それだけではこの残差を修復できない。
同じ列を正の共通測度で直交化されたmonic多項式列とする候補も、必要な三項漸化式を満たさない。

この検査は、次数依存の変数変更・別のgauge・別の多項式列・非Jacobi作用素・非主小行列compressionを否定しない。
各Z_Eの零点位置、全Eでの零点保存、RH、Silvaの対称性と局所一様近似定理についての反証ではない。
**E>6には拡大せず、この固定Jacobi候補を停止する。**


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/silva-jacobi-certificate.json`](../../../../artifacts/experiments/results/silva-jacobi-certificate.json)
- [`experiments/scripts/silva_degree_four_certificate.py`](../../../../artifacts/experiments/scripts/silva_degree_four_certificate.py)
- [`experiments/scripts/silva_jacobi_certificate.py`](../../../../artifacts/experiments/scripts/silva_jacobi_certificate.py)
