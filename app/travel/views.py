from flask import Blueprint, jsonify
from .functions import cheapest_flight, lltocode, distance, cost, nearest_airport 

import json

travel = Blueprint('travel', __name__, url_prefix='/travel')


@travel.route('/car/<origin>/<destination>/<mpg>')
def car(origin, destination, mpg):
    miles = distance(origin.split(","), destination.split(','))
    pounds = cost(miles=miles,mpg=float(mpg))
    resp = {
        'origin': origin,
        'destination': destination,
        'mpg': mpg,
        'distance': miles,
        'cost': pounds
    } 
    return jsonify(resp)

@travel.route('/plane/<origin>/<destination>/<date>/<adults>')
def plane(origin, destination, date, adults):
    f = open('/home/cthomas/CelebStalker/app/travel/airports.json', 'r')
    airport_data = json.loads(f.read())
    f.close()
    origin_airport = nearest_airport(origin.split(','))
    origin_code = lltocode([origin_airport['location']['lat'], origin_airport['location']['lng']], airport_data)
    
    destination_airport = nearest_airport(destination.split(','))
    dest_code  = lltocode([destination_airport['location']['lat'], destination_airport['location']['lng']], airport_data)

    return origin_code + dest_code
