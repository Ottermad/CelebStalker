from app.travel.functions import cheapest_flight

passengers = {}

passengers['adult'] = 1
passengers['child'] = 0
passengers['senior'] = 0

x = cheapest_flight('LHR', 'JFK', passengers, '2015-07-29')
print(x)
