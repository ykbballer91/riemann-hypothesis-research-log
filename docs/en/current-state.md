# Current state — what is established and what remains open

**STATUS: RIEMANN HYPOTHESIS OPEN**

Latest public update: **2026-10-05**. Research records dated 2026-10-01–02 have been imported, and the conditional transfer was checked against primary sources and its hypotheses. This is the canonical editorial overview. A [new state record](../../data/current-state-2026-10-05.json) has been added; the [earlier state record](../../data/research-state.json) is preserved.

## The selected direct route

**CMP**, the complex comparison between the actual finite Weil ground and the prolate proxy, and **ES**, eventual simplicity and evenness of that ground, both remain open. Their hypotheses must hold on the same cofinal sequence.

The review accepts a conditional branch: **if ES and strong L² capture of the theta kernel hold on that sequence**, an existing real-zero convergence theorem yields CMP without prescribing a convergence rate. ES is an explicit hypothesis of this branch. The earlier, ES-independent CMP-R remains a valid rate-based sufficient condition.

## Current boundary and next action

General L² convergence alone does not yield complex convergence. This branch uses the additional real-zero, real-type and exponential-type structure obtained under ES. Neither eventual ES nor actual strong L² capture has been established.

The remaining questions concern simple-even ground states and strong L² capture on one sequence. This task stops at import, review and publication; no further proof search or numerical investigation has been started automatically.

## Technical details of the latest update

**CASE D — CMP OPEN + ES OPEN.** The earlier **12 of 19 items** refers to delegated generic or fixed-scope proofs, not 12 solved RH obstacles. Newly discharged asymptotic obligations for the actual Weil family: **0**.

- With $p_{\lambda,N}=P_N\ell_\lambda$ and $D_{\lambda,N}=\|(I-P_v)p_{\lambda,N}\|_2$, the joint sufficient condition is eventual ES, $D_{\lambda,N}\to0$ and $\log\lambda/(N+1)\to0$ on one sequence. This package remains unproved.
- ES requires eventual $e_->e_+$ and $\Delta_+>0$. The certificate at $c=\lambda^2=13$, $N=4$ remains a single-endpoint result.
- The raw proxy is not assumed exactly even. Its odd-component bound and ordinary projection error follow from existing estimates. Four diagnostic cases are not promoted to asymptotic proofs.
- The joint transfer applies to real-type transforms before value normalization. Normalization at $z_*=i/4$, the known proxy limit and zero preservation remain conditional on the preceding hypotheses.

[Latest update and adoption review](updates/2026-10-05-joint-transfer.md) · [Earlier CMP-R update](updates/2026-10-01-cmp-es.md) · [Roadmap](roadmap.md)

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

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
