#!/usr/bin/env nodejs

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
//var iconv = require('iconv-lite');
var url = process.argv[2] || 'http://yundijie.com/price/query_pickup_quotes'


header = {

  "Content-Type":"application/json; charset=UTF-8",
  "Authorization":"Basic 6auY5Lya5aifOjEyMzQ1Ng==",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  "Accept-Encoding":"gzip, deflate",
  "Accept-Language":"zh-CN,zh;q=0.8",
  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14',
  'Cookie': 'cla_sso_token=702a7a62cbd142e35843; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=84123C258BC1CCD2274E4787117CDEF9; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476027955'

}


request.get({url:url, headers: header , encoding:null },function(error, response, body) {
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

  $ = $.load(body); 
  //js_info = JSON.parse(body)['html']
  getJson = json.loads(body)
  console.log(getJson)

});
