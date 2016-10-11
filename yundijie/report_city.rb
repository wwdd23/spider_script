res = [['Ename','placeName', 'placeAddress', 'placeLat', 'placeLng',
        'placeId', 'source', 'score', 'placeIcon' 
]]
$mongo_spider['cityinfo'].find().each do |row|

  
  data = row['result']

  res << [
    row['enname'],
    data['placeName'],
    data['placeAddress'],
    data['placeLat'],
    data['placeLng'],
    data['placeId'],
    data['source'],
    data['score'],
    data['placeIcon'],
  ]


end
File.open('/tmp/city.xls', 'w+') {|f| f.write(XlsGen.gen(res))}
