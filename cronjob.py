from crontab import CronTab
#import api
def cronstatus():
    cron = CronTab(user=True)
    job = None
    for j in cron:
        if j.command == 'sh /home/sage/cron_python/cronjob.sh':
            job = j
            break
    if job is None:
        return "error: job not found"
    return job.is_enabled()
# def cronjob(api: str):
#     cron = CronTab(user=True)
#     job = None
#     for j in cron:
#         if j.command == 'sh /home/sage/cron_python/cronjob.sh':
#             job = j
#             break

#     if api == "on":
#         job.enable(True)
#     elif api == "off":
#         if job.is_enabled():
#             job.enable(False)
#     cron.write()

print(cronstatus())