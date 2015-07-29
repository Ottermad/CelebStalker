from flask import Flask
from app.ticketmaster.views import ticketmaster
from app.travel.views import travel

app = Flask(__name__)
app.config['DEBUG'] = True
app.register_blueprint(ticketmaster)
app.register_blueprint(travel)
