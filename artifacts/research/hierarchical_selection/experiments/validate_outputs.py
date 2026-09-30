# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/hierarchical_selection/experiments/validate_outputs.py
# Original SHA-256: 1da06b0e8853f2314e008ffcacea7921f9e56a64a42a5e716816a3c192a424bf
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Preservation, artifact and diagnostic consistency checks, not formal proof."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
import mpmath as mp

ROOT=Path(__file__).resolve().parents[3]
TRACK=ROOT/'research/hierarchical_selection'
mp.mp.dps=70
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((TRACK/'preservation_baseline.json').read_text())
changed=[s for s,h in baseline['sha256'].items()
         if not (ROOT/s).is_file() or sha(ROOT/s)!=h]
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
assert not changed and head==baseline['head'], (changed,head)

required=[
 'research/hierarchical_selection.md',
 'research/higher_order_gamma_selection.md',
 'research/fourier_resolution_transition.md',
 'research/prime_rank_one_flow.md',
 'research/sonine_filtration_audit.md',
 'research/hierarchical_selection_candidate_matrix.md',
 'proofs/audits/hierarchical_selection_adversarial.md',
 'research/hierarchical_selection_state.json',
]
assert all((ROOT/s).is_file() for s in required)
files=sorted(set([ROOT/s for s in required]+[p for p in TRACK.rglob('*') if p.is_file()]))
jsons=[]; scripts=[]; badlinks=[]; badmath=[]; controls=[]
for p in files:
 if p.suffix not in ('.json','.md','.txt','.py'): continue
 s=p.read_text()
 if any(ord(c)<32 and c not in '\n\r\t' for c in s): controls.append(str(p))
 if p.suffix=='.json': json.loads(s); jsons.append(str(p.relative_to(ROOT)))
 if p.suffix=='.py': ast.parse(s,filename=str(p)); scripts.append(str(p.relative_to(ROOT)))
 if p.suffix=='.md' and p.name!='request.md':
  if s.count(r'\[')!=s.count(r'\]'): badmath.append(str(p.relative_to(ROOT)))
  for t in re.findall(r'\]\(([^\s)]+)\)',s):
   if t.startswith(('http://','https://','#','mailto:')): continue
   if not (p.parent/t.split('#')[0]).exists(): badlinks.append([str(p.relative_to(ROOT)),t])
assert not badlinks and not badmath and not controls, (badlinks,badmath,controls)

scaled=json.loads((TRACK/'experiments/scaled_boundary_results.json').read_text())
assert len(scaled['effective_profile_tests'])==12
assert len(scaled['first_theta_fourier_diagnostics'])==20
max_identity_error=mp.mpf(0)
for r in scaled['scalar_profile_identity_checks']:
 h=mp.mpf(r['h'])
 expected=1-(mp.atan(h)+h/(1+h*h))/mp.pi
 max_identity_error=max(max_identity_error,abs(expected-mp.mpf(r['J_e_minus_v'])))
assert max_identity_error<mp.mpf('1e-46')
for r in scaled['effective_profile_tests']:
 m=r['m']; J=mp.matrix([[mp.mpf(x) for x in row] for row in r['matrix']])
 H=mp.matrix([[mp.factorial(i+j)/mp.mpf(2)**(i+j+1) for j in range(m+1)] for i in range(m+1)])
 assert min(mp.eigsy(J,eigvals_only=True))>0
 assert min(mp.eigsy(J-H,eigvals_only=True))>-mp.mpf('1e-44')
 assert min(mp.eigsy(2*H-J,eigvals_only=True))>-mp.mpf('1e-44')
 c=mp.matrix([mp.mpf(x) for x in r['monic_minimizing_profile_coefficients']])
 assert abs(c[m]-1)<mp.mpf('1e-46')
 assert mp.norm((J*c)[:m,0])<mp.mpf('1e-42')

actual=json.loads((TRACK/'experiments/actual_resolution_results.json').read_text())
assert [c['N'] for c in actual['cases']]==[4,8,12,20,40]
assert sum(len(c['restricted']) for c in actual['cases'])==15
for c in actual['cases']:
 h=mp.pi*c['N']/(2*mp.log(3)*(mp.pi*9))
 assert abs(h-mp.mpf(c['h']))<mp.mpf('1e-43')
 for r in c['restricted']:
  eig=list(map(mp.mpf,r['eigenvalues']))
  assert eig==sorted(eig)
  assert mp.mpf(r['raw_coefficients_leading_one'][0])==1
state=json.loads((ROOT/'research/hierarchical_selection_state.json').read_text())
assert state['rh_status']=='OPEN' and not state['rh_closed'] and not state['G_star_proved']
assert not state['actual_full_ground_to_k_comparison_proved']
assert not state['uniform_m_to_infinity_control_proved']
assert not state['sharp_necessary_transition_constant_identified']
assert state['support_all_fixed_finite_m_selection_proved'] and state['resolved_full_selector_is_k']

snapshot=json.loads((TRACK/'notes/independent_audit_snapshot.json').read_text())
assert snapshot['status']=='PASS'
audit_changed=[p for p,h in snapshot['sha256'].items() if sha(ROOT/p)!=h]
assert not audit_changed,audit_changed

result={
 'time_utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS','rh_status':'OPEN',
 'prior_files_checked':len(baseline['sha256']),
 'prior_files_changed':changed,'head_unchanged':True,
 'required_outputs_present':required,
 'json_syntax_checked':jsons,'python_ast_checked':scripts,
 'broken_local_links':badlinks,'unbalanced_display_math':badmath,
 'control_characters':controls,
 'effective_profile_problems':12,'sampled_Fourier_diagnostics':20,
 'actual_small_cutoff_endpoints':5,'actual_restricted_problems':15,
 'scalar_profile_identity_max_rounding_error':mp.nstr(max_identity_error,12),
 'independently_audited_artifact_hashes_matched':len(snapshot['sha256']),
 'artifact_sha256':{str(p.relative_to(ROOT)):sha(p) for p in files if p.name!='validation.json'},
 'scope':'File preservation, syntax, saved diagnostics and audit snapshot consistency. Not interval numerical certification, machine-checked proof, external-paper full re-audit, actual full-ground comparison, or RH proof.'
}
(TRACK/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('status','prior_files_checked','prior_files_changed','head_unchanged',
 'effective_profile_problems','sampled_Fourier_diagnostics','actual_small_cutoff_endpoints',
 'actual_restricted_problems','independently_audited_artifact_hashes_matched')},indent=2))
