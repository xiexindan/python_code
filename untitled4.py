#列表元素的删除操作
'''
lst=[10,20,30,40,50,60,30]
lst.remove(30)   #从列表中移除一个元素，如果有重复元素只移第一个元素
print(lst)
lst.remove(100)   #元素不存在弹出ValueError
'''

'''
lst=[10,20,40,50,60,30]
#pop()根据索引移除元素
lst.pop(1)
print(lst)  #[10,40,50,60,30]
lst.pop(5)   #超出了边界   ，如果指定的索引位置不存在，将抛出异常
lst.pop()
print(lst)  #如果不指定参数（索引），将删除列表中的最后一个元素
'''

'''
#切片操作。删除至少一个元素，将产生一个新的列表对象
lst=[10,40,50,60]
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)   #[40,50]

#不产生新的列表对象，而是删除原列表中的内容
lst[1:3]=[]
print(lst)    #[10,60]
'''

'''
#清除列表中的所有元素
lst=[10,60]
lst.clear()
print(lst)    #[]
'''

'''
#del语句将列表对象删除
lst=[]
del lst
print(lst)    #'lst'没有定义
'''

'''
#列表元素的修改操作
#1.为指定索引的元素赋予一个新值
lst=[10,20,30,40]
#一次修改一个值
lst[2]=100
print(lst)    #[10,20,100,40]
#2.为指定的切片赋予一个新值
lst[1:3]=[300,400,500,600]
print(lst)
'''

'''
#列表元素的排序操作
#1.调用sort()方法,默认为升序排序
lst=[20,40,10,98,54]
print('排序前的列表',lst,id(lst))
#开始排序
lst.sort()
print('排序后的列表',lst,id(lst))    #排序是在原列表的基础上执行的
#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)  #reverse=True表示降序排序，reverse=False表示升序排序
print(lst)
lst.sort(reverse=False)
print(lst)

#2.调用内置函数sorted(),将产生一个新的列表对象
lst=[20,40,10,98,54]
print('原列表',lst)
#开始排序
new_list=sorted(lst)
print(lst,id(lst))
print(new_list,id(new_list))
#指定关键字参数，实现列表元素的降序排序
desc_list=sored(lst,reverse=True)
print(desc_list)    #原列表不发生改变
'''

#列表生成式，即生成列表的公式
'''语法格式：
[i*i for i in range(1,10)]
'''

lst=[i for i in range(1,10)]  #列表中存储的是i的值
print(lst)
lst=[i*i for i in range(1,10)] 
print(lst)   #[1,4,9,16,25,36,49,68,81]
#列表中的元素的为2,4,6,8,10
lst2=[i*2 for i in range(1,11)]
print(lst2)   #[2,4,6,8,10,12,14,16,18,20]
lst2[5:10]=[]
print(lst2)
#或者
lst2=[i*2 for i in range(1,6)]
print(lst2)
