#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pp
import time
import random
import urllib.request
import requests
import re


#函数区域

def text_create(name, msg):
    '''创建文件'''
    full_path =name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)   
    file.close()
    
    
def hanshu1(x1):
    '''生成一个随机数字和小写字母组成的字符串，x1为最大位数'''
    x1=int(x1)
    num1=random.randint(1,x1)#生成随机位数
    a=1
    str1=''
    while a<=num1:
        num2=random.randint(0,1)#判断是数字还是小写字母，0是数字，一是小写字母
        if num2==0:
            str2=str(random.randint(0,9))
        if num2==1:
            str2=chr(random.randint(97,122))
        str1+=str2
        a+=1
    return(str1)

def hanshu2(url2):
    with open('url1.txt','r',encoding='utf-8') as f:
        url1 = str(f.read())
        f.close()
    url='http://'+url2+'.'+url1+'/'
    opener = urllib.request.build_opener()
    try :
        opener.open(url)
        a1=1
    except urllib.error.HTTPError:
        a1=0
    except urllib.error.URLError:
        a1=0
    if a1==1:
        r = str(requests.get(url))
        a = re.findall(r"\d+\.?\d*",r)
        a = int("," . join(a))
        ztm1=str(a)
        output1=url + ' '+'状态码:' + ztm1
        return(output1)

print('输入扫描域名:')
url1=input()        
text_create('url1', url1)

#创建检查列表
list1 = list() 

##创建pp server进程
job_server = pp.Server() 
start_time =time.time()

##以pp模式运行函数hanshu1()多线程32次
print('输入扫描强度:')
a=input()
x11=0

#循环主体
while x11==0:
    inputs=(a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a)
    results = [(input,job_server.submit(hanshu1,(input,),(random.randint,),("random",))) for input in inputs ]

    #结果去重并转换为元组
    list2=list()
    for input, result in results:
        mo1=str(result())
        if mo1 in list1:
            mo1=str(result())
        else:
            list2.append(mo1)
            list1.append(mo1)

    list2=list(set(list2))
    list2=tuple(list2)

    results2 = [(m2,job_server.submit(hanshu2,(m2,),(urllib.request.build_opener,),("urllib.request","requests","re",))) for m2 in list2 ]
    for m2, result2 in results2:
        mo2=str(result2())
        if mo2=='None':
            mo2='None'
        else:
            print(mo2)
    


# In[ ]:




