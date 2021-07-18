from flask import Flask, render_template
from pymongo import MongoClient
from flask_cors import CORS
from view import reservation

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'salad reservation system secret key'

app.register_blueprint(reservation.bp_salad, url_prefix='/salad')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)