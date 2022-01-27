# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:15:25 2022

@author: HP
"""

'''
#字典元素的遍历
scores={'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item,scores[item],scores.get(item))
'''

'''
#字典的特点
#1.字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
d={'name':'张三','name':'李四'}
print(d)
d={'name':'张三','nikename':'张三'}
print(d)
#2.字典中的元素是无序的
lst=[10,20,30]
lst.insert(1,100)
print(lst)
#字典没法插入
#3.字典中的key必须是不可变对象
#不可变对象为整数或者字符串，列表为可变对象
d={lst:100}
print(d)    #错误
#4.字典也可以根据需要动态地伸缩
#5.字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''

'''
#字典生成式
#内置函数zip()
items=['Fruits','Books','Others']
prices=[96,78,85]
d={item.upper():price for item,price in zip(items,prices)}
print(d)
items=['Fruits','Books','Others']
prices=[96,78,85,100,120]
d={item.upper():price for item,price in zip(items,prices)}
print(d)
'''

'''
#什么是元组
#不可变序列和可变序列
#可变序列：列表，字典
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))   #内存地址不发生修改
#不可变序列：字符串，元组
s='hello'
print(id(s))
s=s+'world'
print(id(s))   #内存地址发生更改
print(s)
'''

'''
#元组的创建方式
#1.直接小括号
t=('Python','world',98)
print(t)
print(type(t))

t2='Python','world',98
print(t2)
print(type(t2))   #只有第一种创建方式可以省略小括号

t3=('python')  #代表元组中只有一个元素
print(t3)
print(type(t3))    #python  <class 'str'>

#2.使用内置函数tuple()
t1=tuple(('Python','world',98))
print(t1)
print(type(t1))
#3.只包含一个元组的元素需要使用逗号和小括号
t3=('python',)  #如果元组中只有一个元素，逗号不能省略
print(t3)
print(type(t3)) 
'''

#空元组的创建方式
#空列表的创建方式
lst=[]
lst1=list()

d={}
d2=dict()

#空元组
t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)
