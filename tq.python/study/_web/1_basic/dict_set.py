# dict set

# dict
print("-------dict-----------")

dict={"123": 123, "123": 123123, "234": 123, 123: 123}
print(dict)
print(dict["123"])
print(dict["234"])
print(dict[123])

print(123123 in dict)

# get
value = dict.get(12312)
print(value)

dict.pop(123)
print(dict)

print("---------- set ----------")
s = set([1,2,123,12,31,23,12,312,33,4])
print(s)

s.add("123")
print(s)

s.remove(1)
print(s)

# 交集 并集
s1 = set([123,12,31,23,1])
s2 = set(["asd", 45,45,4,56,456,12,1])

print(s1 & s2)

# 再议不可变对象
a = 'tangqing'
b = a.replace('a', "asda")
print(a)
print(b)

