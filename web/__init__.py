from flask import Flask, render_template

app = Flask(__name__)

@app.route('/travel')
def travel():
	return render_template('travel.html')


@app.route('/events')
def events():
	return render_template('events.html')


@app.route('/hotels')
def hotels():
	return render_template('hotels.html')


@app.route('/')
def home():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(port=8080, debug=True)