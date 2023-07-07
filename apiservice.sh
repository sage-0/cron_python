cd /home/sage/cron_python
#do
/usr/bin/gunicorn -c /home/sage/cron_python/config.py api:app
echo "起動しました"
