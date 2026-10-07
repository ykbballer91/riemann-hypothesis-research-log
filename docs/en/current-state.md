# Current state — what is established and what remains open

**STATUS: RIEMANN HYPOTHESIS OPEN**

Latest public update: **2026-10-07**. Research completed: **2026-10-06**. CORE-S derives simplicity of the even ground from strict parity ordering using the known commutator structure of the actual finite Weil matrices. A [new state record](../../data/current-state-2026-10-07.json) is added; the [2026-10-05 state](../../data/current-state-2026-10-05.json) and [earlier record](../../data/research-state.json) are preserved.

## The selected direct route

**CMP**, complex comparison between the actual finite Weil ground and the prolate proxy, and **ES**, eventual simplicity and evenness of that ground, both remain open.

CORE-S shows that $e_+<e_-$ forces a one-dimensional even ground eigenspace in the actual finite family. ES is therefore equivalent to strict parity ordering; the internal even gap $\Delta_+>0$ no longer requires an independent proof. The current joint sufficient route is **theta-kernel capture + strict parity on the same resolving cofinal sequence → ES → adopted transfer → RH**.

## Current boundary and next action

Actual capture and eventual strict parity ordering on a cofinal sequence remain unproved. Neither compatibility nor incompatibility on the same sequence has been established. The finite conditional simplicity result supplies neither a uniform spectral gap nor eventual ES.

General L² convergence alone does not imply complex convergence. The adopted joint transfer uses the additional real-zero, real-type and exponential-type structure obtained under ES. The earlier ES-independent CMP-R remains a separate rate-based sufficient condition.

The research questions concern capture and parity ordering on that same sequence. This task stops at synchronizing the completed result with the public record; it starts no proof search or numerical investigation.

## Technical details of the latest update

**CASE D — CMP OPEN + ES OPEN.** The earlier **12 of 19 items** refers to delegated generic or fixed-scope proofs, not 12 solved RH obstacles. This result removes the independent simplicity check; newly discharged asymptotic obligations for the actual Weil family remain **0**.

- For every $a>0$ and integer $N\ge1$, $\mathrm{ES}(a,N)\iff e_-(a,N)>e_+(a,N)$. The finite lemma passed a separate internal audit; that is not external peer review.
- With $G_{+,j}$ the orthogonal projector onto the entire even ground eigenspace, the open joint proposition is $C_j=\|(I-G_{+,j})P_{N_j}R_{a_j}k\|_2\to0$ and eventual $e_->e_+$ on one sequence with $a_j\to\infty$ and $a_j/(N_j+1)\to0$.
- CORE-S removes the separate $\Delta_+>0$ condition, without proving a uniform gap bound. The certificate at $c=\lambda^2=13$, $N=4$ remains a single-endpoint result.
- The October 5 proxy-based capture condition and its ordinary projection estimates are retained. The raw proxy is not assumed exactly even. Finite diagnostics are not promoted to asymptotic proofs.
- The joint transfer applies to real-type transforms before value normalization. Normalization at $z_*=i/4$, known proxy convergence and zero preservation follow only after the hypotheses are established. No CMP-R $\lambda^r$ rate is added to this branch.

[Latest update: CORE-S](updates/2026-10-07-core-s.md) · [Joint-transfer sources and hypotheses](updates/2026-10-05-joint-transfer.md) · [Earlier CMP-R](updates/2026-10-01-cmp-es.md) · [Roadmap](roadmap.md)

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

**COFINAL COMPATIBILITY: NOT ESTABLISHED.**

**COFINAL INCOMPATIBILITY: NOT ESTABLISHED.**

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
