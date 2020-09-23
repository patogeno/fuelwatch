from flask import Flask, escape, request, render_template
from services.stations import getStations
import json
import random

app = Flask(__name__)
with open('server_assets/australian_postcodes.json') as f:
    suburbs = json.load(f)

# Filter to leave only WA suburbs
suburbs = [s for s in suburbs if s['state'] == 'WA']

@app.route('/')
def main():
    suburb = random.choice(suburbs)
    subname = escape(suburb['locality']).capitalize()
    stations = getStations(subname)
    return render_template('index.html', stations=stations, suburb=subname)

@app.route('/<suburb>')
def per_suburb(suburb):
    sub = escape(suburb).capitalize()
    stations = getStations(sub)
    return render_template('index.html', stations=stations, suburb=sub)

if __name__ == "__main__":
    app.run()