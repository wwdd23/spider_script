#!/usr/bin/env node

//试例
////./kancho_rakuten_calendar_hotel.js 'http://hotel.travel.rakuten.co.jp/hplan/calendar/?f_no=10888&f_syu=trp&f_camp_id=2968487&f_flg=PLAN&f_hizuke=20150823&f_otona_su=3&f_s1=0&f_s2=0&f_y1=0&f_y2=0&f_y3=0&f_y4=0&f_heya_su=1&f_teikei=quick&f_calendar=20150923&f_thick=1&callback=jQuery15209357266612350941_1440322872116&render=jsonp&_=1440326975173';
////
////注意参数  f_no=10888 f_syu=trp f_camp_id=2968487 f_hizuke=20150823 f_otona_su=3 f_calendar=20150923
////          酒店id     roomCode   roomId           当前日期          使用人数      日历时
//间点
//
var $ = require('cheerio');
var request = require('request');
var fs = require('fs');
var MongoClient = require('mongodb').MongoClient;
var DB_CONN_STR = 'mongodb://localhost:27017/test_spider';


// 连接字符串格式为mongodb://主机/数据库名
//exports.mongoose = mongoose;
//var iconv = require('iconv-lite');
var url = process.argv[2] || 'https://fr.huangbaoche.com/reflash/cla/city_airports.js?1475999177939'

// url area  https://fr.huangbaoche.com/reflash/cla/static_area.js?1475999177939   


header = {

  "Content-Type":"application/json; charset=UTF-8",
  "Authorization":"Basic 6auY5Lya5aifOjEyMzQ1Ng==",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding":"gzip, deflate",
  "Accept-Language":"zh-CN,zh;q=0.8",
  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
  //  'Cookie': 'cla_sso_token=702a7a62cbd142e35843; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=84123C258BC1CCD2274E4787117CDEF9; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476027955'

}

