#!/usr/bin/env python
#-*- coding: utf-8 -*-


import httplib
import json
import StringIO
import gzip
import pymongo
import urllib
import datetime

def get_data(urls,ename):
    # 连接数据库
    conn = httplib.HTTPConnection("yundijie.com")
    headers = {
            'Content-Type':'application/json; charset=UTF-8',
            'Authorization':'Basic 6auY5Lya5aifOjEyMzQ1Ng==',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            #'Cookie':'JSESSIONID= 23B95B78993912477ACCDDFD733CDF37',

            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
            'Cookie': 'JSESSIONID=7402CFE46187B6367595ABDDAB1AAAD9; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1475983325,1475994954; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476242872; cla_sso_token=bdaf19557f1042d77105; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F'
            }
    
    #conn.request("POST", "/price/query_pickup_quotes", json.JSONEncoder().encode(params), headers)
    #conn.request(method = "GET", url = "http://yundijie.com/search/addresses?offset=0&limit=50&input=Asia Hotel Bangkok&cityId=230&location=13.689999,100.750112", headers =  headers)

    conn.request(method = "GET", url = urls, headers = headers)
    response = conn.getresponse()
    data = response.read()
    if response.status == 200:
        print 'success'
        data = StringIO.StringIO(data)
        gz = gzip.GzipFile(fileobj=data)
        data = gz.read()
        gz.close()
        client = pymongo.MongoClient('localhost', 27017)
        spider = client['test_spider']
        spiderdata = spider['cityinfo']
    
        datas = json.loads(data)
        print datas.keys()
        print datas['status']
        print datas['data']
    
        count = datas['data']['count']
        # 插入数据
        spiderdata.insert_one({
            "ename": ename,
            "create_at": datetime.datetime.now(),
            "result": datas['data']['places'][0]
            })

    else:
        print 'fail'
    conn.close() 
