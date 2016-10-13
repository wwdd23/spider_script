#!/usr/bin/env python
#-*- coding:utf-8 -*-
############################
#File Name:
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2016-10-11 10:42:31
############################

import time

#import read_params
import ydj_search 
import string

import urllib
import datetime
import json

import ydj_pickup
from pprint import pprint
import math


f = open("/tmp/pickup.json",'r')             # 返回一个文件对象
line = json.loads(f.readline())
count = 0
for i in line:
    #pprint(i)
    time.sleep(4)
    print count
    ydj_pickup.pickup(i)
#line = f.readlines()
#print line
#for i in line:
#    print i




#print line
#for i in line:
#    print i,
#    url = "http://yundijie.com/search/addresses?offset=0&limit=50&" + urllib.urlencode({"input":i})
#    print url
#    time.sleep()
#    ydj_search.get_data(url,i.strip('\n') )

#while line:
#    # print(line, end = '')　　　# 在 Python 3中使用
#    print line,                 # 后面跟 ',' 将忽略换行符
#    line = f.readline()
#    url = "http://yundijie.com/search/addresses?offset=0&limit=50&" + urllib.urlencode({"input":line})
#    print url
#    time.sleep(3)
#    #ydj_search.get_data(url,line.strip('\n'))

f.close()
