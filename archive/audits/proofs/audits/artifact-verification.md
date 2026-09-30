**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `proofs/audits/artifact-verification.md` · Original SHA-256: `4dc5e0801478c5f03e56482f542e2885ba088ba0dce588afc80a1eb9839baa57`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 成果物の検査 — 数学的完成判定とは別

2026-09-29、research checkpoint 03。PDF本文はcheckpoint01から未変更。以降の認証はMarkdownとJSONに分離。

- `paper/main.tex` をTectonic 0.17 / BibTeXでコンパイル成功。9頁。
- `paper/main.log` にOverfull・Underfull・Warning・undefined・Missing characterなし。
- 全頁をPNGで目視確認。最終変更後の第9頁で参考文献の収まり、式、余白、改頁を再確認。
- PDF SHA-256: `30d1bdeaf9791938c73493dab54cc484b3ce8808280e3fae054129fad0048e8a`。
- 追加構造トラックはMarkdownに分離し、PDFをRHの完成論文に変更していない。
- NumPy実験を実行しJSONを保存。区間認証のない近似値と解析的反例を分離。
- metadata validatorはmain graph19ノード、主台帳31records、構造statement台帳22records、Lean7宣言の記録を照合。
- Lean本体の成功ログは `formal/lean/verification/`。追加は二block下界の実代数1宣言だけ。
- c13,N4の9次行列は独立Arb求積192bitsと区間LDLで9正pivotを認証。
  原著コード384bitsとのN0/N1/N4比較91成分が包含一致。JSON再読込の9次認証も成功。
- 原著401次例のログは取得物として監査したのみ。再実行済みとは扱わない。
- `source_cache` と仮想環境をGit・archiveから除外。公開原本の版とhashは取得監査に記録。
- 固定窓[-1/2,1/2]の全mode認証は192bit headと解析tail/coupling、224bit別実行、
  保存行列の別Cholesky、5成分の別adaptive求積が成功。主グラフT090はこの局所結果のみ。

これは出力・記録の整合性検査。RH証明、外部査読、新規性、数学的完全性を認定するものではない。


---

**公開版の参照案内（編集注）**


以下は原記録のprovenanceで、公開版には含めていません（非リンク）。第三者原著は本文の外部引用URLを参照してください。

- `formal/lean/verification` — SOURCE REFERENCE NOT INCLUDED
