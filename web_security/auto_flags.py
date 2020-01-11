# -*- coding: utf-8 -*-
# author = 'K0ctr'

import requests
import json
# 比赛ID
gameid = "VmEK8aWQTwWUswf-MksxXA"
# 战队ID
teamId = "QH1wg19yTom9EzN8MMspoA"
# 用户ID
userId = "V2j-jJ_iTeCcLczt_mYGpQ"

url = "http://192.168.1.31/submitFlags"
with open('flags.txt','r') as flags:
    for flag in flags:
        print(flag)
        data = {"matchId": gameid, "teamId": teamId, "userId": userId, "answer": flag}
        requests.post(url, data=json.dumps(data))
        requests.post(url, data=data)#json.dumps(data))


