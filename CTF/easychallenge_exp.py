# -*- coding: utf-8 -*-
# author = 'K0ctr'


import base64
import re

q = "UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==="


def decode1(ans):
    s = ""
    for i in ans:
        i = (ord(i) - 25) ^ 36
        s += chr(i)
    return s


def decode2(ans):
    # 与py2对照写法的不同
    ans_list = re.findall(r'.{2}', ans)
    s = ""
    for i in ans_list:
        i = (int(i, 16) ^ 36) - 36
        s += chr(i)
    return s


def decode3(ans):
    return base64.b32decode(bytes(ans, 'utf-8')).hex()


print(decode1(decode2(decode3(q))))
print(decode1(decode2('a')))