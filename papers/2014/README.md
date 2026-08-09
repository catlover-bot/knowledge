# Papers  2014

<details><summary>On Automatically Generating Commit Messages via Summarization of Source Code Changes</summary>

以下の論文は、ソースコードの変更セットから自動的にコミットメッセージを生成するアプローチ「ChangeScribe」を提案・評価したものです。

---

## 論文情報

* **タイトル**: On Automatically Generating Commit Messages via Summarization of Source Code Changes
* **著者**: Luis Fernando Cortés-Coy, Mario Linares-Vásquez, Jairo Aponte, Denys Poshyvanyk ([conf.researchr.org][1])
* **発表**: 2014 IEEE 14th International Working Conference on Source Code Analysis and Manipulation (SCAM 2014) ([cs.wm.edu][2])

---

## 背景と課題

* 研究調査によれば、23,000以上のJavaプロジェクト中で約10％しか「記述的」なメッセージがなく、66％以上が15語未満と極めて短いか空白であることが報告されています。これはソフトウェアの保守性や履歴分析の妨げになります ([researchgate.net][3])。
* 手動で書かれるコミットメッセージは記述負荷が高く、書き忘れや質の低いメッセージが多いことから、自動生成のニーズが高まっています。

---

## ChangeScribe のアプローチ

1. **変更セットの抽出**

   * Gitの二つの隣接バージョン $V_{i-1}, V_i$ からJGitを使って差分（Addition・Deletion・Modification）を取得します ([cs.wm.edu][2])。
2. **コミットステレオタイプ判別**

   * 変更の型（リファクタリング、バグ修正、機能追加など）をカテゴリ化し、大まかな「コミットタイプ」を自動推定。
3. **インパクトセット分析**

   * 変更対象クラス／メソッドに加え、それを参照する外部メソッドも含めた“影響範囲”を算出し、メッセージの詳細レベルを制御します ([cs.wm.edu][2])。
4. **自然言語メッセージ生成**

   * （1）全体概要文：コミットステレオタイプ＋主要な変更ファイル数をテンプレートで生成
   * （2）詳細説明文：各変更要素（クラス名、メソッド名、プロパティ変更など）を文法テンプレートで列挙

---

## 評価

* **データセット**：複数のオープンソースJavaプロジェクトから抽出したコミット履歴
* **ユーザ調査**：23名の開発者を対象に、ChangeScribe生成メッセージと実際のメッセージを比較。

  * **有用度**：ChangeScribe 出力が「有用」と評価された割合は約75％
  * **完成度**：要約の網羅性・明瞭性において、手動メッセージと同等以上との評価を多数得ています ([researchgate.net][3])。

---

## 主な貢献と示唆

* **実装可能なツール**
  SCAM 2015では、論文で提案した手法を実装したEclipseプラグイン版「ChangeScribe」も公開し、実際の開発環境で支援ツールとしての利用を検証しています ([cs.wm.edu][4])。
* **テンプレート＋構造要約の有効性**
  シンプルなテンプレート手法ながら、差分情報と影響範囲を組み合わせることで、開発者が理解しやすいメッセージを高い精度で自動生成できることを実証。
* **今後の展望**

  * リファクタリング検出の強化によるより詳細な文言生成
  * バグ追跡システム連携による課題／チケット情報の自動付与
  * 自然言語生成モデル（LLM）とのハイブリッド化による自由記述性の向上

---

この論文は、Diff解析から直接コミットメッセージを“要約”として組み立てる最初期の実用ツールとして高く評価されており、以降の学習ベース／LLMベース手法の礎を築いた研究です。

[1]: https://conf.researchr.org/details/scam-2024/SCAM-2024-research-track/28/MIP-Presentation-On-Automatically-Generating-Commit-Messages-via-Summarization-of-S?utm_source=chatgpt.com "MIP Presentation: \"On Automatically Generating Commit Messages ..."
[2]: https://www.cs.wm.edu/~denys/pubs/SCAM14-ChangeScribe-CR.pdf?utm_source=chatgpt.com "[PDF] On Automatically Generating Commit Messages via Summarization ..."
[3]: https://www.researchgate.net/publication/267326224_On_Automatically_Generating_Commit_Messages_via_Summarization_of_Source_Code_Changes?utm_source=chatgpt.com "On Automatically Generating Commit Messages via Summarization ..."
[4]: https://www.cs.wm.edu/~denys/pubs/ICSE%2715-ChangeScribeTool-CRC.pdf?utm_source=chatgpt.com "[PDF] ChangeScribe: A Tool for Automatically Generating Commit Messages"

</details>
