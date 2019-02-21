from functools import reduce

print(abs(-10))
print(abs)

f=abs
print(f(-10))

abs = 10
# print(abs(-10))
# 变量可以指向函数

# map/reduce
def f(x):
    return x*x;

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

r = map(str, [1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(str, [1,3223])))

# reduce
def add(x, y):
    return x+y;

print(reduce(add, [1,2,23,3,3,4]))

def fn(x, y):
    return x*10+y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, "123445")))

# filter, 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd, [2,3,3,44,4,4,4])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['1', '', None, "123"])))

# 返回函数
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,23,12,31,231)
print(f)
print(f())

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# 匿名函数
# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
print(list(map(lambda x:x*x, [1,23,12,312,21])))

f = lambda x:x*x
print(f)


# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def now():
    print("123")
f=  now
f()

print(now.__name__)
print(f.__name__)

print("--------- z -------")

def log(func):
    def wrapper(*args, **kwargs):
        print("call %s(): " % func.__name__)
        func(*args, **kwargs);
        print("call %s() success: " % func.__name__)
    return wrapper

@log
def now(x):
    print(x)

now(123)


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')

now()



