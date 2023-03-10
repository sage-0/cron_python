from typing import Union
from fastapi import FastAPI
from cronjob import cronjob

app = FastAPI()

@app.get("/")
def read_root():
    return {"statuscode": "400"}

@app.post("/swich/{switch}")
def read_item(switch: str):
    if switch == "on":
        cronjob(switch)
        return "enable"
    elif switch == "off":
        cronjob(switch)
        return "disable"