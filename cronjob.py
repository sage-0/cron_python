from crontab import CronTab
import api
def cronjob(api: str):
    cron = CronTab(user=True)
    job = cron.find_command('sh /home/sage/cron_python/cronjob.sh')
    if api == "on":
        job.setall('*/30 * * * *')
    elif api == "off":
        job.setall(None)
    cron.write()