import requests
import json

payload = {}

payload["apikey"]= "GxIw3zDAjYxxqzA3aPCtRfJ7bSYSTrKR"
payload["domain_ids"] = "sweden"
payload["attraction_name"] = "twenty"

headers = {'Accept': 'application/json'}

r = requests.get("https://app.ticketmaster.eu/mfxapi/v1/attractions", params=payload, headers=headers)

data = json.loads(r.text)

print(data)