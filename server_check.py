import subprocess
import requests
from discordwebhook import Discord
import time
import os
from dotenv import load_dotenv
load_dotenv()

hosts = ["192.168.0.201", "192.168.0.202"]

def notify(host):
    payload = {'message':'\n'+f'{host}'}  
    headers = {'Authorization': 'Bearer ' + str(os.getenv('line_token')) }
    requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)

    discord = Discord(url=os.getenv('discord_url'))
    discord.post(content=f"<@&1044982707144368180>\n{host}が死んでいます")

def check_server(hosts):
    diedLists = []
    for host in hosts:
        res = subprocess.run(
            ["ping", host, "-c", "1", "-W", "300"], stdout=subprocess.PIPE)
        diedLists.append(
            True) if res.returncode == 0 else diedLists.append(False)
    return diedLists





for i, r in enumerate(check_server(hosts)):
    if r == False:  # サーバーが死んでいる場合
        time.sleep(10)
        for n, re in enumerate(check_server(hosts)):
            if re == False:
                notify(hosts[n])