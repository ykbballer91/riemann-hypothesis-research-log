**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/rate_history_selection_adversarial.md` · Original SHA-256: `4abc2f83fe3149a5fec675fe85c362d6e7e40aaea5f808016b97ad1061a85aa9`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Rate/history selection の独立敵対監査

2026-09-30。RH は OPEN。本ファイルのみが今回の編集対象であり、既存375ファイル、旧監査、主 proof graph、Git を変更しない。対象は `research/rate_history/charter.md` の三機構である。以下の有限模型は実 Weil 形式の反例でも、RH の反例でもない。

## RH1. 線形試験空間と正規化写像 — PASS / 条件を固定

元の Hilbert 内積を固定し、実現済み列を \(f_0,\ldots,f_{m-1}\)、線形写像を

\[
Sc=\sum_jc_jf_j,\qquad G=S^*S,\qquad M_{ij}=Q(f_i,f_j)
\]

とする。ここでは sesquilinear 形式は第1変数反線形とし、\(Q(Sc,Sc)=c^*Mc\) を用いる。線形独立なら

\[
\mathcal R(c)=\frac{c^*Mc}{c^*Gc},\qquad Mc=\mu Gc.
\]

列を個別に正規化する操作は固定された対角基底変更なので、**両方の行列を**変換すればよい。他方

\[
c\longmapsto \frac{Sc}{\sqrt{c^*Gc}}
\]

は非線形である。正規化された和の energy を元の二次形式の値と取り違え、通常の polarization を適用してはならない。各列の norm を1にしても、一般に \(G\ne I\) である。

可逆な基底変更 \(S\mapsto ST\) に対して

\[
(M,G)\mapsto(T^*MT,T^*GT),\qquad c\mapsto T^{-1}c
\]

となる。一般化固有値と物理的直線 \(\mathbf CSc\) は不変だが、通常の \(M\) の固有値、係数の大きさ、係数比の収束速度は不変でない。パラメータ依存の列スケールを状態選択と数えてはならない。

\(G\) が特異なら \(\mathbf C^m/\ker S\) を用いる。真の pullback 形式なら \(M\ker S=0\) である。数値上これが破れる場合は、丸め誤差または不整合な行列組立を検査する。列数が実現先の次元を超える場合は特異性が必然である。

Cholesky 規約にも依存する。\(G=LL^*\) が lower Cholesky なら

\[
H=L^{-1}ML^{-*},\qquad c=L^{-*}x;
\]

\(G=R^*R\) が upper Cholesky なら \(H=R^{-*}MR^{-1},c=R^{-1}x\) である。\(G^{-1}M\) は通常の Euclidean 内積について Hermitian とは限らない。

## RH2. Gram の悪条件性 — 厳密反例 / 数値監査条件

元の空間を \(\mathbf C^2\)、元の内積を通常のものとし、

\[
f_0=e_1,\quad f_1=e_1+\varepsilon e_2,\quad
A=\operatorname{diag}(1,-1)
\]

を取る。このとき

\[
G=\begin{pmatrix}1&1\\1&1+\varepsilon^2\end{pmatrix},\qquad
M=\begin{pmatrix}1&1\\1&1-\varepsilon^2\end{pmatrix}.
\]

一般化固有値は全 \(\varepsilon>0\) で厳密に \(+1,-1\)。しかし \(\det G=\varepsilon^2\)、\(\kappa(G)\sim4/\varepsilon^2\)。行列要素の \(O(\varepsilon^2)\) 差を失うだけで、物理的に norm 1 の方向を消してしまう。微小な差の存在を無視して「実質 rank 1」とする判定は別の問題を解いている。

誤差は元の Gram に相対化する必要がある。正確な \(G>0\) に対して

\[
E=G^{-1/2}(\widetilde G-G)G^{-1/2},\quad
F=G^{-1/2}(\widetilde M-M)G^{-1/2},\quad
H=G^{-1/2}MG^{-1/2}
\]

とし \(e=\|E\|<1,f=\|F\|\)。近似一般化固有値は

\[
B=(I+E)^{-1/2}(H+F)(I+E)^{-1/2}
\]

の固有値であり、

\[
\|B-H\|\le\frac{f+e\|H\|}{1-e}.
\]

これは \(\|(I+E)^{-1/2}\|\le(1-e)^{-1/2}\) と積の差の評価から得る。固有方向にはさらに該当 gap より小さい誤差が必要である。多倍長の midpoint 計算だけでは、この相対誤差の保証にはならない。Gram への ridge、固有値の floor、方向の切り捨ては、正当化を別に示さない限り元の試験問題を変更する。

## RH3. Rate A / B / C の論理的分離

**A: signed defect。** \(Q(Tf,Tf)\to0\) は、正規化前なら単に norm が0へ縮むことでも起こる。unit norm に限っても \(A=\operatorname{diag}(-1,1)\)、\(w=(e_1+e_2)/\sqrt2\) なら \(Q(w)=0\) だが ground energy は \(-1\)。正負の相殺と radical recognition を ground recognition と同一視しない。符号を捨てた \(|Q|\) の最小化も別の問題である。

**B: ground excess。** 単純 ground energy \(e_0\)、次の energy \(e_1\)、\(\Delta=e_1-e_0>0\) が既知なら、unit trial \(w\) に対して

\[
\eta=\frac{Q(w)-e_0}{\Delta}\ge0,\qquad
\|(I-P_0)w\|^2\le\eta.
\]

位相を揃えた ground との距離は高々 \(\sqrt{2\eta}\)。分子が0へ行くだけでは、gap も0へ行く場合に結論はない。有限 radical 試験空間での最低固有値と、同じ \((\lambda,N)\) の **全** Weil head の ground/gap も区別する。これは旧 common-parent 監査の既知補題の再使用であり、新発見ではない。

**C: value-normalized transform。** support が \([-a,a]\) の \(L^2\) 関数の Fourier 評価の norm は

\[
M_a(r)=\left(\frac{\sinh(2ar)}r\right)^{1/2}\ (r>0),\qquad
M_a(0)=\sqrt{2a}.
\]

従って \(a\to\infty\) では \(L^2\) 距離だけで固定の複素 compact 上の transform 比を制御できない。unit vectors \(v,w\) の位相を揃え、距離 \(d\)、基点 \(z_*=i/4\)、\(\kappa=|\widehat w(z_*)|>0\) とする。\(dM_a(1/4)\le\kappa/2\) なら、\(K\subset\{|\Im z|\le r\}\) 上で

\[
\sup_K\left|\frac{\widehat v(z)}{\widehat v(z_*)}
-\frac{\widehat w(z)}{\widehat w(z_*)}\right|
\le\frac{2d}{\kappa}\left(M_a(r)
+M_a(1/4)\sup_K\left|\frac{\widehat w(z)}{\widehat w(z_*)}\right|\right).
\]

これは十分条件であり、実際の特殊関数族に対する必要条件だとは主張しない。一般的な countermodel に actual spectral determinant の全実零点性まで備わっているとも主張しない。Rate A、Rate B、Rate C を同じ「速さ」として順位付けしてはならない。

## RH4. 退化と許容経路だけから選択は出ない — 厳密有限模型


\[
a=\log\lambda\to\infty,\quad N\in\mathbf N,\quad
G_{a,N}=I_2,\quad M_{a,N}=\operatorname{diag}(a^{-2},N^{-1}).
\]

元の内積は固定され、恣意的な測度の選択はない。全ての共同極限 \(a,N\to\infty\) で行列は norm で0へ収束する。しかし

* \(N=\lceil a^{3/2}\rceil\) では ground は \(e_1\)。
* \(N=\lceil a^3\rceil\) では ground は \(e_2\)。

どちらも、旧 spectral approximant 監査の必要条件 \(N/a\to\infty\) を満たす。各経路上では十分大きい \(a\) において ground は単純で、両方の固有値は0へ消える。二経路を交互に取れば ground は収束しない。

従って「退化した同じ極限形式＋許容経路＋vanishing energy」は普遍的な状態選択を与えない。この模型は actual Weil の経路依存を証明しないし、全ての次次数選択原理を否定しない。

反対に、固定された物理的同定で

\[
G_j\to G>0,\qquad r_j^{-1}M_j\to H,\quad r_j>0,
\]

かつ \((H,G)\) の最低固有値が単純なら、一般化固有方向はその直線へ収束する。これが有限次元で有効な選択の十分条件である。実際の主張にはスケール \(r_j\)、符号を含む **全行列** \(H\)、単純性、およびその gap より小さい remainder を示す必要がある。各対角値の減衰の plot や \(M_j\to0\) だけでは代用できない。固定 \(m\) の結論を \(m\to\infty\) へ自動的に延長しない。

## RH5. 端点依存と経路の履歴は別 — PASS / 限定

固定 \((\lambda,N)\)、固定された実現写像 \(S_{\lambda,N}\)、元の内積が決まれば、\(M,G\) は現在の端点から決まる。単純 ground の直線も同様である。有限和の項の計算順、対角化の warm start、固有ベクトルの符号選択は、その形式自体に数学的な記憶を追加しない。

異なる共終経路で極限が違うことは、有限端点の履歴依存とは異なる。縮退点での枝追跡にも追加の規約が必要である。Berry phase や符号変化だけでは物理的固有直線は変わらない。非可換な truncation/projection を異なる順で適用して最終写像が違えば、それは端点の定義を変更した比較である。

本来の history mechanism を採用するには、進化・transport・初期データ・同定と、その近似誤差を別途指定しなければならない。これらは今回の canonical endpoint family から自動生成されない。係数 plot ではなく、共通の log 空間での埋め込み、または明記した unitary dilation により物理的方向を比較する。

## RH6. Prime-power threshold の新項 — 独立再計算 PASS

固定 head 次元で \(L=2\log\lambda\)、\(n=p^k\)、\(h=\log n\)、\(W=\Lambda(n)/\sqrt n\) とする。基底を

\[
V_j(t)=L^{-1/2}\exp\!\left(2\pi ij\frac{t+L/2}{L}\right)
\]

とすれば両端の値は全 \(j\) で \(1/\sqrt L\)。新しい prime correlation は \(L\le h\) で0、\(L=h+\delta\) で overlap 長 \(\delta\)。従って新項は

\[
Q_n(L)=-\frac{2\Lambda(n)}{\sqrt n\,h}\,\delta\,\mathbf1\mathbf1^*
+O(\delta^2).
\]

行列そのものは threshold で **連続**。新項による右微分と左微分の差は

\[
[\partial_LQ_n]_{h}=-\frac{2\Lambda(n)}{\sqrt n\log n}\mathbf1\mathbf1^*
=-\frac2{k\sqrt n}\mathbf1\mathbf1^*.
\]

\(\partial_\lambda L=2/\lambda\) より

\[
[\partial_\lambda Q_n]_{\lambda=\sqrt n}
=-\frac4{kn}\mathbf1\mathbf1^*.
\]

独立の entry 検算でも、対角新項
\(-2W(1-h/L)\cos(2\pi jh/L)\) の右微分は \(-2W/h\)。非対角新項

\[
-W\frac{\sin(2\pi jh/L)-\sin(2\pi \ell h/L)}{\pi(\ell-j)}
\]

も同じ微分を与える。最後の式の \(j,\ell\) は基底添字であり、prime power の記号 \(n\) と区別する。

無シフト基底なら端点の符号 \((-1)^j\) が入り、\(\mathbf1\mathbf1^*\) はその符号ベクトルの outer product になる。prime power でない整数には \(\Lambda(n)=0\) でこの新項はない。

これは新項の微分 kink であり、全 \(Q\) の単調性、\(Q\) の負方向、固有状態の不連続、履歴の存在を意味しない。実現列が parameter に依存する \(M=S^*QS\) には \(S'\) の項もあり、\(G'\) と合わせて扱う。固定次元で単純固有値の gap が保たれるなら、連続な行列族の固有直線も連続である。\(N\) を変える次元イベントとは別の問題。

## RH7. 現時点の判定と追加監査範囲

* **PASS:** 一般化行列の合同不変性、A/B/C の分離、上記 prime-power 新項の連続性と微分係数。
* **REJECT:** 正規化後の写像を線形と扱うこと、Gram を無視した選択、消える energy のみから ground/transform/普遍経路を結論すること、端点の kink を履歴と呼ぶこと。
* **CONDITIONAL:** 安定した Gram と一様に制御された次次数行列に単純 minimum がある場合の方向選択。
* **OPEN:** actual Weil radical-family の全 support＋projection defect の次次数、許容共終経路に一様な remainder、actual state と \(k\) / prolate proxy の同定。

root の数値 script、boundary asymptotics、history note の完成後に、このファイルへ限定した追加監査を追記する。現時点でそれらを読了・認証済みとはしていない。

## RH8. 実際の M/G 計算 — 静的監査 PASS / 非認証

読取対象は新規 research/rate_history/experiments/splitting_probe.py、proxy_trials.py、途中結果を含む splitting_results.json と prolate_trials.json。既存 Weil matrix helper は定義を照合しただけで変更・再実行していない。今回の独立確認で full matrix の Arb 積分を再実行したとは主張しない。

確認した実装の規約は次の通り。

* \(k(t)=e^{t/2}\sum_{n\ge1}(y^2-\tfrac32y)e^{-y}\), \(y=\pi n^2e^{2t}\), \(t\ge0\)。多項式 recurrence は \(P\mapsto(\tfrac12+2y\partial_y-2y)P\) であり、実装は \(k,k'',k^{(4)},k^{(6)}\) に一致する。偶延長と正の半区間の2倍積分は整合している。
* Fourier 係数の \((-1)^n\)、正負添字で等しい実係数、\(1/\sqrt{2a}\) は shifted basis の射影と一致する。
* 個別列正規化後にも \(G=S^TS\) を保持し、\(M=S^TQS\) と lower Cholesky で一般化固有問題を解く。RH1 の合同変換と一致する。
* 選択された有限係数を元の derivative basis へ戻す alpha=c/norms は正しい。その後、別途近似した全実線 Gram によって物理的な global vector を正規化している。finite projection の unit vector と global derivative combination を別々に比較している。
* 真の全 head ground の試験部分空間への射影 norm は \(\mathrm{rhs}^TG^{-1}\mathrm{rhs}\)。単一の選択状態との overlap と区別されている。
* raw prolate proxy との比較は複素係数の Hermitian 内積を用いる。これは inversion-even proxy を作ったことを意味しない。

読取時点の11ケースでは、Gram condition は約 \(3.87\) から \(1936\)、144点と192点の列係数差の最大値は約 \(6.2\times10^{-51}\)。100桁の固有残差は、組み立てた midpoint matrix の固有方程式を解いた精度であり、積分誤差や Arb ball の半径、真の gap の下界を認証しない。二つの積分次数の一致も区間評価ではない。

global_gram() は初読時 \([-4,4]\) と192点積分による近似だった。追加確認で256点へ更新され、192点との差約 \(3.97\times10^{-37}\) と、全実線 Gram の厳密 enclosure ではないという scope が JSON に記録された。この指摘は **RESOLVED**。theta tail が極小であることと、quad remainder が厳密に囲まれたことは別であり、更新後も「high-precision diagnostic / not certificate」という分類が正しい。proxy はさらに浮動小数点による比較である。

今回の数値値から、実際の無限経路上の選択・安定性・速度・一意性は結論しない。有限試験部分空間の minimum と全 head の gap を両方保存している点は、Rate A と B の混同を防いでいる。

## RH9. Ground trajectory / probability gate — 数式 PASS

research/ground_state_trajectory.md 全文、および新規 trajectory_diagnostics.py、prime_event_probe.py を読んだ。そこから参照する Kato 等の原典全文をこの独立監査で再読したとは主張しない。主張に使う有限次元の式は独立計算した。

* 固定区間への unitary dilation と、元の log-space への零延長は異なる比較である。固定 kernel の dilation 像が弱収束0し、rank-one projectors が strong operator topology で0へ行く計算は正しい。その現象を kernel の算術的消滅と呼ばない。
* prime corner の式(5)–(6)は RH6 と一致する。odd sector の係数和が0であるため一次 corner が消えるが、全 ground の偶性にはならない。
* reduced resolvent を使う \(P_0'=-SQ'P_0-P_0Q'S\)、gap 下界を伴う integral estimate、one-sided Hellmann–Feynman は、単純 isolated ground という明記された前件の下で正しい。次元イベントにこの微分公式を直接適用していない。
* 固定有限個の even \(f_j\) に対する周期 integration by parts は \(f_j(a)=f_j(-a)\) で端点項が消え、本文(11)の \(L/[2\pi(N+1)]\) を与える。従って \(N/L\to\infty\) で元の \(L^2\) Gram が正定値極限へ行く。sharp cutoff の全実線 weak derivative が \(L^2\) だとは仮定していない。この証明から energy convergence は出ないという限定も正しい。
* probability-valued spectral measure の scalarization には vector が必要。finite heat state の error bound \((d-1)e^{-\beta\Delta}\) は正しいが、新しい arithmetic selector ではない。縮退時の低温極限は ground projector を rank で割ったものであり、vector の選択ではない。
* trajectory script の cross-window integral は、共通 support 上の sinc 積分と shifted phase \((-1)^{n-m}\) に一致する。有限 endpoint の違いから無限 path limits の違いを断定していない。

初読時の本文§4だけが診断経路を \(\max(6,\lceil a^2\rceil)\)、\(\max(6,\lceil a^3\rceil)\) と記していた。script/JSON の \(\max(4,\ldots)\) へ訂正済みで、この指摘は **RESOLVED**。これは経路ラベルの整合問題であり、上記解析的補題の反証ではない。

## RH10. 実際の support-only defect — 独立解析 PASS

research/rate_history/notes/boundary_rate_analysis.md 全文を読取監査した。以下は actual theta/Weil の support-only 成分に対する独立検算であり、有限 Fourier 射影を含む全 defect を証明したものではない。

### Domain と radical の使用

全 exponential weight に対する \(L^1,L^2\) と weighted variation を課す BR6 は、sharp tail と有限 Fourier 多項式の零延長を含む。jump は測度微分に残る。strip 上の部分積分は一様な \(O((1+|\Re z|)^{-1})\) を与えるので、Weil spectral series の積は \(O((1+|\gamma|)^{-2})\)。零点計数により絶対可算である。

weighted \(L^1,L^2\) 収束と一様 weighted variation を持つ smooth compact 近似に対し、spectral、archimedean、pole、prime の全項が優収束する。prime 側の
\[
|C_f(d)|\le e^{-b|d|}\|e^{b|x|}f\|_2^2,\qquad b>1/2,
\]

は三角不等式と Cauchy–Schwarz から得られ、全 prime sum の domination に十分である。このため sharp extended test class における \(Q(f_j,g)=0\) と \(Q(R_af_j)=Q((I-R_a)f_j)\) は正当である。global \(L^2\) 閉形式も RH も前提にしていない。

### 主係数と全 prime tail

\(Y=\pi e^{2a}\)、\(\beta=2Y\)、\(A_j=f_j(a)\) とする。独立に微分 recurrence の先頭二係数を確認し、
\[
A_j=4^j\pi^{-1/4}Y^{2j+9/4}e^{-Y}(1+O_j(Y^{-1}))
\]

を得る。片 edge の profile \(F_{j,a}(v)\to e^{-v}\) と Fourier profile \((1+i\xi)^{-1}\) から、片側の arch energy は
\[
\frac{A_j^2}{2\beta}\log\frac{\beta}{2\pi}
+o(A_j^2/\beta).
\]

両側を加え、距離 \(2a\) の cross kernel \(-w(|x-y|)\) を評価すると、主項は
\[
\frac{A_j^2}{\beta}\log\frac{\beta}{2\pi}
=\frac{A_j^2}{2Y}\,2a.
\]

ここで \(w(v)=e^{-v/2}/(1-e^{-2v})\)。cross の符号・係数と \(O(e^{-a}A_j^2/\beta^2)\) を確認した。pole は \(O(A_j^2/Y^{3/2})\)。

反対側 tails の prime correlation は \(d=2a+\delta\) で初めて入り、overlap 長 \(\delta\) を保持する必要がある。本文の \(\delta e^{-Y\delta}\) による
\[
\sum_{n>X}\frac{\log n}{\sqrt n}\log(n/X)(n/X)^{-Y}
=O(\log Y/Y^{3/2}),\qquad X=Y/\pi
\]

は整数 \(X\) の直前・直後にも一様である。\(X<n\le2X\) で \(r=n-X\) とすれば、整数間隔の和 \(\sum r e^{-\pi r/2}\) が一様有界だからである。prime distribution の強い評価を隠れた前提にしていない。同側 tails はさらに指数的に小さい。従って BR16 の \(2a+o(1)\) と明示係数は整合する。

### 線形結合による境界消去

交差項も同じ profile を持ち、先頭の境界行列が rank 1 になる点を確認した。これは元の Gram を恒等行列とする操作ではない。

特に
\[
g_a=k-\frac{k(a)}{k''(a)}k'',\qquad
\frac{k(a)}{k''(a)}=\frac1{4Y^2}
\left(1+\frac{11}{2Y}+O(Y^{-2})\right)
\]

について \(g_a\to k\) in global \(L^2\) だが、
\[
\frac{Yg_a(a+v/\beta)}{k(a)}\to-2ve^{-v},\qquad
\int_0^\infty4v^2e^{-2v}dv=1.
\]

従って正規化の前後とも
\[
\frac{Q(R_ag_a)}{Q(R_ak)}\sim\frac2{Y^2}.
\]

元の profile の片側質量は \(1/2\) なので、比の係数2も正しい。新しい profile の logarithmic Fourier moment は
\[
\frac1{2\pi}\int_{\mathbb R}
\log|\xi|\frac4{(1+\xi^2)^2}\,d\xi=-1,
\]

であり0ではない。ただし BR27 は先頭の \(\sim\) だけを主張し、この定数項を0だとしていないので問題はない。「\(k\) 単独より速い組合せ」と「極限で \(k\) と異なる状態」は区別されている。この例自身の global limit は \(k\)。

### 射影と三つの rate

BR29 の periodic endpoint expansion、BR31 の
\[
\|(I-P_N)R_af\|_2^2\sim
\frac{4a^3|f'(a)|^2}{3\pi^4N^3}
\quad(a\ \text{fixed})
\]

の係数を確認した。\(N/a\to\infty\) だけでは \(N/(aY)\to\infty\) にはならず、固定 \(a\) の remainder を共同極限へ代入していない。support-value cancellation の係数 \(11/2\) と derivative cancellation の \(15/2\) は異なる。

radical 恒等式による全 defect の正しい分解は
\[
Q(P_NR_af)=Q(r)+2\Re Q(r,p)+Q(p).
\]

混合項の符号は正しい。RH 未仮定なので positive-form Cauchy–Schwarz で混合項を捨てられない。右辺の noncompact tail に含まれる大きな prime shift を、別の missing-prime error として加えるのは二重計上になる。値正規化の分母、特に derivative の全実線 transform が0で消える点についても限定は正しい。

**判定:** BR16、BR24、BR27 は actual arithmetic の解析的 subcomponent として PASS。全 canonical \(P_NR_a\) の rate、全 span の最速方向、ground/gap、prolate 同定、path independence はここからは出ない。

## RH11. Full projection の無条件上界 — 独立解析 PASS

追加稿 research/rate_history/notes/full_projection_upper_bound.md 全文と式(1)–(19)を独立検算した。この結果は、support-only 漸近とは別に full \(T_{a,N}=P_NR_a\) の **上界** を与える。両者を混同しない。

固定 \(m\)、\(a\ge1\)、\(\Omega=\pi(N+1)/a\ge1\) に対し、同稿の上界は
\[
|Q_W(Tf_i,Tf_j)|\le C_m\left[
a(1+\Omega)^{4m+8}e^{a-\pi\Omega/2}
+\lambda^{8m+24}e^{-2\pi\lambda^2}\right],
\qquad i,j\le m.
\]

以下の鎖を確認した。

1. unconditional Euler summation からの粗い \(\zeta(1/2+it)=O(1+|t|)\) と Gamma factor によって、\(|\widehat f_j(\omega)|\le C_m(1+|\omega|)^{2m+3}e^{-\pi|\omega|/4}\)。ここで \(2+1-1/4=11/4<3\) なので polynomial 指数も安全である。
2. 周期 grid では tail transform の二回の部分積分から、符号を含めて
   \[
   T_a(\omega_n)=-2\bigl((-1)^nf'(a)+\int_a^\infty f''(t)\cos(\omega_nt)\,dt\bigr)/\omega_n^2.
   \]
   Parseval と grid spacing の和により、本文(11)の periodic \(H^1\) 誤差および endpoint 誤差が \(a,N\) に一様に得られる。
3. \(\delta=Tf-f\) の jump は \(\pm Tf(a)\) であり、\(\pm(Tf-f)(a)\) だけではない。同稿はこの項と \(|f(a)|\) を保持している。weighted \(L^1\) と variation の和 \(\mathcal B(\delta)\) に対して
   \[
   |\widehat\delta(x+iy)|\le\mathcal B(\delta)/(1+|x|),\qquad |y|\le1/2.
   \]
   ここで complex integration by parts の \(|z||\widehat\delta(z)|\le V\) と \(\min(A,V/|x|)\le(A+V)/(1+|x|)\) を用いる。定数1の記載も正しい。
4. compact BV の \(Tf\) 自体を mollify し、actual Gamma/pole/prime formula と spectral formula の一致を示す。非compact \(\delta\) の形式が無説明に定義されたことを仮定しない。
5. \(f_j\) の transform が全ての \(z_\rho,\overline{z_\rho}\) で消えるので、零点和で \(\widehat{Tf_j}\) を \(\widehat\delta_j\) に置き換えられる。\(\sum_\rho(1+|\gamma|)^{-2}<\infty\) は重複度込みで成立し、RH を仮定しない。

指定された二経路では
\[
a-\pi\Omega/2
=a-\frac{\pi^2(N+1)}{2a}
\]

が polynomial factor に勝つ。従って **actual full Rate A の消失は、これら二経路について無条件に証明される**。固定 \(m\) の Gram 正定値極限と合わせると、全 restricted Ritz 値にも同じ種類の絶対上界がある。

**限定:** これは符号・leading asymptotic・最速方向を特定しない。全ての \(N/a\to\infty\) に対してこの上界が消えるとは言わず、\(m\to\infty\) への一様性もない。数値定数 \(C_m\) の interval certificate を生成した結果でもない。Rate B の full ground/gap と Rate C の選択状態の transform は別の問題である。

RH7 の OPEN は、この追加により「指定二経路での full recognition 消失」について解消した。ただし full 次次数・最速状態・path-independent selection に関する OPEN は変わらない。

## RH12. 重要な限定追加：support-only \(m=1\) では方向選択が成立

最終主文の「\(m\ge1\) で複数の消去方向」という表現を点検したところ、\(m=1\) の rank-one kernel は1次元であり、projective line は一つだった。この訂正から root/builder が導いた次の限定命題を独立に再証明した。したがって「選択はどの subcomponent にも得られなかった」と結論してはならない。

raw basis \(f_0=k,f_1=k''\) と **support restriction のみ** を用い、
\[
M_a=[Q(R_af_i,R_af_j)]_{i,j=0}^1,\quad
G_a=[\langle R_af_i,R_af_j\rangle]_{i,j=0}^1,\quad
s_a=\frac aY A_1^2>0
\]

とする。既に確認した混合漸近と \(A_0/A_1\sim1/(4Y^2)\) から
\[
\frac{M_a}{s_a}\longrightarrow
\begin{pmatrix}0&0\\0&1\end{pmatrix}
=E_{11},\qquad G_a\longrightarrow G_\infty>0.
\]

従って
\[
G_a^{-1/2}\frac{M_a}{s_a}G_a^{-1/2}
\longrightarrow G_\infty^{-1/2}E_{11}G_\infty^{-1/2}.
\]

右辺は rank 1 の正半定値行列で、固有値は
\[
0,\qquad \nu=(G_\infty^{-1})_{11}
=\frac{(G_\infty)_{00}}{\det G_\infty}>0.
\]

ここでは添字を \(0,1\) とする。したがって十分大きい \(a\) で最小 generalized eigenvalue は単純で、restricted gap は \(s_a\nu(1+o(1))\)。whitened eigenline を元の係数へ戻すと、limit は \(c_1=0\) の直線である。\(R_af_j\to f_j\) in \(L^2\) と合わせて、対応する unit physical vector は位相を除き
\[
\frac{k}{\|k\|_2}
\]

へ収束する。

**判定: PASS — support-only \(\mathcal R_1\) に限った一意な最小方向の極限選択。** これは signed Rayleigh minimum の主張である。最小値 \(\mu_0/s_a\to0\) は得るが、その第一非零漸近や符号をこの議論で決めたわけではなく、\(|Q|\) の最小化を別に解いたとも主張しない。

\(m\ge2\) では同じ最高列スケールだけの極限に高次元 kernel が残る。ここではそこから追加の選択定理を作らない。また、この命題には finite \(P_N\) がなく、full canonical regularization の selector、全 Weil head の ground、cofinal \(N(a)\) の経路独立性、G*、RH への含意はない。最終 verdict の NO FINITE-SCALE SELECTION PRINCIPLE IDENTIFIED は **full canonical system に関するもの** と明記する必要がある。

## RH13. 最終統合の読取監査と数値転記

最終追加レビューの対象は research/rate_history_selection.md、research/radical_degeneracy_lifting.md、research/rate_history_candidate_matrix.md、research/rate_history_state.json、および BR8 の限定選択命題である。参照される過去の外部論文の全再監査、新たな実験の再実行、旧375ファイルの保存 hash の独立全走査は、この最終読取監査に含めない。既存ファイルを変更していないことと、root の preservation validation の検査範囲を区別する。

**解析式の照合。** 主文(U2)の次数は正しい。\(N\sim a^2\) では \(\Omega\sim\pi a\) なので \(a(1+\Omega)^{4m+8}=O_m(a^{4m+9})\)。\(N\sim a^3\) では \(\Omega\sim\pi a^2\) なので \(O_m(a^{8m+17})\)。指数もそれぞれ \(-(\pi^2/2-1)a\)、\(a-\pi^2a^2/2\) の上界へ移せる。ceil と +1 は指数をさらに小さくする。boundary cancellation の \(2/Y^2\) は \(Y=\pi\lambda^2\) より \(2/(\pi^2\lambda^4)\) と一致する。

**数値転記の照合。** splitting_results.json と trajectory_results.json から独立に読み取り、以下を再計算した。これは数値計算自体の interval 認証ではない。

* 11有限 endpoint、33 restricted generalized problems。
* \((\lambda,N)=(13,17)\) の global unit coefficients は
  \[
  (7.49151344585,\ 0.0458599650388,\
  9.39773700605\,10^{-5},\ 6.44928528688\,10^{-8}).
  \]
  先頭を1にすると
  \[
  (1,\ 0.00612158883119,\
  1.25445106306\,10^{-5},\ 8.60878824219\,10^{-9}).
  \]
  初稿の最後の係数 \(8.60933\,10^{-9}\) は \(8.60879\,10^{-9}\) へ訂正済み。
* 同 endpoint の restricted minima、full \(e_0\)、full gap、excess/gap、global \(k\)・full ground・raw proxy との overlap、全試験空間への ground projection の表示丸めは JSON と整合する。
* radical note の四行表、\(\lambda=13\) の \(N=7,17\) 間の二種の overlap、Gram condition と三種の解像度比較も JSON と整合する。

**修正済みの論理・表示事項。** \(m=1\) に複数の projective null directions があるという記述は訂正され、さらに RH12 の正の限定選択結果が main/state/matrix に反映された。候補表の生の縦棒で列が分割される箇所も absolute Q という表現に直された。

**最終 scope。** support-only 主漸近と \(\mathcal R_1\) の signed 最小方向選択、および full \(P_NR_a\) recognition の粗上界は証明済みとして保持できる。full canonical leading rates/selector、全 ground との定量比較、無限経路独立性、G*、RH は未証明。未取得を「存在しないという反証」に変えていない。新規性は主張しない。

machine state の effective boundary form 欄と candidate の Level 3–5 も full canonical 系に限定する訂正を確認した。support-only R1 の正の選択結果との scope の相違は明記され、当該指摘は **RESOLVED**。現版に重大な未修正の数式誤り・過大主張は見つからない。

### 最終読取 snapshot の SHA-256

読取時刻（UTC）: 2026-09-30T02:28:30.913672+00:00

この表は実際に読んだ新規成果物の内容を固定する。対象の後続変更を自動的に監査済みとは扱わない。

|対象|SHA-256|
|---|---|
|research/rate_history_selection.md|e0759654a1878e8369845f7ebc097c7f1687592e9f82da75ba3dc811e064cfe3|
|research/radical_degeneracy_lifting.md|31791fff51d87e2e80fe6e9dc04a4b76d4ed7dc407642a1dd6ea3a0c42b81c25|
|research/rate_history_candidate_matrix.md|ceaf4c52c9b61c23aef69c74b42a5143f81915e541b74c0b2216cbe576120e9a|
|research/rate_history_state.json|6bd023a13702cb75a2b31969e37d06e3b96d879826c712e508c642315f5b2efd|
|research/ground_state_trajectory.md|b956c37e70555f93670f4fc4947c6cf28e5b53d2c6579b10e5ec075463a3634b|
|research/rate_history/notes/boundary_rate_analysis.md|b73e96ddaa1cf47063b3924be2bacdfcaaf7963b83d26feb6a3c41219d94cd5a|
|research/rate_history/notes/full_projection_upper_bound.md|46da953ab9ae37bf2dcf5740d1053df097a530b1bc0bdac95b15502f15614121|
|research/rate_history/experiments/splitting_probe.py|c768b6d405621a18611f7f903d378307363ec65e96885fc993d071b334b679eb|
|research/rate_history/experiments/splitting_results.json|f7ecf08d520384344d5b043ded500bf28450049b6d26fb57fb5fe21cf74000fb|
|research/rate_history/experiments/proxy_trials.py|622d3db94923a4f66465a29d94890099f8e55c7c784eae04f6a6e88376dc45d2|
|research/rate_history/experiments/prolate_trials.json|67ee5c5344c744b9af092b0b721af19f1225324f994291ca33ad0617dda124fe|
|research/rate_history/experiments/trajectory_diagnostics.py|69ad74d2fbae7e6a0e85bebd1333a726d5978e34cd613bd8bf898bc9cff2a9f4|
|research/rate_history/experiments/trajectory_results.json|27f756e82d4cf7cfd03701213a05ac4769d00a1d1c30a7d79a5730ed6fd02951|
|research/rate_history/experiments/prime_event_probe.py|6ab41fd1f67a94862beef409e3785696fc37c61457616071f28ebf198d976f44|
|research/rate_history/experiments/prime_event_results.json|141aec90df16cb4d56a6fa6d6450be5dd5f7f5cbae78a61cd6f806e82bdb18db|


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/ground_state_trajectory.md`](../../../reports/research/ground_state_trajectory.md)
- [`research/radical_degeneracy_lifting.md`](../../../reports/research/radical_degeneracy_lifting.md)
- [`research/rate_history/experiments/prime_event_probe.py`](../../../../artifacts/research/rate_history/experiments/prime_event_probe.py)
- [`research/rate_history/experiments/prime_event_results.json`](../../../../artifacts/research/rate_history/experiments/prime_event_results.json)
- [`research/rate_history/experiments/prolate_trials.json`](../../../../artifacts/research/rate_history/experiments/prolate_trials.json)
- [`research/rate_history/experiments/proxy_trials.py`](../../../../artifacts/research/rate_history/experiments/proxy_trials.py)
- [`research/rate_history/experiments/splitting_probe.py`](../../../../artifacts/research/rate_history/experiments/splitting_probe.py)
- [`research/rate_history/experiments/splitting_results.json`](../../../../artifacts/research/rate_history/experiments/splitting_results.json)
- [`research/rate_history/experiments/trajectory_diagnostics.py`](../../../../artifacts/research/rate_history/experiments/trajectory_diagnostics.py)
- [`research/rate_history/experiments/trajectory_results.json`](../../../../artifacts/research/rate_history/experiments/trajectory_results.json)
- [`research/rate_history/notes/boundary_rate_analysis.md`](../../../reports/research/rate_history/notes/boundary_rate_analysis.md)
- [`research/rate_history/notes/full_projection_upper_bound.md`](../../../reports/research/rate_history/notes/full_projection_upper_bound.md)
- [`research/rate_history_candidate_matrix.md`](../../../reports/research/rate_history_candidate_matrix.md)
- [`research/rate_history_selection.md`](../../../reports/research/rate_history_selection.md)
- [`research/rate_history_state.json`](../../../../data/source-records/research/rate_history_state.json)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `research/rate_history/charter.md` — SOURCE REFERENCE NOT INCLUDED
