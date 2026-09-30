**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `experiments/README.md` · Original SHA-256: `52c76eadc9d77d9ed8a5d72739873284f3f46b791669481ccaa87e43a4dfa4cf`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 反証実験の再現

非認証の反証探索と、Arbによる計算機援用証明書を分ける。どちらからもRHは証明されていない。

- `falsify_models.py`: Python標準ライブラリ。Fractionによる厳密有理数部分とDecimalの非認証求積を区別。
- `kernel_falsification.py`: NumPy 2.3.5。seed=20260929。区分一定モデルのcell積分式は閉形式だが、binary64計算は区間認証なし。

ルートディレクトリから:

```sh
python3 experiments/scripts/falsify_models.py
python3 -m venv .venv
.venv/bin/python -m pip install -r experiments/requirements.txt
.venv/bin/python experiments/scripts/kernel_falsification.py
```

このmacOS環境で利用したNumPy入りPython:
`[local machine path omitted]`。
機械固有の実行ファイルはarchiveに同梱しない。

反例の本体は proofs/failed/ の解析的・代数的導出。
実験だけで無条件の正値性や浮動小数点の符号保証を主張しない。
# 追加: 構造ヒューリスティック反証

`python3 experiments/scripts/structural_falsification.py` をNumPy環境で実行する。
結果は `experiments/results/structural_falsification.json`。
8系統1544例の素数平行移動、対称quartet、Mellin重み、正kernel、nested blocks、
global sampling、実Weil交差項、Euler確率測度の境界を検査する。
有理数恒等式以外はbinary64の非認証数値。実Weil窓差分の負行列式は
`research/structural_audit.md` の別の解析上界で保証する。
主Weil形式の負値やRH反例を発見したという結果ではない。

## 区間証明書

```sh
python3 -m venv .venv-cert
.venv-cert/bin/python -m pip install -r experiments/requirements-cert.txt
.venv-cert/bin/python experiments/scripts/groskin_independent_certificate.py
.venv-cert/bin/python experiments/scripts/window_half_certificate.py
.venv-cert/bin/python experiments/scripts/window_half_crosscheck.py
```

Groskin例はc13,N4の9次有限行列だけ。window-halfはsupport[-1/2,1/2]の全modeを扱い、
偶・奇32次ずつのheadの区間認証と、無限tail・交差項の解析上界を合わせる。
後者の厳密な射程と証明は `proofs/audits/window-half-certificate.md`。
`window-half-independent-224.json` は別担当・別精度の実行。
`window-half-T32-cut64-unverified.json` は初期LDLのnan停止記録であり、成功証明書ではない。

原著組立てとの比較 `groskin_compare_assemblies.py` だけは、版・hashを固定した原著コードの
取得を要する。取得先と手順は `literature/notes/groskin-certificate-audit.md`。
独立証明書の生成に原著コード・零点表・RH仮定は不要。

## Joint symbol と固定積imbalance

```sh
.venv-cert/bin/python experiments/scripts/joint_symbol_certificate.py
.venv-cert/bin/python experiments/scripts/joint_symbol_certificate.py \
  --verify experiments/results/joint-symbol-tail-certificates.json --bits 224
.venv-cert/bin/python experiments/scripts/imbalance_checks.py
```

`python -O` は不可。assertで認証義務を検査する。
joint-symbolは5固定窓の高周波floorだけを認証し、有限headや全Q_W正値性を証明しない。
imbalanceはEuler級数恒等式の区間検査と誤った一般化の反例。ζの線外零点を見つけたという結果ではない。
前者の全閉区間coverはrun-length形式で保存し、Fractionで隙間なく復元する。
後者の厳密な棄却根拠は `proofs/audits/imbalance-reduction.md` と独立監査に記載する。

## 外部proof claimの限定監査

`desogus_targeted_checks.py` は印刷7×7行列の有理数正値性と選択したscalar値、
`desogus_safe_cut_repair.py` は7≤k≤4999の全finite scalar値を独立Arbで検査する。
いずれもactual operator同定やanalytic tailの検証ではない。
`caceres_ratio_checks.py` はprinted X/Yの20個の区間値と全Nの解析error boundを照合する。
Theorem4.1の反証は `proofs/audits/caceres-asymptotic-adversarial.md` の解析証明による。
実行は `.venv-cert/bin/python experiments/scripts/<script>.py`、assertを無効化しない。


---

**公開版の参照案内（編集注）**

本文中のsource-relative pathは原記録の識別子です。収録先:

- [`experiments/requirements-cert.txt`](requirements-cert.txt)
- [`experiments/requirements.txt`](requirements.txt)
- [`experiments/results/joint-symbol-tail-certificates.json`](../../../artifacts/experiments/results/joint-symbol-tail-certificates.json)
- [`experiments/results/structural_falsification.json`](../../../artifacts/experiments/results/structural_falsification.json)
- [`experiments/scripts/falsify_models.py`](../../../artifacts/experiments/scripts/falsify_models.py)
- [`experiments/scripts/groskin_independent_certificate.py`](../../../artifacts/experiments/scripts/groskin_independent_certificate.py)
- [`experiments/scripts/imbalance_checks.py`](../../../artifacts/experiments/scripts/imbalance_checks.py)
- [`experiments/scripts/joint_symbol_certificate.py`](../../../artifacts/experiments/scripts/joint_symbol_certificate.py)
- [`experiments/scripts/kernel_falsification.py`](../../../artifacts/experiments/scripts/kernel_falsification.py)
- [`experiments/scripts/structural_falsification.py`](../../../artifacts/experiments/scripts/structural_falsification.py)
- [`experiments/scripts/window_half_certificate.py`](../../../artifacts/experiments/scripts/window_half_certificate.py)
- [`experiments/scripts/window_half_crosscheck.py`](../../../artifacts/experiments/scripts/window_half_crosscheck.py)
- [`literature/notes/groskin-certificate-audit.md`](../../literature/literature/notes/groskin-certificate-audit.md)
- [`proofs/audits/caceres-asymptotic-adversarial.md`](../../audits/proofs/audits/caceres-asymptotic-adversarial.md)
- [`proofs/audits/imbalance-reduction.md`](../../audits/proofs/audits/imbalance-reduction.md)
- [`proofs/audits/window-half-certificate.md`](../../audits/proofs/audits/window-half-certificate.md)
- [`research/structural_audit.md`](../research/structural_audit.md)

以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `experiments/scripts` — SOURCE REFERENCE NOT INCLUDED
- `proofs/failed` — SOURCE REFERENCE NOT INCLUDED
