# Research timeline

**STATUS: RIEMANN HYPOTHESIS OPEN**

This is the edited research sequence maintained by **@ykbballer91**, with AI-assisted derivations and internal audits. It contains the 17 tracks identified by the read-only publication inventory and one separately dated cyclicity update. A track is a bounded investigation, not a claim of a new theorem of independent research significance.

Dates below come from the named research or completion reports. They are not estimates of when each calculation first occurred. The initial 23 cycles are grouped because individual cycle timestamps were not recorded. Continuous scale flow ran alongside the polarization work; this list does not imply strictly serial execution. One-prime return spans September 29–30.

The Phase 1 Git inventory records 29 commits. Those commits are an archival chronology, not a substitute for report dates: some research was added as a later working-tree snapshot. Historical states are preserved at their own scope; the old main state and release README do not summarize every later track. See the [source map](source-map.md).

## 01. 2026-09-29 — [Initial Weil program: finite positivity and its limits](tracks/01-initial-weil-program.md)

**Question and test.** The opening program asked whether finite certificates, kernel identities and continuity could establish positivity of the Weil quadratic form on every compact support. Weil positivity is a criterion for RH; proving an equivalent statement still requires an independent argument. Twenty-three recorded cycles checked finite forms, fixed support bounds, operator dictionaries, arithmetic identities and selected external proof claims. Tests repeatedly separated a finite matrix from its infinite tail and from the coupling between the two.

**Retained.** A computer-assisted bound was recorded for the full complex form domain on support [−1/2, 1/2]: Q_W(f) ≥ 9 × 10⁻⁸ ‖f‖², with an interval-certified head and analytic tail and coupling bounds.

**Boundary.** No positivity argument for all supports survived. Checking coordinate blocks does not control cross terms. A positive kernel or a symmetry of the zero set does not force every zero onto the symmetry line. A gap in an audited proof claim is recorded at the disputed step, rather than treated as a disproof of every result in that paper.

**Transition.** The 23-cycle handoff led to a separately authorized study of arithmetic generators and their boundary conditions.

**Status.** Completed exploratory program; all-support Weil positivity and RH remain open.

## 02. 2026-09-29 — [Arithmetic generators and boundary conditions](tracks/02-generator-boundary.md)

**Question and test.** Could a generator reconstructed from primes and Gamma factors carry boundary conditions that force the zero spectrum onto the critical line? The comparison covered de Bruijn–Newman evolution, an inverse spectral m-function and modular-surface scattering. In each case the question was whether the actual arithmetic object, including multiplicities, was preserved.

**Retained.** The scattering coefficient gives a precise map from nontrivial zeta zeros to scattering poles, with a no-cancellation check.

**Boundary.** Self-adjointness of the surface Laplacian does not make its scattering resonances real. Requiring the actual inverse spectral function to be Herglotz returns to a condition equivalent to RH. The arithmetic definition of the heat family does not establish its needed threshold at time zero.

**Transition.** The next comparison asked what finite-field Frobenius has that these number-field constructions lack: a positive pairing on the same space that carries the zeros.

**Status.** Exact correspondences retained; no independent confinement mechanism obtained.

## 03. 2026-09-29 — [The missing Frobenius mechanism](tracks/03-missing-frobenius.md)

**Question and test.** Finite-field proofs supply a model for asking where arithmetic origin, trace, duality and purity enter. The aim was to identify the missing theorem over the integers, not to transfer a finite-field analogy by name. The audit compared the curve/Jacobian polarization argument, broader cohomological purity, Deninger proposals and the existing adelic quotient that represents zeta zeros.

**Retained.** For the finite-field abelian-variety argument, positivity of the Rosati pairing and the relation π†π = q act on the same representation.

**Boundary.** Formal duality and positive integer point counts alone do not establish purity. A natural positive ambient Hilbert norm collapses the intended quotient: its null subspace is dense in that completion. No positive pairing with the required faithful arithmetic descent was supplied.

**Transition.** The work split into an arithmetic-polarization audit and a parallel examination of continuous scaling and prime return maps.

**Status.** Missing positivity/purity isolated. The historical main state stops here; later tracks have separate states.

## 04. 2026-09-29 — [Arithmetic polarization and intersection pairings](tracks/04-arithmetic-polarization.md)

