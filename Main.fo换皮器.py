from 经典皮肤 import c,v,e
sylDict = []
for x in c:
    for y in v:
        for z in e:
            sylDict.append(x+y+z)
DICLEN = len(sylDict)

import math
def innerhash(w, depth):
    m = DICLEN #模值，重要
    a = 13 #(aX+c)mod m，乘数
    c = 44 #(aX+c)mod m，加数
    if depth==1:
        return (a*w+c)%m
    else:
        return (a*innerhash(w,depth-1)+c)%m

def wordvalue(w):
    wa = [*w]
    res = 1
    for x in wa:
        res *= ord(x)
    return res

def hashsyl(w, depth=5):
    return sylDict[innerhash(w,depth)]
    
def hashword(w, depth=5, syls=2):
    res = ""
    ww = wordvalue(w)
    for i in range(syls):
        res += hashsyl(ww%DICLEN, depth)
        ww = math.floor(ww/DICLEN)
    return res

i = 1
while i==1:
    q = input("请输入需要换皮的东西：")
    print(hashword(q,5,3))
