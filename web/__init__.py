from flask import Flask, render_template, request, url_for, redirect

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adinpwbfweuiebNFIUpwbfuiew'

base_url = 'http://127.0.0.1:5000/'

@app.route('/travel/<origin>/<destination>/<date>')
def travel(origin, destination, date):
    car = requests.get(base_url + 'travel/car/' + origin + '/' + destination + '/' + '30')
    car_data = car.json()
    date = date[:10]
    print(date)
    plane = requests.get(base_url + 'travel/plane/' + origin + '/' + destination + '/' + date  + '/1')
    plane_data = plane.json()
    print(plane_data)
    return render_template('travel.html', car=car_data, airport=plane_data)


@app.route('/events/<celeb>/<origin>')
def events(celeb, origin):
    r = requests.get(base_url + 'events/search/' + celeb)
    json_data = r.json()
    # id, date, maxprice currency, name
    data = []
    print(json_data)
    for event in json_data['events']:
        e_data = {}
        e_data['id'] = event['id']
        e_data['date'] = event['localeventdate']
        e_data['name'] = event['name']
        e_data['price'] = event['price_ranges']['including_ticket_fees']['max']
        e_data['lat'] = str(event['venue']['location']['address']['lat'])
        e_data['long'] = str(event['venue']['location']['address']['long'])
        data.append(e_data)
    return render_template('events.html', events=data, origin=origin)


@app.route('/hotels/<destination>')
def hotels(destination):
    r = requests.get(base_url + 'hotels/' + destination)
    hotels = [r.json()]
    print(hotels)
    return render_template('hotels.html', hotels=hotels)


@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        celeb = request.form['searchText']
        origin = request.form['lat'] + r',' + request.form['long']
        print(origin)
        return redirect(url_for('events', celeb=celeb, origin=origin))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
