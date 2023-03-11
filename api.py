from typing import Union
from fastapi import FastAPI
from cronjob import cronjob
from cronjob import cronstatus

app = FastAPI()

@app.get("/")
def read_root():
    if cronstatus() == True:
        return "enable"
    elif cronstatus() == False:
        return "disable"
    elif cronstatus() == "error: job not found":
        return "error: job not found"

@app.post("/swich/{switch}")
def read_item(switch: str):
    if switch == "on":
        cronjob(switch)
        return "enable"
    elif switch == "off":
        cronjob(switch)
        return "disable"