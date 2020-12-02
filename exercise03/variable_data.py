# coding=utf-8
'''
@Time   :2020/11/17 10:13
@Author :六月
@Email  :juneren26@gmail.com
@File   :variable_data.py
@IDE    :PyCharm
'''

# 可变数据类型 list、dict、set
# 列表
# 什么是列表：是一种有序集合，他可以随时添加和删除其中的元素
# 定义：通过[]表示，元素可以是任意类型，元素之间用逗号隔开
# 1.创建一个列表
list1 = [1, 2, 3, 4, 5]
print(list1)
# 2.访问列表中元素的值，也是通过索引方式来访问
# 2.1访问第一个元素的值
print(list1[0])
# 2.2访问最后一个元素的值
print(list1[-1])
# 2.3访问部分值
list2 = list1[1:-1]
print(list2)
# 2.4访问超出范围的值，索引越界
# print(list1[9])

# 3.修改列表中的元素值
list1[0] = 0
print(list1)

# 4.增加元素 ，向list1中增加一个元素
# 4.1.append方式增加，在末尾追加元素
list1.append(6)
print(list1)
# 4.2.insert在指定位置增加元素
list1.insert(1, 'lisi')  # 位置通过索引值指定
print(list1)
# 4.3增加多个元素，.extend()方法
zengjiayuansu = [11, 12, 13, 14]
# list1.extend(zengjiayuansu)
print(list1)
# 4.4通过append方式增加多个元素
# append增加后是一个列表，一个列表就是一个元素
# print(list1.append(zengjiayuansu))

# 5.删除元素
list4 = [20, 21, 22, 23, 24, 25]
# 5.1.pop的方式去删除，默认删除最后一个元素
list4.pop()
print(list4)
# 5.2指定删除，可以根据元素的索引值指定删除
list4.pop(1)
print(list4)
# 5.3根据元素的值去删除
list4.remove(24)
print(list4)
# 5.4del方式删除
del list4[-1]
print(list4)
# 5.5列表中有重复元素，删除其中一个
list5 = [6, 6, 7, 8, 9, 1, 2, 3]
# 首先可以找到某个值在列表中出现的次数
print(list5.count(6))
# print(list5.index(6, 0, len(list5)))

# 6.list可以支持运算 + * in/not in
list6 = [1, 2, 3, 4, 5]
list7 = [6, 7, 9, 8]
# 6.1 +运算
list8 = list6 + list7
print(list8)
# 6.2 *运算
print(list7 * 2)
# 6.3 判断
if 1 in list6:
    print('存在')
else:
    print('不存在')

# 7.其他操作
# .sort列表默认升序排序
list7.sort()
print(list7)
# 降序排列
list7.sort(reverse=True)
print(list7)
# list翻转
list7.reverse()
print(list7)

# 字典 dict
# d = {key1:value1,key2:value2,key3:value3......}
# key是键，value是值，key1：value1是键值对，键与值用：隔开，键值对之间用，隔开
# key必须是唯一的，并且数据不可变
# 1.创建一个字典
dict1 = {'xingming': 'zhangsan', 'mima': '123456'}
print(dict1)
# 2.创建一个空字典
dict2 = {}
print(dict2)
# 3.访问字典里面的与元素，通过键去访问
print(dict1['xingming'], dict1['mima'])
# 4.修改字典
dict1['mima'] = 'abcdefg'
print(dict1)
# 5.增加一个键值对
dict1['dizhi'] = 'changshan'
dict1['xingbie'] = 'nan'
print(dict1)
# 6.删除键值对
del dict1['dizhi']
print(dict1)
# 6.1通过函数删除
dict1.pop('xingming')
print(dict1)
# 6.2删除最后一个键值对
dict1.popitem()
print(dict1)
# 6.3删除整个字典
# del dict2
# print(dict2)

# 7.字典常见的内置函数
# 返回某个数据类型的长度
print(len(dict1))

# 8.类型转换
# 想把字典转换成字符串类型
zhuanhuan = str(dict1)
print(zhuanhuan, type(zhuanhuan))

# 9.依次获取字典中的key和value的值
dict3 = {'xingming': 'zhangsna', 'mima': '123456'}
for x, y in dict3.items():
    print(x, y)
# 10.把一下内容作为字典里面的键
list9 = ['xingming', 'mima', 'dizhi', 'xingbie']
dict4 = {}
dict4 = dict4.fromkeys(list9, 'none')
print(dict4)

# 11.字典成员的判断，通过键去判断
if 'xingming' in dict3:
    print('存在')
else:
    print('不存在')

# 12.字典多个元素更新
dict5 = {'xingming': 'zhangsan', 'mima': '123456'}
dict6 = {'xingming': 'lisi', 'dizhi': 'hubei', 'xingbie': 'nan'}
# 把dict6更新到dict4中，会按照不同的key去更新
dict5.update(dict6)
print(dict5)

# 集合数据类型，集合中的数据是无序的
# 集合也是通过{}来表示，集合中的元素可以使任意各种形态
# 元素可以使任意类型，每个元素之间可以用逗号隔开
# 1.创建一个集合，集合会自动去重
set1 = {1, 2, 3, 4, 5, 2, 3, 5, 'nihao'}
print(set1, type(set1))
# 2.创建一个空集合
set2 = {}
print(set2, type(set2))
# 上面创建的非集合而是字典，创建集合如下
set21 = set()
print(set21, type(set21))
# 3.创建集合的另一种方式
set3 = set([1, 2, 3, 4, 3, 2, 5])
print(set3, type(set3))
# 4.访问集合
# print(set1[0])
# 集合是无序的，所以不能访问

# 5.集合支持哪些运算，集合只能求合集并集交集
# a&b交集：共同的部分
# a|b并集：全部元素合并去重
# a-b差集：返回a中所有的元素，除去b中有的元素
# a^b非交集：返回的是a,b中没有重复的元素（返回的是ab中不同的部分）
set4 = {1, 2, 3, 4, 5, 6, 7, }
set5 = {5, 6, 7, 8, 9, 'nihao'}
a = set4 & set5
b = set4 | set5
c = set4 - set5
d = set4 ^ set5
print(a, b, c, d)

# 6.set常见的内置函数
# 集合运算函数

# 此方法类似上面讲的交集
print(set4.intersection(set5))

# 相当于上面的并集
print(set4.union(set5))

# 相当于上面的差集
print(set4.difference(set5))

# 相当于上面的非交集
print(set4.symmetric_difference(set5))

# 7.元素操作的相关函数
# 7.1增加元素，
set4.add(20)
print(set4)

# 7.2删除元素.pop随机删除元素，没有办法指定删除某个位置元素
set4.pop()
print(set4)

# 7.3remove/discard 也是删除，区别是discard删除没有的元素不会报错
set4.remove(20)
print(set4)
set4.discard(100)
print(set4)

# 8.常用的判断函数
# 判断返回有没有重复元素集合，没有重复返回True，有重复返回False
print(set4.isdisjoint(set5))

# 判断某个集合是不是另一集合的子集，是则返回True，不是返回False
set6 = {1, 2, 3, 4, 5, 6}
set7 = {1, 2, 3, 'nihao'}
print(set6.issubset(set7))

# 判断某个集合是不是另一集合的父集，是则返回True，不是返回False
print(set6.issuperset(set7))

# 9.更新
set6.update(set7)
print(set6)


def match(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a