**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/phase3-independent-audit.md` · Original SHA-256: `54314913dd6943d69ae0e9408ebb1a415869a608da47700953be9f64e2ecd893`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase III structural tests — independent scope / mathematics audit

2026-09-29。DESTROYER の読み取り監査。
対象は `research/notes/phase3_structural_tests.md` の M1–M3、
`experiments/scripts/phase3_structural_checks.py` と対応 JSON、既存の Deninger／有限体比較。
未完成の main document 全体は対象外。RH の証明・反証、全プログラムの否定を意味しない。

**判定：PASS。初回の M3 の限定要求は本文へ反映済み（RESOLVED）。**
修正後の M1–M3 と、追記された M2 の CCM 命題・sector 平均化を再読した。
検査した範囲に重大な未修正点はない。CCM の元の全射性定理の再証明は監査範囲外。

## A. RESOLVED：定数 mode 除去前後で distribution trace は異なる

\(T_p=\log p\)、\(U_t\) を circle の translation とする。
\(h\in C_c^\infty((0,\infty))\)、\(c_h=\int h(t)dt\) と書けば、各 circle では

\[
 \operatorname{Tr}\left(\int h(t)U_tdt\right)
 =\sum_{k\in\mathbb Z}\int h(t)e^{2\pi ikt/T_p}dt
 =T_p\sum_{m\ge1}h(mT_p).
\tag{A1}
\]

右辺は \(p>e^{\sup\operatorname{supp}h}\) で0。
したがって **定数 mode を含む元の circle trace** の素数和は正時間に局所有限である。

一方、各 circle の定数 mode を除いた場合は

\[
 \operatorname{Tr}\left(\int h(t)U_t^{\perp}dt\right)
 =T_p\sum_{m\ge1}h(mT_p)-c_h.
\tag{A2}
\]

\(c_h\ne0\) なら、大きい全素数で同じ \(-c_h\) が残るので、
この除去後の局所 trace の素数和自体も発散する。
修正後の本文は、存在する分布和を (A1) に限定し、(A2) の素数和の発散も明記した。
この初回指摘は解決済み。これは direct sum の問題を修復する指摘ではなく、
除去後には分布 trace の義務も失うことを明確にする指摘。

## B. M1：all-n の厳密検算

\(F_1\) の特性多項式は \(X^2-7X+9\)。
\(\alpha_+\alpha_-=9\) と
\(1<\alpha_-<2<3<\alpha_+<6\) が成立し、purity は失敗する。
\(9T^2P(1/(9T))=P(T)\) は分子・分母の両方に成り立つので、表示された FE も正しい。

整数性は \(Z(T)\in1+T\mathbb Z[[T]]\) から Euler 因子を低次から順に取り出す
帰納法で示せる。各段階で指数は整数、log 比較で Möbius 式が得られる。
有限 n のチェックをこの証明の代替としていない。

\(N_m>0\) は \(m=1\) で3、\(m\ge2\) では
\(9^m-6^m-2^m>0\) から従う。
proper divisor は全て \(\lfloor n/2\rfloor\) 以下なので、本文の \(nb_n\) の下界は正しい。
\(9^n\) で割った4項の上界は \(n\ge2\) で減少し、\(n=2\) にて
\(409/648<1\)。従って全 \(n\) で \(b_n>0\)。
\(b_n\) 個ずつの有限 n-cycle の disjoint union は要求された固定点数を持つが、
finite-type curve を構成したことにはならない。

交代形式 \(J\)、不定対称形式 \(H\)、\(\det H=-13\)、
\(F_1^\dagger F_1=9I\)、\(\operatorname{Tr}(A^\dagger A)=-2\) は独立計算で一致。
この \(\dagger\) を幾何学的 Rosati と呼ばない修正も適切。

有限次元で \(F^*MF=qM\), \(M>0\) は
「semisimple かつ全固有値の絶対値 \(\sqrt q\)」と同値。
固有値の絶対値だけから Jordan block の排除はできない、という留保は必要であり正しい。
幾何的 polarization／functoriality まで同値と拡大していない。

## C. M2：LF quotient の topology

各固定 support 上で \(\ell_a\) は sup norm で連続だから、test function の LF 位相でも
連続。従って \(N_a\) は LF 閉。
\(\ell_a(T_tf)=e^{at}\ell_a(f)\) より全実数 t の作用で不変。
\(\ell_a(g)=c\ne0\) のとき \(z\mapsto zg/c\) は連続 section なので、
\(E/N_a\simeq\mathbb C\) は代数的だけでなく topological にも成立する。

表示された \(g_R\) は \(\ell_a(g_R)=1\)、
\(\|g_R\|_2=e^{-aR}\|g\|_2/|c|\to0\)。
\(N_a\) は \(L^2\) 稠密であり、Hilbert quotient は0になる。
非零な1次元商の character \(e^{at}\) は、いかなる正定値 Hermitian norm でも unitary
にはならない。これは実際の算術 quotient の失敗を証明した模型ではない。

指数評価 \(\ell_a\) は一般の Schwartz 空間全体には定義できない。
本文は LF と明記しており、その点も適切。
\(N\subset\operatorname{rad}B\) が代表元非依存の form descent の必要条件であることと、
quotient infimum norm を別に作ることの区別にも問題はない。

### C2. 追加された actual arithmetic の結果：引用採用と独立な帰結の区別

[CCM07 v1, Proposition 6.4(1)–(2), (6.12)](https://arxiv.org/html/math/0703392)
の本文・証明を直接照合した。原命題の二つの入力は、restriction の像 \(V\) が
trace pairing の radical に含まれること、および任意の test function \(f\) と
\(\epsilon>0\) に対し、ある \(v\in V\) によって

\[
 \int_{C_{\mathbb K}}|f(u)+v(u)|^2|u|\,d^\times u<\epsilon
\]

とできることである。原著の (2) の証明は、先行する Connes 論文 Appendix 1 の
\(\delta=0\) での \(\mathfrak E\) の全射性を引用している。
今回、その元の全射性証明を独立に再証明・全面再監査したとはしない。

この既知入力から、当該 norm による test-space の Hilbert completion では
\(V\) が稠密で、商 seminorm が全 class で0となる帰結は正しい。
\(T_af(u)=f(a^{-1}u)\) なら変数変換から norm の二乗は \(|a|\) 倍になる。
本文の \(a^{-1/2}T_a\) は正の modulus \(a\) をパラメータにした規約で正しい。
また、\(V\) を radical に持つ非零 pairing がこの norm で連続なら稠密性により0となる。
したがって同じ pairing を当該 ambient norm に対する一様 bounded comparison で
正値化する案は使えない。別 norm・別偏極・unbounded form 全般の否定にはならない。

\(\mathbb K=\mathbb Q\)、コンパクト単位群 \(K=\widehat{\mathbb Z}^{\times}\)
には正規化 Haar 確率測度を取る。\(|k|=1\) なので
\(P_0f(u)=\int_Kf(ku)\,dk\) は当該 Hilbert norm の収縮射影。
restriction の \(K\)-同変性に加え、Bruhat–Schwartz 関数の平均
\(\eta_0(x)=\int_K\eta(kx)\,dk\) は同じ空間と
\(\eta_0(0)=\int\eta_0=0\) を保つ。有限 adele 変数での開 stabilizer を用いれば、
この平均が依然 Bruhat–Schwartz であることも確認できる。
従って \(P_0V\subset V_0\) かつ、\(K\)-不変な \(f\) について

\[
 \|f+P_0v\|_{\rm ar}=\|P_0(f+v)\|_{\rm ar}
 \leq\|f+v\|_{\rm ar}.
\]

よって ζ に対応する自明な compact-unit sector でも同じ商 norm の消失が従う。
非コンパクトな modulus 群全体を平均しているのではない。
この sector 帰結・norm 計算は独立に検算した。原命題の引用採用、generic LF 模型、
actual arithmetic での特定 norm の失敗を本文が別々に記載した scope は適切である。

## D. M3：作用素・trace・weight

各 \(L^2(C_p)\) 上の self-adjoint translation generator は、符号規約を固定すれば
固有値 \(2\pi k/T_p\) を持つ。
direct sum の定義域は二乗 graph norm が総和可能なベクトルで定まる。
定数 mode が無限重複するので resolvent は compact ではない。
全定数 mode を除いても \(2\pi/T_p\to0\) の直交固有ベクトル列があり、
resolvent の compactness は回復しない。

\(S_h=\int h(t)U_tdt\) は bounded operator だが、\(c_h\ne0\) なら
元の直和では固有値 \(c_h\) が無限重複する。
定数 mode 除去後も第一 mode の固有値
\(\int h(t)e^{2\pi it/T_p}dt\to c_h\) なので compact でなく、従って trace class でない。
各 block の trace-class 性や (A1) の有限和とは矛盾しない。
block trace の符号相殺を絶対 trace norm の総和へ格上げできない。

\(\log2\) と \(\log3\) の非整比、prime-power distribution、収束域の Euler 積は正しい。
この失敗が否定するのは提示された素朴な直和接着であって、全ての cohomological gluing
や regularized determinant の可能性ではない、という scope は維持されている。

local trivial motive の Frobenius 値1／weight 0 と、global arithmetic \(H^1\) に
求められる weight 1 は別の対象。両者を区別した本文は正しい。

Gamma tower は、\(\Theta_\infty e_n=-2ne_n\) より
\(\eta_s(w)=\pi^w\zeta_H(w,s/2)\) となり、

\[
 -\eta_s'(0)=\frac12\log2+\frac{s}{2}\log\pi-\log\Gamma(s/2).
\]

従って \(\det_\zeta((s-\Theta_\infty)/(2\pi))=\sqrt2/\Gamma_\mathbb R(s)\) は正しい。
この \(\sqrt2\) と Deninger の別の completed-factor 規格化との関係は
`research/notes/phase3_deninger_audit.md` と整合している。
局所 Gamma の具体構成が既にあることと、global \(H^1\) の偏極が未供給であることを
混同していない。

## E. 数値 script と再現範囲

script の読み取り、exact integer／Fraction 部分、4次中心差分の係数を確認した。
script 全体の再実行は JSON を上書きするため行っていない。
script/result の hash 対応は read-only に再計算して一致を確認した。

- script SHA256: `bcf2b66ee7c2db4544fc6b90ea2ca2f8e8390babf8bd1c990122718fd7ff26b3`
- JSON SHA256: `df77df4681843934ad1c446667a0f588876b6f6f5d50ba24c320da4531e33c2d`

\((f(-2h)-8f(-h)+8f(h)-f(2h))/(12h)\) は正しい4次差分。
出力の Gamma 誤差は mpmath の非認証診断であり、表示桁が enclosure とはされていない。
初回 tiny-step の不調を fixed-step に変えても、これを解析式の証明に昇格させていない。
全 n の閉点正性と Gamma の determinant は上述の解析・代数計算を根拠とする。

**結論:** 修正済みの M1–M3 は、検査した範囲で PASS。
M2 の追加は既知の CCM 命題に基づく特定 Hilbert norm の障害であり、
元の全射性定理の新証明ではない。いずれも actual RH や外部研究全体の反証ではない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/scripts/phase3_structural_checks.py`](../../../../artifacts/experiments/scripts/phase3_structural_checks.py)
- [`research/notes/phase3_deninger_audit.md`](../../../reports/research/notes/phase3_deninger_audit.md)
- [`research/notes/phase3_structural_tests.md`](../../../reports/research/notes/phase3_structural_tests.md)