**Question and test.** Could an existing arithmetic intersection or height theorem provide the positive pairing missing from the zero-bearing quotient? The track compared Arakelov heights, explicit-formula “intersection” language, adelic Fourier involutions and product formulas, checking the actual spaces and subtraction of pole terms.

**Retained.** Known positivity theorems retain their stated geometric domains. The height theory of an arithmetic surface is different from a degree-zero quotient on Spec Z.

**Boundary.** No exact map identified the established height space with the full zero representation. A natural Fourier-star proposal has negative directions even for actual pole-free tests; this defeats that proposed pairing, not RH or the Weil criterion. Calling an explicit-formula term an intersection does not supply an intersection geometry or a Hodge-index theorem.

**Transition.** The separate scaling track examined the real arithmetic prime orbits directly, then weakened the desired conclusion to a bound for a single prime return.

**Status.** Existing geometric theorems retained; the required arithmetic polarization was not constructed.

## 05. 2026-09-29 — [Continuous scale flow and prime return maps](tracks/05-continuous-scale-flow.md)

**Question and test.** Prime periodic orbits have lengths log p. The question was whether their actual arithmetic return maps could explain the real part 1/2 of every zero. The audit separated a mapping torus, its fiber monodromy, local p-adic transverse action and a genuine smooth Poincaré return map. It also separated local orbit modes from the global zero representation.

**Retained.** The known orbit C_p = ℝ₊×/p^ℤ has length log p. In the chosen lift, the deck convention and the positive-time inverse return convention must be distinguished.

**Boundary.** Local Haar unitarity does not recover a discrete zeta divisor: the local model has extra modes. A faithful common Hilbert metric on the global arithmetic quotient remains missing. Symplecticity, indefinite pairings and time reversal do not replace it.

**Transition.** The next track asked for the weaker requirement of two-sided subexponential growth of the return operator at p = 2.

**Status.** Known arithmetic geometry clarified; no new purity theorem or spectral realization claimed.

## 06. 2026-09-30 — [One-prime return and a faithful Banach completion](tracks/06-one-prime-return.md)

**Question and test.** If one arithmetic return operator grows subexponentially in both directions while retaining every zero evaluation, can it force every zero character to have zero real exponent? The work fixed the actual test quotient and constructed a normed completion from a specified quotient seminorm. It checked continuity of zero evaluations and finite jets, rather than assuming a Hilbert space or an exact spectrum.

**Retained.** A two-sided subexponential return bound forces the real exponent of every retained character to vanish; the scalar implication was also formalized.

**Boundary.** The available arithmetic bounds are exponential. No RH-independent subexponential estimate was proved. Banach completion does not establish Hilbert structure, absence of extra spectrum, a determinant formula or full topological equivalence to the original quotient.

**Transition.** The next experiment constructed representatives explicitly using Möbius inversion and a cutoff, so that any growth improvement would have a concrete arithmetic obligation.

**Status.** Faithful evaluation retention and an abstract sufficient lemma proved; its arithmetic growth hypothesis remains open.

## 07. 2026-09-30 — [Dyadic arithmetic reduction](tracks/07-dyadic-arithmetic-reduction.md)

**Question and test.** Can the representative of a class be pushed into one side of the logarithmic line with a quantitatively small norm after repeated dilation by 2? The construction used full integer Möbius inversion of the arithmetic sum, a smooth cutoff and a moment correction. Sampling the flow at powers of 2 does not restrict the arithmetic input to powers of 2.

**Retained.** For arbitrary admissible input, an explicit representative cancels the right tail. An unconditional upper bound has rate 2ⁿᐟ²(1 + n).

**Boundary.** The construction supplies no independent endpoint cancellation. The unconditional exponent 1/2 was not proved optimal. A compactly supported folding argument is obstructed by the actual arithmetic subspace, rather than repaired by the cutoff.

**Transition.** The inquiry moved to the signed combinatorics of Möbius cancellation: first a prime complex, then prime phases and a weighted halfspace.

**Status.** Explicit reduction and unconditional rate retained; the desired endpoint is an equivalent reformulation, not progress toward proving RH.

## 08. 2026-09-30 — [Prime complexes and parity pairing](tracks/08-prime-complex-parity.md)

**Question and test.** The Möbius sum is a signed Euler characteristic. Could a canonical matching on a prime complex leave only a square-root-sized obstruction? The complex Δ_X consists of finite prime subsets whose product is at most X. The convention is M(X) = − reduced χ(Δ_X). Toggling the smallest prime, 2, yields an explicit matching and filtered chain description.

