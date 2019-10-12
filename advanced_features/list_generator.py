import L

print("生成器")


def fib(max):
    sum = 0
    x = 0
    y = 1
    while sum < max:
        print(y)
        x, y = y, x + y  # 注意这里的写法 x = y , y = x+y 有顺序的
        sum += 1
    return print("over")


fib(10)

print('将上面的函数定义成 生成器函数')


def fib_g(max):
    sum = 0
    x = 0
    y = 1
    while sum < max:
        yield y
        x, y = y, x + y  # 注意这里的写法 x = y , y = x+y 有顺序的
        sum += 1
    return print("over")


print('定义成生成器后， 需要有中断的操作 否则yield会一直执行下去的')
for u in fib_g(6):
    L.e(u)

print('使用yield 的说明 ；只能调用一次next 才会执行下一次的迭代')


def odd():
    print("first")
    yield 1
    print("two")
    yield 2
    print("three")
    yield 3


#
# g = odd()
# print(next(g))
# print(next(g))
# print(next(g))

L.e("关于捕获yield的错误 , 注意生成器的返回值 是在while的外部！！！")
generator = odd()
while True:
    try:
        L.e(next(generator))
    except StopIteration as e:
        L.e('StopIteration 错误的返回值', e.value)
        break

L.eln("定义一个杨辉三角")


def triangles():
    list = [1]
    while 1:
        yield list
        list = [0] + list + [0]
        list = [list[i] + list[i + 1] for i in range(len(list) - 1)]


g = triangles()
for i in range(5):
    L.e(next(g))
