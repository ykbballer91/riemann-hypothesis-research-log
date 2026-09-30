**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/notes/phase3_structural_tests.md` · Original SHA-256: `120d5956fd768a0e35588139fc91c1f9bc18e80390e81eba7bb1543397317a17`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase III — 三つの限定された構成・破壊試験

2026-09-29。RHはOPEN。ここで反証するのは移植候補の一般則であって、実際のζ、
有限体上の曲線、Connes–ConsaniやDeningerの研究全体ではない。
内部で構成した後に既知性を照合した。新規性を主張しない。

## M1. 正の閉点数とFrobenius双対性だけでpurityを導けるか

候補命題：整数閉点数、有限次元graded trace、rational determinant、
weight 1の双対性がそろえば、H¹の全固有値の絶対値は√q。
この命題は偽。次の模型は幾何的cohomologyと称していない。

q=9、H⁰=Q、H¹=Q²、H²=Qとし、

    F₀=1, F₁=[[0,-9],[1,7]], F₂=9,
    Z(T)=(1-7T+9T²)/((1-T)(1-9T)).

α±=(7±√13)/2、S₀=2,S₁=7,Sₙ=7Sₙ₋₁−9Sₙ₋₂とすれば
Nₙ=9ⁿ+1−Sₙ=Σᵢ(−1)ⁱTr(Fᵢⁿ)。
α₊α₋=9、1<α₋<2<3<α₊<6<9。
Z(1/(9T))=Z(T)も成立する。
Z(9^(−s))の零点の実部はlog₉α±であり、約0.759244と0.240756。
いずれも0と1の間だが1/2ではない。

閉点数bₙ=(1/n)Σ_{d|n}μ(d)N_{n/d}は全nで正整数。
整数性：Z∈1+TZ[[T]]を次数順に一意なEuler積
Πₙ(1−Tⁿ)^(−bₙ)に分解する係数帰納からbₙ∈Z。
対数微分から上記Möbius式と一致する。
正性：b₁=3。n≥2ではNₘ≤9ᵐ+1かつNₘ>0を用い、

    nbₙ ≥ Nₙ − Σ_{m|n,m<n}Nₘ
         > 9ⁿ − 6ⁿ − 2ⁿ − Σ_{m=1}^{⌊n/2⌋}(9ᵐ+1) > 0.

最後の引く項を9ⁿで割った上界は
(2/3)ⁿ+(2/9)ⁿ+(9/8)9^(−n/2)+(n/2)9^(−n)。
各項は整数n≥2で減少し、n=2で409/648<1。
各nにつきbₙ個のn-cycleを取る置換集合を作れば、#Fix(Fⁿ)=Nₙまで実現できる。
これはfinite-type schemeの構成ではない。反証対象の公理にschemeを含めていない。

J=[[0,1],[-1,0]]に対しF₁ᵀJF₁=9J。
さらにH=[[2,7],[7,18]]にもF₁ᵀHF₁=9Hが成立するがdet H=−13。
したがって対称なscaled-invariant formの存在を足しても不足。
形式的adjoint A†=J⁻¹AᵀJについてF₁†F₁=9Iだが、
A=diag(1,−1)でTr(A†A)=−2。この†を幾何的な正のRosati involutionとは呼ばない。

追加公理候補：同じFに対し正定値Hermitian Mが存在しF*M F=qM。
これを加えれば固有vector vの評価から|α|²=qで、合成模型は排除される。
ただしこれは有限次元では「Fがsemisimpleで全|α|=√q」と同値：
逆向きは固有基底を正規直交とするMを作ればよい。
固有値の絶対値だけからは逆は成り立たない（Jordan blockが反例）。
幾何的polarizationの存在やfunctorialityまで逆向きに得られるわけではない。
古典的零点へ同定済みの作用に同じ正性を仮定しても、独立な算術的証明にはならない。

**Decision:** formal trace/duality ⇒ purity を棄却。
正の幾何的polarizationがどこで働くかは明確になったが、それを仮定として移植しない。
有限体の曲線ではJacobian上の既知のRosati正性がこの役目を独立に果たす。
数値検査は補助。全nについての主張は上記解析証明による。

## M2. 周囲のunitarityを算術商へ自動的に移せるか

候補命題：EがunitaryなHilbert表現に稠密に入り、Eの自然な強い位相でNが閉かつ
全作用に不変なら、E/Nにもスペクトルを失わずunitaryな商normが入る。
これも偽。位相と商の順序を取り違えている。

E=C_c^∞(R)に通常のLF位相を入れ、a>0、
ℓₐ(f)=∫f(x)e^(ax)dx、Nₐ=ker ℓₐとする。
Tₜf(x)=f(x−t)はL²(R)上でunitaryだが、
ℓₐ(Tₜf)=e^(at)ℓₐ(f)。従ってE/Nₐ≅Cは非unitaryなcharacter e^(at)を持つ。
NₐはLF位相で閉で、TₜとT₋ₜの両方に不変である。

一方、c=ℓₐ(g)≠0となるg∈Eを固定し、
g_R=e^(−aR)g(·−R)/cとするとℓₐ(g_R)=1、||g_R||₂→0。
任意のfに対してf−ℓₐ(f)g_R∈NₐかつL²でfへ収束する。
よってNₐはL²稠密。Hilbert閉包による商は0になり、元の商のmodeを消す。

一般に、正形式Bをそのまま代表元非依存に商へ下ろすにはN⊂rad Bが必要。
正定値BならN=0しかない。別の商norm inf_{n∈N}||f+n||は作れるが、
それが非零で、元の算術商の位相・作用・trace・重複度を保つかは別定理である。
Hilbert閉部分空間が全unitary群で不変なら商もunitary、という正しい定理は否定しない。

この反例は実際のConnes–Consani–Marcolli cokernelが同じ稠密性を持つという主張ではない。
既知の算術商ではtest-spaceの選択とrange closureに意味があり、それを任意のL²商へ
置換するだけでは全零点同定を保てない、という移植候補の一般則を止める。

### actual arithmeticでの、特定の自然normに対する障害

さらに原典 [CCM07 Proposition 6.4(2), (6.12)](https://arxiv.org/pdf/math/0703392v1)
には独立した算術的事実がある。restrictionの像Vの元をfへ加えることで、

    ||f+v||²_ar = ∫_{C_K}|f(u)+v(u)|² |u| d×u < ε

を任意のε>0に対して実現できる。同Prop.(1)ではVはtrace pairingのradicalに入る。
したがってこのnormのHilbert閉包で商を作ると、全classの商seminormが0になる。
これは全指数重みのSchwartz topologyでの商が非零であることと矛盾しない。
この一つの自然Hilbert normについては、generic模型をactual arithmeticへ無断転用せず、
原著の命題を使って同じ障害を確認できる。

||T_af||²_ar=a||f||²_arなのでa^(−1/2)T_aはこの周囲の空間でunitary。
しかしそのunitarityをHilbert商へ下ろすだけなら商は0で、零点を全て失う。
さらにVをradicalに持つ非零trace pairingがこのambient normに連続なら、
稠密性によりそのpairingは0となり矛盾する。従って一様なbounded-comparisonで
当該normから正性を受け渡す案も使えない。別の幾何的偏極やunbounded formは否定しない。
これは既知結果の帰結であって、新しいRH補題ではない。

ζのsectorでも同じ結論を保つ。K=Zhat×、P₀f=∫_K f(ku)dkとすると、
|k|=1からP₀は当該normの収縮射影。v(u)=Σ_{q∈Q×}η(qu)∈Vについて
η₀(x)=∫_Kη(kx)dkはBruhat–Schwartz性とη₀(0)=∫η₀=0を保ち、P₀v∈V₀。
従ってK不変fには||f+P₀v||_ar≤||f+v||_arを使える。
原命題はConnesのδ=0でのsurjectivityを引用している。その全証明を新しく再監査したのではなく、
原命題を既知入力とし、このsector平均化と商normへの帰結を独立に検算した。

**Decision:** ambient positivityの自動descentを棄却。
actual quotient上のtrace positivityを直接要求すると既知のRH同値条件へ戻る。
その形式と独立な正の幾何的構成を結ぶ比較定理は得られていない。

## M3. 各素数の純粋なlocal actionとinfinite placeをそのまま接着できるか

### まずweightの対象を区別する

ζ_Qはtrivial motiveのL-functionで、各pのunramified local representationは一次元、
Frobₚ=1、Euler因子は(1−p^(−s))⁻¹。これは既知のweight 0である。
その局所固有値1を、未知のglobal arithmetic H¹の零点ρと同一視しない。
後者に求めるweight 1は、前者のlocal purityを別の名前で呼んでも得られない。

有限体ではlog N(x)=deg(x)log q。Qでは全log pを一つの整数周期に乗せられない。
もしlog2=mℓ、log3=nℓなら2ⁿ=3ᵐとなり一意分解に反する。
したがって固定qの整数iterateをそのまま移植する案は不可能。
正の実数flowはこの障害を取り除くが、スペクトルのweightを定めない。

### prime orbitのexactな局所構成

Tₚ=log p、Cₚ=R/TₚZ上のtranslationを取る。Fourier modeは2πk/Tₚ。
Poisson公式による局所distribution traceは

    Σ_{k∈Z} exp(2πikt/Tₚ) = Tₚ Σ_{m∈Z}δ(t−mTₚ).

h∈C_c^∞((0,∞))ならΣₚΣ_{m≥1}log p h(m log p)は局所有限であり、
explicit formulaの正時間prime-power部分をexactに得る。
Euler積のlogもRe(s)>1で
ΣₚΣ_{m≥1}p^(−ms)/mに一致する。ここまではRH不要。

しかしH=⊕ₚL²(Cₚ)には零Fourier modeが無限個あり、生成子はcompact resolventを持たない。
定数modeを全て除去しても第一周波数2π/log p→0で、compact resolventは回復しない。
∫h(t)Uₜdtは∫h≠0なら定数mode上に同じ非零固有値を無限個持つのでtrace classでない。
定数mode除去後もその固有値に近づく無限列があり、同じ結論。
定数modeを含む元のcircle tracesの正時間分布和は存在するが、Hilbert直和上のordinary traceではない。
各orbit内のFourier和に必要なcancelationを、無条件のtrace class性へ格上げできない。
定数modeを除去した後は各局所traceから∫hが引かれるので、∫h≠0ならその素数和も発散する。

全orbitのEuler積は解析接続によりζに一致する。しかし、この一致だけから、
上のHilbert直和に自然なglobal regularized determinantがあり、その零点がglobal H¹の
固有値だとは言えない。局所mode、分布的trace、解析接続後のglobal零点の階層が違う。

### archimedean factorのexactな局所構成

Γ_R(s)=π^(−s/2)Γ(s/2)。標準tower e_n,n≥0にΘ∞e_n=−2ne_nを置く。
これは非自明零点を入力しないlocal factorの模型である。全global cohomologyの定義ではない。
Re(s)>0で、(s−Θ∞)/(2π)のspectral zetaは
π^w ζ_H(w,s/2)。ζ_H(0,a)=1/2−aと
ζ_H′(0,a)=logΓ(a)−(1/2)log(2π)から

    det_ζ((s−Θ∞)/(2π)) = √2 π^(s/2)/Γ(s/2) = √2/Γ_R(s).

√2はこのregularization規約から決まり、自由なcountertermではない。
これは既知のlocal determinantの計算。Hodge/Rees構成についてはDeninger監査を参照。
Γ_Rの極0,−2,−4,…とζの自明零点の相殺、完成関数の極0,1、
ξ=s(s−1)Γ_Rζ/2の全体を一つのgraded determinantとして実現するには、
global complex、degree間の接着、trace/determinantの整合性がさらに必要。
local towerだけでは非自明零点を制御しない。

**Decision:** local weight 0 + exact Γ factor ⇒ global weight 1、という直和接着を棄却。
実際のlocal factorsは保持したが、positive global H¹とactual determinantの同時実現に失敗。
全ての非自明な接着を不可能と証明したわけではない。

## 統合判定

M1は正のpolarizationの必要箇所、M2は位相・商の比較、M3はlocal/globalの接着を切り分けた。
三回とも既知算術からactual zero quotientの正性を独立に導く段階へ届かない。
同じmissing positivityを「Frobenius」「weight」「cohomological gluing」と呼び替えて再試行しない。
全て主RHグラフへの合流なし。追加仮定なし。一般的なcohomology programの不可能性も主張しない。

参照：
[Milne, Abelian Varieties, I §14 / II §1](https://www.jmilne.org/math/CourseNotes/AV.pdf)、
[DLMF 25.11.13, 25.11.18](https://dlmf.nist.gov/25.11)、
Connes–Consani–MarcolliとDeningerの原典・正確な適用範囲は隣接の監査ノートに記録。
