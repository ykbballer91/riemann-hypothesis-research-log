# 18. Cyclicity of the even derivative family — dated update

**STATUS: RIEMANN HYPOTHESIS OPEN**

Update recorded 2026-09-30, after the 17-track publication inventory. This update completes **Priority 1 only**. “Full ground capture” is the source directory name, not a theorem proved in this update.

## Starting idea

The fixed finite-dimensional selection theorem leaves a basic question: does the union of the tested derivative families even reach every even square-integrable function? Density is a necessary approximation resource, but supplies no uniform rate for a growing family.

## What was tested

Use the actual normalization

$$
\widehat{k}(x)=\int_{\mathbb R}k(t)e^{-ixt}\,dt=\Xi(x)/4,
\qquad \Xi(x)=\xi(1/2+ix).
$$

The proof studies the positive measure $d\mu(x)=|\Xi(x)|^2dx$. Standard Gamma decay and an unconditional zeta bound imply a finite exponential moment for every exponent below $\pi/2$. Since Xi is a nonzero entire function, its real zeros have measure zero; RH and simplicity of those zeros are unnecessary.

## What survived

The unconditional conclusion is

$$
\boxed{\overline{\mathrm{span}\,_{\mathbb C}\lbrace k^{(2j)}:j\ge0\rbrace}^{\,L^2(\mathbb R)}
=L^2_{\mathrm{even}}(\mathbb R).}
$$

The real-span version also holds in real even L². Carleman's condition gives polynomial density in L²(μ); even symmetrization, the onto isometry $h\mapsto\Xi h$, and Plancherel give the result. A second proof uses analytic Fourier transforms and uniqueness. Neither proof divides by a uniformly bounded inverse of Xi.

For the change of variable $y=x^2$, the Stieltjes moment condition uses $m_{2n}^{-1/(2n)}$. It must not be replaced by the different Hamburger condition involving $m_{4n}$. A supplementary moment asymptotic is not needed for the density proof.

## What remains unproved

L² density does not establish density in the Weil form domain, a form core, a uniform approximation bound, stable coefficients, or a gap outside a fixed derivative family. It does not justify exchanging the limits in support, Fourier resolution and derivative order. The known radical identities cannot be extended using unproved continuity or closability in L².

**Full ground capture, estimates uniform in growing m, the ES ground-state hypotheses, G*, and RH remain open.** Priority 2 and later tasks were not undertaken in this update.

## Why the work stopped here

The requested cyclicity question has a positive, unconditional answer. A new argument would be needed to convert qualitative density into the quantitative and form-topological control required for ground selection. This page records that boundary rather than treating density as completion of the larger program.

## Current scope

Cyclicity: **proved in the written argument, with scoped internal AI-agent audit**. The proof applies established moment and Fourier principles; no novelty claim is made. It has not been externally peer reviewed or formalized in Lean.

## Canonical records

- [Main proof](../../archive/reports/research/full_ground_capture/cyclicity.md)
- [Moment sources and independent direct proof](../../archive/reports/research/full_ground_capture/notes/moment_problem_sources.md)
- [Supplementary moment asymptotic](../../archive/reports/research/full_ground_capture/notes/moment_asymptotic.md)
- [Scoped internal audit](../../archive/audits/proofs/audits/full_ground_cyclicity_adversarial.md)
- [Dated state record](../../data/source-records/research/full_ground_capture/state.json)

[Research timeline](../timeline.md) · [Reproducibility](../reproducibility.md) · [References](../references.md)
