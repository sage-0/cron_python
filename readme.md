# 概要
このプログラムはlinuxのcrontabにすでに登録されているタスクの有効・無効をAPIを通してできるようにしたものとpythonでサーバーにPingを打ちサーバーの生存状態を簡易的に監視するプログラムが含まれています。
#### 忙しい人のために
***
- 生存状態確認プログラム server_check.py
- crontabの有効・無効および状態確認 cronjob.py
- api.py
***

# トークン情報
トークン情報は`Raspberry piのcron_python/.env`に保存してください。
# <span style="color: red; ">注意</span>
 作業する際は各自Branchを建てて作業すること！

# ![起動](https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200)
`uvicorn api:app --reload --host 0.0.0.0 --port 8000`
このリポジトリをラズパイとかにクローンして上のコマンドを`cron_python/`の中で実行すると任意のIPアドレスでAPIにアクセスできるようになります。
