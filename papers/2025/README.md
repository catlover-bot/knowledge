# Papers  2025

<details><summary>An Empirical Study on Commit Message Generation using LLMs via In-Context Learning</summary>

以下の論文は、LLM（大規模言語モデル）とIn-Context Learning（ICL）を用いたコミットメッセージ生成の能力を体系的に評価した経験的研究です。以下、主要な内容を整理してご紹介します。

---

## 背景と目的

* **コミットメッセージの重要性**
  開発者がバージョン管理システム（例：Git）にコード変更を登録する際、自然言語で簡潔に変更内容や意図を記述した「コミットメッセージ」は、ソフトウェアの保守性向上やコードレビューの効率化に不可欠である一方、多くのプロジェクトで質が低いメッセージが散見される（例：44%に品質問題）。
* **従来手法の課題**

  * ルール／テンプレートベースやIRベースの手法は限定的で意図を捉えにくい。
  * 学習ベース手法は大量のラベル付きデータや計算資源を要し、異プロジェクトへの一般化能力も限定的（性能が26.9～73.4%低下）。
* **本研究の狙い**
  LLMが事前学習時に大量のコミット–メッセージ対を含むことに着目し、追加の学習なしにプロンプト＋数例のデモンストレーション（ICL）でコミットメッセージ生成を行う場合の性能を評価。

---

## 研究デザイン

1. **研究課題（RQ）**

   * RQ1: プロンプト設計（Instruction／制約情報の有無）やデモ数／選択／並び順が性能に与える影響
   * RQ2: 最適設定下での各種LLMと最先端手法との比較（ベンチマーク：MCMD）
   * RQ3: LLMが失敗するケースの根本要因分析（200例をサンプリング）
2. **データセット**

   * **MCMD**: 従来から用いられる多言語ベンチマークセット
   * **MCMD-New**: 潜在的なデータ漏洩を防ぐために、新規リポジトリおよび同一リポジトリの最新コミットで構築
3. **手法**

   * プロンプトは「役割記述」「制約（要約文字数等）」の有無で4種
   * デモンストレーションの選択方法は「ランダム」と「類似度ベースの検索」
   * 評価モデル：GPT-3.5-Turbo、DeepSeek-V2-Chatなど主要LLM
   * 比較対象：CodeT5等をファインチューニングした先行モデル
4. **評価指標**

   * **客観的指標**: BLEU、ROUGEなど自動メトリクス
   * **主観的指標**: 人手アノテーションによる品質評価
   * さらに、LLMを用いた自動評価の信頼性も検証

---

## 主な結果

1. **RQ1: プロンプト／デモ設定の影響**

   * ゼロショットではプロンプト変更の影響が大きいが、少数ショットではデモンストレーション数で性能が安定（多すぎると逆効果）
   * 検索ベースのデモ選択がランダム選択より統計的に有意に高性能、順序はほぼ無影響
2. **RQ2: LLM vs. 先行モデル**

   * **GPT-3.5-Turbo** と **DeepSeek-V2-Chat** が最良性能を示し、全指標で他のLLMを上回る
   * MCMD-New（新データ）では、LLMは先行ベースラインを有意に上回り、一般化能力に優れる
   * MCMD（既存データ）でも、ファインチューニング済モデルと同等の性能を達成
   * 主観評価でもLLMが優位。特に、LLMによる自動評価が人手評価との相関が高く、信頼性が高いことを示唆
3. **RQ3: 失敗ケースの原因分析**

   * 主な要因は「文脈知識の不足」「不適切なデモンストレーション」「モデルの誤謬（hallucination）」
   * 高品質なデモとより高度なモデルの組み合わせで多くの失敗を是正可能と示唆

---

## 貢献と今後の方向性

* **貢献**

  1. ICLを用いたコミットメッセージ生成の包括的評価
  2. 設定要因（プロンプト／デモ）やLLMの比較を通じた知見
  3. 失敗原因の分析に基づく今後の研究指針
  4. コード・データセット公開による再現可能性の担保
* **将来の研究**

  * デモ選択の最適化手法の探究
  * 文脈情報（コミット履歴、Issueトラッカー情報等）の統合
  * より高度な自己評価・品質保証メカニズムの開発

---

本研究は、LLM本来の知識をチューニングなしで活用する新たなアプローチとして示唆に富み、特に汎化性能の高さや評価メトリクスの信頼性向上など、コミットメッセージ生成分野における今後の発展に大きく寄与するものと言えます。

</details>

