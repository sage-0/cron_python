from typing import Union
from fastapi import FastAPI
from crontab import crontab

app = FastAPI()

@app.get("/")
def read_root():
    return {"statuscode": "400"}

@app.post("/swich/{switch}")
def read_item(switch: Union[str, int]):
    if switch == "on":
        crontab(switch[0])
        return {"statuscode": "400"}
    elif switch == "off":
        crontab(switch[0])
        return {"statuscode": "400"}