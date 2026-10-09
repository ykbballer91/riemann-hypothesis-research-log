# 再現手順と検証の限界 {#_1}

**STATUS: RIEMANN HYPOTHESIS OPEN**

公開資料は選択したコード、出力、書面の議論を保存しています。公開準備では数学実験・区間認証・Leanビルドを再実行していません。過去の `PASS` は入力、版、精度、領域とともに読む必要があります。内部AI担当の一致は外部査読ではありません。

## L0〜L7について再現できる範囲

[2026-10-09の更新](updates/2026-10-09-logic-rh-l7.md)は選択的な公開要約です。完全な新規証明・内部監査・コード・有理endpoint一式は非公開で保存しており、この公開ツリーから全主張を独立再現できるとは表示しません。以下のreplay・公開manifestは以前に公開した資料の範囲です。

L7の通常ZFC論証と長さ上界は、生成済みのHilbert証明文字列や機械証明ではありません。原研究の有限比較は入力違反の受理例を含まず、違反保存の実行成功として数えていません。L6は外部検証の公開生ログ・固定版照合と局所検算を利用し、自前kernel/comparatorは未実行です。[参考文献](references.md)から固定した外部原稿・報告へ進めます。

今回の公開編集では研究コード・数学実験・Leanを再実行していません。サイト構築、文書・リンク・日英・公開安全性の確認は、数学的な再証明とは別です。


## 研究コードを実行せずに確認する {#_2}

公開リポジトリのルートで、次を実行します。

```sh
python3 artifacts/replay.py --list
python3 artifacts/replay.py \
  --script experiments/scripts/window_half_certificate.py \
  --prepare-only
```

補助スクリプトは公開資料のハッシュを確認し、選んだ元の相対配置を隔離した作業領域に再構成します。依存関係・第三者資料はダウンロードせず、準備だけなら研究スクリプトを実行しません。不完全・実行不能な再現は[実験資料の案内（原文）](../../artifacts/README.md)に記載しています。[対応表](../../data/source-manifest.json)は元のハッシュと公開用ハッシュを区別し、公開見出しを付けたファイルが元のハッシュと一致することは要求しません。

依存関係は別環境に入れてください。保存された基本要件はNumPy 2.3.5、区間認証はpython-flint 0.9.0とmpmath 1.4.1を指定しています。後続診断にはSciPy等が必要な場合があります。これは当時の環境記録で、現在の全プラットフォームでの動作保証ではありません。

当時の要件：[基本](../../archive/reports/experiments/requirements.txt)・[区間認証](../../archive/reports/experiments/requirements-cert.txt)。

必要環境があれば `--prepare-only` を外して、そのPythonで選んだスクリプトを動かせます。以下はヘルプだけを要求します。

```sh
python3 artifacts/replay.py \
  --script experiments/scripts/window_half_certificate.py \
  -- --help
```

`--` 後の引数はスクリプトへ渡します。新しい出力は隔離領域に残り、補助スクリプトは旧結果との一致や認証の妥当性を判定しません。全実行の前にコードと数学的義務を確認してください。認証スクリプトでは必要な不等式をassertで検査するため `python -O` は使わないでください。

## 四種類の証拠 {#_3}

| 種類 | 確認できること | 確認できないこと |
|---|---|---|
| 有理数・記号による正確な計算 | 記載された導出のもとでの有限恒等式・不等式 | 無限算術作用素との未証明の同定 |
| 浮動小数点・高精度診断 | 数値観察、反証候補 | 桁数を増やしただけでの符号認証 |
| 球・区間認証と解析評価 | 指定の有限不等式と、記載があれば無限の裾・結合の評価 | 全支持・全パラメータの一様正値性 |
| Lean証明 | 明示前提下の指定宣言 | 未形式化の解析前提、Weil判定、RH |

## 保存した計算の例 {#_4}