<details><summary>Evaluating Pre-trained Large Language Models on Zero-Shot Prompts for Parallelization of Source Code</summary>

---

## 1. 論文情報

**タイトル**
Evaluating Pre-trained Large Language Models on Zero-Shot Prompts for Parallelization of Source Code
**著者**
Devansh Yadav, Shouvick Mondal（Indian Institute of Technology Gandhinagar） ([researchgate.net][1])

---

## 2. 背景と目的

* **並列化の重要性**
  科学技術計算などの分野では、多コア環境を活かすためコードの並列化が必須。手動での並列化は依存関係管理や同期機構の挿入が煩雑で、データレースやメモリアクセスエラーを避けるのが難しい。
* **従来ツールの扱い**
  Intel C Compiler（icc）は高度な最適化機能を備え、PolyBenchベンチマークなどで自動並列化を行えるが、適用可能範囲や得られる性能には限界がある。
* **LLMへの期待と課題**
  近年の大規模言語モデル（GPT-3.5, GPT-4o, Claude など）はコード生成能力が高いが、ゼロショットの設定で並列化タスクを正確かつ安全にこなせるかは未検証。本研究では、プロンプトや追加学習なしに「逐次 C コード → OpenMP 並列コード」変換がどこまで実用的かを評価する ([researchgate.net][1])。

---

## 3. 実験デザイン

1. **対象モデル**
   23 種類の事前学習済み LLM をゼロショットで評価。
2. **ベースライン**
   Intel C Compiler（icc）による auto-parallelization。
3. **ベンチマーク**
   PolyBench C ベンチマーク 30 カーネルを使用し、各モデルで合計667 バージョンの並列化コードを生成。
4. **評価指標**

   * *Speedup*：並列化後コードの実行速度を計測し、icc 並列版との比較
   * *正当性チェック*：コンパイル可否、Intel Inspector を用いたデータレースやメモリエラーの検出を通じて、信頼できる並列化実装のみを分析対象にフィルタリング ([researchgate.net][1])。

---

## 4. 主な結果

* **性能（Speedup）の分布**

  * 全テストケースのうち、26.66% が icc 並列版（平均 Speedup 1.08×）を上回る速度改善を実現 ([researchgate.net][1])。
  * 最優秀モデルは最大 7.5× の Speedup を達成し、十数年にわたるコンパイラ技術を凌駕するケースも確認。
* **エラー率**

  * 生成コードのうち約 10–20% にコンパイルエラーやデータレースが含まれ、LLM ごとにばらつきあり。
  * GPT-4o や Claude-3-Haiku は比較的低いエラー率かつ高い Speedup を示した一方、GPT-3.5 Turbo はデータレースやメモリ問題が多数発生 ([researchgate.net][1])。
* **典型的失敗パターン（RQ1）**

  * ループ変数のスコープ指定ミスによる共有変数への同時書き込み
  * Reduction ループの原子操作不足
  * イテレーション依存の誤判断による並列化不可ループへの OpenMP 指令挿入ミス

---

## 5. 考察と今後の展望

1. **LLM のポテンシャル**
   ゼロショットでも一定の並列化能力を持ち、特に最先端モデルは icc を上回る場面もある。
2. **品質保証の必要性**
   依然としてコンパイルエラーやデータレースが散見されるため、自動生成後の静的／動的検証は必須。
3. **研究課題**

   * プロンプト設計（Chain-of-Thought やフィードバックループ）による信頼性向上
   * モデルのファインチューニングやドメイン適応によるエラー削減
   * 生成コード検証を含むエンド-ツー-エンドの自動並列化パイプライン構築

---

**まとめ**
本研究は、長年にわたり洗練されてきたコンパイラ技術と、最先端 LLM の“ゼロショット”並列化能力を初めて体系的に比較した点で意義深く、LLM ベースのコード最適化ツール開発に向けた新たな可能性と課題を明らかにしています。

[1]: https://www.researchgate.net/profile/Shouvick-Mondal/publication/388350808_Evaluating_Pre-trained_Large_Language_Models-on-Zero-Shot-Prompts-for-Parallelization-of-Source-Code/links/679378a096e7fb48b99bb04e/Evaluating-Pre-trained-Large-Language-Models-on-Zero-Shot-Prompts-for-Parallelization-of-Source-Code.pdf "Evaluating Pre-trained Large Language Models on Zero Shot Prompts for Parallelization of Source Code"

</details>

<details><summary>CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation</summary>

