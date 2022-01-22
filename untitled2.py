# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:08:05 2022

@author: HP
"""

'''流程控制语句break和continue在二重循环中的使用'''
'''for i in range(5):    #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            break      #结束内层循环，执行外层循环,通常与分支结构一起使用
        print(j)
 '''
       
'''for i in range(5):    #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()
'''    
    

'''变量可以存储一个元素，列表可以存储N多个元素,相当于其他元素中的数组'''
#a=10   #变量存储的是一个对象的引用
'''lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
'''

#列表的创建：使用中括号、调用内置函数list()
'''lst=['hello','world',98,'hello']
print(lst[0],lst[-4])
lst2=list(['hello','world',98])
'''

lst=['hello','world',98,'hello']
print(lst.index('hello'))      #0,如果列表中有相同元素只返回列表中相同元素的第一个元素的索引
print(lst.index('Python'))
print(lst.index('hello',1,3))   #在1-3的位置上查找hello,不包括3


