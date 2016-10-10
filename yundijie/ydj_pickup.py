#!/usr/bin/env python
#-*- coding: utf-8 -*-


import httplib
import json
import StringIO
import gzip
import pymongo

conn = httplib.HTTPConnection("yundijie.com")

headers = {
        'Content-Type':'application/json; charset=UTF-8',
        'Authorization':'Basic 6auY5Lya5aifOjEyMzQ1Ng==',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie':'JSESSIONID= 23B95B78993912477ACCDDFD733CDF37',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
        'Cookie':'JSESSIONID=B057E8AB6C2A10380562D6E455E0B105; cla_sso_token=3002e53498cc4c47bc16; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1475983325,1475994954; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476088465',

        }
#params = ({"bindHyCardInfo":{"mobileNo":"1881026xxxx","userId":"2","cardno":"7926279367963021","cardpasswd":"xxxxxxxxxxxxxxx","ip":"127.0.0.1"},"header":{"version":"1.0.1","from":"1000","to":"2000","tid":"7926279367963021","time":"12312","token":"SEW342WEER2342","ext":""}})
params = ({"airportCode":"CDG","startLocation":"49.009670,2.547860","endLocation":"48.873642,2.3062469","serviceDate":"2016-11-11 08:00:00","startDate":"2016-11-12","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"CDG","airportHotWeight":0,"airportId":449,"airportLocation":"49.009670,2.547860","airportName":"戴高乐国际机场","bannerSwitch":1,"isHotAirport":0,"landingVisaSwitch":0,"cityId":138,"location":"49.009670,2.547860"},"pickupAddress":{"placeAddress":"35 Rue de Berri, 75008 Paris, 法国","placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png","placeId":"ChIJEzb-M8Fv5kcR9yv80he-4sA","placeLat":48.873642,"placeLng":2.3062469,"placeName":"Hotel Champs Elysées Plaza*****","score":0.9033104181289673,"source":"google"}})

conn.request("POST", "/price/query_pickup_quotes", json.JSONEncoder().encode(params), headers)
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
    spiderdata = spider['spiderdata']

    datas = json.loads(data)
    print datas.keys()
    print datas['status']
    #for data in datas['data']:
    params_info = json.dumps(params, ensure_ascii=False, indent=4)  
    
    params_data = json.loads(params_info)
    airport = params_data['airportInfo']['airportName']
    address = params_data['pickupAddress']['placeName']
    
    startDate = params_data['startDate']
    serviceDate = params_data['serviceDate']
    
    
    print airport
    print address
    print startDate
    print serviceDate
    spiderdata.insert_one({
        "startDate": startDate, 
        "serviceDate": serviceDate,
        "airportName": airport,
        "address": address,
        "result": datas['data']
        })

    print(data)

else:
    print 'fail'
conn.close() 
