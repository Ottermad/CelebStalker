from app.ticketmaster.functions import *
import json

d = search_attraction("taylor")

ids = [str(attraction['id']) for attraction in d['attractions']]

events = get_events(ids)

dest = [events['events'][0]['venue']['location']['address']['lat'],events['events'][0]['venue']['location']['address']['long']]
dest = [str(d) for d in dest]
origin = ['45.501689', '-73.567256']


print(distance(origin, dest))