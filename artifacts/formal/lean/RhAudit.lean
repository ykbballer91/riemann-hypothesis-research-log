/- STATUS: RIEMANN HYPOTHESIS OPEN
Sanitized historical Lean source; not rebuilt during this export.
Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
Source: formal/lean/RhAudit.lean
Original SHA-256: 64639579e8ae44afba86ed91bf83278fc102988a12a1631f270f4c133f612775
-/
import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Order.OrderClosed
import Mathlib.Tactic

/-!
Audit kernels only. No declaration in this file states or assumes RH.
The analytic Weil-form estimates and the Weil criterion are NOT formalized here.
-/

open Filter Set
open scoped Topology

namespace RhAudit

/-- Pointwise convergence of nonnegative forms preserves nonnegativity.
No uniform bound over vectors is required for this implication. -/
theorem nonneg_of_pointwise_limit {E : Type*}
    (qN : ℕ → E → ℝ) (q : E → ℝ)
    (hlim : ∀ x, Tendsto (fun n => qN n x) atTop (𝓝 (q x)))
    (hpos : ∀ n x, 0 ≤ qN n x) : ∀ x, 0 ≤ q x := by
  intro x
  exact ge_of_tendsto' (hlim x) (fun n => hpos n x)

/-- A vanishing, pointwise lower error suffices; it is an explicit hypothesis. -/
theorem nonneg_of_vanishing_lower_error {E : Type*}
    (qN err : ℕ → E → ℝ) (q : E → ℝ)
    (hlim : ∀ x, Tendsto (fun n => qN n x) atTop (𝓝 (q x)))
    (herr : ∀ x, Tendsto (fun n => err n x) atTop (𝓝 0))
    (hlower : ∀ n x, -err n x ≤ qN n x) : ∀ x, 0 ≤ q x := by
  intro x
  have hsum : Tendsto (fun n => qN n x + err n x) atTop (𝓝 (q x)) := by
    simpa only [add_zero] using (hlim x).add (herr x)
  apply ge_of_tendsto' hsum
  intro n
  linarith [hlower n x]

/-- Density transfers positivity only with continuity in the chosen topology. -/
theorem nonneg_on_dense {E : Type*} [TopologicalSpace E]
    (q : E → ℝ) (s : Set E) (hq : Continuous q)
    (hs : Dense s) (hpos : ∀ x ∈ s, 0 ≤ q x) : ∀ x, 0 ≤ q x := by
  have hsub : closure s ⊆ {x | 0 ≤ q x} :=
    closure_minimal hpos (isClosed_le continuous_const hq)
  intro x
  exact hsub (hs x)

/-- A two-dimensional obstruction to extending positive coordinate restrictions. -/
def blockForm (x y : ℝ) : ℝ := x^2 + 4*x*y + y^2

theorem coordinate_restrictions_nonneg (x : ℝ) :
    0 ≤ blockForm x 0 ∧ 0 ≤ blockForm 0 x := by
  constructor <;> simpa [blockForm] using sq_nonneg x

theorem larger_block_negative : blockForm 1 (-1) = -2 := by
  norm_num [blockForm]

/-- Arithmetic coefficient in the off-axis quartet toy model.
The Fourier realization of the witness is proved on paper, not in this file. -/
theorem quartet_coefficient :
    (-32 : ℚ) * (1/4)^2 * (1 - (1/4)^2) = -15/8 := by
  norm_num

/-- Scalar lower bound for coupling two blocks. This only formalizes the real
algebra; no infinite-dimensional operator or computed certificate is assumed. -/
theorem two_block_lower_bound (μ δ ε ell x y : ℝ)
    (hε : 0 ≤ ε) (hμ : ell + ε ≤ μ) (hδ : ell + ε ≤ δ) :
    ell * (x^2 + y^2) ≤ μ * x^2 + δ * y^2 - 2 * ε * x * y := by
  have hx : 0 ≤ (μ - ell - ε) * x^2 :=
    mul_nonneg (by linarith) (sq_nonneg x)
  have hy : 0 ≤ (δ - ell - ε) * y^2 :=
    mul_nonneg (by linarith) (sq_nonneg y)
  have hxy : 0 ≤ ε * (x - y)^2 := mul_nonneg hε (sq_nonneg (x - y))
  nlinarith

/-- The real scalar Schur equivalence with a strictly positive first diagonal.
Only finite-dimensional algebra is formalized: no Weil form, operator domain,
support propagation, or infinite-dimensional inverse is asserted here. -/
theorem scalar_schur_equivalence (a b c : ℝ) (ha : 0 < a) :
    (∀ x y : ℝ, 0 ≤ a*x^2 + 2*b*x*y + c*y^2) ↔ 0 ≤ c - b^2/a := by
  have hane : a ≠ 0 := ne_of_gt ha
  constructor
  · intro h
    have hvalue := h (-b/a) 1
    have hid : a*(-b/a)^2 + 2*b*(-b/a)*1 + c*1^2 = c - b^2/a := by
      field_simp [hane]
      ring
    rw [hid] at hvalue
    exact hvalue
  · intro hs x y
    have hid : a*x^2 + 2*b*x*y + c*y^2 =
        a*(x + b/a*y)^2 + (c - b^2/a)*y^2 := by
      field_simp [hane]
      ring
    rw [hid]
    exact add_nonneg (mul_nonneg (le_of_lt ha) (sq_nonneg _))
      (mul_nonneg hs (sq_nonneg y))

#print axioms nonneg_of_pointwise_limit
#print axioms nonneg_of_vanishing_lower_error
#print axioms nonneg_on_dense
#print axioms coordinate_restrictions_nonneg
#print axioms larger_block_negative
#print axioms quartet_coefficient
#print axioms two_block_lower_bound
#print axioms scalar_schur_equivalence

end RhAudit
