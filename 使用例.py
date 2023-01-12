from 换皮器 import src2syl,syl2syl
a1 = src2syl("人造语言群")
b1 = src2syl("魔法阵")
ab1 = src2syl("魔法阵人造语言群")
ab2 = syl2syl([a1,b1])

print(a1)
print(b1)
print(ab1)
print(ab2)

from 换皮器 import src2ms,ms2ms
a2 = src2ms("人造语言群",3)
b2 = src2ms("魔法阵",3)
ab2 = src2ms("魔法阵人造语言群",3)
ab4 = ms2ms([a2,b2],3)

print(a2)
print(b2)
print(ab2)
print(ab4)

from 换皮器 import letter_src2ms
a3 = letter_src2ms("conlang group",3)
b3 = letter_src2ms("magic circle",3)
ab3 = letter_src2ms("magic circle conlang group",3)
ab6 = ms2ms([a3,b3],3)

print(a3)
print(b3)
print(ab3)
print(ab6)

print(letter_src2ms("santa",2))
print(letter_src2ms("satan",2))