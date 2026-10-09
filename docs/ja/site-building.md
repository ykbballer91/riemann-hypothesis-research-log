# 日英サイトのビルドと表示確認

**STATUS: RIEMANN HYPOTHESIS OPEN**

編集用Markdownは `docs/ja/` と `docs/en/` に置き、同名ファイルを `/ja/`・`/en/` の対応ページへ出力します。各ページに言語切替、言語別ナビゲーション、正規URL、`html lang`、相互の `hreflang` を設定します。`index` は `guide`、`source-map` は `sources`、`home` は言語別の入口へ対応します。

ルートと旧 `/docs/*.html` は、言語別の正規本文から生成する互換ページです。転送と可視リンクを備え、独立した最新状態を持ちません。JavaScriptでクエリと見出し位置を保持し、旧見出しの別名も残します。歴史的な公開研究状態記録と、その状態メタデータは変更しません。

最新の公開用要約は[10月9日の状態記録](../../data/current-state-2026-10-09.json)に別置きします。旧日付の記録は当時の証拠として保持します。日英の現在地ではBと有限Weilの別会計を説明し、新しい研究原資料一式はビルド入力へコピーしません。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-site.txt
.venv/bin/python tools/build_site.py
.venv/bin/python tools/validate_public.py --site
.venv/bin/python tools/validate_bilingual.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory _site
```

生成先 `_site` と仮想環境はGit対象外です。TeXをMarkdown処理から保護し、jsDelivrのMathJax 3.2.2で表示します。長い数式・表は本文全体を広げず、その領域内で横移動できます。

## 編集と証拠の境界

各編集ファイルには同名の対応訳が必要です。研究報告、監査、実験資料、状態記録は原文のまま保持します。378件の原文対応表と既存公開ハッシュは変更しません。整理前の公開文は `archive/editorial/pre-bilingual-2026-10-01/` に参照先を調整して保存します。これは編集履歴であり、新しい数学的結果ではありません。

公開検証器は内部リンク・見出し、JSON、原文ハッシュ、未解決表示、著者、公開日、配信条件を確認します。日英検証器は対応URL、言語メタデータ、ナビゲーション、現在地の整合、旧URLも検査します。数学の証明や研究実験の再実行ではありません。モバイル表示と匿名アクセスは[編集作業の検証記録](../../audit/bilingual_review.md)にまとめます。

## GitHub Pagesへの配信

`main`へのpushでビルド・検証を行います。配信にはさらに `deploy=true` の明示的実行、公開リポジトリ、`PUBLICATION_APPROVED=true` が必要です。既存の条件は保持します。ビルド成果物だけでは公開サイトへの反映ではありません。検査済みリビジョンに固定した公式[GitHub Pages Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)を使います。
