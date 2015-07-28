from flask import Flask
from app.ticketmaster.views import ticketmaster

app = Flask(__name__)
app.config['DEBUG'] = True
app.register_blueprint(ticketmaster)