request.get( { method: 'GET', url: url, gzip: true, timeout: 5 * 1000 } , function(error, response, body) {
  if (error && error.code ==='ETIMEDOUT') {
    process.exit(0);
    return;
  }
  if(response == null) {
    process.exit(0);
    return;
  }
  if(response.statusCode != 200) {
    process.exit(0);
    return;
  }


  // 插入到mongo表中
  var insertData = function(db, callback) {  
    //连接到表  
    var collection = db.collection('airportinfo');
    console.log('in mongo');

    var api_info = body.match(/\{.*\}/)[0];//去除前后多余字段

    obj = JSON.parse(api_info);



    var count = 0;
    for(var key in obj.all) {
      if(obj.all.hasOwnProperty(key)){
        count++;
        console.log(key);

        for ( i = 0 ; i< obj.all[key].length ; i++) {
          if (obj.all[key][i]['airports'].length > 1) {
            //console.log(obj.all[key][i]['airports']);

            for ( y = 0 ; y < obj.all[key][i]['airports'].length ; y++) {
    //          console.log(obj.all[key][i]['airports'][y]);
     //         console.log(obj.all[key][i]['airports'][y]['cityName']);
              console.log("in----" + key);
              var data = {
                "airportCode": obj.all[key][i]['airports'][y]['airportCode'],
                "airportHotWeight":  obj.all[key][i]['airports'][y]['airportHotWeight'],
                "airportId":  obj.all[key][i]['airports'][y]['airportId'],
                "airportLocation":  obj.all[key][i]['airports'][y]['airportLocation'],
                "airportName":  obj.all[key][i]['airports'][y]['airportName'],
                "bannerSwitch":  obj.all[key][i]['airports'][y]['bannerSwitch'],
                "isHotAirport":  obj.all[key][i]['airports'][y]['isHotAirport'],
                "landingVisaSwitch":  obj.all[key][i]['airports'][y]['landingVisaSwitch'],


                "areaCode": obj.all[key][i]['areaCode'],
                "childseatSwitch":  obj.all[key][i]['childseatSwitch'],
                "cityCode":  obj.all[key][i]['cityCode'],
                "cityEnName":  obj.all[key][i]['cityEnName'],
                "cityHotWeight":  obj.all[key][i]['cityHotWeight'],
                "cityId":  obj.all[key][i]['cityId'],
                "cityInitial":  obj.all[key][i]['cityInitial'],
                "cityLocation":  obj.all[key][i]['cityLocation'],
                "cityName":  obj.all[key][i]['cityName'],
                "citySpell":  obj.all[key][i]['citySpell'],
                "continentId":  obj.all[key][i]['continentId'],
                "continentName":  obj.all[key][i]['continentName'],
                "dstSwitch":  obj.all[key][i]['dstSwitch'],
                "hasPrice":  obj.all[key][i]['hasPrice'],
                "isHotCity":  obj.all[key][i]['isHotCity'],
                "isPasscityHot":  obj.all[key][i]['isPasscityHot'],
                "neighbourTip":  obj.all[key][i]['neighbourTip'],
                "passcityHotWeight":  obj.all[key][i]['passcityHotWeight'],
                "placeCode":  obj.all[key][i]['placeCode'],
                "placeId":  obj.all[key][i]['placeId'],
                "placeName":  obj.all[key][i]['placeName'],
                "timezone":  obj.all[key][i]['timezone'],
                "tip":  obj.all[key][i]['tip']
              }

              collection.insert(data, function(err, result) { 
                if(err)
                {
                  console.log('Error:'+ err);
                  return;
                }     
                callback(result);
              });
            }
          } else {
              console.log("in----111" + key);
              console.log(obj.all[key][i]['airports'][0]['airportName']);
              var data = {
                "airportCode": obj.all[key][i]['airports'][0]['airportCode'],
                "airportHotWeight":  obj.all[key][i]['airports'][0]['airportHotWeight'],
                "airportId":  obj.all[key][i]['airports'][0]['airportId'],
                "airportLocation":  obj.all[key][i]['airports'][0]['airportLocation'],
                "airportName":  obj.all[key][i]['airports'][0]['airportName'],
                "bannerSwitch":  obj.all[key][i]['airports'][0]['bannerSwitch'],
                "isHotAirport":  obj.all[key][i]['airports'][0]['isHotAirport'],
                "landingVisaSwitch":  obj.all[key][i]['airports'][0]['landingVisaSwitch'],


                "areaCode": obj.all[key][i]['areaCode'],
                "childseatSwitch":  obj.all[key][i]['childseatSwitch'],
                "cityCode":  obj.all[key][i]['cityCode'],
                "cityEnName":  obj.all[key][i]['cityEnName'],
                "cityHotWeight":  obj.all[key][i]['cityHotWeight'],
                "cityId":  obj.all[key][i]['cityId'],
                "cityInitial":  obj.all[key][i]['cityInitial'],
                "cityLocation":  obj.all[key][i]['cityLocation'],
                "cityName":  obj.all[key][i]['cityName'],
                "citySpell":  obj.all[key][i]['citySpell'],
                "continentId":  obj.all[key][i]['continentId'],
                "continentName":  obj.all[key][i]['continentName'],
                "dstSwitch":  obj.all[key][i]['dstSwitch'],
                "hasPrice":  obj.all[key][i]['hasPrice'],
                "isHotCity":  obj.all[key][i]['isHotCity'],
                "isPasscityHot":  obj.all[key][i]['isPasscityHot'],
                "neighbourTip":  obj.all[key][i]['neighbourTip'],
                "passcityHotWeight":  obj.all[key][i]['passcityHotWeight'],
                "placeCode":  obj.all[key][i]['placeCode'],
                "placeId":  obj.all[key][i]['placeId'],
                "placeName":  obj.all[key][i]['placeName'],
                "timezone":  obj.all[key][i]['timezone'],
                "tip":  obj.all[key][i]['tip']
              }

              collection.insert(data, function(err, result) { 
                if(err)
                {
                  console.log('Error:'+ err);
                  return;
                }     
                callback(result);
              });
            }
          
          
          }
        }
      }
    }
  
  //插入数据

  MongoClient.connect(DB_CONN_STR, function(err, db) {
    console.log("连接成功！");
    insertData(db, function(result) {
      console.log(result);
      db.close();
    });
  });

  //console.log(JSON.stringify(obj['all'].length, undefined, 3));
  //console.log(JSON.stringify(obj,undefined,3));


  //for (var i = 0 ; i< obj.all.length ; i++) {
  //  console.log(obj.all[i]);
  //}

 // setTimeout(function () {
 //   process.exit(0);
 // }, 1000);
})

