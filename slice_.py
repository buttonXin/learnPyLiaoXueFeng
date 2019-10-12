from collections.abc import Iterable

print("切片的使用")
L = ['123', '234', 333, 444, 555]
print(L[3], )
print('左边包含，后边不包含', L[3:L.__len__()])
print('从最左边开始，不需要写', L[:3])
print('倒数取数字 , -1是最后一个', L[-1], L[:-1], L[-3:-1], L[-2:-2])

print('通过切片取数据')
data = list(range(100))

print('前10个', data[:10])
print('前20个,每2个取一个', data[:20:2])
print('所有的,每5个取一个', data[::5])

print('字符串也是切片，取出来还是字符串'[::2])

# 迭代
print('迭代 for  in')
map = {'a': 1, 'b': 2, 'c': 3}
for key in map:
    print('迭代map的key--->', key)

for value in map.values():
    print('迭代map的value--->', value)

for key, value in map.items():
    print('迭代map的key value--->', key, value)
for a in 'acb':
    print('迭代字符串', a)

print('判断一个对象是否可以进行迭代', isinstance('nnn', Iterable),
      isinstance([9, 9, 9], Iterable), isinstance(666, Iterable))

print('py里实现java的迭代')
for x, y in enumerate([33, 22, 11]):
    print('下标' + str(x), '数值' + str(y))


