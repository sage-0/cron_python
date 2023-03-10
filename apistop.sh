#!/bin/sh

# ワーカー数設定
readonly worker=2
# プログラムが配置されているディレクトリへ移動
cd /home/sage/cron_python
# PID取得
pid=`cat prod.pid`
# プロセスを取得
data=`lsof -i:8000`
# プロセス存在確認
if [ -n "$data" ]; then
        # ワーカー数だけループしてkill
        for i in `seq 0 $worker`
        do
                process_id=$((pid + i))
                echo "${process_id} をkillします"
                kill -9 $process_id
        done
else
        echo "プロセスが存在しないため終了します"
fi
