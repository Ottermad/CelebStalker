from app.travel.functions import cheapest_flight, lltocode, distance, cost, nearest_airport 

import json


origin = '45.501689,-73.567256'
destination = '43.653226,-79.383184'

date = '2015-07-31'
adults = '1'

f = open('/home/cthomas/CelebStalker/app/travel/airports.json', 'r')
airport_data = json.loads(f.read())
f.close()
origin_airport = nearest_airport(origin.split(','))
origin_code = lltocode([origin_airport['location']['lat'], origin_airport['location']['lng']], airport_data)
  
destination_airport = nearest_airport(destination.split(','))
dest_code  = lltocode([destination_airport['location']['lat'], destination_airport['location']['lng']], airport_data)

cheapest = cheapest_flight(origin_code, dest_code, date=date, passengers={'adult': int(adults), 'child': 0, 'senior': 0})
print(cheapest)
