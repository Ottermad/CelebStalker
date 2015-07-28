from app.ticketmaster.functions import *

d = search_attraction("tomas", "sweden")

ids = [str(attraction['id']) for attraction in d['attractions']]

get_events(ids, "sweden")
