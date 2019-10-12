from function_ import my_abs

print(123, 'das', '213', 'sada')
# name = input("拟定 名字：")
# print("你好", name)
print("""
第一行
第二行
第三行""")
# 布尔值
print(True, 4 > 2, 4 > 5)
# and、or和not
# &、|| 和 !  与java对应
print(4 > 2 and 4 > 3)
print(4 > 2 or 4 > 5)
print(not 4 > 5)

# 除法
print(20 / 6)  # 结果是3.3333
# // 取整数
print(20 // 6)  # 结果是3

# 字符串的编码
print('a', (ord('a')))
print('中', ord('中'))
print(98, chr(98))

# byte数据
dataByte = b'12'
print(len('12'), len(dataByte))

# 占位符
print(("hi %s ,你在干什么啊,%s") % ("老高", '你管'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# list
list = ["ws", 'sad', '33']
print(list)
list.append('ffff')
print(list)
endPop = list.pop()
print(list, '---', endPop)
pop = list.pop(2)
print(list, '---', pop)
list.insert(1, "666")
print(list)

# tuple 不可变的集合
t = (1, 2, 3, 4)
print(t)
contains__ = t.__contains__(7)
print(t, contains__)
index = t.index(3)
print(index)

# 判断语句
age = 3
if age > 18:
    print("你是成人")
else:
    print('你是小孩')

# 更细致的判断
if age > 18:
    print("你是成人")
elif age > 6:
    print('你是小孩')
else:
    print("你是婴儿")

#     使用input  和 int来进行
# birth = input('你的年龄：')
birth = 11

if int(birth) > 2000:
    print("00后")
else:
    print('00前')

# 练习
weight = 75
height = 1.82

mbi = weight / height / height
print(mbi)
if mbi < 18.5:
    print('过轻')
elif mbi < 25:
    print('正常')
elif mbi < 28:
    print('过重')
elif mbi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# for x循环

names = ['a', 'b', 'c']
for name in names:
    print(name)
# 序列
print(range(5))
sum = 0
for x in range(101):
    sum += x
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello, ' + x)

# break 语句
n = 3
while n < 100:

    if n > 8:
        break
    n += 1
    print(n)
    if n % 2 == 0:
        print("偶数", n)
        continue
print('end', n)

# 字典  map
print("map 字典的learn")
d = {'lao':33, 'gao': 44, 'ni': 55}
print(d['gao'])
hao = 'hao'
d[hao] = 12
print(hao in d , d[hao], d.get('haso',-3))
print(d)
d.pop(hao)
print(d)

# 创建set
print('创建set')
s = set([1,2,3,1])
s2 = set()
s2.add(1)
s2.add(1)
s2.add(1)
print(s , s2)

# 排序
print("排序")
list3 = [1,4,6,2,5]
print(list3)
list3.sort()
print(list3)

# 调用下面的函数
print(my_abs(-3),my_abs(-33),my_abs(-3333))