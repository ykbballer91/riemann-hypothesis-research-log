**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/joint-symbol-adversarial.md` · Original SHA-256: `b8126de53b094316e1044afd7c0840fa0a4e0ea897e74427f3743832b23e22a1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Joint symbol cutoff の敵対監査

2026-09-29。担当 DESTROYER。RH は OPEN。以下は symbol cutoff 候補の反証であり、RH の反例・証明、全窓の Weil 正値性、新規性を主張しない。

## 1. 対象と結果

$$
H(t)=\Re\psi(1/4+it/2)-\log\pi,\quad
P_a(t)=\sum_{\log n<2a}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n),
\quad \Psi_a=H-P_a,\quad
A_a=\sum_{\log n<2a}\frac{2\Lambda(n)}{\sqrt n}.
$$

敵対対象は $\mathsf H(a):\ \Psi_a(t)\ge0\ (\forall t\ge T_*(a)=2\pi e^{2a})$。
**指定された 5 個の $a$ 全てで偽。** 正確な有理数入力、Arb/ACB 256 bit、直接 digamma 評価により負点を認証した。各点の半径 $1/100$ の区間全体でも $t>T_*(a)$ と $\Psi_a(t)<0$ を認証した。

| 正確な $a$ | $T_*(a)$ 概数 | 正確な負点 $t$ | $\Psi_a(t)$ 概数 |
|---|---:|---:|---:|
| $4/5$ | 31.12082055 | $91/2$ | −0.885295709883 |
| $1$ | 46.42680871 | $109$ | −1.290445950835 |
| $119/100$ | 67.88920692 | $172$ | −1.496274958845 |
| $6/5$ | 69.26065987 | $281$ | −2.112751230914 |
| $7/5$ | 103.32476297 | $223$ | −2.646062919958 |

表の小数は表示用。全 ball は [joint-symbol-counterexamples.json](../../../../artifacts/experiments/results/joint-symbol-counterexamples.json)。SHA-256:

~~~text
a85ad4429e8c330938481f205fa57f5d264a49c11c8ca5e14f48900270faa4b4
~~~

使用した素数冪は順に

~~~text
4/5:     2,3,4
1:       2,3,4,5,7
119/100: 2,3,4,5,7,8,9
6/5:     2,3,4,5,7,8,9,11
7/5:     2,3,4,5,7,8,9,11,13,16
~~~

$119/100$ から $6/5$ への移動では $n=11$ が入る。窓変更では prime 集合と strict endpoint 規約も再検証する。固定窓の certificate をそのまま別窓へ移さない。

## 2. 再現コードと認証範囲

float64 格子と $H(t)\approx\log(t/(2\pi))-1/(24t^2)$ は候補選択だけに用いた。下記認証にはその近似を使わない。$2a<\log18$ を証明し、18 未満の全素数冪を整数演算で列挙する。threshold 判定が未確定なら停止する。環境は python-flint 0.9.0。

~~~python
from flint import arb, acb, ctx
from math import isqrt
import json
from pathlib import Path
ctx.prec=256
pi=arb.pi()
specs=[(4,5,91,2),(1,1,109,1),(119,100,172,1),
       (6,5,281,1),(7,5,223,1)]
saved=json.loads(Path(
 "experiments/results/joint-symbol-counterexamples.json").read_text())
for (an,ad,tn,td),rec in zip(specs,saved["cases"]):
    a,t=arb(an)/ad,arb(tn)/td
    assert 2*a<arb(18).log()
    terms=[]
    for p in range(2,18):
        if any(p%d==0 for d in range(2,isqrt(p)+1)):
            continue
        q=p
        while q<18:
            gap=2*a-arb(q).log()
            assert gap>0 or gap<0
            if gap>0:
                terms.append((q,2*arb(p).log()/arb(q).sqrt()))
            q*=p
    terms.sort()
    assert [q for q,w in terms]==rec["prime_powers"]
    cutoff=2*pi*(2*a).exp()
    def symbol(x):
        H=acb(arb(1)/4,x/2).digamma().real-pi.log()
        P=sum((w*(x*arb(q).log()).cos() for q,w in terms),arb(0))
        return H-P
    value=symbol(t)
    interval=arb(t,arb(1)/100)
    interval_value=symbol(interval)
    assert t-cutoff>0 and value<0
    assert interval-cutoff>0 and interval_value<0
    assert arb(rec["symbol_value"]).contains(value)
    assert arb(rec["neighborhood_symbol_ball"]).contains(interval_value)
    print(an,ad,tn,td,"negative point and interval: PASS")
~~~

区間半径は内部で $1/100$ を外向き包含し、表示された幅を入力には使わない。point ball の幅と区間評価の幅は別物。厳密認証は FLINT/Arb の保証と実行環境を信頼する計算証明であり、ライブラリ内部の形式検証ではない。

## 3. Constant-comb barrier の正しい適用範囲

$P_a(t)\le A_a$ は frequency-independent 上界として最適。$P_a(0)=A_a$ に加え、一意分解から $\log p$ の整数線形独立性が従い、連続時間の Kronecker 近似により全位相は任意に大きい $t$ で同時に $0\bmod2\pi$ に近づく。素数冪の位相も近づくため $\sup_{t\ge T}P_a(t)=A_a$。従って $P_a\le A_a-\delta$ を tail 全体に使う改善は $\delta>0$ について不可能。

しかし、$H(t)-P_a(t)$ の joint lower bound の障害ではない。prime comb が大きい場所では $H$ も大きくなり得る。定数 envelope

$$
\Psi_a(t)\ge b_a(t)=\log(t/(2\pi))-1/t-A_a
$$

