# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:43:40 2022

@author: HP
"""

#获取字典视图的三个方法
#1.keys()获取字典中所有的key
scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))  #将所有key组成的视图转成列表
#2.values()获取字典中所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values))
#3.items()获取字典中所有key,value对
items=scores.items()
print(items)
print(list(items))   #转换之后的列表元素是由元组组成的

