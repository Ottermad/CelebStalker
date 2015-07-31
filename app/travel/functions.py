import requests
from .google_flights import flights_request
from .config import GOOGLE_API_KEY, FOURSQUARE_CLIENT_ID, FOURSQUARE_CLIENT_SECRET, FOURSQUARE_VERSION, FOURSQUARE_AIRPORT_ID
import json

def distance(origin, dest):
    payload = {}
    payload["key"] = GOOGLE_API_KEY 
    payload["destinations"] = dest[0] + ',' + dest[1]
    payload["origins"] = origin[0] + ',' + origin[1]
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=payload)
    data = r.json()
    print(r.url)
    miles = data['rows'][0]['elements'][0]['distance']['value'] / 1600.0
    return miles

def distance_walk(origin, dest):
    payload = {}
    payload["key"] = GOOGLE_API_KEY 
    payload["destinations"] = dest[0] + ',' + dest[1]
    payload["origins"] = origin[0] + ',' + origin[1]
    payload['mode'] = 'walking'
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=payload)
    data = r.json()
    print(data)
    miles = data['rows'][0]['elements'][0]['distance']['value'] / 1600.0
    return miles


def cost(mpg, miles):
    gallons = miles / mpg
    pounds = gallons * 4.996
    return pounds


def nearest_airport(location):
    airports_data = get_airports(location)
    airport = filter_airports(airports_data)
    return airport


def get_airports(location):
    payload = {}
    payload['v'] = FOURSQUARE_VERSION
    payload['client_id'] = FOURSQUARE_CLIENT_ID
    payload['client_secret'] = FOURSQUARE_CLIENT_SECRET
    payload['categoryId'] = FOURSQUARE_AIRPORT_ID 
    payload['ll'] = ",".join(location)
    r = requests.get('https://api.foursquare.com/v2/venues/search', params=payload)
    return r.json()


def filter_airports(data):
    venues = data['response']['venues']
    correct = None
    distance = 1000000
    for venue in venues:
        categories = venue['categories']
        short_name = categories[0]['shortName']
        venue_distance = venue['location']['distance']
        if short_name == 'Airport' and venue_distance < distance:
            correct = venue
    return correct


def lltocode(location, airport_data):
    code = None
    for airport in airport_data:
        if 'lat' not in airport.keys() or 'lon' not in airport.keys():
            continue
        if is_close(location, (airport['lat'], airport['lon'])):
            code = airport['iata']
            break
    return code 


def is_close(location1, location2):
    lat_is_close = False
    lng_is_close = False
    location1 = [float(x) for x in location1]
    location2 = [float(x) for x in location2]
    if abs(location1[0] - location2[0]) < 0.4:
        lat_is_close = True
    if abs(location1[1] - location2[1]) < 0.4:
        lng_is_close = True
    return lat_is_close and lng_is_close


def cheapest_flight(start, end, passengers, date):
    data = flights_request.format(
        passengers['adult'],
        passengers['child'],
        passengers['senior'],
        start,
    	end,
    	date,
    	'GB'
    )
    payload = {}
    payload["key"] = GOOGLE_API_KEY
    headers = {'Content-Type': 'application/json'}
    r = requests.post("https://www.googleapis.com/qpxExpress/v1/trips/search", data=data, params=payload, headers=headers)
    print(r.status_code)
    json_data = r.json()
    print(json_data)
    price = json_data['trips']['tripOption'][0]['saleTotal']
    resp = {
        'price': price,
        'origin': start,
        'destination': end
    }
    return json.dumps(resp)
