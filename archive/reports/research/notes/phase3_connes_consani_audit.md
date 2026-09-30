**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase3_connes_consani_audit.md` · Original SHA-256: `4de148e17ab7811766263088d6ca9277e783deac9898367a947aa6836398353e`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# PHASE III — Connes–Consani の Frobenius 役割監査

2026-09-29。対象は指定された Arithmetic Site、Scaling Hamiltonian と、全零点の cohomological realization を区別するために必要なアデール類空間の一次資料。最新証明主張の探索は行っていない。以下は原文の定理・定義・適用範囲の照合であり、各論文の全証明の独立再証明ではない。新規性および RH の進展は主張しない。ページはリンク先 PDF の先頭を 1 とする。

## 固定した一次資料

| ID | 著者・資料 | 使用箇所 |
|---|---|---|
| AS14 | A. Connes, C. Consani, *The Arithmetic Site*, arXiv:1405.4527v1 (2014-05-18); C. R. Math. 352 (2014), 971–975 | [版固定 PDF](https://arxiv.org/pdf/1405.4527v1), Theorems 2.6–2.7, PDF pp.3–4。 [出版情報](https://www.numdam.org/item/CRMATH_2014__352_12_971_0/) |
| GAS15 | 同著者, *Geometry of the Arithmetic Site*, arXiv:1502.05580v1 (2015-02-19) | [版固定 PDF](https://arxiv.org/pdf/1502.05580v1), Theorem 3.8 p.13; §4.2–4.3 pp.15–17; Theorem 7.7 p.38 |
| SH19 | 同著者, *The Scaling Hamiltonian*, arXiv:1910.14368v1 (2019-10-31) | [版固定 PDF](https://arxiv.org/pdf/1910.14368v1), §2.2 pp.11–12; Theorem 2.5 p.13; Lemma 3.4/Corollary 3.5 p.15; Fact 3.6 p.17; Conjecture 4.1 p.18 |
| CCM07 | A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392v1 (2007-03-13) | [版固定 PDF](https://arxiv.org/pdf/math/0703392v1), Definition 4.10 pp.21–22; Proposition 4.13 p.23; Theorem 4.16 pp.24–25; Theorem 6.1 p.28; Proposition 6.2/Corollary 6.3 p.29 |

## 七つの役割

| Frobenius の役割 | 証明済みの内容・locator | 残る区別 |
|---|---|---|
| Arithmetic origin | AS14 Theorem 2.6：整数乗法の topos と半環からの点が、下記のアデール商になる。 | 零点の対角配置から定義した空間ではない。 |
| Iterates | AS14 Theorem 2.6 の点上では \(Fr_\lambda:x\mapsto x^\lambda\)、従って \(Fr_\lambda Fr_\mu=Fr_{\lambda\mu}\)。 | GAS15 Theorem 7.7 の **correspondence の合成**は別で、非有理 \(\lambda,\mu\) かつ有理 \(\lambda\mu\) では接線的変形 \(Id_\epsilon\) が入る。全実パラメータで無条件に通常の合成則とはしない。 |
| Trace | SH19 Theorem 2.5：半局所 cutoff trace の厳密な漸近公式。CCM07 Theorem 6.1：別の大域 cohomology 上の明示公式。 | cutoff の発散項を引いた有限部分の符号は、元の Hilbert 空間の正性から従わない。 |
| Spectrum | CCM07 Proposition 4.13/Theorem 4.16：全非自明零点が自然重複度付きで trace に現れる。 | 1999 年の Hilbert 実現で臨界零点のみを得る事実と混同しない。全零点実現には急減少関数空間を用い、正定値 Hilbert 実現とはしていない（CCM07 p.2）。 |
| Determinant | AS14 Theorem 2.7 / GAS15 Theorem 4.2：分布的 counting の対数微分から完成 \(\zeta\) を回収。 | この定理は、正定値有限次元 \(H^1\) の Frobenius characteristic polynomial や、自己共役生成子の regularized determinant の定理ではない。今回読んだ資料からその昇格はできない。 |
| Duality | SH19 Lemma 2.2–2.3：加法 Fourier と反転・局所因子の関係。CCM07 (6.9)：\(f^\sharp(g)=|g|^{-1}\overline{f(g^{-1})}\)。 | 反転・関数等式の双対性だけを正の polarization と同一視しない。 |
| Purity | CCM07 Proposition 6.2/Corollary 6.3 は全 test の trace 正値性と RH の **同値定理**。SH19 Conjecture 4.1 は支持を制限した半局所的証明戦略。 | 同値条件の正値性を無条件に与える純粋性定理は、これらの資料には供給されていない。 |

## 算術 site と counting の正確な範囲

AS14 の site は \((\widehat{\mathbb N^\times},\bar{\mathbb N})\)。Theorem 2.6 は \([0,1]_{\max}\) 上の点を
\[
\mathbb Q^\times\backslash\mathbb A_{\mathbb Q}/\widehat{\mathbb Z}^{\times}
\]
と同定し、Frobenius を idèle の scaling と同定する。GAS15 の \(\mathbb Z_{\max}\) と \(\mathbb R_+^{\max}\) を使う版は Theorem 3.8 / Remark 3.9 による。構造半環の版を混ぜない。

GAS15 §4.2 の有限素点寄与は、そこで指定する片側支持の test \(g\) に対して
\[
\sum_{m\ge1}(\log p)g(p^m).
\]
無限素点は principal-value 分布を与える。Theorem 4.2 はこの counting distribution \(N\) から
\[
-\partial_s\log\zeta_{\mathbb Q}(s)
=\int_1^\infty N(u)u^{-s}d^\times u,
\qquad \zeta_{\mathbb Q}(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]
を正規化・分布解釈付きで回収する。通常の有限な点数の列でも、単独の有限次元行列の determinant でもない。同 §4.3 p.17 は、この site の表示を Lefschetz 公式として理解するための適切な **Weil cohomology** を未解決としている。これは下記の既存 cyclic cohomology の不存在を意味しない。

## 全零点を回収する既存 cyclic quotient

CCM07 §4 の入力は \(\mathbb A_K/K^\times\)、その groupoid Schwartz 代数、idèle class group \(C_K\) への restriction。数体での test 空間は (4.20)
\[
\mathbf S(C_K)=\bigcap_{\beta\in\mathbb R}|\cdot|^\beta\mathcal S(C_K).
\]
原点評価と積分が消える部分からの restriction を取り、Definition 4.10 では cyclic module の像の **closure** で商を取る。その cyclic homology が \(H^1\) である。単に零点集合から構成した \(\ell^2\) ではない。

\(K=\mathbb Q\) の \(\widehat{\mathbb Z}^{\times}\)-不変 sector、すなわち自明文字を取り、\(\widehat h(s)=\int_0^\infty h(u)u^s d^\times u\) とすると、Theorem 4.16 の内容は
\[
\operatorname{Tr}\underline\vartheta_m(h)|_{H^1_1}
=\sum_{\rho}m_\rho\widehat h(\rho).
\]
対象は非自明零点全体で、臨界線外も排除せず重複度を含む。一般文字 sector は対応する Hecke \(L\) を扱う。Theorem 6.1 はこの trace の算術側を \(\widehat h(0)+\widehat h(1)\) と全局所 principal values で表す。したがって「exact arithmetic representation がない」という棄却理由は適切でない。ただし今回の照合は、この cohomological trace の意味を、正定値 Hilbert 空間の通常の自己共役 spectrum に強めてはいない。

### 次段で維持する topology・trace の境界

- 自明文字 sector では \(t=\log u\) により test topology を全指数重み付き Schwartz seminorms で表せる。例えば \(\sup_t e^{k|t|}(1+|t|)^N|\partial_t^j h(e^t)|\)、整数 \(k,N,j\ge0\)、を使う Fréchet topology。単一の \(L^2\) weight の閉包へ勝手に置換しない。
- scalar restriction の像は CCM07 Definition 4.14 / (4.37) の \(\mathcal V=\{\sum_{k\in K^\times}\eta(kx):\eta(0)=\int\eta=0\}\)。Definition 4.10 の closure は上記急減少空間／cyclic module の topology におけるもの。**像そのものが閉であるという定理を同定したわけではない。** Lemma 4.15 の quotient 上の convolution を、この closure 規約と共に読む。
- Theorem 4.16 は各 \(h\in\mathbf S(C_K)\) の積分作用 \(\underline\vartheta_m(h)=\int h(a)\underline\vartheta_m(a)d^\times a\) を trace class とする。CCM07 §3.2、§6.1 は Meyer の nuclear-space setting を参照する。これは核型空間での trace theorem の引用採用であり、正定値 Hilbert 空間の Schatten \(S_1\) と独立に同定したものではない。未積分 \(\underline\vartheta_m(a)\)、生成子自身、任意の荒い test にまで trace class を主張しない。
- (4.44) 直後、PDF p.25 の natural multiplicity は零点の位数を trace に数える。これは独立な自己共役作用素の幾何学的 eigenspace dimension や零点の単純性を証明したという意味ではない。本監査では全定理の関数解析的証明の再構成まで行っていない。

### normalized adjoint が条件付きになる正確な場所

以下は原文 (4.47), (6.9) からの短い代数的帰結であり、追加の正値性定理ではない。\(B(f,g)=\operatorname{Tr}\underline\vartheta_m(f\star g)\)、\(H(f,g)=B(f,g^\sharp)\)、\(T_af(u)=f(a^{-1}u)\)、\(a>0\)、と置く。共役線型性は第二変数に置く。test core 上で
\[
(T_ag)^\sharp=aT_{a^{-1}}g^\sharp,
\quad H(T_af,g)=aH(f,T_{a^{-1}}g),
\quad H(T_af,T_ag)=aH(f,g).
\]
従って \(W_a=a^{-1/2}T_a\) は \(H\) を保存する。しかし \(H\) が不定値でもこの等式は成り立つ。正値性を証明し、null space を商にして完成する段階で初めて、これを Hilbert adjoint の式 \(T_a^\dagger=aT_{a^{-1}}\)、\(W_a^\dagger=W_{a^{-1}}\) として使える。生成子 \(\Theta\) の \(\Theta^\dagger=1-\Theta\) はさらに共通微分 domain 上の条件付き表現であり、未検証の全域作用素等式にしない。

同じ点は trace の零点側でも明瞭である：
\[
H(f,g)=\sum_\rho m_\rho\widehat f(\rho)
\overline{\widehat g(1-\bar\rho)}.
\]
関数等式の対称性はこの Hermitian pairing を与えるが、各項を \(m_\rho|\widehat f(\rho)|^2\) とするには \(\rho=1-\bar\rho\) が必要。全 test の非負性は原文 Proposition 6.2/Corollary 6.3 の RH 同値条件そのものである。

なお、この値の pairing は Mellin transform の jet を直接検出しない。従って null quotient と Hilbert completion が、元の cohomological representation の generalized eigenspaces と自然重複度をそのまま保持する、と今回の照合だけでは言えない。これは Theorem 4.16 の重複度付き trace を否定するものではなく、追加の Hilbert 実現へ移す際の未検証義務である。単純零点を黙って仮定しない。

## 半局所 Hamiltonian が供給するもの

SH19 §2.2 の有限 \(S\ni\infty\) では
\[
A_S=\prod_{v\in S}\mathbb Q_v,\quad
X_S=A_S/\mathbb Q_S^\times,\quad
C_{\mathbb Q,S}=A_S^\times/\mathbb Q_S^\times.
\]
その特定の \(L^2(X_S)\) 構成と Fourier を使う。\(R_\Lambda=\widehat P_\Lambda P_\Lambda\) に対し Theorem 2.5 は
\[
\operatorname{Tr}(\vartheta_a(h)R_\Lambda)
=2h(1)\log\Lambda+
\sum_{v\in S}\int'_{\mathbb Q_v^\times}
\frac{h(w^{-1})}{|1-w|}d^\times w+o(1).
\]
仮定は compactly supported \(h\in\mathcal S(C_{\mathbb Q,S})\) と所定の basic additive character。\(R_\Lambda\) は一般に正の直交射影ではない。

さらに Lemma 3.4/Corollary 3.5 の符号機構は Hardy subspace の不変性／inner-function 条件を要する。実際の局所因子はその条件を満たさず、Fact 3.6 は提案された一般不等式 (3.1) の不成立を示す。これを「unitary だから Weil positive」と修復することはできない。

## 最終不足と採否

CCM07 の pairing を \(\langle f,g\rangle=\operatorname{Tr}\underline\vartheta_m(f\star g)\) とすると、欠けている直接の主張は
\[
\langle f,f^\sharp\rangle\ge0\quad\text{for every }f\in\mathbf S(C_K).
\]
Proposition 6.2/Corollary 6.3 はこれを全 Hecke \(L\) の RH と同値化している。\(\mathbb Q\) の自明文字 sector では通常の Weil criterion に戻る。radical を商にすることも、双対性も、この符号を供給しない。

SH19 §4 の対応する正確な未完部分は Conjecture 4.1：\(S=\{\infty\}\cup\{p:p<q\}\) で支持 \((q^{-1/2},q^{1/2})\) の全 test を扱う Weil inequality。周囲の定式化では pole-annihilation 条件 (4.1)、\(\int h_1(x)x^{\pm1/2}d^\times x=0\)、も維持する。任意の大きさの支持を覆うよう \(q\) を増やせる定理が必要であり、固定 \(S\) の trace formula だけで全域正値性は出ない。

**初期比較の判定：算術的起源・全零点の trace 回収は既知の有効な条件なし入力として認める。一方、純粋性／正の polarization に当たる最後の符号定理は未供給。** この bounded audit から新たな作用素を製造したり、既存の全域 Weil 正値性 gap が解消したと主張したりしない。RH を仮定せず同じ quotient 上の符号を算術から得る補題がなければ、主証明への距離は短縮しない。
