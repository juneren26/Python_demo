# coding=utf-8
'''
@Time   :2020/12/2 11:51
@Author :六月
@Email  :juneren26@gmail.com
@File   :function_&moudle_.py
@IDE    :PyCharm
'''

n = 0
for c in 'http://www.baidu.com/':
    n = n + 1
print(n)

# 函数
# 函数是组织好的，可以重复使用的，用来实现单一或相关功能的代码段
# 自己创造的函数，叫自定义函数
# 函数的定义
# def 函数名（参数列表）：
#   实现特定功能的多行代码
#   return 返回值
# 定义一个函数：用来比较两个数字的大小的函数，将数值大的数字返回
# def compare(a, b):
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     else:
#         return a


# 调用函数：
# 返回值=函数名（值或者参数变量）
# result = compare(11, 15)
# print(result)

# 定义一个空函数，没有实际意义的
# def emptyfunction（）：
#      pass

# 参数的传递
# 形式参数：在定义函数时，函数名后面括号的参数就是形式参数
# 实际参数：在调用函数式，函数名后面括号中的参数称为实际参事

# 值传递，引用传递
# 值传递适用于不可变类型字符串、数字、元组
# 通过函数体后不能修改函数外变量的值

# 引用传递适用可变数据类型列表、字典
# 通过函数体可以改变函数外参数的值

list1 = [1, 2, 3, 4]


def changelist(listn):
    list1.append(listn)


changelist([5, 6, 7])
print(list1)

# 参数类型
# 必须参数，关键字参数，默认参数，不定长参数
# （1）必须参数
def function1(parm1,parm2):
    print(parm1,parm2)
# 调用它
# function1('1')
function1(1,2)
# 必须参数：必须以正确的顺序传入参数，调用时参数数量必须和申明的一样

# （关键字参数）
# 是一个特殊的必须参数，他可以通过关键字传值
# function1(parm1=1,parm2=2)

# （3）默认参数：在定义的过程中设置了默认值
# 定义
def function2(param1,param2 = 'default'):
    print(param1,param2)
# 调用
function2('nihao')
# 如果有默认值，传入新值，新值会覆盖调默认值
function2('nihao','shijie')
# 也可以用关键字去传入参数
function2(param1='haha')

# （4）不定长参数
# 在定义的过程中，不确定会有多少个参数，就设置成不定长参数
# 可以在参数前加一个*，或者**表示不定长参数
# 1.参数前面带一个*，把不确定长度的参数存储在元组里，可以通过元组调用其中某一项参数
# 定义不定长参数
def function3(name,*param3):
    print(name)
    print(param3)

# 调用不定长参数
function3('zhangsan','25','changsha')
# 2.参数前面带两个*，把不确定长度的参数存储在字典里面
def function3(name,**param4):
    print(name)
    print(param4)
function3('zhangsan',age='28',dizhi='changsha')

# *可以单独出现，在调用的时候必须通过关键字传值
def function4(num1,num2,*,num4):
    return num1 + num2 + num4
print(function4(1,2,num4=3))

# 注意不定长参数可以单独存在
def function5(*args):
    print(args)
# function5()

# *和**的不定长参数也可以同时被定义
def function6(*param5,**param6):
    print(param5)
    print(param6)
function6(1,2,3,name='hahah',age='18')

# 函数的嵌套
# 函数与函数之间可以进行相互调用
# 调用嵌套：在定义的过程中调用另一个函数
def function7():
    print('nihao function7')
def function8():
    print('nihao function8')
    function7()
function8()

# 定义嵌套：在函数里面定义函数
def function9():
    print('nihao  function9')
    def function10():
        print('nihao function10')
    function10()
function9()

# 函数的递归
# 自己调用自己
# def function11():
#     print('nihao function11')
#     function11()
# function11()
# 调用出现死循环

# def function12():
#     print('nihao function12')
#     function13()
# def function13():
#     print('nihao function13')
#     function12()
#
# function13()

# 匿名函数lambda表达式
# 语法：lambda 参数1，参数2，。。。：表达式
# 注意一下，接的是表达式，而不是代码块，必须要关键字lambda

# 比如通过函数求和
# 通过普通函数求和
def sum(a,b):
    return a+b
print(sum(1,3))
# 通过匿名函数求和
sum1 = lambda a,b:a+b
print(sum1(1,2))

# 匿名函数和函数的区别
# 匿名函数不可以使用其他变量，只能对内部参数做运算，函数里可以使用函数外的参数

# 模块
# 为什么要使用模块？
# 随着项目功能和需求的增多，代码量也会加大，把全部代码放在一个文件会显得冗余，因此需要使用模块分区管理

# python模块：是一个python文件，以.py结尾
# 导入模块
# 一般导入的内容放在文件的最开始
# import
import time
time.time()

# from...import从某个模块导入一个指定的部分
from time import sleep

# 跨目录调用模块
from time import sleep

# 全部导入
from exercise03.variable_data import *

# import 搜索路径
# 当你导入一个模块python解释器对模块位置有一个搜索顺序
# 1.当前目录
# 2.如果不在当前目录，python会搜索总的下的每个目录
# 3.如果都找不到，python会查看安装默认路径