**Retained.** The unmatched cells correspond to odd squarefree integers in (X/2, X]; their total number, and hence the relevant total Betti count, has linear asymptotic 2X/π².

**Boundary.** The unsigned topological remainder is linear, so this matching does not give the desired signed cancellation. A prime-vertex pairwise-product graph is not the complex: at X = 15 all three edges on {2,3,5} exist but the triple face does not. Its flag completion would change the topology. This is not a no-go theorem for every possible nonlocal pairing.

**Transition.** The next track tested whether prime-logarithm phase statistics supplied the missing signs.

**Status.** Exact combinatorial identities retained; no square-root estimate for M(X) obtained.

## 09. 2026-09-30 — [Prime-logarithm phases: the arithmetic comma track](tracks/09-arithmetic-comma.md)

**Question and test.** Prime logarithms generate a torus flow. Could nonresonance, long-time phase statistics or pretentious distance control the distinguished phase at which the Möbius sum is read? Exact finite Fourier identities, Mellin/Perron reconstruction, time-averaged sinc factors, high moments and near returns were checked. The cost of removing smoothing was kept explicit.

**Retained.** The phase-to-arithmetic reconstruction is exact within its stated cutoff and convergence domains.

**Boundary.** Equidistribution and root-mean-square time control do not give the required pointwise square-root estimate. Hardy-space boundary evaluation can be unbounded. A normalization by the number of sign configurations is not cancellation of the actual signed sum.

**Transition.** The next track retained the actual prime-product constraint as a Boolean weighted halfspace rather than replacing it by a phase distribution.

**Status.** Exact bridges and their losses retained; phase statistics alone did not provide the missing estimate.

## 10. 2026-09-30 — [Weighted prime halfspaces](tracks/10-weighted-prime-half-space.md)

**Question and test.** Write squarefree integers as prime subsets subject to a logarithmic weight bound. The question was whether this structure forces cancellation between even and odd subset sizes. The track checked finite-difference bounds, exact large-prime decompositions, Gibbs tilts and the Selberg–Delange family S_z(X) = Σ_{n≤X} μ²(n)z^{ω(n)}. Here μ is the Möbius function and ω counts distinct prime factors.

**Retained.** The finite combinatorial identities preserve parent multiplicities and the actual signs. Generic central-binomial bounds can be sharp even with rationally independent weights.

**Boundary.** Vanishing local coefficients is not a finite-X pairing and does not bound the remaining global term. Unsigned influence or anti-concentration estimates do not evaluate the needed signed covariance. Tilt reconstruction is exact only when its normalization and covariance terms are retained.

**Transition.** The next track isolated the global remainder and asked what a smoothed explicit formula actually determines.

**Status.** Local expansions and exact finite identities retained; no fixed-power cancellation estimate obtained.

## 11. 2026-09-30 — [The global remainder beyond local asymptotic orders](tracks/11-global-remainder.md)

**Question and test.** If every coefficient in a local asymptotic expansion vanishes, where does the Möbius sum remain? The work used a fixed Gaussian readout to separate local expansion data from global singularities. For R(u) = Σ μ(n)e^{−(u−log n)²}, absolute convergence gives the transform √π e^{s²/4}/ζ(s) for Re s > 1. Contour shifts were checked with explicit height grouping and multiplicities.

**Retained.** Finite left shifts yield a controlled grouped residue description. This is not an arbitrarily reordered or absolutely convergent sum over individual zeros.

**Boundary.** An infinite shift to the left and the proposed unrestricted trivial-zero series fail their convergence requirements. A full analytic germ does determine its connected meromorphic continuation; it cannot be changed while keeping every Taylor coefficient. Vanishing Selberg–Delange coefficients are not vanishing Taylor coefficients of 1/ζ.

**Transition.** The program paused new constructions for an inventory of actual arithmetic estimates and the precise pointwise gap.

**Status.** Exact transform and finite-shift statements retained; the target growth estimate remains equivalent to RH.

## 12. 2026-09-30 — [Strategy reset: arithmetic estimates and closure](tracks/12-mobius-closure-audit.md)

**Question and test.** This was an inventory rather than a new proof route. It asked whether existing bilinear, short-interval, correlation or causal-closure estimates already supplied the missing pointwise bound. The audit distinguished pointwise estimates, almost-all statements, logarithmic averages and shift averages. It checked the fixed Gaussian window, sliding derivative energies and the arithmetic delay equations.

