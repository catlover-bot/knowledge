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


$$
\mathrm{Attention}(\boldsymbol Q, \boldsymbol K, \boldsymbol V)
=
\mathrm{Softmax}\left(\frac{\boldsymbol Q \boldsymbol K^{\top}}{\sqrt{d}}\right)\boldsymbol V
$$

Attentionの計算には、クエリ、キー、バリューの3つの入力が必要。しかし、上図のAttentionには1つの入力しかない。そこで、1つの入力からクエリ、キー、バリューをそれぞれ生成し、その後でAttentionの計算を行う（以下図）。  
<img width="1024" height="253" alt="image" src="https://github.com/user-attachments/assets/42cb307a-f70d-4a9f-bd4f-a2a13a96bf08" />  



</details>
