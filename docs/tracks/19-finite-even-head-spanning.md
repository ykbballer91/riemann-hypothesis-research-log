# 19. Finite even Fourier heads — rank and conditioning

**STATUS: RIEMANN HYPOTHESIS OPEN**

Update recorded 2026-09-30, after the even-L2 cyclicity result. This update completes **Priority 2 only**. It does not start growing-order asymptotics or full-ground capture.

## Starting question and exact object

How much of a fixed finite even Fourier head is reached by restricting the actual theta-kernel derivatives to a window and projecting them? Use the recorded normalization $\widehat k(x)=\Xi(x)/4$, with $\Xi(x)=\xi(1/2+ix)$, and $R_af=1_{[-a,a]}f$.

The head $E_N^+$ has dimension $N+1$. Its orthonormal basis, zero outside the window, is

$$b_0(t)=(2a)^{-1/2},\qquad b_n(t)=(-1)^na^{-1/2}\cos(\pi nt/a),\quad 1\le n\le N.$$

The actual columns are $P_NR_ak^{(2j)}$. Full-line Fourier samples are a separate ideal model: the actual interval projection already satisfies $P_N(1-R_a)=0$. Confusing that projection with full-line sampling would make the proposed tail comparison invalid.

## Auxiliary results retained

For the ideal model, put $\omega_n=\pi n/a$ and $t_n=\omega_n^2$. Its matrix is a diagonal Xi-weight matrix times the Vandermonde matrix $(t_n^j)$ and the column sign matrix. If $r$ of the $N+1$ Xi samples are nonzero, its exact rank is $\min(m+1,r)$. Without a grid hit, the minimal order is $m=N$.

An exact Xi grid zero removes one ideal row, regardless of its multiplicity. The zero-frequency row is nonzero. Opposite frequencies have already been identified in the even sector. None of these statements assumes RH or simple zeros.

For the actual sharp-support columns the boundary terms remain. Writing $B_{nj}=\langle R_ak^{(2j)},b_n\rangle$ gives

$$B_{nj}=-\omega_n^2B_{n,j-1}+d_nk^{(2j-1)}(a),\qquad d_0=\sqrt{2/a},\quad d_n=2/\sqrt a\ (n\ge1).$$

Thus an ideal zero row need not be an actual zero row. The derivatives are taken before support restriction; differentiating the sharply cut function would introduce boundary distributions and change the problem.

The written argument establishes:

- For **each fixed** $a>0,N$, some finite initial derivative family spans the actual head exactly. Cyclicity and finite dimensionality give existence, without an explicit general order bound.
- For **each fixed** $N$, the minimal prefix $m=N$ spans for all sufficiently large $a$. It can fail only at a finite set of positive window widths. The locations, number, and possible emptiness of that set remain undetermined.
- A concrete tail-versus-smallest-singular-value inequality certifies $m=N$ on stated finite parameter ranges. It does not use a floating determinant as a rank proof.

In particular, an Arb interval calculation certifies full rank for every $a\in[1.499999,1.500001]$ with $N=m=4$, and every $a\in[1.999999,2.000001]$ with $N=m=6$. These are certificates for finite column rank and raw-coordinate singular-value lower bounds, **not** for Weil positivity or physical-Gram singular values.

## Conditioning is a separate obligation

Lagrange cardinal polynomials give an explicit upper bound $L$ on the ideal inverse norm. An analytic theta-tail majorant gives $\|E_{\mathrm{tail}}\|\le\tau$. Then $L\tau<1$ implies

$$\sigma_{\min}(B)\ge L^{-1}-\tau>0.$$

The arithmetic derivation is accompanied by known Vandermonde and discrete-orthogonal-polynomial tools; those tools are not presented as new research. See [references](../references.md).

Changing from monomials to orthogonal polynomial coordinates preserves the span, but does not automatically improve the physical map. The record distinguishes raw coefficient norm, the projected head Gram, and the global or support-restricted physical $L^2$ Gram. Whitening by the head Gram alone would conceal lift cost.

For fixed $m=N$ and $a\to\infty$, the raw smallest singular value is $\Theta_N(a^{-2N-1/2})$ and the raw condition number is $\Theta_N(a^{2N})$. Global physical-Gram normalization does not remove that small-singular-value order. Exact spanning therefore does not establish uniform stability.

High-precision numerical tables are explicitly diagnostic. Their physical Gram uses finite theta and integration cutoffs. The separately documented Arb bounds are the finite certificates; they are not inferred from agreement of floating calculations.

## Why the work stopped

Every vector in a fixed head, including any even ground vector in that head, can consequently be expressed in the **projected** derivative hierarchy using sufficiently many columns. This algebraic inclusion is not a theorem selecting the ground, controlling its coefficients, or comparing a moving ground with $k$.

The needed order, physical lift cost, form-norm error, and constants in the fixed-order hierarchy have not been controlled in a joint limit. **Growing-order selection, full even-ground capture, parity/ES, G*, and RH remain open.** Priority 3 was not started.

## Canonical records

- [Main scoped report](../../archive/reports/research/full_ground_capture/priority2/finite_even_head_spanning.md)
- [Algebraic rank and finite exceptions](../../archive/reports/research/full_ground_capture/priority2/notes/algebraic_rank.md)
- [Tail and conditioning proof](../../archive/reports/research/full_ground_capture/priority2/notes/tail_conditioning.md)
- [Literature and coordinate audit](../../archive/reports/research/full_ground_capture/priority2/notes/conditioning_literature.md)
- [Numerical diagnostics and their limits](../../archive/reports/research/full_ground_capture/priority2/notes/diagnostics.md)
- [Interval certificate code](../../artifacts/research/full_ground_capture/priority2/experiments/certify_tail_criterion.py) and [recorded output](../../artifacts/research/full_ground_capture/priority2/experiments/tail_certificates.json)
- [Independent internal audit](../../archive/audits/proofs/audits/full_ground_finite_head_adversarial.md)
- [Dated state](../../data/source-records/research/full_ground_capture/priority2/state.json)

The audit is an internal AI-agent review, not external peer review or Lean formalization. No novelty claim or implication that RH is nearly proved is attached to these auxiliary results.
