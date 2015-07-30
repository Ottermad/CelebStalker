from flask import Blueprint, jsonify

from .functions import closest_hotel

import json

hotels_b = Blueprint('hotels', __name__, url_prefix='/hotels')

@hotels_b.route('/<location>')
def hotels(location):
    location = location.split(",")
    return jsonify({'response': closest_hotel(location)})
