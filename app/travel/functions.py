import requests

def distance(origin, dest):
    payload = {}
    payload["key"] = 'AIzaSyCDNXGrIwOa4SZXNoa6TszRi9ot9-8Cyc4'
    payload["destinations"] = ",".join(dest)
    payload["origins"] = ",".join(origin)
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=payload)
    data = r.json()
    miles = data['rows']['elements']['distance']['value'] / 1600.0
    return miles


def cost(mpg, miles):
    gallons = mpg / miles
    pounds = gallons / 4.996
    return pounds


def nearest_airport(location):
    payload = {}
    payload['v'] = '20130815'
    payload['client_id'] ='0NXAHOK0SKFLWOKWYHD23HX55SPWPI2QU2ACPNGAGQTQ12IP'
    payload['client_secret'] = '0VPTQABEQK4CK2E41QYD1JXDGCESBJ4ZZSRD03BF3LJ1C40O'
    payload['categoryId'] = '4bf58dd8d48988d1ed931735'
    payload['ll'] = ",".join(location)
    #payload['query'] = "Airport"
    #payload['intent'] = 'checkin'



    r = requests.get('https://api.foursquare.com/v2/venues/search', params=payload)
    return r.text

def cheapest_flight(start, end):
    pass

def get_airports(location):
    payload = {}
    payload['v'] = '20130815'
    payload['client_id'] ='0NXAHOK0SKFLWOKWYHD23HX55SPWPI2QU2ACPNGAGQTQ12IP'
    payload['client_secret'] = '0VPTQABEQK4CK2E41QYD1JXDGCESBJ4ZZSRD03BF3LJ1C40O'
    payload['categoryId'] = '4bf58dd8d48988d1ed931735'
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