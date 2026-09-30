/- STATUS: RIEMANN HYPOTHESIS OPEN
Sanitized historical Lean source; not rebuilt during this export.
Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
Source: research/one_prime/formal/ReturnLemma.lean
Original SHA-256: b870ee307670b880942c6d4396ba6772b929ecd7071276b6c4870cbee1b2bf69
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic

/-! Scalar kernel of the subexponential-return lemma.
No arithmetic quotient, zeta theorem, operator norm, or RH is assumed here.
The conversion from operator/seminorm bounds is proved in abstract_return.md.
-/

namespace OnePrimeReturn

theorem growth_comparison (a b C : ℝ) (hb : 0 < b)
    (h : ∀ n : ℕ, a ^ n ≤ C * b ^ n) : a ≤ b := by
  by_contra hab
  have hratio : 1 < a / b := (one_lt_div hb).2 (lt_of_not_ge hab)
  obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt C hratio
  have hle : (a / b) ^ n ≤ C := by
    rw [div_pow]
    exact (div_le_iff₀ (pow_pos hb n)).2 (h n)
  exact (not_lt_of_ge hle) hn

theorem subexponential_le_one (a : ℝ)
    (h : ∀ b : ℝ, 1 < b → ∃ C : ℝ, ∀ n : ℕ, a ^ n ≤ C * b ^ n) :
    a ≤ 1 := by
  by_contra ha
  have hgt : 1 < a := lt_of_not_ge ha
  obtain ⟨C, hC⟩ := h ((a + 1) / 2) (by linarith)
  have hh := growth_comparison a ((a + 1) / 2) C (by linarith) hC
  linarith

theorem bilateral_subexponential_eq_one (a : ℝ) (ha : 0 < a)
    (hf : ∀ b : ℝ, 1 < b → ∃ C : ℝ, ∀ n : ℕ, a ^ n ≤ C * b ^ n)
    (hb : ∀ b : ℝ, 1 < b → ∃ C : ℝ, ∀ n : ℕ, (a⁻¹) ^ n ≤ C * b ^ n) :
    a = 1 := by
  have hupper := subexponential_le_one a hf
  have hinv := subexponential_le_one a⁻¹ hb
  have hprod := mul_le_mul_of_nonneg_left hinv (le_of_lt ha)
  have hne : a ≠ 0 := ne_of_gt ha
  simp only [mul_inv_cancel₀ hne, mul_one] at hprod
  exact le_antisymm hupper hprod

theorem real_exponent_zero (alpha L : ℝ) (hL : 0 < L)
    (hf : ∀ b : ℝ, 1 < b → ∃ C : ℝ, ∀ n : ℕ,
      (Real.exp (alpha * L)) ^ n ≤ C * b ^ n)
    (hb : ∀ b : ℝ, 1 < b → ∃ C : ℝ, ∀ n : ℕ,
      ((Real.exp (alpha * L))⁻¹) ^ n ≤ C * b ^ n) : alpha = 0 := by
  have hexp := bilateral_subexponential_eq_one (Real.exp (alpha * L))
    (Real.exp_pos _) hf hb
  have hz : alpha * L = 0 := Real.exp_injective (hexp.trans Real.exp_zero.symm)
  exact (mul_eq_zero.mp hz).resolve_right (ne_of_gt hL)

#print axioms growth_comparison
#print axioms subexponential_le_one
#print axioms bilateral_subexponential_eq_one
#print axioms real_exponent_zero

end OnePrimeReturn
