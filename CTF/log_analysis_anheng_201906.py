# -*- encoding:utf-8 -*-
# Author: Koctr


from urllib import parse

with open('access.log', 'r', encoding='utf-8') as log:
    with open('access_url_decode.log', 'w', encoding='utf-8') as log_ayalysis:
        for line in log:
            log_ayalysis.write(parse.unquote(line))

flag = ""
with open("access_url_decode.log", 'r', encoding='utf-8') as log:
    log_text = log.readlines()

for i in range(len(log_text)):
    try:
        if int(log_text[i + 1][36:38]) - int(log_text[i][36:38]) == 0 \
                or int(log_text[i + 1][36:38]) - int(log_text[i][36:38]) == 1:
            # 145是解码之后的位置
            flag = flag + log_text[i][145]
            # 解码后145位置有单引号？
            if log_text[i][145] == "\'":
                flag = flag + log_text[i][146]
    except Exception as e:
        print(e)
print(flag)
print(flag.replace("\'", ""))
