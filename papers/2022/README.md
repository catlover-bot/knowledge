# Papers  2022

<details><summary>Fine-tuning gpt-2 to patch programs, is it worth it?.</summary>

- [参考](https://real.mtak.hu/150350/1/Lajko-ISSQ2022.pdf)
    > GPT-2が、コードやプログラムにも適用可能かを調査している。そのために、著者たちはコードの「パッチ」をあてる、すなわちプログラムのバグ修正や機能改善のためにモデルを利用する方法を考えた。  
    > この研究では、プログラムに関連するデータセットを使って、GPT-2をファインチューニングし、コードの修正に活用できるかを試行した。  
    > 実験のプロセスでは、一般的なプログラムエラーやバグを含むデータセットを集め、それを元にGPT-2にファインチューニングを行った。次いで、ファインチューニングされたモデルがコードのパッチを生成できるか、あるいはどの程度効果的にバグを修正できるかをテストした。  
    > 結果として、ファインチューニングされたGPT-2は、ある程度のプログラム修正を自動で生成できることが確認されたが、すべてのケースで最適な解決策を提案するわけではないことも明らかになった。つまり、GPT-2は特定のシンプルな問題に対するアプローチとしては有用であるものの、より複雑なバグ修正には限界があることが示唆される。さらに、研究はGPT-2のサイズやファインチューニングに使ったデータセットの影響についても考察している。より大きなモデルや多様で質の高いデータセットを使用した場合、パフォーマンス向上の可能性がある。  
    > 結論として、GPT-2をファインチューニングしてプログラム修正に利用することは一定の価値があるものの、現状では補助的なツールとしての活用が妥当であり、この技術のさらなる進化が必要とされている。  
</details>

<details><summary>RACE: Retrieval-Augmented Commit Message Generation</summary>

以下の論文は、EMNLP 2022（2022年12月開催）で発表された、差分（diff）からコミットメッセージを生成する際に「類似コミットの再利用」を導入したモデル「RACE」を提案する研究です。

---

## 論文情報

* **タイトル**: RACE: Retrieval-Augmented Commit Message Generation
* **著者**: Ensheng Shi, Yanlin Wang, Wenchao Gu, Lun Du, Hongyu Zhang, Shi Han, Dongmei Zhang, Hongbin Sun
* **会議**: The 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022) ([aclanthology.org][1], [aclanthology.org][2])
* **DOI**: 10.18653/v1/2022.emnlp-main.372

---

## 背景

従来の学習ベース（Seq2Seq）コミットメッセージ生成モデルは、学習データ中の特徴を拾うだけで、似た変更が繰り返されるリポジトリでは冗長・反復的なメッセージを生成しがちでした。そこで本論文では、既存のリポジトリから「類似のコミット＋メッセージ」ペアを検索し、それを“お手本（exemplar）”として組み込むことで、より正確かつ多様なメッセージを生成する枠組みを提案しています ([aclanthology.org][1])。

---

## 手法概要

1. **Retrieve（検索）**

   * 現在のコード差分（diff）に最も類似すると推定される過去コミットを、埋め込み検索とBM25を組み合わせたハイブリッド方式でリトリーブ。
2. **Exemplar Guider（お手本案内器）**

   * リトリーブしたコミットと現差分との意味的類似度を学習的に評価し、高いものほど生成時の参照度を高めるガイディング機構を導入。
3. **Generate（生成）**

   * オリジナルの入力（diff）と選ばれたお手本メッセージを連結して、Transformerベースのデコーダに与え、最終的なコミットメッセージを生成。

---

## 実験と主な成果

* **データセット**：Java, JavaScript, Python, Ruby, PHP の5言語にまたがる大規模リポジトリから抽出した約50万件の〈diff, message〉ペア
* **ベースライン**：NMTGen, CommitBERT, CodeT5-small, CodeT5-base など
* **評価指標**：BLEU スコアおよび人的評価
* **結果**：

  * BLEU では最良のベースライン（NMTGen）比で平均43%の改善を達成
  * CommitBERT, CodeT5-small, CodeT5-base に対してもそれぞれ11%、15%、16%の相対向上を確認
  * 人的評価でも、「意図の正確性」「情報の網羅性」で高い評価を獲得 ([aclanthology.org][2])

---

## 貢献と示唆

1. **Retrieval-Augmentation の有効性**
   リトリーブした類似コミットを例示として活用するだけで、モデル単体よりも大幅に性能向上が可能であることを実証。
2. **Exemplar Guider の導入**
   単純なコピーメカニズムではなく、例示の適合度を動的に学習し制御する手法を示した点が新規。
3. **多言語対応**
   5つのプログラミング言語にまたがるデータで評価し、汎用性を確認。

今後は、さらに多様なリポジトリ構造への適用や、動的・オンライン学習によるリトリーバルモデルの更新などが期待されます。

[1]: https://aclanthology.org/2022.emnlp-main.372/?utm_source=chatgpt.com "RACE: Retrieval-augmented Commit Message Generation"
[2]: https://aclanthology.org/2022.emnlp-main.372.pdf?utm_source=chatgpt.com "[PDF] RACE: Retrieval-Augmented Commit Message Generation"

</details>
