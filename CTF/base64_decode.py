# -*- coding: utf-8 -*-
# author = 'K0ctr'


import base64


f=open(r'D:\ctf_for_match\53.txt','rb')
f2=open(r'D:\ctf_for_match\54.txt','wb')
base64.decode(f,f2)
f.close()
f2.close()