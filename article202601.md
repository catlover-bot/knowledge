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
Transformerの最後の処理は、線形変換とソフトマックス関数である(以下図)。  
<img width="1002" height="200" alt="image" src="https://github.com/user-attachments/assets/eebe75d5-8f9c-4866-a8d3-8fe3f9b115cd" />

形状が(c,e)のテンソルは、線形変換によって(c,v)の形状に変換される。vはトークンの語彙サイズを表します。そして、ソフトマックス関数を適用する。この操作により、c個の確率分布が得られる。つまり、Transformerはc個のトークンID列を入力すると、同じ数のc個の確率分布が得られることになる(以下図)。  
<img width="1024" height="267" alt="image" src="https://github.com/user-attachments/assets/cd09f0e3-44a3-4a56-96ce-c0a2c63e265b" />  

ここで重要なのは、各位置の確率分布は、その位置の次にクルトークンの予測を表すという点である。上図の例では、  
- 1つ目の出力は["A"]から次のトークン（" cat"）を予測する確率分布
- 2つ目の出力は「"A", " cat"」から次のトークン（" sat"）を予測する確率分布

を表します。そのため、["A", " cat", " sat", " on", " the"]の次のトークンを予測したい場合は、最後の行（5つ目）の確率分布を用いる。  
なお、各位置の確率分布で、その位置の次にクルトークンの予測を表すようにするには、「Attentionマスク」という仕組みが必要になる。  
> 💡**条件付き確率と文章の確率**
> Transformerはc個のトークンを入力すると、c個の条件付き確率分布を同時に出力する。たとえば、トークン列x_1,...,x_cが与えられたときには次の確率分布を出力する。
> - 1番目の出力：P(・|x_1)
> - 2番目の出力：P(・|x_1,x_2)
> - ...
> - c番目の出力：P(・|x_1,...,x_c)
> ここでP(・|x_1,...,x_i)はトークン列x_1,...,x_iが与えられたときの次のトークンの確率分布を表す。記号・は「任意のトークン」を意味し、この分布から各トークンの確率が得られる。
> また、文章全体の確率は、確率の連鎖律により次のように計算できる。
> P(x_1,...,x_c)=P(x_1)・P(x_2|x_1)・P(x_3|x_1,x_2)・・・・P(x_c|x_1,...x_c-1)
> Transformerは一度の順伝播で、これら全ての条件付き確率を同時に効率的に計算できる（ただし、P(x_1)）については別で求める必要がある。

## TransformerにおけるAttentionの役割
ここまでTransformerの基本構成を見てきた。次に、このTransformerという全体のシステムの中でAttentionがどのような働きをしているのかを説明する。  
まず重要な前提として、Transformerでは各トークンの埋め込みベクトルが段階的に更新されていく仕組みになっている。この更新は、AttentionとFFNからなるTransformerブロックを繰り返し適用することで実現される。  
<img width="1024" height="333" alt="image" src="https://github.com/user-attachments/assets/c1e8e984-b15d-4c2d-9257-2efab5ac499a" />

上図が示すように、Transformerブロックは通過するテンソルの形状は(c,e)で一貫している。つまり、テンソルの各行とトークンの対応関係は変らずに、その内容がブロックごとに更新されていく。例えば、2行目の「 cat」に対応するベクトルは、その位置を維持したまま更新が行われる。  
> 💡FFNとAttentionの比較
> FFNは各トークンに対応するベクトル（＝トークンベクトル）を独立して変換する。つまり、他のトークンベクトルの影響を受けない。このように各位置（トークン）ごとに独立して適用されることから、FFNはPosition-wise FFN（位置ごとのFFN）とも呼ばれる。
> 一方、Attentionではすべてのトークンべクトルが系列内の他のトークンベクトルと相互に参照し合いながら更新されていく。すなわち、あるトークンの表現が他のトークンからの情報に基づいて変化する（以下図）。  
> <img width="1024" height="539" alt="image" src="https://github.com/user-attachments/assets/f75172bb-0909-4c29-9827-52be1831cde7" />

それでは、Attentionの役割を具体例で説明する。まずは次の2つの例文を見て。
- I ate a  fresh orange(私は新鮮なオレンジを食べた)
- Her dress is bright orange(彼女のドレスは鮮やかなオレンジ色だ)
この2つの文がトークン化と埋め込みによって下図のように処理されたとする。

<img width="1024" height="320" alt="image" src="https://github.com/user-attachments/assets/c1bdbcc7-92e0-43ba-bf19-e8fb3e0c9df0" />

上図では、両方の「 orange」トークンに同じ埋め込みベクトルが割り当てられている。しかし、orangeという言葉は、最初の例文では「果物」、2つ目では「色」を表している。  
では、この「 orange」ベクトルはどのような状態なのだろうか。イメージでは、以下図に示すように、「一般的なorange」の概念を表現している。つまり、果物としての意味や色としての意味や色としての意味が混在した状態である。  
<img width="1024" height="438" alt="image" src="https://github.com/user-attachments/assets/c74a59e8-ab5b-4030-a3a7-d67b7f8db843" />

ここでAttentionが重要な役割を果たす。Attentionは周囲のトークンとの関係性から、埋め込みベクトルを文脈に合わせて調整する。そして、その結果を残差接続を通じて元の埋め込みベクトルに加算する。1つ目の例文では、「 orange」に対応する埋め込みベクトルは、「 ate」や「 fresh」との関係性から、果物としての意味へと更新されるでしょう。  
<img width="1770" height="858" alt="image" src="https://github.com/user-attachments/assets/5ad3fa01-f9c1-4610-b4ea-55f5e212f6b0" />

TransformerではAttentionとFFNによる変換が複数層にわたって繰り返される。各トークンは層を重ねるごとに周囲の情報を取り込み、より洗練された表現へと発展していく。この仕組みにより、Transformerはトークンの意味を文脈に応じて柔軟に調整できるようになる。  
> 💡**TransformerにおけるFFNの役割**
> Attentionは他のトークンから情報を集めて文脈を反映させる。一方、FFNは各トークンの表現を独立に変換する。FFNでは線形変換と非線形変換を組み合わせることで、単純な線形変換では捉えられない複雑なパターンを学習できる。
</details>
