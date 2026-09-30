# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: research/rate_history/experiments/splitting_probe.py
# Original SHA-256: c768b6d405621a18611f7f903d378307363ec65e96885fc993d071b334b679eb
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Actual finite Weil splitting of k,k'',k^(4),k^(6).

High-precision diagnostic, NOT an interval or asymptotic certificate.
Arb matrix midpoints and high-precision Gauss integration are used.
No zeta zeros, fitted rates, invented metric, or old output writes.
"""
from pathlib import Path
import sys, json, re, math
sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'experiments/scripts'))
from groskin_independent_certificate import build
import mpmath as mp

OUT=Path(__file__).parent
mp.mp.dps=100
NUM=re.compile(r'[-+]?\d+(?:\.\d*)?(?:e[-+]?\d+)?')
def midpoint(ball):
    return mp.mpf(NUM.search(ball.str(120,more=True)).group())
def val(x):
    return mp.nstr(x,45)
def serialize(A):
    return [[val(A[i,j]) for j in range(A.cols)] for i in range(A.rows)]
def realdot(x,y):
    return (x.T*y)[0]

# k(t)=exp(t/2) sum_n P0(pi*n² exp(2t))*exp(-pi*n² exp(2t)), t>=0.
# Only even derivatives are used; Poisson symmetry gives f_j(-t)=f_j(t).
polys=[[mp.mpf(0),-mp.mpf(3)/2,mp.mpf(1)]]
for r in range(6):
    p=polys[-1]; q=[mp.mpf(0)]*(len(p)+1)
    for j,c in enumerate(p):
        q[j]+=(mp.mpf('0.5')+2*j)*c
        q[j+1]-=2*c
    polys.append(q)

def fs(t):
    t=abs(t); fac=mp.exp(t/2); y0=mp.pi*mp.exp(2*t)
    out=[mp.mpf(0)]*4
    # n>12 contributes <1e-200 at t=0, including degree-eight polynomials.
    for n in range(1,13):
        y=y0*n*n
        if y>800: break
        ex=fac*mp.exp(-y)
        for j in range(4):
            out[j]+=mp.polyval(list(reversed(polys[2*j])),y)*ex
    return out

QUAD={}
def quadrature(n):
    if n not in QUAD: QUAD[n]=mp.gauss_quadrature(n,"legendre")
    return QUAD[n]

def columns(cut,N,nquad):
    a=mp.log(cut)/2; nodes,weights=quadrature(nquad)
    ints=mp.matrix(N+1,4); norms=mp.matrix(4,4)
    for x,w in zip(nodes,weights):
        t=a*(x+1)/2; wt=a*w/2; f=fs(t)
        for j in range(4):
            for k in range(4): norms[j,k]+=2*wt*f[j]*f[k]
        for n in range(N+1):
            sc=2*(-1)**n/mp.sqrt(2*a)*mp.cos(mp.pi*n*t/a)*wt
            for j in range(4): ints[n,j]+=sc*f[j]
    B=mp.matrix(2*N+1,4)
    for n in range(-N,N+1):
        for j in range(4): B[n+N,j]=ints[abs(n),j]
    return B,norms

def global_gram():
    # a=4 already gives negligible theta tail; no infinite integral inference from fit.
    _,G=columns(mp.exp(8),0,256)
    _,Glo=columns(mp.exp(8),0,192)
    return G,mp.norm(G-Glo)

def score(cut,N,Q,B,Gfull,proxy=None):
    norms=[mp.sqrt(realdot(B[:,j],B[:,j])) for j in range(4)]
    S=mp.matrix(B)
    for j in range(4):
        for i in range(S.rows): S[i,j]/=norms[j]
    G=S.T*S; M=S.T*Q*S
    evals,U=mp.eigsy(Q)
    e0=evals[0]; gap=evals[1]-e0; ground=U[:,0]
    normsQ=mp.norm(Q)
    assert gap>mp.mpf('1e-85')*normsQ, "increase precision for full gap"
    bproxy=None
    if proxy:
        bproxy=mp.matrix([mp.mpc(str(z[0]),str(z[1])) for z in proxy['coefficients']])
        bproxy/=mp.sqrt(mp.re((bproxy.H*bproxy)[0]))
    trials=[]
    for j in range(4):
        R=M[j,j]
        trials.append({'derivative_order':2*j,'R':val(R),'excess':val(R-e0),
          'excess_over_gap':val((R-e0)/gap),
          'ground_overlap_squared':val(realdot(ground,S[:,j])**2)})
    restricted=[]
    for m in (1,2,3):
        Gm=G[:m+1,:m+1]; Mm=M[:m+1,:m+1]
        L=mp.cholesky(Gm); Li=L**-1
        H=Li*Mm*Li.T
        mu,V=mp.eigsy(H)
        C=Li.T*V
        c=C[:,0]; direction=S[:,:m+1]*c
        if realdot(direction,S[:,0])<0: c=-c; direction=-direction
        # Physical global coefficients in UNNORMALIZED derivative basis.
        alpha=mp.matrix([c[j]/norms[j] for j in range(m+1)])
        Hglobal=Gfull[:m+1,:m+1]
        gn=mp.sqrt(realdot(alpha,Hglobal*alpha))
        alpha/=gn
        alpha4=mp.matrix(list(alpha)+[mp.mpf(0)]*(3-m))
        kk=mp.matrix([1,0,0,0]); kk/=mp.sqrt(Gfull[0,0])
        eigres=mp.norm(Mm*C-Gm*C*mp.diag(mu))
        grameigs=mp.eigsy(Gm,eigvals_only=True)
        overlap=realdot(ground,direction)**2
        # Fraction of true ground seen by the full realized radical subspace.
        rhs=S[:,:m+1].T*ground
        sub_overlap=realdot(rhs,(Gm**-1)*rhs)
        record={'m':m,'eigenvalues':[val(x) for x in mu],
          'restricted_gap':val(mu[1]-mu[0]),
          'selected_column_coefficients':[val(x) for x in c],
          'selected_global_derivative_coefficients':[val(x) for x in alpha4],
          'selected_global_k_overlap_squared':val(realdot(alpha4,Gfull*kk)**2),
          'selected_finite_k_overlap_squared':val(realdot(direction,S[:,0])**2),
          'selected_ground_overlap_squared':val(overlap),
          'ground_projection_into_radical_subspace_squared':val(sub_overlap),
          'selected_excess_over_full_gap':val((mu[0]-e0)/gap),
          'gram_condition':val(grameigs[-1]/grameigs[0]),
          'generalized_residual':val(eigres)}
        if bproxy is not None:
            record['selected_projected_prolate_overlap_squared']=val(abs((bproxy.H*direction)[0])**2)
        restricted.append(record)
    return {'cut':cut,'lambda':val(mp.sqrt(cut)),'a':val(mp.log(cut)/2),'N':N,
      'full_e0':val(e0),'full_gap':val(gap),'Q_norm':val(normsQ),
      'M_normalized_columns':serialize(M),'G_normalized_columns':serialize(G),
      'projection_column_norms':[val(n) for n in norms],'trials':trials,
      'restricted':restricted,
      'ground_coefficients':[val(x) for x in ground],
      'full_eigen_residual':val(mp.norm(Q*U-U*mp.diag(evals)))}

def main():
    cuts=(9,25,49,81,121,169)
    proxyfile=OUT/'prolate_trials.json'
    proxydata=json.loads(proxyfile.read_text()) if proxyfile.exists() else []
    proxyidx={(c['cut'],c['N']):c for c in proxydata}
    Gfull,global_gram_change=global_gram(); records=[]
    for cut in cuts:
        a=math.log(cut)/2
        paths={'quadratic':max(4,math.ceil(a*a)), 'cubic':max(4,math.ceil(a*a*a))}
        maxN=max(paths.values())
        balls,_,_=build(cut,maxN,448)
        Qmax=mp.matrix([[midpoint(x) for x in row] for row in balls])
        Bhi,normshi=columns(cut,maxN,192)
        Blo,normslo=columns(cut,maxN,144)
        coefferr=mp.norm(Bhi-Blo)
        for N in sorted(set(paths.values())):
            sl=slice(maxN-N,maxN+N+1)
            Q=Qmax[sl,sl]; B=Bhi[sl,:]
            rec=score(cut,N,Q,B,Gfull,proxyidx.get((cut,N)))
            rec['paths']=[name for name,value in paths.items() if value==N]
            rec['quadrature_column_change_144_to_192']=val(coefferr)
            rec['quadrature_unprojected_gram_change']=val(mp.norm(normshi-normslo))
            records.append(rec)
            print(cut,N,'e0',mp.nstr(mp.mpf(rec['full_e0']),8),
              'split',[(r['m'],mp.nstr(mp.mpf(r['eigenvalues'][0]),7),
                 mp.nstr(mp.mpf(r['selected_global_k_overlap_squared']),7),
                 mp.nstr(mp.mpf(r['selected_ground_overlap_squared']),7)) for r in rec['restricted']],flush=True)
            result={'rh_status':'OPEN','kind':'HIGH_PRECISION_DIAGNOSTIC_NOT_CERTIFICATE',
              'precision_digits':mp.mp.dps,'Arb_matrix_bits':448,
              'paths':'N=max(4,ceil(a^2)) and N=max(4,ceil(a^3)), a=log(lambda)',
              'global_gram_derivatives':serialize(Gfull),
              'global_gram_scope':'Numerical integration on [-4,4], theta tails omitted below working precision, not a rigorous enclosure of the full-line Gram.',
              'global_gram_quadrature_change_192_to_256':val(global_gram_change),
              'cases':records,
              'scope':'Finite m<=3, finite path prefixes only. Arb midpoints, non-interval eigenanalysis and quadrature. No asymptotic rate, limit, RH, or path dependence inferred.'}
            (OUT/'splitting_results.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
