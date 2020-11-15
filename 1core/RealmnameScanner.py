#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools
import os
import time
import random
import urllib.request
import requests
import re

def hanshu1(url1,url2):
    
    headers = ('User-Agent', '1551wtmsb')
    # 或者随便起个名字，如 headers = {'User-Agent': 'Firefox'}
    
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
        a1=url + ' '+'状态码:' + ztm1
    return(a1)

print('—————————————')
print('RealmnameScanner for 1 core 1.3.0')
print('—————————————')

print('')    
print('输入扫描域名:',end='')
url1=input()
print('')

print('输入扫描强度：',end='')
x=int(input())
print('')

ax=1
x1=1
   
while ax==1:
    
    an=str(ax)
    word1='开始扫描'+an+'位子域名：'
    print(word1)
    for i in itertools.combinations_with_replacement('0123456789qwertyuiopasdfghjklzxcvbnm', x1):
        a=str(''.join(i))
        try:
            m=hanshu1(url1,a)
            if m==0:
                a=a
            else:
                print(m)
        except:
            wordx='http://'+a+'.'+url1+'/'+' '+'被可访问域名主动拒绝'
            print(wordx)
    
    word2=an+'位子域名扫描结束'
    print(word2)
    print('')
    if x1==x:
        ax=0
    else:
        x1+=1
    
print('已完成，按任意键退出')
input()


# In[ ]:




