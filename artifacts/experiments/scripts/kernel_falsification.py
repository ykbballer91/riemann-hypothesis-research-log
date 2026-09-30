#!/usr/bin/env python3
# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: experiments/scripts/kernel_falsification.py
# Original SHA-256: 199f9b7719f6e8712034acee36ab6eb6181beca955a35ad1006a81a94d5214e1
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""固定支持の核最適化不等式に対する8族の反証探索。

EXPERIMENTAL EVIDENCE。全て binary64 浮動小数点、区間認証なし。
区分一定関数の二重積分と f0 との距離には閉形式を使い、求積はしない。
これは解析的証明の代替でも新規結果でもない。
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path

import numpy as np


SEED = 20260929
A = 1.0 / math.sqrt(2.0)
C_MT = 0.5 + A / math.tan(A)
F0_NORM_SQUARED = (1.0 + math.sin(math.sqrt(2.0)) / math.sqrt(2.0)) / (4.0 * math.sin(A) ** 2)


def gaussian_cell_values(edges: np.ndarray, center: float, width: float) -> np.ndarray:
    """Gaussian の cell 平均。値を定める erf 評価自体は浮動小数点。"""
    erf_values = np.array([math.erf((float(x) - center) / (math.sqrt(2.0) * width))
                           for x in edges])
    return width * math.sqrt(math.pi / 2.0) * np.diff(erf_values) / np.diff(edges)


def trig_cell_values(edges: np.ndarray, frequency: float, sine: bool = False) -> np.ndarray:
    omega = 2.0 * math.pi * frequency
    if sine:
        return -np.diff(np.cos(omega * edges)) / (omega * np.diff(edges))
    return np.diff(np.sin(omega * edges)) / (omega * np.diff(edges))


def mass_one(values: np.ndarray, delta: float) -> np.ndarray:
    """区間長1なので定数補正で質量を1にする。丸め残差は記録する。"""
    result = values.copy()
    result += 1.0 - delta * float(np.sum(result))
    return result


def density(values: np.ndarray, delta: float) -> np.ndarray:
    mass = delta * float(np.sum(values))
    if not mass > 0.0:
        raise ValueError("Density prototype has nonpositive sampled mass")
    return mass_one(values / mass, delta)


def perturb(baseline: np.ndarray, values: np.ndarray, amplitude: float, delta: float) -> np.ndarray:
    mean_zero = values - delta * float(np.sum(values))
    return mass_one(baseline + amplitude * mean_zero, delta)


