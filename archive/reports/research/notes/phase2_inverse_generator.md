**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase2_inverse_generator.md` · Original SHA-256: `343f7dd9dcca85c7a2728fc57c39052e96c1743eb67d7d98c2f5d6c2aaf7b054`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase II / Track B — 全素数 germ からの逆スペクトル生成子

2026-09-29。内部構成の後に限定した一次資料照合を実施。RH は OPEN。
ユーザー指定の11見出しを使用。
本ノートだけを作成し、主状態・主依存グラフを変更しない。
独立導出を新規性と呼ばず、既知の条件付き逆定理と、その前件の未証明を分ける。

## 1. Candidate generator

今回の具体的候補は、全素数データで一意に定まる完成対数微分

\[
\Xi(z)=\xi(1/2+iz)=\xi(1/2-iz),\qquad
\boxed{m_\xi(z)=-\frac{\Xi'(z)}{\Xi(z)}}. \tag{B1}
\]

これは最初から自己共役作用素があると仮定する構成ではない。
次節の絶対収束する prime germ から有理型関数を固定した後、
その関数が正 Hamiltonian の Weyl 関数になれるかを検査する。
候補の正性を定義や公理に入れない。

**本ノートの到達点:** 算術 germ と全零点データの関数論的対応は正確に閉じる。
しかし正 Hamiltonian を得るための Herglotz 前件は RH と正確に同値である。
従って逆スペクトル定理を適用するだけでは独立な RH 入力を得ない。

## 2. Arithmetic input

\(s=1/2-iz\)、\(\Im z>1/2\) と置く。\(\Re s>1\) なので
\(\zeta'/\zeta=-\sum_{p,k\ge1}(\log p)p^{-ks}\) は絶対局所一様収束する。
\(\xi(s)=(s-1)\Gamma(1+s/2)\pi^{-s/2}\zeta(s)\) より

\[
\boxed{m_\xi(z)=i\left\{
\frac1{s-1}+\frac12\psi(1+s/2)-\frac12\log\pi
-\sum_p\sum_{k\ge1}(\log p)p^{-ks}\right\}.} \tag{B2}
\]

ここでは極項・Gamma 項・全素数冪を固定している。任意 counterterm はない。
既知の \(\xi\) の整関数延長から (B2) の有理型継続は (B1) に一意に一致する。
これは解析接続の一意性であり、収束級数を critical strip へ項ごとに代入する操作ではない。
全素数 germ は全零点を決めるが、そのこと自体は極の実数性を証明しない。

通常の \(z_\rho=(\rho-1/2)/i\) を使えば、非自明零点 \(\rho\) の位数が \(r\) のとき

\[
m_\xi(z)=-\frac{r}{z-z_\rho}+\text{holomorphic part}. \tag{B3}
\]

理由は \(\Xi(z)=(z-z_\rho)^r h(z),\ h(z_\rho)\ne0\) という局所分解のみ。
対数微分の極は**単純**だが、留数 \(-r\) が元の重複度を保存する。
\(\xi\) は \(s=0,1\) で非零、Gamma 極と trivial zeros は完成時に消えるため、
全 \(m_\xi\) に非自明零点以外の有限極はない。

## 3. Boundary data

\(\Xi\) は実偶整関数、位数1、\(\Xi(0)>0\)。従って
\(m_\xi(\bar z)=\overline{m_\xi(z)}\)、\(m_\xi(-z)=-m_\xi(z)\)、\(m_\xi(0)=0\)。
これらは無条件。零点が \(|\Im z|<1/2\) にあるという古典的 strip 条件も無条件である。

既知の Hadamard 積で零点を \(\lambda,-\lambda\) ごとに組にすると
\(\sum r_\lambda/|\lambda|^2<\infty\) により、
\(m_\xi=\sum r_\lambda[(\lambda-z)^{-1}+(-\lambda-z)^{-1}]\)
は極を避けた compact 上で正常収束する。一般には \(\lambda\) は非実を許す。
\(\Im z>1/2\) では各単項の虚部が正なので、

\[
\Im m_\xi(z)>0\qquad(\Im z>1/2) \tag{B4}
\]

が無条件に従う。これは既知の zero-free Euler half-plane と整合する弱い結果である。
\(0<\Im z\le1/2\) への延長を含まず、全上半平面の Herglotz 条件ではない。
上半平面を平行移動して既知領域に入れるとスペクトル変数と境界も変わるため、
元の全 \(z_\rho\) を実スペクトルとして捕捉したことにはならない。

**条件付き canonical boundary の規約。**
\(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\)、\(JY'=zHY\)、\(U(z,0)=I\) とし、
\(U(z,\cdot)(1,m(z))^{\mathsf T}\in L^2_H[0,\infty)\) により Weyl 関数を定める。
正の trace-normalized \(H\) なら無限端は limit point。
半正定値 \(H\) では null directions を割る weighted space と線形関係を用いる場合があり、
通常の \(L^2(dx)\) 上の微分作用素・domainを無断で同一視しない。
本ノートでは実際の \(H\) を構成していないため、算術的微分作用素の domain を確保したとはしない。

## 4. Evolution law

正 Hamiltonian が独立に得られた場合だけ、transfer は

\[
U'=-zJHU,\qquad \det U=1.
\]

\(H=\begin{pmatrix}a&b\\b&c\end{pmatrix}\)、\(r=Y_2/Y_1\) の chart では

\[
r'=-z(a+2br+cr^2). \tag{B5}
\]

これは条件付きの正しい Riccati 恒等式である。算術 germ (B2) から
\(a,b,c\) の正性を導出する法則ではない。\(Y_1=0\) での chart の極を
canonical system 自体の不存在と混同しない。

既存の有限 Euler 積による誤った境界の問題は**予備排除だけ**として保持する。
有限 \(P\) で (B2) の素数和だけを切ると、\(s=1\) の極を打ち消す
\(\zeta\) の極がなく、\(z=i/2\) に留数 \(-1\) の人工極が残る。
これを直接引く最小補正でも、\(z=i\)、\(s=3/2\) で

\[
\Im m_P^{\rm reg}(i)
=\tfrac12\psi(7/4)-\tfrac12\log\pi
-\sum_{p\in P}\frac{\log p}{p^{3/2}-1}
<\tfrac12\log\frac{7}{4\pi}<0.
\]

\(\psi(x)<\log x\) は Gamma 密度に関する \(\mathbb E\log X<\log\mathbb EX\) で直接従う。
有限素数の修復探索は再開しない。これは全素数の (B1) の反証ではなく、
今回の主要成果や新しい大規模候補とも数えない。

## 5. Why 1/2 appears

\(1/2\) は既知の完成関数の対称中心であり、\(s\leftrightarrow1-s\) を
\(z\leftrightarrow-z\) とする座標を固定する。正 canonical system の逆定理が
数値 \(1/2\) を算術なしで選ぶわけではない。
\(z_\rho\in\mathbb R\) と \(\Re\rho=1/2\) はこの座標で同値。
その同値を新しい zero-exclusion 原理とは数えない。

## 6. What forbids off-line states

ここで有効な禁止原理は Herglotz–Nevanlinna 性、すなわち
\(m\) が全 \(\mathbb C_+\) で正則かつ \(\Im m\ge0\) であること。
正 canonical system ではこれが Weyl 恒等式から従う。
しかし actual \(m_\xi\) については

\[
\boxed{m_\xi\text{ is Herglotz on }\mathbb C_+
\iff \text{RH}.} \tag{B6}
\]

順方向：非実零点があれば実構造により上半平面にも零点があり、(B3) が正則性を破る。
逆方向：RH 下では正の distinct heights \(\gamma\) と重複度 \(r_\gamma\) を用いて

\[
\Xi(z)=\Xi(0)\prod_{\gamma>0}(1-z^2/\gamma^2)^{r_\gamma},
\quad
\boxed{m_\xi(z)=\sum_{\gamma>0}r_\gamma
\left(\frac1{\gamma-z}+\frac1{-\gamma-z}\right).} \tag{B7}
\]

位数1・偶性により余分な指数因子はない。
\(\sum r_\gamma/\gamma^2<\infty\) が正常収束を保証し、各項の虚部は正。
spectral measure は正確に \(\mu=\sum_{\gamma>0}r_\gamma(\delta_\gamma+\delta_{-\gamma})\)。
余分な原子や連続部分はなく、重複度は原子の質量に保存される。

**重複度と domain の区別。** 条件付きの最小 spectral model は
\(\mathcal H=L^2(\mu)\)、\((Tf)(t)=tf(t)\)、
\(D(T)=\{f:\int t^2|f(t)|^2d\mu<\infty\}\)。これは自己共役で、
スペクトルの集合は exact、各 distinct height の固有空間は一次元。
質量 \(r_\gamma\) は norming weight であり、固有空間の次元ではない。
\(\Xi=(z^2-1)^q\) という模型でも両原子の質量は \(q\) だが、この scalar model の
両固有空間は一次元である。重複度 \(q\) を持つ演算子を要求するなら
別の多重channel構成か単純性の証明が必要で、scalar inverse theorem は供給しない。

また \(\mu(\mathbb R)=\infty\) なので定数1を Hilbert ベクトルにしない。
\(v(t)=(1+t^2)^{-1/2}\in L^2(\mu)\) を用いると、正則化した表示は
（この表示の内積は第2変数線形）

\[
m_\xi(z)=\langle v,(I+zT)(T-zI)^{-1}v\rangle.
\]

この模型も RH を仮定した零点測度からの再構成であり、素数からの無条件自己共役構成ではない。

Hermite–Biehler 表現に変えても同じである。
\(A=\Xi,B=-\Xi',E=A-iB\) とすると、\(A\ne0\) の点で
\(|E|^2-|E^\sharp|^2=4|A|^2\Im(B/A)\)。
\(B/A=m_\xi\) の正性は (B6) に戻る。
多重実零点に由来する共通実因子と、採用する HB 定義の実零点条件は別途処理する。
共通因子を黙って消して全零点・重複度対応を主張しない。

## 7. Known prior art

構成を固定した後、次の二つの一次論文の該当箇所だけを読んだ。全文の独立検証ではない。

- George Csordas / Alain Escassut, *The Laguerre inequality and the distribution of zeros of entire functions*,
  AMBP 12 (2005), 331–345、[原論文 PDF](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf)。
  Definition 1.1 は実整関数の genus ≤1 型積と実軸対称 strip を規定。
  printed p.334, Theorem 2.3 / (2.4) は複素 Laguerre 不等式による L–P 判定を述べる。
  \(f\ne0\) で \(|f|^2\) を除けば \(\Im(-f'/f)/\Im z\) の符号条件となる。
  したがって (B6) は既知の基準の範囲であり、cycle18の境界を回避する新原理ではない。
  査読公刊、使用箇所照合済み、全論文独立証明検証 NO。
- Jonathan Eckhardt / Aleksey Kostenko / Gerald Teschl,
  *Spectral asymptotics for canonical systems*, J. Reine Angew. Math. 736 (2018), 285–315、
  [著者公開 PDF](https://www.mat.univie.ac.at/~gerald/ftp/articles/AsymCS.pdf)。
  §2.1 (2.1)–(2.8) は正半定値局所可積分 Hamiltonian、limit point、Weyl 関数と測度の規約。
  PDF p.4 Theorem 2.2 は **Herglotz 関数を入力として** trace-normalized Hamiltonian を
  a.e. 一意に再構成する de Branges 定理を再掲する。
  Proposition 2.3 は **既に正 Hamiltonian と対応 Weyl 関数がある列**について、
  積分 Hamiltonian・transfer・Weyl 関数の所定位相の収束を同値とする。
  任意の Euler 切断を Herglotz 列に変える定理ではない。
  査読公刊、該当定理と前後の条件を照合、全文独立検証 NO。

既存 Suzuki の大域 determinant 条件を再び「解決された入力」として使用していない。
逆定理の正しさと actual prime germ がその入力条件を満たすことは別の命題である。

## 8. RH-equivalent hidden assumption?

**YES、正確に (B6)。** 全素数 germ から関数の一意性・全極・重複度までを得る部分は無条件。
その同じ関数に Herglotz 性を追加する部分が RH 同値である。
「ある正 Hamiltonian の Weyl 関数が (B2) と非空開集合で一致する」も、
解析接続の一意性により (B6) と同値になる。局所一致を弱い仮定と誤分類しない。

## 9. Synthetic counterexample status

実偶多項式
\(F(z)=((z-1)^2+1/16)((z+1)^2+1/16)\) は実軸上で正、
全零点が \(|\Im z|<1/2\) にあるが、\(-F'/F\) は上半平面に極を持つ。
対称性・strip・実軸正性・正しい局所 pole multiplicity だけから Herglotz 性は出ない。
これは full prime germ を共有せず、\(\xi\) の反例ではない。
有限 Euler 切断の予備反例も全 \(m_\xi\) の反証とは扱わない。
数値探索は行っていない。符号・極・重複度の判断は明示式による。

統合時の追加検算: ROOTの phase2_boundary_falsification.py で
Im(−F′/F)(1+i/5)=−428313920/24221529<0 を有理数でexactに確認した。

## 10. Exact missing lemma

不足している内容は、所定の prime germ (B2) から、
\(0<\Im z\le1/2\) を含む **全上半平面**の正則性・虚部非負性を独立に導く算術評価。
これを「Herglotz 条件」「正 Hamiltonian の存在」「HB 関数」と呼び換えても同じ義務である。
本ノートはその評価を証明していない。

要求が零点の位数と固有空間次元までの一致なら、さらに scalar spectral weight と
幾何学的 multiplicity の区別が必要。これは Herglotz 逆定理だけからは閉じない。
無条件に得た (B4) は既知の strip の外側の情報であり、この missing lemma より真に弱いが、
RH 経路を短縮する新しい算術評価ではない。

## 11. Decision

**Track B のこの候補は EQUIVALENT-REFORMULATION として停止。**
prime germ → exact meromorphic pole data の接続、重複度の留数表示、
条件付き spectral domain は明確になった。しかし正生成子への入口が RH 同値であり、
既知の inverse theorem によってその入口を無条件に通過することはできない。
実際の微分 Hamiltonian・多重度一致の自己共役生成子・新しい全域算術評価は未構成。
新規性、RH の証明距離短縮、主グラフへの合流は主張しない。
有限 prime 修復・Suzuki 全域条件の再命名へ展開せず、本候補の境界記録として終了する。

独立監査: BUILDERがB1–B7、正常収束、無条件の外側半平面、Herglotz同値、
正則化resolvent、domainとmultiplicityを検算しPASS。
引用されたinverse theoremの全文独立再証明は監査範囲に含まない。
