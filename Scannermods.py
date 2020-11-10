#!/usr/bin/env python
# coding: utf-8

# In[25]:


import urllib.request


def mod1(tempUrl):
    '''判断网页收能访问，能返回1，不能返回0'''
    opener = urllib.request.build_opener()

    try :
        opener.open(tempUrl)
        a=1
    except urllib.error.HTTPError:
        a=0
    except urllib.error.URLError:
        a=0
        
    return(a)


# In[56]:


import requests
import re


def mod2(tempUrl):
    '''返回url的返回值'''
    r = str(requests.get(tempUrl))
    a = re.findall(r"\d+\.?\d*",r)
    a = int("," . join(a))
    return(a)


# In[ ]:




