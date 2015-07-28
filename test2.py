from app.travel.functions import nearest_airport, filter_airports, get_airports

data = get_airports(('51.507351', '-0.127758'))

filtered = filter_airports(data)

print(filtered)