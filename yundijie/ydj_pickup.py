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

def pickup(params):
    ua = get_ua.get_random_ua()
    headers = {
            'Content-Type':'application/json; charset=UTF-8',
            'Authorization':'Basic 6auY5Lya5aifOjEyMzQ1Ng==',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            #'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
            'User-Agent': ua,
            'Cookie':'JSESSIONID=FA421051C0F377D492AC21AFE2794041; cla_sso_token=9ca653147a0945fc9f62; login_name=BDtest17; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1476429644; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476685105'

            }
    #params = ({"airportCode":"CDG","startLocation":"49.009670,2.547860","endLocation":"48.873642,2.3062469","serviceDate":"2016-11-11 08:00:00","startDate":"2016-11-12","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"CDG","airportHotWeight":0,"airportId":449,"airportLocation":"49.009670,2.547860","airportName":"戴高乐国际机场","bannerSwitch":1,"isHotAirport":0,"landingVisaSwitch":0,"cityId":138,"location":"49.009670,2.547860"},"pickupAddress":{"placeAddress":"35 Rue de Berri, 75008 Paris, 法国","placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png","placeId":"ChIJEzb-M8Fv5kcR9yv80he-4sA","placeLat":48.873642,"placeLng":2.3062469,"placeName":"Hotel Champs Elysées Plaza*****","score":0.9033104181289673,"source":"google"}})
    
    params = params
    #params = ({"airportCode":"BKK","startLocation":"13.689999,100.750112","endLocation":"13.7513821,100.5311441","serviceDate":"2016-10-13 08:00:00","startDate":"2016-10-13","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"BKK","airportHotWeight":0,"airportId":25,"airportLocation":"13.689999,100.750112","airportName":"素万那普国际机场","bannerSwitch":1,"isHotAirport":1,"landingVisaSwitch":0,"cityId":230,"location":"13.756137,100.501747"},"pickupAddress":{"placeName":"Asia Hotel Bangkok","placeAddress":"296 Phayathai Rd, Ratchathewi, Bangkok 10400泰国","placeLat":13.7513821,"placeId":"ChIJH2h86IGe4jARyjZ6wppSlkQ","source":"google","score":1.2428967952728271,"placeLng":100.5311441,"placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png"}})
    
    conn.request("POST", "/price/query_pickup_quotes", json.JSONEncoder().encode(params), headers)
    response = conn.getresponse()
    data_tmp = response.read()
    if response.status == 200:
        print 'success'

        data = StringIO.StringIO(data_tmp)
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
        if datas['status'] != 200:
            print "status error %d" % datas['status']
            next
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
            "created_at": (datetime.date.today()).isoformat(),
            "startDate": startDate, 
            "serviceDate": serviceDate,
            "airportName": airport,
            "address": address,
            "type": "pickup",
            "result": datas['data']
            })
    
        print(data)
    
    else:
        print 'fail'
    conn.close()

def main():
    params = ({"airportCode":"ZRH","startLocation":"47.4508733,8.5662762","endLocation":"22.2799097,114.1737282","serviceDate":"2016-11-14 08:00:00","startDate":"2016-11-14","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"ZRH","airportHotWeight":0,"airportId":574,"airportLocation":"47.4508733,8.5662762","airportName":"苏黎世机场","bannerSwitch":1,"isHotAirport":0,"landingVisaSwitch":0,"cityId":163,"location":"47.368736,8.544955"},"pickupAddress":{"placeName":"中环广场","placeAddress":"香港灣仔港灣道18號","placeLat":22.2799097,"placeId":"ChIJL3xyB1wABDQR2wvMIPNSGOU","source":"google","score":0.002276170300319791,"placeLng":114.1737282,"placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png"}})
    tmp = pickup(params)
    print tmp

if __name__ == '__main__':
    main()

