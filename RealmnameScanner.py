#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


def rounum(a,b):
    '''生成a到b之间的随机数'''
    num=random.randint(a,b)
    return num


def rouxiao():
    '''随机小写字母'''
    num=chr(rounum(97,122))
    return num


# In[ ]:


import Scannermods

print('——————————————————————')
print('RealmnameScanner v1.00')
print('——————————————————————')

list1 = list()##创建一个检索列表

print('输入主域名:')
url1 = input()

a=0
n=1
n2=1 ##n2为二级域名位数

a=1
a1=1
n1=1
a2=36

print('开始扫描....')
print('')

while a>=0:
    while a1<=a2:
        b1=1
        url2=''
        while b1<=n2:
            if rounum(0,1)==0:
                url2+=str(rounum(0,9))
            else:
                url2+=rouxiao()
            b1+=1
        if (url2 in list1):
            a+=0
        else:
            list1.append(url2)
            url='http://'+url2+'.'+url1+'/'
            
            if Scannermods.mod1(url)==1:
                ztm1=str(Scannermods.mod2(url))
                output1=str(a)+' '+ url + ' '+'状态码:' + ztm1
                print(output1)
            ##
            
            a1+=1
            a+=1
    a1=1
    a2=a2*36
    n2+=1

    
input()


# In[ ]:




