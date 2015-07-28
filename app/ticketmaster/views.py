from flask import Blueprint, jsonify

from .functions import search_attraction, get_events

ticketmaster = Blueprint('ticketmaster', __name__, url_prefix='/events')


@ticketmaster.route('/search/<name>')
def search(name):
    data = search_attraction(name)
    ids = [str(person['id']) for person in data['attractions']]
    events = get_events(ids)
    return jsonify(events)
