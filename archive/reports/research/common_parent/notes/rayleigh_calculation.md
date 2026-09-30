**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/common_parent/notes/rayleigh_calculation.md` · Original SHA-256: `774d1a240a39482303220fb7a72a2b4f71cf227e35afb089dec9b260acc86b09`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Step 31: actual scoring と、得られた量の限界

2026-09-30。RH OPEN。有限データは証明ではない。

## 1. 算術から計算する式

[dictionary](../../common_variational_dictionary.md) の \(Q=Q_{\lambda,N}\) と
\(b=P_Nk_\lambda/\|P_Nk_\lambda\|\) を用いた。
同じmatrixにするために必要な射影を明示し、raw \(k_\lambda\) を偶化しなかった。
\[
 R_B=b^*Qb=R_{\rm pole}+R_\Gamma+R_{\rm prime},\qquad
 \varepsilon=R_B-e_0,\quad \Delta=e_1-e_0,\quad \eta=\varepsilon/\Delta.
\]
有限matrixの厳密なentriesはCCM §4および旧repoで既に監査された
prime-power finite sumとarchimedean積分で与えられる。
新scriptはその三成分を別々に組み立て、旧 \(c=13,N=4\) Arb行列と照合した。

oldの \(c\) は \(\lambda^2\) というprime-power cutoffであり、
prolateのparameter \(c_{\rm prolate}=2\pi\lambda^2\) とは違う。

## 2. 再現手順と数値の意味

- seed：orthonormal Legendre基底で
  \(P_c=-((1-y^2)h')'+c^2y^2h\) のeven blockをRitz近似。
- even block内のindex0,2がprolate次数0,4。各積分はLegendre定数係数から計算。
- mean-zero方向 \(h_4-(I_4/I_0)h_0\) を使う。各modeの任意スカラー変更に不変。
- seedを \(x=\lambda y\) へ戻し、有限整数和で \(k_\lambda\) を生成。
- log座標のjumpとその反転位置を全て積分分割点に含める。
- Legendre次数80→128、各segmentのGauss次数32→64、
  archimedean積分次数256→512で診断上の変動を確認。
- \(\lambda^2=2,3,5,9,13,25\)、\(N=4,8,16\) の18例。
- gapがdouble精度を下回るため9例を288-bit Arb assembly、75桁mpmathで再計算。
  そのtrial係数はdouble計算からの丸め値。proxy近似全体をinterval認証したわけではない。
  Arb行列もmidpointをmpmathへ渡すので、固有値・gap・score自体も区間認証ではない。

再実行は bundled Python（NumPyあり）で
research/common_parent/experiments/rayleigh_probe.py、
次に .venv-cert/bin/python で
research/common_parent/experiments/high_precision_scores.py を実行する。
旧scriptは関数をread-onlyでimportし、旧結果を上書きしない。
high-precision側はbytecode書込も無効にした。

## 3. 診断結果

次は高精度matrixと丸めtrialの値。掲載桁は比較の尺度を示すだけで誤差保証ではない。

| \(\lambda^2\) | \(N\) | \(e_0\) | \(R_B\) | \(\Delta\) | \(\varepsilon/\Delta\) | ground overlap squared |
|---:|---:|---:|---:|---:|---:|---:|
|2|4|\(1.73553\,10^{-3}\)|\(1.95493\,10^{-3}\)|\(1.03506\,10^{-1}\)|\(2.11972\,10^{-3}\)|0.99978990|
|3|4|\(3.05582\,10^{-7}\)|\(3.07328\,10^{-7}\)|\(5.32075\,10^{-5}\)|\(3.28082\,10^{-5}\)|0.99999995|
|5|4|\(9.04246\,10^{-11}\)|\(6.00467\,10^{-7}\)|\(1.58783\,10^{-8}\)|37.8112|0.99548421|
|5|8|\(4.57014\,10^{-15}\)|\(5.60528\,10^{-13}\)|\(2.20320\,10^{-12}\)|0.252341|0.99988509|
|9|8|\(1.78802\,10^{-20}\)|\(2.76804\,10^{-11}\)|\(8.69688\,10^{-18}\)|\(3.18280\,10^6\)|0.99470913|
|13|8|\(7.67439\,10^{-23}\)|\(8.19928\,10^{-10}\)|\(3.90717\,10^{-20}\)|\(2.09852\,10^{10}\)|0.98487843|

掲載 \(R_B\) の正確な表示値は
[high_precision_results.json](../../../../../artifacts/research/common_parent/experiments/high_precision_results.json) を正本とする。
いくつかの \(R_B\) は極小でもgapはそれ以上に小さい。
低いenergyだけでground proximityを認証できない。

大きな \(\eta\) は「距離が大きい」の下界ではない。
たとえば最後の行でもoverlap squaredは約0.985である。
それはこのgapを用いた一般上界が弱いことを意味する。
固定 \(N\) の悪化や有限パラメータの非単調性から、適切な同時極限の失敗を結論しない。

### precision gate

doubleのみの \(c=9,N=8\) では、gapがroundoffに埋もれground overlapの値まで壊れた。
これらは最初のJSONに gap_resolved_in_float64=false として残し、
結論にはhigh-precision再計算の方だけを用いた。
小さな負のdouble固有値をWeil不正値性やRH反例と扱っていない。

## 4. exact gap lemma

\(Q=Q^*\)、単位ground \(v_0\)、単純最小固有値 \(e_0\)、
\(e_1-e_0=\Delta>0\)、単位trial \(b\) とする。
固有vector展開 \(b=\sum c_jv_j\) から
\[
 \varepsilon=\sum_{j\ge1}(e_j-e_0)|c_j|^2
      \ge\Delta(1-|c_0|^2).
\]
従って
\[
 \operatorname{dist}(b,\mathbb Cv_0)^2\le\eta,\qquad
 \min_{|\omega|=1}\|b-\omega v_0\|^2
      =2(1-|c_0|)\le2\eta.
\tag{R}
\]
この補題は有限次元で完全であり、下に有界な自己共役作用素なら
form domainと孤立単純groundを指定して同じspectral measure証明が使える。

残差 \(r=(Q-R_B)b\) については、\(R_B<e_1\) の同定があれば
\[
 \|(I-P_0)b\|\le\frac{\|r\|}{e_1-R_B}.
\]
残差が0でもexcited stateであり得るため、lowest clusterへの同定を省略しない。
認証下界 \(\beta\le e_1\)、\(\beta>R_B\) があれば分母を \(\beta-R_B\) に弱められる。

## 5. \(\eta\to0\) と G* は同じではない

\(p=P_Nk_\lambda\)、\(c=\langle v_0,p\rangle\) とする。
投影scalarを許せば(R)から
\[
 \|cv_0-k_\lambda\|_2\le
 d_{\lambda,N}:=\|p\|_2\sqrt{\eta}+\|(I-P_N)k_\lambda\|_2.
\tag{R2}
\]
既知のscalar規格化で \(\widehat k_\lambda\to\mathscr X/4\) を用いる。
任意 \(r>0\) について
\[
 \sup_{|\Im z|\le r}|c\widehat v_0(z)-\widehat k_\lambda(z)|
 \le \left(\frac{\lambda^{2r}-1}{r}\right)^{1/2}d_{\lambda,N}.
\tag{R3}
\]
証明は \([-a,a]\) 上のCauchy–Schwarzと
\(\int e^{2r|t|}dt=(\lambda^{2r}-1)/r\)。
従って \(0<r<1/2\) 全てで右辺が0へ行けば、\(z_*=i/4\) の非零極限も使ってG*が出る。
単なる \(\eta\to0\) にはこの窓依存率もprojection tailも含まれない。
共通有限support内の \(L^2\) 収束を、増大するsupportでの複素一様収束と同一視しない。

raw proxyは小さいjumpを持ち得るので、根拠なく \(H^1\) Fourier-tail評価を使わない。
周期端点jumpを含めた全変動 \(V_\lambda\) を用いれば
\[
 \|(I-P_N)k_\lambda\|_2
       \le \frac{\sqrt{\log\lambda}}{\pi\sqrt N}V_\lambda
\]
が安全なBV評価。これを実際に(R3)の必要率まで評価する義務は残る。

## 6. 判定

Step31の有限代入とgap比較は実行した。
無条件の全パラメータalmost-minimizer bound、gap比の極限、
残差の算術的なrateは取得していない。
粗い下界、有限例のoverlap、prolate自身のleakageではこの不足を埋められない。
数値表を増やすだけの延長は行わない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/common_parent/experiments/high_precision_results.json`](../../../../../artifacts/research/common_parent/experiments/high_precision_results.json)
- [`research/common_parent/experiments/high_precision_scores.py`](../../../../../artifacts/research/common_parent/experiments/high_precision_scores.py)
- [`research/common_parent/experiments/rayleigh_probe.py`](../../../../../artifacts/research/common_parent/experiments/rayleigh_probe.py)
- [`research/common_variational_dictionary.md`](../../common_variational_dictionary.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/high_precision_results.json` — SOURCE REFERENCE NOT INCLUDED
