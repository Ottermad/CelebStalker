from flask import Flask, render_template, request, url_for, redirect

import requests

app = Flask(__name__)

base_url = 'http://6a8fd9ce.ngrok.com/'

@app.route('/travel')
def travel():
	return render_template('travel.html')


@app.route('/events/<celeb>')
def events(celeb):
	r = requests.get(base_url + 'events/search/' + celeb)
	json_data = r.json()
	# id, date, maxprice currency, name
	data = []
	for event in json_data['events']:
		e_data = {}
		e_data['id'] = event['id']
		e_data['date'] = event['localeventdate']
		e_data['name'] = event['name']
		e_data['price'] = event['price_ranges']['including_ticket_fees']['max']
		data.append(e_data)
	return render_template('events.html', events=data)


@app.route('/hotels')
def hotels():
	return render_template('hotels.html')


@app.route('/', methods=('GET', 'POST'))
def home():
	if request.method == 'POST':
		celeb = request.form['searchText']
		return redirect(url_for('events', celeb=celeb))
	return render_template('index.html')

if __name__ == '__main__':
	app.run(port=8080, debug=True)