# 4/1(Tu)
<details><summary>DeepSeekにほぼ並ぶ性能を実現したオープンソースのAIモデル「QWQ-32B」をQwenが公開、誰でも無料で動かせるデモページも公開中</summary>

![image](https://github.com/user-attachments/assets/03c11d4c-786c-42c2-82ee-182bd48b15a9)  

Alibaba CloudのAI研究チームであるQwenが、AIモデル「**QWQ-32B**」を2025年3月6日にリリースした。320億パラメーターのモデルでありながら6710億パラメーターの**DeepSeek-R1**と同等の性能を持つとされている。  

[QwQ-32B: Embracing the Power of Reinforcement Learning | Qwen](https://qwenlm.github.io/blog/qwq-32b/)  

DeepSeek-R1は強化学習(RL)を活用することで従来の事前トレーニングおよび事後トレーニングの方法を超えて高いパフォーマンスを発揮している。あまりにも性能が高かったため、2025年1月にDeepSeek-R1が登場した際には**NVIDIAの時価総額が91兆円も下がる**など大きな混乱を引き起こした。  

Qwenの研究チームは広範な世界知識で事前トレーニングを施した基板モデルに対し強化学習を適用したとのこと。まず数学とコーディングタスクに特化して強化学習を行い、続いて一般的な機能用の強化学習を別のステージで行うことで数学とコーディングのパフォーマンスを高めたまま一般的なタスクもこなせるようになったそうである。  

各種のベンチマーク結果は以下である。赤色で示されたのがQwQ-32Bで、青色がDeepSeek-R1-671Bである。いずれのベンチマークにおいてもQwQ-32BはDeepSeek-R1-671Bモデルと同等の性能を発揮していることがわかる。  

![image](https://github.com/user-attachments/assets/12dc9d8c-61b5-4635-8ff9-7257545509bd)  

誰でも無料でQwQ-32Bを試せる[デモ](https://huggingface.co/spaces/Qwen/QwQ-32B-Demo)が用意されているので使ってみる。今回は「ある自然数ｎに対して、n^3+(n+1)^3+(n+2)^3が常に9で割り切れることを証明してください」というプロンプトを入力した。  

プロンプトを入力すると、まず思考フェーズが始まる。問題文を日本語で入力したが、思考の中身を見ると正しく理解できている模様。  
![image](https://github.com/user-attachments/assets/55e0093e-36d0-4b12-9fa7-810004d612d9)  

約3分の思考を経て、英語ではあるものの正しい解答が出力された。  
![image](https://github.com/user-attachments/assets/05e62fc9-c1a5-488f-a107-d06b386f94e4)  

日本語の出力にも対応しているようで、「日本語で出力してください」と指示することで解答を日本語に変換してくれた。  
![image](https://github.com/user-attachments/assets/1117b318-8ee1-4a50-86bf-96c79e6fcb9d)  

Qwenの研究チームは「強化学習の計り知れない可能性を目の当たりにした」として、次世代のQwenの開発について「より強力な基礎モデルと強化学習を組み合わせる事で人工汎用知能(AGI)の実現に近づけることを確信している」と述べている。
</details>

<details><summary>GPT-4o miniやClaude 3を無料かつ匿名で誰でも使える「Duck.ai」が登場</summary>

![image](https://github.com/user-attachments/assets/5c867248-b2d4-4f31-926e-5af291b108e4)  

ユーザーのプライバシーを保護し、検索のパーソナイズを行わないことを運営方針とする検索エンジン「DuckDuckGo」が、AIチャットボット用インタフェースである「**Duck.ai**」を一般公開した。誰でも無料かつ匿名で、GPT-4o miniやClaude 3、Llama 3.3などのチャットモデルと会話することが可能  

[Duck.ai](https://duck.ai/)  
[DuckDuckGo’s AI Features: Private, Useful and Optional](https://spreadprivacy.com/ai-feature-upgrade/)  

Duck.aiにアクセスして、「開始」をクリックする。  
![image](https://github.com/user-attachments/assets/d63b52cf-cd58-4401-8a45-265379a67d47)  

プライバシーポリシーと利用規約が表示されるので、目を通したら「同意」をクリック。  
![image](https://github.com/user-attachments/assets/f302372f-c510-4566-8b67-7be1c7506703)  

Duck.aiの画面は以下。  
![image](https://github.com/user-attachments/assets/ee1a9a61-c635-4558-81bd-39ae3da9c4f5)  

左上に表示されているモデル名をクリックすると、チャットモデルを選択することができる。現時点ではGPT-4o mini、Llama 3.3 70B、Claude 3 Haiku、o3-mini、Mistral Small 3の5種類から選択できる。  
![image](https://github.com/user-attachments/assets/0054f9ad-f9a3-49bb-b49a-180fbe0f801a)  

試しに、5つんｐモデルに「あなたのモデル名を教えてください」と尋ねてみた。GPT-4o miniは「私はOpenAIの原画モデル」と教えてくれたが、「具体的にGPT-3.5というバージョン」とのことであった。  
![image](https://github.com/user-attachments/assets/c0fc6afc-74c8-46b4-b225-906d4a8515a7)  

Llama 3.3 70Bは、なぜかAI開発・利用プラットフォームのTogether AIを名乗っている。  
![image](https://github.com/user-attachments/assets/9e4778ba-4288-4070-9001-de246a094ca4)  

Claude 3 Haikuはかなり細かい回答を返してくれた。DuckDuckGoのプレイバシーレイヤーを通しており、モデル情報が匿名化されていることを明かしてくれる。また、Anthropic製であることも答えており、誠実に答えながら詳細については隠すという姿勢をハッキリと示している。  
![image](https://github.com/user-attachments/assets/8bd6e3e5-8a77-45b6-9240-97ec1b3e5f98)  

GPT o3-miniは以下の通り。  
![image](https://github.com/user-attachments/assets/eb387aca-eb74-4d8b-96da-fe8d57070d61)  

Mistral Small 3は、「Mistral AI製である」ということだけ教えてくれた。  
![image](https://github.com/user-attachments/assets/2d8f28a4-af34-4805-9029-7133f993cbde)  

DuckDuckGoによると、Duck.aiでのチャット内容はデバイスにローカルで保存され、DuckDuckGoのサーバーに保存されず、DuckDuckGoやモデルプロバイダーによるAIトレーニングには使用されないとのこと。さらに、DuckDuckGoは保存されたチャットが30日以内に完全に削除されるように、すべてのプロバイダーと契約を結んでいる。
</details>

# 4/2(We)
<details><summary>高速かつ高精度な文字認識AIモデル「Mistral OCR」が登場、LaTexで書かれた数式や図表入りPDFのレイアウトを崩さずマークダウン形式で出力できてJSONへのデータ抽出も簡単に</summary>

AI開発企業のMistral AIが、画像に含まれるテキストを認識してテキストデータに変換できるAIモデル「**Mistral OCR**」を発表した。Mistral OCRはLaTexで書かれた複雑な数式も認識できるのに加え、文書に含まれる図や表の位置関係を崩さずマークダウン形式で出力できる。  

[Mistral OCR | Mistral AI](https://mistral.ai/news/mistral-ocr)  

Mistral AIはMistral OCRの能力を示す例を複数公開している。まず、処理前のオリジナルデータが以下。テキストだけでなく図や表も含まれている。  
![image](https://github.com/user-attachments/assets/d85c687e-a881-42c2-beaf-9401105b047c)  

Mistral OCRで処理した結果はこのようである。図とテキストの位置関係を崩さずに変換できた。また、表の内容も行や列の関係を崩さずに変換できている。OCR結果はマークダウン形式で出力され、出力結果をJSONなどの構造化されたデータ形式にまとめることも可能。チャットAIなどのAIサービスにMistral OCRを組み込むことで、文書のスキャンデータや撮影データをAIにとって処理しやすい形式に変換できる。  
![image](https://github.com/user-attachments/assets/7ebcb3e7-ebd1-4e2d-9f25-337f013b0ca0)  

複雑な数式を含む文書もOCR処理できる。処理前の元データはこのようである。  
![image](https://github.com/user-attachments/assets/db2da3c9-886e-442d-af6a-a74ebace7c5f)  

処理結果は以下の通り。数式をそのままの見た目で変換できた。  
![image](https://github.com/user-attachments/assets/0db3cada-3a41-4bf9-b25f-b600d9a8b978)  

Mistral OCRの性能を「Google Document AI」「Azure OCR」「Gemini 1.5 Flash」「Gemini 1.5 Pro」「Gemini 2.0 Flash」「GPT-4o」と比較した表が以下。Mistral OCRは数式やスキャンデータを含むすべてのカテゴリで最も精度の高いOCRが可能である。  

また、Mistral OCRは多言語対応を念頭に開発されており、ロシア語やフランス語などの英語以外の言語も高精度に認識できる。  

Mistral OCRは動作速度の速さも特徴で、単一ノードで1分当たり最大2000ページのOCR処理が可能である。以下の「図表を含むPDFファイルをマークダウン形式に変換するデモ」を再生すると、処理の速さがよく分かる。  

[Mistral OCR on Alphafold paper - YouTube](https://www.youtube.com/watch?v=6lRBm0KnzBI)  

Mistral OCRは「[Le Chat](https://gigazine.net/news/20241119-mistral-ai-le-chat/)」で無料で使える。また、APIはMistral AIの開発者向けプラットフォーム「la Plateforme」を通じて利用可能。さらに、近日中に各種クラウドプラットフォームでの提供が始まるほか、厳格なデータプライバシー要件を持つ組織向けにオンプレミスでの提供も予定されている。

</details>

<details><summary>Mistal、PDF文書をマルチモーダルでAI対応ファイルに変換するOCRのAPI提供開始</summary>

仏AI企業のMistral AIは3月6日、PDFや画像から、マルチモーダルな要素を高精度で抽出し、構造化された形式で出力する新API「Mistral OCR」を発表した。有償で提供する他、AIチャットbot「Le Chat」で無料で試すこともできる。  

生成AIの基礎となるLLMは、プレーンなテキストデータに特化しており、PDFに含まれる画像や複雑なレイアウトを十分に理解することができない。Mistral OCRがPDFのようなマルチモーダルドキュメントを抽出、出力することで、PDFを直接理解するのが困難なLLMでも、PDFに含まれる情報を効果的に活用できるようになる。  

Mistral OCRは、PDFの内容を単にテキスト化するのではなく、Markdownでフォーマットする。  

![image](https://github.com/user-attachments/assets/ed2e83b1-49bb-4bf6-8635-b574cf2288fe)  

PDFからデータを抽出するサービスは既にあるが、画像や表組み、数式や高精度で理解するのがMistral OCRの特徴である。以下のようなベンチマークを紹介している。なお、比較している他のLLMには画像抽出機能はない。  

![image](https://github.com/user-attachments/assets/0e65f1c6-ed03-4fb4-a31a-fc3c7bbb67bb)  

APIでの提供は、1000ページ当たり1ドル。Mistralの他、AWS、Azure、Google Cloud Vertexなどのクラウドパートナーを通じても提供する。また、機密性の高いデータを扱う企業向けに、オンプレミス展開も提供する。  

[公式ブログ](https://mistral.ai/fr/news/mistral-ocr)に、数式やヒンディー語の文書など、OCR前後の文書の比較例が掲載されている。
</details>

<details><summary>さまざまなAIをWindowsのローカルPCで動かせる「Run llama.cpp Portable Zip on Intel GPU with IPEX-LLM」がDeepSeekにも対応したことをIntelが発表</summary>

近年、高度な生成AIや大規模言語モデルが多数登場しているが、それらを動作させるには高価なGPUなど、相応の危機が必要となる。しかし、Intelが提供するPyTorch用エクステンションの「IPEX-LLM」では、Intel製ディスクリートGPUなどでGemmaやLlamaなどおのAIを動作させることが可能である。今回、そんなIPEX-LLMがDeepSeek-R1に対応したことをIntelが発表した。  
[ipex-llm/docs/mddocs/Quickstart/llamacpp_portable_zip_gpu_quickstart.md at main · intel/ipex-llm · GitHub](https://github.com/intel/ipex-llm/blob/main/docs/mddocs/Quickstart/llamacpp_portable_zip_gpu_quickstart.md)  

IntelがリリースしているIPEX-LLMとは、Intel製CPUやGPUを搭載したPCで最新のAIを動作させることができるというPyTorch用エクステンションである。  

今回、IntelはIPEX-LLM上でオープンソースソフトウェアライブラリのllama.cppを基にした「llama.cpp Portable Zip」を使うことで、Intel製GPUでもllama.cppを直接実行できるようになったことを発表した、これ伴い、llama.cpp Portable ZipでDeepSeek-R1-671B-Q4_K_Mが実行可能になったことを明らかにしている。  

IntelはGithub上で、llama.cpp Portable Zipのインストール方法ならびにllama.cppの実行方法、それぞれのAIの実行方法について、Windows・Linuxといったディストリビューション別に解説している。  

[ipex-llm/docs/mddocs/Quickstart/llamacpp_portable_zip_gpu_quickstart.md at main · intel/ipex-llm · GitHub](https://github.com/intel/ipex-llm/blob/main/docs/mddocs/Quickstart/llamacpp_portable_zip_gpu_quickstart.md)  

なお、Intelはllama.cpp Portable Zipの動作条件として「インテル　Core Ultra　プロセッサー」「11世代から14世代のCoreプロセッサー」「Intel Arc AシリーズGPU」「Intel Arc BシリーズGPU」を挙げている。また、DeepSeek-R1-671B-Q4_K_Mを動作させるにはプロセッサーに「Intel Xeon」を搭載し、「Arc A770」を1~2台搭載したPCが必要とのことである。  
</details>
