**STATUS: RIEMANN HYPOTHESIS OPEN**

> 公開用に整形した研究原資料の履歴snapshotです。本文の「現在」「完了」「PASS」は原記録の対象・時点に限定され、RH証明や公開環境での再実行を意味しません。
> Public credit: @ykbballer91 · AI-assisted research log · Text: CC BY 4.0.
> Source: `literature/notes/frontier-overview.md` · Original SHA-256: `7eb9f203cbca2ba2fd937d3d38a0ad3f0b9777ddd8350e4cfcfdb0fabe0a0d8c`.
> 原資料パスと公開パスの対応・書換え・export hashは[公開source manifest](../../../../data/source-manifest.json)を参照。本文のコード・検証ログは履歴であり、このexportでは再実行していません。

---

# 初回 frontier とルート判断

調査日: 2026-09-29。一次論文・著者原稿・公式情報を優先した、候補選択用の調査。
全文献を網羅したという主張はしない。2026年プレプリントは、原文の定理の存在確認と
その証明の独立検証を区別する。ここに挙げた成果は本プロジェクトの新規成果ではない。

|領域|確認した一次資料・状態|完全証明までの障害|
|---|---|---|
|公式問題・ξ|[Clay](https://www.claymath.org/millennium/riemann-hypothesis/)、Riemann 原稿への公式リンク。RH は Unsolved。ξ の標準正規化は既知。|零点対称性から臨界線性は従わない。|
|explicit formula・Weil criterion|Connes–Consani / Suzuki の原文、詳細は `weil-frontier.md`。|全許容関数での正値性が未証明。|
|finite Weil forms・作用素|2025–2026 CCM / Suzuki。固定窓の近似、作用素実現、仮定付き結果を区別。|全窓にわたる追加仮定、零点同定を伴う極限。|
|Li criterion|Li (1997), DOI 10.1006/jnth.1997.2137、出版社原文情報。|全 n の非負性は RH 同値。有限検証では足りない。全文定理番号は未照合。|
|de Branges|Conrey–Li, arXiv:math/9812166v1。|特定の十分正値条件には障害。de Branges 法全体が不可能とは言わない。|
|Hilbert–Pólya・trace formula|Connes, arXiv:math/9811068v1。|臨界零点のスペクトル解釈と、全零点の完全なスペクトル同定は別問題。|
|Euler 積近似|CCM と Connes の2026展望原稿に関係する候補。|元の Euler 積の絶対収束域は Re(s)>1。臨界帯への延長と零点収束は別途証明が必要。|
|Nyman–Beurling / Báez-Duarte|Báez-Duarte arXiv:math/0202141v2, Theorem 1.1 を原文照合。|指示関数の L² 閉包所属が RH 同値。素朴な Möbius 部分和は L² 収束を提供しない。|
|mollifier / moments|Pratt–Robles–Zaharescu–Zeindler arXiv:1802.10521 は過去の下限。|正の割合という結論は全零点の主張ではない。|
|zero density|Guth–Maynard arXiv:2405.20552、原稿要旨を確認。|零点数の上界は、軸外零点数がゼロという結論ではない。|
|2026 pair correlation|Lamzouri arXiv:2609.02882v1, Theorem 1.1。Wang arXiv:2609.07918v1, Theorem 1.1。|原稿で無条件の割合改善を主張。独立に全証明を検証していないため RH 推論の依存には採用しない。|
|function fields|Deligne, La conjecture de Weil I, DOI 10.1007/BF02684373。|有限体上の幾何と Frobenius の仕組みを ζ(s) に移す構成がない。|
|random matrices|Montgomery (1973) 著者提供 PDF の冒頭で RH 仮定を確認。|統計的な対応だけでは全零点の位置を確定できない。最近の無条件版とは仮定を分ける。|

## 2026年の割合改善について

[Lamzouri の原稿](https://arxiv.org/html/2609.02882v1) は
\(\liminf N_0^s(T)/N(T)\ge 3/2-\cot(1/\sqrt2)/\sqrt2\)
を Theorem 1.1 に掲げる。査読状況・解析部分全体の独立検証は未確認。
本プロジェクトが原稿の主張を独立証明したとは扱わない。
同じ原稿の Remark 3.4 は、そこで使う核のクラスで最適定数に達していることを述べる。
この限定された最適化問題を初等的に再導出して、核の取り替えだけで RH に至るという
候補を先に検査する。割合が仮に100%に達しても有限個／密度ゼロの例外を排除しない。

## 初期選択

Weil ルートを、正規化と反証の仕組みを明示しやすい研究対象として選ぶ。
成功確率が他の方法より高いという根拠はないので、数値スコアは付けない。
最初の成果物は「同値条件を増やすこと」ではなく、誤った移行を棄却する監査記録。
連続性の橋が閉じた後は、その橋自体を研究の未解決核心と数え続けない。
全窓正値性が RH 同値のままであれば、補題名を変えて進展としない。

## 次の数学的課題

1. 作用素の閉包・form core が正しく扱われた既知結果を再発明しない。
2. 全窓の正値性を仮定しない、実質的な追加構造があるか検査する。
3. 核最適化の既知障壁を確認したら、その同じクラスの計算探索を止める。
4. 最新固定窓の計算証明主張はコード・誤差境界を再現できるまで保留する。
