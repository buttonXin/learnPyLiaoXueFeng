import os

print('列表生成式')

print(list(range(1, 11)))
range_ = [x * x for x in range(1, 11)]
print("额外的操作,在for前面添加 操作", range_ )

range_ = [x * x for x in range(1, 11) if x %2 ==0]
print("额外的操作，也可以在后面进行判断的操作",range_)
range_ = [m+n for m in 'abc' for n in 'xyz']
print('多层循环',range_)

range_ = [d for d in os.listdir('..')]
print('输出os的列表',range_)

map = {'a':1,'b':2,'c':3}
range_ = [k+"="+str(v) for k ,v in map.items() ]
print('可以将map的输出进行强化,生成一个list',range_)
map = {'a':1,'b':2,'c':3}
range_ = [k.upper()+"="+str(v) for k ,v in map.items() ]
print('可以将map的输出进行强化,生成一个list,并将key更改成大写',range_)

print('练习')
L = ['Hello', 'World', 18, 'Apple', None]
range_ = [ s.lower() for s in L if isinstance(s,str)]
print('输出的时候，必须是str的结构,否则会报错',range_)







