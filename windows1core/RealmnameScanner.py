import itertools
import os
import time
import random
import urllib.request
import requests
import re
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit , QTextBrowser , QLineEdit
from threading import Thread
from time import sleep

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

def ping1(x,url1):
    ''''''
    ax=1
    x1=1
    while ax==1:
        an=str(x1)
        word1='开始扫描'+url1+' 的'+an+'位子域名：'
        print(word1)
        text3.append(word1)
        for i in itertools.combinations_with_replacement('0123456789qwertyuiopasdfghjklzxcvbnm', x1):
            a=str(''.join(i))
            word1=('正在扫描：'+'http://'+a+'.'+url1+'/'+'\r')
            print(word1, end=' ')
            text2.setText(word1)
            try:
                m=hanshu1(url1,a)
                if m==0:
                    a=a
                else:
                    print('    '+m)
                    text3.append('    '+m)
            except:
                wordx='    http://'+a+'.'+url1+'/'+' '+'被可访问域名主动拒绝'
                print(wordx)
                text3.append(wordx)
        
        word2 = url1+' 的'+an+'位子域名扫描结束。'
        print(word2)
        text3.append(word2)
        text3.append("")
        print('')
        if x1>x:
            ax=0
        else:
            x1+=1

def thread1():
    ''''''
    x = int(text0.text())
    url1 = text1.text()

    thread = Thread(
        target=ping1, 
        args=(x, url1)
    )

    thread.start()

app = QApplication([])

window = QMainWindow()
window.resize(600, 750)
window.move(500, 50)
window.setWindowTitle('RealmnameScanner for 1 core 1.3.1')

text1 = QLineEdit(window)
text1.setPlaceholderText('需要扫描的主域名：')
text1.move(30,15)
text1.resize(350,30)

text0 = QLineEdit(window)
text0.setPlaceholderText('二级域名长度：')
text0.move(390,15)
text0.resize(120,30)

text2 = QLineEdit(window)
text2.move(30,50)
text2.resize(540,30)

text3 = QTextBrowser(window)
text3.move(30,85)
text3.resize(540,650)

button0 = QPushButton('确定', window)
button0.move(520,15)
button0.resize(50,30)
button0.clicked.connect(thread1)

window.show()
app.exec_()