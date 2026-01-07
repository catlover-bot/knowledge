# 1/6
<details><summary>Transformerについて</summary>
  
# Transformerの基本構造
重要なことは、AttentionがどのようにTransformerに統合され、全体の中でどんな役割を果たしているかという点である。  

## Transformerの動作プロセス
Transformerがテキストを処理するためには、テキストをトークンのID列に変換する必要がある。  
<img width="1574" height="252" alt="image" src="https://github.com/user-attachments/assets/53020dff-67d5-4527-8bd8-e8d14b3cab50" />

このID列がTransformerに入力される。以下の図は、Transformerの仕組みをできるだけシンプルに表したものである。  
<img width="1024" height="248" alt="image" src="https://github.com/user-attachments/assets/65021559-8594-46e0-a3cd-e7e2a776952e" />

上図に示す通り、Transformerの処理は大きく3つのステップに分けられる。  
1. Embed:トークンのID列は、Embed(埋め込み)によって、ベクトル表現に変換される。
2. AttentionとFFN：次にAttentionとFFN（Feed-Forward Network）による変換が繰り返し実行される。
3. LinearとSoftmax：最後にLinear（線形変換）によって各トークンのベクトルを語彙サイズと同じ次元数に変換し、ソフトマックス関数を用いて次に出現するトークンの確率分布を生成する。

以降、各ステップの処理について詳しく見ていく。

## **ステップ1：Embed**
Transformerの最初のステップはEmbedである。これは各トークンIDを高次元のベクトルーーこれを「埋め込みベクトル」と呼ぶーーに変換する（以下図参照）。
<img width="1574" height="814" alt="image" src="https://github.com/user-attachments/assets/38ec4bd5-61fb-45ea-8333-31c1a40c968c" />

トークンIDの数をc、埋め込みベクトルの次元数をeで表記している。トークンID列の形状は(c,)、その埋め込みベクトルをまとめたテンソルの形状は(c,e)となる。

## **ステップ2：AttentionとFFN**
Transformerの核心部は、AttentionとFFNで構成される。この処理単位はTransformerブロックと呼ばれ、繰り返し適用される。  
<img width="1024" height="261" alt="image" src="https://github.com/user-attachments/assets/05175cfa-1cc5-4ceb-a372-17742d449911" />  
Transformerブロックでは、AttentionとFFNの出力は元の入力と加算される。これを残差接続と呼ぶ。この残差接続により、勾配消失問題が緩和され、より深いネットワークの学習が可能になる。  
> 💡同じ形状のテンソルが流れる
> Transformerブロックを通過するデータは、一貫して同じ形状を維持する。データの形状は常に(c,e)である。この一貫性により、Transformerブロックによる複数回の処理が可能となり、さらに残差接続も実現できる。

<img width="216" height="37" alt="image" src="https://github.com/user-attachments/assets/6c5928ea-18db-4d20-9156-ec0bd4fbf6ee" />


Attentionの計算には、クエリ、キー、バリューの3つの入力が必要。しかし、上図のAttentionには1つの入力しかない。そこで、1つの入力からクエリ、キー、バリューをそれぞれ生成し、その後でAttentionの計算を行う（以下図）。  
<img width="1024" height="253" alt="image" src="https://github.com/user-attachments/assets/42cb307a-f70d-4a9f-bd4f-a2a13a96bf08" />  

上図の「Matmul」は行列積を表し、数式では次のようになる。  
<img width="98" height="47" alt="image" src="https://github.com/user-attachments/assets/110173bd-ec65-43af-862b-153153601b25" />

ここでxはAttentionへの入力を表し、W_q、W_k、W_vはそれぞれ学習可能な重み行列を表す。このように、クエリ、キー、バリューはすべて同じ入力xから生成される。これがSelf-Attentionと呼ばれる仕組みである。「ソフトなディクショナリ」では、クエリ、キー、バリューがそれぞれ別々に与えられるイメージであるが、Self-Attentionでは同じ入力xからすべてを生成する。  
> 💡クエリ、キー、バリューの形状
> 式（2.1）の行列積による形状変換の過程は以下の図になる。
> <img width="1024" height="776" alt="image" src="https://github.com/user-attachments/assets/386129dc-32ee-42b8-9fe6-d965c410eaa7" />
> 図の通り、QとKの形状は(c,d)で一致させる必要がある。これは、クエリとキーの内積を計算するためである。一方、ｖの形状は(c,e)である。eは埋め込みベクトルの次元数で、出力はこの次元数に合わせる必要がある。

次にFFNである。FFNでは、線形変換と非線形変換を交互に適用する。最も＠シンプルな構成を下図に示す。  
<img width="946" height="270" alt="image" src="https://github.com/user-attachments/assets/d54d60d1-f7a3-4ac6-8441-213af6a6e698" />

上図のとおり、入力として形状が(c,e)のテンソルを受け取り、同じ形状のテンソルを出力する。

## **ステップ3：LinearとSoftmax**
</details>
