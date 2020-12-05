# coding=utf-8
'''
@Time   :2020/12/3 10:12
@Author :六月
@Email  :juneren26@gmail.com
@File   :osmoudle.py
@IDE    :PyCharm
'''

# 文件及os模块
# 打开文件open（）
# file=open（file name路径，访问模式）
# r：以只读的方式打开
# rb：以二进制格式打开一个文件用于只读
# w：打开一个文件只用于写入
# a：追加
# 在当前路径下创建一个文本文件
# 注意：对文件操作完后，记得关闭文件，否则会占用服务器内存
# file1 = open('1.txt', 'w+')
# 往文件中写入内容
# file1.write(
# '''zhangsanha
# lisi
# wangmazi''')
# file1.close()

# read（）：每次读取整个文件
# readline（）:每次读取一行内容
# readlines（）：一次性读取文件所有行，自动将文件内容分析称一个行的列表，for in结构进行处理

# file2=open('1.txt','r+')
# 用read的方式读取文件内容
# print(file2.read())
# file2.close()
# 读取一行内容
# print(file2.readline())
# 循环读取所有含内容
# for x in file2.readlines():
#     print(x)
# 读取指定某一行的数据，返回一个列表中
# print(file2.readlines()[0])

# 如何获取指针当前的位置tell
# file3=open('1.txt','r+')
# file3.readline()
# print(file3.tell())
# file3.close()

# 想要往文件中增加一行内容
# a+：做追加，指针放在文件末尾曲追加
# w+：先找到文件，然后把指针放在开头，把源文件清空，最后才去加入内容
# file4 = open('1.txt','w+')
# file4.write('zhaolusi\ntansongyun')
# file4.close()
# file4 = open('1.txt','r+')
# print(file4.readlines())

# seek（偏移数，参数）
# 参数：0文件开头进行读取
# 1表示从当前位置进行读取
# 2表示从文件末尾开始读取
# file5=open('1.txt','r+')
# seek(x,y)从文件的y位置开始，读取x个字符
# 从文件的开头开始读取偏移2个字符
# file5.seek(2,0)
# print(file5.read(2))

# 读取6个字符
# file5.seek(0,0)
# print(file5.read(6))
# file5.close()

# with...as可以自动关闭文件的，不需要另外调用close去关闭文件
# with open(路径，模式)as 变量：
#   代码块
with open('1.txt','r') as file1:
#    # 对文件进行其他操作
    print(file1.read())

# os模块：提供了很多方法来处理文件及目录
import os
# file6=r'C:\Users\Administrator\Desktop\scot'
# 创建一个目录
# os.mkdir(file6)
# 删除目录
# 删除空目录
# os.rmdir(file6)

# 删除非空目录
# import shutil
# shutil.rmtree(file6)

# 如何重命名目录
# os.rename(源文件名，新文件名)
# os.rename(r'C:\Users\Administrator\Desktop\scot',r'C:\Users\Administrator\Desktop\scot1')

# 如何获取当前文件项目的路径os.getcwd
print(os.getcwd())

# 获取上级（父级）路径
# path1 = os.getcwd()
# print(path1)
# parent1 = os.path.join(path1,os.pardir)
# os.pardir获取当前目录的父目录（上一级目录）
# os.path.join链接两个或者更多路径的一个组件
# print('父级：',parent1)
# print('父级路径：',os.path.abspath(parent1))
# a1 = os.path.abspath(__file__) # 获取当前工作脚本的完成路径
# print(a1)

# 获取文件权限os.access(path,mode)
# Mode:os.F_OK(是否存在)、os.R_OK(可读)、os.W_OK(可写)、os.X_OK(可执行)
# os.access(路径，模式)它的作用是检验文件或目录的权限
# 比如我要访问一个路径下是否存在1.txt这个文件
file7=r'C:\Users\Administrator\Desktop\scot'
print(os.access(file7,os.F_OK))
print('判断文件是否可写',os.access(file7,os.W_OK))

# 判断路径是否为文件或者是目录
# 判断是否为文件
print(os.path.isfile(file7))
# 判断是否为文件夹
print(os.path.isdir(file7))

# 目录和文件拼接成路径
print('拼成：',os.path.join(r'C:\Users\Administrator\Desktop\scot','1.txt'))

# 可以把路径分割成目录和文件，存放在元组里
print(os.path.split(file7))

# 如何更改文件的权限os.chmod(path,mode),mode可读r/可写w/可执行x
# 所有者USR
# 其他用户OTH
# 用户所在组的权限GRP
# 想要修改某个文件的权限
import stat
file8 = r'C:\Users\Administrator\Desktop\scot'
# windows下取消只读
os.chmod(file8,stat.S_IWRITE)

