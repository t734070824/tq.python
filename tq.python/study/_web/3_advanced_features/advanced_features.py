# 高级特性
from collections import Iterable
# 切片 [x:n] [x,n)

L = list(range(0,5))
print(L)
print(L[0:3])

L = list(range(0,100))
print(L[:10])
print(L[-10:])
print(L[-10:-1])
print(L[:10:2])
print(L[:20:3])

# 字符串切片
print('ADAsdasda'[:3:2])

# 迭代
# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d={1:1, 2:2, 3:3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for ch in "ABC":
    print(ch)



print(isinstance("AS", Iterable))

for x,y in [(1,2), (123,123)]:
    print(x,y)

# 列表生成式
L = [x*x for x in range(1,11)]
print(L)

L= [x*x for x in range(1,11) if x%2==0]
print(L)

import os
L = [d for d in os.listdir("../../")]
print(L)

# 生成器
g  = (x*x for x in range(10))
for n in g:
    print(n)

# TODO https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000