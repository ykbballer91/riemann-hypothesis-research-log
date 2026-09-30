**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/zhu-certificate-audit.md` · Original SHA-256: `7ee0ea746a924b86d96f99ecfc027a6724e4b0df983c3dc0e83be00e018899f5`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Zhu 2608.24827v2: L=0.8 証明書の所在・版・適用範囲監査

調査日: 2026-09-29 (JST)。担当: LITERATURE AUDITOR。対象は Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, [arXiv:2608.24827v2](https://arxiv.org/abs/2608.24827v2)。このノートの `L=0.8` は support 半幅であり、Lemma 8 等の定理番号ではない。

**判定: 原文 v2 の PDF・TeX は取得できたが、公表が記述されている計算 package の公開先・現物は今回の探索で確認できなかった。** `verify_certificate.py`、200次行列、Cholesky factors、JSON、実行 log、著者 SHA-256 manifest は取得した arXiv source に含まれない。従ってコードの静的監査・証明書再実行・infinite tail/coupling の実装保証は未実施。存在しないと断定する結果ではなく、確認した版と検索範囲での未発見である。原論文全証明の独立検証は **NO**、計算再現は **NO**、査読掲載は未確認。RH の証明として採用しない。

## 1. 版固定と取得物

arXiv の履歴では v1 は 2026-08-25 17:07:51 UTC、v2 は 2026-09-02 17:32:21 UTC。本文の日付 September 3, 2026 と提出日時は区別する。v2 の comments は著者名・所属の更新を明記している。検索 index に旧著者名 Marcus Chuk が残るが、今回の書誌は取得した v2 の Xuefeng Zhu に固定する。

通常のネットワーク取得が DNS エラーになった後、公開資料取得の許可を得て次を保存した。ダウンロード資料からコードの実行・import・TeX コンパイルはしていない。tar の展開時は絶対パス・`..`・通常ファイル/ディレクトリ以外を排除した。

基点: `literature/source_cache/zhu/`。

| 取得物 | 正確な取得 URL | bytes | SHA-256 |
|---|---|---:|---|
| `arxiv-2608.24827v2-source.tar` (内容は gzip tar) | https://arxiv.org/src/2608.24827v2 | 470846 | `1afc4e867bc69cabf5128db8b70187af61804e55bd773a16cdf16d17c4284c73` |
| `arxiv-2608.24827v2.pdf` | https://arxiv.org/pdf/2608.24827v2 | 924766 | `70332e428dd7ab82a352131787ac3db4b321459f0e12a6765a8ab1e6fbc22026` |

source archive の内容は以下の **6 通常ファイルだけ**であり、`arxiv-v2/` に展開した。

| ファイル | bytes | SHA-256 (当方計算) |
|---|---:|---|
| `00README.json` | 213 | `d1f6b1a71c9accb812ec5121d1fff7910c025ca7bb201948bacdb40941bc14e5` |
| `main.tex` | 122242 | `14ec17c2b2e1d3d8069c1d424dae4f5aa6c92b75c73b89d10915ed868495f2c5` |
| `weil_discrimination.png` | 120580 | `1c7462aa7b6e0b7fb75e7586fdad97540d054db8cd561304158549fa77aa6b31` |
| `weil_final_verdict.png` | 127739 | `ae31e3697757eebf0a011a125e12b594ece36954d4d5b1381f5ae4ea3927fbac` |
| `weil_minimizer_portrait.png` | 93745 | `2d355d9cfcdde31cea3d863cd1621f203bdd12c3b3b7356106ef70539bde1572` |
| `weil_mp_verdict.png` | 128440 | `c04e24bcbff8352e4e1769c741d29942effa9d753caf6fa8e6830d9cab9b889b` |

`00README.json` は arXiv のビルド指定（pdflatex、TeX Live 2025、main.tex）であり、計算証明書の JSON ではない。これらの hash は取得物の版を固定するため当方が計算した値であって、著者公表 manifest との照合成功を意味しない。

## 2. 公開コード・ライセンス・再現手順の確認結果

[v2 §17 Reproducibility](https://arxiv.org/html/2608.24827v2#S17) は、source、software versions、zero data、certified matrices、Cholesky factors、run logs、error budgets、SHA-256 hashes と `verify_certificate.py` を補足資料として提供すると記す。検証器の説明は「アーカイブ行列の再 factorization、倍精度桁数の residual 再計算、求積 budget `c_err` と tail constants `ε_D,ε_B` の再導出」。§10 は repository に言及する。しかし本文 TeX の全 URL・href・supplementary・ancillary・repository・SHA・script 参照を検索しても、**公開 repository / release / download の URL は記載されていない**。唯一の通常外部 URL は引用文献の mpmath.org だった。arXiv abs に ancillary file の一覧も表示されなかった。

| 求めたもの | 今回の状態 |
|---|---|
| 原著 package URL / version / commit | 未確認 |
| `verify_certificate.py` 現物 | 未取得、コード内容不明 |
| `pwl_parity_recon.py` 現物 (§6 で言及) | 未取得 |
| `M_200`、Cholesky factor、数値 JSON | 未取得 |
| 著者公表 SHA-256 manifest | 未取得 |
| 原著コードの license | 未確認 |
| 原著の正確な依存版・CLI 引数 | 未確認 |
| 実際に使用できる再現コマンド | 確認できず |

論文の [arXiv license 表示](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html) は arXiv に対する perpetual non-exclusive distribution license。これを MIT / CC-BY 等のコード再利用許諾に読み替えない。ソース archive に独立の LICENSE はない。

本文の環境説明は Python 3、mpmath、大規模 run の gmpy2 backend、L=0.8 の lower-bound assembly 50 decimal digits、総約40 CPU-hoursと parity runs 約2 CPU-hours。実物の `requirements.txt` 等を取得できていないため、固定依存版や過去実行の環境は再現できない。ファイル名だけから未確認の CLI を作って「原著の再現手順」とはしない。

探索した文字列: `"2608.24827" "verify_certificate"`, `"Weil positivity in compact windows" code`, `"Xuefeng Zhu" "Weil" github`, `"2608.24827" site:github.com`, `"verify_certificate.py" "Weil"`, `"Weil positivity" "Zhu" "supplementary"`, 旧著者名を含む同様の検索。GitHub / Zenodo / OSF / Figshare / dlut.edu.cn に限定した検索も行った。ヒットした第三者の関連研究・紹介・別証明書を原著 package の代用品とはしない。検索エンジンの未発見は公開物不存在の証明ではない。著者への連絡はしていない。

## 3. 固定窓の還元: 正確な前件と有限→無限の主張

以下は [v2 本文](https://arxiv.org/html/2608.24827v2) と取得した `main.tex` の statement/式を整理したもの。独立な全面的証明審査は別作業であり、ここでは引用を PROVED に昇格しない。

実偶 `f`、`supp f⊆[−L,L]`、`F(t)=∫f(x)e^{itx}dx` として、原文は

```text
Q(f)=2 F(i/2)²+(1/(2π))∫_R |F(t)|² Ψ_L(t) dt,
Ψ_L(t)=Re ψ(1/4+it/2)−log π−Σ_(log n<2L) 2Λ(n)/√n cos(t log n),
A_L=Σ_(log n<2L) 2Λ(n)/√n.
```

と置く。pole のこの正の二乗表示は実偶 sector のもの。一般複素 `f` へこの式を無変更で適用せず、§6 の parity decomposition と odd pole の負符号を必要とする。

**Lemma 3.1 (Crude envelope).** `t≥15/4` で `Ψ_L(t)≥log(t/(2π))−1/t−A_L`。Binet formula からの解析評価で RH を仮定しない。

**Theorem 1.1 (One-stroke reduction), 証明 §4.** `L>0` を固定し、`β*=log(T♯/(2π))−1/T♯−A_L>0` を満たす `T♯` を選ぶ。`A_L≥0` なのでこの条件は必要な `T♯>2π>15/4` も保証する。すると実偶 sector で

```text
Q(f)≥R(f)=2 F(i/2)²+(1/π)∫_0^T♯ (Ψ_L(t)−β*)|F(t)|²dt+β*||f||².
```

偶 Legendre basis `T_n(x)=P̄_n(x/L)/√L`, `n=0,2,…` を用いる。`ν_n=n+1/2`、`T̂_n(t)=(-1)^(n/2)2√(Lν_n)j_n(tL)`。有界な reduced form は `M_R=β*I+2ppᵀ+C` となり、最初の N モードと無限 tail で

```text
M_R = [ A  B ; B*  D ]
```

と分解する。必要なのは有限 head `λ_min(A)≥λ_0` に加え、**無限 tail 全体**の `D≥(β*−ε_D)I` と、**全 head–tail coupling**の作用素ノルム `||B||≤ε_B` である。これらが成立すれば

```text
Q(f)≥[min(λ_0,β*−ε_D)−ε_B]||f||².
```

原文は `|j_n(x)|≤x^n/(2n+1)!!` を使う forbidden-region 評価、tail の Gershgorin row sums、coupling の Schur bound `||B||≤√(||B||_1||B||_∞)` でこの2誤差を扱う。初めの discarded order `2N ≳ eLT♯/2` は漸近的目安であり、それだけで特定の ε を保証する厳密条件には置き換えられない。

**infinite tail の扱いは本文構想に含まれる。** 固定サイズの matrix PSD だけから全窓正値性へ飛躍する構成ではない。ただし取得できた現物には、無限 row/column sums の数値 enclosure を再計算するコード・入力がなく、実装がこれらの前件を満たすかは未確認。

form domain の注意: 有限 support の任意の `L²` 関数でも、`∫log(2+|t|)|F(t)|²dt` が自動的に有限とは限らない。引用時は有限 form domain と extended-valued `Q=+∞` の解釈、smooth core からの閉形式への拡張を区別する。有限-dimensional eigenvalue 計算がその domain の同定を代行することはない。

## 4. L=0.8 の計算主張と誤差 budget

**Theorem 1.2** は実偶 `L²` test に `Q(f)≥8.9×10^−18 ||f||²` と主張する。**Corollary 6.3** が parity の各実部・虚部を合わせて同じ固定窓の一般複素 test へ拡張する。後者には odd-sector certificate が別途必要である。`L=0.8` の prime-power support は `{2,3,4}`。

| 項目 | 原文の数値・条件 | 現物確認 |
|---|---|---|
| head assembly (§5.1) | `T♯=200`, `N=200` even orders 0…398、50 digits、800 panels、幅1/4、32-point Gauss–Legendre | 行列・nodes・weights・評価 code 未取得 |
| envelope | `A_L≈2.9419735`, `β*≈0.5134667` | finite prime sum の原式は確認、実行なし |
| pole assembly | Gauss order320、entire integrand の求積残差を評価 | factor/vector 未取得 |
| Lemma 5.1 | Bernstein parameter6.55、strip `|Im t|≤0.4`、`|Ψ_L−β*|≤20`、`M≤4.9×10^4` | 原文 statement 確認、独立 enclosing 計算なし |
| quadrature | per-entry `ε_Q≤1.03×10^−44`, `c_err=Nε_Q≤2.06×10^−42` | 原著 verifier 未取得 |
| first tail (§5.3) | order400、`max_(t≤200)|T̂_400(t)|≤4.3×10^−108`、pole tail `<10^−390` | 具体的 certificate 未取得 |
| infinite tail/coupling | `ε_D≤10^−100`, `ε_B≤10^−100` | 無限 sums を保証する実装・JSON 未取得 |
| Lemma 5.2 / shifted Cholesky | shift `λ_0+c_err`, `λ_0=9×10^−18`, residual `r=1.06×10^−50`, roundoff slack `s=3.6×10^−43` | 行列/factor/log 未取得 |
| odd sector (§6.2) | `T♯=150`, 200 odd orders1…399、`c_err=1.6×10^−42`、約`8.2065×10^−15` の shift | 別 certificate 未取得 |

Lemma 5.2 自体は近似因子 `LLᵀ≥0` と厳密 residual bound から得る有限行列不等式。**Cholesky が数値的に成功するだけでは足りず**、丸め slack、入力 parsing、exact integral と assembled matrix の距離を全て含む必要がある。原文 §5.4 の論理は `λ_min(A)≥λ_0−(r+s)` と無限 tail/coupling の組合せであり、いずれか一つの誤差 budget を省くと Theorem 1.2 の証明書にはならない。

静的に確認を要する具体点: §4 の `C_nm=(1/π)∫_0^T♯ (...)T̂_nT̂_m dt` に続く掲示 entry bound には、supremum を積分へ適用した通常の上界に現れる長さ因子 `T♯/π` が表示されていない。ここでは omission らしい箇所を指摘するに留め、別の積分評価で救えるか、実装に係数があるか、最終 `10^−100` が依然十分かは reduction の独立監査へ渡した。公開コード未取得のため実装での補完を仮定しない。

§17 は検証器が `M_200` から `9.0×10^−18` を返すと説明するが、本文 §5.4 の exact budget は `9×10^−18−(r+s)−ε_B`。表示丸めの `9.0` をそれ以上の厳密下界と読まない。安全側に丸めた Theorem 1.2 の `8.9×10^−18` と区別する。

## 5. Ground state・RH・撤回との境界

**Theorem 6.2** の simple-even ground state 主張には even lower/upper、second even min–max lower bound、odd lower/upper の各証明書が必要。200次 head の第二固有値だけを全 window の第二 min–max 値に同一視できず、対応する tail/coupling と frame/Gram の扱いが要る。原文は codimension-one restriction と block lift を述べるが、Householder frame と residual 現物は未取得。

§6 冒頭は CCM との normalization dictionary の逐行照合を実施していないと自ら断っている。正の scalar 倍が ordering を保つことと、原典と今回の形式が実際にその scalar 倍で一致することは別であり、operator theorem への接続を確認済みにしない。

今回の lower-bound statements は RH を前提にしていないと明示される。一方 **Theorem 1.3 / §13** の `λ*(L)≤exp(−Le^L)` は RH 仮定付きで、無条件に引用してはならない。Landau–Widom 定数 `2π²` は fitted law / Conjecture 12.1 であり、全窓下界や一般の計算量下界を証明した値ではない。零点側の試行ベクトル生成は幾何側 certificate と区別する。

**§7 の L=1.19 (support 2.38) 証明主張は撤回されている。** per-prime 最小化の `A_eff` は prime comb の下界であって、symbol の下界に必要な comb 上界を与えない。950次行列の数値正定値性を全窓の定理と扱わない。

仮に L=0.8 の全証明書が再現されても、一つの固定窓の局所結果である。すべての L に対する PSD、ground-state zeros の大域収束、ζ零点の実性は得られない。有限 test-space と無限 test-space、さらに固定窓と全窓という2段階の量化を保持する。

## 6. 引継ぎと採用判定

本担当が完了したのは v2 原資料の隔離取得・hash 計算・全文中の公開先探索・定理と certificate 前件の整理。取得したファイル以外のコードを代用せず、何も実行していない。主台帳・graph は変更していない。

現在入手できる一次資料だけでは「原著の L=0.8 計算証明書が infinite tail/coupling まで検証済み」と判定できない。**現物取得・実行再現の状態は NOT REPRODUCED**。これは Theorem 1.2 の偽性の証明でも、§4 の抽象 block inequality の否定でもない。

次に必要な現物は、v2 に対応づけた immutable source snapshot、license、依存版、全 head matrix と factor、求積誤差を再導出する入力、全無限 sums の tail/coupling bounds、roundoff budget、parity/frame 証明書、著者 manifest。入手できなければ独立実装の結果は「原著の再現」ではなく「本文の特定の構成を独立に検査した結果」として範囲を明記する。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/zhu` — SOURCE REFERENCE NOT INCLUDED
