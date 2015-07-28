from .config import TICKETMASTER_API

import requests
import json



def search_attraction(name, domain="canada"):
    payload = {}
    payload["apikey"] = TICKETMASTER_API
    payload["domain_ids"] = domain
    payload["attraction_name"] = name
    headers = {'Accept': 'application/json'}
    r = requests.get("https://app.ticketmaster.eu/mfxapi/v1/attractions/suggestions", params=payload, headers=headers)
    data = json.loads(r.text)
    return data

def get_events(attraction_ids, domain="canada"):
    payload = {}
    payload["apikey"] = TICKETMASTER_API
    payload["domain_ids"] = domain
    payload["attraction_ids"] = ",".join(attraction_ids)
    headers = {'Accept': 'application/json'}
    r = requests.get("https://app.ticketmaster.eu/mfxapi/v1/events", params=payload, headers=headers)
    return r.json()
