# -*- coding: utf-8 -*-
# author = 'K0ctr'


import hashlib


for i in range(100000000, 1, -1):
    m = hashlib.new('md5', bytes(str(i), encoding='utf-8')).hexdigest()
    if m.lower().startswith('aaaaaa'):
        print(i, m) # 37161640, 97341349
        break
