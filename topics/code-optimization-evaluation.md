# コード最適化の「改善率」を読む前に

IRの命令数が減った。では、プログラムの実行も速くなったのか。

ここを飛ばすと、違う目的の研究を同じ順位表へ入れてしまう。コンパイラのパスを選ぶ研究と、ソースを書き換える研究では、動かせる範囲も正しさの確かめ方も違う。まず出力と測定対象をそろえて読むためのノート。公開論文の比較から考えたもので、モデルを再実験した結果ではない。

## 何の10%なのか

| 指標 | 直接測っているもの | そこからは分からないこと |
| --- | --- | --- |
| IR命令数 | 中間表現に含まれる命令の個数 | そのまま実行時間には換算できない |
| バイナリサイズ | 指定した出力部分のバイト数 | メモリ使用量や実行速度の全体 |
| 実行時間 | 指定環境・入力での経過時間 | 別の入力や機器でも同じだけ改善するか |

たとえば「10%改善」は仮の数字だが、命令数の10%と時間の10%では答えたい問いが違う。表へ転記する前に、何を、何の単位で、何と比べた数字かを書いておく。

**Large Language Models for Compiler Optimization**では、LLVMのパス順序を選び、`-Oz`に対するIR命令数の削減を評価する。論文も命令数をバイナリサイズの不完全な代理指標として扱っている。[1] **Meta LLM Compiler**のフラグ調整もサイズ最小化が目的で、変換を実行するのはコンパイラ。生成したパス列の検査と差分テストを併用している。[2]

一方、**Performance-Aligned LLMs**では生成・書き換えたソースの正確性と速度を評価する。ここでも`pass@k`と、試行回数を含む速度指標は同じ意味ではない。[3] 同じ「コードを良くする」研究でも、この辺りで比較の道筋が分かれる。

![ソースの変更とコンパイラ判断の変更を分け、正確性を確かめてから実行時間とコードサイズを別々に測る図](../assets/diagrams/optimization-objectives.svg)

比較の手順を整理した概念図。矢印の先へ進めば性能が上がるという図ではなく、実測値も含めていない。

## どこまで変更してよいか

ソースを書き換えるなら、アルゴリズムやデータ構造まで変えられる。IRの変換では型や制御フローを扱い、アセンブリの変換では命令セットやABIが制約になる。同じIRを入力していても、出力が新しいIRなのかコンパイラのパス列なのかで課題は変わる。

