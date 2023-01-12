from 经典皮肤 import c,v,e
sylDict = []
for x in c:
    for y in v:
        for z in e:
            sylDict.append(x+y+z)
DICLEN = len(sylDict)

import math
def h(a): #h函数，将外来词运算为DICLEN以内的数字
    return ord(a) % DICLEN

def x(a): #x函数，将数个h的结果运算为DICLEN以内的数字
    res = 1
    for i in a:
        res *= i
    return res % DICLEN

def w(a): #w函数，将DICLEN以内的数字转换为音节
    return sylDict[a]

def W(a): #逆w函数，将音节转换为DICLEN以内的数字
    return sylDict.index(a)

def multi_h(a): #对字符串内每个字符依次进行h操作
    return [h(i) for i in [*a]]

import math
def h_ms(a, syls): #h函数，将外来词运算为MODE以内的数字
    return ord(a) % (DICLEN**syls)

def x_ms(a, syls): #x函数，将数个h的结果运算为MODE以内的数字
    res = 1
    for i in a:
        res *= i
    return res % (DICLEN**syls)

def w_ms(a, syls): #w函数，将MODE以内的数字转换为单词
    aa = a
    res = ""
    for i in range(syls):
        res += sylDict[a%DICLEN] + '.'
        a = math.floor(a/DICLEN)
    return res[:-1]

def W_ms(a): #逆w函数，将单词转换为MODE以内的数字
    aa = a.split('.')
    aa.reverse()
    res = 0
    for i in aa:
        res += sylDict.index(i)
        res *= DICLEN
    return math.floor(res/DICLEN)

def multi_h_ms(a,syls): #对字符串内每个字符依次进行h_ms操作
    return [h_ms(i,syls) for i in [*a]]

def src2syl(a):
    return w(x(multi_h(a)))

def syl2syl(a):
    return w(x([W(i) for i in a]))

def src2ms(a, syls):
    return w_ms(x_ms(multi_h_ms(a,syls),syls),syls)

def ms2ms(a, syls):
    return w_ms(x_ms([W_ms(i) for i in a],syls),syls)

def letter_h(a):
    res = 0
    for i in a:
        res += ord(i)
        res *= 128
    return math.floor(res/128) % DICLEN

def letter_h_ms(a,syls):
    res = 0
    for i in a:
        res += ord(i)
        res *= 128
    return math.floor(res/128) % (DICLEN**syls)

def letter_multi_h(a):
    return [letter_h(i) for i in a.split()]

def letter_multi_h_ms(a,syls):
    return [letter_h_ms(i,syls) for i in a.split()]

def letter_src2syl(a):
    return w(x(letter_multi_h(a)))
    
def letter_src2ms(a, syls):
    return w_ms(x_ms(letter_multi_h_ms(a,syls),syls),syls)

i = 1
while i==1:
    q = input("请输入需要换皮的东西：")
    print(src2ms(q,3))
