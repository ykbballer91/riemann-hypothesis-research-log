# STATUS: RIEMANN HYPOTHESIS OPEN
# Sanitized historical research code; not rerun during this export.
# Public credit: @ykbballer91; AI-assisted; SPDX-License-Identifier: MIT
# Source: literature/build_ledger.py
# Original SHA-256: 74e6feca00ac6a11dfb4ee63b92a58e9d26ce8f0111a894ec53af116b4892e0c
# Use artifacts/replay.py for an isolated reconstructed source layout.
"""Generate the ledger and BibTeX from explicit, reviewed metadata."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=[]
def add(i,title,authors,year,url,claim,theorem,assumptions,rh='NO',peer='PREPRINT',notes='',verified='NO'):
 rows.append(dict(id=i,title=title,authors=authors,year=year,url=url,claim_used=claim,exact_theorem=theorem,assumptions=assumptions,depends_on_RH=rh,peer_reviewed=peer,verified_independently=verified,notes=notes))
add('CMI','Riemann Hypothesis: official problem page','Clay Mathematics Institute',2026,'https://www.claymath.org/millennium/riemann-hypothesis/','RHの公式な未解決状態と定義','Unsolved / Riemann Hypothesis','非自明零点。数値確認は定義を置き換えない',peer='NO',notes='2026-09-29閲覧。研究論文ではない。')
add('RVM2022','Counting zeros of the Riemann zeta function','Elchin Hasanalizade and Quanli Shen and Peng-Jie Wong',2022,'https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf','零点計数 O(T log(T+2))','Sections 1–2, N_Q(T); 最適数値定数は使用しない','全非自明零点を重複度込みで数える',peer='YES',notes='J. Number Theory 235, 219–241; DOI 10.1016/j.jnt.2021.06.032。BUILDERが原文照合。')
add('Weil1952','Sur les formules explicites de la theorie des nombres premiers','Andre Weil',1952,'https://cds.cern.ch/record/471308','Weil判定法の原典追跡','原版の定理番号未照合。現代C_c∞版はSuzuki2023で照合','原典のテスト空間は逐条未確認',peer='NO',notes='Lund supplement pp.252–265。書誌確認のみ。定理細部の根拠に単独使用しない。')
add('Suzuki2023','Aspects of the screw function corresponding to the Riemann zeta function','Masatoshi Suzuki',2023,'https://arxiv.org/pdf/2206.03682v4','Weil基準の正確なC_c∞版','Section 3.2, equations (3.3)–(3.5)','全complex compactly supported smooth test functions; multiplicities','NO','YES','J. Lond. Math. Soc. 108, 1448–1487。PDF版はVersion of May 31, 2023（arXivヘッダ30 May 2023）。HTMLの2026本文Dateは参照せず版固定PDFを採用。')
add('Suzuki2025','On the Hilbert space derived from the Weil distribution','Masatoshi Suzuki',2025,'https://doi.org/10.4153/S0008414X25101739','定義とWeil判定法の規約照合','Section 1 (1.1),(1.2); Section 3.1 (3.3)','定義は無条件。Theorem 1.1のHilbert空間同型はRH仮定','NO','YES','RHを仮定するTheorem 1.1を無条件依存に採用しない。')
add('Li1997','The positivity of a sequence of numbers and the Riemann hypothesis','Xian-Jin Li',1997,'https://doi.org/10.1006/jnth.1997.2137','Li criterionのルート比較','λ_n≥0 for every nとRHの同値。全文の定理番号未照合','ξから定義された全係数。有限個の計算は不足','NO','YES','出版社abstract照合のみ。主証明依存に採用しない。')
add('BaezDuarte2002','A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis','Luis Baez-Duarte',2002,'https://arxiv.org/pdf/math/0202141v2','離散化されたL²近似基準','Theorem 1.1: χ_(0,1)∈closure span{fractional_part(1/(ax)): a∈N} iff RH','H=L²(0,∞); closure in its norm','NO','PREPRINT','原稿v2本文確認。自然Möbius部分和のa.e.収束とH収束を区別。')
add('ConreyLi1998','A note on some positivity conditions related to zeta- and L-functions','J. Brian Conrey and Xian-Jin Li',1998,'https://arxiv.org/pdf/math/9812166v1','de Branges正値条件の障害調査','本文の条件と適用例を調査用に確認。今回その定理を使用しない','特定のHilbert空間の正値条件。全de Branges手法の不可能性とは異なる','NO','PREPRINT','arXiv版を固定。出版版メタデータの再確認は保留。')
add('Connes1998','Trace formula in noncommutative geometry and the zeros of the Riemann zeta function','Alain Connes',1998,'https://arxiv.org/abs/math/9811068v1','Hilbert–Pólya / trace formulaのルート比較','abstractのspectral interpretationとtrace formulaへのreduction','全trace formulaの成立を未証明条件として残す','NO','PREPRINT','本文88頁の全面監査なし。推論の依存に採用しない。')
add('PRZZ2018','More than five-twelfths of the zeros of zeta are on the critical line','Kyle Pratt and Nicolas Robles and Alexandru Zaharescu and Dirk Zeindler',2018,'https://arxiv.org/abs/1802.10521','mollifier経路の過去の到達点','要旨の無条件割合改善。全文定理番号未照合','全零点を重複度込みで数えた漸近割合','NO','PREPRINT','最新記録という主張はしない。')
add('GuthMaynard2024','New large value estimates for Dirichlet polynomials','Larry Guth and James Maynard',2024,'https://arxiv.org/abs/2405.20552','zero-density経路の進展','要旨: N(σ,T)≤T^(30(1−σ)/13+o(1))。精密σ域は未監査','主定理を使用しないため、未確認の一様域は主張しない','NO','PREPRINT','原稿要旨確認。2026出版情報は今回依存に不要。零点ゼロ個は従わない。')
add('Lamzouri2026','A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line','Youness Lamzouri',2026,'https://arxiv.org/html/2609.02882v1','核最適化問題の出所と限定的barrier','Theorem 1.1; Proposition 2.1; Lemma 3.2; Remark 3.4','Theorem 1.1は無条件の主張。核側はη real even, smooth, support(-1/2,1/2), ∫η²=1','NO','PREPRINT','解析数論部分全体は独立未検証。kernel最適化だけを別途初等証明。')
add('Wang2026','Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals','Biao Wang',2026,'https://arxiv.org/html/2609.07918v1','2026-09 の新着結果を把握','Theorem 1.1, equations (1.7),(1.8)','fixed 0<θ<1, H=T^θ; liminf割合','NO','PREPRINT','原文の主張を確認。独立検証未済で主定理の依存にはしない。')
add('Deligne1974','La conjecture de Weil I','Pierre Deligne',1974,'https://numdam.org/articles/10.1007/BF02684373/','有限体上のRHとの類推範囲','有限体上の幾何学的Weil予想。本文定理番号は本探索で未照合','有限体上の対象。数体のζへの対応構成を含まない','NO','YES','Publ. Math. IHES 43, 273–307。今回ζへの推論に使用しない。')
add('Montgomery1973','The pair correlation of zeros of the zeta function','H. L. Montgomery',1973,'https://www-personal.umich.edu/~hlm/paircor1.pdf','random matrix関連と仮定検査','Section I, Theorem / opening sentence','RHを論文全体で仮定','YES','YES','Proc. Sympos. Pure Math. 24,181–193。最近の無条件版と混同しない。')
add('CarrilloEtAl2019','Nonlinear aggregation-diffusion equations: radial symmetry and long time asymptotics','J. A. Carrillo and S. Hittmeir and B. Volzone and Y. Yao',2019,'https://doi.org/10.1007/s00222-019-00898-x','全実線密度エネルギーの先行研究照合','Section 3, Theorems 3.7 and 3.10','d=1,m=2,M=1,W=2(|x|−1)へ特殊化。有限一次moment。核条件はノートで照合','NO','YES','汎関数は今回のE−1と一致。cosineは既存Euler–Lagrangeから導出できる。原文に同定数が印刷されるとまでは主張しない。')
add('Tschukin2017','Concepts of modeling surface energy anisotropy in phase-field approaches','Tschukin and Silberzahn and Selzer and Amos and Schneider and Nestler',2017,'https://doi.org/10.1186/s40517-017-0077-9','CDFエネルギーと既知sine profileの照合','Isotropic phase-field model, equations (6) and (7)','double-obstacle potential, ε=2√2/π, γ=π/(2√2), φ=Fに特殊化','NO','YES','既知のprofileとの一致。CDF平方剰余の最古の原典としては指定しない。')
add('DLMF59','DLMF 5.9 Integral Representations','NIST Digital Library of Mathematical Functions',2026,'https://dlmf.nist.gov/5.9#E16','独立有限行列のarchimedean積分とdigammaの規約','5.9.16; 5.7.6との部分分数照合','Re(z)>0でのdigamma積分。区間L>0と整数frequencyに特殊化','NO','OFFICIAL_REFERENCE','groskin-computation.mdの解析導出で使用。DLMFの全章を独立再証明したという意味ではない。')
add('PythonFlint09','acb: complex numbers, python-flint 0.9.0 documentation','python-flint developers',2026,'https://python-flint.readthedocs.io/en/latest/acb.html#acb.integral','Arb認証求積のanalytic flagと返却ballの仕様','acb.integral; acb.sinc; digamma/polygamma API','meromorphic integrandは極を含む場合nonfinite ball。有限返却ballを区間LDLへ渡す','NO','OFFICIAL_DOCUMENTATION','原著のpython-flint0.8.0と今回0.9.0を区別。小例独立再現で実使用。ライブラリ内部の形式検証は未実施。')
add('DLMF1054','DLMF 10.54 Spherical Bessel Integral Representations','NIST Digital Library of Mathematical Functions',2026,'https://dlmf.nist.gov/10.54','Legendre Fourier規格化と無限tailの上界','10.54.1 and 10.54.2; power series 10.53.1','nは非負整数。complex引数にはPoisson表示、実引数には絶対値1のcosを使用','NO','OFFICIAL_REFERENCE','固定窓の独立certificateで使用。tailのn!・double factorial・Fourier位相を別途監査。')
extra=json.loads((ROOT/'literature/notes/weil-sources.json').read_text())['sources']
for s in extra:
 peer='YES' if s['id'] in ['CC2021','CC2023','CvS2025'] else 'PREPRINT'
 locators=s.get('locators',['本文定理は未監査'])
 note=s.get('version_warning','')+' '+s['independent_verification']
 if s['id']=='Zhu2026v2':
  locators=['Theorem 1.2', 'Theorem 6.2', 'Corollary 6.3', 'Section 7 (withdrawal)']
  note+=' Theorem 1.3はRHを仮定するためこのNO分類から除外し、独立項目に分離。'
 if s['id']=='Suzuki2026v3':
  locators=['Theorems 1.1, 1.3, 1.4, 1.5', 'Corollary 1.2', 'Corollary 1.6 (conditional limit)']
  note+=' Corollary 1.6はRHでなく未証明の極限条件に依存。Section 7のRH下heuristicは独立項目に分離。'
 add(s['id'],s['title'],' and '.join(s['authors']),s['year'],s['primary_urls'][0],s['use_status'],'; '.join(locators),s.get('domain','abstractのみ確認、主定理に不使用'),'NO',peer,note)
add('Zhu2026Conditional','Weil positivity in compact windows: conditional claim only','Xuefeng Zhu',2026,'https://arxiv.org/html/2608.24827v2','仮定検査のみ。依存不採用','Theorem 1.3','RHを仮定','YES','PREPRINT','同一論文の固定窓主張とは区別。')
add('Suzuki2026Heuristic','Weil quadratic form: heuristic discussion only','Masatoshi Suzuki',2026,'https://arxiv.org/html/2606.09096v3','仮定検査のみ。依存不採用','Section 7','RH下のheuristic','YES','PREPRINT','無条件の作用素構成定理とは区別。')
add('CCLM2014','Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function','Emanuel Carneiro and Vorrapan Chandee and Friedrich Littmann and Micah B. Milinovich',2014,'https://arxiv.org/pdf/1406.5462v1','既知kernel最適化の先行結果','Section 3.5, Corollary 14','Fourier support制限を持つextremal problem。zero correlation側のRH仮定と区別','NO','PREPRINT','BUILDERとDESTROYERが原文照合。最適化部分のみ関連。')
(ROOT/'literature/sources.json').write_text(json.dumps({'checked_at':'2026-09-29','exhaustive':False,'records':rows},ensure_ascii=False,indent=2)+'\n')
labels=[('id','Reference ID'),('title','Title'),('authors','Authors'),('year','Year'),('url','URL/DOI/arXiv'),('claim_used','Claim used'),('exact_theorem','Exact theorem'),('assumptions','Assumptions'),('depends_on_RH','Depends on RH?'),('peer_reviewed','Peer-reviewed?'),('verified_independently','Verified independently?'),('notes','Notes')]
text='# Literature Ledger\n\n確認日: 2026-09-29。NO の独立検証欄は原文未確認を意味するとは限らず、定理の完全な独立再証明・計算再現をしていないという意味。原文の確認箇所は各項目に記す。PREPRINT は使用した版の区分であり、別途出版済みでないことの断定ではない。\n\n'
for r in rows:
 text+='## '+r['id']+'\n\n'+'\n'.join(f'- **{label}:** {r[key]}' for key,label in labels)+'\n\n'
(ROOT/'literature/ledger.md').write_text(text)
def esc(s):
 return str(s).replace('&',r'\&').replace('_',r'\_').replace('%',r'\%')
bib='%% Source metadata checked 2026-09-29. Preprints are not treated as independently verified.\n'
for r in rows:
 bib+='@misc{'+r['id']+',\n  title={{'+esc(r['title'])+'}},\n  author={'+esc(r['authors'])+'},\n  year={'+str(r['year'])+'},\n  url={'+r['url']+'},\n  howpublished={\\url{'+r['url']+'}}\n}\n\n'
(ROOT/'literature/references.bib').write_text(bib)
(ROOT/'paper/references.bib').write_text(bib)
print(f'{len(rows)} references saved')
