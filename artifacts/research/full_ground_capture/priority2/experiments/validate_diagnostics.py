# STATUS: RIEMANN HYPOTHESIS OPEN
# Public credit: @ykbballer91; AI-assisted
# SPDX-License-Identifier: MIT
# Source: research/full_ground_capture/priority2/experiments/validate_diagnostics.py
# Original SHA-256: ee6de8bb5ff8bc793e74e3e97a3187950ceefaa4985c03853efef108778ee24c
"""Compare independent precision/quadrature runs; no proof of rank from floats."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 80
p = Path(__file__).parent
lo = json.loads((p/'probe_85.json').read_text())
hi = json.loads((p/'probe_115.json').read_text())
rows = []
for a, b in zip(lo['records'], hi['records']):
    assert a['N'] == b['N'] and a['label'] == b['label']
    for key in ['actual_sigma_min', 'actual_raw_condition', 'tail_operator_norm']:
        x, y = mp.mpf(a[key]), mp.mpf(b[key])
        assert abs(x-y)/max(abs(y), mp.mpf('1e-1000')) < mp.mpf('1e-30')
    for key in ['actual_global_Gram_singular_values', 'actual_support_Gram_singular_values']:
        x, y = mp.mpf(a[key][-1]), mp.mpf(b[key][-1])
        assert abs(x-y)/abs(y) < mp.mpf('1e-19')
    assert mp.mpf(b['quadrature_crosscheck_relative']) < mp.mpf('1e-95')
    assert all(0 < mp.mpf(s) < 1+mp.mpf('1e-15')
               for s in b['actual_global_Gram_singular_values'])
    rows.append({'a': b['a'], 'N': b['N'],
                 'raw_repeat_agreement_relative': '<1e-30; comparisons of 35-digit serialized values',
                 'physical_min_repeat_agreement_relative': '<1e-19',
                 'independent_quadrature_relative': '<1e-95'})
(p/'diagnostic_validation.json').write_text(json.dumps({
    'RH_assumed': False, 'diagnostics_not_proof': True, 'checks': rows}, indent=2)+'\n')
print('Diagnostic comparisons PASS; this is not an interval proof.')
