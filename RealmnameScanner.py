#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


def rounum(a,b):
    '''生成a到b之间的随机数'''
    num=random.randint(a,b)
    return num


def rouxiao():
    '''随机小写字母'''
    num=chr(rounum(97,122))
    return num


def ben1(n1):
    '''输入位数，生成一个随机二级域名'''
    n1=rounum(1,10)
    ax=1
    result=[]
    with open('data.txt','r') as f:
        for line in f:
            list1=str(list(line.strip('\n').split(',')))
            list1=list1.strip('[')
            list1=list1.strip(']')
            list1=list1.strip("'")
            result.append(list1)
    a1=0
    while a1==0:
        a=1
        url1=''
        while a<=n1:
            b=rounum(0,1)
            if b==0:
                url1+=str(rounum(0,9))
            else:
                url1+=rouxiao()
            a+=1
        if url1 in result:
            a1=0
            ax+=1
        else :
            a1=1
            url2=url1+'\n'
            with open('data.txt','a') as f:            
                f.write(url2)
                f.close()
        if ax>=500:
            a1=1
    return(url1)


# In[1]:


import Scannermods
import sys
import time
import pp

print('——————————————————————')
print('RealmnameScanner v1.00')
print('——————————————————————')

list1 = list()##创建一个检索列表

print('输入主域名:')
url1 = input()

print('')

file1 = open("data.txt", 'w').close()

print('调用线程数：')
usecpu=input()

print('')
print('开始扫描....')
print('')

job_server = pp.Server(int(usecpu))
start_time =time.time()

x=0
a=1
while x==0:
    ap = 36
    inputs=(a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a)
    results = [(input,job_server.submit(ben1,(input,),(rounum,rouxiao,),("random",))) for input in inputs ]

    for input, result in results:
        url2=str(result())
        url='http://'+url2+'.'+url1+'/'
        if Scannermods.mod1(url)==1:
            ztm1=str(Scannermods.mod2(url))
            output1=url + ' '+'状态码:' + ztm1
            print(output1)

