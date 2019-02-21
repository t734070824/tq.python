#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 字符串
print("i'm \"ok\" ")

# '''...'''
print('''123
... 123
... 123''')

### 字符串和编码
print("站我跟 的dss")


print(ord('A'))

print(ord('中'))

print(ord('A'))

print(chr(66))

print(chr(25991))


### bytes
x = b'c'
print(x)

x = len("abs")
print(x)

x=len("唐庆")
print(x)

x=len(b'\xe4')
print(x)

x=len('唐庆'.encode("utf-8"))
print(x)

## 格式化
s='hello, %s'
print(s % 'world')
s="Hi, %s, you have $%d."
print(s % ("tangqing", 100))

### 占位符
### %d	整数
### %f	浮点数
### %s	字符串
### %x	十六进制整数

### format()

print("hi ,{0}, nb {1:.1f}".format("tqngaing",12.514))