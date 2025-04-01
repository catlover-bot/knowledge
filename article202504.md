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