[参考](https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CAD-Llama_Leveraging_Large_Language_Models_for_Computer-Aided_Design_Parametric_3D_CVPR_2025_paper.pdf)  

以下、論文「CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation」（CVPR 2025）について詳しくまとめます。

## 概要

CAD-Llamaは、大規模言語モデル（LLM）をパラメトリック3D CADモデリングに適用するためのフレームワークです。まずCAD設計履歴をPythonライクなコード形式（Structured Parametric CAD Code, SPCC）に変換し、階層的なテキスト注釈を付与します。その後、SPCCコーパスを用いたアダプティブ事前学習と、CAD特化の命令チューニングを順に行うことで、LLMに空間知識と設計意図の理解能力を獲得させます ([openaccess.thecvf.com][1])。

## 背景と課題

従来のCAD生成モデルは、点群やメッシュなどジオメトリ入力をCADコマンドに変換する手法が主流でしたが、LLMによる直接的なパラメトリックシーケンス生成は未踏の領域でした。また、LLMは自然言語やコード生成には長けていますが、CADコマンドに含まれる空間構造や設計意図を自明には扱えません ([openaccess.thecvf.com][1])。

## 手法

1. **階層注釈パイプライン**

   * 各CADモデルをコンポーネントごとに分解し、3Dレンダリング画像と2DスケッチをVLM（GPT-4o）へ入力して詳細説明を生成（第1段階）。
   * 次に全体像と部品間の関係性を捉えた抽象／詳細説明を生成し、各部品に短い識別名を付与（第2段階）。
   * これらをSPCC形式のコードに組み込み、階層構造を反映させた注釈付きデータを得る ([openaccess.thecvf.com][1])。

2. **アダプティブ事前学習**

   * 得られたSPCCコーパスを用いて、DeepSpeed＋Flash-Attention環境下でLLMをフルファインチューニングし、CADコマンド列の生成能力を獲得させる ([openaccess.thecvf.com][1])。

3. **命令チューニング**

   * LoRAによるパラメータ効率的なチューニングで、テキスト→CAD生成や部品追加・削除など複数の下流タスクに対応可能な指示モデルへと最適化する ([openaccess.thecvf.com][1])。

## 実験設定とベースライン

* **無条件生成**：DeepCAD, SkexGen, HNC-CAD
* **テキスト→CAD**：Text2CAD, CAD-Translator
* **下流タスク**：GPT-4, GPT-3.5, LLaMA3-8B, Mistral-7B
* 評価指標には、Coverage (COV), MMD, JSD, Success Ratio, Noveltyなどを使用 ([openaccess.thecvf.com][1])。

## 実験結果

* **無条件生成**：CAD-LlamaはJSDやMMDで最良、Success Ratioでは99.90%を達成し、既存手法を上回る安定性と分布適合性を示した ([openaccess.thecvf.com][1])。
* **テキスト→CADタスク**：ACCT（生成命令の正確性）が84.72%と、Text2CAD（69.91%）やCAD-Translator（70.36%）を大きくリード。MCD, MMD, JSDも大幅改善 ([openaccess.thecvf.com][1])。
* **CAD関連下流タスク**：キャプション生成やコマンド／パラメータ追加・削除タスクで平均63.58%を獲得し、GPT-4比で約15.7ポイントの改善。特に構造化注釈による理解力向上が顕著 ([openaccess.thecvf.com][1])。
* **アブレーション**：SPCC（階層注釈＋コード形式）が、単一説明やシーケンス形式に対し20～40%近い精度向上を実証し、階層化とコード表現の効果を裏付けた ([openaccess.thecvf.com][1])。

## 貢献と今後の展望

1. LLMの生成的事前学習をCADコマンド生成へ拡張する新パラダイムを提案。
2. VLMを用いた2段階階層注釈パイプラインで、詳細かつ構造化されたSPCCフォーマットを構築。
3. 多タスク命令チューニングにより、設計補完から編集操作まで幅広いCADタスクに対応。
4. 将来的には3D拡張や商用CADツール連携、さらに大規模モデルへの適用により、LLM駆動CAD生成の可能性が一層拡大すると期待される ([openaccess.thecvf.com][1])。

[1]: https://openaccess.thecvf.com/content/CVPR2025/papers/Li_CAD-Llama_Leveraging_Large_Language_Models_for_Computer-Aided_Design_Parametric_3D_CVPR_2025_paper.pdf "CAD-Llama: Leveraging Large Language Models for Computer-Aided Design Parametric 3D Model Generation"

</details>
