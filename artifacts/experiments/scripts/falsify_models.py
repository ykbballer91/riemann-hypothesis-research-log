#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/falsify_models.py
# Original SHA-256: f19e4effbf0697bb0d782a1d7d515a759ae60f3d564df1cbb72c4d384bc6ac80
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""RH 研究の偽短絡を検査する独立した有限モデル。

標準ライブラリのみ。Fraction による厳密計算と、明示的に非保証とした
Decimal 積分近似を分離する。これらは ζ の零点についての反例ではない。
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class QC:
    """有理実部・虚部を持つ複素数。丸めを一切行わない。"""

    re: F
    im: F = F(0)

    def __add__(self, other: QC | F | int) -> QC:
        other = as_qc(other)
        return QC(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> QC:
        return QC(-self.re, -self.im)

    def __sub__(self, other: QC | F | int) -> QC:
        return self + -as_qc(other)

    def __mul__(self, other: QC | F | int) -> QC:
        other = as_qc(other)
        return QC(self.re * other.re - self.im * other.im,
                  self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def conj(self) -> QC:
        return QC(self.re, -self.im)

    def square(self) -> QC:
        return self * self

    def data(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im)}


def as_qc(value: QC | F | int) -> QC:
    return value if isinstance(value, QC) else QC(F(value))


def smooth_bump_moment(subintervals: int, precision: int) -> Decimal:
    """Composite Simpson: 積分誤差は保証しない。高精度は演算桁数のみ。"""
    assert subintervals > 0 and subintervals % 2 == 0
    with localcontext() as context:
        context.prec = precision
        step = Decimal(2) / subintervals
        total = Decimal(0)
        for k in range(1, subintervals):
            x = Decimal(-1) + step * k
            value = (-Decimal(1) / (1 - x * x) + x / 4).exp()
            total += (4 if k % 2 else 2) * value
        return +(step * total / 3)


def calculate(precision: int) -> dict:
    compression_values = [
        {"N": n, "Q(P_N_u)": str((1 - F(1, 4**n)) / 3)}
        for n in (1, 2, 4, 8, 16)
    ]
    assert all(F(row["Q(P_N_u)"]) > 0 for row in compression_values)

    window_values = []
    for parameter in (F(0), F(1), F(2)):
        q_value = 2 - 2 * parameter
        window_values.append({"L": str(parameter), "eigenvalues":
                              [str(1 - parameter), str(1 + parameter)],
                              "Q((1,-1))": str(q_value)})
    assert window_values[-1]["Q((1,-1))"] == "-2"

    # F(s) = ((s-1/2-a)^2+1)((s-1/2+a)^2+1).
    a = F(1, 4)
    roots = [QC(F(1, 2) + sign_re * a, F(sign_im))
             for sign_re in (-1, 1) for sign_im in (-1, 1)]
    root_checks = []
    for rho in roots:
        centered = rho - F(1, 2)
        value = ((centered - a).square() + 1) * ((centered + a).square() + 1)
        assert value == QC(F(0))
        root_checks.append({"rho": rho.data(), "F(rho)": value.data()})
    assert all(rho.re != F(1, 2) for rho in roots)

    # f = ((iD+1)^2+a^2)(exp(-ix) h'), h は偶・非負 bump。
    # A = integral h(x) exp(a*x) dx。下では F_f(z)/A を厳密計算。
    z_plus = QC(F(1), a)
    z_minus = QC(F(1), -a)
    p_plus = (z_plus + 1).square() + a * a
    p_minus = (z_minus + 1).square() + a * a
    transform_plus = a * p_plus
    transform_minus = -a * p_minus
    quartet_coefficient = (transform_plus * transform_minus.conj()
                           + transform_minus * transform_plus.conj())
    assert quartet_coefficient == QC(F(-15, 8))
    for sign in (-1, 1):
        negative_ordinate_z = QC(F(-1), sign * a)
        assert (negative_ordinate_z + 1).square() + a * a == QC(F(0))

    # 高精度近似は証明から隔離する。厳密な負値証明は有理係数と A>0 のみ。
    approximations = []
    with localcontext() as context:
        context.prec = precision
        for n in (256, 512, 1024, 2048):
            moment = smooth_bump_moment(n, precision)
            approximations.append({
                "subintervals": n,
                "A_approx": str(moment),
                "Q_quartet_approx": str(-Decimal(15) / 8 * moment * moment),
            })

    return {
        "status": "EXPERIMENTAL EVIDENCE; exact rational certificates separated",
        "scope_ja": "抽象的な偽短絡の有限モデル。リーマン予想への反例ではない。",
        "arithmetic": {"exact": "fractions.Fraction", "decimal_precision": precision,
                       "quadrature_error_certified": False},
        "F01_missing_form_convergence": {
            "domain": "D=c00 direct_sum C*u inside l2, u_j=2^(-j), j>=1",
            "form": "Q(x+alpha*u)=sum_j |x_j|^2 - |alpha|^2",
            "all_coordinate_compressions_PSD": True,
            "Q(u)": "-1", "limit_Q(P_N_u)": "1/3",
            "finite_values": compression_values,
            "missing_hypothesis": "Pointwise convergence of forms on the target domain",
        },
        "F01b_escaping_negative_direction": {
            "operator": "A_n=I-2*projection_onto(e_n)",
            "fixed_k_compression_for_n_gt_k": "I_k",
            "Q_n(e_n)": "-1", "strong_limit": "I",
            "caution_ja": "実際のstrong limitはPSD。この例は極限PSDを反証せず、各nの全体PSDへの量化交換だけを反証する。",
        },
        "F02_dimension_and_window_growth": {
            "dimension_example": {"matrix": [[1, 0], [0, -1]],
                                  "first_compression_eigenvalue": 1,
                                  "full_negative_witness": [0, 1], "witness_value": -1},
            "window_matrix": "[[1,L],[L,1]]", "window_values": window_values,
            "increment_L0_to_L2_at_witness_1_minus1": "-4",
        },
        "F03_ordinates_are_insufficient": {
            "entire_function": "((s-1/2-1/4)^2+1)*((s-1/2+1/4)^2+1)",
            "functional_symmetries": ["F(1-s)=F(s)", "F(conj(s))=conj(F(s))"],
            "roots_verified_exactly": root_checks,
            "self_adjoint_ordinate_operator": "diag(-1,1,-1,1)",
            "all_roots_off_critical_line": True,
            "not_zeta_ja": "ζやξではない。関数等式の基本対称性だけでは不十分だと示す。",
        },
        "F04_off_axis_Weil_type_quartet": {
            "spectral_points": "z=+/-1 +/- i/4",
            "test_function": "f=((iD+1)^2+1/16)(exp(-ix)*h_prime)",
            "bump": "h(x)=exp(-1/(1-x^2)) for |x|<1, and 0 otherwise",
            "A": "integral h(x)*exp(x/4) dx > 0",
            "F_f(1+i/4)_div_A": transform_plus.data(),
            "F_f(1-i/4)_div_A": transform_minus.data(),
            "F_f(-1+/-i/4)": "0",
            "Q_quartet_div_A_squared": quartet_coefficient.data(),
            "exact_negative_bound": "Q_quartet <= -(15/8)*exp(-8/3) < 0",
            "numerical_only_integral_approximations": approximations,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--precision", type=int, default=70)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results" / "falsify_models.json")
    args = parser.parse_args()
    if args.precision < 30:
        parser.error("--precision must be >= 30")
    result = calculate(args.precision)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"result": str(args.output), "exact_assertions": "PASS",
                      "RH_proved_or_disproved": False}, ensure_ascii=False))


if __name__ == "__main__":
    main()
