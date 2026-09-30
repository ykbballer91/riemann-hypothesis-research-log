**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/prime_jump_obstruction.md` · Original SHA-256: `08325ee41b0592ac257cdf990f3a46afdb3c98767c5e917970a8d38dfbc1aaf0`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 素数局所寄与の jump energy 化 — 対角発散の障害

状態: **限定候補を棄却**。RHはOPEN。本ノートは添付物理論文の式を使用しない。
新規性は主張しない。以下の恒等式は平行移動のユニタリ性の直接計算である。

## 正確な対象

対数座標で $\tau_a f(u)=f(u+a)$、$w_n=\Lambda(n)/\sqrt n$ と置く。
$f\in C_c^\infty(\mathbb R)$、$\operatorname{supp}f\subset[-L,L]$ とする。
内積は第一変数線形で、$\langle f,g\rangle=\int f\bar g$。
Weil形式の素数部分は

$$P_X(f)=2\sum_{2\le n\le X}w_n\operatorname{Re}\langle\tau_{\log n}f,f\rangle.$$

明示公式の規約では $Q_W(f)=B(f)-P_\infty(f)$。
$B$ は archimedean 項と極に由来する項の和であり、正値とは仮定しない。
固定した $f$ に対して $P_\infty=P_X$ は $X\ge e^{2L}$ で安定する。
これは零点側の高さ cutoff の話ではない。

一次資料: Connes–Consani, *Spectral triples and ζ-cycles* (2023),
[§2.1, (2.6)–(2.12), Proposition 2.1](https://ems.press/content/serial-article-files/44477?nt=1)。
同論文の乗法Haar座標から $u=\log x$ に移したもの。

## 仮説 SJ

「正の素数重みを持つ自然な差分エネルギーを足し上げれば、全Weil形式を
有限な非負エネルギーとして表し、正の残差だけで閉じられる。」

この候補を最も直接に定式化したものは

$$E_X(f)=\sum_{2\le n\le X}w_n\|\tau_{\log n}f-f\|_2^2,\qquad
Q_W(f)=\lim_{X\to\infty}E_X(f)+R(f),\quad R(f)\ge0.$$

ここでは $R(f)$ を有限値とする。この正確な候補はFALSE。

## 解析的反証

$S_X=\sum_{n\le X}w_n$ と書くと、ユニタリ性より

$$E_X(f)=2S_X\|f\|_2^2-P_X(f).$$

$\log n>2L$ では2つのsupportは交わらず、対応するエネルギーは
$2w_n\|f\|_2^2$。一方、素数上の部分和だけでも

$$S_X\ge (\log2)\sum_{p\le X}p^{-1/2}
\ge (\log2)\sum_{p\le X}p^{-1}\longrightarrow\infty.$$

最後はEulerの素数逆数和の発散を用いる。したがって非零の任意の $f$ について
$E_X(f)\to+\infty$。有限な $Q_W(f)$ との同一視は不可能。
正しい恒等式は、十分大きい $X$ に対して

$$Q_W(f)=E_X(f)+B(f)-2S_X\|f\|_2^2.$$

残差 $B(f)-2S_X\|f\|_2^2$ は $-\infty$ に向かう。
正のjump energyへの書き換えは、符号未定の相殺を別の場所に移しただけである。
有限エネルギーを得るにはrenormalizationが必要で、その正値性はこの恒等式から従わない。

この反証は、別の重み、別のHilbert空間、非局所の補正を持つすべての可能な
因数分解を否定するものではない。正確なSJ候補だけを棄却する。

## 数値反証と再現

`experiments/scripts/structural_falsification.py` は滑らかなbumpを $[-0.4,0.4]$ に置き、
L²ノルムを1とし、$X=2,10,100,1000,10000$ で恒等式の右辺を数値評価する。
出力は `experiments/results/structural_falsification.json`。
$E_X$ は約0.9801から394.9319へ増え、引くべき対角項も同じだけ増える。
差は約 $-0.00019197$ で安定する。binary64の非認証実験であり、上の解析的証明の代用ではない。

## RHとの関係・既知性・採用判定

- 重みが正であることは正定値核を意味しない。
  $\tau_a+\tau_{-a}$ のFourier multiplierは $2\cos(at)$ で符号が変わる。
  これは平行移動群の指標から導かれた式であり、原資料の任意の波形式ではない。
- 誤ったSJ候補はRHより容易な補題として採用しない。既知の明示公式と
  elementaryな差分恒等式の再導出として保管する。
- 演算子積の表記だけで正値性を宣言するルートは停止。
  なお $Q_W=A^*A$ の存在を抽象的に要求するだけなら、正値形式からの商空間構成と同値で、
  Weil基準によりRHそのものを再包装している。
- 添付論文はこのノートの数学的出典ではなく、主証明グラフへの依存辺は作らない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/structural_falsification.json`](../../../../artifacts/experiments/results/structural_falsification.json)
- [`experiments/scripts/structural_falsification.py`](../../../../artifacts/experiments/scripts/structural_falsification.py)
