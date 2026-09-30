**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/caceres-asymptotic-adversarial.md` · Original SHA-256: `b1840c7256bab3eff7fd55f0fe6b532b881cb47bdcf8fbaf4b50f1e6cff927de`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Cáceres 2609.28529v1 — 漸近的 rigidity の独立敵対監査

2026-09-29、DESTROYER。対象は Pedro Cáceres, [Asymptotic Balance and Structural Rigidity in the Riemann Zeta Function, arXiv:2609.28529v1](https://arxiv.org/abs/2609.28529v1)。
**判定: Theorem 4.1 / (55) は厳密な解析的反例により FALSE。外部 RH 証明としてこの経路は STOP。これは RH の反例ではなく、RH は OPEN。**

## 1. 原本固定・読取範囲

固定 PDF:
caceres-2609.28529v1.pdf（原資料参照・公開版未収録: `literature/source_cache/caceres-2609.28529v1.pdf`）

~~~text
SHA256:
65d4ec84fc34f01f87e12d357582f8b91fadf9549594a1a9a170892615c42e70
~~~

ファイル hash を独立再計算し一致を確認した。22ページの PDF のうち、実ページ3、5、6、8、10、11を Poppler でレンダリングし画像を読んだ。以下のページ数は **PDF の物理ページ／フッターの Page n of 22** であり、重複 text layer 内の旧原稿ページ数ではない。頁3と5には定義と Euler–Maclaurin 部分が反復掲載されている。

| 場所 | 原文の内容 | 独立判定 |
|---|---|---|
| p.3、反復 p.5、(13) | 包含端点 sum の Euler–Maclaurin 展開 | YES、固定 $s$ の漸近式として正しい |
| p.3、反復 p.5、(15)–(16) | (13) からの移項と remainder order | FAILED、端点の符号が逆 |
| p.3、反復 p.5、(17)–(18) | $X_N,Y_N$ の定義 | 画像で確定、下記の printed 定義 |
| p.8、Lemma 3.1、(37)–(38) | 零点で二乗絶対値の差が0へ収束 | printed 定義では FALSE、§5 |
| p.10、(46)–(50) | $O$ bound から ratio divergence へ | FAILED、直前の bound 自体と両立しない |
| p.11、Theorem 4.1、(55) | $\sigma>1/2$ で $\infty$、$\sigma<1/2$ で0 | FALSE、全 strip の厳密反証、§3 |

## 2. 定義と量化

各正整数 $N$ と固定した $s=\sigma+it$ に対し、原文は

$$
S_N(s)=\sum_{n=1}^{N}n^{-s},\qquad
X_N(s)=S_N(s)+\frac12N^{-s},\qquad
Y_N(s)=\frac{N^{1-s}}{1-s}
$$

と定義している。$n^{-s}=\exp(-s\log n)$、$\log n$ は実対数。
その比は

$$
Q_N(s)=\frac{|X_N(s)|^2}{|Y_N(s)|^2}.
$$

監査範囲は $0<\sigma<1$、$s$ は $N$ と共に動かさない。$Y_N$ はこの範囲で常に非零。
Theorem 4.1 はこの ratio の一般的な漸近命題であり、statement に $\zeta(s)=0$ という追加仮定はない。
以下の反証には零点の探索・RH・確率モデル・数値的外挿を一切使わない。

## 3. 最小 cut: ratio は全 strip で1に収束する

**独立定理:** 任意の固定 $s$、$0<\Re s<1$ に対し、

$$
\boxed{\frac{X_N(s)}{Y_N(s)}\longrightarrow1,\qquad Q_N(s)\longrightarrow1.}
$$

Euler–Maclaurin や $\zeta$ の解析接続すら使わない証明を与える。
$f(x)=x^{-s}$ とすると

$$
S_N(s)-\int_1^N f(x)\,dx
=f(N)+\sum_{k=1}^{N-1}
\left(f(k)-\int_k^{k+1}f(x)\,dx\right).
$$

$|f'(u)|=|s|u^{-\sigma-1}$ だから

$$
\left|f(k)-\int_k^{k+1}f(x)\,dx\right|
\le\int_k^{k+1}\int_k^x |s|u^{-\sigma-1}\,du\,dx
\le |s|\int_k^{k+1}u^{-\sigma-1}\,du.
$$

従ってすべての $N\ge1$ で

$$
\left|S_N-\int_1^Nf\right|\le1+\frac{|s|}{\sigma}.
$$

$\int_1^Nf=Y_N-1/(1-s)$ と printed endpoint correction を戻せば

$$
|X_N-Y_N|
\le \frac1{|1-s|}+\frac32+\frac{|s|}{\sigma}.
$$

一方 $|Y_N|=N^{1-\sigma}/|1-s|\to\infty$。よって

$$
\left|\frac{X_N}{Y_N}-1\right|
\le\epsilon_N(s):=
\left[1+|1-s|\left(\frac32+\frac{|s|}{\sigma}\right)\right]
N^{\sigma-1}\longrightarrow0
$$

および

$$
|Q_N-1|\le2\epsilon_N+\epsilon_N^2\longrightarrow0.
$$

これで原文 (55) の両 off-center case は直接否定された。例えば $s=1/4$ でも $s=3/4$ でも limit は1である。
$t=0$ だけの特殊性を疑う場合も、同じ証明により $s=1/4+i$ と $3/4+i$ が反例になる。虚部を任意の固定された実数、既知零点の高度などに置き換えても証明は変わらない。

この結果は **零点ではない点でも相対的 balance が自動的に起こる**ことを示す。
極限 $Q_N\to1$ から零点や $\sigma=1/2$ を識別する情報は得られない。

### 実数の反例に対するさらに初等的な証明

$0<\sigma<1$ とすると単調積分比較により

$$
\frac{(N+1)^{1-\sigma}-1}{1-\sigma}
\le S_N(\sigma)
\le1+\frac{N^{1-\sigma}-1}{1-\sigma}.
$$

これを $Y_N(\sigma)=N^{1-\sigma}/(1-\sigma)>0$ で割るだけでも $X_N/Y_N\to1$ が従う。
従って反例 $s=1/4,3/4$ は高度な zeta 理論に依存しない。

## 4. Euler–Maclaurin による別の検証と端点符号

[DLMF 25.2.8–25.2.9](https://dlmf.nist.gov/25.2#iii) の表示、または原文自身の (13) から、固定 $s\ne1$、$\sigma>0$ に対して

$$
S_N(s)
=Y_N(s)+\zeta(s)+\frac12N^{-s}
+O_s(N^{-\sigma-1}).
$$

したがって正しい移項は

$$
\zeta(s)=S_N(s)-\frac12N^{-s}-Y_N(s)
+O_s(N^{-\sigma-1}),
$$

であり、原文 (15) の $+\frac12N^{-s}$ は誤り。
printed $X_N$ を保ったまま恒等式 $\zeta=X_N-Y_N+R_N$ を成立させるなら

$$
\boxed{R_N(s)=-N^{-s}+O_s(N^{-\sigma-1}).}
$$

$R_N=O_s(N^{-\sigma-1})$ ではない。実際 $N^sR_N\to-1$ に対し、主張された bound はその絶対値が $O_s(N^{-1})$ になることを要求してしまう。

また

$$
\frac{X_N}{Y_N}
=1+(1-s)\zeta(s)N^{s-1}+\frac{1-s}{N}+O_s(N^{-2}),
$$

なので再び任意の固定 $0<\sigma<1$ で ratio は1へ収束する。
**端点の plus を minus に修正しても、この主反例は消えない。**

## 5. Printed Bridge Lemma への独立攻撃

原文 p.8 の Lemma 3.1 は、$\zeta(\rho)=0$ なら

$$
|X_N(\rho)|^2-|Y_N(\rho)|^2\to0,
\qquad
|X_N(\rho)|^2-|Y_N(\rho)|^2=O(N^{-2\sigma})
$$

とする。しかし printed $X_N$ では、$\rho=\sigma+it$ を零点とすると

$$
X_N=Y_N+N^{-\rho}+O_\rho(N^{-\sigma-1}).
$$

二乗の cross term を保持すると

$$
\begin{aligned}
|X_N|^2-|Y_N|^2
&=2\Re\!\left(\overline{Y_N}N^{-\rho}\right)+O_\rho(N^{-2\sigma})\\
&=\frac{2(1-\sigma)}{|1-\rho|^2}N^{1-2\sigma}
+O_\rho(N^{-2\sigma}).
\end{aligned}
$$

特に任意の critical-line zero $\rho=1/2+it$ において

$$
\boxed{\lim_{N\to\infty}(|X_N|^2-|Y_N|^2)
=\frac1{1/4+t^2}>0.}
$$

critical-line zeros の存在は RH の仮定ではない（[DLMF §25.10](https://dlmf.nist.gov/25.10) もその無限存在を記録している）。従ってこれは実在する零点で printed Bridge Lemma を反証する。全零点が critical line 上にあると仮定する必要はない。

endpoint を minus に直した $X_N^-=S_N-\frac12N^{-s}$ なら、零点で $X_N^--Y_N=O_\rho(N^{-\sigma-1})$ となり Bridge の bound は修復できる。しかし §3–4 の全 strip ratio limit はその修正後も1であり、Theorem 4.1 の失敗は残る。

## 6. 最小推論エラーの位置

原文 p.10 の (47) は固定 $s$ に対し $|X_N|^2=O_s(N^{2-2\sigma})$、(44) は $|Y_N|^2=N^{2-2\sigma}/|1-s|^2$。
したがってこの2式だけでも $Q_N=O_s(1)$ が従い、同ページの (50) がいう $Q_N\to\infty$ と矛盾する。

さらに $1/2<\sigma<1$ において、原文の説明にある ordinary Dirichlet sum の収束は成立しない。上で証明した $S_N=Y_N+O_s(1)$ と $|Y_N|\to\infty$ が直接それを否定する。
$\sum n^{-2\sigma}$ の収束など、別の diagonal energy の収束を $\sum n^{-s}$ 自体の収束へ置き換えることもできない。

p.11 の Figure 4 は ratio の finite plot であって極限証明ではない。画像上は off-center curves も1付近に近づいて見えるが、その観察だけを反証根拠にはしていない。反証根拠は §3 のすべての $N$ に対する bound である。

## 7. 独立計算への read-only 監査

root が作成した [caceres_ratio_checks.py](../../../../artifacts/experiments/scripts/caceres_ratio_checks.py) を read-only で確認した。
5個の固定 $s$、4個の $N$ に対して、inclusive sum、printed plus endpoint、$Y_N$ の複素指数、Arb の ratio と §3 の elementary bound の確定比較は定義と整合している。
本担当による別の数値再実行は行っていない。有限値が極限の証明であるとは扱わない。著者コードの取得・実行もしていない。

本監査の厳密性は finite table の桁数に依存しない。§3 の elementary estimate と §4–5 の正しい Euler–Maclaurin expansion により、最小 cut は確定する。
この失敗した ratio criterion を別の未証明条件で延命することは今回の監査範囲外とし、この proof route はここで停止する。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/scripts/caceres_ratio_checks.py`](../../../../artifacts/experiments/scripts/caceres_ratio_checks.py)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/caceres-2609.28529v1.pdf` — SOURCE REFERENCE NOT INCLUDED
