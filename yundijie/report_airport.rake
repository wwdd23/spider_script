$mongo_spider['airportinfo'].find().first



result = [
  [
    'airportCode',
    'airportHotWeight',
    'airportId',
    'airportLocation',
    'airportName',
    'bannerSwitch',
    'isHotAirport',
    'landingVisaSwitch',
    'areaCode',
    'childseatSwitch',
    'cityCode',
    'cityEnName',
    'cityHotWeight',
    'cityId',
    'cityInitial',
    'cityLocation',
    'cityName',
    'citySpell',
    'continentId',
    'continentName',
    'isHotCity',
    'isPasscityHot',
    'neighbourTip',
    'passcityHotWeight',
    'placeCode',
    'placeId',
    'placeName',
    'timezone',
    'tip',

  ]

]

$mongo_spider['airportinfo'].find().each do |n|

  result << [
    n['airportCode'],
    n['airportHotWeight'],
    n['airportId'],
    n['airportLocation'],
    n['airportName'],
    n['bannerSwitch'],
    n['isHotAirport'],
    n['landingVisaSwitch'],
    n['areaCode'],
    n['childseatSwitch'],
    n['cityCode'],
    n['cityEnName'],
    n['cityHotWeight'],
    n['cityId'],
    n['cityInitial'],
    n['cityLocation'],
    n['cityName'],
    n['citySpell'],
    n['continentId'],
    n['continentName'],
    n['isHotCity'],
    n['isPasscityHot'],
    n['neighbourTip'],
    n['passcityHotWeight'],
    n['placeCode'],
    n['placeId'],
    n['placeName'],
    n['timezone'],
    n['tip'],
  ]

end

Emailer.send_custom_file(['wudi@haihuilai.com'], 'test', XlsGen.gen(result), 'test.xls').deliver

File.open('/tmp/test.xls', 'w+') {|f| f.write(XlsGen.gen(result))}

"isHotCity"=>1, 
"isPasscityHot"=>1, 
"neighbourTip"=>"", 
"passcityHotWeight"=>19744, 
"placeCode"=>"AU", 
"placeId"=>1, 
"placeName"=>"澳大利亚", 
"timezone"=>10, 
"tip"=>""}
