from flask import Flask, render_template, request, url_for, redirect

import requests

app = Flask(__name__)

base_url = 'http://127.0.0.1:5000/'

@app.route('/travel/<origin>/<destination>/<date>')
def travel(origin, destination, date):
	return render_template('travel.html')


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


@app.route('/hotels')
def hotels():
	return render_template('hotels.html')


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