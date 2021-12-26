# SchedulingViewer
JSON形式でスケジューリング結果を受け取って描画するツールです。

## 使い方
python3 scheduling_viewer.py [入力JSONファイル] [出力先HTMLファイル]
- 引数なしの場合のデフォルトの入力: sample.json
- 引数なしの場合のデフォルトの出力: output.html

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
