# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    def __init__(self, name):
        self.name = name


s = Student("TQ")
s.score = "TQ"
print(s.name)
print(s.score)
print(type(s.score))

class Me(object):
    name="me"

m = Me()
print(m.name)

class He(object):
    pass

h = He()
h.name="qwe";
print(h.name)

# 尝试给实例绑定一个方法：
def set_age (self, age):
    self.age = age

from types import MethodType
h = He()
h.set_age = MethodType(set_age, h)
print(h)
print(h.set_age)
h.set_age(525)
print(h.age)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
He.set_score = set_score

h = He()
h.set_score(26)
print(h.score)

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# __slots__
class H3(object):
    __slots__ = ("name", "age")

h = H3()
h.name="123"
h.age=25
print(h.name)
print(h.age)

# h.score=22
# 'H3' object has no attribute 'score'

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class H4(H3):
    pass

h = H4()
h.score=254
print(h.score)

# @property
# 如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# 规范变量
class Studeng2(object):
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Studeng2()
s.set_score(22)
print(s.get_score())

# 还是装饰器
class Studeng3(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Studeng3()
s.score=60
print(s.score)

# 多重继承
class Animal(object):
    pass

# 犬类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 行为
class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("flying...")



class Dogg(Mammal, Runnable):
    pass

print(isinstance(Dogg(), Runnable))

# 定制类, 特殊函数
class Student5(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'ssda name: %s' % self.name

print(Student5("sadasda"))

s = Student5(123)

# __iter__
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素
class Fib(object):
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a

f = Fib()
print(f[100])

# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b=1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b=b,a+b
            return L

f = Fib()

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
# 避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def users(self, value):
        return Chain('%s/%s' % (self._path, value))

    __repr__ = __str__


s = Chain().status.user.timeline.list
print(s)


print(Chain().users('michael').repos)

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("my name is %s " % self.name)

s = Student("asdasd")
s()

# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：

# enum
# value属性则是自动赋给成员的int常量，默认从1开始计数。
from enum import Enum
Month = Enum("num", ("123","34"))
for name,member in Month.__members__.items():
    print(name, '--', member, '--', member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun =0
    Mon=1

print(Weekday)


# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 动态创建一个 类
def fn(self, name="world"):
    print("T %s" % name)

T = type("T", (object, ), dict(s=fn))
t = T()
print(t)
t.s(123)

# type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 运行期创建类

# metaclass
# 要控制类的创建行为，还可以使用metaclass。
# 先定义metaclass，就可以创建类，最后创建实例。
class ListMetaclass(type):
    def __new__(cls, name ,base, attrs):
        attrs["add"] = lambda self, value:self.append(value)
        attrs["print123"] = lambda self, value:print("123: ", value)
        return type.__new__(cls, name, base, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

# __new__()方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的名字；
#
# 类继承的父类集合；
#
# 类的方法集合。

L = MyList()
L.add(123)
print(L)
L.print123("aaa")

# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# ORM就是一个典型的例子。