このため、変換の段階、正しさの条件、目的指標、探索予算、実行環境をそろえてから比較したい。たとえば[IRCoder](../papers/2024/README.md#ircoder)はIRによる多言語コード生成の改善を調べているが、そこから生成物の高速化までを結論にはできない。[4] ACPOはコンパイラ内の判断をMLで置き換える枠組みで、LLM手法の結果として一括集計するものでもない。[5]

容量が厳しい組込み用途ならサイズが先に来る。長時間の計算なら、実行時間に加えて最適化に使う時間も効いてくる。変更範囲を抑えるためにフラグ選択から試す案はあるが、それで目的に届くかは別途測る必要がある。アルゴリズムを変えたいなら、ソースまで対象にする理由が生まれる。

## 最良の一つを出すまでに何回試したか

一発で出たコードと、多数の候補から最速だけを選んだコードを比べるなら、候補を選ぶ費用も結果の一部になる。モデル版、プロンプト、温度、候補数、再試行、ツール呼び出しを保存する。選択に使った入力と、最後に評価する入力は分けておく。

ここで気になるのは、速い候補だけを残したときに消える失敗だ。誤答、クラッシュ、時間切れは何件あったか。正解した候補の速度と、全体で正解を出せた割合を並べないと、使う際の見通しが立たない。

実行時間、出力サイズ、メモリ使用量は別々に残す。推論・探索・検証にかかる時間も、生成物の実行時間とは別に残す。繰り返し使う処理なら、一回あたりに浮く時間で最適化費用を回収できるかを考えられる。短い処理を一度しか動かさない用途なら、同じ改善率でも判断は変わる。

## 測る前に固定すること

以下は各論文を読んだ上での評価案で、共通ベンチマークの仕様ではない。

**どこまで同じ答えならよいか。** 入力範囲、出力、副作用、例外、整数の桁あふれ、浮動小数点の許容誤差を決める。コンパイル成功とテスト通過は別々に記録する。有限のテストを通ったことから、全入力での同値性までは言えない。

**何を基準にするか。** 元コード、入力、コンパイラ版をそろえる。ソースを書き換えたなら、元コードも同じ最適化設定でコンパイルする。フラグを探索したなら、許したパス集合と、同じ目的の標準設定・探索法を明記する。IRやアセンブリを使う場合は、その対象環境と検証手段も要る。

**測定の揺れをどう見るか。** CPU/GPU、OS、スレッド数、入力サイズを固定し、ウォームアップして順序を変えながら反復する。全測定値とばらつきを残す。ただし、ばらつきが小さくなっても、偏った測り方が直ったとは限らない。LLVMの測定指針もノイズと偏りを分けている。[6]

## 整数列の合計で、比較器だけを小さく作る

手順を追うための例として、ループによる合計と手書きの`sum`を比べる。Python 3の標準ライブラリだけで動くが、このノートでは速度を測定していない。LLMの比較に使うなら候補関数をモデルの出力に替え、採用候補だけでなく全候補と生成条件を残す。

```python
import json
import platform
import statistics
import sys
import time


def baseline(xs):
    total = 0
    for x in xs:
        total += x
    return total


def candidate(xs):
    return sum(xs)


functions = {"baseline": baseline, "candidate": candidate}
data = tuple((17 * i + 3) % 1000 - 500 for i in range(100_000))
cases = [(), (0,), (-1, 1), (2**80, -2**80, 7), data]
for f in functions.values():
    for xs in cases:
        assert f(xs) == baseline(xs)
    for _ in range(3):
        f(data)

samples = {name: [] for name in functions}
expected = baseline(data)
for round_id in range(15):
    order = list(functions) if round_id % 2 == 0 else list(reversed(functions))
    for name in order:
        start = time.perf_counter_ns()
        for _ in range(20):
            result = functions[name](data)
        elapsed = time.perf_counter_ns() - start
        assert result == expected
        samples[name].append(elapsed / 20)
print(json.dumps({"python": sys.version, "os": platform.platform(),
                  "median_ns": {k: statistics.median(v) for k, v in samples.items()},
                  "samples_ns": samples}, indent=2))
```

入力の作成と正解の検査は計時の外に置いた。比率を出すなら「基準の中央値÷候補の中央値」と定義する。同じマシン・Python版で実行し、CPU型番と電源設定も記録する。

この小例で分かるのは、指定した整数列を、温まったキャッシュのもとで処理する場合の比較まで。入力分布を替えたらどうなるか、別のPython版でも同じかは、別に測る問いとして残る。未検査の生成コードを入れる場合は隔離環境で実行する。

既知のベンチマークで勝った場合も、未知入力や別のCPUへの保証は増えていない。学習データとの重複が分からなければ、その点も未確認として結果と一緒に残す。改善率だけを転記するより、次に試す条件が見える形にしたい。

出典再確認：2026-10-06。以下の公開論文と公式文書を参照した。比較器の速度測定や、各手法の追試は行っていない。

## 次に読む既存メモ

[MLGOの図解ノート](../papers/2021/mlgo.md)では、ソースを書き換える生成器を使わず、コンパイラ内の判断を学習する例を扱う。学習と利用時の推論を分けて考える入口になる。

1. [Large Language Models for Compiler Optimization](../papers/undated.md#llm-compiler-optimization)：パス選択とIR命令数の関係
2. [Meta LLM Compiler](../papers/undated.md#meta-llm-compiler)：サイズ評価と生成パス列の検査
3. [Performance-Aligned LLMs](../papers/2024/README.md#performance-aligned-llms)：正確性・速度・試行回数の扱い
4. [IRCoder](../papers/2024/README.md#ircoder)：IRを学習することと高速化の違い

## 出典と確認範囲

- [1] [Cummins et al., Large Language Models for Compiler Optimization, arXiv:2309.07062v1](https://arxiv.org/pdf/2309.07062v1)：II、IV-B・D。目的指標、比較基準、生成コード評価。
- [2] [Cummins et al., Meta Large Language Model Compiler, arXiv:2407.02524v1](https://arxiv.org/html/2407.02524v1)：2.2、3.1、5.1。バイナリサイズの定義、パス選択と正確性確認。
- [3] [Nichols et al., Performance-Aligned LLMs for Generating Fast Code, arXiv:2404.18864v1](https://arxiv.org/html/2404.18864v1)：VI、VII-A・D、VIII。指標、比較モデル、評価条件。
- [4] [Paul et al., IRCoder, ACL 2024](https://aclanthology.org/2024.acl-long.802.pdf)：4、5。多言語生成・理解の評価。
- [5] [ACPO: AI-Enabled Compiler-Driven Program Optimization, arXiv:2312.09982v1](https://arxiv.org/html/2312.09982v1)：4.2、5.1.1。コンパイラ内の判断とMLモデル構成。
- [6] [LLVM公式文書：Benchmarking tips](https://llvm.org/docs/Benchmarking.html)：Introduction、General。反復測定とノイズ・偏りの区別。

## 関連する横断ノート

- [点群評価の実務](point-cloud-evaluation.md)：モデル比較でも、探索・選択に使うデータと最終評価を分けて考える。
- [形式証明の検証](formal-proof-validation.md)
- [CADと3D表現の選び分け](cad-representations.md)

[テーマ別の入口へ戻る](README.md)
