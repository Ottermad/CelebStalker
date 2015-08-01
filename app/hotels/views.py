from flask import Blueprint, jsonify

from .functions import closest_hotel

import json

hotels_b = Blueprint('hotels', __name__, url_prefix='/hotels')

@hotels_b.route('/<location>')
def hotels(location):
    location = location.split(",")
    closest = closest_hotel(location)
    new_data = {
    	'longitude': closest['Longitude'],
    	'latitude': closest['Latitude'],
    	'name': closest['HotelName'],
    	'price': closest['MaxPrice'],
    	'image': closest['HotelImage']
    }
    return jsonify(new_data)