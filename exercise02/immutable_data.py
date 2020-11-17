# coding=utf-8
'''
@Time   :2020/11/16 11:12
@Author :六月
@Email  :juneren26@gmail.com
@File   :immutable_data.py
@IDE    :PyCharm
'''

'''
常用的数据类型
什么是数据类型：一类数据的类型统称
特点：python是不需要申明数据类型的
python中常见的数据类型
number 、string 、tuple 不可变数据类型
list 、 dict 、 set可变数据类型
'''

# 一、number类型（数字类型、不可变类型）
# int、 float 、bool
# 运算符
# 算术运算符 + - * / //（取整） %（取余） **（幂）
# 比较运算符 == != > >= <= <
# 赋值运算符 = += -=

# 1.整数
x = 6
y = 2
z = x + y
print(z)
print(x + y, x - y, x * y, x / y, x // y, x % y, y ** x)

# 2.浮点数
x1 = 5.20
y1 = 5.30
z1 = x1 + y1
print(z1)

# //向下取整  向上取整为>= 取大于等于变量的  向下取整为<= 取小于等于变量的
# //除取整数，当分子分母都为整数，向下取整
num1 = 8
num2 = 3.0
print(num1 / num2)
print(num1 // num2)

# 3.布尔值 T 1 F 0
print(2 + 3 > 4)
print(1 == 2)

# 4.赋值运算符
a = 3
b = 12
# b = b+a
b += a
print(b)
# b=b-a
b -= a
print(b)

# 5.常用的函数
# int（）
print(int(5 / 3))
print(float(5 / 3))
# float
print(float(18))
print(float(True))
print(float(False))

# 返回绝对值
# abs（数字类型的变量）
num3 = -12
print(abs(num3))

# 向上取整 math.ceil()
import math

num4 = 2.589
print(math.ceil(num4))
# 向下取整 math.floor()
print(math.floor(num4))

# 四舍五入round（数字变量，小数位数）
print(round(num4))
print(round(num4, 2))

# 返回某区间随机整数，random
import random

print(random.randint(0, 20))
# 随机返回0-1的值
print(random.random())
print(round(random.random(), 2))

# 二、string类型（字符串类型、不可变数据类型）
# 1.定义字符串类型的时候可以通过单引号、双引号、三引号
str = '一炮一个pdd'
print(str)
# 2.可以支持切片，类似数组的概念
# 切片：从字符串序列中截取一部分相应的元素重新组成的一个串
# 格式：字符串变量名[开始：结束：步数] step默认为1
# 定义两个字符串
# 开始：开始截取的位置，利用索引进行标注，索引是从0开始

str1 = 'abcdefg'
str2 = 'abc'

# 切片
print(str1[0:4])
# !!!注意：切片气质为左闭右开，左边的索引包含，右边的索引值不包含

# 3.如果要获取字符串str1的最后一个字符
print(str1[-1])
print(str1[:-1])
print(str1[:])

# 4.隔一个字符取一个值
print(str1[::2])
# 如果step是整数就从左往右取，如果step是负数就从右往左取

# 5.实现字符串的翻转
print(str1[::-1])

# 6.如何更新字符串
str3 = 'abcdefg'
# print(str3[-1])
# str3[-1]=1
# print(str3)
# 通过拼接的方式修改
str3 = str3[:-1] + '1'
print(str3)

# 7.字符串的运算（+ *）
name1 = 'zhangsan'
name2 = 'lisi'
name3 = name1 + name2
# *表示复制几次
name4 = name1 * 2
print(name3, name4)

# in / not in
if 'a' in str3:
    print('存在')
else:
    print('不存在')

# 8.特殊字符
# 换行 \n
str4 = 'abc\ndefg'
print(str4)
str5 = r'abc\ndefg'
print(str5)
# r表示用原格式
# \\替代\ 通过r使用原格式
str6 = r"E:\桌面文件\2020.11完成\CRM客户标签优化项目"
print(str6)
# \' \'' \''' \n(换行) \t(制表符空格)
print('1\t2')

# 9.字符串的格式化
# 第一种表示方法
# 比如我要打印
print('xxx工作年限：？年')
# 这些都是可变的变量，我们可以用变量替代他
print('%s的工作年限：%d 年' % ('zhangsan ', 3))

# 第二种表示方法，format需要传入值的时候要用大括号
print('{}工作年限：{}年'.format('lisi', 4))
# fromat和%的区别
# %需要顺序传值、format不需要顺序传值，可以指定船只的位置，已索引的方式去传值
print('{1}工作年限：{0}年'.format(4, 'laowang'))

# 第三种方式
# f-string它仅支持py3.7以上的内容
name = '张若晨'
age = 1001
print(f'{name}帅小子：{age}岁')

# 10.字符串常见的其他内置函数
# 通过某个分隔符把字符串连接起来用
# ''.join,通过-把它连接起来
list1 = ['你好', 'world']
str7 = '-'.join(list1)
print(str7)

# 还原成list1的形式，用。split指定分隔符，从左边开始分隔
list2 = str7.split('-')
print(list2)
# 从右边进行分隔，.rsplit
list3 = str7.rsplit('-')
print(list3)

# 还可以指定具体还原成几个部分
list4 = ['nihao', 'shijie', 'zhangsan']
str8 = '-'.join(list4)
print(str8)
# 可以指定具体还原时分隔几次
list5 = str8.split('-', 1)
print(list5)

# 11.替换某个字符串，replace，出了拼接以外的函数
str9 = 'abcdefg'
str10 = str9.replace('abc', '123')
print(str10)

# 统计字符串的方法
# 统计字符串的长度，最大值，最小值
print(len(str10), max(str10), min(str10))

# 查找字符串find（'a',kaishi(索引值)，结束），得出的结果表示查找的字符所在的索引位置
print(str10.find('e', 0, len(str10)))
# 如果没有之后找到，匹配不到会返回-1
print(str10.find('a', 0, len(str10)))
# 还可以用index，如果匹配不到会报错
# print(str10.index('a',0,len(str10)))

# 12.判断业务的时候，返回True，或者False
str10.isalnum()  # 判断字符串含有字母和数字
str10.isdigit()  # 判断是否为整型
str10.isdecimal()  # 判断是不是浮点数
str10.isalpha()  # 判断是不是字母
str10.islower()  # 判断是不是小写
str10.isnumeric()  # 判断是不是数字
print(str10.isalnum())
print(str10.isnumeric(), str10.islower())

# 常见的字符串大小写转换函数
# 转换小写、大写、首字母大写
print(str10.lower(), str10.upper(), str10.capitalize())

# 13.逻辑运算符：and or not
# and同时为正确，就是正确
# or 其中一个正确，就是正确
# not不是这个正确，就是那个正确

c = 100
d = 200
print(d > c and d > c)
print(d > c or d < c)

# 14.位运算：通过二进制来进行运算
# 成员运算符号 ： in、not in
str1 = 'nihao zhangsan '
if 'n' in str1:
    print("cunzai")
else:
    print('bucunzai')

# 身份运算符is、is not
# is就是判断两个对象是否属于同一个对象，类似于内存地址
# is not判断他是否不属于同一对象
a1 = 10
b1 = 10
print(a1 is b1)
print(id(a1), id(b1))

# 运算符优先级，先运行高优先级在运算低优先级，类似于先做乘除再算加减

# tuple 元组
# ()通过它标识，元素是可以任意类型的，元素之间通过，隔开
# 1.创建一个元组
tup1 = (1, 'nihao', '3.5')
print(tup1)
# 2.创建一个空元组
tup2 = ()
print(tup2, type(tup2))
# 3.创建一个只有一个元素的元组，后面需要加一个，来消除数字歧义
tup3 = (1,)
print(tup3, type(tup3))
# 4.可以创建任何数据类型的元组
tup4 = (1, 2, 3, 'world', [1, 2, 3, 4])
print(tup4)
# 5.访问元素中的元素，可以通过切片的方法去访问，根据索引来确定
print(tup4[4])
# 6.去头去尾访问
print(tup4[1:-1])
# 7.访问元组当中部分元素
print(tup4[::2])
# 8.更新元素
# tup4[3] = 'nihao'  此方法不能更新，元组是不可变数据类型不能这样更新
tup6 = ('nihao',)
tup5 = tup4[0:3] + tup6 + tup4[3:]
print(tup5)
# 9.复制元素
print(tup4 * 3)
# 10.元组还可以做判断
if 'nihao' in tup5:
    print('存在')
else:
    print('不存在')
# 11.删除元组的元素
# 不可以删除元组里面的元素，只能通过拼接的方式去更新
# del tup4[1] 此方法不可以
# 但可以删除整个元组对象
# del tup4
# print(tup4)
# 12.元组常用的其他函数
# 把元祖转换成列表
print(list(tup4))
