from typing import Union
from fastapi import FastAPI
from cronjob import cron_job
from cronjob import cron_status

app = FastAPI()

@app.get("/")
def read_root():
    status = cron_status()
    if isinstance(status, bool):
        return "enable" if status else "disable"
    else:
        return status

@app.post("/switch/{switch}")
def read_item(switch: str):
    if switch == "on":
        status = cron_job(switch)
        if status == "success: job enabled":
            return "enable"
        else:
            return status
    elif switch == "off":
        status = cron_job(switch)
        if status == "success: job disabled":
            return "disable"
        else:
            return status
