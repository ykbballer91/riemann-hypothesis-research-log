**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/window-half-independent.md` · Original SHA-256: `6fc51b166fb8c8300af7572f5acf97483d8b7c8ed799f2bd147454e0c95c7e62`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 固定窓 [-1/2,1/2] 認証の独立再実行・敵対監査

日付: 2026-09-29。担当: DESTROYER。**RH は OPEN。**

対象は [window_half_certificate.py](../../../../artifacts/experiments/scripts/window_half_certificate.py) と [数学的証明書](window-half-certificate.md)。固定窓 $[-1/2,1/2]$、$T=32$、cut order $64$、Gauss order $32$、panel 幅 $1/4$、head shift $10^{-7}$ を監査した。偶 sector の次数 $0,2,\ldots,62$ と奇 sector の次数 $1,3,\ldots,63$ は **各32次の head**。無限 tail は別の解析評価で含める。

**判定:** この指定入力について数学的な正規化・求積誤差・無限 tail/cross の導出に欠陥は見つからず、224bit の別実行は成功した。保存した head ball を256bitで読み直し、元の LDL helper を使わない別実装の interval Cholesky でも両 sector を再認証した。得られる全形式の下界は $9.9\times10^{-8}$ より大きく、親証明書が採用する $9\times10^{-8}$ を支持する。

これは **一つの窓に限る計算機援用証明の監査**。完全な RH 監査、全窓共通の正性、原著 Zhu の $L=0.8$ の計算再現、新規性の認定ではない。

## 1. 実行と独立性の範囲

元の192bit結果を上書きせず、作業ディレクトリを [local machine path omitted] に変更し、同じ assembly script を別プロセス・224bitで実行した。

~~~sh
'[source repository]/.venv-cert/bin/python' \
  '[source repository]/experiments/scripts/window_half_certificate.py' \
  --bits 224
~~~

この再実行は独立に書き直した assembly ではなく、**同じプログラムの別精度・別プロセスでの再実行**。一方、後述の Cholesky は独立に書いた別アルゴリズムであり、数学的な定数・符号は実装とは別に導出した。いずれも python-flint 0.9.0 と Arb/FLINT を共通の信頼基盤とする。

完全な224bit JSON は、生成物と byte-for-byte 同一のまま [window-half-independent-224.json](../../../../artifacts/experiments/results/window-half-independent-224.json) へコピーした。root の [192bit JSON](../../../../artifacts/experiments/results/window-half-T32-cut64.json) は変更していない。

| 項目 | 224bit 再実行の結果 |
|---|---|
| even shifted pivots | 32/32 が厳密に正 |
| odd shifted pivots | 32/32 が厳密に正 |
| $\beta$ | $0.6163506929218338718\ldots$ |
| 各 entry の解析的求積誤差上界 | $8.713\times10^{-45}$ 未満 |
| $\varepsilon_B$ | $3.785\times10^{-29}$ 未満 |
| $\varepsilon_D$ | $2.361\times10^{-60}$ 未満 |
| 指定窓の全mode下界 | $10^{-7}-\varepsilon_B>9.9\times10^{-8}$ |
| 実行時間 | 約6.5秒、この環境での観測値 |

pivot は eigenvalue ではない。認証するのは shifted head が正定値であること。

## 2. ハッシュと192bit結果との照合

SHA-256 を実ファイルの bytes から計算した。

| Artifact | SHA-256 |
|---|---|
| root192 JSON | fffcc4c3b501f7628be6f71d97349d0166c6c70ee9b96fd634d44d99d2d0b88f |
| independent224 JSON | 44ed72882b8b3f5c676141a2980560916e8cd3f638e5302c0f27324564691b5c |
| assembly script | d4b176096168c13f53459f27e1ae9a9db9e045a4b774c097f49a9939d5c408d0 |
| LDL helper script | a8d277e17898f39a86d4729a9c47534a6db0d087f4a1ccbaca58d891f7e239e8 |

両 JSON 内の script/helper hash は等しく、監査時の実ファイルとも一致した。

以下は head の **保存済み ball 文字列配列** に対し、UTF-8 の
json.dumps(head, ensure_ascii=False, separators=(',', ':')) の SHA-256 を計算したもの。超越的な厳密行列値そのものを hash 化したという意味ではない。

| Head | SHA-256 |
|---|---|
| root192 even | ec652a787278509fea93af7edd5f19da05ba35d3ec766a7b8009b254dfb1642d |
| independent224 even | f81621ec45d2300877638660bab985f4f2b9583d28ad7d94b84335d0b52e274f |
| root192 odd | bc75ccf5857f27aad5accb6ec85029517895750644b6df05adc567255af15a44 |
| independent224 odd | 62564abde818ec8c839f729458b39ccebda55b35311b5557176cd90b918bb9a8 |

384bit で両 JSON の decimal balls を解析し比較した。

| 比較 | even | odd |
|---|---:|---:|
| entry ball の overlap | 1024/1024 | 1024/1024 |
| 224bit ball が192bit ball に包含 | 12/1024 | 18/1024 |
| 192bit ball が224bit ball に包含 | 12/1024 | 18/1024 |
| shifted pivot ball の overlap | 32/32 | 32/32 |

$\beta$、求積誤差、$\varepsilon_B$、$\varepsilon_D$、指定窓の全mode下界 の5項目も全て overlap した。**全 entry の包含は成立していない**。両精度に同じ解析的求積誤差を加えているため、精度を上げたことだけで包含関係を推定しない。overlap は整合性検査であり、正性の証明は各 ball に対する独立の因子分解と解析的 error enclosure による。

## 3. 保存された head に対する別実装 interval Cholesky

元の LDL helper を import せず、保存された各 head から厳密な shift を引き、平方根を使う Cholesky を別実装した。全ての新しい diagonal remainder を ball 比較で正と確認してから平方根を取る。零を跨ぐ値を成功扱いする分岐はない。

次のコードを project root で実行した。確認対象 JSON hash を最初に固定し、224bit JSON を256bitで再読込する。

~~~python
from pathlib import Path
import hashlib, json
from flint import arb, ctx

ctx.prec = 256
p = Path('experiments/results/window-half-independent-224.json')
assert hashlib.sha256(p.read_bytes()).hexdigest() == (
    '44ed72882b8b3f5c676141a2980560916e8cd3f638e5302c0f27324564691b5c')
r = json.loads(p.read_text())
assert r['precision_bits'] == 224 and r['certificate_passed']
shift = arb(1)/10**7
assert arb(r['head_shift']).contains(shift)

for sec in r['sectors']:
    A = [[arb(s) for s in row] for row in sec['head']]
    n = len(A)
    assert n == 32
    C = [[arb(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        d = A[j][j] - shift - sum(
            (C[j][k]*C[j][k] for k in range(j)), arb(0))
        assert d > 0
        C[j][j] = d.sqrt()
        for i in range(j+1, n):
            C[i][j] = (
                A[i][j] - sum(
                    (C[i][k]*C[j][k] for k in range(j)), arb(0))
            ) / C[j][j]
    print(sec['parity'], 'independent interval Cholesky PASS', n)

assert arb(r['full_window_lower_bound']) > arb('9.9e-8')
~~~

結果は even/odd とも32段階で PASS。head は近似求積値だけでなく、解析的な Gauss 誤差を既に各 entry ball に加えたものなので、この再認証も厳密な leading block を含む行列に対する判定である。異なる entry 間の interval dependency を無視することは enclosure を広くし得るが、偽の狭い enclosure を作る方向には働かない。

## 4. 数学的な読取検査

### 4.1 正規化と parity

$a=1/2$、
$\phi_n(x)=\sqrt{(2n+1)/(2a)}P_n(x/a)$ に対して

\[
\widehat\phi_n(t)=\sqrt{2a(2n+1)}\,i^n j_n(at).
\]

odd sector の Fourier transform は共通の $i$ を含むが、Hermitian product ではそれが消える。コードの実振幅 $(-1)^{\lfloor n/2\rfloor}\sqrt{2n+1}\,j_n(t/2)$ は両 parity で整合する。pole coefficient にこの Fourier phase を移していないことも確認した。

$j_n(z)=z^n(2n+1)!!^{-1}\,{}_0F_1(n+3/2;-z^2/4)$ と modified spherical Bessel の正符号版が、それぞれ multiplier と pole に使われている。installed API の hypgeom_0f1 は既定で非正則化版であり、この式と一致する。

even pole の符号 $+2pp^t$ と odd pole の符号 $-2pp^t$ は正しい。odd の負項を捨てて positivity を見かけ上増やしてはいない。

### 4.2 複素 ellipse 上の symbol bound

panel 半幅は $1/8$。Bernstein parameter $\rho=6$ の半短径は $35/96<0.4$、全実部範囲は $[-25/96,T+25/96]\subset[-0.3,T+0.3]$。

$z=1/4\pm it/2$ は $\Re z\ge0.05$、$|z|\le T/2+0.6$。部分分数展開

\[
\psi(z)=-\gamma-\frac1z+\sum_{k\ge1}\frac{z}{k(k+z)}
\]

より、$|k+z|\ge k$ と $\sum k^{-2}<2$ を使って
$|\psi(z)|<1+20+2|z|\le T+22.2$。
half-sum、$\log\pi<2$、$|\cos(t\log2)|<2$ を合わせれば

\[
|\Psi(t)-\beta|\le M_0=T+25+2A+|\beta|.
\]

ここでは非正則な real-part 関数を複素解析的と見なしていない。実軸の値は half-sum の解析的延長と一致する。

Legendre の積分表示から $|j_n(at)|\le e^{a|\Im t|}$。$n,m<64$ に対する全 integrand、$1/\pi$ 込みの上界は

\[
M=\frac{M_0(2\cdot64-1)e^{0.4}}{\pi}.
\]

コードの係数と一致した。

### 4.3 Gauss error の定数

ellipse 上での上界が $M$ なら、次数63までの Chebyshev 切断の一様誤差は

\[
E\le 2M\,\frac{\rho^{1-64}}{\rho-1}.
\]

32点 Gauss は次数63の多項式に exact。物理 panel 長を $h$ とすると、積分と正の quadrature weights はともに全質量 $h$ なので、その差の誤差は $2hE$ 以下。全 panel 長の和 $T$ により

\[
\varepsilon_{\rm entry}\le
4TM\,\frac{\rho^{1-64}}{\rho-1}.
\]

積分長・$1/\pi$・偶 sector の係数に欠落はない。node/weight は Arb の certified Legendre-root API の ball で評価され、有限求積の丸めと特殊関数評価の誤差は ball 演算に含まれる。

### 4.4 無限 tail と head/tail coupling

$X=aT=16$、
$b_n=\sqrt{2n+1}X^n/(2n+1)!!$ に対し

\[
\frac{b_{n+1}}{b_n}
=\frac{X}{\sqrt{(2n+1)(2n+3)}}
\le\frac{16}{129}<1\quad(n\ge64).
\]

コードが用いる $16/129$ は安全な上界。全次数 $n\ge64$ の幾何和を取っているので、even tail と odd tail の双方を包含する。pole の同じ評価は $X$ を $1/4$ に替え、$e^{1/4}$ を掛けたもの。

Fourier evaluation vector の全ノルムは Parseval で $\sqrt{2a}=1$ 以下。従って

\[
\|B\|\le\frac{M_0T}{\pi}\eta_F+2e^{1/4}\eta_p,
\quad
D\ge\left(\beta-\frac{M_0T}{\pi}\eta_F^2-2\eta_p^2\right)I.
\]

コードと一致する。$T/\pi$ を保持し、Zhu 本文で反証した不完全な entry bound を使っていない。両 head と tail の lower bound と $\|B\|$ から全空間の下界を出しており、有限 PSD のみから無限次元へ飛躍してはいない。

## 5. 認証の正確な範囲

対象は零延長した $H=L^2([-1/2,1/2])$ の形式作用域

\[
\mathcal D=
\left\{f\in H:\int_{\mathbb R}\log(2+|t|)|\widehat f(t)|^2dt<\infty\right\}.
\]

幾何側で定義された Weil 形式について、任意の複素 $f\in\mathcal D$ に対し $Q_W(f)\ge9\times10^{-8}\|f\|_2^2$ という親命題を支持する。domain 外を $+\infty$ とする拡張は可能だが、全 $L^2$ で零点和が絶対収束するとは主張しない。

有限積分の bounded form $R_T$ の正性を全 $H$ 上で認証したため、Legendre basis を unbounded $Q_W$ の operator core とする追加の主張は不要。必要な全次数の完備性・tail の収束・coupling は明示されている。

残る信頼基盤は、Weil 幾何側の規約、特殊関数恒等式、上の解析的不等式、Arb/FLINT とランタイム、保存・再読込である。Lean による全工程の形式検証ではない。既知の有限窓手法の独立実装・限定監査であり、RH の解決や新規性は主張しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/window-half-T32-cut64.json`](../../../../artifacts/experiments/results/window-half-T32-cut64.json)
- [`experiments/results/window-half-independent-224.json`](../../../../artifacts/experiments/results/window-half-independent-224.json)
- [`experiments/scripts/window_half_certificate.py`](../../../../artifacts/experiments/scripts/window_half_certificate.py)
- [`proofs/audits/window-half-certificate.md`](window-half-certificate.md)
