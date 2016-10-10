#!/usr/bin/env node
var $ = require('cheerio');
var request = require('request');
var fs = require('fs');
var MongoClient = require('mongodb').MongoClient;
var DB_CONN_STR = 'mongodb://localhost:27017/test_spider';
var url = process.argv[2] || 'http://yundijie.com/search/addresses?offset=0&limit=50&input=Asia%20Hotel%20Bangkok&cityId=230&location=13.689999,100.750112'

header = {
  "Content-Type":"application/json; charset=UTF-8",
  "Authorization":"Basic 6auY5Lya5aifOjEyMzQ1Ng==",
  "Accept": "application/json, text/javascript, */*; q=0.01",
  'Accept-Language':'zh-CN,zh;q=0.8',
  'Accept-Encoding':'gzip, deflate, sdch',
  "Accept-Language":"zh-CN,zh;q=0.8",
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',

  'Cookie':'cla_sso_token=78292837bfe24f3f5834; login_name=%E9%AB%98%E4%BC%9A%E5%A8%9F; JSESSIONID=462DC331C985F72C082735D05954E477; Hm_lvt_c01e035e5dc6df389fa1746afc9cf708=1475908244,1476020986; Hm_lpvt_c01e035e5dc6df389fa1746afc9cf708=1476107248',


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
  //var api_info = body.match(/\{.*\}/)[0];//去除前后多余字段

  //obj = JSON.parse(body);
  console.log(body);

})
