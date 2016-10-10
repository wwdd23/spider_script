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
var url = process.argv[2] || 'http://yundijie.com/search/addresses?offset=0&limit=50&input=Asia%20Hotel%20Bangkok&cityId=230&location=13.689999,100.750112'

// url area  https://fr.huangbaoche.com/reflash/cla/static_area.js?1475999177939   


header = {
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding":"gzip, deflate, sdch",
  "Accept-Language":"zh-CN,zh;q=0.8",
  "Cache-Control":"no-cache",
  "Connection": "keep-alive",
  "Cookie":"cla_sso_token=78292837bfe24f3f5834; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=79428E052E537716C8AA2F8CD6800AD2; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476110502",
  "Host":"yundijie.com",
  "Pragma":"no-cache",
  "Referer":"http://yundijie.com/order/pickup",
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
  "X-Requested-With":"XMLHttpRequest",

//  "Content-Type":"application/json; charset=UTF-8",
//  "Authorization":"Basic 6auY5Lya5aifOjEyMzQ1Ng==",
//  "Accept": "application/json, text/javascript, */*; q=0.01",
//  "Accept-Encoding":"gzip, deflate",
//  "Accept-Language":"zh-CN,zh;q=0.8",
//  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
//  'Cookie': 'cla_sso_token=78292837bfe24f3f5834; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=462DC331C985F72C082735D05954E477; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476107248'
//  //  'Cookie': 'cla_sso_token=702a7a62cbd142e35843; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=84123C258BC1CCD2274E4787117CDEF9; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476027955'

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

  console.log(body);
 // var api_info = body.match(/\{.*\}/)[0];//去除前后多余字段

 //  obj = JSON.parse(api_info);



 //  var count = 0;
 //  for(var key in obj.all) {
 //    if(obj.all.hasOwnProperty(key)){
 //      count++;
 //  console.log(key);

 //    }
 //  };
 // 
 // console.log(obj.all['1'].length);
 // console.log(obj.all['2'].length);
 // console.log(obj.all['3'].length);
 // console.log(obj.all['4'].length);
 // console.log(obj.all['5'].length);
 // console.log(obj.all['6'].length);
 // console.log(obj.all['6'][1]['cityName']);

 // for ( i = 0 ; i< obj.all['1'].length ; i++) {
 //   if (obj.all['1'][i]['airports'].length > 1) {
 //     //console.log(obj.all['1'][i]['airports']);

 //     for ( y = 0 ; y< obj.all['1'][i]['airports'].length ; y++) {
 //       console.log(obj.all['1'][i]['airports'][y]);



 //     }
 //   }
 // }
 // //console.log(JSON.stringify(obj['all'].length, undefined, 3));
 // //console.log(JSON.stringify(obj,undefined,3));


 // //for (var i = 0 ; i< obj.all.length ; i++) {
 // //  console.log(obj.all[i]);
 // //}

 // setTimeout(function () {
 //   process.exit(0);
 // }, 3000);
})

