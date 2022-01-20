# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 15:26:23 2022

@author: HP
"""

for i in range(1,10):  #行数
    for j in range(1,i+1):    # 每行*的个数与行数相等
        print('*',end='\t')
    print()    


for i in range(1,10):  #行数
    for j in range(1,i+1):    # 每行*的个数与行数相等
        print(i,'*',j,'=',i*j,end='\t')
    print()    