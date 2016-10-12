#!/usr/bin/env python
#-*- coding:utf-8 -*-
############################
#File Name:
#Author: wudi
#Mail: programmerwudi@gmail.com
#Created Time: 2016-10-10 11:48:20
############################

import json
from pprint import pprint

def cat():
    #params = ({"airportCode":"CDG","startLocation":"49.009670,2.547860","endLocation":"48.873642,2.3062469","serviceDate":"2016-11-11 08:00:00","startDate":"2016-11-12","startTime":"08:00","flightInfo":{"is_custom":1},"airportInfo":{"airportCode":"CDG","airportHotWeight":0,"airportId":449,"airportLocation":"49.009670,2.547860","airportName":"戴高乐国际机场","bannerSwitch":1,"isHotAirport":0,"landingVisaSwitch":0,"cityId":138,"location":"49.009670,2.547860"},"pickupAddress":{"placeAddress":"35 Rue de Berri, 75008 Paris, 法国","placeIcon":"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png","placeId":"ChIJEzb-M8Fv5kcR9yv80he-4sA","placeLat":48.873642,"placeLng":2.3062469,"placeName":"Hotel Champs Elysées Plaza*****","score":0.9033104181289673,"source":"google"}})
    

    params = ( {"airportCode"=>"BKK", "startLocation"=>"13.689999,100.750112", "endLocation"=>"100.5311441,13.7513821", "serviceDate"=>"2016-10-13 16:35:40 +0800", "startDate"=>"2016-10-13", "startTime"=>"08:00", "flightInfo"=>{:is_custom=>1}, "airportInfo"=>{:airportCode=>"BKK", :airportHotWeight=>0, :airportId=>25, :airportLocation=>"13.689999,100.750112", :airportName=>"素万那普国际机场", :bannerSwitch=>1, :isHotAirport=>1, :landingVisaSwitch=>0, :cityId=>230, :location=>nil}, "pickupAddress"=>{"placeName"=>"Asia Hotel Bangkok", "placeAddress"=>"296 Phayathai Rd, Ratchathewi, Bangkok 10400泰国", "placeLat"=>13.7513821, "placeId"=>"ChIJH2h86IGe4jARyjZ6wppSlkQ", "source"=>"google", "score"=>1.2428967952728271, "placeLng"=>100.5311441, "placeIcon"=>"https://maps.gstatic.com/mapfiles/place_api/icons/lodging-71.png"}})
    
    info = json.dumps(params, ensure_ascii=False, indent=4)  
    
    data = json.loads(info)
    airport = data['airportInfo']['airportName']
    address = data['pickupAddress']['placeName']
    
    startDate = data['startDate']
    serviceDate = data['serviceDate']
    
    
    print airport
    print address
    print startDate
    print serviceDate
