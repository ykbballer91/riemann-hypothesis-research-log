**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/phase4_pairing_adversarial.md` · Original SHA-256: `07a0de524c497aa3519b91761c9efef37bf8309c2098ec4e72d5effeb8e9f116`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Phase IV — pairingの反証と独立監査

2026-09-29。対象はPhase IVで列挙した具体的移植命題。RHや外部研究全体の反証ではない。
Phase IIIおよびその主グラフへの書込み・合流はない。

## AD1：稠密なnull subspaceを持つ正形式は可閉なら零

HをHilbert空間、D⊂Hを稠密線形domain、qをD上の非負Hermitian form、
N⊂DをHに稠密な線形空間、q[n]=0 (n∈N)とする。
qがHに関してclosableならq=0。

証明：Cauchy–Schwarzによりq(n,x)=0。x∈Dに対しn_j∈N、n_j→xを取る。
y_j=x−n_j→0、q[y_j−y_k]=0、q[y_j]=q[x]。
closabilityの判定条件からq[x]=0。任意のxについて成立。□

qが既にclosedならform norm=H normなのでD=H。
Hilbert/moduleへ写すR:D→KもNを消し可閉なら、R(x−n_j)=Rxを用いてR=0。
従って非有界なclosed-form representationや可閉なharmonic liftへ変更するだけでは回避できない。

CCM Proposition6.4の指定weighted L²でV₀は稠密なので適用できる。
原pairingがpositiveなら非可閉となる、という条件付き結論であり、positiveではないと証明したのではない。
別のtopologyではこの仮定を外せる。原著の稠密性定理は引用採用で、全証明の再証明ではない。
証明担当DESTROYER、rootが可閉性判定・CS・domainを再計算してPASS。

## AH：Spec Zの幾何的次数を間違えない

D=Σn_p[p]+a∞、div(r)=Σv_p(r)[p]−log|r|∞。
積公式によりdeg div(r)=0、r=Πp^(n_p)で全有限成分を消せる。
従ってCHhat¹(Spec Z)≅R、degree0 quotient=0。
Spec Z上のcodim1×codim1を算術曲面の数値intersectionと同一視する案は成立しない。
GS/Moriwakiの定理を使える別のarithmetic surfaceを指定しても、ζの全零点との比較は別。
BUILDERによる原典照合と内部計算、DESTROYERによるAH1–AH2の式の再計算を通過。

## IF：pole除去でもformal star positivityは出ない

F=[[0,−9],[1,7]]、F†=7I−F、F†F=9I。
R(X)=(X−1)(X−9)(X−3)はdegree/co-degreeの両評価を消すが、
R(F)†R(F)=−243I、trace=−486。
これは形式的point-count modelの反例で、幾何的Rosati正性を備えた曲線ではない。
LITERATUREの導出をrootの有理数matrix計算で独立検算。
actual explicit formulaのmixed termが負という事実も、全Weil formの負性とは区別する。
指定のsupport incrementへ戻る探索は再開しない。

## PF：actual adelic test上のFourier-starの負方向

h∞(x)=(8(πx²)³−30(πx²)²+15πx²)e^(−πx²)、h=h∞⊗Π1_(Z_p)。
Fh=−h、h(0)=∫h=0、||h||²=585/(32√2)。
よってP_F(h,h)=−585/(32√2)<0。
実際のEuler/Γを含むTate integralもZ(h,s)=(2s−1)ξ(s)と一致する。
この多項式はtestのMellin乗数で、別のxi-like targetへ変更したのではない。
原Weil pairingの負方向やRH反例へは読み替えない。

root導出、DESTROYERによる独立Gaussian微分・Fraction moments・Mellin計算がPASS。
追加のmpmath Fourier/Mellin求積は非認証診断で、解析証明の代替ではない。
詳細独立監査：`../../research/phase4/notes/root_star_audit.md`。
加法/乗法Haarとvector-valued H¹ domainの精密化は反映済み。

## GEN：似た作用素式を同値としない

Θ=diag(3/4,1/4)、J=swapは正内積でJΘJ⁻¹=1−Θ*を満たすが線外。
Jを取り除く理由なしにΘ*=1−Θと同一視しない。
literal Θ⁻¹=1−Θは二次多項式Θ²−Θ+I=0を強制し、全ζ零点を表現できない。
Θ*Θ=cIは円周制約であり、垂直線ではない。一般Cには固定modulusの結論もない。

## MULT：正なtrace pairingでも全modeを失い得る

A=C[ε]/(ε^m)、ε♯=−ε、Θ=ρ+ε、Reρ=1/2とする。
B(a,b)=Tr(M_aM_(b♯))=m a₀ overline(b₀)はPSDだがradical=(ε)。
positive quotientは1次元で、m次元のJordan情報を失う。
normの係数mはoperator traceのm重複度にはならない。
actual CCMのlocal moduleがこの形だとの同定を今回は追加していない。
これはその同定を主張するcandidateに対するconditional/synthetic gate。

## 証拠と最終範囲

`research/phase4/experiments/check_pairings.py` はexact Fraction演算でIF/PF/GENを検算。
出力は同directoryの `pairing_checks.json`。script SHA256を結果に記録。
数値診断はcertified=false。照合した原典を形式証明した、という主張はしない。
positive arithmetic geometryの比較定理は得られず、主RHグラフへの合流0。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`research/phase4/experiments/check_pairings.py`](../../../../artifacts/research/phase4/experiments/check_pairings.py)
- [`research/phase4/notes/root_star_audit.md`](../../research/phase4/notes/root_star_audit.md)
