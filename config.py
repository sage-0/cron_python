
# 実行するPythonがあるパス
pythonpath = './'
# ワーカー数
workers = 2
# ワーカーのクラス、*2 にあるようにUvicornWorkerを指定 (Uvicornがインストールされている必要がある)
worker_class = 'uvicorn.workers.UvicornWorker'
# IPアドレスとポート
bind = '0.0.0.0:8000'
# プロセスIDを保存するファイル名
pidfile = './prod.pid'
# デーモン化する場合はTrue
daemon = True
# エラーログ
errorlog = './logs/error_log.txt'
# プロセスの名前
proc_name = 'proxy_manager_api'
# アクセスログ
accesslog = './logs/access_log.txt'
