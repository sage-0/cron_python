import subprocess
import requests
from discordwebhook import Discord
import time

hosts = ["192.168.0.201", "192.168.0.202"]


def notify(host):
    payload = {'message':'\n'+f'{host}'}  
    headers = {'Authorization': 'Bearer ' + 'pWuEO27O8VdZ2mdogIVjxfSTVbEjf2EPrKBEKYcSEVV' }
    requests.post('https://notify-api.line.me/api/notify', data=payload, headers=headers)

    discord = Discord(url="https://discord.com/api/webhooks/1044980421588426833/J6_9t0abQdgAYweP8yX_gzEP7aTKDRbNNx5ZR1azp3Mcw6TrN-3-XbxnLSIYz-pTNzaz")
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