def families(n: int, edges: np.ndarray, baseline: np.ndarray) -> list[tuple[str, str, np.ndarray]]:
    delta = 1.0 / n
    centers = (edges[:-1] + edges[1:]) / 2.0
    result = []
    for width in (0.05, 0.15, 0.30):
        result.append(("Gaussian", f"center=0,width={width}",
                       density(gaussian_cell_values(edges, 0.0, width), delta)))
    for radius in (0.08, 0.20, 0.45):
        raw = np.zeros(n)
        mask = np.abs(centers) < radius
        raw[mask] = np.exp(-1.0 / (1.0 - (centers[mask] / radius) ** 2))
        result.append(("compact_smooth_bump", f"radius={radius};midpoint prototype",
                       density(raw, delta)))
    for center in (-0.30, 0.22):
        for width in (0.01, 0.025):
            result.append(("localized", f"center={center},width={width}",
                           density(gaussian_cell_values(edges, center, width), delta)))
    for frequency in (1, 3, 7):
        for amplitude in (0.25, 1.5):
            result.append(("oscillatory", f"frequency={frequency},amplitude={amplitude}",
                           perturb(baseline, trig_cell_values(edges, frequency), amplitude, delta)))
    for frequency in (n // 4, n // 2 - 1, 3 * n // 4):
        result.append(("high_frequency", f"frequency={frequency},amplitude=2",
                       perturb(baseline, trig_cell_values(edges, frequency, sine=True), 2.0, delta)))
    for sign in (-1, 1):
        for width_cells in (1, 3):
            center = sign * (0.5 - 0.5 * delta)
            width = width_cells * delta
            result.append(("boundary_concentrated", f"side={sign},width_cells={width_cells}",
                           density(gaussian_cell_values(edges, center, width), delta)))
    rng = np.random.default_rng(SEED + n)
    for draw in range(4):
        raw = rng.normal(size=n)
        for amplitude in (0.25, 1.0, 4.0):
            result.append(("seeded_random", f"seed={SEED+n},draw={draw},amplitude={amplitude}",
                           perturb(baseline, raw, amplitude, delta)))
    # 平均ゼロ部分空間の連続極限における最低方向 h(x)=sin(pi*x)。
    mode = trig_cell_values(edges, 0.5, sine=True)
    for amplitude in (0.2, 1.0, 3.0):
        result.append(("approximate_eigenfunction", f"h=sin(pi*x),amplitude={amplitude}",
                       perturb(baseline, mode, amplitude, delta)))
    assert len(set(name for name, _, _ in result)) == 8
    return result


def evaluate(name: str, parameters: str, f: np.ndarray, matrix: np.ndarray,
             cell_integrals_f0: np.ndarray, delta: float) -> dict:
    norm_squared = delta * float(f @ f)
    cross = float(f @ cell_integrals_f0)
    distance_squared = norm_squared - 2.0 * cross + F0_NORM_SQUARED
    energy = float(f @ matrix @ f)
    gap = energy - C_MT
    stability_rhs = (2.0 / 3.0) * distance_squared
    residual = gap - stability_rhs
    scale = max(1.0, abs(energy), norm_squared, abs(cross))
    # この閾値は候補の選別用であり、誤差の数学的上界ではない。
    screening_tolerance = 1e-10 * scale
    return {
        "family": name,
        "parameters": parameters,
        "mass_residual": delta * float(np.sum(f)) - 1.0,
        "min_cell_value": float(np.min(f)),
        "max_cell_value": float(np.max(f)),
        "C_f": energy,
        "C_f_minus_C_MT": gap,
        "L2_distance_to_f0_squared": distance_squared,
        "two_thirds_distance_squared": stability_rhs,
        "stability_residual": residual,
        "gap_over_distance_squared": gap / distance_squared if distance_squared > 0 else None,
        "screening_tolerance_not_certified": screening_tolerance,
        "negative_beyond_screening_tolerance": residual < -screening_tolerance,
    }


def run(n_values: list[int]) -> dict:
    grids = []
    all_samples = []
    for n in n_values:
        delta = 1.0 / n
        edges = np.linspace(-0.5, 0.5, n + 1)
        indices = np.arange(n)
        kernel = delta ** 3 * np.abs(indices[:, None] - indices[None, :]).astype(float)
        np.fill_diagonal(kernel, delta ** 3 / 3.0)
        matrix = delta * np.eye(n) + kernel
        weights = np.full(n, delta)
        cell_integrals_f0 = np.diff(np.sin(math.sqrt(2.0) * edges)) / (2.0 * math.sin(A))
        baseline = mass_one(cell_integrals_f0 / delta, delta)

        # 既知の区分一定関数f=1による積分行列の独立整合性確認。
        constant_energy = float(np.ones(n) @ matrix @ np.ones(n))
        assert abs(constant_energy - 4.0 / 3.0) < 1e-12
        assert abs(float(np.sum(cell_integrals_f0)) - 1.0) < 1e-12

        samples = [evaluate(name, parameters, values, matrix, cell_integrals_f0, delta)
                   for name, parameters, values in families(n, edges, baseline)]
        all_samples.extend({"N": n, **row} for row in samples)

        inverse_weight = np.linalg.solve(matrix, weights)
        denominator = float(weights @ inverse_weight)
        optimizer = mass_one(inverse_weight / denominator, delta)
        optimizer_result = evaluate("discrete_minimizer", "M^-1*w/(w^T*M^-1*w)",
                                    optimizer, matrix, cell_integrals_f0, delta)
        lagrange_residual = matrix @ optimizer - optimizer_result["C_f"] * weights
        optimizer_result.update({
            "closed_discrete_optimum_1_over_w_M_inverse_w": 1.0 / denominator,
            "lagrange_equation_max_abs_residual": float(np.max(np.abs(lagrange_residual))),
            "N_squared_continuum_energy_gap": n * n * optimizer_result["C_f_minus_C_MT"],
        })
        baseline_result = evaluate("cell_average_f0", "exact cell integral;binary64 evaluation",
                                   baseline, matrix, cell_integrals_f0, delta)
        grids.append({
            "N": n,
            "delta": delta,
            "constant_one_energy_minus_4_over_3": constant_energy - 4.0 / 3.0,
            "family_counts": dict(Counter(row["family"] for row in samples)),
            "sample_count": len(samples),
            "minimum_sample_stability_residual": min(row["stability_residual"] for row in samples),
            "maximum_absolute_sample_mass_residual": max(abs(row["mass_residual"]) for row in samples),
            "discrete_minimizer": optimizer_result,
            "cell_average_f0": baseline_result,
            "samples": samples,
        })

    extra_results = [{"N": grid["N"], **grid[key]} for grid in grids
                     for key in ("discrete_minimizer", "cell_average_f0")]
    combined_results = all_samples + extra_results
    candidates = [row for row in combined_results if row["negative_beyond_screening_tolerance"]]
    minimum = min(combined_results, key=lambda row: row["stability_residual"])
    return {
        "status": "EXPERIMENTAL EVIDENCE",
        "scope_ja": "既知の固定支持変分不等式への反証探索。RHの証明・反証ではなく、新規性も主張しない。",
        "arithmetic": "numpy float64 / Python binary64; interval certification NOT performed",
        "model_ja": "各等分cell上で一定の実関数。Gaussian等は入力値を作るための原型名であり、検査する関数自体は区分一定。",
        "integration_ja": "M=delta*I+B, offdiag B_ij=delta^3*abs(i-j), diagonal=delta^3/3 は区分一定関数の厳密な積分式。f0との内積とf0のL2ノルムにも閉形式を使う。求積誤差はないが、全式の浮動小数点評価誤差は未認証。",
        "sampling_ja": "入力原型の有限cell近似と、定義済みの区分一定関数の積分を区別する。格子間収束や未検査関数についての結論は出さない。",
        "inequality": "C(f)-C_MT >= (2/3)*||f-f0||_L2^2 for integral(f)=1",
        "C_MT": C_MT,
        "f0_L2_norm_squared": F0_NORM_SQUARED,
        "seed": SEED,
        "total_eight_family_samples": len(all_samples),
        "total_with_discrete_minimizers_and_f0_averages": len(combined_results),
        "negative_candidate_count": len(candidates),
        "negative_candidates": candidates,
        "minimum_stability_residual_case": minimum,
        "summary_ja": "負の候補なしは証明ではない。解析的証明の代替には使用しない。" if not candidates
                      else "負の候補あり。丸め・正規化・式を独立精査してから反例と判定する。",
        "grids": grids,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results" / "kernel_falsification.json")
    args = parser.parse_args()
    result = run([32, 64, 128, 256])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "samples": result["total_eight_family_samples"],
        "negative_candidates": result["negative_candidate_count"],
        "minimum_stability_residual": result["minimum_stability_residual_case"]["stability_residual"],
        "discrete_minimizer_gaps": [{"N": grid["N"],
                                     "C_minus_C_MT": grid["discrete_minimizer"]["C_f_minus_C_MT"]}
                                    for grid in result["grids"]],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
