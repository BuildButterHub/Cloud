from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Координаты для городов
cities = {
    'new_york': {'latitude': 40.7128, 'longitude': -74.0060},
    'california': {'latitude': 36.7783, 'longitude': -119.4179},
    'texas': {'latitude': 31.9686, 'longitude': -99.9018},
    'chicago': {'latitude': 41.8781, 'longitude': -87.6298},
}
