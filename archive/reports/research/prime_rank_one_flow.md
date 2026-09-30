**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/prime_rank_one_flow.md` · Original SHA-256: `233051a64789382f58740dcf1193923713bc3bdba19b4c02deab1b95e4e42229`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Prime-power derivative event と rank-one spectral flow の適用範囲

2026-09-30。RH OPEN。Hierarchical Selection Track B の bounded audit。
既存ファイル・state・graph は変更しない。新規性を主張しない。

**判定：actual repeated prime insertion の closed rank-one flow は得られない。**
一つの derivative event と frozen rank-one model の間には正確な辞書がある。
しかし有限幅の actual new-prime term は既に符号不定で、rank-one ではない。
以下はこの障害を actual form 内で示す。

## B1. 一次資料と使用する範囲

O. Dobosevych–R. Hryniv,
*Direct and Inverse Spectral Problems for Rank-One Perturbations of Self-adjoint Operators*,
Integral Equations and Operator Theory **93**, 18 (2021),
[DOI](https://doi.org/10.1007/s00020-021-02630-y),
[公刊版 PDF・著者所属機関 repository](https://er.ucu.edu.ua/server/api/core/bitstreams/0c546298-2d9f-4d22-af35-48b3fcffc89d/content),
[arXiv:2007.08841](https://arxiv.org/abs/2007.08841)。
今回の頁番号は 18-page 公刊版。

§2 pp.3–5 は \(A\) が self-adjoint、simple discrete spectrum、
uniform separation \(\inf(\lambda_{n+1}-\lambda_n)>0\) を仮定する。
摂動 \(B=A+\langle\cdot,\varphi\rangle\psi\) は一般に self-adjoint とは限らない。
characteristic function は (2.3)–(2.5)。
Theorem 3.1 p.5 は固有値を重複度付きで配置した
\(\sum|\mu_n-\lambda_n|<\infty\)、
Theorem 4.1 p.9 はその条件を満たす指定 spectrum の実現を扱う。
これらの infinite-dimensional main theorems を
current expanding Weil matrix に無条件適用しない。
特に uniform separation と固定 infinite operator の同定は供給されない。
同論文の一般 non-self-adjoint inverse construction を
actual Hermitian update の自由な spectrum 設計に使わない。

以下の finite-matrix resolvent/interlacing は、その characteristic formula の
self-adjoint special case を直接導出する。
Aronszajn–Krein 型という名称で呼ぶが、別の古典原論文を全文再監査したとはしない。

## B2. Frozen model：exact secular equation と resolvent

固定有限 Hermitian 行列 \(A\)、非零 \(v\in\mathbb C^d\)、\(\alpha>0\) に対し
\[
 A_\tau=A-\tau\alpha vv^*,\qquad 0\le\tau\le1,\qquad q=\tau\alpha .
\]
\(z\notin\sigma(A)\) として
\[
 R_0(z)=(A-zI)^{-1},\qquad m_0(z)=v^*R_0(z)v
       =\sum_\ell\frac{\|P_\ell v\|^2}{\lambda_\ell-z}.
\]
ここで \(P_\ell\) は distinct eigenvalue ごとの spectral projector。
determinant lemma と一回の積から
\[
 \det(A_\tau-zI)=\det(A-zI)(1-qm_0(z)),
 \tag{B1}
\]
\[
 R_\tau(z)=R_0(z)+
       \frac{q\,R_0(z)vv^*R_0(z)}{1-qm_0(z)},\qquad
 m_\tau(z)=\frac{m_0(z)}{1-qm_0(z)} .
 \tag{B2}
\]
複素 \(z\) では右辺の最後の \(R_0(z)\) を \(R_0(z)^*\) に変更しない。
secular equation は \(1-qm_0(z)=0\)。
old eigenvalue で分母が極となる場合は determinant 全体の cancellation を扱う。
\(P_\ell v=0\) の old eigenspace は保存され、一般の重複 eigenspace でも
\(v^\perp\) 成分は保存される。secular roots だけで全 multiplicity を数えない。

old spectrum 外の real root \(\mu\) の eigenline は
\[
 \operatorname{span}\{(A-\mu I)^{-1}v\},\qquad
 \|(A-\mu I)^{-1}v\|^2=m_0'(\mu).
 \tag{B3}
\]
\(q>0\)、\(A\) が単純で \(v\) が全 eigendirection に非直交なら、
各 coupled pole 間に一つの root と、最小 pole より下の一つの root がある。
coupling が 0 の場合に strict interlacing を主張しない。

昇順・重複度付き固有値を \(\lambda_0,\ldots,\lambda_{d-1}\)、
\(\mu_0,\ldots,\mu_{d-1}\) とすると、\(q\ge0\) に対し
\[
 \mu_0\le\lambda_0\le\mu_1\le\lambda_1
          \le\cdots\le\mu_{d-1}\le\lambda_{d-1}.
 \tag{B4}
\]
単純 branch の Hellmann–Feynman 公式は
\[
 \mu_j'(\tau)=-\alpha|v^*u_j(\tau)|^2\le0.
 \tag{B5}
\]
gap の微分は二つの overlap の差なので符号は固定されない。
ground が isolated simple、gap \(\Delta_\tau>0\) の区間では
\[
 P_0'=\alpha(Svv^*P_0+P_0vv^*S),\quad
 S=(A_\tau-\mu_0)^{-1}(I-P_0),\quad
 \|P_0'\|\le 2\alpha\|v\|^2/\Delta_\tau .
 \tag{B6}
\]
固有値の interlacing は gap 下界や ground の一定方向への収束を与えない。

## B3. Actual event：一次極限と joint limit の誤差

\(L=2a=2\log\lambda\)、\(h=\log n\)、\(n=p^r\)、
\(c_n=\Lambda(n)/\sqrt n\)。
固定 Fourier index \(|j|\le N\) の基底
\[
 V_{j,L}(t)=L^{-1/2}e^{2\pi ij(t/L+1/2)}
\]
を零延長する。new-prime matrix は \(-c_n(C+C^*)\) で
\[
 C_{j\ell}=\langle\tau_hV_{j,L},V_{\ell,L}\rangle,\qquad
 \tau_hf(t)=f(t-h).
\]
\(L\le h\) で 0。\(L=h+\delta>h\) なら exact に
\[
 C_{j\ell}(L,h)=\frac1L\int_0^\delta
   \exp\left(\frac{2\pi i[j(\delta-u)+\ell u]}L\right)\,du.
 \tag{B7}
\]
従って fixed \(N,h\) で
\[
 -c_n(C+C^*)=
 -\frac{2\Lambda(n)}{\sqrt n\,h}\delta\,{\bf1}{\bf1}^*
 +O_{N,h,n}(\delta^2).
 \tag{B8}
\]
これは前トラックの derivative corner の直接再確認。
\(0<\delta\le h/2,\ d=2N+1\) ならさらに
\[
 \left\|C-\frac{\delta}{h}{\bf1}{\bf1}^*\right\|
 \le C\,d(N+1)\frac{\delta^2}{h^2}.
 \tag{B9}
\]
各 entry の phase difference を
\(|e^{ix}-1|\le|x|\)、\(|j(\delta-u)+\ell u|\le N\delta\) で抑え、
entrywise bound の \(d\) 倍を operator bound とした。
leading matrix norm は \(d\delta/h\) なので、
\((N+1)\delta/h\to0\) は relative rank-one approximation の十分条件。
単に \(\delta\to0\) として \(N\to\infty\) の一様性を得たとは言わない。

critical resolution \(N\asymp aY,\ Y=\pi\lambda^2,\ h\asymp2a\) では、
cutoff の整数差 \(g\) に相当する log 間隔 \(\delta\asymp g/\lambda^2\) に対して
\(N\delta/h\) は一般に 0 へ行かない。
したがって derivative event を次の event までそのまま積分する操作は未正当化。

また actual background \(B(L)\) は Gamma・pole・既存 primes・basis scaling を含む。
event 近傍で
\[
 Q(h+\delta)=B(h)+\delta B'(h)
             -\frac{2c_n}{h}\delta\,{\bf1}{\bf1}^*
             +O_{N,h,n}(\delta^2).
 \tag{B10}
\]
frozen \(A=B(h)\) から rank-one 項だけを動かすと、
同じ一次の \(B'(h)\) を落としてしまう。
(B4)–(B6) はその frozen model に exact、
actual full \(L\)-variation の monotonicity にはならない。

## B4. 有限 event term は actual form 内ですでに符号不定

\(N\ge1,\ h<L<2h\)、従って \(0<\delta=L-h<a=L/2\) とする。
new-prime contribution 単独を
\[
 D_{n,L}(f)=-2c_n\Re\int_{a-\delta}^{a}
                  f(t-h)\overline{f(t)}\,dt
 \tag{B11}
\]
と書く。
constant basis \(f_0(t)=L^{-1/2}\) では積分 \(=\delta/L>0\)、
従って \(D_{n,L}(f_0)<0\)。
一方、同じ current \(E_N\) 内の real odd vector
\(f_1(t)=\sin(\pi t/a)\) では
\[
 f_1(t)>0\quad(a-\delta<t<a),\qquad
 f_1(t-h)<0\quad(-a<t-h<-a+\delta).
\]
ゆえに \(D_{n,L}(f_1)>0\)。
**actual new-prime term はこの範囲で indefinite、従って rank one ではない。**
odd direction の効果が一次で消えることと矛盾せず、
positive contribution はより高い次数から現れる。

これは actual \(Q_W\) 全体の負方向の証明ではない。
Gamma・pole・他 primes を含む全体の sign は別問題。
しかし有限 prime insertion を negative rank-one update とする exact dictionary は、
この二つの actual trial vectors により排除される。

## B5. Boundary rank-one form との exact 接点と非同一性

smooth に動く trial columns \(p_i(L)\in E_N(L)\) を係数行列 \(C_{\rm tr}(L)\) で表す。
基底の両端値が \(L^{-1/2}\) なので
\[
 {\bf1}^*c_i=\sqrt L\,p_i(a).
\]
event \(L=h\) の derivative jump を pull back すると
\[
 C_{\rm tr}^*
 \left(-\frac{2\Lambda(n)}{\sqrt n\,h}{\bf1}{\bf1}^*\right)C_{\rm tr}
 =-\frac{2\Lambda(n)}{\sqrt n}
      \bigl(\overline{p_i(a)}p_j(a)\bigr)_{ij}.
 \tag{B12}
\]
sesquilinear convention を逆にすればこの表示を転置共役する。
smooth trial variation は新項が event 自体で 0 のため jump へ寄与しない。
support-only の even \(f_j\) でも、(B11) の一次展開から同じ endpoint covector
\(A_j=f_j(a)\) が直接現れる。

従って boundary-evaluation covector の共有は exact。
ただし support-only recognition の leading form は正の係数 times \(AA^*\)、
(B12) は負の derivative corner であり、scale・背景・remainder も異なる。
この共有だけでは二つの forms、Schur hierarchy、selectors の同値性にならない。

## B6. Repeated update の閉じ方と止まる箇所

同じ固定 \(A,v\) に negative rank-one updates だけを加える模型なら
\[
 A_r=A-s_rvv^*,\qquad
 m_r(z)=m_0(z)/(1-s_rm_0(z))
 \tag{B13}
\]
と scalar recursion が閉じる。これは既知の代数であり、
actual prime flow を得たという意味ではない。
さらに \(s_r\to\infty\) なら fixed dimension の ground line は \(\operatorname{span}v\) へ行く。
これは leading operator \(-s_rvv^*\) の単純最低固有値から従う。

current basis の \(v={\bf1}\) なら physical vector は endpoint Dirichlet kernel。
それを actual \(k\) と同定する理由はない。
\(N\to\infty\) では \(\|{\bf1}\|^2=2N+1\) が発散し、
同じ \({\bf1}\) を固定 \(\ell^2\) vector として無限 rank-one operator にできない。

異なる \(v_r\) の Sherman–Morrison update 自体は exact でも、
次の scalar \(v_{r+1}^*R_rv_{r+1}\) には cross resolvent data が必要。
current problem ではさらに (B10) の full background drift、
(B11) の higher-rank finite insertion、\(N\)-embedding が残る。
これらを閉じる uniform arithmetic law は今回得られていない。

**Track B 結論。** frozen secular equation・interlacing は使用可能な既知道具。
actual event の uniformity 条件と actual sign-indefinite finite term は
literal rank-one-renormalization 仮説の限定 kill。
新しい canonical attracting line、actual closed recursion、
boundary selection との全体的 exact equivalence は未取得。
state の prime_rank_one_closed_flow_found は false のままが適切である。
