#!/usr/bin/env python
#-*- coding: utf-8 -*-

import httplib
import json
import StringIO
import gzip
import pymongo
import get_ua

import datetime

conn = httplib.HTTPConnection("yundijie.com")

def trans(params):
    
    ua = get_ua.get_random_ua()
    headers = {
            'Content-Type':'application/json; charset=UTF-8',
            'Authorization':'Basic 6auY5Lya5aifOjEyMzQ1Ng==',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            #'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
            'User-Agent': ua,
            #'Cookie': cookies,
            'Cookie': 'JSESSIONID=FA421051C0F377D492AC21AFE2794041; cla_sso_token=9ca653147a0945fc9f62; login_name=BDtest17; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1476429644; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476684919',

            #'Cookie':'JSESSIONID=AC5AE2594627900BCC1B188BD5E30419; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1475983325,1475994954; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476331358; cla_sso_token=41ac3ae3d4e64b09b923; login_name=BDtest17'
            }
    #params = ({"airportCode":"CDG","startLocation":"49.009670,2.547860","endLocation":"48.873642,2.3062469","serviceDate":"2016-11-11 08:00:00","startDate":"2016-11-12","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"CDG","airportHotWeight":0,"airportId":449,"airportLocation":"49.009670,2.547860","airportName":"戴高乐国际机场","bannerSwitch":1,"isHotAirport":0,"landingVisaSwitch":0,"cityId":138,"location":"49.009670,2.547860"},"pickupAddress":{"placeAddress":"35 Rue de Berri, 75008 Paris, 法国","placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png","placeId":"ChIJEzb-M8Fv5kcR9yv80he-4sA","placeLat":48.873642,"placeLng":2.3062469,"placeName":"Hotel Champs Elysées Plaza*****","score":0.9033104181289673,"source":"google"}})
    
    
    params = params

    conn.request("POST", "/price/query_transfer_quotes", json.JSONEncoder().encode(params), headers)
    response = conn.getresponse()
    data = response.read()
    if response.status == 200:
        print 'success'
        print data
        data = StringIO.StringIO(data)

        print data.len
        try:
            gz = gzip.GzipFile(fileobj=data)
            print gz
            data = gz.read()
            gz.close()
        except:
           print "none gz pass"
           gz.close()
           return
        client = pymongo.MongoClient('localhost', 27017)
        spider = client['test_spider']
        spiderdata = spider['spiderdata']
    
        datas = json.loads(data)
        print datas.keys()
        print datas['status']
        #for data in datas['data']:
        params_info = json.dumps(params, ensure_ascii=False, indent=4)  
        
        params_data = json.loads(params_info)
        airport = params_data['airportInfo']['airportName']
        address = params_data['transferAddress']['placeName']
        
        startDate = params_data['startDate']
        serviceDate = params_data['serviceDate']
        
        
        print airport
        print address
        print startDate
        print serviceDate
        spiderdata.insert_one({
            "created_at": (datetime.date.today()).isoformat(),
            "startDate": startDate, 
            "serviceDate": serviceDate,
            "airportName": airport,
            "address": address,
            "type": "transfer",
            "result": datas['data']
            })
    
        print(data)
    
    else:
        print 'fail'
    conn.close() 