**Retained.** Absolute-convergence identities and the unique Möbius inverse in the specified past-decaying class were fixed.

**Boundary.** Known average correlation conclusions do not supply square-root-scale control of every readout. Causal uniqueness does not imply forward stability. Shrinking the Gaussian width with the observation point can make an all-positive sum bounded, so it changes the question instead of proving cancellation.

**Transition.** No next route followed automatically from this inventory. A later, separately requested track tested an arithmetic restoring-force interpretation.

**Status.** Three proposed mechanisms were not justified. The audit did not claim that all mathematical strategies were exhausted.

## 13. 2026-09-30 — [Arithmetic restoring force](tracks/13-restoring-force.md)

**Question and test.** Could the actual theta kernel impose a force that confines zeros, without simply assuming a global sign condition equivalent to RH? The track derived off-axis cosine/hyperbolic-sine equations, examined logarithmic derivatives and fixed the de Bruijn–Newman heat sign and time convention. It separated real-axis repulsion from confinement of complex branches.

**Retained.** Known forward strip contraction and the simple-zero evolution law remain valid in their stated domains. Multiple collisions require separate treatment.

**Boundary.** The required global restoring sign returns to an RH-equivalent criterion. Positivity and evenness of the theta kernel do not supply it. A proposed total-positivity property of the actual kernel fails; this is distinct from the Fourier real-zero question.

**Transition.** The next comparison asked whether existing local real-zero theorems could be connected to the actual global approximation family.

**Status.** Correct evolution laws retained; the time-zero confinement regime remains unproved.

## 14. 2026-09-30 — [Local-to-global zero confinement](tracks/14-local-to-global.md)

**Question and test.** Several local or constrained transforms have real zeros. The task was to identify exactly what must converge to transfer that conclusion to Xi. The audit compared Hermite–Mellin results, local-field statements, completed transforms with finite correction factors, semilocal Sonin stability and the finite Weil-ground construction.

**Retained.** The hypotheses of the real-zero theorems include their specific vector, positivity, support or orthogonality conditions. A completed transform containing ζ as a factor cannot remove off-line zeta zeros by a holomorphic correction.

**Boundary.** No theorem identifies the normalized true ground state with that proxy. The missing comparison G* is convergence of their transforms on compact subsets of |Im z| < 1/2, together with the required ground-state hypotheses. The combined criterion is sufficient; an RH converse for G* was not established.

**Transition.** The common-parent track asked whether an actual energy identity, residual estimate or spectral gap could provide this comparison.

**Status.** Local theorems and proxy convergence retained; the global bridge remains open.

## 15. 2026-09-30 — [A common variational parent?](tracks/15-common-parent.md)

**Question and test.** The actual Weil ground state and a prolate proxy both appear near the arithmetic kernel. Could one variational principle force them to agree? The work fixed the pullback Q(Eh), its induced metric E*E, and the difference between the prolate h₀/h₄ zero-integral mixture and a usual concentration ground state. It tested energy excess, residuals and gaps.

**Retained.** For a simple ground state with positive gap Δ, Rayleigh excess gives an angle bound controlled by (R_B − e₀)/Δ. Transferring it to Fourier transforms on expanding support also costs a weighted norm factor.

**Boundary.** No common-parent identity or sufficient excess-to-gap decay was proved. A near-zero energy cannot select a unique vector from a large radical. A large upper-bound ratio is not a lower bound on actual distance. The finite high-precision diagnostics are not interval certificates or a theorem about all cutoffs.

**Transition.** The next track examined how finite cutoffs split that degeneracy and whether rates or path history select a direction.

**Status.** An exact variational dictionary and sufficient estimates retained; full ground comparison remains open.

## 16. 2026-09-30 — [Rates, history and finite-cutoff splitting](tracks/16-rate-history.md)

**Question and test.** Could the way support and Fourier cutoffs increase select the arithmetic kernel from the global radical? The track separated support restriction R_a from periodic Fourier projection P_N, examined prime-power threshold events, and compared diagnostic paths N ≍ a² and N ≍ a³.

**Retained.** For the two-dimensional family span{k,k″}, support-only minimization selects k after normalization. An explicit boundary cancellation improves its rate.

**Boundary.** Energy upper bounds are not leading asymptotics or a ground-selection theorem. Beyond two derivatives, the leading nullspace has larger dimension. At this stage neither path-dependent nor path-independent limiting selection had been proved.

