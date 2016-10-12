#encoding: utf-8
namespace :create_post do 

  dese "接机post数据生成"
  task :xxxx => :enviroment do 
    send = []
    info.each do |n|
      coutnry = n[0]
      aircode = n[1]
      hotel = n[3]
      airport_send = {
        "airportCode": airport['airportCode'],
        "airportHotWeight": airport['airportHotWeight'],
        "airportId":airport['airportId'],
        "airportLocation":airport['airportLocation'],
        "airportName": airport['airportName'],
        "bannerSwitch":airport['bannerSwitch'],
        "isHotAirport":airport['isHotAirport'],
        "landingVisaSwitch": airport['landingVisaSwitch'],
        "cityId":airport['cityId'],
        "location":airport['cityLocation']}

      #pickup task
      pickup_re = {
        "airportCode"=> airport['airportCode'],
        "startLocation" => airport['airportLocation'],
        "endLocation" => "#{house['result']['placeLat']},#{house['result']['placeLng']}",
        "serviceDate" => "#{Time.now.tomorrow.to_date.to_s} 08:00:00", # 修正格式
          "startDate" => Time.now.tomorrow.to_date.to_s,
          "startTime" => "08:00",
          "flightInfo" => {"is_custom":1},
          "airportInfo" => airport_send,
          "pickupAddress" => house['result'],
      }

      send << pickup_re
    end
    File.open('/tmp/pickup.json', 'w+') {|f| f.write(send.to_json)}
  end


  dese "送机POST数据生成"
  task :xxxx => :enviroment do 
    send = []
    date_array = Time.now.tomorrow.to_date...(Time.now.to_date + 30.days)

    date_array.each do |date|
      info.each do |n|
        coutnry = n[0]
        aircode = n[1]
        hotel = n[3]

        airport_send = {
          "airportCode": airport['airportCode'],
          "airportHotWeight": airport['airportHotWeight'],
          "airportId":airport['airportId'],
          "airportLocation":airport['airportLocation'],
          "airportName": airport['airportName'],
          "bannerSwitch":airport['bannerSwitch'],
          "isHotAirport":airport['isHotAirport'],
          "landingVisaSwitch": airport['landingVisaSwitch'],
          "cityId":airport['cityId'],
          "location":airport['cityLocation']}

        #pickup task
        transfer_res = {
          "airportCode"=> airport['airportCode'],
          "endLocation" => airport['airportLocation'],
          "startLocation" => "#{house['result']['placeLat']},#{house['result']['placeLng']}",
          "serviceDate" => "#{date.to_s} 08:00:00", 
            # 修正格式
            "startDate" => date.to_s,
            "startTime" => "08:00",
            "flightInfo" => {"is_custom":1},
            "airportInfo" => airport_send,
            "transferAddress" => house['result'],
        }

        send << transfer_res 
      end
    end
    File.open('/tmp/transfer.json', 'w+') {|f| f.write(send.to_json)}
  end

end
