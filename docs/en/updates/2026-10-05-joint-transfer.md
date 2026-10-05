# A conditional transfer from ES and strong L² convergence

**STATUS: RIEMANN HYPOTHESIS OPEN.**

Research records: 2026-10-01–02. Import, primary-source review and public update: **2026-10-05**.

## What changed

A conditional connection has been checked: **if** eventual simplicity and evenness of the finite Weil ground (ES) and strong L² convergence to the theta kernel hold **on the same sequence**, an existing real-zero convergence theorem yields complex comparison (CMP) without prescribing a convergence rate.

Neither ES nor the required strong L² convergence has been proved. CMP and RH remain open. This is not a general assertion that L² convergence implies complex convergence.

## Why return to this direction?

Before comparing two finished objects, the research asked whether they came from the same generating rules. The imported records examine generating formulas, prime repetitions, mean drift, dilation and positive inner products.

One distinction emerged: negative signs and missing mixed terms can arise from taking a logarithm or derivative—the way an object is read—without determining its underlying structure. Symmetry and the existence of a natural positive space also did not supply a positive metric that faithfully retains the actual zeta zeros. These are scoped findings, not impossibility results for every alternative approach.

The main route therefore returned to direct CMP plus ES. The latest question was whether the known real-zero theorem could also help transfer the comparison. This review checks that implication and its hypotheses; it does not start a third route.

## Current boundary

- **CMP: OPEN / ES: OPEN.** The necessary hypotheses on a common cofinal sequence remain unproved.
- Newly discharged asymptotic obligations for the actual moving Weil family: **0**.
- The earlier CMP-R remains a rate-based sufficient condition that does not assume ES. The new joint branch has different hypotheses.
- Four finite diagnostics are neither asymptotic proofs nor interval certificates. The earlier single-endpoint simple-even certificate is not promoted to eventual ES.

**EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED.**

## Next action

The remaining questions are whether the actual ground is eventually simple and even, and whether its direction captures the theta kernel strongly in L², on one sequence. This update stops at import and review; no further proof search or numerical investigation has been started automatically.

## Technical details

### Hypotheses of the conditional transfer

Let $a_j=\log\lambda_j\to\infty$, and let $v_j$ be a real unit ground state of the exact finite Weil matrix, extended by zero outside its interval. ES means that the minimum in the full finite space is simple and its state is even. A minimum within a restricted trial space does not suffice.

Assume eventual ES and, for real scalars $c_j$, strong convergence on that same sequence:

$$
\begin{gathered}
\|c_jv_j-k\|_{L^2(\mathbb R)}\longrightarrow0,\\
\widehat k(z)=\Xi(z)/4\not\equiv0.
\end{gathered}
$$

CCM's finite theorem gives real zeros for $\widehat v_j$. Together with real type and exponential type, this places the transforms in the Laguerre–Pólya (LP) class. Plancherel supplies strong L² convergence on the real axis, which can then be passed to the Clunie–Kuijlaars convergence theorem.

For this application, approximate each LP function by a real-rooted polynomial on an expanding disk. On a real interval where the limit is nonzero, these polynomials converge in measure. This meets the hypotheses of the original Corollary 1.3; the identity theorem identifies the entire limit. Consequently, on every compact subset of the complex plane,

$$
\sup_{z\in K}|c_j\widehat v_j(z)-\Xi(z)/4|\longrightarrow0
\qquad(K\Subset\mathbb C).
$$

This is a conclusion **under the stated hypotheses**. Normalize by the nonzero value at $z_*=i/4$ only after this step. The known strip convergence of the proxy then gives CMP. A transform divided prematurely by a nonreal scalar, or a determinant carrying an exponential phase, is not simply treated as a real LP function.

### A joint sufficient condition using the proxy

Write $\ell_\lambda$ for the raw prolate proxy, $R_a$ for support restriction, $P_N$ for the finite Fourier projection, and $p_{\lambda,N}=P_N\ell_\lambda$. The proxy is already zero outside $[-a,a]$.

$$
\begin{gathered}
D_{\lambda,N}=\|(I-P_v)p_{\lambda,N}\|_2,\\
P_v f=\langle v,f\rangle v.
\end{gathered}
$$

The existing seed and projection bounds give $\ell_\lambda-R_ak\to0$ and, when $a/(N+1)\to0$, $p_{\lambda,N}\to k$. The raw proxy is not assumed exactly even: its odd component is bounded by the existing error. On one cofinal sequence, the resulting sufficient condition is the following, with the first two inequalities holding eventually:

$$
\begin{gathered}
e_->e_+,\quad\Delta_+>0,\\
D_{\lambda,N}\to0,\quad \frac{\log\lambda}{N+1}\to0.
\end{gathered}
$$

The first two conditions remain open for the actual family. The last controls proxy projection; it does not establish ES or capture. Choosing $N=\lceil(\log\lambda)^2\rceil$ illustrates that resolution condition only. An energy-excess-to-gap upper bound is neither necessary for nor equivalent to $D\to0$.

### Relationship to the earlier record

**CASE D — CMP OPEN + ES OPEN.** The import audit's **12 of 19 items** still refers to generic or fixed-scope proofs that can be delegated to existing theorems. It does not mean that 12 RH obstacles were solved.

The earlier CMP-R asks for $\lambda^rD_{\lambda,N}\to0$ for every $0<r<1/2$, with the corresponding projection resolution. That condition is retained; the new ES-dependent sufficient branch is added alongside it. The [2026-10-01 update](2026-10-01-cmp-es.md) remains a record of what was known then.

## Evidence and sources

The original Clunie–Kuijlaars theorem and its relevant proof were obtained and checked in this review; they had not been retrieved when the handoff was written. A separate reverse-order adversarial pass was also performed by the same AI reviewer. This is not external peer review or formal verification. The four numerical cases received stored-value consistency checks only; their eigenproblems were not rerun.

- Clunie–Kuijlaars, *Approximation by Polynomials with Restricted Zeros* (1994), Corollary 1.3, p.110; proof pp.113–114. [Original paper](https://pure.uva.nl/ws/files/2851818/178_2351y.pdf) · [DOI](https://doi.org/10.1006/jath.1994.1116)
- Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv v1, Theorem 5.10(iii), Lemmas 7.2–7.3. The boundary normalization and this log's $\widehat k=\Xi/4$ convention were checked. [Primary source](https://arxiv.org/html/2511.22755v1)
- [Current public state record](../../../data/current-state-2026-10-05.json) · [Publication review record](../../../audit/handoff_2026_10_05_review.md)

The handoff originals and third-party PDFs are not republished as a bundle. This article is an edited summary of the adoption decision.

**STATUS: RIEMANN HYPOTHESIS OPEN.**
