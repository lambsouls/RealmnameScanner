#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pp
import time
import random
import urllib.request
import requests
import re
import itertools


#函数区域

def text_create(name, msg):
    '''创建文件'''
    full_path =name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)   
    file.close()

def hanshu2(url2):
    
    try:
        headers = ('User-Agent', '1551wtmsb')
        # 或者随便起个名字，如 headers = {'User-Agent': 'Firefox'}

        with open('url1.txt','r',encoding='utf-8') as f:
            url1 = str(f.read())
            f.close()
        url='http://'+url2+'.'+url1+'/'

        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        try :
            opener.open(url)
            a1=1
        except urllib.error.HTTPError:
            a1=0
        except urllib.error.URLError:
            a1=0
        if a1==1:
            r=requests.get(url,timeout=10)
            r.addheaders = [headers]
            r = str(requests.get(url,timeout=10))
            a = re.findall(r"\d+\.?\d*",r)
            a = int("," . join(a))
            ztm1=str(a)
            output1=url + ' '+'状态码:' + ztm1
        else:
            output1='None'
    except:
        output1='http://'+url2+'.'+url1+'/'+' '+'被可访问域名主动拒绝'
    return(output1)

print('————————————')
print('RealmnameScanner v1.3.1')
print('————————————')

print('')    
print('输入扫描域名:',end='')
url1=input()        
text_create('url1', url1)
print('')

#创建检查列表
list1 = list() 

##创建pp server进程和多线程
print('正在创建线程...')
job_server = pp.Server() 
start_time =time.time()
print('线程创建完成')
print('')

##以pp模式运行函数hanshu1()多线程32次
print('输入扫描强度:',end='')
nx=int(input())
n=1
x11=0

#循环主体
while x11==0:
    
    xn1=1
    x=1
    xn=1
    for i in itertools.combinations_with_replacement('0123456789qwertyuiopasdfghjklzxcvbnm', n):
        xn+=1  
    print('                                                       ')
    word2='正在读取'+str(n)+'位库......'
    print(word2)
    
    name='data'+str(n)+'.txt'
    with open(name, encoding="utf-8") as f:
        str1 = f.read()
        url1=eval(str1)
    list2=tuple(url1)

    results2 = [(m2,job_server.submit(hanshu2,(m2,),(urllib.request.build_opener,),("urllib.request","requests","re",))) for m2 in list2 ]
    print("读取完毕，开始继续扫描：")
    for m2, result2 in results2:
        mo2=str(result2())
        xnb=str((xn1/xn)*100)[:10]+'%'
        xn1+=1
        if mo2=='None':
            mo3='\r'+'进度：'+xnb+'\r'
            print(mo3,end= " ")
        else:
            mo3='\r'+'进度：'+xnb+'\r'
            print(mo3,end= " ")
            print(mo2)
    
    word3=str(n)+'位库扫描完毕                      '
    print(word3)
    n=int(n)
    if n<nx:
        n+=1
    else:
        x11=1
    
print('')
print('扫描结束')
input()


# In[ ]:




