import math

print("函数")

print(abs(20), abs(-20))
print(max(1, 2), max(2, 5), max(5, 9, 2))

# 数据转换
print(bool('jj'))

print(hex(255), hex(1000))


# 定义函数
def my_abs(x):
    if x > 0:
        return x
    return -x


print(my_abs(3), my_abs(-3), my_abs(-33))


# pass
def testPass(x):
    pass


print('ccc', testPass('das'))


# 数据类型的检测
def my_abs_instance(x):
    if not isinstance(x, (str, float, int)):
        raise TypeError('这是错误的')
    return x


print(my_abs_instance(1), my_abs_instance("xzc"))


# 求一元二次方程

# a = int(input('a='))
# b = int(input('b='))
# c = int(input('c='))


def quadratic(a, b, c):
    x = -b + abs(math.sqrt(b ** 2 - 4 * a * c)) / (2 / a)
    y = -b - abs(math.sqrt(b * b - 4 * a * c)) / (2 / a)
    return x, y


# print(quadratic(a, b, c))
print(quadratic(2, 2, -4))


# 定义函数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


print('是乘法', power(3, 3), power(4), power(4, 3))

# 可变函数
print('可变函数')


def enroll(name, gender, age=5, city='beijing'):
    if not isinstance(age, int):
        raise Exception('类型错误，age is int 类型')
    print('name = ' + name
          + ',gender = ' + gender
          + ',age = ' + str(age)
          + ',city = ' + city)


enroll("laog", "asd")

enroll('laogao', 'zhengzhou', 25, '焦作')
enroll('laogao', 'zhengzhou', city='焦作')
# enroll('laogao', 'zhengzhou', '焦作')

# 数组的函数
print("数组的函数")


def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end())
print(add_end())
print(add_end())

# 可变函数
print('可变函数')


def calc(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


print('第一次', calc([1, 2, 3]), calc([3, 4, 5, 6]))


def calc2(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


print('第2次', calc2(1, 2, 3), calc2(3, 4, 5, 6))

list = [1, 2, 3, 4, 5]

print("第3次 将集合变成可变的参数，吧里面的内容一个个传进去", calc2(*list))

# 可变参数
print('可变参数')


def preson(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


preson('laogao', 22)
preson('laogao', 22, know='idont know')
myMap = {'wenan': 32, 'job': 'sadasd'}
preson('ces', 4, **myMap)
# 命名可变参数
print('命名可变参数')


def preson2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('当前的限制不管用', name, age, kw)


preson2('dd', 33, city='ff', ok='33')


def preson3(name, age, *, city, job):
    print('当前的限制管用', name, age, city, job)


preson3('as', 22, city=4, job=4)

args = (1, 2)
kw = {'city': 1, 'job': 2}
print("---任意函数都可以用*args, **kw 的形式进行调用！！！当前参数的数量要对应 ---")
preson(*args, **kw)
preson2(*args, **kw)
preson3(*args, **kw)


# 递归函数
print('递归函数')
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print('递归函数-->',fact(1),fact(5))












