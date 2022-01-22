# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 09:20:20 2022

@author: HP
"""
'''
lst=['hello','world',98,'hello','world',234]
#获取索引为2的元素
print(lst[2])
#获取索引为-3的元素
print(lst[-3])
#获取索引为10的元素
print(lst[10])   #超出范围
'''
#列表元素的查询操作
#获取列表中的多个元素,切片操作
#列表名[start:stop:step]
'''lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1
print(lst[1:6:1])    #不包括6
print('愿列表',id(lst))
lst2=lst[1:6:1]
print('切的片段:',id(lst2))
print(lst[1:6])     #默认步长为1
print(lst[1:6:])    #默认步长为1
'''

#start=1,stop=6,step=2
print(lst[1:6:2])
#stop=6,step=2,start采用默认
print(lst[:6:2])    #start默认为0,即列表的第一个元素
#start=1,step=2,stop采用默认
print(lst[1::2])   #[20,40,60,80]，即列表的最后一个元素

print('----------------------step步长为负数的情况------------------------')
print(lst[::-1])   #步长为负数，第一个元素为列表的最后一个元素，最后一个元素为列表的第一个元素
#start=7,stop省略，step=-1
print(lst[7::-1])

#start=6,stop=0,step=-2
print(lst[6:0:-2])

#判断指定元素在列表中是否存在
'''元素 in 列表名
元素 not in 列表名
'''
print('p' in 'python')    #True
lst=[10,20,'python','hello']
print(10 in lst)    #True

#列表元素的遍历
'''for 迭代变量 in 列表名：
   操作
'''
for item in lst:
    print(item)

#列表元素的增加操作
'''在列表的末尾添加一个元素：append()
在列表的末尾至少添加一个元素:extend()
在列表的任意位置添加一个元素：insert()
在列表的任意位置添加至少一个元素：切片
'''
lst=[10,20,30]
lst.append(100)
print(lst)

lst2=['hello','world']
lst.append(lst2)   #将lst2作为一个元素添加到列表的末尾
print(lst)    #[10,20,30,['hello','world']]

lst.extend(lst2)   #向列表的末尾一次性添加多个元素
print(lst)   #[10,20,30,'hello','world']

lst.insert(1,90)   
print(lst)     #[10,90,20,30,'hello',''world]

lst3=[True,False,'hello']
#在任意的位置上添加N多个元素
lst[1:]=lst3
print(lst)









