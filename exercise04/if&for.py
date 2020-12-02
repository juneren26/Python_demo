# coding=utf-8
'''
@Time   :2020/11/17 15:59
@Author :六月
@Email  :juneren26@gmail.com
@File   :if&for.py
@IDE    :PyCharm
'''

'''
顺序结构 、选择结构 、循环结构
条件判断
if语句
if 判断条件（表达式）：
    代码块

if else语句
if判断条件（表达式）：
    代码块
else：

if elif else语句
if 判断条件（表达式）：
    代码块
elif 判断条件（表达式）：
    代码块
else：

'''
# if else语句
# 成绩80以上为优秀，否则一般
score = int(input('请输入分数:'))
# if score >= 80:
#     print('优秀')
# else:
#     print('一般')

# 成绩80分以上评级优秀,60/79成绩一般,60分以下不及格
# if score >= 80:
#     print('优秀')
# elif score >=60:
#     print('一般')
# else:
#     print('不及格')

# if 的嵌套
# if 判断条件（表达式）：
#    if 判断条件（表达式）：
#       代码块
#    elif 判断条件（表达式）：
#       代码块
#    else：
# elif 判断条件（表达式）：
#    代码块
# else：
# 判断成绩的等级(优秀/中等/一般/不及格)
# if 75 > score >= 60:
#     print('一般')
#     if score > 90:
#         print('优秀')
#     elif 90 >= score >= 75:
#         print('中等')
#     else:
#         print('一般')
# else:
#     print('不及格')

# 循环语句
# while  for

# while 循环
# while 条件表达式（循环变量的判断）：
#       代码块（又被称为循环体）
# 条件为真执行循环体，条件为假跳出循环体
# n = 10
# while n > 0:
#     n = n - 1
#     print(n)
# print('结束')

# 实现1+2+3+4...+100?
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i +=1
#     print(i,sum)
# print(sum)

# while循环与else语句同时使用
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
#     print(i,sum)
# else:
#     print(sum)

# str1 = "http://www.baidu.com/"
# i = 0
# while i < len(str1):
#     print(str1[i],end='')
#     i += 1

# for 循环
# 经常用来遍历字符串、列表、元组、字典、集合等序列类型，煮个获取序列中的各个元素
# for 迭代变量 in 字符串、列表、元组、字典、集合：
#     代码块
# list1 = ['zhangsan','lisi','wangwu','zhaoliu']
# for x in list1:
#     print(x)
#
# str1="http://www.baidu.com/"
# for x1 in str1:
#     print(x1,end="")

# 计算一下1+2+3+4...+10的值
# range（x）函数提供了一个整数序列x生成从0到小于x的值
sum = 0
for i in range(11):
    sum += i
print(sum)

# 什么时候用while什么时候用for
# 一般需要遍历某个序列的时候用for
# 一般能用for的时候一定可用while，反过来就不一定了
# 当知道循环次数的时候用for，不知道循环次数的时候用while

# 循环嵌套
i = 0
while i < 10:
    for j in range(10):
        print('i=',i,'j=',j)
    i = i + 1

# 打印一个图案
# *
# **
# ***
# ****
# *****
for x in range(1,6):
    for y in range(0,x):
        print("*",end='')
    print()

# break:跳出整个循环
# continue：跳出本次循环
# pass：空语句，站位语句
# 除去h字母不打印
str = 'nihaohanhan'
for i in str:
    if i == 'h':
        pass
    else:
        print(i,end='')
