#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import itertools
import os



print('—————————————')
print('RealmnameScanner Kumaker')
print('—————————————')

print('')
print('输入创建库的序号：',end='')
x=int(input())
def text_create(name, msg):
    '''创建文件'''
    full_path =name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)   
    file.close()

ax=1
if x>8:
    xn=64*36**(x-9)
    word1='如果内存小于'+str(xn)+'GB'+'将会溢出，请问是否继续？ 1.YES 2.NO  '
    print(word1,end='')
    ax=int(input())

print('')

x1=1
while ax==1:
    
    name1='data'+str(x1)+'.txt'
    if os.path.isfile(name1)==False:
        word2='正在计算data'+str(x1)+''
        print(word2)
        list1=list()
        for i in itertools.combinations_with_replacement('0123456789qwertyuiopasdfghjklzxcvbnm', x1):
            a=str(''.join(i))
            list1.append(a)

        print('正在写入文件...')

        name='data'+str(x1)
        list1=str(list1)
        text_create(name, list1)
        print('写入完成')
        print('')    
    else:
        word2='data'+str(x1)+'已存在，开始计算下一个任务'
        print(word2)
        print('')
    
    x1+=1
    if x1>x:
        ax=2
    
print('已完成，按任意键退出')
input()


# In[ ]:




