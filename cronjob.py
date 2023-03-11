from crontab import CronTab


def get_cron_job():
    cron = CronTab(user=True)
    for job in cron:
        if job.command == 'sh /home/sage/cron_python/cronjob.sh':
            return job
    return None


def cron_status():
    job = get_cron_job()
    if job:
        return job.is_enabled()
    return "error: job not found"


def cron_job(api: str):
    job = get_cron_job()
    if not job:
        return "error: job not found"
    if api == "on":
        job.enable(True)
    elif api == "off" and job.is_enabled():
        job.enable(False)

    cron = CronTab(user=True)
    cron.write()
    return "success"
