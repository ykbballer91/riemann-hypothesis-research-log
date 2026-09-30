**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/dyadic/notes/explicit_mobius_reduction.md` · Original SHA-256: `55631ad3b5e3095c90e65900aa44c04985008aa91bd136fd9f7488ea134cbac8`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Explicit one-sided arithmetic reduction

2026-09-30. This is a direct calculation in the **unchanged** scalar quotient
specified in `../../one_prime/notes/arithmetic_space.md`. RH is OPEN. No new
topology, spectral encoding, or enlargement of the relation space is used.
The inverse-Euler-operator/cutoff architecture already occurs in Meyer,
[math/0311468v1, §5.3, Lemmas 5.3–5.4](https://arxiv.org/html/math/0311468v1#S5.SS3).
No novelty claim is made for the construction or estimates below.

## 1. Fixed data and the actual representative

Write `S f(x)=2 sum_{m>=1} f(mx)` for even Schwartz functions on R. If
`f(0)=integral_R f=0`, then `J S f(t)=exp(t/2) S f(exp(t))` belongs to the
actual arithmetic range V, hence W. Its finite adelic components are exactly
`product_p 1_{Z_p}`. No Euler factor is removed or altered.

Fix once and for all smooth real functions chi and psi on the positive axis:

- chi=0 on x<=1/2, chi=1 on x>=1, 0<=chi<=1;
- psi is supported in (1/2,1), and integral_0^infinity psi(x) dx=1.

For g in E and a=2^n, n>=0, define

\[
 H(x)=x^{-1/2}g(\log x),\quad H_a(x)=a^{-1/2}H(x/a),
 \quad F_a(x)=\frac12\sum_{m\ge1}\mu(m)H_a(mx).                 \tag{1}
\]

The series and each derivative converge locally absolutely on x>0. Define

\[
 c_a=\int_0^\infty\chi(x)F_a(x)\,dx,\qquad
 f_a(x)=\chi(x)F_a(x)-c_a\psi(x)\quad(x>0),                    \tag{2}
\]

and extend f_a evenly to R. This is a Schwartz function, vanishing near 0,
with integral_R f_a=0. In particular, the correction in (2) enforces the
**existing arithmetic moment condition**. It is not a new counterterm in the
Weil form. Choices of chi and psi are not canonical; the proof and rate are
valid for any one fixed such choice, independent of a, g and zeros.

Set

\[
 w_n(g)=-J S f_a\in V\subseteq W,\qquad
 R_n(g)(t)=\sqrt{x}\bigl(H_a(x)-S f_a(x)\bigr),\quad x=e^t.    \tag{3}
\]

These are explicit linear constructions from g using the usual integer
Möbius coefficients, one cutoff, one integral, and arithmetic summation.
They satisfy

\[
 \boxed{T_2^n g+w_n(g)=R_n(g),\qquad
           \operatorname{supp}R_n(g)\subseteq(-\infty,0].}     \tag{4}
\]

Indeed, for x>=1, chi(mx)=1 and psi(mx)=0 for every m>=1. Absolute
convergence permits the divisor regrouping

\[
 2\sum_{m\ge1}F_a(mx)
 =\sum_{r\ge1}H_a(rx)\sum_{d\mid r}\mu(d)=H_a(x).             \tag{5}
\]

Both sides of (3) lie in E, by the pole-free Poisson formula for f_a. Thus
(4) is an E identity, not merely a pointwise equality. R_n is flat at t=0.
It generally has a noncompact left tail. It does **not** give a representative
in one compact dyadic fundamental interval.

## 2. Unconditional bound: exponent 1 becomes 1/2

Put P=p_4(g). Differentiating H gives, for 0<=j<=4,

\[
 |x^j H^{(j)}(x)|
 \le C_j P\min(x^{7/2},x^{-9/2}).                            \tag{6}
\]

The elementary lattice estimate

\[
 \sum_{m\ge1}\min((mh)^{7/2},(mh)^{-9/2})
 \le C h^{-1}(1+h)^{-7/2}
\]

and |mu(m)|<=1 yield, for j<=3,

\[
 |F_a^{(j)}(x)|\le C P\sqrt a\,x^{-j-1}(1+x/a)^{-7/2}.       \tag{7}
\]

Consequently

\[
 |c_a|\le CP\sqrt a(1+\log a),
 \quad \|f_a''\|_{L^1(\mathbb R)}+
       \|x f_a'''\|_{L^1(\mathbb R)}
       \le CP\sqrt a(1+\log a).                              \tag{8}
\]

For the first inequality, split the integral at a: the interval [1/2,a]
costs at most a logarithm and the tail is integrable by (7). For the second,
all derivatives of chi are in [1/2,1]; away from that interval integrate
x^{-3} in the f_a'' and x f_a''' terms. The fixed psi contribution is
bounded by |c_a|. All constants depend only on the fixed cutoffs and the
seminorm convention, not on a or g.

With Fourier convention exp(-2 pi i x xi), Poisson for pole-free even f is

\[
 S f(x)=x^{-1}S\widehat f(x^{-1}),\qquad
 |S f(x)|\le\frac{x}{12}\|f''\|_1.                          \tag{9}
\]

Here 2 zeta(2)/(2 pi)^2=1/12. Let D=x d/dx. Df is also even and pole-free,
since integral Df=-integral f=0, and

\[
 (Df)''=2f''+xf''',\quad
 \partial_t(J S f)=J S\bigl(\tfrac12 f+Df\bigr).             \tag{10}
\]

Applying (9) to f and (1/2)f+Df gives, for 0<x<=1,

\[
 |J S f|+|\partial_t J S f|
 \le Cx^{3/2}(\|f''\|_1+\|xf'''\|_1).                      \tag{11}
\]

The p_1 weight on this half-axis is x^{-1}(1-log x), and
sup_{0<x<=1} x^{1/2}(1-log x)<infinity. The unreduced term obeys
the one-sided bound p_1(T_2^n g; t<=0)<=C a^{-4}p_4(g).
Together with the exact vanishing for t>=0, this proves

\[
 \boxed{p_1(R_n(g))\le C\,2^{n/2}(1+n)\,p_4(g).}             \tag{12}
\]

Taking the infimum over all representatives g of a class, after applying
this explicit construction to each representative, gives

\[
 q_1(T_2^n[g])\le C\,2^{n/2}(1+n)q_4([g]).                  \tag{13}
\]

No assumption that R_n descends as an E-valued map on the quotient is
needed: (4) proves the class identity for every input representative.
This is an inter-seminorm estimate, **not** a bound on the q_1 Banach
operator norm and not a proof that its full spectral radius is sqrt(2).
The exponent 1/2 is an achieved upper bound, not a proved optimal rate.

This reaches the task's Stage B / Level 3 literally. Spectrally it only
implies Re rho<=1, which is already known. It is not new zero-location
information or progress to RH. The full integer Möbius function, hence all
primes, enters (1); only the *return action* is dyadic.

## 3. Exactly what stronger arithmetic cancellation would buy

Assume, **conditionally**, for a fixed 0<theta<1,

\[
 |M(X)|=\left|\sum_{m\le X}\mu(m)\right|\le K_\theta X^\theta
 \quad(X\ge1).                                             \tag{14}
\]

Summation by parts, applied also to K_j(y)=y^j H^{(j)}(y), gives

\[
 |F_a^{(j)}(x)|
 \le C_\theta K_\theta p_4(g)
        a^{\theta-1/2}x^{-j-\theta}\quad(0\le j\le3).         \tag{15}
\]

For example, the relevant integral is
integral_0^infinity y^theta |K_j'(y)|dy, finite by (6) and p_4.
F_a is integrable at 0 by theta<1 and rapidly decreasing at infinity.
Its Mellin transform is, initially for Re s>1,

\[
 \mathcal M F_a(s)=\frac{\mathcal M H_a(s)}{2\zeta(s)}.       \tag{16}
\]

Taking real s down to 1 is justified by dominated convergence on the left;
on the right, zeta has its known simple pole. Thus integral F_a=0.
This step does not presuppose a zero-free half-plane. Therefore

\[
 c_a=-\int_0^\infty(1-\chi)F_a,
 \quad |c_a|\le
 C_\theta K_\theta p_4(g)a^{\theta-1/2}/(1-\theta).           \tag{17}
\]

Equations (15), (17) and the same Poisson estimates prove for the **same**
explicit representatives (1)–(3)

\[
 \boxed{p_1(R_n(g))\le
 C_\theta K_\theta,2^{n(\theta-1/2)}p_4(g).}                \tag{18}
\]

The mean cancellation in (17) is essential. Estimating integral|F_a| on
[1/2,infinity) would discard it and could retain an a^{1/2} cost.
Moment cancellation cannot simply be inferred from local estimates.

The classical condition M(X)=O_epsilon(X^{1/2+epsilon}) for every epsilon>0
is equivalent to RH; see [Báez-Duarte math/0202141v2, §2.1](https://arxiv.org/html/math/0202141v2#S2.SS1)
and [Soundararajan 0705.0723v2, introduction Eq.(1)](https://arxiv.org/pdf/0705.0723v2).
In particular RH implies (14) with every
theta in (1/2,1), which would prove the desired subexponential estimate by
(18). Conversely that estimate for these representatives implies RH by
the nonzero zero evaluations and reflection. Consequently the following
endpoint assertion about this **fixed, zero-independent algorithm** is
RH-equivalent:

\[
 \forall\epsilon>0\ \exists C_\epsilon:
 p_1(R_n(g))\le C_\epsilon2^{\epsilon n}p_4(g)
 \quad(g\in E,n\ge0).                                      \tag{19}
\]

For epsilon>=1/2, (19) under RH follows by choosing any smaller positive
epsilon first. Equation (19) is rejected as an independent bridge. We have
not proved that every possible reduction algorithm must pass through
Mertens estimates, or that arithmetic relations cannot give a better
estimate by a different method.

## 4. Arithmetic fidelity

Every w_n is produced by the genuine test function
eta_n=f_a tensor product_p 1_{Z_p}. The value and integral constraints
hold exactly. Compact-unit averaging fixes this eta_n already. The
archimedean Schwartz function, its Fourier transform, and both pole
conditions are in the construction from the start. This preserves the
actual W and all its Mellin zero evaluations/jets. No zero ordinate or
real part is used in chi, psi, f_a, c_a or w_n. No topology is weakened.
The archimedean local factor is not replaced by an artificial Gamma factor.

**Decision:** retain the unconditional identity and rate (12) as a
constructive bound in the fixed quotient. Stop the subexponential endpoint
route after identifying (19) as RH-equivalent; it is not an independently
proved arithmetic cancellation principle.
