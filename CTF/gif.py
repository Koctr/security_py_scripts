# -*- coding: utf-8 -*-
# author = 'K0ctr'


# gif 二进制转字符串
import re

a = '01100110011011000110000101100111011110110100011001110101010011100101111101100111011010010100011001111101'
b = re.findall(r'.{8}', a)

flag = ''
for i in b:
    flag += chr(int(i, 2))

print(flag)
