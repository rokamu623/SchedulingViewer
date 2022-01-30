# SchedulingViewer
JSON形式でスケジューリング結果を受け取って描画するツールです。

## 使い方
python3 scheduling_viewer.py [入力JSONファイル] [出力先HTMLファイル] [表示倍率]
- 引数なしの場合のデフォルトの入力: sample.json
- 引数なしの場合のデフォルトの出力: output.html
- 引数なしの場合のデフォルトの倍率: 0(自動調節)

表示倍率の引数に整数または小数を入力することで、出力するグラフの表示倍率が変わります。
引数0を与えるとある程度見やすいように自動調整します。
コマンドライン上の以下の出力により、自動調整の倍率が分かります。
```
ex_rate    : auto_fix
ex_rate    : 0.1
```

入力ファイルはJSON形式に則った以下のフォーマットのファイルを使用すること。<br>
また、sample.jsonはフォーマットに則ったサンプルの入力ファイルである。
```
{
    "coreNum": (int),
    "makespan": (int),
    "taskSet": [
        {
            "coreID": (int),
            "taskName": (str),
            "startTime": (int),
            "executionTime": (int)
        },
        {
            "coreID": (int),
            "taskName": (str),
            "startTime": (int),
            "executionTime": (int)
        },
        ...
    ]
}
```