だけを使うクラスでは正性に $t>T_1(a)=2\pi e^{A_a}$ が必要で、正確な開始点はさらに少し大きい。$T_1$ を joint pointwise 証明でも越えられない barrier と呼ぶのは誤り。

### 明示例: $a=1/2$ で cutoff $12<T_1$

この窓では $P(t)=A\cos(t\log2)$、$A=\sqrt2\log2<0.981$、$T_1>16.7455$。それでも

$$
\boxed{\Psi_{1/2}(t)>9/1000\qquad(t\ge12)}
$$

が成立する。$H'(t)=\frac t2\sum_{k\ge0}(k+1/4)/((k+1/4)^2+t^2/4)^2>0$。
次の有限個の厳密不等式を Arb で認証した:

$$
\begin{gathered}
H(12)>0.6,\quad H(16)>0.9,\quad H(17)>0.99,\\
2\pi<12\log2<3\pi<16\log2<18\log2<4\pi,\\
\cos(12\log2)<0.1,\quad\cos(16\log2)<0.1,\quad
\cos(17\log2)<0.75,\quad b_{1/2}(18)>0.01668.
\end{gathered}
$$

| 区間 | 全区間の評価 | $\Psi$ の下界 |
|---|---|---:|
| $[12,16]$ | cosine の最大は端点、$\cos\le0.1$, $H>0.6$ | $>0.5$ |
| $[16,17]$ | cosine は増加、$\cos<0.75$, $H>0.9$ | $>0.15$ |
| $[17,18]$ | $\cos\le1$, $H>0.99$, $A<0.981$ | $>0.009$ |
| $[18,\infty)$ | 増加する envelope $b(t)\ge b(18)$ | $>0.01668$ |

終端 envelope の独立導出は [fixed-window-reduction.md §2.1](fixed-window-reduction.md)。$u=t/2$ とし、単峰関数 $(x+1/4)/((x+1/4)^2+u^2)$ の整数和を積分と最大値 $1/(2u)$ で抑えると、全 $t>0$ で $\Re\psi(1/4+it/2)\ge\log|1/4+it/2|-1/t\ge\log(t/2)-1/t$。

~~~python
from flint import arb,acb,ctx
ctx.prec=256
pi,ell=arb.pi(),arb(2).log()
A=arb(2).sqrt()*ell
H=lambda t:acb(arb(1)/4,arb(t)/2).digamma().real-pi.log()
assert ell<1 and arb(3).log()>1
assert A<arb(981)/1000
assert 2*pi<12*ell and 18*ell<4*pi
assert 12*ell<3*pi and 16*ell>3*pi
assert (12*ell).cos()<arb(1)/10
assert (16*ell).cos()<arb(1)/10
assert (17*ell).cos()<arb(3)/4
assert H(12)>arb(3)/5 and H(16)>arb(9)/10 and H(17)>arb(99)/100
assert (arb(18)/(2*pi)).log()-arb(1)/18-A>arb(9)/1000
assert 2*pi*A.exp()>12
print("joint cutoff 12, uniform floor 9/1000: PASS")
~~~

この例は symbol tail だけの命題であり、低周波、pole、head–tail coupling を含む Weil 形式全体の正性を単独では与えない。

## 4. 有限標本から tail 正性へ進む条件

等間隔格子 $t_0+jh$ に対し $g(t)=1-2\sin^2(\pi(t-t_0)/h)$ は全格子点で $1$、中点で $-1$。任意の有限不規則標本集合 $S$ にも $u\notin S$ と $K>\log2/\min_{s\in S}|s-u|^2$ を選べば $g(t)=1-2e^{-K(t-u)^2}$ が同じ障害を示す。実解析性を加えても有限 sampling だけでは足りない。これらは toy example であり $\Psi_a$ や RH への反例ではない。

実際の認証には次が必要。

- $[T,U]$ を隙間なく覆う有限閉区間の全てで $\Psi_a(I_j)$ の外向き enclosure の下端が同じ明示値 $\beta$ 以上。未確定区間は分割・精度上昇するか失敗とし、無視しない。
- 格子を用いる場合は両端点を含め、最大間隔 $h$、点での厳密下界 $m$ と微分上界 $D$ から $m-Dh/2$ を全区間下界とする。
- 遠方 $[U,\infty)$ には別途 $b_a(U)\ge\beta$ 等の解析的証明。有限 covering のみでは tail 証明にならない。

例えば $[u,v]\subset(0,\infty)$ では [groskin-tail.md §3](groskin-tail.md) の導出から

$$
|\Psi_a'(t)|\le\frac1u+\frac{13}{10u^2}
 +\sum_{\log n<2a}\frac{2\Lambda(n)\log n}{\sqrt n}.
$$

float による cutoff 提案は構わないが、証明書では $a,T,U,\beta$ を正確に固定する。symbol の偶性で負周波数も処理する。

## 5. 過剰な含意を止める

今回の負区間は $\mathsf H(a)$ を反証するが、Weil 形式の負方向は与えない。固定 support の Fourier 質量を任意に狭い区間へ完全局在できるとは限らず、pole 項も必要。

反対に、任意固定 $a$ に対する十分大きい cutoff の tail 正性は $H(t)\to\infty$ と $P_a$ の有界性から既に従う。cutoff の改善だけで有限 head の符号、無限 mode の coupling、全窓の量化は解決しない。全称の Weil 正値性は RH 同値であり、今回の結果からは得られない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/joint-symbol-counterexamples.json`](../../../../artifacts/experiments/results/joint-symbol-counterexamples.json)
- [`proofs/audits/fixed-window-reduction.md`](fixed-window-reduction.md)
- [`proofs/audits/groskin-tail.md`](groskin-tail.md)
