from flask import Flask, escape, request, render_template
from services.stations import getStations
import random

app = Flask(__name__)
# Read suburbs from file
with open('server_assets/suburbs.txt') as f:
    suburbs = f.readlines()

# Trim, Capitalize and Escape each suburb
suburbs = [escape(s.rstrip().capitalize()) for s in suburbs]

@app.route('/')
def main():
    suburb = random.choice(suburbs)
    stations = getStations(suburb)
    return render_template('index.html', stations=stations, suburb=suburb, suburbs=suburbs)

@app.route('/<suburb>')
def per_suburb(suburb):
    sub = escape(suburb).capitalize()
    stations = getStations(sub)
    return render_template('index.html', stations=stations, suburb=sub, suburbs=suburbs)

if __name__ == "__main__":
    app.run()