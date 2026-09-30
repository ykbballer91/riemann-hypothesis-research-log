**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/nyman_beurling_closure_gate.md` · Original SHA-256: `bc4c2e107e717b25b7e63ad5669544a84468f84d383d5e30a0a19a971b8083cf`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Nyman–Beurling: positive increment と closure の分離

2026-09-29。discovery resetの比較。既知criterionの整理であり、新しいRH証明入力ではない。

[Báez-Duarte 2003](https://arxiv.org/abs/math/0202141) の自然数dilationによるcriterionと、
[Bettin–Conrey–Farmer 2012, Introduction/Theorem 1](https://arxiv.org/pdf/1211.5191) を確認した。
後者の最適Möbius重み付き近似はRHと負のzero-derivative momentの仮定を使う。
その上界を無条件の入力として採用できない。自然な無重みMöbius列の収束も仮定しない。

## Exact positive decrement は最初から存在する

H=L²(R,dt/[2π(1/4+t²)])、v_n(t)=ζ(1/2+it)n^(-1/2-it)、
V_N=span{v_1,...,v_N}、P_Nを直交射影、r_N=1−P_N1とする。
各v_nは無条件の通常のζ成長評価からHに属する。有限のv_nは線形独立なのでGram行列は正定値。
この同じ無限Hilbert空間の正確な入れ子の部分空間について

\[
e_{N+1}=(I-P_N)v_{N+1},\qquad
d_N^2=\|r_N\|^2,\qquad
d_N^2-d_{N+1}^2
=\frac{|\langle r_N,e_{N+1}\rangle|^2}{\|e_{N+1}\|^2}\ge0.
\]

これはGram行列のSchur complementと同じ射影恒等式。新規性なし、RH不要。
任意のcountertermも、有限データからの極限推測も使わない。

しかし全Nの正増分、正Gram pivot、exact restrictionだけではd_N→0を強制しない。
反例はH=ℓ²({0,1,...})、v_n=e_n (n≥1)、target=e_0+Σ_{n≥1}2^(-n)e_n。
ここでは全innovation normが1、各decrementは4^(-N−1)>0なのに、d_N²→1。
この模型はζの反例ではなく一般的伝播推論の反例。

## 必要な新入力

ζ固有のinnovation sumがtargetの全normを回収すること、すなわちd_∞=0が未解決。
単にこの条件を「完全性」「保存」「散逸」「cyclicity」と呼び直すのはRH同値変形なので棄却する。
あらかじめ独立に指定・証明された定量boundにより
decrement≥c_N d_N²、0≤c_N≤1、Σc_N=∞を示せれば閉じるが、そのような算術評価は得ていない。
この十分条件がRHより弱いと主張しない。c_Nを実際のdecrement/d_N²と定義して済ませることも禁止。

**判断:** この枠組みにはcanonicalな正増分はあるが、現在の入力だけではclosureを埋めない。
新しい独立な算術評価なしにfinite Gram表を拡大しない。主graph mergeは0。
