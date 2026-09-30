# Reproducibility and limits of the checks

**STATUS: RIEMANN HYPOTHESIS OPEN**

The public archive preserves selected code, output and written arguments. Publication preparation did not rerun the mathematical experiments, interval certificates or Lean builds. A historical `PASS` must be read with its input, version, precision and domain. Internal AI-agent agreement is not external peer review.

## Start without executing research code

From the public repository root:

```sh
python3 artifacts/replay.py --list
python3 artifacts/replay.py \
  --script experiments/scripts/window_half_certificate.py \
  --prepare-only
```

The helper verifies exported payload hashes and reconstructs the selected original relative layout in an isolated workspace. It does not download dependencies or third-party sources, and preparation alone executes no research script. The [artifact guide](../artifacts/README.md) lists blocked or incomplete reproductions. The [source manifest](../data/source-manifest.json) distinguishes original and exported hashes; old source hashes are not expected to equal files with new publication headers.

Use a separate environment for the dependencies you choose to install. The saved basic requirements pin NumPy 2.3.5; the interval-certificate requirements pin python-flint 0.9.0 and mpmath 1.4.1. Other later diagnostics may require SciPy or additional packages. These historical pins are recorded context, not a claim that every current platform has been tested.

Historical requirements: [basic](../archive/reports/experiments/requirements.txt) and [interval certificates](../archive/reports/experiments/requirements-cert.txt).

Once the required environment is available, omit `--prepare-only` to run the selected script with that Python. For example, the following requests only the script's help:

```sh
python3 artifacts/replay.py \
  --script experiments/scripts/window_half_certificate.py \
  -- --help
```

Arguments following `--` are passed to the script. New outputs stay in the isolated workspace. The helper does not compare them with old results or declare a certificate valid. Review the script and linked mathematical obligations before a full run. Do not use `python -O` for certificate scripts: their assertions check required inequalities.

## Four kinds of evidence

| Kind | What it can establish | What it does not establish |
|---|---|---|
| Exact rational or symbolic calculation | A finite identity or inequality, subject to the stated derivation | An unproved identification with an infinite arithmetic operator |
| Floating-point or high-precision diagnostic | A numerical observation and possible falsification lead | A certified sign merely because more digits were used |
| Ball/interval certificate plus analytic bounds | The specified finite inequalities and, where supplied, the infinite tail and coupling estimate | Uniform positivity for every support or every parameter |
| Lean proof | The named declarations under their explicit hypotheses | Unformalized analytic hypotheses, the Weil criterion or RH |

## Selected historical computations

- [Exact finite models](../artifacts/experiments/scripts/falsify_models.py): Fraction calculations are exact; Decimal quadrature in the same script is explicitly non-certified. The countermodels refute proposed implications, not RH.
- [Small finite Weil matrix](../artifacts/experiments/scripts/groskin_independent_certificate.py): Independent assembly and certification concern c = 13, N = 4, a 9-dimensional matrix. The large original 401-dimensional calculation was not independently reproduced here.
- [Whole half-window certificate](../artifacts/experiments/scripts/window_half_certificate.py): The interval-certified even and odd finite heads are combined with written infinite-tail and coupling bounds. The resulting domain is support [−1/2,1/2], not all supports.
- [Half-window crosscheck](../artifacts/experiments/scripts/window_half_crosscheck.py): A separately implemented integral comparison checks the stated finite components; read the audit for its exact overlap with the main certificate.
- [Joint-symbol high-frequency certificates](../artifacts/experiments/scripts/joint_symbol_certificate.py): Five fixed windows and their high-frequency floors. This does not certify their finite heads or the full Weil form on all five windows.
- [Finite scalar repair in a claim audit](../artifacts/experiments/scripts/desogus_safe_cut_repair.py): Checks the specified finite k range by Arb. It does not repair the unresolved identification of the actual operator or its analytic tail.

The main half-window proof obligations and independent scope are in [the certificate audit](../archive/audits/proofs/audits/window-half-certificate.md) and [the independent audit](../archive/audits/proofs/audits/window-half-independent.md). A saved unverified, interrupted or NaN result is not a successful certificate. The larger-window interrupted script remains historical evidence of an attempted computation.

Later common-parent, rate-history and hierarchy experiments are finite diagnostics with recorded precisions and parameter paths. They do not prove all-cutoff convergence, a full-matrix gap or a theorem uniform in derivative order. Their written analytic results are separate from the plotted or tabulated evidence.

Two historical scripts require excluded third-party material: the original-assembly Groskin comparison and the Desogus TeX extraction check. The replay helper refuses to run those as standalone reproducers. Old repository-preservation validators also require private baselines and are not validators of this public tree. Nothing is silently downloaded to fill these gaps.

## Formal verification

[The Lean scope note](../artifacts/formal/lean/README.md) records Lean 4.19.0 and a pinned Mathlib revision. [RhAudit.lean](../artifacts/formal/lean/RhAudit.lean) contains eight declarations: positivity under explicit limits or continuity, elementary block inequalities, a finite counterexample coefficient, and a scalar Schur equivalence. [The saved axiom log](../artifacts/formal/lean/verification/axioms.txt) lists the ordinary Lean logical axioms and no `sorryAx`.

[ReturnLemma.lean](../artifacts/research/one_prime/formal/ReturnLemma.lean) contains four scalar growth declarations. It does not formalize the arithmetic quotient, its operator norm or the zeta-zero theorem. The fixed-window analytic tail, special functions, cyclicity proof and full RH have not been formalized.

Toolchains and Mathlib are not vendored. To rebuild, first reconstruct the layout, then use the saved toolchain and manifest in its `formal/lean` directory. The historical instructions include `lake build` and `lake env lean RhAudit.lean`; fetching the pinned dependencies is a separate network operation. Preserve the manifest rather than treating a freshly updated dependency tree as the historical build.

## The latest cyclicity update

The result is an ordinary analytic proof of density of the even derivatives in even L². Its internal audit checks the Fourier normalization, exponential moments, moment criterion and direct uniqueness proof. It has no finite-head numerical certificate and no claimed conditioning estimate. Density in L² is not a statement about the Weil form topology or full ground capture.

A new rerun should record the script and dependency versions, exported payload hash, parameters, precision, output and which analytic assumptions were checked. That would be new evidence with a new scope. It should not overwrite a historical claim or turn a scoped check into a global RH assertion.
