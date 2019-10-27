# -*- coding: utf-8 -*-
# author = 'K0ctr'


import base64
import shutil
import binascii


while True:
    with open(r'C:\ctf_match\base64.txt', 'rb') as init_file:
        with open(r'C:\ctf_match\decode.txt', 'wb') as decode_file:
            try:
                base64.decode(init_file, decode_file)
            except binascii.Error:
                break
    shutil.copyfile(r'C:\ctf_match\decode.txt', r'C:\ctf_match\base64.txt')

flag = open(r'C:\ctf_match\base64.txt', 'r', encoding='utf-8')
print(flag.read())
flag.close()
