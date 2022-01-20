# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 09:38:48 2022

@author: HP
"""

#print()函数的使用
#print函数可以输出的内容：数字、字符串、含有运算符的表达式
#print函数可以将内容输出的目的地：显示器、文件
#print()函数的输出形式：换行、不换行

#print(520)
#print('helloworld')
#print("helloworld")
#print(3+1)

#将数据输出到文件中 注意点，1.所指定的盘要存在，2.使用file=fp
#fp=open('G:/text.txt','a+')#以读写的方式打开文件,（a+的含义：如果文件不存在就创建文件，存在就在文件内容的后面继续追加）
#print('helloworld',file=fp)#输出到什么地方
#fp.close

#不进行换行输出（输出内容在一行当中）
#print('hello','world','python')#逗号分隔

#转义字符：反斜杠+想要实现的转义功能首字母
#print('hello\nworld')#换行
#print('hello\tworld')
#print('helloooo\tworld')#\t：四个字符
#print('hello\rworld')#回车（world将hello进行了覆盖）
#print('hello\bworld')#退一个格（将o退没了）

#print('http:\\www.baidu.com')
#print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，在字符串之前加r或R
#print(r'hello\nworld')
#注意事项：最后一个字符不能是反斜线
#print(r'hello\nworld\')


#name='玛丽塔'
#print(name)
#print('标识',id(name))
#print('类型',type(name))
#print('值',name)

#name='玛丽塔'
#name='规划局'#多次赋值后，变量名会指向新的空间

#整数类型
#可以表示正数、负数、0
#n1=90
#n2=-97
#n3=0
#二进制以0b开头，八进制以0o开头，十六进制以0x开头

#浮点数
#n1=1.1
#n2=2.2
#print(n1+n2)
#from decimal import Decimal
#print(Decimal('1.1')+Decimal('2.2'))

#布尔类型：用来表示真或假的值
#True:1,False:0
#f1=True
#F2=False
#print(f1,type(f1))
#print(f2,type(f2))
#布尔值可以转为整数计算
#print(f1+1) #2
#print(f2+1) #1

#字符串类型
#单引号、双引号、三引号
#str1='人生苦短 ，我用python'
#str2='人生苦短 ，我用python'
#str3='''人生苦短 ，
#我用python'''
#print(str1,typr(str1))
#print(str2,typr(str2))
#print(str3,typr(str3))

#类型转换
#name='张三'
#age=20
#print(type(name),type(age)) #name与age的数据类型不同
#print('我叫'+name+'今年,'+age+'岁') # '+'为连接符，当将str类型与int类型连接时，报错，解决方案为类型转换
#print('我叫'+name+'今年,'+str(age)+'岁') #将int类型通过str()函数转成了str类型
#print(----------int()将其他的类型转int类型---------------)
#s1='128'
#f1=98.7
#s2='76.77'
#ff=True
#s3='hello'
#print(type(s1),type(f1),type(s2),type(ff),type(s3))
#print(int(s1),type(int(s1))) #将str转成int类型，字符串为数字串
#print(int(f1),type(int(f1))) #将float转成int类型，截取整数部分，舍掉小数部分 
#print(int(s2),type(int(s2))) #将str转成int类型，报错，因为字符串为小数串
#print(int(ff),type(int(ff))) #1
#print(int(s3),type(int(s3))) #将str转成int类型时，字符串必须为数字串（整数），非数字串不允许转换
#print(-----------------float()将其他的类型转成float类型-----------------------)
#s1='128.98'
#s2='76'
#ff=True
#s3='hello'
#i=98
#print(type(s1),type(s2),type(ff),type(s3),type(i))
#print(float(s1),type(float(s1)))
#print(float(s2),type(float(s2)))  #76.0
#print(float(ff),type(float(ff)))   #1.0
#print(float(s3),type(float(s3)))   #字符串中的数据如果是非数字串，则不允许转换
#print(float(i),type(float(i)))     #98.0


#python中的注释
#单行注释：#；多行注释：一对三引号之间；



#input函数的使用
#present=input('大圣想要什么礼物呢')  #根据提示语输入一个数据，将输入的数据存储在变量中
#print(present)
#从键盘录入两个数，计算两个整数的和
#a=input('请输入一个加数：')
#b=input('请输入另一个加数：')
#print(type(a),type(b))   #input类型的结果是str类型
#print(a+b)   #加号起连接作用   1020
#a=int(a)
#b=int(b)

#print(1+1)  #加法运算   算数运算符
#加减乘除运算
#print(1/2)  #除法运算  0.5
#print(11//2)  #5  整除运算
#print(11%2)    #取余运算  1
#print(2**2)   #表示2的2次方   4
#print(9//4)     #2
#print(-9//-4)     #2
#print(9//-4)           #-3
#print(-9//4)      #-3  一正一负向下取整
#print(9%-4)   #-3
#print(-9%4)    #3   一正一负要公式   余数=被除数-除数*商

#赋值运算符
#a=b=c=20   #链式赋值
#print(------------------------支持参数赋值------------------------------)
#a=20
#a+=30
#print(a)
#-=,*=,/=,//=,%=
#print(---------------解包赋值-----------------)
#a,b,c=20,30,40   #左右变量个数和值的个数应该一样
#print(a,b,c)
#print(-------------------交换两个变量的值----------------------)
#a,b=10,20
#print('交换之前：'，a,b)
#交换
#a,b=b,a
#print('交换之后：'，a,b)

#比较运算符,比较运算符的结果为布尔类型
#a,b=10,20   
#print('a大于b吗?',a>b)   #False
#<=,>=,==,!=
'''一个 = 称为赋值运算符，== 称为比较运算符
     一个变量由三部分组成：标识、类型、值
     == 比较的是值还是标识呢？比较的是值
     比较对象的标识使用 is '''
#a=10
#b=10
#print(a==b)    #True    a与b的value相等
#print(a is b)   #True    a与b的id标识相等
#list1=[11,22,33,44]
#list2=[11,22,33,44]
#print(lis1==list2)   #True
#print(list1 is list2)     #False
#print(a is not b)     #False
     
#布尔运算符
#a,b=1,2
#print(a==1 and b==2)
#and,or,not（非),in,not in
#print('----------in与not in-------------)
#s='helloworld'
#print('w'in s)   #True
     
#位运算符，将数据转成二进制进行计算
#位与&，位或|左移<<,右移>>
#左移位：高位溢出，低位补0，相当于乘2；右移位：高位补0，低位截断

#运算符的优先级
#算数：先算乘除，再算加减，幂运算优先；>位运算：>比较运算>布尔运算>赋值运算
     
     
     
#程序的组织结构：顺序结构、选择结构、循环结构
#对象的布尔值
#以下对象的布尔值为False:False,数值0，None,空字符串，空列表，空元组，空字典，空集合
#选择结构
#单分支结构：如果下雨，就带伞
#money=1000   #余额
#s=int(input('请输入取款机金额'))   #取款金额
#判断余额是否充足
#if money>=s:
     #money=money-s
     #print('取款成功，余额为:',money)

#双分支结构：如果是妖怪就打，不是就不打     二选一
#从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
#num=int(input('请输入一个整数'))
#条件判断 :使用比较运算符进行比较的运算结果
#if num%2==0:
     #print(num,'是偶数')
#else:
     #print(num,'是奇数')

#多分支结构   多选一执行
'''从键盘录入一个整数,
90-100 A
80-89 B
70-79  C
60-69  D
0-59  E
小于0或大于100属于非法数据（不是程序的有效范围）'''
#score=int(input('请输入一个成绩:'))
#判断
#if score>=90 and score<=100:       #if 90<=score<=100:
    #print('A级')
#elif score>=80 and score<=89:
    #print('B级')
#elif score>=70 and score<=79:
    #print('C级')
#elif score>=60 and score<=69:
    #print('D级')
#elif score>=0 and score<=59:
    #print('E级')
#else:
    #print('对不起，成绩有误，不在成绩的有效范围内')
    
#嵌套if
'''会员  >=200 八折
          >=100 九折
           不打折
非会员   >=200 9.5折
          不打折  
'''
#answer=input('您是会员吗？y/n')
#是会员要输入金额，不是会员也要输入金额，写在判断之前
#money=float(input('请输入您的购物金额:'))
#外层判断是否是会员
#if answer=='y':           #会员
    #print('会员')
    #if money>=200:
        #print('打八折，付款金额为:',money*0.8)
    #elif money>=100:
        #print('打九折，付款金额为:',money*0.9) 
    #else:
        #print('不打折，付款金额为:',money)
#else:
    #print('非会员')                    #非会员
    #if money>=200:
        #print('打9.5折，付款金额为:',money*0.95)
    #else:
        #print('不打折，付款金额为:',money)
    
#条件表达式
'''从键盘录入两个整数，比较两个整数的大小'''
#num_a=int(input('请输入一个整数:'))
#num_b=int(input('请输入第二个整数:'))
#比较大小
#if num_a>=num_b:
    #print(num_a,'大于等于'，num_b)
#else:
    #print(num_a,'小于'，num_b)
#使用条件表达式进行比较
#print(str(num_a)+'大于等于'+str(num_b)    if num_a>=num_b  else  str(num_a)+'小于'+str(num_b)   )
    
#pass语句，什么都不做，只是一个占位符，用到需要写语句的地方
#answer=input('您是会员吗？y/n')
#判断是否是会员
#if answer=='y':           #会员
   #pass
#else:
   #pass
#age=int(input('请输入您的年龄:'))
#if age:
    #print(age)
#else:
    #print('年龄为:',age)
   
    
    
#内置函数range()
#range()的三种创建方式
'''第一种创建方式，只有一个参数(小括号中只给了一个数)'''
#r=range(10)  #[0,1,2,3,4,5,6,7,8,9],默认从0开始，默认相差1称为步长
#print(r)    #range(0,10)
#print(list(r))  #用于查看range对象中的整数序列    list是列表的意思  
  
'''第二种创建方式，给了两个参数(小括号中给了两个数)'''
#r=range(1,10)   #指定了起始值，从1开始，到10结束(不包含10)，默认步长为1
#print(list(r))     #[1,2,3,4,5,6,7,8,9]

'''第三种创建方式，给了三个参数'''
#r=range(1,10,2)  
#print(list(r)) #[1,3,5,7,9]

'''判断指定的整数在序列中是否存在 in,not in'''
#print(10 in r)  #False  10不在当前的r这个整数序列中

#循环结构
#循环的分类：while,for-in
#a=1
#判断条件表达式
#if a<10:
    #执行条件执行体
    #print(a)     #1
    #a+=1       
    
#a=1
#判断条件表达式
#while a<10:
    #执行条件执行体
    #print(a)    #1,2,3,4,5,6,7,8,9
    #a+=1
 
#计算0-4之间的累加和
'''4步循环法
1.初始化变量  2.条件判断  3.条件执行体（循环体）   4.改变变量
总结：初始化的变量与条件判断的变量与改变的变量为同一个'''
#sum=0  #用于存储累加和
'''初始化变量为0'''
#a=0
'''条件判断'''
#while a<5:
#'''条件执行体'''
     #sum+=a
#'''改变变量'''
     #a+=1
#print('和为',sum)   #10
     
#sum=0
#while sum<5:
    #sum=sum+1
#print(sum)     #5 错误

#计算1-100之间的偶数
#sum=0
#初始化变量
#a=1
#条件判断
# while a<=100:
    #条件执行体(求和)
    #条件判断是否为偶数
    #if a%2==0:       if not bool(a%2):
        #sum+=a
    #改变变量
    #a+=1
# print('1-100之间的偶数和为',sum)    #2550
    
    
#sum=0
#初始化变量为2
#a=2
#条件判断
#while a%2==0 and a<=100:
    #条件执行体
    #sum+=a
    #改变变量
   # a+=2
#print('和为',sum)   #2550 正确
   
#for-in循环
'''可迭代对象中还有元素吗？(条件)
没有，直接输出下一句代码
自定义变量自动被赋予当前迭代对应的元素值 -》 循环体 -》对条件进行判断是否还有元素'''  
# for 自定义的变量 in 可迭代对象(字符串、序列):       #在可迭代对象中依次取出一个值，赋给自定义变量
   #循环体
#for item in 'Python' :      #第一次取出来的是P,将P赋值给item,将item的值输出
#    print(item)
   
#range()产生一个整数序列，也是一个可迭代对象
#for i in range(10):
   #print(i)
   
#如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
#for _ in range(5):
   # print('人生苦短,我用Python')     #输出5个 人生苦短,我用Python
   
#使用for循环，计算1-100之间的偶数和
#sum=0  #用于存储偶数和
#for item in range(1,101):
     #if item%2==0:
         #sum+=item
#print('1-100之间的偶数和为'，sum)    #2550
         
#输出100-999之间的水仙花数
#水仙花数：153=3*3*3+5*5*5+1*1*1
# for item in range(100,1000):
         #ge=item%10
         #shi=item//10%10
         #bai=item//100
         #print(bai,shi,ge)
         #判断
         #if ge**3+shi**3+bai**3==item:
             #print(item)
 
#流程控制语句break
#跳出、退出循环
'''从键盘去录入密码，最多录入三次，如果正确，就结束循环'''
#for item in range(3):
    #pwd=input('请输入密码：')
    # if pwd=='8888':
         #print('密码正确')
         #break
    # else:
        # print('密码错误')
        
#a=0
#while a<3:
        #条件执行体（循环体）
        #pwd=input('请输入密码：')
        #if pwd=='8888':
            #print('密码正确')
            #break
        #else:
            #print('密码错误')
            
        #改变变量
        #a+=1
        
#流程控制语句continue
#用于结束当前循环，进入下一循环，从头再来
#要求输出1-50之间所有5的倍数
'''for item in range(1,51):
     if item%5==0:
         print(item)
'''        
'''什么样的数不是5的倍数
1,2,3,4,6,7,8,9...
与5的余数不为0的数都不是5的倍数'''

#使用continue实现
'''for item in range(1,51):
    if item%5!=0:
        continue
    print(item)
 '''   
#else语句
'''while else 和 for else 没有碰到break时执行else'''
#输入密码的问题
'''for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:    #循环正常结束，没有执行break时才会执行
    print('对不起，三次密码均输入错误')'''
 
'''a=0
while a<3:
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a+=1     
else:
    print('对不起，三次密码均输入错误')
'''
    
#嵌套循环
#内层循环给外层循环做循环体
'''输出一个三行四列的矩形'''
'''for i in range(1,4):    #表示的是行数,执行三次，一次是一行
    for j in range(1,5):
        print('*',end='\t')     #不换行输出,end为分隔符参数，为end传递一个字符，print函数就不会再末尾添加一个换行符
    print()    #换行,自带了'\n',所以，print()为一个\n
'''



    


    

        
        
    
    
    

        
        
        
    
    
    
         
   
   
    
    
