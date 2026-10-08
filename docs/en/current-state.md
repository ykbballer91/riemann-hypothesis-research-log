# Current state: what is established and what remains

**STATUS: RIEMANN HYPOTHESIS OPEN**

The latest state is **2026-10-08, at the end of Cycle 17**. This release adds the [Cycles 6–17 update](updates/2026-10-08-cycles-6-17.md) and [current state record](../../data/current-state-2026-10-08.json). [CORE-S](updates/2026-10-07-core-s.md), the [October 5 joint transfer](updates/2026-10-05-joint-transfer.md) and earlier records remain dated history.

## The adopted direct route

The central obligations are **capture in the full even ground space (CAP)** and **strict parity ordering (PAR)** on the same resolving cofinal sequence. Both are unproved: **2 → 2**. This counts obligation types in the chosen sufficient route, not distance to RH or a universal minimum number of propositions.

$$a_j\to\infty,\qquad\frac{a_j}{N_j+1}\to0,$$

$$\mathrm{CAP}:\quad\|(I-G_{+,j})P_{N_j}R_{a_j}k\|_2\to0,$$

$$\mathrm{PAR}:\quad e_-(a_j,N_j)>e_+(a_j,N_j)\quad\text{eventually}.$$

$$\mathrm{CAP}+\mathrm{PAR}\Longrightarrow\mathrm{CORE\text{-}S}/\mathrm{ES}\Longrightarrow\text{adopted transfer}\Longrightarrow\mathrm{RH}.$$

$G_{+,j}$ is the physical L² orthogonal projector onto the entire even ground eigenspace. Results on separate sequences cannot be joined. CORE-S supplies finite simplicity from strict parity in the actual matrix family; the independent $\Delta_+>0$ condition remains removed. The adopted transfer is conditional on additional real-zero structure.

## Latest auxiliary results and their limits

Cycle 15 proved that **prime-only** minimization cannot capture a fixed nonzero even L² target on any resolving cofinal sequence. This is not a counterexample to capture for the completed Weil form.

Cycle 16 identified the completed endpoint residual. Cycle 17 established unconditionally that it takes both signs arbitrarily far out for every fixed nonzero real $h\in C_c^\infty(0,b)$. The result extends to fixed smooth linear kernels.

**A fixed-trial difference is not the difference of the true minima.** This oscillation excludes fixed-profile one-sided trial ordering for all sufficiently large continuous parameters. It does not extend to every cofinal subsequence, adaptive profiles, actual ground crossings or a disproof of CAP/PAR.

## Unproved status

- **CMP: NOT ESTABLISHED.**
- **ES: NOT ESTABLISHED.**
- **EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**
- **COFINAL COMPATIBILITY: NOT ESTABLISHED.**
- **COFINAL INCOMPATIBILITY: NOT ESTABLISHED.**

**CASE D — CMP OPEN + ES OPEN.** The earlier import audit delegated 12 of 19 items to general theory or fixed-scope results; it did not solve 12 RH obstacles. Cycles 6–17 closed 0 adopted CAP/PAR obligations.

Ordinary L² proximity alone does not yield complex comparison. The adopted ES-plus-strong-L² transfer uses additional real-zero structure. The ES-independent [earlier CMP-R](updates/2026-10-01-cmp-es.md) remains a separate rate-based sufficient condition. The simple-even certificate at $c=13,N=4$ still covers only that point.

## Next question and stopping point

Actual arithmetic input proving capture and strict parity on one sequence remains missing. Cycle 17 passed independent internal AI review in its fixed-kernel scope; this is not external peer review, formal verification or academic approval. This publication release stops without Cycle 18, new proof exploration or numerical work.

[Mathematical details and sources](updates/2026-10-08-cycles-6-17.md) · [Roadmap](roadmap.md) · [Timeline](timeline.md)

## Retained snapshot — 2026-09-30, before the import/CMP/ES update

