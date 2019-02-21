# 函数

# abs
print(abs(-100))


# max

print(max(1,2,33))

# 类型转换
print(int("13"))
print(bool(";"))
print(bool(1))
print(bool(set()))

# 定义函数
print("-----定义函数")
def my_abs(x):
    return x

print(my_abs(123))


# 参数
print("--------------参数")

def power(x):
    return x*x

print(power(44))


def power(x, n):
    s=1
    while n > 0:
        n=n-1
        s=s*x
    return s

print(power(222,2))

print(power(n=2, x=3))

# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L;

print(add_end())
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

print(add_end())
print(add_end())
print(add_end())


# 可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum = sum+n*n
    return sum

print(calc(1,23,12,31,2))

nums = [1,22,3,23]
print(calc(*nums))

# 关键字参数
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

person(1,2)
person(1,2, c=2)

# 命名关键字参数
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
def person(name, age, *, city, job):
    print(name, age, city, job)

person(123,123, city=2, job=3)

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数


# 递归函数
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)

print(fact(50))

# 尾递归优化
def fact_iter(n, product):
    if n==1:
        return product
    return fact_iter(n-1, n*product)
print(fact_iter(50, 1))