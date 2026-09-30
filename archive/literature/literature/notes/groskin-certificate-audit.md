**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/groskin-certificate-audit.md` · Original SHA-256: `49a28709335601849bb592f2f4353502909b9c4c93ab66bc8d5684baacbb99e1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# Groskin 2607.02828v3: 公開検証パッケージと有限証明書の監査

取得・静的確認日: 2026-09-29 (JST)。対象は Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, [arXiv:2607.02828v3](https://arxiv.org/abs/2607.02828v3)。本ノートは公開ソースの所在・版・整合性と有限証明書の射程を記録する。**取得・文献監査担当は**ダウンロードされたコードを実行せず、依存パッケージもインストールしなかった。これは当担当の作業履歴であり、後続の root による実行まで未実施とする記述ではない。論文全証明・Arb 実装の全面的独立検証は **NO**、査読済み掲載は今回確認できず、arXiv preprint として扱う。RH 証明としての採用は **NO**。

**後続の検証状況 (同日追記)。** root は全文静的確認後、原著 v3 コードを `c=13,N=4,384 bits` で再実行し9正 pivot を確認した。さらに原著実装を import せず、S/CC/XC の Arb 直接求積を192 bitsで行い、同じ9次行列の正定値性を独立認証した。`c=13,N=0,1,4` の計91成分では原著384-bit ball が直接求積192-bit ball に包含された。実行環境は python-flint 0.9.0、mpmath 1.4.1 で、著者指定依存版そのものの再現ではない。詳細と信頼基盤は [計算監査](../../../audits/proofs/audits/groskin-computation.md)、結果は [原著再実行](../../../../artifacts/experiments/results/groskin-c13-n4-author-rerun.json)、[独立認証](../../../../artifacts/experiments/results/groskin-c13-n4-independent.json)、[91成分照合](../../../../artifacts/experiments/results/groskin-assembly-comparison.json) を参照。以下の初回取得時点の所見と区別する。**`c=100,N=200` の401次 headline 証明書は未再現のまま**。

## 1. 所在・取得結果

原論文 §4 の Data and code availability に、ancillary files、[著者 GitHub の該当フォルダ](https://github.com/akivag613/connes-cvs-/tree/main/papers/2_guinand_weil_dictionary_tail_order)、[Zenodo concept DOI 10.5281/zenodo.21124802](https://doi.org/10.5281/zenodo.21124802) が明示されている。公開ソースは実在し、arXiv の版を固定した source archive から取得できた。通常のローカル通信が DNS エラーになった後、公開資料取得のネットワーク許可を得て取得した。

| 対象 | 正確な取得 URL | 取得サイズ | SHA-256 |
|---|---|---:|---|
| arXiv v3 source archive | https://arxiv.org/src/2607.02828v3 | 122313 bytes | `f741dbad271ba6d8e4970178666e10c9ad7bca1dea82efb42b48d3499f860857` |
| arXiv v3 PDF | https://arxiv.org/pdf/2607.02828v3 | 383620 bytes | `608ea9a933faa75717f17ec529bd1b2c1666f0a92afa53d64a93ce94f0588924` |

ローカル基点は `literature/source_cache/groskin/`。原本を `arxiv-2607.02828v3-source.tar` および `arxiv-2607.02828v3.pdf` に保存した。source は拡張子に反して gzip 圧縮 tar であり、形式を自動判定して読み取った。展開前に絶対パス・`..`・非通常ファイルを排除し、`arxiv-v3/` に展開した。この取得・展開工程では原本のコードを import したり実行したりしていない。

arXiv の版履歴は v1 2026-07-02、v2 2026-08-13、v3 2026-08-14 14:49:04 UTC。PDF 表紙の July 2026 と v3 の提出日時は別物である。同じ v3 の [HTML](https://arxiv.org/html/2607.02828v3)、PDF およびソースの §4・主要定理・修正説明を参照したが、ローカル LaTeX 再ビルドによる PDF 同一性検証はしていない。

## 2. パッケージの完全性とライセンス

`arxiv-v3/anc/SHA256SUMS` に列挙された **39 ファイルを全件 SHA-256 計算し、39/39 一致、欠落・不一致 0**。これは公表 manifest と取得バイト列の整合性検査であり、数学の正しさや証明書再現成功を意味しない。

| 重要ファイル (`arxiv-v3/anc/` 内) | SHA-256 |
|---|---|
| `SHA256SUMS` | `3188ecce64705d6fc13e849e754f01ad55c9ddbaba735a105fbe8c1f51ec70c8` |
| `arb_ldlt_certify.py` | `ea475850cc79b80a2eb33b439435f3602b8d04523ecd3c08312e53ae3a735089` |
| `c100_N200_arb_ldlt_prec9000.log` | `e2b3c7139fac99fce4aaf502462fb8d00290d6be053ed3b2a59181afd278ce58` |
| `c100_N200_arb_ldlt_prec9000_provenance.json` | `ccb6327eb2f5fc2d81fae923b2db272d4371b7bcbd0ef995562fb99e04538e98` |
| `arch_tail_exact_asymptotic.py` | `6c35b5065babee4cadb626d18a642a63069f1fd86e5aef131c4a69620525d3f7` |
| `arch_tail_exact_vs_asymptotic.json` | `f2edfb1298184e465c0e29becacdb84f04515efeb8c9835e144ab906f29f1277` |
| `requirements.txt` | `59c775ca138e3576d3f675e039405b953e2fc53fb873b3a35b7038bed78aa75d` |

コードの `LICENSE` は MIT、copyright 2026 Akiva Groskin。論文・図は `LICENSE-PAPER-CC-BY-4.0.txt` の CC BY 4.0。`requirements.txt` は次の固定版を指定する。

```text
mpmath==1.3.0
sympy==1.14.0
python-flint==0.8.0
matplotlib==3.10.8
```

歴史的な大規模計算の記録には Python 3.12.11、python-flint 0.8.0、Apple M2 Max 単一コア約15分とある。これは著者の過去の環境・所要時間であり、当環境で確認した値ではない。

## 3. v3 と GitHub / Zenodo の版境界

GitHub API `https://api.github.com/repos/akivag613/connes-cvs-/commits/main` の応答を `github-main-commit.json` に保存できた。取得時の main は commit [`9881eeb02ceb9f7c94e65c0eaaa2a3e81e3e7aaf`](https://github.com/akivag613/connes-cvs-/commit/9881eeb02ceb9f7c94e65c0eaaa2a3e81e3e7aaf)、commit 日時 2026-09-08T14:46:12Z、メッセージ “Clarify Python cache and build-output exclusions”。これは **v3 に対応する commit の同定ではない**。この commit の全ファイルは取得していない。

Web で得られた GitHub main の README は、2026-08-16 の `B_exact` → `B_quadrature` 改称と full pivot transcript の追記を含み、v3 同梱物より新しい。一方、GitHub の checksum ページにはそれより古い artifact 集合が表示され、Web キャッシュの取得時点が揃っていない。従って main の複数ページを継ぎ合わせて「一つの検証済み package」とはしない。GitHub で表示された PDF checksum も arXiv PDF の上記 checksum と一致せず、PDF のビルド差か本文版差かは未判定。

Zenodo concept DOI は最新版へ向く識別子であり、固定 deposit version ではない。今回 DOI/record の Web アクセスは失敗し、API `https://zenodo.org/api/records/21124802` のローカル取得も接続待ちで中断した。**version-specific DOI、ダウンロード URL、deposit checksum、v3 とのバイト同一性は未確認**。取得済みの arXiv v3 を再現の基準とする。README の「Zenodo PDF と byte-identical」という記述は著者の主張としてのみ残す。

v3 の訂正対象は、`mp.nsum` の未収束な系列加速による `h_+'(50), h_+'(100), h_+'(1000)` の ancillary 値。v3 の script は trigamma の直接評価に変更され、artifact には約 `0.02000066676`, `0.01000008334`, `0.001000000083` が記録されている。著者は Lemma 3.1 の bound と本文定理に変更なしと明記している。これらの数値を当方が再計算したわけではない。

## 4. 原定理の射程と RH 依存

以下は原文の statement を読み取ったもの。RH を仮定しない有限系の主張であり、全証明の独立監査済みという判定ではない。`c>1`, `N≥0`, `L=log c`, `rho=2π/L`, `I_N={-N,…,N}` とする。

**Theorem 2.5 (finite dictionary).** 実 even-sector vector `v∈R^(N+1)` から論文所定の band-limited `g_v` を作ると、有限行列 `Q∞(c,N)` の二次形式は、`1/2+iz` が ζ の非自明零点となる **複素数 z 全体** の `g_v(z)` の和に等しい（重複度込み）。零点を実数と仮定していない。この有限族から任意の Weil test function への逆写像や全関数空間の正値性は得られない。Lemma 2.1 の CCM closed forms との entry identification が実装と原典をつなぐ追加検証箇所である。

**Lemma 3.1.** `h_+(t)=Re ψ(1/4+it/2)−log π` について、`t>0` で単調増加、`h_+'(t)≤1/t+13/(10t²)`。Arb による `0<h_+(7)<0.1072` を入力し、`t≥7` の `h_+(t)≤log t−8/5` を導く。初回取得担当はその Arb 評価を再実行しなかった。後続の [計算監査](../../../audits/proofs/audits/groskin-computation.md) でこの上下界を認証し、[tail 監査 §3](../../../audits/proofs/audits/groskin-tail.md) では特殊関数ライブラリを用いない有理上下界から必要な符号と envelope を独立導出した。いずれも RH を仮定しない有限定数評価である。

**Theorem 3.2.** `T₂>T₁>max(rho N,7)`、`p_T(n)=1/(T/rho−n)`, `q_T(n)=1/(T/rho+n)` のとき、

```text
Q_arch,T₂ − Q_arch,T₁
 = (1/π²) ∫[T₁,T₂] h_+(T) sin²(LT/2)/rho · (p_T p_Tᵀ + q_T q_Tᵀ) dT.
```

この増分は **固定有限周波数空間 C^(2N+1)** 上で正定値、自然な添字順の全小行列式も正という主張である。正定値なのは post-band の archimedean 増分であり、prime block や全 Weil form を正定値とする定理ではない。

**Corollary 3.3.** `Q_T^tot=Q_prime^(c)+Q_pole+Q_arch,T`、`B_T` を上の正の tail の trace とすると、同じ `T>max(rho N,7)` で

```text
0 ≺ Q∞ − Q_T^tot ≼ B_T I,
λ_j(Q_T^tot) < λ_j(Q∞) ≤ λ_j(Q_T^tot)+B_T.
```

従って `λ_j(Q_T^tot)≥0` なら対応する cutoff-free eigenvalue は正、`λ_j(Q_T^tot)<−B_T` なら負と決定できる。原文は曖昧帯を `[−B_T,0)` と記すが、**左端を含める記述はそのまま採用しない**。[tail 監査 §6](../../../audits/proofs/audits/groskin-tail.md) の指摘 E1 により、正確な `B_T=tr(Q∞−Q_T)` と `N≥1` では `λ_j(Q_T^tot)=−B_T` から既に cutoff-free の負性を認証できる。`N=0` の同じ等号では cutoff-free 固有値は0と決まる。一般に未決定とする帯は開区間 `(-B_T,0)` と区別する。これは条件付き認証規則の端点修正であり、実際の ζ 行列でその等号を実現したという主張ではない。`N≥1` の明示的上界は

```text
B_T ≤ 2(2N+1)rho/π² · [log(T)/(T−rho N) + log(T/(T−rho N))/(rho N)].
```

`(c,N)` を固定した `T→∞` では

```text
B_T = (2N+1)rho/(π²T) · (log(T/(2π))+1) · (1+o(1)).
```

この漸近式は `(c,N)` に一様な誤差評価ではない。`c=100,N=200,T=800` の artifact にある `<0.8965687...` は dyadic Arb budget と解析 tail bound の組合せによる著者の計算結果。`B_exact≈0.4203` は数値積分であり、名前だけで厳密な interval enclosure と解釈してはならない。

**量化の制約。** `T→∞` は一つの固定有限行列の archimedean integral cutoff を除く極限。`N→∞`, support window `c→∞`, 全 test function の PSD の証明にはならない。有限個の `(c,N)` の成功を ∀`c,N` に昇格させてはならない。全窓と適切な form core 上の exact restriction/closure に至れば Weil criterion の RH 同値条件が戻るため、その未証明前件をこの論文が解消したとは扱わない。

## 5. Arb 証明書の実装を読む限りでの所見

対象は `arb_ldlt_certify.py`。以下は取得担当が依存を import せずテキストだけを読んだ初回所見である。後続の root の全文静的確認・解析照合・小例実行は [計算監査](../../../audits/proofs/audits/groskin-computation.md) に記録され、幾何級数剰余の安全性もそこで確認されている。ここでは401次の再現済み判定へ拡張しない。

- `build_arb_tau(c,N,prec)` は `tau=W02−WR−Wp` の `(2N+1)×(2N+1)` 実対称 ball 行列を組み立てる。digamma/trigamma と幾何級数を用い、prime powers は `q≤c` の有限整数列挙。**この証明書は finite-T certificate に tail を足したものではなく、closed forms による cutoff-free finite matrix の直接計算**である。
- `_geom_sums` は4系列に `rem=4*exp(−c_next L)/(1−exp(−2L))` の半径を加える。係数上界、Arb radius の解釈、式の規約・符号と Lemma 2.1 の一致が誤差保証の主要な確認点。Arb を使うという事実だけでは、誤った行列式や誤った剰余式を排除できない。
- `certified_inertia` は pivoting をしない interval `LDLᵀ`。各 pivot ball が厳密に正または負と判定された場合のみ inertia を数える。0 を含む場合は `undetermined_pivot` を返す。適切な enclosure が成立すれば有限行列に対する証明の構造になる。取得担当はその前件と実行結果を確認せず引き渡し、後続の小例の認証範囲は冒頭の追記に限定する。
- `--selftest` は `selftest()` と引数なしで呼ばれるため、CLI の `--c/--N/--prec` に関係なく **c=13,N=8,prec=300** の self-test。大規模行列を mpmath で再検算する指定ではない。
- self-test は mpmath 80 桁、系列打切り約 `1e−70`、相対許容 `1e−60` の同じ closed formulas の agreement test。厳密な ball containment 検査ではないことは README と code 自身も明記する。
- 未確定 pivot があっても main は非零 exit code を明示しない。自動判定では終了コードだけでなく JSON の `undetermined_pivot is null`, `n_pos==2N+1`, `n_neg==0`, `certified_positive_definite==true` を確認する必要がある。
- v3 には全401 pivot ball の transcript がなく、headline log と summary JSON があるだけ。第三者が実装を再実行せず独立の小さな checker で401本の interval を読み直せる証明書とは、現物上確認できない。

headline の著者記録は `c=100,N=200,prec=9000 bits,n_pos=401,n_neg=0`。ただし log の build/LDL 時間は `733.2s/90.7s`、JSON は `715.1s/88.4s` と異なる。log の時刻・文言も現行 v3 script の出力と一致せず、JSON は `2026-07-02T06:29:27` を記録する。別実行・過去 script に由来し得るが、**両者を同一 invocation の完全な追跡記録と同定できない**。正値性の反証ではなく、再現時に残る provenance の制限である。

## 6. 取得時に親担当へ渡した最小再現手順（当担当は未実行）

arXiv `anc/` は **flat directory** であり、GitHub 用 README の `scripts/`, `artifacts/`, `audit/` という配置と異なる。そのまま README の `python3 scripts/...` を打つと path が存在しない。原本 cache を保全し、`anc/` を作業用ディレクトリへコピーしてそこで実行する。script によっては既定名の JSON を上書きするので、原本上で実行しない。

固定依存を別環境に導入し、コピーした `anc/` を cwd とした場合の最小 Arb 例:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 arb_ldlt_certify.py --selftest --c 13 --N 8 --prec 300 --json-out fresh-c13-N8.json
```

著者の `VERIFICATION.md` の期待値は `n_pos=17,n_neg=0,CERTIFIED`。これが今回実際に再現されたという意味ではない。標準ライブラリだけで走る最小の代数 guard は `python3 audit_exact_series_identity.py` だが、これだけで行列の正値性を検証したことにはならない。

headline と tail の再現コマンドは、同じ作業用コピー上でそれぞれ:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 arb_ldlt_certify.py --selftest --c 100 --N 200 --prec 9000 --json-out fresh-c100-N200.json
PYTHONDONTWRITEBYTECODE=1 python3 arch_tail_budget.py --c 100 --N 200 --T 800 --prec 300 --dyadic-count 80 --json-out fresh-tail-c100-N200-T800.json
```

再実行 JSON の日時・所要時間は変動するため、アーカイブ SHA 一致を新規出力の成功条件にしない。まず取得物 SHA を照合し、次に入力パラメータ・理論 enclosure・全 pivot の符号と結果の同一性を検査する。

## 7. 判定と未完項目

確認済み: v3 の公開ソース・PDF の取得、39/39 checksum 整合、ライセンス、固定依存、原文に基づく有限定理の条件、最小実行コマンドの構文・flat layout 補正、静的 code の上記挙動。

後続担当が確認した範囲: 原著コード `c=13,N=4,384 bits` の9正 pivot、原著実装を import しない直接求積192-bit行列の9正 pivot と保存後再読込、`N=0,1,4` の91成分の ball 包含、closed forms と直接積分の解析照合、幾何級数剰余の係数上界、`h_+(7)` の所要区間。根拠と制限は [計算監査](../../../audits/proofs/audits/groskin-computation.md)、辞書規約は [辞書監査](../../../audits/proofs/audits/groskin-dictionary.md)、tail と Corollary 3.3(ii) 左端の修正は [tail 監査](../../../audits/proofs/audits/groskin-tail.md) を参照。取得担当自身による実行ではない。

未確認: **401次・9000-bit headline の実行再現**、原定理全証明・全付属数値出力の全面的独立検証、Zenodo 固定 deposit version/hash、GitHub immutable commit と arXiv v3 の完全対応、full401 pivot certificate の v3 外での独立確認、査読掲載。これらを PASS に昇格していない。小例の認証を全窓・全次数の正値性へ拡張しない。

この package は有限計算を具体的に検査するための有用な公開入力である。全窓 PSD、RH、全 test-space の自己共役実現または prime-location theorem の証拠としては使用しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/results/groskin-assembly-comparison.json`](../../../../artifacts/experiments/results/groskin-assembly-comparison.json)
- [`experiments/results/groskin-c13-n4-author-rerun.json`](../../../../artifacts/experiments/results/groskin-c13-n4-author-rerun.json)
- [`experiments/results/groskin-c13-n4-independent.json`](../../../../artifacts/experiments/results/groskin-c13-n4-independent.json)
- [`proofs/audits/groskin-computation.md`](../../../audits/proofs/audits/groskin-computation.md)
- [`proofs/audits/groskin-dictionary.md`](../../../audits/proofs/audits/groskin-dictionary.md)
- [`proofs/audits/groskin-tail.md`](../../../audits/proofs/audits/groskin-tail.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `literature/source_cache/groskin` — SOURCE REFERENCE NOT INCLUDED
