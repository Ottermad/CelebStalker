from app.travel.functions import nearest_airport, filter_airports, get_airports, is_close, lltocode

import json

data = get_airports(('51.507351', '-0.127758'))

filtered = filter_airports(data)

f = open('/home/cthomas/CelebStalker/app/travel/airports.json', 'r')
airport_data = json.loads(f.read())
f.close()

loc = (
	filtered['location']['lat'],
	filtered['location']['lng']
)

print(lltocode(loc, airport_data))