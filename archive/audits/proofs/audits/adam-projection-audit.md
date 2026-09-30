**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/adam-projection-audit.md` · Original SHA-256: `12fc619da39bcab660962a84135e742b07c26db0aca00f309c9fae46a0527a56`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Adam v4 — 近似作用素の最小cut監査

2026-09-29。DIRECT候補の判定: **REJECTED_FATAL_COUNTEREXAMPLE_TO_LEMMA_1**。
RHそのものへの反例ではない。主グラフ合流0、証明距離の短縮なし。

一次資料: Dumitru Adam,
[On the Method for Proving RH Using the Alcantara-Bode Equivalence (II), v4](https://www.preprints.org/manuscript/202601.0459/v4)。
v4公開2026-09-09。版URLは取得時に版なしURLへ転送されたため、本文の版表示も照合した。
Webツール抽出応答を `literature/source_cache/adam-202601.0459v4.web.json` に保存。
SHA256 `f4923774fc4ef3d9454e670b337a4020312a9d0675f569a0e6c2282ecec90b0f`。
HTML原本またはPDFを取得したとは扱わない。

監査範囲は §3.1 Eq.(7), Note 2, Lemma 1 と、それを使う Theorem 4。
全文の全主張を検証したとはしない。各原主張は PROVED-IN-PAPER=YES、
Lemma 1 の収束について INDEPENDENTLY-VERIFIED=FAILED-AS-STATED。
反例および下記の修復障害は ROOT/BUILDER/DESTROYER が独立確認し、LITERATUREが本文を照合した。

## 固定した一関数による厳密反例

\(H=L^2(0,1)\)、\(\rho(y,x)=\{y/x\}\) とし、
\[
(Tu)(y)=\int_0^1\rho(y,x)u(x)\,dx.
\]
dyadic mesh \(h=2^{-m}\) のセル指示関数を \(I_{h,k}\) と書く。
論文 Eq.(7) が定める核を文字通り使うと
\[
\rho_h(y,x)=h^{-1}\sum_k I_{h,k}(y)\rho(y,x)I_{h,k}(x).
\]
これは異なるセルの間の結合をすべて消している。

\(u=\mathbf1_{(1/2,1)}\) を一度だけ固定する。全dyadic \(h\le1/2\) で
\(0<y<1/2\) に対し
\[
T_hu(y)=0,\qquad Tu(y)=\int_{1/2}^1 y/x\,dx=y\log2.
\]
したがって
\[
\|(T_h-T)u\|_2^2\ge (\log2)^2\int_0^{1/2}y^2\,dy
=\frac{(\log2)^2}{24},\quad \|u\|_2^2=\frac12,
\]
\[
\boxed{\ \|T_h-T\|\ge \frac{\log2}{\sqrt{12}}>0\quad(h\le1/2).\ }
\]
作用素ノルム収束だけでなく、この固定した \(u\) に対する強収束も成立しない。
Lemma 1.1 が偽なので、それに依存する Theorem 4 の証明は成立しない。
反例は実際の \(\{y/x\}\) 核を使い、一般の別核への置換ではない。

Arb 192bit の補助数値確認:
\(\log2/\sqrt{12}\in[0.200094355642157279524183908673122107962209768370359725688
\pm3.28\cdot10^{-58}]\)。解析反例自体はこの数値を必要としない。
再実行: `.venv-cert/bin/python` で
`from flint import arb,ctx; ctx.prec=192; print(arb(2).log()/arb(12).sqrt())`。
窓拡大や零点の有限表は使用していない。

## 誤った極限と定義の区別

標準直交射影 \(P_h\) は各 \(u\) について \(P_hu\to u\) を満たすが、
有限次元の真部分空間への射影なので \(\|I-P_h\|=1\) である。
例えば一セルの前半と後半で符号を変え、正規化したHaar関数がその等号を実現する。
Note 2 の強収束からノルム収束への推論は誤り。

さらに正の左端点を持つセル \((a,b)=((k-1)h,kh)\), \(k\ge2\) では、
ほとんど至る所 \(\{y/x\}=y/x-\mathbf1_{x\le y}\) だから
\[
T_hf(y)=h^{-1}\left(y\int_a^b\frac{f(x)}x\,dx-\int_a^y f(x)\,dx\right).
\]
セルへの制限は階数1作用素と無限階数Volterra作用素との差。
従って Eq.(7) 自体は有限階数ではなく、\(S_h\) を \(S_h\) へ写すとも限らない。
有限圧縮の対角二次形式を、この作用素全体と混同してはならない。

Theorem 1 は共通 \(\alpha>0\) の下界を明記している。
それを単なる各点での正値性と読み替えて反証しない。
ノルム収束と共通下界を仮定する一般的な単射性の十分条件自体は、ここでの反例対象ではない。

## 最小修復を試すと何が残るか

正しい圧縮 \(K_h=P_hTP_h\) なら、\(T\) がHilbert–Schmidtでコンパクトであることから
\[
\|T-K_h\|\le\|(I-P_h)T\|+\|(I-P_h)T^*\|\longrightarrow0.
\]
これは有限次元近似により直接証明できる標準的なコンパクト作用素の事実。
ただし Eq.(7) とは別の定義である。

\(d_{ij}^h=\int_{\Delta_i}\int_{\Delta_j}\rho(y,x)\,dx\,dy\) と書くと、
正規直交基底 \(e_{h,k}=h^{-1/2}I_{h,k}\) に関する正しい圧縮行列は
全セル対を含む \(h^{-1}d_{ij}^h\)。最初のセルだけでも
\[
\langle K_he_{h,1},e_{h,1}\rangle
=h^{-1}d_{11}^h=h\frac{3-2\gamma}{4}\to0.
\]
最後の積分値は、変数変換 \(t=y/x\) と
\(\int_1^\infty\{t\}t^{-2}dt=1-\gamma\) により
\(\int_0^1\{y/x\}\,dx=y(1-\gamma-\log y)\) を積分して得られる。

論文 Eq.(9)–(10), Theorem 4A の \((3-2\gamma)/4\) は、
文字通りの \(T_h\) の二次形式に対する \(h^{-2}\min_k d_{kk}^h\) である。
正しい圧縮、または \(T^*T\) の共通下界ではない。

一般にも、稠密な増大部分空間に共通の
\(\operatorname{Re}\langle Tf,f\rangle\ge\alpha\|f\|^2\), \(\alpha>0\)
があれば、連続性で全空間へ延び、Cauchy–Schwarzから \(\|Tf\|\ge\alpha\|f\|\)。
これは無限次元のコンパクト作用素では不可能: 正規直交列 \(f_j\rightharpoonup0\)
に対してコンパクト性は \(Tf_j\to0\) を強制する。
正しい \(Q=T^*T\) もコンパクトなので、同じ共通下界の修復はできない。

分類: 近似の定義は収束だけなら REPAIRABLE。しかし必要な共通下界は
修正後の実作用素について FATAL。非一様な下界から単射性を導く新しい独立評価は得ていない。
コンパクト単射作用素は存在するため、この障害は \(T\) の非単射性やRH否定を意味しない。
この近似ルートは終了し、有限行列を大きくする作業へ進まない。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/adam-202601.0459v4.web.json` — SOURCE REFERENCE NOT INCLUDED
