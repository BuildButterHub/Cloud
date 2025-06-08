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

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    city = city.lower()
    if city not in cities:
        return jsonify({'error': 'City not found'}), 404

    latitude = cities[city]['latitude']
    longitude = cities[city]['longitude']
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

    response = requests.get(url)
    data = response.json()

    if 'current_weather' not in data:
        return jsonify({'error': 'Weather data not available'}), 500

    temperature = data['current_weather']['temperature']

    return jsonify({'city': city, 'temperature_celsius': temperature})

if __name__ == '__main__':
    app.run(debug=True)
