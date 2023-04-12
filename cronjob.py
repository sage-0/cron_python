from crontab import CronTab

def cron_status():
    cron = CronTab(user=True)
    for job in cron:
        if job.command == 'sh /home/sage/cron_python/cronjob.sh':
            if job:
                return job.is_enabled()
        else:
            return "error: job not found"

def cron_job(api):
    cron = CronTab(user=True)
    for job in cron:
        if job.command == 'sh /home/sage/cron_python/cronjob.sh':
            if not job:
                return "error: job not found"
            if api == "on":
                if not job.is_enabled():
                    job.enable(True)
                    cron.write()
                    return "success: job enabled"
            elif api == "off":
                if job.is_enabled():
                    job.enable(False)
                    cron.write()
                    return "success: job disabled"
            else:
                "error: invalid input"