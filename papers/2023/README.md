# Papers  2023

<details><summary>TRIGO: Benchmarking Formal Mathematical Proof Reduction for Generative Language Models</summary>

[参考](https://aclanthology.org/2023.emnlp-main.711.pdf)  

## 背景と問題提起
- Automated Theorem Proving(ATP)は、結論から公理まで形式的に推論を検証できるため、言語モデルの「厳密な」推論能力を評価するのに適している
- 既存ベンチマーク（LeanStep,MiniF2Fなど）は主に記号推論に焦点を当て、複雑な数値結合操作（項のグループ化、因数分解、同値変形など）を含まない
- 特に三角関数式の簡約は、数値と式構造の両方を深く理解しなければならず、現在の生成モデルにとって大きな挑戦となる

## TRIGOタスクの定義
- **目標**：与えられた三角関数式をLeanの形式言語を入力し、ステップごとの証明（tactic）を通じて式を簡約する。

例：
```lean
lemma Trigo_0 : sin(π/3) + 2 * cos(π/12) * 2 - cos(π/2) = sqrt(3) + 1 := 
begin
  rw cos_pi_div_two,
  have h: cos (π/12) ^ 2 = cos (π/6) / 2 + 1 / 2,
  ring_exp,
  ...,
end
```
のように、半角公式の適用や定数変形を正しく選択する必要がある。

## データセット構築
1. **TRIGO-real**：
   - 高校の演習問題・試験問題集（"tiku"など）から三角関数式の問題と解答を収集し、427問を手動でステップ注釈
2. **TRIGO-web**：
   - ウェブ上の類似問題をさらに453問収集し、テストセットとして利用
3. **TRIGO-gen**：
   - 上記の手動注釈をもとにLean-Gymベースの自動生成プログラムで、証明長や数値規模を制御した人工サンプルを生成
4. **注釈ツール**：
   - Sympyを用いて85種類の変形ルール（半角・加法公式など）にマッチさせつつ、ステップごとの正当性をチェック

## 評価実験
- **モデル比較**：GPT-4をはじめ、各種生成モデルにTRIGOタスクを解かせる
- **失敗例**：GPT-4は一度は正しい式変形を示すものの、存在しないtactic名を生成したり、誤ったsubgoalで完了と判断したりといった形式検証の落とし穴に陥る
- **難易度設定**：実データと自動生成データを組み合わせたスプリットで、モデルの分布外一般化能力を詳しく分析

## 主な結果と意義
- TRIGOは「数値操作+形式的証明」という二重のチャレンジを伴い、現状の最先端LLM（GPT-4など）でさえ高いパス率を達成できないことを示した
- 複雑な数値結合・式変形能力が、今後のATPにおける重要な研究テーマであることを提起
- データセット・注釈ツール・自動生成コードを公開し、形式的数学推論コミュニティへの貢献とベンチマークとしての展開を促進
</details>

<details><summary>Introduction to Mathematical Language Processing: Informal Proofs, Word Problems, and Supporting Tasks</summary>

[参考](https://aclanthology.org/2023.tacl-1.66.pdf)  

## 背景と目的
- **数学的言語処理（Mathematical Language Processing;MLP）**は、数学的要素（式、変数、定理など）と自然言語の両方を扱いながら、「数学的に厳密」かつ「説明可能」な解答を生成することを目指す
- 従来、数学の自動化には形式的証明システムを用いた厳密推論が必要でしたが、近年のTransformer系モデルやLLMは豊富な知識と推論能力を示した
- 本論文は、MLPを構成する五つ戦略的サブタスクを整理・分析し、各分野の手法、データセット、評価指標、現状の限界、研究動向、今後の展望を俯瞰的にレビューすることを目的としている

## 代表的タスクの分類
論文は、以下の五つを「代表的タスク」として取り上げ、推論の＜抽象的⇄生成的＞スペクトル上に配置する
1. **Identifier-Definition Extraction**  
   変数や記号（例：ψ(x)）とそれに対応する自然言語での定義（例：wavevector）を抽出するタスク
2. Formula Retrieval  
   LaTexやMathMLで表現された数式検索。クエリ数式に類似する候補式をランキングする
3. Natural Language Premise Selection (NLPS)  
   定理証明の前提となる文を、大量のテキストから選び出す情報検索タスク
4. Math Word Problem Solving (MWP)  
   「文章題」を解いて答えを算出する。解答には識別子と定義抽出、前提選択も含まれる
5. Informal Theorem Proving  
   型式証明ではなく、自然言語＋数式によるステップ形式の「非形式的証明」を生成し、論理的に結論へ至る過程を表現する

## 主な手法と進化
- **抽出的タスク**（identifier‑definition extraction, formula retrieval）は、従来は手工学的特徴＋統計的モデル（CRF,SVM）から始まり、近年はBERT系の細微調整やグラフニューラルネットワークによるエンコーディングへと移行
- **生成タスク**（MWP, informal proving）では、GPT系LLMや専用のシーケンスモデルを用い、入出力のペアを大規模に学習・生成させる手法が主流に
- **中間的タスク**（premise selection）は、グラフ構造＋自己注意機構を組み合わせたモデルや、LLMへの直接プロンプト/微調整アプローチが精度を伸ばしている

## 現在の限界と今後の課題
- **データ多様性の不足**：多くのタスクは特定ドメイン（arXiv論文、教科書）に偏っており、汎用性の高いデータセットが不足
- **スコープと評価の不統一**：同じタスク名でも定義や評価志保湯が研究ごとに異なるため、直接比較が困難
- **形式⇄非形式ギャップ**：形式的証明システムと自然言語モデル間での"autoformalization"手法がまだ発展途上
- **複合タスクの必要性**：現実的な問題解決には、識別子抽出→前提選択→証明生成の連鎖的処理が必須であり、単一タスク最適化からの脱却が求められる

## まとめと展望
- MLPは「抽出から生成へ」、さらに「非形式⇄形式」ブリッジを行う潮流にあり、各分野の手法は着実に進化中
- 今後は、統一ベンチマーク・マルチモーダル手法（テキスト＋画像＋数式）・人間とAIの混合推論プロセスなど、より実用的で堅牢なシステム開発に注力が移ると予想される
</details>

<details><summary>Revisiting Learning-based Commit Message Generation</summary>

以下の論文は、ICSE 2023 で発表された学習ベースのコミットメッセージ生成技術を「パターン」の観点から再評価した研究です。

---

## 1. 論文情報

**タイトル**: Revisiting Learning-based Commit Message Generation
**著者**: Jinhao Dong, Yiling Lou, Dan Hao, Lin Tan ([cs.purdue.edu][1])
**会議**: 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) ([cs.purdue.edu][1])

---

## 2. 研究背景

* コミットメッセージはコード変更の意図や理由を示し、ソフトウェア保守やバグ解析、自動リリースノート生成など多くのタスクで重要な役割を果たします。しかし、多くのプロジェクトで低品質あるいは空のメッセージが散見され、約14％が空メッセージという報告もあります ([cs.purdue.edu][1])。
* これまでに、ルールベース、情報検索ベース、学習ベースといった自動生成手法が提案されており、特に深層学習を用いた学習ベース技術はBLEUなどのNLP指標で高評価を得ていますが、生成メッセージの「中身」がどのようなものかは明らかでありませんでした ([cs.purdue.edu][1])。

---

## 3. 研究目的と研究質問

本研究の狙いは、学習ベース手法が「どのような形式のコミットメッセージを生成しているか」を定量的・定性的に明らかにすることです。

* **RQ1**: 既存手法がどのようなパターンのメッセージを生成しているか？
* **RQ2–RQ4**: データセットの構成、入力表現、モデル構成要素が生成パターンにどのように影響するか？ ([cs.purdue.edu][1])

---

## 4. 手法概要

1. **パターン抽出**

   * まず、既存の学習ベース手法（NMT, PtrGN, CODIS, CoreGen, FIRA）で生成されたメッセージを対象に、Sequential Pattern Mining (MaxSP) を適用し頻出サブシーケンスを抽出。
   * そこから手動マージを経て「Addition」「Removal」「Fix」「Avoidance」の4大パターンにまとめ上げています ([cs.purdue.edu][1])。
2. **パターン比率の測定**

   * 生成メッセージとゴールド（実際のコミットメッセージ）の双方でパターンに該当する割合（Pattern Ratio）を算出。
3. **要因分析**

   * RQ2: 学習データ中のパターン比率を変化させて生成結果を比較
   * RQ3: 入力を差分マーク（“+”“-”“ ”）のみに変えた場合の性能評価
   * RQ4: Attention, Copy, Anonymization といったモデル要素の有無によるパターン生成への影響調査 ([cs.purdue.edu][1])。

---

## 5. 主な発見

* **単純パターン偏重**
  生成メッセージの約90％が「Addition/Removal/Fix/Avoidance」といった単純パターンに該当し、実際のメッセージ（約50％）よりも著しく高い割合を示す ([cs.purdue.edu][1])。
* **差分マークのみで十分**
  入力を“+”/“-”/“ ”だけに簡素化しても、元のコード構造や意味情報を含む場合とほぼ同等のパターン比率を維持。モデルはトークンの差分マークを主要な手がかりとして利用していることを示唆します ([cs.purdue.edu][1])。
* **データセットの影響**
  訓練データ中のパターン比率が高いほど、生成結果でも同様の比率が増加。一方、非パターンデータを増やしても非パターン生成率はほとんど改善せず、非パターン生成がモデルにとって難易度が高いことが示されました ([cs.purdue.edu][1])。
* **モデル要素の寄与**
  Attention や Copy 機構のON/OFFでパターン比率に違いが見られ、特に変更行マークへの重点度合いがモデル挙動に大きく影響することが判明しました ([cs.purdue.edu][1])。

---

## 6. 貢献と示唆

1. **パターン視点の評価指標提案**
   従来のBLEU等の集約スコアに加え、生成メッセージの構造的な特徴を捉える定量指標を提示。
2. **学習ベース手法の限界露呈**
   モデルは差分マークに依存しすぎており、構文／意味情報を十分活用していない実態を明らかにしました。
3. **改善の方向性提示**
   非パターン／複雑パターン生成のためには、差分以外のコード情報や文脈理解を強化する必要があることを示唆しています ([cs.purdue.edu][1])。

---

## 7. 今後の展望

* 差分以外の抽象構文木（AST）や静的解析情報を活用した多様なパターン生成手法の検討
* 非パターン事例に対するデータ収集・拡張によるモデル学習の強化
* 実開発ワークフローへの統合評価（人間による可読性・有用性評価など）

本論文は、学習ベースのコミットメッセージ生成研究に対して新たな評価軸を提供し、今後の研究方向を具体的に示した重要な知見を与えています。

[1]: https://www.cs.purdue.edu/homes/lintan/publications/commit-icse23.pdf?utm_source=chatgpt.com "Revisiting Learning-Based Commit Message Generation"

</details>

<details><summary>Modeling Collaborative Dialogue in Minecraft with Action-Utterance Model</summary>

[参考](https://aclanthology.org/2023.ijcnlp-srw.10.pdf)  

---

## 1. 研究背景と目的

近年のニューラル対話システムは、人間と協調してタスクを完遂する能力が求められています。しかし、仮想環境上での共同作業研究では、行動（action）生成と発話（utterance）生成が別々に扱われることが多く、実際の協調設定では両者を自律的に判断・実行できるモデルが必要です。本研究では、Minecraft上の共同作業データセットを用い、次に「行動を行うか」「発話するか」を自律的に決定し、かつ内容を生成できる**Action-Utterance Model**を提案します ([aclanthology.org][1]).

---

## 2. データセットとタスク定義

* **Collaborative Garden Task Corpus**（Ichikawa & Higashinaka, 2022）

  * 1,092対話、合計31,416発話、657,693ブロック操作を記録。対話は日本語で行われ、10×10×4領域内で17種類のブロックを用いたガーデン作成タスクを含む ([aclanthology.org][1]).
* **Next Action-Utterance Generation Task**

  * あるターンtにおいて、過去対話・行動履歴 $H_t$、ワールドステート $W_t$、アバター位置・向きを入力とし、次のアクションタイプ（UTT／BLOCK／SKIP／FINISH）と、その内容（発話テキスト $u_t$ またはブロック操作集合 $b_t$）を予測する ([aclanthology.org][1]).

---

## 3. 提案モデル：Action-Utterance Model

**全体構成**（Figure 2）

1. **テキスト情報**：過去 $N=10$ ターン分の〈発話＋状態変化ΔW＋ワールドステートW〉をトークナイズ
2. **非言語情報埋め込み**

   * Voxelデータ用 Flattened Voxel Block Encoder
   * 位置情報（GPS）用 MLP
   * 向き情報（Compass）用 MLP
     でそれぞれ「1トークン相当」のベクトルに変換し、テキスト埋め込みと連結 ([aclanthology.org][1]).
3. **LLM デコーダ**：Transformerデコーダ（OpenCALM-Large, 830Mパラメータ）をLoRA微調整し、次アクションタイプ＋内容を生成
4. **出力**：最初にタイプトークン、続いて UTT なら発話テキスト、BLOCK なら最大4件のブロック操作を出力 ([aclanthology.org][1]).

---

## 4. 実験設定

* **データ分割**：1,092対話を train:980 / val:56 / test:56 にランダム分割 ([aclanthology.org][1]).
* **比較モデル**

  * **行動タイプ分類**：Random, Majority
  * **行動生成**：Random feasible operations
  * **発話生成**：UG (Utterance-only Transformer)
* **学習**：LoRA による MLE 最適化、検証損失最小チェックポイントを利用 ([aclanthology.org][1]).
* **評価指標**

  * 行動タイプ分類：Accuracy, Macro-F1
  * 行動生成：Jaccard (全属性／タイプのみ)
  * 発話生成：BLEU-1/2, Distinct-1 ([aclanthology.org][1]).

---

## 5. 実験結果

### 5.1 行動タイプ分類

| モデル                                                                         | Accuracy  | Macro-F1 |
| --------------------------------------------------------------------------- | --------- | -------- |
| Random                                                                      | 0.24      | 0.19     |
| Majority                                                                    | 0.61      | 0.19     |
| **Action-Utterance**                                                        | **0.81**★ | **0.67** |
| ★ は Random/Majority と比較し McNemar検定で $p<0.05$ の有意改善 ([aclanthology.org][1]). |           |          |

### 5.2 行動生成

* Jaccard全属性: 0.34 → 事後フィルタや他手法比較で大幅改善
* Jaccardタイプのみ: 0.72
  （詳しい数値は論文 Table 2 を参照）

### 5.3 発話生成

* BLEU-1: 0.18
* BLEU-2: 0.07
* Distinct-1: 0.42
  発話専用モデル UG を上回る多様性と正確性を実現 ([aclanthology.org][1]).

---

## 6. 考察

* **自律判断**：Contextに基づく行動 vs 発話の選択が高精度
* **依存関係の難しさ**：最後の行動と無関係な次行動生成は依然課題
* **非言語情報の効果**：ワールドステート・位置情報埋め込みが性能向上に寄与

---

## 7. 結論と今後の展望

Action-Utterance Model は、Minecraftの共同対話タスクにおいて「行動か発話か」の判断とその内容生成を\*\* unified\*\*に行う初のモデルとして、高性能を示しました。今後は以下の課題があります：

* 行動選択のさらなる一般化
* 長期的プランニングとの統合
* リアルタイムユーザ実験による評価

以上が本論文の詳細なまとめです。さらに深い技術的検討や実装支援が必要であればお知らせください。

[1]: https://aclanthology.org/2023.ijcnlp-srw.10.pdf "Modeling Collaborative Dialogue in Minecraft with Action-Utterance Model"

</details>

<details><summary>People Make Better Edits: Measuring the Efficacy of LLM-Generated
 Counterfactually Augmented Data for Harmful Language Detection</summary>

[参考](https://www.google.com/url?client=internal-element-cse&cx=000299513257099441687:fkkgoogvtaw&q=https://aclanthology.org/2023.emnlp-main.649.pdf&sa=U&ved=2ahUKEwiT4KKJ6PeNAxWtzTQHHZMeCxsQFnoECAMQAg&usg=AOvVaw1CnsQzsjtbH1fx1N1x5aUq&fexp=72986057,72986056)  

## 研究背景と目的
近年、性差別的・ヘイトスピーチ的な発言の検出モデルは、訓練データ中の「スプリアスな特徴（例えば特定の単語の有無）」に依存しやすく、ドメイン外（OOD）データへの一般化が不足しがちである。  
**Counterfactually Augmented Data(CAD)**は、既存の文例を「ラベルが反転するような最小限の変更」加えて拡張する手法で、モデルが本質的なタスクに注目する助けとなる。しかし、手動生成は労力とコストが大きいため、LLMを用いて自動生成したCADが、手動CADに匹敵する効果をもたらすかを検証するのが本研究の目的である。  

## 2. 手法概要

1. **CAD生成**

   * **手動CAD**: 先行研究（Samory et al., 2021; Vidgen et al., 2021）で作成されたものを再利用
   * **自動CAD**:

     * **Polyjuice**（GPT‑2ベース, 制御コード8種）
     * **ChatGPT**（GPT‑3.5ベース，OpenAI API経由）
     * **Flan‑T5**（Instruction‑tuned T5ファミリー）
       各方式で生成した複数のCADからランダムに1つを選択し，元文とペアとして使用 。

2. **モデルアーキテクチャ**

   * **RoBERTa**, **Flan‑T5**, **SVM + FastText** を微調整
   * ベースラインとして，ChatGPT／Flan‑T5のfew-shot分類（FSGPT, FSFT）およびPerspective API（PTox）も評価 。

3. **評価指標**

   * **マクロF1**を主指標とし，インドメイン（ID）と複数のOODテストセット（性差別検出で3～4種類，ヘイトスピーチ検出で5種類）＋ヘイトチェック（HC）で比較 。

---

## 3. 実験設定

* **訓練データ構成**: オリジナル文とCAD（50:50または25:75）の割合でサンプリングし，各CAD方式ごとに同等サイズの訓練セットを構築
* **データ難易度解析**: V-Informationの点ごとの拡張である**Pointwise V-Information (PVI)** を用い，各CADインスタンスの「学習しやすさ」を定量化し，CAD特性（編集距離，意味的類似度，編集タイプなど）との関連を解析 。

---

## 4. 主な結果と考察

1. **OOD性能の比較（RQ1）**

   * **手動CAD**を含むモデル（mCAD）は，ID性能は低いものの，ほとんどすべてのOODデータセットで最大のマクロF1を達成
   * \*\*ChatGPT CAD（aCADGPT）\*\*が自動CAD中で最も効果的であり，手動CADにかなり肉薄
   * **Polyjuice, Flan‑T5 CAD**（aCADPJ, aCADFT）は，変更が不十分であるためOOD性能が低い
   * \*\*手動＋自動CAD混合（amCAD）\*\*は性差別検出で最高のOOD性能を示す&#x20;
   * Few‑shot ChatGPT（FSGPT）も競合的な性能を示すものの，訓練データとのデータ重複の影響に注意が必要 。

2. **CAD特性の分析（RQ2）**

   * **編集距離**: Polyjuice/Flan‑T5は平均2トークン程度と小さすぎ，ChatGPTは10トークン以上と大きすぎ，手動は中間
   * **意味的類似度**（SBERT）: Polyjuice/Flan‑T5は0.9前後（高すぎ），ChatGPTは0.67（手動CADに近い）
   * **編集タイプ**: 性差別では性別語の削除，ヘイトではアイデンティティ語の編集が重要
   * **PVI解析**: CADを訓練に含めるとOODデータの平均PVIが負から正に向上し，学習しやすさが改善（性差別: −0.05→0.10, ヘイト: −0.19→0.17） 。
     → 自動CADは「ラベルを反転させるだけの十分な変更」がされていないケースが多く，ラベル誤りを誘発しやすい。

---

## 5. 貢献と示唆

* **手動CADが依然最も効果的**だが，**ChatGPT CADが次点**を占め，完全自動化の可能性を示唆
* 自動CADを活用するには，**自動生成→人手によるラベル検証**のハイブリッド運用が望ましい
* CAD特性の定量分析により，「編集距離」と「意味的乖離」がOOG性能向上に与える影響を明らかに
* 提案モデル・生成データ一式はGitHubで公開中: [https://github.com/Indiiigo/automatedCAD](https://github.com/Indiiigo/automatedCAD)&#x20;

---

</details>

<details><summary>沈黙の認識</summary>

以下、この論文 “The perception of silence” (PNAS, 2023) について、セクションごとに詳しく解説します。

---

## 論文情報

* **タイトル**: The perception of silence
* **著者**: Rui Zhe Goh, Ian B. Phillips, Chaz Firestone
* **所属**: Johns Hopkins University（Department of Psychological and Brain Sciences & Department of Philosophy）
* **刊行誌**: Proceedings of the National Academy of Sciences (PNAS), Vol. 120, No. 29, e2301463120
* **公開日**: 2023年7月10日（オンライン公開）／2023年7月18日（印刷版） ([PubMed][1], [国立科学アカデミー行動科学誌][2])

---

## 1. 研究背景

人間の聴覚は通常「音」を捉える感覚として理解されますが、日常生活では「沈黙」の経験──例えば耳を澄ませたときの一瞬の静寂や音楽終了後の余韻──もあります。
哲学・認知科学の分野では、「沈黙を知覚するのか（perceptual）、それともただ不在を判断するのか（cognitive）」をめぐり長年の論争があります。しかし、これまで実験的に沈黙が“本当に”知覚されるかを直接検証した研究はほとんどありませんでした ([PubMed][1], [EurekAlert!][3])。

---

## 2. 研究目的

本研究では、聴覚イベントの表象を示す「時間歪みを伴う聴覚錯覚」（例: one-is-more illusion）に着目し、

> **“沈黙が音と同様に錯覚を引き起こすか”**
> を実験的に検証することで、沈黙の知覚性（perceptual status）を問います ([PubMed][1], [EurekAlert!][3])。

---

## 3. 実験方法

1. **沈黙ベースの錯覚（Silence Illusions）の設計**

   * 代表的な音ベースの錯覚を、音の代わりに「無音区間（silence）」へ置き換え。
   * 例：

     * 「one-is-more illusion」 → 「one-silence-is-more illusion」
     * 2つの短い無音区間（合計長さ一定） vs. 1つの長い無音区間を比較。
2. **参加者**: 合計約1,000名の被験者をオンライン実験で募集。
3. **手続き**:

   * 忙しい飲食店や駅の雑踏をシミュレートしたサウンドスケープ中で、音が一瞬途切れる「無音区間」を提示。
   * その後、被験者に「長い無音 vs. 2つの短い無音、どちらが長く感じるか」を回答させる。 ([EurekAlert!][3])。

---

## 4. 結果

* **錯覚の再現性**:

  * 音ベースと同様に、「one long silence」を「two short silences」よりも長く感じるという錯覚が確認された。
  * 他の複数の錯覚実験でも、音版と無音版でほぼ同一の結果を示し、統計的に有意な時間歪みが観察された。
* **解釈**:

  * これらは「沈黙が単なる不在ではなく、聴覚的イベントとして処理されうる」ことを示唆する。 ([EurekAlert!][3])。

---

## 5. 考察と意義

* **理論的示唆**:

  * 従来の “音のみが聴覚対象” という見解に対し、「何もない状態（silence）も“聞く”対象となり得る」という新たな視点を提供。
* **方法論的貢献**:

  * 無音版聴覚錯覚という汎用的手法を提案し、「欠如の知覚（perception of absence）」研究へ応用可能。
* **今後の展望**:

  * 音に先行しない沈黙の知覚程度、さらには視覚的消失現象（visual disappearance）など他の感覚欠如にも手法を拡張する計画。 ([EurekAlert!][3])。

---

以上のように，本研究は実験的証拠をもって沈黙の知覚性を示し，「聞く」という行為の概念を再定義する画期的な成果を挙げています。さらに詳しい統計解析や追加実験デザインに関する質問などがあれば、お気軽にお知らせください。

[1]: https://pubmed.ncbi.nlm.nih.gov/37428927/?utm_source=chatgpt.com "The perception of silence - PubMed"
[2]: https://www.pnas.org/doi/10.1073/pnas.2301463120?utm_source=chatgpt.com "The perception of silence - PNAS"
[3]: https://www.eurekalert.org/news-releases/994869 "The sound of silence? Researchers prove people hear it | EurekAlert!"

</details>
