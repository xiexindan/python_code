# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:02:27 2022

@author: HP
"""

'''
#字典：花括号
#以键（冒号前)值(冒号后)对的方式存储数据
#无序的序列
#字典的创建
#1.使用花括号
scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))
#2.使用内置函数dict()
student=dict(name='jick',age=20)
print(student)
#空字典
d={}
print(d)
'''

'''
#字典中元素的获取
#1.[]
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])    #100
print(scores['陈六'])     #KeyError: '陈六'
#2.get()方法
scores={'张三':100,'李四':98,'王五':45}
print(scores.get('张三'))     #100
print(scores.get('陈六'))    #None
print(scores.get('麻七',99))   #99是在查找'麻七'所对应的value不存在时,提供的一个默认值
'''

'''
#字典的常用操作
#key的判断：in,not in
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)    #True
print('张三' not in scores)    #False
#字典元素的删除
del scores['张三']    #删除指定的键-值对
scores.clear()    #{}  清空字典的元素
print(scores)
#字典元素的新增
scores={'张三':100,'李四':98,'王五':45}
scores['陈六']=98   #新增元素
print(scores)
scores['陈六']=100   #修改元素
print(scores)
'''
