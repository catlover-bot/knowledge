# PointNet++：近くの形を集め、広い形へつなぐ

PointNetは点ごとの特徴を全体へ集約するが、距離で決まる近隣関係を段階的に学ぶ構造を持たない。PointNet++は小さな近傍の特徴を作り、その特徴同士をさらにまとめる。細部から広い文脈へ進む階層が核になる。[公式解説・図1][project]

## set abstractionで何を残すか

入力は各点の座標と、必要なら色などの特徴。各段では次の三つを行い、「少数の代表点の座標＋局所特徴」を出力する。[§3.2][paper]

1. **Sampling**：FPS（最遠点サンプリング）で、既に選んだ点への最短距離が最大の点を順に追加し、近傍の中心を選ぶ。
2. **Grouping**：中心から半径内の点を集めるball queryで、重なり得る局所領域を作る。
3. **局所PointNet**：中心を引いた相対座標と点特徴に共有MLPを適用し、近傍内のmax poolingで固定長の特徴へまとめる。[公式実装][layers]

これを繰り返すと、上位段は下位段の局所特徴を使って広い範囲を扱う。分類では全体の特徴へ進み、点ごとのラベルが必要な場合は、特徴を元の点へ戻す処理も必要になる。[公式解説・図1][project]

![入力点群からFPSと球近傍を経て局所特徴を作り、上位の特徴へまとめる4段階](../../assets/diagrams/pointnet-hierarchy.svg)

図は本稿用の独自の概念図。処理の関係を簡略化したもので、実測結果ではない。

## 半径と点数を混同しない

ball queryは空間的な広さを決め、含まれる点数は密度で変わる。k近傍法は点数を決め、覆う範囲が変わる。実装の点数上限は、半径とは別の設定だ。公式CUDA実装では球内で最初に見つかった点を上限まで採り、足りない枠は既存点の反復で埋める。固定長の配列でも、異なる点が同数あるとは限らない。[§3.2][paper] [近傍探索の実装][grouping]

半径の意味は座標の単位にも依存する。公式ModelNetローダーは平均を引き、原点からの最大距離で割る。こうした正規化後の半径0.1を、実空間の10 cmと読み替えてはいけない。局所中心を引くだけの処理も、回転や大きさまで自動で揃えるものではない。[正規化の実装][dataset] [局所座標の実装][layers]

## 密な場所と疎な場所で、何を見るか

説明用に、同じ椅子の同じ脚を密・疎に観測したとする。同じ正規化を施した半径0.1の領域に、密な観測では24点、疎な観測では3点しかない。これは架空の例で、精度測定ではない。小さい領域では疎な側の断面形状を捉えにくく、範囲を広げると隣の脚まで混ざり得る。単に半径を大きくすればよいわけではない。

- **MSG**：同じ段・同じ中心で複数半径の特徴を別々に抽出し、連結する。細部と広い文脈を併用できる。[公式実装][layers]
- **MRG**：下位段の小領域から集約した特徴と、その領域の元の点を直接PointNetで処理した特徴を連結する。疎なときは細分化した側が頼りにくいため、直接処理の経路が補う。最下位段で大近傍を何度も処理するMSGの計算負担も抑える。[§3.3][paper]

原著は学習時のランダムな点の脱落も使い、異なる密度で特徴を組み合わせる方法を学ばせる。密度を測って半径を決定的に切り替える規則、と理解すると仕組みを取り違える。[§3.3][paper]

## 不変性と頑健性は別々に確かめる

近傍集合が同じなら、共有処理とmax集約は点順序に依存しない。ただし処理全体は別途確認が要る。公式FPSは配列の先頭点から始まり、同距離候補の選択も比較順に左右され得る。ball queryの上限で残る点も入力順で変わる。これは公開コードから分かる実装上の注意で、階層構造の直観だけから厳密な順序不変性を保証できない。[FPS実装][sampling] [近傍探索の実装][grouping]

密度変化を扱う設計から、外れ値・座標ノイズ・遮蔽すべてへの耐性は導けない。本稿では実装の再実行はしていない。使う際は、正規化、半径、点数上限、脱落学習を揃え、点の並べ替えと各種劣化を分けて調べたい。[点群評価の整理](../../topics/point-cloud-evaluation.md)と[劣化評価の論文](../2022/point-cloud-corruptions.md)へ。基礎となる集約は[PointNet](pointnet.md)を参照。

## 出典と確認範囲

- Qi, Yi, Su, Guibas, *PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space*, NeurIPS 2017。
- [原論文PDF][paper]：§1、§3.1–3.4、§4.1、図2–4。密度対策の設計と評価範囲を確認した。
- [著者の公式プロジェクト][project]：Abstract、図1の説明。
- 著者公開リポジトリの確認時master（固定コミット `42926632a3c33461aebfbee2d829098b30a23aaa`）：[層の構成][layers]、[FPS][sampling]、[ball query][grouping]、[ModelNetの正規化][dataset]。コードを読んだ範囲の説明で、実行検証ではない。リンクは確認したコードの版に固定した。
- 出典確認日：2026-10-05。椅子の例・図・評価時の提案は本稿独自の説明。

[paper]: https://proceedings.neurips.cc/paper/2017/file/d8bf84be3800d12f74d8b05e9b89836f-Paper.pdf
[project]: https://web.stanford.edu/~rqi/pointnet2/
[layers]: https://github.com/charlesq34/pointnet2/blob/42926632a3c33461aebfbee2d829098b30a23aaa/utils/pointnet_util.py
[sampling]: https://github.com/charlesq34/pointnet2/blob/42926632a3c33461aebfbee2d829098b30a23aaa/tf_ops/sampling/tf_sampling_g.cu
[grouping]: https://github.com/charlesq34/pointnet2/blob/42926632a3c33461aebfbee2d829098b30a23aaa/tf_ops/grouping/tf_grouping_g.cu
[dataset]: https://github.com/charlesq34/pointnet2/blob/42926632a3c33461aebfbee2d829098b30a23aaa/modelnet_dataset.py
