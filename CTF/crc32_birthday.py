# -*- coding: utf-8 -*-
# author = 'K0ctr'


import binascii

crc = 0x3a189e9d

year, mouth, day = 0, 0, 0
for i in range(1000, 9999 + 1):
    year = str(i)
    for j in range(1, 12 + 1):
        mouth = str(j).zfill(2)
        for k in range(1, 31 + 1):
            day = str(k).zfill(2)
            flag = year + mouth + day
            if ((binascii.crc32(flag.encode())) & 0xffffffff) == crc:
                print(flag)
