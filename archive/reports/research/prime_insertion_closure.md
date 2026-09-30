**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_insertion_closure.md` · Original SHA-256: `20f58e6e297094a83fdb66e146eb0308e58de9fd35cc0eb57dd8d207b55129c9`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 素数追加とmodular極限の内部検査

2026-09-29。前巡で一般の正移動係数によるPSD移植は棄却した。
今回は整数の積構造を使い、一素数の**全幾何級数**による更新と、
実際のtheta核の有限素数近似を調べた。外部論文の証明の追跡ではない。
以下は独立導出と反証で、新規性やRH証明への距離短縮を主張しない。

## 1. 対数重みの素数冪への厳密な再編成

[前巡](internal_first_principles.md)と同じ

\[
k(t)=e^{t/2}(4\pi^2e^{4t}-6\pi e^{2t})e^{-\pi e^{2t}},\quad
\Phi(s)=\sum_{n\ge1}n^{-1/2}k(s+\log n)
\]

を使う。\(L\Phi(s)=\sum n^{-1/2}\log n\,k(s+\log n)\) について

\[
\boxed{L\Phi(s)=\sum_{d\ge2}\frac{\Lambda(d)}{\sqrt d}\Phi(s+\log d),\quad s\ge0.} \tag{1}
\]

\(\log n=\sum_{d\mid n}\Lambda(d)\) を代入して \(n=dm\) と添字を付け替える。
対数重みを含めた絶対収束は、\(n^4e^{-\pi n^2/2}\) と
\(e^{9s/2}e^{-(\pi/2)e^{2s}}\) の積による上界から従う。
したがって、前巡の差引項は任意の補正ではなく、素数冪の移動作用として確定する。
この恒等式自体が差引項の符号を決めるわけではない。

## 2. 一素数の更新: 正項と負項のexact ledger

半直線上で、実急減関数 \(f\) に対し

\[
K[f](a,b)=\tfrac14\int_0^\infty(2t+a+b)f(t+a)f(t+b)dt,
\quad H[f](a,b)=\int_0^\infty f(t+a)f(t+b)dt
\]

と定める。\(S_\ell f(t)=f(t+\ell)\)、\(\ell=\log p\)、\(r=p^{-1/2}\)、
\(T=(I-rS_\ell)^{-1}\)、\(g=Tf\)、\(h=Tg\) と置く。

\[
\mathcal G_p[f](a,b)=\sum_{i,j\ge0}r^{i+j}K[f](a+i\ell,b+j\ell),
\quad H_\ell[h](a,b)=\int_0^\ell h(t+a)h(t+b)dt.
\]

移動後の \(2t+a+b\) の差を正確に残すと

\[
\boxed{K[g]=\mathcal G_p[f]+\frac\ell4H[g]
-\frac\ell4\{(1-p^{-1})H[h]+p^{-1}H_\ell[h]\}.} \tag{2}
\]

導出: \(N=T-I=rS_\ell T\) とすると差引項は
\(D=(\ell/4)\int[(Ng)(t+a)g(t+b)+g(t+a)(Ng)(t+b)]dt\)。
\(g=h-rS_\ell h\) より
\(D=(\ell/4)(H[h]-r^2H[S_\ell h]-H[g])\)。
\(H[S_\ell h]=H[h]-H_\ell[h]\) を代入すれば (2)。

括弧内も加算側の \(H[g]\) もPSDだが、その差の符号は確定しない。
\(S_\ell\) が \(L^2(0,\infty)\) の収縮であることから

\[
-\frac{\ell}{2(\sqrt p+1)}H[g]\preceq D
\preceq\frac{\ell}{2(\sqrt p-1)}H[g]. \tag{3}
\]

これは局所的な真の評価。例えば \(v=(I-rS_\ell)u\) と置き、
\(\|rS_\ell u\|\le r\|u\|\) を用いると
\(-r\|v\|^2/(1+r)\le\Re\langle rS_\ell u,v\rangle
\le r\|v\|^2/(1-r)\) が平方完成で従い、(3)を得る。
actualな \(p\)-free seed で \(\mathcal G_p[f]\) が費用を支払うという
独立評価は得られていない。これを前提として反復する案は採用しない。

## 3. 全幾何級数でもPSD保存は偽

\(p=2\)、\(\ell=\log2,r=2^{-1/2}\)、\(f(t)=e^{-t^2}\) を取る。
基底核は \(K[f](a,b)=f(a)f(b)/8\succeq0\)。しかし

\[
g(t)=\sum_{j\ge0}r^je^{-(t+j\ell)^2},\quad
\mu(t)=\frac{\sum j r^je^{-(t+j\ell)^2}}{g(t)}
\]

に対して \(K[g]\) はPSDではない。確率重みで規格化すると

\[
(\log g)''=-2+4\ell^2\operatorname{Var}_t(j),\qquad
\mu'=-2\ell\operatorname{Var}_t(j)<0.
\]

\(A_j=j^2r^je^{-j^2\ell^2}\) とすると
\(A_1<1/2,A_2<4/11,A_{j+1}/A_j<3/16\ (j\ge2)\)。
根拠は \(2/3<\ell<7/10\)、\(r<3/4\) および
\(e^{4/9}>3/2,e^{16/9}>11/2,e^{20/9}>9\) で、有限Taylor和で有理数検算できる。
従って全 \(t\ge0\) で

\[
\operatorname{Var}_t(j)\le E_t[j^2]<271/286,
\qquad (\log g)''<-1021/7150<0.
\]

\(h_a(t)=g(t+a)/g(a)\) と置くと、\(t>0\) で
\(h_0>h_1>0\)、\(\mu(t)>\mu(t+1)>0\)。
\(g'+2tg=-2\ell\mu g\) を部分積分し、二点係数
\(c=(1/g(0),-1/g(1))\) で境界平方を消せば

\[
\boxed{c^T[K[g](i,j)]_{i,j=0,1}c
=-\frac\ell2\int_0^\infty(h_0-h_1)
[\mu(t)h_0-\mu(t+1)h_1]dt<0.} \tag{4}
\]

**全幾何級数に対する解析的反例**であり、単一shiftや有限打切りで代用していない。
独立求積は約 \(-0.0117730483963790582\) で、(2) のledgerとも一致する。
求積自体は非認証。符号の証明は (4) と無限尾の有理数評価である。

## 4. 実際の有限素数近似はmodular境界を保存しない

有限素数集合 \(\mathcal P\) と、その素数だけを因子に持つ整数集合
\(\mathcal S(\mathcal P)\) を用い、全実数 \(t\) で

\[
\Phi_{\mathcal P}(t)=\sum_{n\in\mathcal S(\mathcal P)}n^{-1/2}k(t+\log n)
\]

とする。増大する素数集合によるexhaustionでは、\(\Phi_{\mathcal P}\to\Phi\) は
全ての固定compact上で全階微分を含め一様。しかし全実線上では別の振る舞いになる。

\(h_0(t)=e^{t/2}e^{-\pi e^{2t}}\)、\(k=(D^2-1/4)h_0\) とすると

\[
\int_\mathbb R k=-\frac{\Gamma(1/4)}{8\pi^{1/4}}=-a<0,
\quad C_{\mathcal P}=\prod_{p\in\mathcal P}(1-p^{-1/2})^{-1}<\infty,
\]
\[
\boxed{\int_\mathbb R\Phi_{\mathcal P}=-a C_{\mathcal P}.} \tag{5}
\]

有限集合では平行移動の \(L^1\) ノルムと係数の総和でFubiniを正当化できる。
\(\mathcal P_X=\{p\le X\}\) なら
\(C_{\mathcal P_X}\ge\sum_{n\le X}n^{-1/2}\to\infty\)。
一方 \(\Phi>0\) で積分は有限正値。
従って \(\|\Phi_{\mathcal P_X}-\Phi\|_1\to\infty\)。
有限素数のFourier変換を \(z=0\) でさえ項別極限することはできない。

さらに \(h_{\mathcal P}=\sum_{n\in\mathcal S}n^{-1/2}h_0(t+\log n)\)
は有限集合で \(H^2\cap C_0\) に属し、\(t\ge0\) で厳密減少する。
\(h_{\mathcal P_X}(-\log X)\ge e^{-\pi}\lfloor X\rfloor/\sqrt X\)。
負側で取る最大点 \(t_X\) では
\(\Phi_{\mathcal P_X}(t_X)\le-h_{\mathcal P_X}(t_X)/4\) なので、
反射欠損 \(D_{\mathcal P}(t)=\Phi_{\mathcal P}(t)-\Phi_{\mathcal P}(-t)\) は

\[
\|D_{\mathcal P_X}\|_\infty\ge
\frac{e^{-\pi}\lfloor X\rfloor}{4\sqrt X}\longrightarrow\infty. \tag{6}
\]

### 正エネルギーも極限を閉じない

\(A_{\mathcal P}=h_{\mathcal P}-h_{\mathcal P}\circ(-I)\) とすれば
\(D_{\mathcal P}=(D^2-1/4)A_{\mathcal P}\) だから

\[
-\int A_{\mathcal P}D_{\mathcal P}
=\int(|A_{\mathcal P}'|^2+|A_{\mathcal P}|^2/4)\ge0. \tag{7}
\]

これは実在する正エネルギーだが、modular関係から
\(A_{\mathcal P}\to-\sinh(t/2)\) 局所、\(D_{\mathcal P}\to0\) 局所。
極限の \(A\) は \(H^1\) に入らず、(7) の右辺はFatouにより発散する。
実際、極限の被積分関数を \([-R,R]\) に積分すると \(\tfrac12\sinh R\)。
正エネルギーの存在と、極限でも使える一様な制御を混同しない。

## 5. 正の側を偶延長しても、有限系には非実零点が無限個ある

そこで自然な別案 \(\psi_{\mathcal P}(t)=\Phi_{\mathcal P}(|t|)\) を検査した。
これは正・偶で、\(0<\psi_{\mathcal P}\le\Phi\)。任意の固定 \(R\ge0\) について

\[
\int e^{R|t|}|\psi_{\mathcal P}(t)-\Phi(t)|dt\longrightarrow0,
\]

従って Fourier整関数 \(F_{\mathcal P}\) は \(F_\Phi\) へ複素平面上で局所一様収束する。
**それでも全ての有限素数集合で \(F_{\mathcal P}\) は無限個の非実零点を持つ。**

証明を零点の数値探索なしで与える。個別項
\(g_n(t)=e^{t/2}(4x_n^2-6x_n)e^{-x_n},\ x_n=\pi n^2e^{2t}\) に対し

\[
g_n'(t)=-e^{t/2}x_n(8x_n^2-30x_n+15)e^{-x_n}<0
\quad(n\ge2,t\ge0).
\]

全核の偶性 \(\Phi'(0)=0\) と微分級数の絶対収束より

\[
d_{\mathcal P}:=\Phi_{\mathcal P}'(0)
=-\sum_{n\notin\mathcal S(\mathcal P)}g_n'(0)>0. \tag{8}
\]

有限集合では省略された素数が必ず存在する。つまり偶延長には原点で微分の跳びがある。
右側関数 \(f=\Phi_{\mathcal P}\) は全階微分が \([0,\infty)\) 上可積分で∞で消える。
四回の部分積分から

\[
F_{\mathcal P}(x)=-\frac{2d_{\mathcal P}}{x^2}
+\frac{2f'''(0)}{x^4}+rac2{x^4}\int_0^\infty f^{(4)}(t)\cos(xt)dt
=-\frac{2d_{\mathcal P}}{x^2}+O_{\mathcal P}(x^{-4}). \tag{9}
\]

従って実軸の十分遠方で厳密に負。整関数は非零なので、実零点は有限個。
一方 \(\psi_{\mathcal P}(t)\le Ce^{9|t|/2-\pi e^{2|t|}}\) より
\(\log M_{\mathcal P}(r)=O(r\log r)\)、整関数の位数は高々1。
もし全零点も有限なら、Hadamard分解で \(F_{\mathcal P}=e^{az+b}Q(z)\)。
偶性が \(a=0\) を強制するが、非零多項式はRiemann–Lebesgueの
\(F_{\mathcal P}(x)\to0\) と矛盾する。ゆえに非実零点は無限個。
さらに \(F_{\mathcal P}(iy)>0\) なので虚軸にもなく、四つ組として現れる。

最小の \(\mathcal P=\{2\}\) では、Arb192bitと独立な二つの尾評価から
\(d_{\{2\}}=8.26527956381008077537\ldots\times10^{-8}>0\) を照合した。
これは原点微分の認証。非実零点の存在・個数は (8)〜(9) と解析的議論による。

この反例の対象は**正半直線を原点で偶延長した有限素数近似**。
通常の有限Euler積、全 \(\xi\)、別のmodular近似、RHの反例とは扱わない。
局所一様極限で非実零点がどこへ移るかを証明しておらず、極限の零点配置は未解決のまま。

## 判定と独立検査

- (1)〜(3): ROOT/BUILDER 独立導出。一般PSD保存は (4) で棄却。
- (4): DESTROYER の解析構成をROOTが全尾の有理数評価と別求積で確認。
- (5)〜(7): LITERATURE担当の内部導出をROOTが積分・境界・最大値の議論で検算。
- (8)〜(9) と無限個の非実零点: ROOTが構成し、LITERATURE/DESTROYERが独立監査。
- [再現スクリプト](../../../artifacts/experiments/scripts/prime_insertion_checks.py)と
  [結果](../../../artifacts/experiments/results/prime-insertion-checks.json)に厳密値・非認証値・scopeを分離保存。

**この有限素数追加による正値性伝播・自然な偶completionの全実零点保存という候補は終了。**
素数集合や零点表の拡大を続けない。次に有限系を作るなら、全核に固有のmodular境界条件を
最初から保つ別の構成が必要で、単に最後に偶化する操作では足りない。
独立した全域正値化は未達、主証明グラフ合流0、RHはOPEN。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/prime-insertion-checks.json`](../../../artifacts/experiments/results/prime-insertion-checks.json)
- [`experiments/scripts/prime_insertion_checks.py`](../../../artifacts/experiments/scripts/prime_insertion_checks.py)
- [`research/internal_first_principles.md`](internal_first_principles.md)
