**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/arithmetic_comma/notes/phase_statistics_gate.md` · Original SHA-256: `d0f12f867e5aa1f56f7814971e61a853cb235334a7d960f29deb096c025860e3`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Distinguished-phase obstruction: direct proof and scope

2026-09-30. This note is a direct finite-dimensional calculation, not a novelty claim. RH remains OPEN. It does not change the Euler factors of the actual target; comparison coefficients are used only as falsifiers of proposed general implications.

## PS1. Identical phase laws, different coefficient sums

Fix \(X\ge1\), \(P=\{p:p\le X\}\), and the actual squarefree cutoff
\[
 \mathcal A_X=\{n\le X:\mu(n)^2=1\},\qquad N_X=|\mathcal A_X|.
\]
For \(n\in\mathcal A_X\), let \(\kappa(n)\in\{0,1\}^{|P|}\) be its prime exponent vector. Define
\[
 C_X(z)=\sum_{n\in\mathcal A_X}z^{\kappa(n)},\qquad
 F_X(z)=\sum_{n\in\mathcal A_X}\mu(n)z^{\kappa(n)}.
\]
The weighted half-space cutoff is retained exactly in both polynomials. Since
\(\mu(n)=(-1)^{|\kappa(n)|}\),
\[
 \boxed{F_X(z)=C_X(-z).}                                      \tag{PS1}
\]
Multiplication by \((-1,\ldots,-1)\) preserves normalized Haar measure. Consequently \(F_X\) and \(C_X\), as complex-valued random variables on the torus, have identical distributions. In particular all mixed moments, all \(L^q\) norms, and every bounded continuous statistic of their values coincide.

For the continuous flow \(z(t)=(e^{-it\log p})_{p\in P}\), unique factorization gives nonzero frequency for each nonconstant torus character. Its time average tends to zero. Approximation by trigonometric polynomials then proves the same Haar limit for every continuous observable. Thus the two polynomials have identical limiting time distributions for each fixed \(X\).

Nevertheless,
\[
 C_X(1)=N_X,\qquad F_X(1)=M(X),\qquad F_X(-1)=N_X.              \tag{PS2}
\]
Also
\[
 \int|F_X|^2dm=\int|C_X|^2dm=N_X.                             \tag{PS3}
\]
Therefore RMS of order \(\sqrt{N_X}\) in time cannot imply a bound of that size at the distinguished identity phase: the positive-coefficient example has value \(N_X\) there, with exactly the same phase law. Elementary squarefree counting gives \(N_X=6X/\pi^2+O(\sqrt X)\), though only \(N_X\to\infty\) is needed for this obstruction.

Dense recurrence of the same continuous flow gives an additional exact statement:
\[
 \boxed{\sup_{t\ge t_0}\left|\sum_{n\le X}\mu(n)n^{-it}\right|=N_X
        \quad\text{for every fixed }t_0\ge0.}                \tag{PS4}
\]
The upper bound is the triangle inequality; density after any time \(t_0\) approximates the phase \((-1,\ldots,-1)\). This is a supremum, not necessarily an attained maximum. It does not contradict small (M(X)) at \(t=0\), and gives no useful bound on the first large excursion time.

**Exact scope.** Marginal phase laws, or even random-initial-phase finite-time joint laws, cannot distinguish the two coefficient systems: the sign flip commutes with the flow. A deterministic joint correlation with a fixed cutoff/reconstruction kernel can distinguish them. The exact Haar bridge uses just such a correlation. No impossibility theorem for all phase methods follows.

## PS2. Finite-time error and a weighted comma distribution

For \(a_n\in\mathbb C\), supported on \(n\le X\),
\[
 \frac1T\int_0^T\left|\sum_n a_nn^{-it}\right|^2dt
 =\sum_{m,n}a_m\overline{a_n}
 e^{iT\log(n/m)/2}\operatorname{sinc}(T\log(n/m)/2),           \tag{PS5}
\]
where \(\operatorname{sinc}(0)=1\). This includes phase, multiplicity, coefficient sign, and the original cutoff. If \(m<n\le X\),
\[
 \log(n/m)\ge(n-m)/n\ge(n-m)/X.
\]
For \(|a_n|\le1\), setting \(N=\lfloor X\rfloor\) gives the elementary sufficient bound
\[
 \left|\frac1T\int_0^T|\cdots|^2dt-\sum_n|a_n|^2\right|
 \le\frac{4X}{T}\sum_{h=1}^{N-1}\frac{N-h}{h}
 =O(X^2\log(2X)/T).                                        \tag{PS6}
\]
This is neither optimal nor a lower bound on the averaging time needed. Even a perfect mean-square estimate would not overcome PS1.

A precise signed "all commas" object, rather than a single smallest gap, is
\[
 \mathcal D_X=\sum_{a,b\in\mathcal A_X}\mu(a)\mu(b)
                 \delta_{\log a-\log b}.                    \tag{PS7}
\]
Its Fourier transform is \(|F_X(z(t))|^2\). It is the pushforward of the finite signed measure with atoms \((\log a,\log b)\), both coordinates in \([0,\log X]\); this lifted measure retains cutoff locations separately. Equation PS5 is its pairing with the averaging kernel. The diagonal mass is \(N_X\). Off-diagonal atoms can have either sign. Replacing them by absolute values loses the cancellation being sought; asserting a small signed kernel integral without an arithmetic proof just renames that problem.

Higher moments include exact multiplicative resonances. For example \(2\cdot15=3\cdot10\) produces a fourth-moment diagonal although the four integers are distinct. This does not violate independence of prime logs: after combining prime exponents the relation is the zero vector. For every equality of products of squarefree integers, the product of all participating Möbius signs is (+1). Indeed both sides have the same total prime exponent count. This also proves directly that every even absolute Haar moment in PS1 is identical for the signed and positive models.

## PS3. Evaluation norm, not an absent Hilbert norm

Let \(V_X\subset L^2(\mathbb T^{|P|})\) be spanned by the \(N_X\) cutoff monomials. They are orthonormal. Evaluation at \(z=1\) has exact norm \(\sqrt{N_X}\), with representer \(C_X\). Therefore
\[
 |F_X(1)|\le\sqrt{N_X}\,\|F_X\|_2=N_X.
\]
The square-root time RMS loses its gain under point evaluation. This is a finite-dimensional identity, not a matter of choosing a more convenient completion. In the infinite \(H^2\) model, boundary evaluation is unbounded, as detailed in the Fourier bridge note. A new bound must control the actual arithmetic correlation with the evaluation/cutoff vector, not simply its norm.

## PS4. Two-prime comma versus Boolean cutoff

With only primes 2 and 3, the squarefree model has exactly four atoms (1,2,3,6). There is no growing family of exponent pairs ((m,n)) in that Boolean model. Large coefficients in \(m\log2-n\log3\) enter the Fourier analysis of torus observables or long recurrence times; they do not add squarefree states to the original problem. Replacing the Boolean exponents by arbitrary nonnegative integers changes the arithmetic target. Assigning alternating signs to prime powers produces Liouville-type coefficients, not Möbius coefficients.

The exact toy discrepancy is (1,0,-1,0) on the successive ranges ([1,2),[2,3),[3,6),[6,\infty)). Fixed finite-prime subsystems eventually have total discrepancy zero. A useful passage to Mertens requires growing prime sets, uniformly controlled kernels, and their nonrectangular cutoff.

## PS5. Experiments and independent audit

`../experiments/check_phase_bridge.py` checks exact subset signs, the two- and three-prime step tables, six exact Haar moment cases, higher-moment product resonance, and a cutoff consisting of primes in ((50,100]). It also computes finite-time integrals from PS5 and samples two small torus flows. Sampled box frequencies are diagnostics only; no growth fitting, statistical hypothesis test, or finite verification is used as an RH proof.

DESTROYER independently verified PS1, the distinction between marginal law and fixed-kernel correlation, and PS4's supremum argument. The present note records these elementary obstructions without claiming that they are new to the literature.

**Decision:** exact non-resonance and even full phase-distribution knowledge do not supply the missing distinguished-phase estimate. Keep the exact bridges; reject distribution-only cancellation and uniform-in-all-time square-root proposals. The remaining arithmetic correlation is not bounded by this track.


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_phase_bridge.py` — SOURCE REFERENCE NOT INCLUDED
