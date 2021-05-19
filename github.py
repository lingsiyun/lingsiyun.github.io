#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 22:51:25 2021

@author: pi
"""
import os
import time  #导入模块
t=0
while True:
    time.sleep(1)
    t=t+1
    p=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(p)
    if t==60:
        
        print(t)
        t=0
        with open('index.html', 'r+') as f:
            content = f.read()        
            f.seek(0, 0)
            f.write(p+'\n'+content)
        b=os.popen("cd /home/pi/github/lingsiyun.github.io && git add --all && git commit -m '注释' && git push").read()
        print(b)

    
    
    #打印当前秒数






