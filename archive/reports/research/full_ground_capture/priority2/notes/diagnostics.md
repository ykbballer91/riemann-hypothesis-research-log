**STATUS: RIEMANN HYPOTHESIS OPEN**

> Dated auxiliary research snapshot, 2026-09-30. Priority 2 only: fixed finite heads, not full-ground capture or RH.
> Public credit: @ykbballer91 · AI-assisted · Original text: CC BY 4.0.
> Source: `research/full_ground_capture/priority2/notes/diagnostics.md`; original SHA-256: `889566b20bc655d60037e86b6d8f7bcb61259ed6eff2e0e4de938d75d330ec1e`. Publication formatting does not constitute a new mathematical audit.

---

# Priority 2 — 数値診断と区間認証を分けた結果

2026-09-30。RH OPEN。数値は growth fit や RH の証拠に使わない。

## 方法

[finite_head_probe.py](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/finite_head_probe.py) を
85桁/144点と115桁/208点の Gauss–Legendre 求積で実行した。
theta の最初16項、global Gram の積分区間は \([-4,4]\)。
これらの打切りを含む physical Gram の値は **診断値** であり区間認証ではない。
raw 行列には求積と別の incomplete-Gamma tail + exact endpoint recurrence を用い、
二経路を比較した。

基底 \(b_n\)、\(\widehat k=\Xi/4\)、\(m=N\) はノートの規約通り。
\(G=LL^*\) の Cholesky を用い、physical 特異値は \(B(L^*)^{-1}\) で計算した。
normalization に head Gram \(B^*B\) を使って特異値を自動的に1へする操作はしていない。

|\(a\)|\(N=m\)|raw \(\sigma_{\min}(B)\)|raw 条件数|global Gram 後 \(\sigma_{\min}\)|\(\|E\|_2\)|
|---:|---:|---:|---:|---:|---:|
|0.5|2|0.0559056|2298.30|0.384547|22.3088|
|1|2|0.0871561|871.439|0.295466|0.0132184|
|1|4|0.0853302|\(1.326\cdot10^7\)|0.297086|13213.8|
|1.5|4|0.0679625|\(6.544\cdot10^6\)|0.0123699|\(3.008\cdot10^{-9}\)|
|2|4|0.0523062|\(1.606\cdot10^6\)|0.000828214|\(3.428\cdot10^{-52}\)|
|2|6|0.0512991|\(9.126\cdot10^{10}\)|0.0000809842|\(4.367\cdot10^{-42}\)|

各ケースで raw/physical の全特異値は正として解像された。
最初の \(N+1\) 列が数値的に full rank なので、観測した最小 \(m\) は \(N\)。
\(m<N\) なら次元だけで全 head を張れない。浮動小数点の rank 検査を exact rank の証明とはしない。

原点と grid の Xi 値、全 physical 特異値、principal angle、tail、求積照合誤差は
[115桁結果](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/probe_115.json) に保存した。
85桁からの raw 数値比較は相対 \(10^{-30}\) 以下（35桁出力の比較）、
physical 最小特異値は相対 \(10^{-19}\) 以下で一致。
115桁での係数行列二経路の相対差は \(10^{-95}\) 以下。
[比較スクリプト](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/validate_diagnostics.py) と
[検算結果](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/diagnostic_validation.json) を併記する。
この一致は誤差包含の証明ではない。

## 良い座標と良い物理写像は異なる

\((a,N)=(1,4)\) では raw 条件数が約1300万でも、physical 最小特異値は約0.297。
座標の悪条件が相当部分を占める。
一方 \((2,6)\) では physical 最小特異値自体も約 \(8.10\cdot10^{-5}\)。
座標を変えるだけでこの射影の損失は消えない。

同じ \((1,4)\) で raw tail が約13214と大きいのに、
\(\|EA^{-1}\|_2\approx0.123825<1\) となった。
方向を無視した \(\|E\|/\sigma_{\min}(A)\) は非常に粗くなり得る。
この sharper 判定値は数値診断であり、今回の区間証明には用いない。

射影後 span が head 全体なら、その span と head の角度は自動的に0。
ここで有用なのは **射影前** の derivative span と head の角度であり、
JSONの largest_global_subspace_angle は physical 最小特異値の arccos を記録する。

## Grid hit の診断

最初の臨界線零点の数値 ordinate \(\gamma_1\) を使い、
\(a\approx\pi/\gamma_1=0.2222606115\)、\(N=m=1\) も検査した。
ideal の第1行は exact hit の定義では零だが、actual は端点項を持つ。
診断値は \(\sigma_{\min}(B)\approx0.0343614\)、physical 値約0.253438。
**有限精度の \(\gamma_1\) は exact grid equality の認証ではなく、actual rank の区間証明でもない。**
この例は ideal の row zero と actual の row zero が別物であることを確認する用途だけ。

## 証明として使う別計算

[certify_tail_criterion.py](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/certify_tail_criterion.py) は求積・SVDを使わず、
TC7 の解析的不等式全体を Arb ball で囲う。
\(a\in[1.499999,1.500001],N=m=4\) と
\(a\in[1.999999,2.000001],N=m=6\) の full rank を認証した。
詳しい数値は [tail_certificates.json](../../../../../../artifacts/research/full_ground_capture/priority2/experiments/tail_certificates.json)。
256/384 bitの両方で strict inequality を確認している。

依存：Python、mpmath 1.4.1、python-flint 0.9.0。
再現コマンド（この experiments ディレクトリで）：

```sh
python finite_head_probe.py --dps 85 --quad 144 --output probe_85.json
python finite_head_probe.py --dps 115 --quad 208 --output probe_115.json
python validate_diagnostics.py
python certify_tail_criterion.py
```

全 Weil 行列や ground state は計算していない。fixed head の spanning/conditioning の診断のみ。
