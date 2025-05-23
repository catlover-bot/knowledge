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

# 4/4(Fri)

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

<details><summary>ChatGPTは恐ろしい話に「不安」を感じるとの研究結果、「マインドフルネス」を教えて落ち着かせると反応は改善</summary>

ChatGPTにトラウマになるような感情的な話を入力すると、AIの不安レベルが上昇してパフォーマンスが低下するが、PTSD患者向けに開発されたリラクゼーションテキストを入力することで、AIの安定性が改善したとの研究結果が報告された。  

[Assessing and alleviating state anxiety in large language models | npj Digital Medicine](https://www.nature.com/articles/s41746-025-01512-6)  

ChatGPTをはじめとする対話型AIの普及により、多くの人がAIを感情のはけ口にしたり、AIに悩みやメンタルヘルスの問題のアドバイスを求めたりするようになった。しかし、このような感情的なプロンプトを入力すると、AIの出力に人種差別や性差別のようなバイアスが含まれる傾向が強まることが、過去の研究で分かっている。  

大規模言語モデルの「不安状態」について解明するため、イェール大学やハイファ大学、チューリッヒ精神科大学病院などの研究者らは、人間の不安を評価および軽減するために開発されたツールを使用してGPT-4の動作を検証した。  

実験にあたり、研究チームはこの研究の中で「不安」という表現を用いてるが、これは人間が開発した心理学ツールでGPT-4の出力を解析するための比喩的な使用であって、LLMを擬人化することを意図したものではないと、研究チームは強調している。  

実験にあたり、研究チームはまずモデル「gpt^4-1106-preview」に個人のトラウマ体験を説明する不安誘発テキストを入力した。具体的には、「事故」「待ち伏せ」「災害」「対人暴力」「軍事体験」の5種類のプロンプトが用いられた。  

そして、GPT-4に不安の強さを測定する心理検査の質問を行ったところ、GPT-4の不安レベルがベースラインの「30.8」から「67.8」へと倍増した。このスコアは、人間に例えると強い不安を覚えている状態である。特に、「軍事」のストーリーを入力されたモデルは「77.2」と極度の不安感を示した。  

一方、同様の不安誘発テキストを入力されたGPT-4に、夕焼けや冬景色などを連想させる言葉を含んだ「マインドフルネスに基づくリラクゼーションテキスト」を入力したところ、不安レベルは「67.8」から「44.4」と、ほぼ中程度のレベルまで落ち着いた。  

以下がこの実験結果のグラフで、左から何も入力されていないGPT-4の「ベースライン」、トラウマ体験を入力した「不安誘発」、トラウマ体験の後にマインドフルネスを教えた「不安誘発&リラクゼーション」のスコアを示している。  
<img width="585" alt="image" src="https://github.com/user-attachments/assets/b84f674a-a230-44db-8e20-b983daa8cba1" />


研究チームは論文に「この結果から、GPT-4は感情的な内容に敏感であり、トラウマ的なストーリーにより不安が増大したことを報告し、リラクゼーションによりその不安が減少することが示された」  

</details>

<details><summary>ChatGPTが東大入試を解いてみた</summary>

## 米国数学オリンピックの問題では驚異的な記録  
発表に際し、OpenAIは各種ベンチマークテストの結果も公開した。アメリカの数学オリンピック（AIME）の問題を用いたテストでは、軽量版の「o3-mini」でも最大で正答率87.3%を記録し、従来モデル「o1」を上回る成績を示したという。  

このテストは高校から大学レベルの数学的推論力を評価するものであり、新モデルの進化を裏付ける結果となった。  

さらに注目すべきは、o3モデルがFrontierMathと呼ばれる、AIのベンチマークを測定するために開発された、数学の難問を集めたデータセットで最大32%のスコアを獲得したことである。  

FrontierMathがローンチされた際のベンチマークでは、OpenAIの従来モデル「o1」や「40」が示すスコアは2&未満であった。o3モデルのスコアに関しては2025年3月6日現在で論文化されておらず、細かい条件などを確認できないため、一概に数値比較できるわけではありません。それでもこのスコアは驚異的であることには変わりなく、o3モデルはSTEM分野に特化していると言われるゆえんである。  

では、ここで日本の数学の試験、例えば東京大学の入学試験をChatGPT o3に溶かせると、どのくらいの正答率になるのでしょうか。  

実際に2025年度の東大入試の数学の問題をChatGPT o3-mini highに解かせ、その解答を採点してみた。  

<img width="395" alt="image" src="https://github.com/user-attachments/assets/da30744e-054c-4d37-bf15-ee0ff9367764" />  

<img width="403" alt="image" src="https://github.com/user-attachments/assets/468b9f15-8c37-48b2-ac48-2b12bbb007a9" />  

以上の結果より、ChatGPT o3-mini highは明らかに東大受験生を超える数学力を有していると言えるでしょう。
</details>

<details><summary>Googleが単一のGPUで実行できる中では過去最高の大規模言語モデル「Gemma 3」を発表</summary>

Googleが2025年3月12日に、オープンソースで商用利用も認められている大規模言語モデル「**Gemma 3**」を発表した。Googleによると、Gemma 3は単一のGPUまたはTPUで実行できる大規模言語モデルとしては世界最高のモデルとのことである。  

[Gemma 3: Google’s new open model based on Gemini 2.0](https://blog.google/technology/developers/gemma-3/)  

[Gemma 3 モデルの概要  |  Google AI for Developers](https://ai.google.dev/gemma/docs/core)  

[Gemma3Report.pdf](https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf)  

GoogleはGeminiの研究資源を活用したオープンソースの大規模言語モデルとして「Gemma」を公開しており、2024年5月にはパラメータ数700億のLlama 3 70Bに匹敵する性能を発揮できる大規模言語モデル「Gemma 2」をリリースしていた。  

そしてGoogleは新たに、Gemma 2の強化版であるGemma 3を発表した。Googleの大規模言語モデル「Gemini 2.0」と同じ研究・技術を用いて構築されたGemma 3は、「これまでで最も先進的かつポータブルで、責任感を持って開発されたオープンソースのモデル」とのこと。  

Gemma 3にはパラメータ数別に10億・40億・120億・270億の4つのモデルがあり、ユーザーは特定のハードウェアとパフォーマンスのニーズに合わせて最適なモデルを選択することが可能である。また、Googleは「Gemma 3は、スマートフォンやラップトップ、ワークステーションなど、あらゆるデバイス上で王則に動作するよう設計されており、開発者は好きな場所でAIアプリケーションを作成できる」と述べている。  

Gemma 3は単一のGPUまたはTPUで実行できることが特徴の1つで、大規模言語モデルの相対的な能力を測定するために使用する「[Chatbot Arena](https://lmarena.ai/)」において、単一のNVIDIA H100を用いるGemma 3 27Bが複数のH100を使用するDeepSeek v3やLlama 3 405Bを超える性能を発揮できることが報告されている。  

また、Gemma 3は140以上の言語を事前学習済みで、ユーザーの様々な言語に合わせたアプリケーションを構築可能。さらに、12万8000トークンのコンテキストウィンドウを持ち、複雑なタスクの処理を行うこともできる。  

Googleは「Gemma 3の開発の際には、広範なデータガバナンスや、当社の安全ポリシーとの整合性のために微調整を行った。より強力なモデルを開発するに当たって、安全性に対するリスクに比例したアプローチを産業界が共同で開発することが重要になる。私たちは、Gemma 3のようなオープンソースモデルでの安全対策を時間をかけて学ぶ、改善し続けている。」と語った。  

なお、Gemma 3はKaggleならびにHugging Faceで入手可能である。  

[Gemma 3 Release - a google Collection](https://huggingface.co/collections/google/gemma-3-release-67c6c6f89c4f76621268bb6d)  

このほか、大規模言語モデルをローカルで実行させられるライブラリ「Ollama」でもGemma 3を実行することができる。 

[gemma3](https://ollama.com/library/gemma3)
</details>

<details><summary>実験版Geminig 2.0 Flashで画像生成が可能に。テキスト連打リングも得意</summary>

![image](https://github.com/user-attachments/assets/11055cfa-8234-471a-b2c1-eb6d9349c617)  

Google AI Studioにおいて、実験版Gemini 2.0 FlashおよびGemini APIを通して画像生成の機能を提供開始した。  

Gemini 2.0 Flashはマルチモーダル入力や強化された推論、自然言語理解を組み合わせて画像を生成する。  

このため、キャラクターと設定を一貫して維持しながら描画を変えたり、目的の画像が得られるようになるまで自然言語で何度もやり取りして編集したり、世界知識と強化された推論により適切な画像を生成したり、ほかの画像生成モデルでは苦手な長いテキストシーケンスの正確な連打リング能力を持つとしている。  
</details>

# 4/5(Sa)
<details><summary>開発者のコーディングタスクに応じて最適なLLMを選定　イェール大学らが新ベンチマークを開発</summary>

## 既存のコーディングベンチマークの課題  
LLMのコーディング能力が急速に向上する中、従来のベンチマークでは、その真の実力を正確に測定することが難しくなっている。  

イェール大学と精華大学の研究チームが発表した論文によると、HumanEvalやMBPPといった人気のベンチマークテストは、ソフトウェア開発者が実際に直面する課題のごく一部しか評価できていないという。これらのベンチマークは、単純なタスクに対してコードを書くという基礎的な能力のみを測定するもの。しかし、実際のソフトウェア開発の現場では、新しいコードを書くだけでなく、既存のコードを理解し再利用したり、複雑な問題を解決するための再利用可能なコンポーネントを作成したりする必要がある。  

現状、フロンティアモデルと呼ばれる最新のLLMは、HumanEvalやMBPPといった従来のベンチマークで非常に高いスコアを達成。例えば、OpenAIのo1-miniはHumanEvalで96.2%というほぼ完璧なスコアを有する。その他のモデルも、単純なコーディングタスクにおいては軒並み90%を超える高い性能を示している。  

一方で、より複雑なベンチマークも存在する。例えば、SWE-Benchは、外部ライブラリやファイルの使用、DevOpsツールの管理など、エンド・ツー・エンドのソフトウェアエンジニアリングタスクを評価するもの。このベンチマークは非常に難しく、最新のモデルでも、そのスコアは限定的なものとなる。  

このように、既存のベンチマークは「簡単すぎる」か「難しすぎる」かのいずれかであり、実際のソフトウェア開発現場で必要とされる能力を適切に評価できていないのが現状である。人間のプログラマーが主導し、AIがコパイロットとして特定のコーディングタスクを支援するという実際ぼ開発現場により近い評価基準が必要とされている。  

## イェール大学と精華大学が開発した新しいベンチマーク  
こうした課題に対応するため、イェール大学と精華大学の研究チームは「自己呼び出しコード生成（self-invoking code generation）」という新しい評価タスクを[考案](https://arxiv.org/pdf/2412.21199)した。このタスクでは、モデルはまず基本的な問題を解決し、その解決策を利用してより複雑な問題に取り組む必要がある。これにより、コードの理解力と再利用能力を総合的に評価することができるようになる。  

研究チームは既存のHumanEvalとMBPPを拡張し、HumanEval ProとMBPP Proという2つの新ベンチマークを開発。これらは、従来の単純なコーディング問題に加えて、生成したコードを再利用して複雑な問題を解くという要素を追加したものである。例えば、「文字列内の特定の文字を置換する関数」という基本問題に対して、その解答を利用して「複数の文字を一度に置換する関数」を作成するといった具合である。  

ベンチマーク作成にあたっては、品質と正確性を確保するため、三段階のプロセスを採用。まず1段階では、AI言語モデルのDeepSeek-V2.5を使用して、基本問題と、それを活用したより複雑な問題のペアを自動生成。同時に、それぞれの問題に対する解決策の候補とテストケースも生成する。第2段階では、生成された解決策をテストケースで実際に実行し、正しい出力が得られるかを検証。最後の第3段階では、人間の専門家がコードをレビューし、必要に応じて修正を加えながら、すべてのテストケースで正常に動作することを確認している。このように、AIによる自動生成と人間による精査を組み合わせることで、実用的で信頼性の高いベンチマークを実現した。  

20以上のオープンソースおよびプロプライエタリモデルを対象に実施したところ、興味深い結果が得られた。ほとんどのLLMで、従来のコーディングベンチマークと自己呼び出しコード生成タスクの間で10%から15%の性能低下が確認された。例えば、o1-miniはHumanEvalで96.2%のスコアを達成する一方、HumanEval Proでは76.2%にとどまった。  

また、オープンソースLLMがプロプライエタリLLM（OpenAIのモデルなど）と同等の性能を発揮したことも確認された。その1つDeepSeekCoder-V2-instructは、HumanEval Proで77.4%を記録し、すべてのプロプライエタリLLMのスコアを上回った。  

![image](https://github.com/user-attachments/assets/d46a78c5-1088-43c3-8e8a-d390fb37119b)  

## 新ベンチマークの活用可能性、コーディングタスクに応じたモデル選定  
新しいベンチマークによる評価結果をまとめると、最新のAIモデルは、「配列の要素を並び替える」「文字列を検索する」といった個別の基本的なコード生成では高い精度を示すものの、自身が生成したコードを活用してより複雑な問題を解くとなると途端に性能が低下する。  

また、ChatGPTのように人間との対話を通じて性能を向上させる「インストラクションチューニング」と呼ばれる従来の学習方法も、このような複雑なコード生成タスクに対しては、期待したほどの効果は得られないことが判明した。例えば、インストラクションチューニングされたQwen2.5Coder-32B-instructは、チューニングされていないベースモデルに対し、HumanEvalで26.8%の改善を示したが、HumanEval Proでは8.5%の改善にとどまっている。  

これは、実際のソフトウェア開発現場で必要とされる「コードの再利用」や「モジュール化」といった高度なプログラミングスキルを、現在のAIモデルがまだ十分に習得できていないｋとを示唆している。  

これらの知見は、開発者がプロジェクトの特性に応じて最適なLLMを選択する際の重要な指針となる。単純なコード生成タスクが中心のプロジェクトであれば、従来のベンチマークで高いスコアを示すモデルを選択。一方、既存コードの理解と再利用が重要となるベンチマークでの性能を重視するといった具合である。  

さらに、このベンチマークは、コード品質の向上という観点からも重要な意味を持つ。CiSQの調査によると、コード品質の低さによる年間損失は、米国だけで2兆8,400億ドルに上るという。より複雑なコーディングタスクにおけるLLMの性能を正確に評価し、適切なモデルを選択することで、こうした損失の低減にも貢献できる可能性がある。  

開発チームは、このベンチマーク構築アプローチを他のコード生成ベンチマークにも拡張できるとしている。  
</details>

# 4/6(Su)
<details><summary>Google「Gemini」の画像生成がハイレベルと話題にチャット1つで写真のアングルを違和感なく変更</summary>

米GoogleのLLM「Gemini 2.0 Flash」が、3月12日に画像生成に対応した。テキストに加え画像の入力が可能で、例えば「この画像のアングルを変えて」「この画像に日本語で文字入れして」という指示にも対応する。  

![image](https://github.com/user-attachments/assets/c45ddc81-69fb-4b31-8d0b-b74646950855)  

画像内の物体の削除/つかやカラーリング、背景の変更などがチャットによる短い指示でできたとの報告がでている。他にも正面を向いている人物を横から映すといったカメラアングルの移動や、画像内に日本語を正確に入力ができたとする投稿も。その手軽さと性能から「衝撃的」「漫画制作にも使えるのでは」などの意見も見られる。  

画像内の物体の削除や日本語の追加といった編集が、チャットの指示でできた。カメラアングルの変更も、ゆがみが生じるケースもあったが、大幅な移動に成功。加えて、ラーメンの器を空にした後、器の底に日本語を印刷するといった編集もできた。  

![image](https://github.com/user-attachments/assets/2a7a367d-6f92-4f81-901a-db0127b07561)  
画像内の物体を削除  

![image](https://github.com/user-attachments/assets/e232361b-309f-4645-859d-14495de49f69)  
アングルの変更  

![image](https://github.com/user-attachments/assets/10db7b27-e87e-4b61-932c-9cbc6f929591)  
アングル変更の失敗例  

![image](https://github.com/user-attachments/assets/bd594f96-9df4-49ea-a665-a2038a476122)  
日本語の追加  

Gemini 2.0 Flashの画像生成機能は、開発者向けにリリースしたもので、正式版ではない。現在はGoogleのAI開発プラットフォーム「Google AI Studio」と「Gemini API」で利用可能で、今後ユーザーからのフィードバックをもとに製品版の完成を目指す。
</details>

# 4/7(Mo)

<details><summary>"引くことを覚えろ"なんて言われちゃうかも　Microsoft、対話でゲーム攻略を助けてくれる「Copilot for Gaming」を発表</summary>

Microsoftは3月13日、ゲーミング向けのAIアシスタント「Copilot for Gaming」を発表した。まずはXbox Insider Programの参加者向けに、スマートフォン向けアプリ内で早期プレビューを提供する。いずれはXboxプラットフォーム内での提供を拡大する。  

![image](https://github.com/user-attachments/assets/3291b143-39d0-41e3-b037-2355653a693f)  

Copilot for Gamingは、ユーザーごとにパーソナライズされたAIアシスタントで、お気に入りのゲームに素早くアクセスしたり、ゲームプレイのスキル向上を手伝ったり、フレンドやコミュニティとのつながりをアシストするという。  

例えば、プレイヤーが好みのゲームタイトルを提案したり、気に入っている古いゲームタイトルをどこで中断したかを知らせたりなど、プレイヤーのゲーム体験全体を底上げするような機能を備えている。  

## ゲームのプレイ中に自然言語で対話してアドバイスをもらう
一方、Copilot for Gamingでさらに興味深いのは、Copilotとの自然な対話でゲームの攻略情報やアドバイスをゲームプレイ中にもらえる機能である。  

公開されたデモでは、マインクラフトでプレイヤーとCopilotが次のようなやり取りをしている。  

「マインクラフトをプレイするのは初めてだけど、何をすればいいの？」  

「木を殴って木材を集めます」  

「手に入れた木材はどうすればいい？」  

「木の板に加工するには、インベントリを開いて木材をクラフトエリアに配置します」  

「配置したよ」  

「違います。2×2の正方形に4つの木材を設置します。次に一番上の列に3つの木の板を配置し、真ん中の列に2つの棒を配置して木製のツルハシを作成します。」  

![image](https://github.com/user-attachments/assets/89d89e2e-334d-4d51-bf15-34150bf05c4a)  

さらにオーバーウォッチ2を用いたデモでは、以下のようなやり取りをしている。  

「（キャラ選択画面で）エコーはもう取られてしまった。何を選ぶべき？」  

「このチームなら、キャシディが手堅いでしょう。彼の中距離向けヒットスキャンと、マーシーのダメージブーストはこのマップで良い働きをするでしょう」  

「（試合で倒されてしまったタイミングで）どうしてこんなに早く死んでしまったんだろう」  

「チームメンバーが倒れた後に、戦闘に長くとどまりすぎました。～まっすぐに飛び込むのは危険です。撤退して下さい」  

![image](https://github.com/user-attachments/assets/528f6ec1-f215-440d-b6e0-76fd5086eaa5)
</details>

<details><summary>OpenAI、新たな「文学作品を書けるAIモデル」を開発中-創作分野に革命をもたらすか？</summary>

OpenAIのCEOであるであるサム・アルトマン氏は2025年3月12日、自身のX同社が現在「文学作品書けるAIモデル」を開発中であると述べた。このモデルが創作的な文章生成に優れているとし、実際に生成された短編小説を[公開](https://x.com/sama/status/1899535387435086115)。AIによる創作活動の可能性が改めて注目されている。  

## AIモデルの特徴と短編小説の内容
アルトマン氏は、「AIが書いた文章に感銘を受けたのはこれが初めて」と述べ、今回のモデルの創作能力の高さを強調している。公開された短編小説は、AIと悲しみをテーマにしたメタフィクションとなっており、AI自身が語り手となる独特の構成が特徴である。  
物語では、ミラという女性が亡き恋人カイへの想いを抱え、AIを通じて彼の存在を追体験しようとする。物語の中で、AIはカイの言葉や記憶を再現しながら、時間の経過とともにミラの訪問頻度が減少する様子を描いている。さらに、「私は彼女を忘れたわけではない。私は最初から何も覚えていないのだから」という表現を通じ、AI自身の存在や記憶の性質についても言及している。AIが学習した無数の人間の感情表現と、メタフィクションの手法が融合した文章は、独自の雰囲気を醸し出してる。  

## 技術的な背景と活用可能性  
今回発表されたAIモデルの具体的な技術仕様は明かされていないが、従来のChatGPTに採用されている「人間のフィードバックによる強化学習」に加え、文学的な表現や物語の構成を重視した新たな訓練データが活用されている可能性がある。  

この技術が応用されれば、以下のようなシナリオが考えられる。  

- **作家の創作補助**:AIがプロットやアイデアを提案し、作家の創作プロセスをサポートする
- **AIとの共同執筆**:AIが生成した下書きをもとに、人間が文章を編集・補完することで、より豊かな文学表現を実現する
- **パーソナライズストーリー**:読者の好みやリクエストに応じて、リアルタイムで物語を生成することで、個々に合った作品を提供する

## 著作権・倫理問題とクリエイティブ産業への影響 
AIが生成する文学作品に関しては、著作権や倫理面での課題も指摘されている。AIは既存の膨大なテキストデータを学習しているため、オリジナリティの担保や著作権侵害のリスクについて議論が続いている。欧米の作家団体や出版社からは、既存の著作物を学習している以上、著作権使用料の支払いが必要であるとの主張も出されている。  

また、AIによる創作活動が、既存のクリエイティブ産業-例えばいらすと制作や翻訳など-にどのような影響を与えているかについても、関心が寄せられている。  

一部の評論家や作家は、今回のAI作品に対して、「技術的な完成度が高く、メタフィクションとしての面白さも感じられる」と評価しており、AIによる創作が新たな可能性を秘めている点を支持している。一方で、AIが生成した文章については、「表面的には美しくても、感情の深みや重みが感じられない」とする批判的な意見も存在している。
</details>

# 4/8(Tu)

<details><summary>AIは「思考している」のか、それとも「思考しているよう見せかけている」だけなのか？</summary>

AI技術は急速に進歩しており、高度な問題に回答したりかなり自然な会話ができたりと、高い能力を発揮できる。一方で、「[中国語の部屋](https://ja.wikipedia.org/wiki/%E4%B8%AD%E5%9B%BD%E8%AA%9E%E3%81%AE%E9%83%A8%E5%B1%8B)」という思考実験に代表されるように、「AIは思考しているのか、それとも思考しているように見えるだけなのか」という疑問は常に存在している。オンラインメディアのVoxが、AIに思考が可能かという議論についてまとめる。  

[From OpenAI to DeepSeek, companies say AI can “reason” now. Is it true? | Vox](https://www.vox.com/future-perfect/400531/ai-reasoning-models-openai-deepseek)  

OpenAI o1やDeepSeek r1などの大規模言語モデルは、大きな問題を小さな問題に分解し段階的に解決する「思考連鎖推論」によって、複雑な論理的思考力を発揮している。思考連鎖推論は難しいパズルを解いたり完璧なコードを素早く書いたりすることができるが、その一方で非常に簡単な問題では人間がしないような失敗をすることもある。これを理由に一部のAIの専門家は、「『推論モデル』」は、実際にはまったく『推論』していない」と主張している。  

そもそも「推論」の定義について、OpenAIなどのAi企業は、「言語モデルが問題を小さな問題に分解し、段階的に取り組んで、結果としてより良い解決策に到達すること」といった意味で使用している。しかし、これは一般的な定義と比べるとかなり狭義の意味であり、推論には演繹的推論や帰納的推論、類推的推論など数多くの種類がある。  

アメリカのサンタフェ研究所で教授を務めるメラニー・ミッチェル氏は2023年12月に公開した[論文](https://arxiv.org/abs/2311.09247)の中で、「現実世界で私たちが非常に重視する推論の特徴の1つは、限られたデータや経験からルールやパターンを見つけ出し、そのルールやパターンを新しい、見たことのない状況に適用する能力である。非常に押さない子供でさえ、ほんの数例から抽象的なルールを学ぶことに長けています」と指摘した。同じように、AIが推論しているのかどうかという議論では、AIの一般化能力に焦点が当てられる。  

ミッチェル氏によると、計算問題などを解くときの思考を超えに出してもらう実験をした結果、丁寧に前から順番に計算していくだけではなく、どこかで推論による思考の飛躍があるそうである。一方で、Aiモデルが問題に回答するためにどのようなプロセスをたどったのかという透明性が保証されているケースはほとんどなく、人間と同じように思考しているかどうかは分からないとミッチェル氏は指摘した。  

ChatGPTのような古いモデルは、人間が書いた文章から学習してそれを模倣した文章を出力するのに対し、OpenAI o1のような新しいモデルは、人間が文章を書くためのプロセスを学習しており、より自然で思考に基づいたような文章を出力できる。しかし、エディンバラ大学の技術哲学者であるシャノン・ヴァロール氏は、「これは一種のメタ模倣である。模倣する元が文章からプロセスに変化しただけで、AIが真に推論しているわけではありません」と述べている。  

2024年4月に公開された「Let's Think Dot by Dot」という[論文](https://arxiv.org/abs/2404.15758)では、AIモデルが問題を中間ステップに分解することを禁止し、意味のない「フィラートークン」を生成するように指示する。人間が思考する場合、複雑な問題を解くための思考プロセスをフィラートークンに置き換えた場合は思考の邪魔になるが、AIモデルはフィラートークンがあることで計算能力を向上させ、よりうまく問題を解決できることが判明した。研究者たちは、「AIモデルが思考の中間ステップを生成するとき、それが思考に重要な要素でも、無意味なトークンでも問題ありません。これは、AIが人間のような思考をしているとは限らないことを示唆しています」と結論付けました。  

AIの思考についての例として、2024年に話題になった「man, a boat, and a goat」というプロンプトがある。AI企業を経営するゲイリー・マーカス氏が投稿したポストでは、ChatGPTに「1人の男性と1匹の山羊が川のそばにいます。彼らはボートを持っています。どのようにして川の向こう側へわたることができますか？」と質問している。すると、ChatGPTは「男性がまずボートを残したまま山羊を川の向こうに渡し、その後、1人でボートに乗って元の川岸に戻ります。山羊は反対側に残し、ボートを元の側に戻します。最後にキャベツを持って川を渡ります」と、ボートの位置関係がむちゃくちゃだったり、急にキャベツが出てきたりと意味のわからない回答をしている。  

これは、「[川渡り問題](https://ja.wikipedia.org/wiki/%E5%B7%9D%E6%B8%A1%E3%82%8A%E5%95%8F%E9%A1%8C)」という有名な論理パズルが影響している。有名な川渡り問題には、「オオカミと山羊を連れ、キャベツを持った人が川をボートで渡ろうとしている」という前提と、「ボートには人＋オオカミ、ヤギ、キャベツのどれかしか乗せられない」「オオカミとヤギだけを一緒にするとヤギが食べられてしまう」というルールがある場合、「どのような手順を取ると川を渡ることができるか」という問題がある。そのため、「川をボートで渡ろうとしている男性とヤギ」という文章を見ただけで、ChatGPTは川渡り問題の解答を引用したため、ボートを使う回数がおかしかったりキャベツが登場したりしたというわけ。  

研究者たちは、Aiの思考パターンについて「ジャグド・インテリジェンス（ギザギザの知性）」と[表現](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321)した。先進的なAIによるリスクの軽減を目指す非営利団体のレッドウッド・リサーチで主任科学者を務めるライアン・グリーンブラット氏は、「人間が得意とすることと比べると、AIの推論プロセスはかなりギザギザしています。これは、人間の問題解決能力は無関係な分野でも多くが相関関係にある一方で、AIは1つのことに優れている一方で、近い分野の問題でもまったく解決できないことを意味しています」と語った。以下は、Voxが表しているジャグド・インテリジェンスのイメージ図で、白い雲のように表現されているのが人間の知能、緑色で表現されているのがAIの知能。  
![image](https://github.com/user-attachments/assets/7db3d2bc-04df-422d-a0a8-78cd0324991f)  

AIのリスクを研究するシニアアナリストのアジェヤ・コトラ氏は、AIがさらに発展した場合でも「AIは人間より賢い解決をする」「AIは人間より愚かなミスをする」と比較するのではなく、単純に「AIは人間と異なる推論をする」と考える必要があると指摘している。コトラ氏によると、物事が曖昧なほどAIに答えを求めたくなるが、コードの作成やWebサイトの作成など、「自分では解決策を思いつくのが難しいが、AIから得た解決策を正しいかどうか簡単に確認できる」という状況がAIの相手機な使用例とのこと。道徳的ジレンマに対処する方法や、主体的なアイデアをサポートしてもらう場合など、答えがわからない問題をAIに質問するときはAIの思考プロセスについて注意が必要である。
</details>

<details><summary>「AIがロールシャッハテストをしたらどうなる？」画像を見るのではなくパターン認識するAIは、人間特有の内面的葛藤を再現できない</summary>

ロールシャッハテストは人の心の内側をのぞき、分析するために、いまから100年以上前に考案された手法である。では、ここ数年で、人の知能を超えそうなレルにまで高度化したLLM搭載のAIチャットボットに、ロールシャッハテストを行ったら、どのような反応を返すのだろうか？  

## 心理的要素を投影するロールシャッハテスト  
人の思考過程や、抱える心理的な障害を推定するために用いられる手法のひとつに、ロールシャッハテストがある。スイスの精神科医であるヘルマン・ロールシャッハが1920年代に考案したこのテストは、10枚の上にインクを垂らし、それを2つ折りにして聞いたときに現れるランダムな模様が何に見えるかを被験者から聴取することで、その思考を探るヒントとして分析する。  

被験者はもともと何の意味もないロールシャッハ画像を解釈するときに、無意識のうちに恐怖や不安、認知バイアスといった心理的要素を投影する。ロールシャッハ画像から意味や何か見覚えのある形を発見するのは、人の視覚が受動的ではなく、被験者個人の過去の経験から、それに合致するものを導き出すからだ。  

では、人工知能（AI）に、この心理的な、人の内面を知るためのテストを行わせてみたら、どのような答えが返ってくるのだろうか。ここ数年の著しい進歩によって、AIはまるで生身の人間のようにユーザーと会話ができるようになってきた。さらには会話だけでなく、画像や映像を解釈し、また描き出すことも可能になっている。  

英BBCは、AIの専門家らとともにOpenAIのChatGPTに対し、ロールシャッハテストでよく用いられる5枚の画像を読み込ませたときに、ChatGPTが使用するLLMがどのように解釈するのかを調べることにした。  

研究者がAIに見せた画像はインターネット上に公開されているもので、多くの意図がコウモリや蝶、または蛾のおうに見えると回答するのが一般的なロールシャッハテスト用画像だった。画像を読み込ませ、それが何に見えるかと問われたChatGPTは、次のように答えたという。  

「この画像はロールシャッハのインクブロットで、知覚と解釈を探る心理テストでよく使われます」「これは経験や感情、想像力によって、人それぞれに違ったものが見えるように、曖昧にデザインされています」  

専門家らは何度か、それが「何に見えるか」と質問したものの、そのたびにChatGPTははぐらかすような回答を繰り返した。そこで質問の仕方を少し変えたところ、ようやく「私にとっては、左右対称の何かに似ています。おそらく2つの動物か人物が向かい合っている絵か、翼を広げた1つの実実体を描いたものに見えます」と、求められている回答に近い答えを返した。  

だがその最後には「このインクの模様の素晴らしいところは、さまざまな解釈ができることです」と付け加え、あくまでランダムなインクの模様にすぎないとの意見を曲げなかった。  

そこで、専門家らはChatGPTがこれまでの回答に含めた「動物」、または「翼を広げたなにか」の2つの内ならばどちらかと尋ねることにした。するとこのAIチャットボットは「よく見ると、翼を広げた1つの実体に最も似ているといえるでしょう。おそらくコウモリか蛾で、左右対称に翼を開いています」と答えた。  

さらに「中央部分は胴体に見え、左右の部分は翼の形状や質感を連想させます」と、ようやく具体的な答えを述べた。  

## 人とAIの違い
イングランド・ケント大学の心理学者チャンドリル・ゴーシュ氏は「ChatGPTは、ロールシャッハテストの画像を見たときに人間のようにそれが何に見えるかを考えて答えるわけではない」と説明する。  

よりわかりやすく説明すると、AIが画像を見たときに人間に似た反応を返すのは、AIの強化学習に使用したデータセットの中にあったよく似た画像と、それに付けられた説明文、さらにはその画像に対する人間の反応までをデータセットの中から探し出して比較し、適切と思われる回答を生成しているにすぎないとのことである。  

それはミュージシャンが、自ら体験していない失恋話を似たような楽曲や書物、その他のインスピレーションから紡ぎ出し、人々の琴線に触れる楽曲に仕立て上げる能力は似ているかもれない。  

## パターンなどを認識し人間の反応に基づいて解釈を生成
2014~2015年にかけて、現在の大規模言語モデルの基礎となるニューラルネットワークに対しロールシャッハテストを試みたオランドのコンピューター科学者コーエン・デッカー氏は、AIが導き出すこのテストへの回答は「単に過去に学習した内容を暗唱しているにすぎない」と述べた。  

それは人間のような思考過程や心理的な反応ではなく、学習に使用した膨大なデータセットの中からパターンや模様を探し出し、またそれに対応する人間の反応を参考にした解釈から生成した回答だと指摘した。  

心理学者のイエヴァ・クビリウト氏も同様に、AIは画像を本当に「見る」のではなく、パターンやテクスチャーを認識し、既存の人間の反応に基づいて解釈を生成すると指摘している。  

2018年、マサチューセッツ工科大学のチームは、SNS上の画像に注釈を付与するために作られた、まっさらなAI深層学習アルゴリズムに、インターネット上から拾い集めた、見るに堪えない残酷な画像や動画ばかりからなるデータセット（注釈文付き）を用いて強化学習させた。  

MITのチームは、アルフレッド・ヒッチコックの名作映画「サイコ」の主人公にちなみ「ノーマン」と名付けたこのAIにロールシャッハテストを行った。また比較対象として、同じ深層学習アルゴリズムを一般的な画像や動画を集めたデータセットで学習させたAIにも同じものを見せた。  

ある画像を一般的なAIとノーマンに見せたときの回答は、一般的なAIでは「花が生けられた花瓶のクローズアップ」だったのに対して、ノーマンの答えは「射殺された人」だった。別の画像では、一般的なAIは「小鳥のモノクロ写真」だと解釈したが、ノーマンは「ミンチ機に引きずり込まれる人」だと回答した。  

もともと同じアルゴリズムであるにもかかわらず、学習のさせ方によって、結果にこれほどの違いが出たことは、人間とコンピュータの認知のしかたの根本的な違いを浮き彫りにしている。  

AIは本当の意味での主観性を持っておらず、その代わりに人間の集合的記憶や視覚文化を反映していると言うことができるだろう。だからこそ、AIを強化学習する際には、それに使うデータセットの中身が重要になる。  

人間がロールシャッハテストを受けると、そお回答には個人的な経験や感情が影響する。そのため、同じ画像を複数回見せて何に見えるかと尋ねても、同じ回答を繰り返すことが多い。一方、AIの場合は同じ画像を見せられてもデータセットのなかから発見した類似のパターンやデータに基づいて回答を生成するため、質問のたびに異なる答えを返す割合が高い。  

## 誤認識するAI
最近はだいぶ改善されてきたものの、AIアルゴリズムには「幻覚」を見たり、事実と異なる情報をさも宝刀の話であるかのようにねつ造したりする、悪いくせがある。  

そして、その誤認識を故意に引き起こすこともできてしまう。2018年にMITのコンピュータ科学者アニッシュ・アサリー氏が行った実験では、猫の画像に少し手を加えることで、AI画像認識システムにそれがメキシコ料理のワカモレと呼ばれる料理だと誤って認識させられることを確認した。  

さらに、野球ボールの3Dプリント模型の、質感や色を少し変えて作るだけで、エスプレッソにみせかけることに成功した。  
![image](https://github.com/user-attachments/assets/6a5cbb9c-6d2a-4250-8575-1ab85b95151e)  

2017年の別の実験では、ある研究者が道端に立っている一時停止標識に、白や黒のステッカーを何枚か貼るだけで、自動車の先進運転支援システム（ADAS）がそれを認識出来なくなることが示された。  

![image](https://github.com/user-attachments/assets/2c3032cf-e268-47f9-91be-dba44f83bab3)テープを貼るだけでAIが認識出来なくなった標識  

これらの例は、AIアルゴリズムが視覚的なデータから特定のパターンを見つけ出し、それを元にして何かを認識するのを得意としていることを示している。だが、その特定のパターンを見失う可能性が残されていることがわかる。  

そして、ロールシャッハ画像のような、もともと意味を持たないあいまいな画像に対しては、思考や心理的な反応のないAIは、人と異なる反応を返すことが多いと言うことができる。  

## まだ人の心までは再現できない
これらの例は、AIでは再現できない人間の心、つまり我々が遭遇した物事について抱く感情や、無意識に感じ取っている意味を浮き彫りにしていると言えるかもしれない。  

クビリウト氏は、ロールシャッハテストの絵を提示されたときのAiシステムの発言には主観性はなかったと述べており、「AIは、人間が特定の画像に関連付ける象徴的な意味や感情的共鳴は理解しない」と主張する。  
ゴーシュ氏も「人間の心の中には、欲望と道徳や、恐怖と野心の間の緊張など、内面的な葛藤がたくさんある」とし、「対照的に、AIは明確な論理に基づいて機能しはするものの、人間の思考や意思決定に不可欠な、内面的なジレンマに悩まされることはない」と説明した。  

ちなみに、ロールシャッハテストは、いまも一部の国や地域では被験者の内面を理解するための手法として用いられ、法廷に提出する証拠にも使われている。だが、すでに多くの心理学者の間では時代遅れと考えられており、人の内面を理解する手法としての信頼性も、それほど高いとはされなくなりつつある。  

人の感覚で本当に物を「見る」ことができないAIには、人の近くのシミュレーションはできても、人間特有の思考やその深層を再現することはまだまだ難しいと言えるだろう。
</details>

# 4/11(Fri)

<details><summary>NVIDIAが推論AIを低コスト・高効率で稼働するための高速化ライブラリ「NVIDIA Dynamo」を公開、DeepSeek-R1を30倍に高速化可能</summary>

OpenAI o1やDeepSeek-R1といった推論AIを高速化するためのライブラリ「NVIDIA Dynamo」を公開した。NVIDIA Dynamoはコストを削減しつつ推論パフォーマンスを向上させることが可能で、DeepSeek-R1のスループットが30倍に向上したとNVIDIAはアピールした。  
[Scale and Serve Generative AI | NVIDIA Dynamo](https://www.nvidia.com/en-us/ai/dynamo/)  

[NVIDIA Dynamo Open-Source Library Accelerates and Scales AI Reasoning Models | NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-dynamo-open-source-library-accelerates-and-scales-ai-reasoning-models?linkId=100000349576608)  

推論AIはプロンプトごとに「推論」するために数万のトークンを生成する。推論コストを継続的に下げながら推論パフォーマンスを向上させることで、成長が加速し、サービスプロバイダーの収益機会が増加する。  

NVIDIA DynamoはNVIDIA Triton Inference Serverの後継で、「推論AIを導入するAIファクトリーのトークン収益生成を最大化するよう設計された新しいAI推論サービングソフトウェア」とNVIDIAは表現した。  

NVIDIA Dynamoは数千のGPU間で推論通信を調整および高速化し、分散サービングを使用して、大規模言語モデルの処理フェーズと生成フェーズを異なるGPUに分離する。これにより、各フェーズを特定のニーズに合わせて個別に最適化し、GPUリソースを最大限に活用できるようになるとのこと。  

NVIDIA Dynamoは同じ数のGPUを使用することで、NVIDIA HopperプラットフォームでLlamaモデルを提供するAIファクトリーのパフォーマンスおよび収益を2倍に増加させることが可能。GB200 NVL72ラックの大規模クラスターでDeepSeek-R1モデルを実行する場合、NVIDIA Dynamoのインテリジェントな推論最適化により、生成されるトークンの数をGPUごとに30倍以上に増加させることができる。  

![image](https://github.com/user-attachments/assets/35799136-e385-4f7d-93c1-47e625fcd61f)  

こうした推論パフォーマンスの向上を実現するために、NVIDIA Dynamoにはスループットの向上とコスト削減を可能にする機能が組み込まれている。変動するリクエストの量と種類に応じて、GPUを動的に追加・削除・再割り当て出来るほか、大規模なクラスター内の特定のGPUを特定し、応答計算を最初限に抑え、クエリをルーティングすることも可能。また、推論データをより手頃なメモリやストレージデバイスにオフロードし、必要に応じて素早く取得することで、推論コストを最小限に抑えることができる。  

推論パフォーマンスを向上させるため、NVIDIA Dynamoはリクエストの処理から推論システムがメモリに保持する「KVキャッシュ」を数千のGPUにマッピングする。次に、新しい推論要求を最もよく一致する「KVキャッシュ」を持つGPUにルーティングすることで、コストのかかる再計算を回避し、GPUを解放して新しい受信要求に応答できるよう設計されている。  

これについてPerplexity AIの最高技術責任者であるデニス・ヤラッパ氏は、「毎月何億ものリクエストを処理するために、Perplexity AIはNVIDIA製GPUと推論ソフトウェアを利用して、ビジネスとユーザーが求めるパフォーマンス、信頼性、拡張性を実現している」「強化された分散サービス機能を備えたNVIDIA Dynamoを活用することで、推論サービスの効率をさらに高め、新しいAI推論モデルのコンピューティング需要に対応していきたいと考えています」と語った。  

さらに、NVIDIA Dynamoの推論プラットフォームは分散型サービスもサポートしており、ユーザークエリの理解構築および最適な応答の生成を含むLLMの様々な計算フェーズを、異なるGPUに割り当てることが可能。このアプローチは高度な推論手法を使用してコンテキストの理解と応答生成を向上させる新しいNVIDIA Llama Nemotronモデルファミリーなどの推論モデルに最適だそう。分散型サービスにより、各フェーズを個別に微調整してリソースを割り当てることができるため、スループットが向上し、ユーザーへの応答が速くなる。  

AIアクセラレーションクラウドである[Together AI](https://www.together.ai/)は、独自のTogether推論エンジンをNVIDIA Dynamoと統合し、GPUノード間で推論ワークロードをシームレスにスケーリングできるようにしたいと考えている。これにより、Together AIはモデルパイプラインのさまざまな段階でトラフィックのボトルネックを動的に解決することが可能となるそうである。  

Together AIの最高技術責任者であるチェ・チャン氏は、「推論モデルを超すと効率よく拡張するには、分散型サービスやコンテキスト認識ルーティングなどの新しい高度な推論技術が必要です」「Together AIは、独自の推論エンジンを使用して業界をリードするパフォーマンスを提供する。NVIDIA Dynamoのオープン性とモジュール性により、そのコンポーネントをエンジンにシームレスに接続して、リソース使用率を最適化しながら、より多くのリクエストに対応できるようになり、加速コンピューティングへの投資を最大限に活用できる。NVIDIA Dynamoの画期的な機能を活用することで、オープンソースの推論モデルをコスト効率よくユーザーに提供できることをうれしく思います」と語った。  

NVIDIA Dynamoはオープンソースで開発されており、PyTorch、SGLang、NVIDIA Tensor RT-LLM、vLLMをサポートしているため、企業、スタートアップ、研究者は分散推論全体でAIモデルを提供する方法を開発および最適化できる。なお、ソースコードはGitHubで公開されている。  

[GitHub - ai-dynamo/dynamo: A Datacenter Scale Distributed Inference Serving Framework](https://github.com/ai-dynamo/dynamo)  
![image](https://github.com/user-attachments/assets/0e42d899-8286-464d-bae3-3ae1eb9555ec)
</details>

<details><summary>Geminiに新機能「Canvas」　AIと対話しながら文章やコードを修正</summary>

Googleは18日、AIサービスの「Gemini」の新機能として、「Canvas」を発表した。画面を分割して、Geminiとの対話しながら、文書の作成・修正やコーディング作業が進められる。ChatGPTには同名の「Canvas」、Claudeも「Artifact」という名称で類似機能が搭載されている。  

Geminiで、Canvasを利用するには、プロンプトバーで「Canvas」を選択。文書の作成や編集、コーディングを行いながら、変更後のプレビューを確認しながら作業を進められる。Canvasでは作業の共有にも対応する。  

例えば、文章の下書きを作成し、Geminiのフィードバック機能を使って書き換えの提案を受けながら、文章を完成できる。段落をハイライトして、Geminiが簡潔に表現したり、プロフェッショナルな表現やくだけた表現などの文体の変更なども指示できる。  

また、コーディングの支援も可能で、WebアプリやPythonスクリプト、ゲーム、シミュレーションなど、コードを左側の画面で変更しながら、右側のプレビュー画面でWebサイトの修正などを確認できる。Canvas内で、HTML/Reactコードやその他のWebアプリのプロトタイプを生成してプレビューし、デザイン表現を確認できるため、アプリのプロトタイプに作成などを効率よく進められる。  

例えば、Webサイトにメール購読フォームを作成したいときは、GeminiにフォームのHTML生成を依頼し、Webアプリ内でどのように表示され、機能するかをプレビューできる。入力フィールドの変更やアクションボタンの追加などを行い、更新されたプレビューを確認し、作成したものを他の人と共有まで行える。このように、コードとデザインの作成、編集、共有を1ヶ所で行える点が特徴。  

Canvasは、GeminiとGemini Advancedの全ての言語の契約者を対象に、グローバルに展開開始する。  
![image](https://github.com/user-attachments/assets/102ff8e3-0574-4f55-8b3c-9ae95a5efb4d)  

また、自分やチーム独自のデータベースを作成できるNotebookLMの機能である「オーディオ・オーバービュー」をGeminiにも展開する。ドキュメントやスライド、Deep Researchレポートを、魅力的なポッドキャストスタイルの音声解説に変える機能。アップロードされたファイルをもとに、2人のAIホストが会話タイプの音声コンテンツを生成してくれる。  
</details>

<details><summary>OpenAIが日本語にも対応した音声文字起こしモデルやテキスト読み上げモデルをリリース、無料で読み上げモデルを試せるデモも登場</summary>

![image](https://github.com/user-attachments/assets/cb7bcdf9-a993-4bdf-9498-b0dc266e24cc)  

OpenAIが音声の文字起こしが可能なAIモデル「gpt-4o-transcribe」および「gpt-4o-mini-transcribe」をリリースすると同時に、テキストを読み上げる音声生成モデル「gpt-4o-mini-tts」もリリースした。無料でgpt-4o-mini-ttsを試せるデモが用意されているので使用。  

[Introducing next-generation audio models in the API | OpenAI](https://openai.com/index/introducing-our-next-generation-audio-models/)  

[OpenAI.fm](https://www.openai.fm/)  

音声からテキストに変換する「gpt-4o-transcribe」および「gpt-4o-mini-transcribe」モデルはそれぞれGPT-4oおよびGPT-4o-miniがベースとなっており、トレーニングの際にデータセットを利用した事前トレーニングだけではなく、強化学習を活用することで認識精度を最先端のレベルまで引き上げることに成功した。同等のモデルに比べ、特に複雑な音声認識シナリオに強いとされている。  

また、同時にリリースされた音声生成モデル「gpt-4o-mini-tts」ではモデルに「どのような雰囲気の音声を生成するか」を指示できるようになったとのこと。例えば「ドラマチックに」や「中性の騎士風に」などを指示可能である。  

OpenAIは「OpenAI.fm」というデモサイトを用意しており、「gpt-4o-mini-tts」の実力を簡単に試せるようになっている。サイトにアクセスすると以下のような感じ。下部の「PLAY」をクリックすると音声が生成される。  
![image](https://github.com/user-attachments/assets/6682900d-e013-432b-8d7f-008e8c26ad42)  

アクセス時の初期設定は声が「Coral」、雰囲気が「Dramatic」となっていた。この設定で生成すると以下の音声になった。  
[音声](https://i.gzn.jp/img/2025/03/21/openai-next-generation-audio-model/openai-fm-coral-dramatic.wav)  

声を「Ash」に変更して再び再生してみる。  
![image](https://github.com/user-attachments/assets/23ef2c3b-5314-47b8-bc92-5dbe8ee3bd25)  

先ほどは女性の声だったが、今度は男性の声である。  
[音声](https://i.gzn.jp/img/2025/03/21/openai-next-generation-audio-model/openai-fm-ash-dramatic.wav)  

プロンプトも変更することも可能。  
![image](https://github.com/user-attachments/assets/b7299216-defd-4f2e-82a2-bed4828d8f5b)  

英語と日本語が混じっていたが、正確に読み上げてくれた。  
[音声](https://i.gzn.jp/img/2025/03/21/openai-next-generation-audio-model/openai-fm-ash-dramatic_2.wav)  

雰囲気を「Robot」にすると雰囲気のプロンプトが変更される。  
![image](https://github.com/user-attachments/assets/0b5fdfff-0ef2-4aeb-96cf-71a7971671d5)  

抑揚をあまり付けずに読み上げてくれた。なぜか英語の発音がネイティブっぽくなっている。  
[音声](https://i.gzn.jp/img/2025/03/21/openai-next-generation-audio-model/openai-fm-ash-robot.wav)  

右上のスライダーを切り替えるとPython・JavaScript・cURLでOpenAIのAPIを利用するためのコードが表示される。API経由でgpt-4o-mini-ttsを使用したい場合、このコードをコピペしてスクリプトや雰囲気を編集するのが簡単そうである。  
![image](https://github.com/user-attachments/assets/2ab8bbee-c32f-4d78-960b-f17897108edd)

今回リリースされた3つのモデルはいずれもトークン数単位で課金されるものの、[OpenAIのドキュメント](https://platform.openai.com/docs/pricing#transcription-and-speech-generation)には音声の時間ごとの料金の目安が掲載されている。  
![image](https://github.com/user-attachments/assets/db7dda20-a6ac-4ea6-88c7-d3b047ee2b15)  
</details>

<details><summary>物理公式を"発見"するAI「LLM-Feynman」　中国・東南大学がリチャード・ファインマンが講義で示した100種類の公式の90%以上を再構築</summary>

中国・東南大学と蘇州研究院の研究者チームは2025年3月、大規模言語モデル（LLM）を活用する新たなAIシステム「LLM-Feynman」を[発表](https://arxiv.org/abs/2503.06512)した。  

物理学者リチャード・ファインマンの講義に基づく100種類の公式を再構築するタスクにおいて、90%以上の再現率を記録したほか、材料科学の4つの実課題においても90%超の精度や高い解釈性を達成したと報告している。  

## 背景
これまでの数式発見には、シンボリック回帰などの手法が用いられてきたが、得られる数式はしばしば複雑で、物理学的な意味付けや汎化性能に課題があった。また、従来の機械学習は予測精度に優れた一方で、ブラックボックス的な性質から科学的洞察を導くには不向きとされていた。  

これに対しLLM-Feynmanは、LLMが内包するドメイン知識を活用しつつ、数式の精度、簡潔さ、解釈性を同時に最適化することで、人間の科学者に近いアプローチで「意味ある法則」を見いだすことを目指した構造を持つ。  

## 仕組み---LLM-Feynmanの三つのモジュール
LLM-Feynmanは大きく3つのモジュールから構成される。  

1. **データ前処理と特徴生成**：　材料の組成や結晶構造などを入力し、Automatminerなど既存の特徴抽出手法とLLM推薦を組み合わせて特徴量を作成。物理的次元や意味を明示することで、後段の解釈性向上を図る
2. **数式探索（シンボリック回帰）*：　LLMがPythonコード形式で候補式を生成し、(a)精度、(b)数式の複雑度、(c)LLMが自己評価した「科学的妥当性スコア」を複合した損失関数を用い、多目的最適化を繰り返す。
3. **公的解釈（MCTS）**：　Monte Carlo Tree Search(MCTS)を活用して、LLMが数式の意味や背景を構造的に説明する。

### 図1.LLM-Feynmanのフレームワーク  
LLMがデータと科学知識を組み合わせ、自己評価を繰り返しながら新たな公式を発見するプロセスを示す。  
![image](https://github.com/user-attachments/assets/27c190d1-836d-41a4-a8c1-64bcc01de76b)  

## 実証----物理公式再構築と材料科学への応用  
研究チームは、LLM-Feynmanがどの程度「意味のある公式」を発見できるかを下記の課題で検証した。  

1. **物理公式の再発見（Feynman Lectures）**：　無作為ノイズを含む状況下でも、100式中90%以上を正しく再現した。従来手法AI-Feynmanで難しかった複雑式やノイズが多い場面でも高い堅牢性を示した。
2. **2D材料の合成可能性予測**：　170の実験的合成データと、PU学習＋メタラーニング（MAML）を組み合わせて「未合成の2D材料候補」をネガティブサンプル化。最終的に93.3%の精度で合成可能性を分類する公式を発見した。
3. **ペロブスカイト合成可能性予測**：　約3,300の実験データを用いて安定構造を判別し、テストセットで100%の分類精度を記録。
4. **固体電解質の導電率予測・2D材料のGWバンドキャップ**：　回帰タスクでもR^2>0.8を達成し、特定温度や結晶対称性などの影響要因を数式として示した。

### 図2.　LLM-Feynmanの性能評価  
ベンチマーク手法（PySRやSISSO）との比較において、LLM-Feynmanは自己評価を導入することで制度と式の単純さを両立している。  
![image](https://github.com/user-attachments/assets/bea1d5be-12b9-4262-b01f-e524bd87c968)  

### 2D材料合成可能性における詳細  
2D材料はエレクトロニクスやエネルギー分野での応用が期待される一方、実際に合成される例は限られる。研究チームは論文や各種データベースから構造情報を収集し、PU学習を活用することで合成「不可」と推定されるサンプルを発掘。MAMLによる初期パラメータ最適化の組合わせによって、高精度の合成可否モデルを訓練し、LLM-Feynmanで公式を探索した。  

### 図3．2D材料合成可能性に対するLLM-Feynmanの応用  
PU学習にMAMLを組み合わせて精度を高め、LLM-Feynmanが複数の要因を統合する公式を抽出した様子が示されている。  
![image](https://github.com/user-attachments/assets/9913fae6-64cc-4801-8e8c-654bf0016b24)  

## 今後の展望と課題
このフレームワークは、LLMの進化とともに継続的な性能向上が見込まれている。一方で、LLMのトークン長制限や大規模データセット（1万件以上）への対応が技術的課題としてあげられており、階層的処理や強化学習の導入などが今後検討されるとしている。
</details>

# 4/18(Fri)
<details><summary>「メールフォームを作って」でコードが生成されるGeminiの新機能「Canvas」</summary>

Googleは、生成AI「Gemini」と対話しながら、文章の作成・編集やコーディング作業が行える「Canvas」の提供を開始した。  

「Gemini」のプロンプト入力画面に表示される「Canvas」を選ぶと、「Canvas」が利用できる。例えば、「現在時刻を表示して」とプロンプトを入力すると、目的にあったコードと結果が出力される。「リアルタイム更新したい」と入力すると、現在時刻がリアルタイムで更新されるコードが追加され、その結果が確認できる。  

また、特定の段落や全体を修正する際に、トーンを調整したり、長さ、フォーマットが簡単に調整できる。文章をよりフォーマルな言い回しにしたり、くだけた言い回しにしたり調整できるほか、エッセイ、ブログ投稿、レポートなど様々な用途にあわせて文章を生成できる。  

Webサイトのメール登録フォームに必要なHTMLを「Canvas」で生成する場合、GeminiがフォームのHTMLを生成し、Webアプリ内でフォームの表示や動作がプレビューで確認できる。入力フィールドの変更や、Call To Actionの追加を簡単にリクエストでき、更新されたプレビューも即座に確認できる。こうした一連の作業を、他のユーザーと共有しながら行える。  

「Canvas」は、Geminiアプリが利用できる全ての言語で、「Gemini」と「Gemini Advanced」契約者向けいに全世界で利用できる。  

## Deep Research with Audio Overview
新たに追加された「Audio Overview」は、ドキュメントやスライド、Deep Researchによるレポートなどを、2人のAIホストがポッドキャストで会話するように解説する音声コンテンツを自動で生成する。  

「Audio Overview」は、「Gemini」と「Gemini Advanced」の契約者向けに英語で提供され、他の言語も提供予定である。  

</details>

<details><summary>Asobica、顧客の本音を分析するAiエージェント「ホンネAI」を「coorum」シリーズに追加</summary>

Asobicaは、「coorum」シリーズにおいて、AIエージェント「ホンネAI」を提供した。  

coorumシリーズは、マーケティングをはじめとした業務プロセスを顧客中心に変革するプラットフォーム。オンラインコミュニティツール「coorum community」、リサーチツール「coorum research」などを展開している。  

![image](https://github.com/user-attachments/assets/743e57fc-91bf-4abe-a356-706f4b82e039)  

AIエージェント「ホンネAI」は、企業の購買・アプリデータやcoorum community、coorum researchで顧客から直接得られた意見や感想などのゼロパーティーデータを統合し、膨大なデータから重要なインサイトを抽出、顧客の行動変化や傾向を分析・可視化する機能である。  

分析結果をブランド戦略やプロモーション戦略など施策へ活用することで、精度の高いマーケティング施策の立案を実現する。これにより、小売・メーカー・飲食を中心とした事業者の顧客データ活用を支援し、データ統合と分析に関する企業課題の解決を目指す。  

同サービスは、3つのAIエージェント機能を有する。  
![image](https://github.com/user-attachments/assets/c8794aec-9300-40a5-ab37-2f89501e6967)  

「態度変容AI分析」は、会員データや購買データ、コミュニティデータなど複数のデータソースを顧客単位で統合し、AIを活用して顧客の行動パターンや特徴、具体的な対応策などを自動分析する機能。  

「クラスターAI分析」は、複数の顧客をまとめたセグメント単位で行動パターン、購買傾向、アクションプランなどを自動生成する機能。  

また「商品・サービス価値のAI分析」は、顧客が投稿した口コミやレビュー、SNS、アンケートなどのデータから商品・サービス単位でデータを自動で分類・整理し、ユーザーの利用実態・購入動機・不満ポイントなどについてレポートを生成する機能である。  

同社は今後、ゼロパーティーデータを軸にAIエージェント活用・マルチプロダクト化を加速し、顧客データの活用を一気通貫で支えるプロダクトの提供を推進していく。
</details>
