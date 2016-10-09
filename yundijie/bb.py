#!/usr/bin/env python
#-*- coding:utf-8 -*-
############################
#File Name:
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2016-10-09 22:53:02
############################


import os, sys, re, json
import subprocess
import requests
from lxml import etree
import urllib  
import urllib2  
import cgi
import gzip
import StringIO


url = 'http://yundijie.com/'
#req = urllib.request.Request(url, headers = {
#req = requests.get(url, headers = {
r = urllib2.Request(url, headers = {
    'Content-Type':'application/json; charset=UTF-8',
    'Authorization':'Basic 6auY5Lya5aifOjEyMzQ1Ng==',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    #'Cookie':'JSESSIONID= 23B95B78993912477ACCDDFD733CDF37',
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
    'Cookie': 'cla_sso_token=702a7a62cbd142e35843; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=84123C258BC1CCD2274E4787117CDEF9; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476027955'
    })
response = urllib2.urlopen(r)  
page = response.read()
#html =str(response.read(),'utf-8')

#html = page.decode('unicode').encode('utf-8')

data = StringIO.StringIO(page)
gz = gzip.GzipFile(fileobj=data)
data = gz.read()
gz.close()

print data
#html = page.decode('unicode').encode('utf-8')
#print page




