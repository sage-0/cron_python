from crontab import CronTab
import api
def cronjob(api: str):
    cron = CronTab(user=True)
    job = None
    for j in cron:
        if j.command == 'sh /home/sage/cron_python/cronjob.sh':
            job = j
            break

    if api == "on":
        job.setall('*/30 * * * *')
    elif api == "off":
        job.setall(None)
    cron.write()