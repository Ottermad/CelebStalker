from flask import Flask, render_template, request, url_for, redirect, session

import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adinpwbfweuiewadawadadwabNFIUpwbfuiew'

base_url = 'http://127.0.0.1:5000/'


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        celeb = request.form['searchText']
        origin = request.form['lat'] + r',' + request.form['long']
        session['query'] = {'celeb': celeb, 'origin': origin}
        return redirect(url_for('events', celeb=celeb, origin=origin))
    return render_template('index.html')


@app.route('/events', methods=('GET', 'POST'))
def events():
    if request.method == "POST":
        session['query']['date'] = request.form['date']
        session['query']['destination'] = request.form['destination']
        return redirect(url_for('travel'))
    else:
        r = requests.get(base_url + 'events/search/' + session['query']['celeb'])
        print(r.url)
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
        return render_template('events.html', events=data)


@app.route('/travel', methods=('GET', 'POST'))
def travel():
    if request.method == 'POST':
        session['query']['mode'] = request.form['mode']
        session['query']['travelCost'] = request.form['cost']
        return redirect(url_for('hotels'))
    origin = session['query']['origin']
    destination = session['query']['destination']
    date = session['query']['date']
    try:
        car = requests.get(base_url + 'travel/car/' + origin + '/' + destination + '/' + '30')
        car_data = car.json()
    except:
        car_data = False
    try:
        date = date[:10]
        print(date)
        plane = requests.get(base_url + 'travel/plane/' + origin + '/' + destination + '/' + date  + '/1')
        plane_data = plane.json()
        print(plane_data)
    except:
        plane_data = False
    return render_template('travel.html', car=car_data, airport=plane_data)


@app.route('/hotels', methods=('GET', 'POST'))
def hotels():
    if request.method == "POST":
        session['query']['hotel'] = request.form['hotel']
        session['query']['hotelPrice'] = request.form['price']
        return redirect(url_for('checkout'))
    destination = session['query']['destination']   
    print(destination)
    r = requests.get(base_url + 'hotels/' + destination)
    print(r.url)
    hotels = [r.json()]
    print(hotels)
    print(session['query'])
    return render_template('hotels.html', hotels=hotels)


@app.route('/checkout')
def checkout():
    return render_template("checkout.html")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
