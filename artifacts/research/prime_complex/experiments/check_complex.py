# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/prime_complex/experiments/check_complex.py
# Original SHA-256: ca53d18a237963ae38b76f4a7fc970f6aa8fe5c6e5fedc0f837d72e8917de687
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Finite exact structural checks. No asymptotic fit or RH inference.

Independent checks include rational boundary ranks, Hodge kernel ranks,
ordinary F_2 persistence reduction, incidence matchings and weighted models.
"""
from pathlib import Path
from collections import Counter, deque
from itertools import combinations
from math import isqrt, prod
from random import Random
import json
from flint import fmpq_mat

OUT = Path(__file__).with_name('results.json')
LIMIT = 10000


def sieve(limit):
    factors = [[] for _ in range(limit+1)]
    primes = []
    for p in range(2, limit+1):
        if not factors[p]:
            primes.append(p)
            for n in range(p, limit+1, p):
                factors[n].append(p)
    mu = [0]*(limit+1)
    mu[1] = 1
    for n in range(2, limit+1):
        if prod(factors[n]) == n:
            mu[n] = (-1)**len(factors[n])
    return primes, factors, mu


PRIMES, FAC, MU = sieve(LIMIT)


def faces(X):
    return [n for n in range(1, X+1) if MU[n]]


def critical(X):
    return [n for n in faces(X) if n % 2 and 2*n > X]


def acyclic(X, matching):
    fs = faces(X)
    adjacency = {n: [] for n in fs}
    indegree = {n: 0 for n in fs}
    pairs = {frozenset(pair) for pair in matching}
    for n in fs:
        for p in FAC[n]:
            m = n//p
            source, target = (m, n) if frozenset((m, n)) in pairs else (n, m)
            adjacency[source].append(target)
            indegree[target] += 1
    queue = deque(n for n in fs if indegree[n] == 0)
    count = 0
    while queue:
        n = queue.popleft()
        count += 1
        for m in adjacency[n]:
            indegree[m] -= 1
            if indegree[m] == 0:
                queue.append(m)
    return count == len(fs)


def maximum_incidence_matching(X):
    fs = faces(X)
    adjacency = {n: [] for n in fs if MU[n] == 1}
    for n in fs:
        for p in FAC[n]:
            m = n//p
            even, odd = (n, m) if MU[n] == 1 else (m, n)
            adjacency[even].append(odd)
    mate = {}

    def augment(n, visited):
        for m in adjacency[n]:
            if m in visited:
                continue
            visited.add(m)
            if m not in mate or augment(mate[m], visited):
                mate[m] = n
                return True
        return False

    for n in adjacency:
        augment(n, set())
    pairs = [(n, m) for m, n in mate.items()]
    return pairs


def boundary_matrix(X, k):
    # Augmented degree of n is omega(n)-1, including n=1 in degree -1.
    columns = [n for n in faces(X) if len(FAC[n])-1 == k]
    rows = [n for n in faces(X) if len(FAC[n])-1 == k-1]
    matrix = fmpq_mat(len(rows), len(columns))
    row_index = {n: i for i, n in enumerate(rows)}
    for j, n in enumerate(columns):
        for i, p in enumerate(FAC[n]):
            matrix[row_index[n//p], j] = (-1)**i
    return matrix


def rational_homology(X, hodge=False):
    fs = faces(X)
    dims = Counter(len(FAC[n])-1 for n in fs)
    top = max(dims)
    boundary = {k: boundary_matrix(X, k) for k in range(-1, top+2)}
    ranks = {k: B.rank() for k, B in boundary.items()}
    betti = {k: dims[k]-ranks[k]-ranks[k+1] for k in range(-1, top+1)}
    predicted = Counter(len(FAC[n])-1 for n in critical(X))
    assert all(betti[k] == predicted[k] for k in betti)
    for k in range(0, top+1):
        product_matrix = boundary[k-1]*boundary[k]
        assert all(entry == 0 for entry in product_matrix.entries())
    kernel = {}
    if hodge:
        for k in range(-1, top+1):
            B, C = boundary[k], boundary[k+1]
            laplacian = B.transpose()*B + C*C.transpose()
            kernel[k] = dims[k]-laplacian.rank()
        assert kernel == betti
    return {'X': X, 'betti_by_augmented_degree': betti,
            'hodge_kernel_by_degree': kernel if hodge else None,
            'total_reduced_betti': sum(betti.values())}


def persistence(cap):
    fs = faces(cap)
    index = {n: i for i, n in enumerate(fs)}
    pivot_column = {}
    births = set()
    intervals = []
    for n in fs:
        col = 0
        for p in FAC[n]:
            col ^= 1 << index[n//p]
        while col:
            low = col.bit_length()-1
            if low not in pivot_column:
                break
            col ^= pivot_column[low]
        if not col:
            births.add(n)
        else:
            low = col.bit_length()-1
            birth = fs[low]
            assert birth in births
            pivot_column[low] = col
            intervals.append((birth, n, len(FAC[birth])-1))
    actual = sorted(intervals)
    predicted = sorted((n, 2*n, len(FAC[n])-1)
                       for n in fs if n % 2 and 2*n <= cap)
    assert actual == predicted
    dead = {b for b, _, _ in actual}
    alive = sorted(births-dead)
    assert alive == critical(cap)
    return {'cap': cap, 'finite_intervals': actual,
            'alive_at_cap': alive,
            'all_intervals_match_birth_n_death_2n': True}


def naive_toggle(n, X):
    # Smallest prime for which toggling is admissible: this is NOT an involution.
    for p in PRIMES:
        if n % p == 0:
            return n//p
        if n*p <= X:
            return n*p
    return n


def weighted_model(weights, X):
    # Weights are exact integers and vertices remain independent labels.
    vertices = range(len(weights))
    fs = []
    for k in range(len(weights)+1):
        for S in combinations(vertices, k):
            if prod(weights[j] for j in S) <= X:
                fs.append(frozenset(S))
    face_set = set(fs)
    matched = [(S, S|{0}) for S in fs if 0 not in S and S|{0} in face_set]
    residual = [S for S in fs if 0 not in S and S|{0} not in face_set]
    parity_sum = sum((-1)**len(S) for S in fs)
    assert parity_sum == sum((-1)**len(S) for S in residual)
    assert len(fs) == 2*len(matched)+len(residual)
    # Every proper residual face lies in the minimum-vertex star.
    assert all((S-{v})|{0} in face_set for S in residual for v in S)
    return {'weights': weights, 'X': X, 'face_count': len(fs),
            'pairs': len(matched), 'residual_count': len(residual),
            'signed_residual': parity_sum}


table = []
for X in [2, 3, 5, 10, 15, 30, 60, 100, 210, 1000, 5000, 10000]:
    fs, residual = faces(X), critical(X)
    matching = [(n, 2*n) for n in fs if n % 2 and 2*n <= X]
    assert len(fs) == 2*len(matching)+len(residual)
    assert acyclic(X, matching)
    assert sum(MU[n] for n in fs) == sum(MU[n] for n in residual)
    isolated = [p for p in PRIMES if X//2 < p <= X]
    row = {
        'X': X, 'squarefree_faces_including_empty': len(fs),
        'toggle2_pairs': len(matching), 'unmatched': len(residual),
        'unmatched_mu_plus': sum(MU[n] == 1 for n in residual),
        'unmatched_mu_minus': sum(MU[n] == -1 for n in residual),
        'M': sum(MU[n] for n in fs),
        'min_unmatched_location': min(residual) if residual else None,
        'max_unmatched_location': max(residual) if residual else None,
        'large_prime_singletons_X_over_2': len(isolated),
        'any_face_matching_unmatched_lower_bound': max(0, len(isolated)-1)
    }
    if X <= 210:
        maximal = maximum_incidence_matching(X)
        row['maximum_incidence_matching_unmatched'] = len(fs)-2*len(maximal)
        row['maximum_matching_is_acyclic'] = acyclic(X, maximal)
    table.append(row)

homology = [rational_homology(X, hodge=X<=60)
            for X in [1, 2, 3, 5, 10, 15, 30, 60, 100, 210]]
bars = persistence(1000)
details = [{'n': n, 'primes': FAC[n], 'mu': MU[n],
            'homology_degree': len(FAC[n])-1,
            'largest_prime': max(FAC[n]) if n>1 else None,
            'birth': n, 'death': 2*n}
           for n in critical(100)]

bad_involution = {'X': 5, 'face': 3, 'first': naive_toggle(3, 5),
                  'second': naive_toggle(naive_toggle(3, 5), 5)}
assert bad_involution['first'] == 1 and bad_involution['second'] == 2

# A minimal deterministic countermodel: equal-weight independent vertices.
# At cutoff equal to the weight, the complex is a disjoint set of vertices.
weighted = [weighted_model([2, 3, 5, 7], X) for X in [5, 15, 30, 210]]
weighted += [weighted_model([4]*8, 4),
             weighted_model([2, 4, 8, 16], 20),
             weighted_model([3, 7, 11, 19], 100)]
assert weighted_model([4]*8, 4)['signed_residual'] == -7
rng = Random(20260930)
for _ in range(3):
    weights = sorted(p*rng.randint(1,4) for p in [2,3,5,7,11])
    model = weighted_model(weights, 300)
    model['kind'] = 'seeded prime-weight perturbation, not actual prime arithmetic'
    model['seed'] = 20260930
    weighted.append(model)

# All-integers substitution violates the prime-set encoding (4 and 2 coincide).
all_integer_collision = {'distinct_integers': [2, 4],
                         'same_prime_set': [2], 'mu_values': [-1, 0]}
flag_counterexample = {'X': 15, 'vertices': [2,3,5],
                      'edge_products': [6,10,15], 'triple_product': 30}

result = {
    'rh_status': 'OPEN',
    'purpose': 'exact finite structural falsification; no growth fitting',
    'arithmetic_table': table,
    'rational_homology_and_hodge_checks': homology,
    'persistence': bars,
    'critical_records_X100': details,
    'naive_smallest_admissible_toggle_failure': bad_involution,
    'weighted_synthetic_models': weighted,
    'all_integers_collision': all_integer_collision,
    'flag_completion_counterexample': flag_counterexample,
    'all_checks_passed': True,
    'limitations': [
        'Rational ranks and integer checks are exact; no finite data proves an asymptotic bound.',
        'Persistence computation uses F_2; the separate filtered Z-chain proof supplies coefficient-independent intervals.',
        'Maximum incidence matchings are diagnostics and need not be acyclic.',
        'Synthetic weighted models do not preserve actual prime arithmetic and are not RH counterexamples.'
    ]
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'table': table, 'exact_rational_tests': len(homology),
                  'barcode_pairs_checked': len(bars['finite_intervals']),
                  'all_checks_passed': True}, indent=2))
