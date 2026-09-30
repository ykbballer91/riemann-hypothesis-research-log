# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/local_to_global/experiments/check_normalization_and_tail.py
# Original SHA-256: 563e725dcdb2c5a285af7924aca8926ccfdb88a281887569890156a588cfe6f6
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Diagnostic checks only. No zero-location or convergence inference from samples."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 65


def xi(s):
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 2


def h(x):
    return mp.pi / 2 * x**2 * (2 * mp.pi * x**2 - 3) * mp.exp(-mp.pi * x**2)


def k_positive_log(t):
    u = mp.exp(t)
    return mp.sqrt(u) * sum(h(n * u) for n in range(1, 13))


def cstr(z):
    return {"real": mp.nstr(mp.re(z), 30), "imag": mp.nstr(mp.im(z), 30)}


checks = []
for s in (mp.mpf(2), mp.mpf(3), mp.mpc(2, 1)):
    observed = mp.quad(lambda x: h(x) * x ** (s - 1), [0, 0.5, 1, 2, 4, mp.inf])
    exact = s * (s - 1) / 8 * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2)
    error = abs(observed - exact)
    assert error < mp.mpf("1e-50")
    checks.append({"s": cstr(s), "mellin_abs_error": mp.nstr(error, 8),
                   "zeta_times_mellin_divided_by_xi": cstr(mp.zeta(s) * observed / xi(s))})

fourier_checks = []
for z in (mp.mpf(0), mp.mpf(2), mp.mpc(0, "0.25"), mp.mpc(3, "0.3")):
    observed = 2 * mp.quad(lambda t: k_positive_log(t) * mp.cos(z * t),
                           [0, 0.5, 1, 1.5, 2, 3])
    error = abs(observed - xi(mp.mpf("0.5") + 1j * z) / 4)
    assert error < mp.mpf("1e-45")
    fourier_checks.append({"z": cstr(z), "fourier_abs_error": mp.nstr(error, 8)})

# The N=0 admissible finite model has v=1 and Fourier transform 2 sin(a z)/z.
# Normalized at z*=i/4 it tends to 0 on R but not at z*, so it cannot converge
# locally uniformly to a nonzero holomorphic function on the critical strip.
tail_diagnostic = []
for a in (4, 8, 16, 32, 64):
    denom = 4 * mp.sinh(mp.mpf(a) / 4)
    tail_diagnostic.append({
        "log_lambda": a, "N": 0,
        "normalized_value_at_0": mp.nstr(a / denom, 20),
        "normalized_value_at_i_over_4": "1",
        "normalized_value_at_0_4i":
            mp.nstr((mp.sinh(mp.mpf("0.4") * a) / mp.mpf("0.4")) / denom, 20),
        "real_tail_spacing": mp.nstr(mp.pi / a, 20),
    })

result = {
    "purpose": "normalization verification and explicit failed limiting path",
    "precision_decimal_digits": mp.mp.dps,
    "certified_interval_computation": False,
    "proof_location": "../notes/spectral_approximants_and_exact_gap.md",
    "mellin_checks": checks,
    "fourier_checks": fourier_checks,
    "N_zero_tail_diagnostic": tail_diagnostic,
    "rh_inference": "NONE",
    "all_diagnostic_assertions_passed": True,
}
path = Path(__file__).with_name("results.json")
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"assertions": "PASS", "output": str(path)}, ensure_ascii=False))