The following earlier summary is preserved as history, not as an expanded list of current main tracks. Its evidence is mapped in [source-map](source-map.md).

## Fixed finite derivative spaces

Set $a=\log\lambda$, $Y=\pi\lambda^2$, and

$$\mathcal R_m=\mathrm{span} \lbrace k,k'',\ldots,k^{(2m)}\rbrace,\qquad \widehat k(x)=\Xi(x)/4.$$

The hierarchical-selection record establishes a support-only selection theorem for **each fixed finite $m$**: the minimizing direction within the restricted family tends to $k$. For the canonical support restriction followed by Fourier projection, the same restricted conclusion is obtained under

$$\liminf\frac{N}{aY}>\frac4{\pi^2}.$$

This is a sufficient resolution condition. The record does not identify it as necessary or optimal. Constants in a fixed-$m$ statement have not been made uniform for $m\to\infty$. See [hierarchical selection](tracks/17-hierarchical-selection.md).

## Unconditional cyclicity

The subsequent auxiliary theorem states

$$\overline{\mathrm{span} \lbrace k^{(2j)}:j\ge0\rbrace}^{L^2}=L^2_{\mathrm{even}}(\mathbb R).$$

The proof uses exponential integrability of $|\Xi(x)|^2dx$, a polynomial-density argument, and Plancherel. It does not assume RH or simple zeros. Even polynomials are dense in the **even** weighted sector, not in the entire weighted space. See [cyclicity](tracks/18-even-l2-cyclicity.md).

Qualitative $L^2$ density does not give a uniform approximation rate for a changing ground state. It also does not establish density in a Weil form norm, stability of a finite derivative-column system, or convergence of Fourier transforms throughout a complex strip.

## Fixed finite even heads

The [Priority 2 update](tracks/19-finite-even-head-spanning.md) proves that each fixed head $E_N^+$, of dimension $N+1$, is exactly spanned by a sufficiently long initial derivative family after sharp restriction and projection. The ideal no-tail rank is $\min(m+1,r)$, where $r$ counts nonzero Xi grid samples. Without a grid hit, the ideal minimal order is $m=N$.

For each fixed $N$, the actual minimal prefix $m=N$ works for all sufficiently large windows; the exceptional positive window widths form a finite, not explicitly determined set. Analytic tail bounds plus Arb arithmetic certify two explicit small parameter intervals. These are auxiliary finite-rank results. Physical-Gram diagnostics are distinct from those certificates.

Exact spanning does not give uniform conditioning: with $N=m$ fixed, the physical smallest singular value still decays in the large-window limit. No quantitative order bound or form-norm estimate for a moving ground follows.

## What remains open

1. An explicit optimal derivative cutoff at every parameter, and uniform quantitative conditioning/lift bounds for changing finite heads. The fixed-head exact-spanning existence theorem and specified finite certificates are established.
2. Bounds on every relevant constant when the derivative cutoff $m$ grows with $a,N$.
3. Quantitative capture of a **parameter-dependent full finite even ground state in the joint limit**, rather than fixed-head algebraic representation or minimization within a fixed trial space.
4. The needed relation between even and odd ground levels, together with a simple/even lowest state along the required approximation sequence (the recorded ES condition).
5. The normalized transform comparison $G^*$ between the actual Weil ground state and the prolate proxy, on the complex sets required for zero preservation.
6. Transfer to the actual $\Xi$ through correctly normalized, locally uniform convergence.

None of the auxiliary results above bypasses these obligations. The [roadmap](roadmap.md) separates established arrows from open ones.

## Evidence boundaries

These are written auxiliary arguments with internal independent AI audit records. Selected earlier Lean declarations formalize particular elementary lemmas; they do not formalize the current entire research chain. Numerical overlap, finite spectral agreement, source-preservation checks, and publication validation have their own narrower scopes.

No new unconditional bound on the real parts of all zeta zeros has been obtained here. No percentage of RH completion is assigned.
