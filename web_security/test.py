# -*- coding: utf-8 -*-
# author = 'K0ctr'


def a(flag):
    data={"a": flag}
    return data

with open("f.txt","w") as f:
    for i in range(0,100):
        f.write(str(i)+"\n")

with open("f.txt",'r') as f:
    for line in f:
        data=a(line.strip())
        print(data["a"])