**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `research/local_to_global/notes/search_scope_and_additional_inputs.md` · Original SHA-256: `270ccf7f3c999c02caaa720771fffbd86e3c554541fd2a9c46f8262ce466bbc1`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 文献範囲と追加 convergence input の選別

2026-09-30。検索の存在確認と数学的採用を区別する。
必須6原典の範囲・頁は各専門ノートに記載。全既知研究を網羅したという主張はしない。

## 1. 2026 の overview

[Connes, arXiv:2602.04022v1](https://arxiv.org/html/2602.04022v1)
§6.1 はground real-zero theoremを前件付きで述べる。
§6.5 Fact 6.4 はprolate proxyのstrip収束と
\(C\lambda^{-1/2-\alpha}/(1-2\alpha)\) を述べる。
§6.6 は (i) actual Weil groundのsimple/even、(ii) proxyとの十分な近似、
を残す。§7.6 のUV prolateの結果は高域挙動の一致であり全零点のexact同定ではない。
同じsurveyのheat traceの定理にはRHを仮定するものがあり、今回の無条件入力へ混ぜない。

## 2. 直接関連する追加 preprint の検査

[Śliwiński, arXiv:2601.12133v1](https://arxiv.org/html/2601.12133v1)
は本familyの近似誤差を扱うため全文7頁を確認した。
しかしその Theorem 3.1 の証明を本監査の入力にしない。
理由は「未査読だから」だけではなく、次の数学的な不整合である。

- CCMのrank-one perturbationとmetric quotientを普通の \(E_N\) compressionとして扱う。
- finite-dimensional compression上に \([x,D]=iI\) をそのまま持ち込めない：
  有限次元ではcommutatorのtraceは0で、\(iI\) のtraceは非零。
  periodic differential domainでもposition multiplicationのdomain不変性が必要。
- 一つの状態のspectral varianceから、別に指定されたζ零点列への平均距離の
  下界は導けない。たとえ正しいuncertainty inequalityがあってもこの橋はない。

これは当該 lower-bound 証明を採用しないという判定であり、
actual CCM spectraの正しい誤差漸近を本監査が決定した意味ではない。
さらに必要なのはglobal convergenceの上界であり、この種の下界だけではG*を解かない。

[Groskin, arXiv:2605.20224v4](https://arxiv.org/abs/2605.20224v4)
は数値実装・有限cutoff診断を提供し、abstractは収束未解決・証明主張なしとする。
v1の検索摘要とv4本文では数値負固有値のcutoff artifactの扱いに差があるため、
検索摘要だけでRH反例・Weil不正値性などを結論しない。
本監査はその大規模数値結果を再現したとは主張せず、
新しいcompact一様収束estimateの出典として採用しない。

一般的なFredholm determinant連続性・finite-section・stable-polynomial
結果は、対応するtrace-norm/tail/作用素dictionaryをactual構成で検証できない限り
追加算術入力として数えない。
非一次の研究まとめ、個人の条件付きRH主張、検索結果だけの「証明済み」は採用しなかった。

## 3. 採用と不採用の結論

採用：CCM Lemmas 7.2–7.3 のproxy estimate、Theorem 5.10 のexact formula、
CvS の固定窓real-zero theorem、CCMの正確なSonin map、局所RHの特定対象の定理。

未取得：actual ground/prolate比較の窓一様評価、必要cofinal列のES証明、
actual normalized determinantのnormal-family boundとlimit identification。
取得できなかったことは、この種の定理が将来不可能という証明ではない。