- [正確な有限模型](../../artifacts/experiments/scripts/falsify_models.py)：Fractionは正確、同じコードのDecimal積分は非認証。反証するのは提案された含意で、RHではありません。
- [小さなWeil行列](../../artifacts/experiments/scripts/groskin_independent_certificate.py)：独立構成・認証は $c=13,N=4$ の9次元行列。原典の401次元計算をここで独立再現してはいません。
- [半幅窓全体の認証](../../artifacts/experiments/scripts/window_half_certificate.py)：偶・奇の有限部分の区間認証と、無限の裾・結合の書面上評価を結合。支持 [−1/2,1/2] の結果であり、全支持ではありません。
- [別実装の照合](../../artifacts/experiments/scripts/window_half_crosscheck.py)：積分比較で指定有限成分を確認。主認証との重なりは監査で確認します。
- [高周波記号認証](../../artifacts/experiments/scripts/joint_symbol_certificate.py)：五つの固定窓の高周波下界。各有限部分や全Weil形式を認証するものではありません。
- [証明主張監査の有限修正](../../artifacts/experiments/scripts/desogus_safe_cut_repair.py)：指定の有限k範囲をArbで検査。実際の作用素の同定や解析的裾の欠落は修復しません。

主な半幅窓の義務と独立範囲は[認証監査](../../archive/audits/proofs/audits/window-half-certificate.md)・[独立監査](../../archive/audits/proofs/audits/window-half-independent.md)にあります。未検証・中断・NaNの記録は成功ではありません。大窓の中断スクリプトは試行の履歴として保存します。

共通親・速度履歴・階層の後続実験も、記録された精度と経路の有限診断です。全切断の収束、全行列のgap、微分次数に一様な定理は証明しません。解析結果と表・図の観察は別です。

Groskin原構成の比較とDesogusのTeX抽出検査は、除外した第三者資料を必要とします。補助スクリプトは単独再現としての実行を拒否します。旧原文保存検査も私的基準を必要とし、公開ツリーの検証器ではありません。不足を黙ってダウンロードで補いません。

## 形式化の範囲 {#_5}

[Leanの案内（原文）](../../artifacts/formal/lean/README.md)はLean 4.19.0と固定Mathlib版を記録します。[RhAudit.lean](../../artifacts/formal/lean/RhAudit.lean)の8宣言は、明示的極限・連続性のもとでの正値性、初等ブロック不等式、有限反例の係数、スカラーSchur同値です。[保存公理ログ](../../artifacts/formal/lean/verification/axioms.txt)には通常のLean論理公理があり、`sorryAx` はありません。

[ReturnLemma.lean](../../artifacts/research/one_prime/formal/ReturnLemma.lean)はスカラー成長の4宣言です。算術商、作用素ノルム、ゼータ零点定理は形式化していません。固定窓の解析的裾、特殊関数、巡回性、RH全体も未形式化です。

ツールチェーンとMathlibは同梱しません。再ビルドには配置を再構成し、`formal/lean` の保存ツールチェーンと対応表を使います。当時の指示には `lake build` と `lake env lean RhAudit.lean` があり、固定依存の取得は別の通信操作です。最新版へ更新した環境を当時のビルドと同一視しないでください。

## 巡回性と後続の有限空間更新 {#_6}

巡回性は偶微分族の偶L²稠密性の通常の解析的証明です。内部監査はFourier規約、指数モーメント、モーメント条件、直接一意性証明を確認します。有限空間の数値認証や条件数評価ではなく、Weil形式位相や全体捕捉の主張でもありません。

新しく再実行する場合は、版、公開資料ハッシュ、パラメータ、精度、出力、確認した解析前提を新たな証拠として記録します。過去の主張を上書きしたり、限定検査をRHの主張へ変えたりしません。

[Priority 2](tracks/19-finite-even-head-spanning.md)は階数の書面上議論、高精度診断、解析＋Arb認証を区別します。元の特異値・階数の認証は指定の二区間。物理GramのSVDには有限theta和と有限積分を用いるため診断のままです。元の実行は今回の公開検査で再実行したものではありません。