**Transition.** The next track resolved a hierarchy for each fixed finite derivative family, using higher-order Schur terms and a stronger Fourier-resolution scale.

**Status.** Rate and finite-endpoint facts retained. Later refinements apply to restricted families and do not retrospectively prove a full-ground statement here.

## 17. 2026-09-30 — [Hierarchical selection in fixed derivative families](tracks/17-hierarchical-selection.md)

**Question and test.** After the leading boundary energy becomes degenerate, do successive terms select k within F_m = span{k,k″,…,k⁽²ᵐ⁾}? The order of operations is the actual projection P_N R_a. The work derived fixed-m support asymptotics, controlled their Gram matrices, compared Fourier resolution with the boundary scale, and separately audited prime rank-one perturbations and Sonin filtrations.

**Retained.** For every fixed finite m, the support-restricted smallest eigenvalue is eventually simple and its normalized minimizer tends to k/‖k‖. The recorded leading term is a(m!)²Y^(7/2−2m)e^(−2Y)/(√π‖k‖²), with Y = πe^(2a).

**Boundary.** Constants and errors are not uniform in growing m. No estimate controls the complementary directions of the full finite matrix. Evenness/simplicity of the relevant full ground states and G* remain missing. Restricted selection is not full ground capture.

**Transition.** A separately dated update asked only whether the union of these derivative families is dense in even L². It did not start the later full-ground steps.

**Status.** Fixed finite-m hierarchy established within its stated domain; full ground, growing m and RH remain open.

## 18. 2026-09-30 — [Cyclicity of the even derivative family](tracks/18-even-l2-cyclicity.md)

**Question and test.** Is the union of all even derivative families dense in the actual even L² space? Carleman density and an independent analytic-Fourier uniqueness argument.

**Retained.** Unconditional closure span{k^(2j)} = L²_even.

**Boundary.** No form-core, uniform growing-m or full-ground conclusion follows.

**Transition.** Priority 1 completed; no later priority was started.

**Status.** Cyclicity proved; full ground, G* and RH open.

Internal audits are not external peer review. A proved auxiliary statement, a conditional criterion, an interval computation and a floating-point diagnostic are different kinds of evidence. None of the entries establishes RH.

## 19. 2026-09-30 — [Finite even Fourier heads](tracks/19-finite-even-head-spanning.md)

**Question and test.** After cyclicity, the next authorized task fixed the actual even Fourier head, separated ideal full-line samples from support-restricted columns, and compared tail errors with Vandermonde inverse bounds.

**Retained.** Every fixed head has exact finite-prefix spanning. For fixed Fourier dimension, the minimal prefix works eventually and has only finitely many possible exceptional window widths. Two finite parameter intervals have analytic-plus-Arb rank certificates.

**Boundary.** The exception set is not explicitly classified. Physical singular values can deteriorate despite exact rank. No uniform cutoff, coefficient, form-error or moving-ground estimate follows. Floating physical-Gram diagnostics are not interval certificates.

**Transition and status.** Priority 2 stopped here. Growing-order selection, full-ground capture, parity/ES, G* and RH remain open. No later priority was started.


## 20. 2026-10-01 公開更新 — [既存定理の委譲と CMP / ES](updates/2026-10-01-cmp-es.md)

**更新。** 2026-09-30の完了済み研究を反映。既存定理監査の19項目中12項目は一般理論・固定範囲の証明を委譲できる。actual moving-Weil の未解決漸近評価が新たに解決した件数は0。

**残った義務。** 現在採用する直接ルートはCMPとESの二種類に集中する。CMPの複素一様比較は具体的な速度の十分条件へ、ESは偶・奇の最低値差と偶側内部の固有値差へ整理された。双方とも未証明であり、同じ共終列上での成立が必要。一点の単純・偶最低状態の有限認証を、最終的なESへ一般化しない。

**なぜ変えたか。** 既存数学で閉じている一般部分を外し、実際のゼータに固有の未証明部分へ対象を絞るため。

**NEXT ACTION。** 必要な速度での最低状態・プロレート近似の接近と、最終的な単純・偶性を独立に検証する。第三ルートへ自動的に広げない。

**状態。** CASE D — CMP OPEN + ES OPEN. EVEN FULL-GROUND CAPTURE: NOT ESTABLISHED. STATUS: RIEMANN HYPOTHESIS OPEN.
