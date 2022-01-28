# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:19:48 2022

@author: HP
"""
'''
t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
#尝试将t[1]修改成100
print(id(100))
t[1]=100    #元组是不允许修改元素的
#由于[20,30]组成的是列表，而列表是可变序列，所以可以向
#列表中添加元素，而列表的内存地址不变
t[1].append(100) #向列表中添加元素
print(t,id(t[1]))
'''

'''
#元组的遍历
t=('Python','world',98)
#第一种获取元组元素的方式是，使用索引
print(t[0])
print(t[1])
print(t[2])
print(t[3])     #报错，索引超出范围
#2.遍历元组
for item in t:
    print(item)
'''

#什么是集合
#集合是没有value的字典
#集合的创建方式
#1.直接{}
s={2,3,4,5,5,6,7,7}  #集合中的元素不能重复
print(s)   
#2.使用内置函数set()
s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,3,4,5,6])
print(s2,type(s2))
s3=set((1,2,4,4,5,65))   #集合中的元素是无序的
print(s3,type(s3))
s4=set('Python')
print(s4,type(s4))
s5=set({12,4,5,66,55,88})
print(s5,type(s5))

#定义空集合
s6={}   #字典类型
print(type(s6))
s7=set()
print(type(s7))