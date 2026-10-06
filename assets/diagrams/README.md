# 解説図の出典と作成方針

作成日：2026-10-05。点群の分割図は2026-10-06に描き直した。

このディレクトリの11点は、各読書ノート・横断ノートのために新しく構成した**独自のSVG概念図**です。著者の図版・スクリーンショット・既存のアイコン素材を転載、トレース、再配布したものではありません。箱、矢印、点列、単純な幾何形状、日本語ラベルを組み合わせて作成しました。数値のグラフや、再実験による測定結果は含みません。

原著から確認した仕組みと、このリポジトリで提案する確認手順・想定例は、参照先の本文で区別しています。論文の結果や保証の範囲は、図だけで判断せず、本文の出典と確認範囲を参照してください。

## 各図の根拠

- **[rag-evidence-flow.svg](rag-evidence-flow.svg)** — [RAGの読書ノート](../../papers/2020/rag.md)。[Lewis et al., arXiv:2005.11401v4](https://arxiv.org/pdf/2005.11401v4)、§2.1–2.3をもとに、段落別の生成分布と確率の統合を図解。候補段落の連結を示すものではありません。Token方式でも質問から得た同じ検索候補を使用します。根拠確認の注意は本ノートの整理です。
- **[mlgo-decision-loop.svg](mlgo-decision-loop.svg)** — [MLGOの読書ノート](../../papers/2021/mlgo.md)。[Trofin et al., arXiv:2101.04808v1](https://arxiv.org/html/2101.04808v1)、§3.1・4.1.1–4.1.4・4.4、および[LLVM公式文書](https://llvm.org/docs/MLGO.html#interacting-with-ml-models)。サイズ向けインライン化の学習と、固定方策を使うコンパイル時の推論を分離しました。サイズ評価は一連の判断後のコードに対するもので、各判断直後の個別報酬を図示していません。
- **[prover-feedback-loop.svg](prover-feedback-loop.svg)** — [DeepSeek-Prover-V1.5の読書ノート](../../papers/2024/deepseek-prover-v1-5.md)。[Xin et al., arXiv:2408.08152v1](https://arxiv.org/html/2408.08152v1)、§2.3・3.1–3.3。推論時のtruncate-and-resumeと探索位置の選択を簡略化した図です。学習時のRLPAFの0/1報酬とは区別し、探索統計や成功率を表していません。
- **[text2cad-sequence.svg](text2cad-sequence.svg)** — [Text2CADの読書ノート](../../papers/2024/text2cad.md)。[Khan et al., arXiv:2409.17106v1](https://arxiv.org/html/2409.17106v1)、§3–4・補足§9。学習用注釈の準備とCAD操作列の生成を分け、利用者側の寸法確認を加えました。穴間隔の例は未実施の想定例であり、既存CADの対話編集能力や製造適合性の実証ではありません。
- **[proof-validation-layers.svg](proof-validation-layers.svg)** — [形式証明の検証ノート](../../topics/formal-proof-validation.md)。[Lean公式手引き：Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)と[Axioms](https://lean-lang.org/doc/reference/latest/Axioms/)、[TRIGO §6.2・9](https://aclanthology.org/2023.emnlp-main.711.pdf)を踏まえた本ノートの確認順。命題の固定、隔離環境での証明検証、公理と信頼の点検、比較条件の保存を別々の問いとして示しています。
- **[optimization-objectives.svg](optimization-objectives.svg)** — [コード最適化の評価ノート](../../topics/code-optimization-evaluation.md)。[Cummins et al., arXiv:2309.07062v1](https://arxiv.org/pdf/2309.07062v1)、II・IV-B・D、[Nichols et al., arXiv:2404.18864v1](https://arxiv.org/html/2404.18864v1)、VI・VII、および[LLVMの測定指針](https://llvm.org/docs/Benchmarking.html)。変更対象と評価指標を分ける本ノートの整理であり、速度とサイズの相関や手法の優劣を示していません。
- **[cad-representations.svg](cad-representations.svg)** — [CAD表現の横断ノート](../../topics/cad-representations.md)。[Modly公式README](https://github.com/lightningpixel/modly/blob/main/README.md)、[CAD-Llama, arXiv:2505.04481v2 §3.2–3.3](https://arxiv.org/html/2505.04481v2)、[AIDL, arXiv:2502.09819v1 §1・3・4](https://arxiv.org/html/2502.09819v1)。メッシュ・操作と数値・幾何制約の違いを、独自の単純形状で対比しました。三分類は排他的な製品分類ではなく、表示形状は加工図面ではありません。AIDLの実験範囲は2Dです。

- **[pointnet-set-function.svg](pointnet-set-function.svg)** — [PointNetの読書ノート](../../papers/2017/pointnet.md)。[Qi et al., arXiv:1612.00593v2](https://arxiv.org/pdf/1612.00593v2)、§4.2。共有MLPとチャネルごとのmax、分類の不変性と点ごとの分割の同変性を説明しました。A＝(1,4)、B＝(3,2)、C＝(2,1)は仮の特徴で、座標や実測値ではありません。点ラベルも仮の例です。T-Netなどの整列処理を省略しています。
- **[pointnet-hierarchy.svg](pointnet-hierarchy.svg)** — [PointNet++の読書ノート](../../papers/2017/pointnet-plus-plus.md)。[Qi et al., NeurIPS 2017](https://proceedings.neurips.cc/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf)、§3.2–3.3、および[著者公開の層の実装](https://github.com/charlesq34/pointnet2/blob/42926632a3c33461aebfbee2d829098b30a23aaa/utils/pointnet_util.py)。FPSによる既存点の選択、固定半径の球近傍、相対座標からの局所特徴、階層化を示しました。橙色の中心は前段の点配置にある点です。円は球近傍の二次元模式図で、配置・密度・縮尺は架空です。MSGは同じ段・同じ中心の複数半径として描き、MRGの別経路と点への特徴の伝播は省略しています。
- **[pointcloud-corruption-protocols.svg](pointcloud-corruption-protocols.svg)** — [点群劣化ベンチマークの読書ノート](../../papers/2022/point-cloud-corruptions.md)。[Ren et al., ICML 2022](https://proceedings.mlr.press/v162/ren22c/ren22c.pdf)、§3.1–3.4、および[Sun et al., arXiv:2201.12296v1](https://arxiv.org/pdf/2201.12296v1)、§3–5・Table 2・Fig. 4。ModelNet-Cの7種類×5強度とDGCNN基準のmCE、ModelNet40-Cの13種類×5強度＋2種類×5視点と未正規化の平均誤り率ERcorを区別しました。ERcorの平均係数は本文の式と表の違いに注意して本ノートが明記したものです。上部は比較時に推論方式を分ける本ノートの整理で、BN／TENTはSunらの評価例。点配置は独自の模式例で、性能や学習・評価範囲の非重複を示す図ではありません。
- **[pointcloud-evaluation-split.svg](pointcloud-evaluation-split.svg)** — [点群評価の横断ノート](../../topics/point-cloud-evaluation.md)。[Kapoor & Narayanan, arXiv:2207.07048v1](https://arxiv.org/html/2207.07048v1)、§2.4・3.2–3.4、[scikit-learn公式の前処理指針](https://scikit-learn.org/stable/common_pitfalls.html)、§12.2–12.3、および[GroupKFold公式文書](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)を踏まえた本ノート独自の提案です。2026-10-06の改稿では、同じ椅子Aから抽出したA1・A2を両側に分けた場合と、椅子A・Bを物体単位で分けた場合を対比しました。点配置は独自に作った架空例で、実データや実際の被験者を含みません。未知物体への評価に必要な分割を説明する図であり、原著ベンチマーク全てがこの手順を採用したという主張ではありません。検証用グループは図から省略していますが、設定選択にはテストと独立した検証用グループが必要です。

## 表示・アクセシビリティ

- 基準幅640pxの縦型構成。`viewBox`を持ち、表示先で幅を縮めても縦横比を保てます。
- 日本語ラベルは22px以上。`Noto Sans CJK JP`等のフォールバックを指定し、外部フォント取得は行いません。
- 各SVGに`title`、`desc`、`role="img"`と`aria-labelledby`を設定。本文の画像にも内容を説明する代替テキストを置いています。
- スクリプト、外部画像、外部リソース、`foreignObject`は使用していません。
- 全11点の表示点検日：2026-10-05。InkscapeとローカルのNoto日本語フォントで幅640px・360pxのPNGを作成し、文字の欠落・重なり・端切れを点検しました。点検用PNGはリポジトリには含めていません。表示先に同じフォントがない場合は字形・字幅が多少変わります。

- 点群の分割図は2026-10-06に再点検。InkscapeとローカルのNoto日本語フォントで幅640px・360pxのPNGを作成し、点配置、分割境界、同じ物体を結ぶ線、ラベルの読みやすさを確認しました。

## 権利について

上記リンクは内容の根拠を示すもので、原著図版の利用許諾や第三者のライセンスを継承するという表示ではありません。このファイルは、新たなリポジトリ全体のライセンス付与を行うものでもありません。
