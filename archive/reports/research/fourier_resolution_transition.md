**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/fourier_resolution_transition.md` · Original SHA-256: `ac2b80d86f43521954c2b240db27be7fd082d123ad0d9b08992acae79f568aa9`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Fourier resolution of the arithmetic boundary layer

2026-09-30. RH OPEN. Existing arithmetic form, periodic Fourier projector and
ordinary log-coordinate L² norm are unchanged. The estimates below concern a
fixed finite derivative space, not the ground state of the whole finite matrix.

## F1. Conventions and the factor of two

Write a=log λ, Y=πe^(2a), β=2Y, and R_a=1_[-a,a]. The boundary coordinate in the
previous proof is v=β(t−a). In that coordinate the leading tail is e^(-v).
In the coordinate v=Y(t−a) suggested in the request it is e^(-2v).

The Fourier grid is ω_n=πn/a. Set

\[
 \Omega_N=\pi N/a,\qquad h_N=\Omega_N/\beta,
 \qquad c_N=N/(aY),\quad h_N=\pi c_N/2.
\]

Replacing N by N+1 changes h_N by π/(aβ), which tends to zero. Geometric
boundary resolution is h_N of order one; asymptotic recovery of the unfiltered
boundary requires h_N→∞. This is a different condition from N/a→∞.

The actual conventions for the periodic projector and arithmetic quadratic
form are those of [CCM, §3.1, (3.19)–(3.21)](https://arxiv.org/html/2511.22755v1#S3.SS1),
fixed in the previous [boundary calculation](rate_history/notes/boundary_rate_analysis.md).
No continuous Fourier cutoff is substituted for that projector.

## F2. Exact periodization identity

For an even rapidly decreasing f, define on I_a=[−a,a]

\[
 G_af(t)=\sum_{\ell\in\mathbb Z}f(t+2a\ell),\qquad
 H_af(t)=G_af(t)-f(t)=\sum_{\ell\ne0}f(t+2a\ell).
\]

G_a is an actual periodization, not a new arithmetic relation. H_a is first
defined on I_a and then periodically extended for applying P_N; the expression
G_a(t)−f(t) on the whole real line is not itself periodic. Their derivatives
have different matching behavior at the seam. Let p=P_NR_af,
extended by zero. Then δ=p−f satisfies the exact identities

\[
 \delta|_{I_a}=(I-P_N)H_af-(I-P_N)G_af,
 \qquad \delta|_{I_a^c}=-f.                       \tag{F1}
\]

The coefficients of G_a are the samples of the full transform:
(2a)^(-1)\widehat f(ω_n). For r=(I−R_a)f,
the coefficients of H_a are (2a)^(-1)\widehat r(ω_n).
Thus F1 keeps both the true Fourier/Gamma tail and the periodically folded
support tail. Omitting either term is generally wrong.

## F3. Uniform jet coordinates, not columnwise cancellation

Use the exact Taylor-jet basis from
[the support hierarchy](higher_order_gamma_selection.md). Its members e_{r,Y},
0≤r≤m, are actual linear combinations of k,k'',…,k^(2m). Put

\[
 B_Y=e^{a/2-Y},\quad
 \kappa_Y=2B_Y^2/\beta=\pi^{-1/2}Y^{-1/2}e^{-2Y}.
\]

For a jet vector z∈C^(m+1), set e_{z,Y}=Σz_r e_{r,Y}. Its normalized right tail is

\[
 F_{z,Y}(v)=B_Y^{-1}e_{z,Y}(a+v/\beta)
 \longrightarrow F_z(v)=e^{-v}\sum_{r=0}^m z_r v^r,
 \qquad v\ge0.                                  \tag{F2}
\]

Convergence holds uniformly for |z|≤1 with every fixed finite collection of
polynomially weighted L¹/L² derivative norms. The proof is the exact polynomial
jet construction, followed by Taylor expansion of Ye^(v/Y), splitting at a
small positive power of Y, and the exponential theta bound on the complement.
The n≥2 theta terms remain exponentially small after the polynomially bounded
change of basis. This uniform statement is essential: entrywise asymptotics in
the original ill-scaled derivative basis cannot be used after cancellation.

Write φ_{z,Y}(ξ)=∫_0^∞F_{z,Y}(v)e^(-iξv)dv. Evenness gives the exact grid identity

\[
 \widehat r(\omega_n)
 =\frac{2B_Y}{\beta}(-1)^n\Re\varphi_{z,Y}(\omega_n/\beta)       \tag{F3}
\]

for real z. Complex vectors follow by sesquilinear polarization, not by taking
the real part of a complex linear combination. Equivalently use the cosine
transform Ψ_{z,Y}=∫F_{z,Y}cos(ξv)dv, which is linear in complex z.

Uniformly in the jet unit ball,

\[
 |\Psi_{z,Y}(\xi)|\le C_m(1+|\xi|)^{-2},\qquad
 \int_{h}^{\infty}|\Psi'_{z,Y}(\xi)|d\xi
 \le C_m(1+h)^{-1},\quad h\ge h_0>0.               \tag{F4}
\]

Two integrations by parts prove the first estimate; another integration and
the weighted derivative bounds in F2 prove the second. These estimates control
both the Riemann sums and the physical-space leakage of the sharp projector.

## F4. When the full Fourier tail is negligible

For each original derivative, Stirling and the elementary unconditional
polynomial bound for ζ on Re s=1/2 give

\[
 |\widehat{k^{(2j)}}(\omega)|
 \le C_m(1+|\omega|)^{2m+3}e^{-\pi|\omega|/4}.
\]

The jet-to-original coefficients grow at most polynomially in Y. Consequently,
for any fixed η>0, if

\[
 \boxed{\quad \Omega_N\ge(4/\pi+\eta)Y\quad}       \tag{F5}
\]

then b=(I−P_N)G_a e_{z,Y} is exponentially small relative to B_Y, uniformly in
the jet unit ball, even after any fixed polynomial factor in Y or Ω_N required
below. Indeed its tail begins at e^(-πΩ_N/4), whereas B_Y contains e^(-Y).
The gap in F5 absorbs the polynomial factors, including e^a=√(Y/π).
In particular weighted BV bounds applied to the actual explicit formula show
Q(b,b) and all mixed terms with the F1 boundary error to be
o(aκ_Y)|z|². Zero locations are not used as inputs to the vectors.

F5 is a proved **sufficient separation condition**, not a proved sharp transition.
It says liminf c_N>4/π². At or below that constant this argument does not discard
the full Fourier term. The balancing constant from an upper bound is not thereby
the necessary selection threshold. Regime I and small critical c remain open here.

## F5. Universal boundary form from the actual periodic projector

Let E F(v)=F(|v|) be the even extension to R, and let H_h be the ordinary
Fourier high-pass multiplier 1_(|ξ|>h) used **only to describe the limit**.
For h_N→h∈(2/π,∞), the right-edge error, in scaled coordinates, is

\[
 \mathcal D_hF(v)=
 \begin{cases}
  (H_h E F)(v),&v<0,\\
  -F(v),&v>0.
 \end{cases}                                      \tag{F6}
\]

At the left edge it is reflected. Formula F6 follows from F3 by Riemann sums;
the frequency spacing is π/(aβ)→0. Parseval on the original circle gives a
particularly direct norm proof without identifying pointwise values at the jump:

\[
 \frac{\|\delta\|_2^2}{\kappa_Y}
 \longrightarrow
 J_h(F):=\|F\|_{L^2(0,\infty)}^2
       +\tfrac12\|H_hEF\|_{L^2(\mathbb R)}^2.       \tag{F7}
\]

The first summand is the unchanged exterior error; the second is periodic
projection leakage on the inside. Thus

\[
 \|F\|_2^2\le J_h(F)\le2\|F\|_2^2,
 \qquad J_\infty(F)=\|F\|_2^2.                    \tag{F8}
\]

The same assertions are uniform on the fixed jet unit ball. If h_N→∞, the
second term tends to zero using F4, and F7 holds with J_∞. No boundary fixed
point has been designed; F6 is forced by F1 and the original projector.

For F=e^(-v), the inside profile is

\[
 K_h(v)=\frac2\pi\int_h^\infty\frac{\cos(\xi v)}{1+\xi^2}d\xi,
\quad
 J_h(e^{-v})=1-\frac{\arctan h+h/(1+h^2)}\pi.       \tag{F9}
\]

The support-only norm is 1/2. The corresponding score multiplier is 2J_h,
strictly greater than 1 for finite h and tending to 1 at infinity. This exhibits
a genuine boundary-resolution crossover; it does not identify a sharp threshold
for selection, which is a different question.

## F6. Transfer from profile norms to the actual arithmetic form

This step must not be replaced by ambient positivity. We estimate separately the
Gamma, polar and all prime-power terms of the actual form.

### F6.1 Physical envelope and the arithmetic terms

Abel summation of the F3 coefficients, using F4 and the Dirichlet-kernel geometric
sum, gives for d=(I−P_N)H_a e_{z,Y}, h_N≥h_0>0,

\[
 |d(t)|\le \frac{C_m B_Y|z|}{1+\beta\,\operatorname{dist}(t,\{-a,a\})},
 \quad |t|\le a.                                  \tag{F10}
\]

Near the seam use the absolute coefficient sum; away from it use the partial
sum bound C/|sin(π(t−a)/(2a))| and total variation of the coefficient sequence.
Outside the interval, the tail is bounded by C_mB_Y|z|e^(-cβ(|t|−a)), with
a fixed c>0 after absorbing its fixed-degree polynomial. These bounds are
uniform for h_N≥h_0; the discarded b has the stronger F5 bound.

Convolving the two edge envelopes gives a same-edge bound

\[
 C_m\frac{B_Y^2|z|^2}{\beta}
      \frac{\log(2+\beta d)}{1+\beta d},
\]

and, for 0≤d≤2a, an opposite-edge bound with d replaced by |2a−d|.
For d>2a an exterior exponential factor is necessary; the bound becomes
C_mB_Y²|z|² β^(-1)log(2+aβ)e^(-c'β(d−2a)).

Set X=e^(2a)=Y/π. Summing at d=log n with the actual weights Λ(n)/√n,
using only Λ(n)≤log n, gives

\[
 |Q_{\rm prime}(\delta)|
 \le C_m B_Y^2|z|^2\frac{(\log Y)^3}{Y^{3/2}}
       +o(a\kappa_Y)|z|^2.                         \tag{F11}
\]

For completeness, n≤X/2 has β|log(n/X)|≳Y and contributes at most this bound.
For X/2<n≤X, let r=X−n. Then β|log(n/X)| is comparable to r and
Σ_(0≤r≤X/2) log(2+r)/(1+r)=O((log X)²), uniformly in the fractional part of X.
The additional prime weight is O(log X/√X). For n>X the exterior exponential
restricts the sum to O(1) integer distance from X; the far tail is exponentially
small. Same-edge terms are bounded by Σ_(n≤X)n^(-1/2)=O(√X) after cancellation
of the log n denominator. This covers prime multiplicities and threshold events.

Also ∫e^(|t|/2)|δ(t)|dt≤C_mB_Y|z|e^(a/2)log(2+aβ)/β, hence

\[
 |Q_{\rm pole}(\delta)|
 \le C_m B_Y^2|z|^2(\log Y)^2/Y^{3/2}
       +o(a\kappa_Y)|z|^2.                         \tag{F12}
\]

Both are o(aκ_Y)|z|². An oscillatory sign assumption about primes was not used.

### F6.2 Archimedean logarithm and low frequencies

Let w(ω)=Re ψ(1/4+iω/2)−log π. The needed statement is

\[
 \frac1{2\pi}\int w(\omega)|\widehat\delta(\omega)|^2d\omega
 =\log(\beta/(2\pi))\,\|\delta\|_2^2
     +O_m(B_Y^2/\beta)|z|^2+o(a\kappa_Y)|z|^2.       \tag{F13}
\]

Here are bounds handling the potentially problematic sharp cutoffs. For any
fixed 0<s<1/2 the scaled edge profiles have uniformly bounded H^s norms.
For the high-pass piece this follows from |Ψ(ξ)|≤C/(1+ξ²); cutting its physical
half-line adds a Gagliardo cross integral C_s∫|g(v)|²|v|^(-2s)dv. On |v|≤1
use the uniform sup bound and s<1/2, and on its complement use the L² bound.
The same proof applies to the finite-circle sums by F4 and Parseval, including
the jumps at the two endpoints. Thus the high-frequency logarithmic moment
is O_m(B_Y²/β)|z|², since log(2+|ξ|)≤C_s(1+|ξ|^(2s)).

At low scaled frequencies |ξ|≤h_0/2, the transform of the interior high-pass
piece is uniformly bounded after division by B_Y/β. Indeed integration of
each mode over [−a,a] introduces denominators ω_n−βξ of size at least |ω_n|/2;
F3–F4 then bound the sum by C_m∫_(h_0)^∞|Ψ(η)|/η dη. The outside tail is L¹.
Hence the integrable factor |log|ξ|| causes no loss near zero. The two-edge
phases do not affect these bounds. Finally
|w(βξ)−log(β/(2π))|≤C+|log|ξ||. These estimates prove F13.

These auxiliary Sobolev estimates are estimates on the existing vectors, not
a replacement metric or topology for selecting a state.

### F6.3 Full effective matrix

All e_{z,Y} lie in the global radical, so Q(p)=Q(δ). Since
log(β/(2π))=2a, F7 and F11–F13 prove

\[
 \boxed{
 \frac{Q_W(P_NR_a e_{z,Y})}{2a\kappa_Y}
 \longrightarrow J_h(F_z)
 }                                                  \tag{F14}
\]

uniformly for |z|≤1, when h_N→h>2/π or h_N→∞. By polarization this is matrix
convergence. More generally, if liminf h_N>2/π, whether or not h_N converges,
there are fixed positive constants b_-,b_+ such that, eventually,

\[
 b_-\,2a\kappa_Y|z|^2
 \le Q_W(P_NR_a e_{z,Y})
 \le b_+\,2a\kappa_Y|z|^2.                         \tag{F15}
\]

This is uniform coercivity only on the a-dependent finite jet span. It is not
Weil positivity on all test functions, nor positivity of the whole finite matrix.

## F7. What this implies for the restricted selector

The jet selection lemma in [the hierarchy note](higher_order_gamma_selection.md)
uses precisely F15, together with convergence of the original derivative Gram
and the fixed physical columns P_NR_af_j→f_j in L²(R). Both forms of convergence
hold whenever N/a→∞, in particular in F5, by SH8 of the support proof. Gram
convergence alone would not rule out a common isometric rotation of all columns.
With the actual fixed-column convergence it yields,
for every fixed m≥1,

\[
 \operatorname{span}u_{a,N,m}\to\operatorname{span}k
 \quad\text{in the original }L^2(\mathbb R),        \tag{F16}
\]

for the lowest direction restricted to P_NR_a R_m, along every path satisfying
liminf N/(aY)>4/π². It is simple eventually. Thus the resolved regime
N/(aY)→∞ is included, and so are sufficiently large **finite** critical ratios.
The full matrix ground is not being identified.

For resolved paths F14 reproduces the support-only effective jet matrix.
For finite critical ratios it gives a different positive jet matrix J_h, while
the same physical direction k is selected. Therefore “full selection requires
infinite boundary resolution” is stronger than what the analysis supports.

The regimes N/(aY)→0, 0<c≤4/π², and the exact boundary value c=4/π² are not
settled by this proof. No sharp necessary transition constant is claimed.

## F8. Scope and remaining gap

This is a fixed-m asymptotic statement with original inner product and actual
prime/Gamma/pole formula. No m→∞ limit, full-ground gap, ES condition, normalized
Fourier comparison G*, or RH conclusion follows. The unknown full-ground
coupling from the prior audits remains. A high-resolution restricted result
does not retrospectively turn the earlier under-resolved computations into
counterexamples or confirmations of the new theorem.

## F9. Limited diagnostics, separately from the proof

[Scaled-profile experiment](../../../artifacts/research/hierarchical_selection/experiments/check_scaled_boundary.py)
checks 12 small J_h variational problems, the scalar F9 identity and 20 sampled
Fourier coefficients. The theta-tail diagnostic uses the first theta term and
finite quadrature, and is labeled accordingly; it is not an exact interval enclosure.
For example 2J_h(e^(-v)) is about 1.181690 at h=1, 1.040519 at h=2 and 1.000419 at h=10.

[Actual-cutoff experiment](../../../artifacts/research/hierarchical_selection/experiments/check_actual_resolution.py)
uses the unchanged arithmetic matrix builder at λ=3 and N=4,8,12,20,40.
It diagonalizes only the restricted derivative spans, not the full ground problem.
The coefficient of k'' in the m=1 restricted minimum, normalized to coefficient
1 on k, changes as follows:

|N|h=Ω/(2Y)|coefficient of k''|
|---:|---:|---:|
|4|0.202275|+0.00444311|
|8|0.404551|+0.00153959|
|12|0.606826|−0.000347017|
|20|1.01138|−0.000382056|
|40|2.02275|−0.000378821|

The 192→256-node column-quadrature difference is about 1.57·10^(-95) at
100 working digits. The Q assembly uses 448-bit Arb midpoints; subsequent
arithmetic is not interval-certified. This table diagnoses a substantial change
with resolution at one endpoint. It proves neither a critical constant nor an
asymptotic selector. The preceding theorem is based on F1–F15, not a fit to this table.


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/hierarchical_selection/experiments/check_actual_resolution.py`](../../../artifacts/research/hierarchical_selection/experiments/check_actual_resolution.py)
- [`research/hierarchical_selection/experiments/check_scaled_boundary.py`](../../../artifacts/research/hierarchical_selection/experiments/check_scaled_boundary.py)
- [`research/higher_order_gamma_selection.md`](higher_order_gamma_selection.md)
- [`research/rate_history/notes/boundary_rate_analysis.md`](rate_history/notes/boundary_rate_analysis.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/check_actual_resolution.py` — SOURCE REFERENCE NOT INCLUDED
- `experiments/check_scaled_boundary.py` — SOURCE REFERENCE NOT INCLUDED
