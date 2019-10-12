from collections.abc import Iterator
from collections.abc import Iterable

import L

L.e('迭代器')

L.e(
    'Iterable 对象',
    isinstance([],Iterable),
    isinstance({},Iterable),
    isinstance('abc',Iterable),
    isinstance(110,Iterable),
    isinstance((x  for x in range(10)),Iterable),

)
L.e()
L.e(
    '迭代器：Iterator',
    isinstance([], Iterator),
    isinstance({}, Iterator),
    isinstance('abc', Iterator),
    isinstance(110, Iterator),
    isinstance((x for x in range(10)), Iterator),
)
L.e(
    'Iterable变成Iterator：',
    isinstance(iter([]), Iterator),
    isinstance(iter({}), Iterator),
    isinstance(iter('abc'), Iterator),
    isinstance((x for x in range(10)), Iterator),
)

# test 将数据变成迭代器， 进行next的调用
it = iter([1,2,3,4])
while True:
    try:
        i = next(it)
        L.e(i)
    except StopIteration:
        L.e("数据越界了")
        break






