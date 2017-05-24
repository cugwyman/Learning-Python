#列表

#2.3.1 list函数
list('hello')

#2.3.2 基本列表操作
#1.元素赋值
x=[1,1,1]
x[1]=2
x

#2.删除元素
names =['wyman','bitch','zhao','juan']
del names[-2:]
names

#3.分片赋值
name = list('bitch')
name
name[3:]=list('ter')
name

#2.3.3 列表方法
#对象.方法（参数）

#append
month.append(3)
#一次加一个对象

#count统计出现次数
x=[[1,2],1,1,[2,1,[1,2]]]
x.count(1)
#2

#extend末尾加另一序列多值
a=[1,2,3]
b=[4,5,6]
a.extend(b)
a
#若a+b则不修改a

#index索引第一个匹配项位置

#remove移除第一个匹配项

#insert插入对象到列表
numbers =[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers

#pop移除最后一个元素，返回该元素值
#堆栈
x=[1,2,3]
x.append(x.pop())
x
#[1,2,3]

#reverse反向存放元素

#sort对列表排序，同时保留原列表
x=[4,6,2,1]
y=x[:]      #x[:]复制整个列表
y.sort()



