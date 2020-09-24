from flask import Flask, escape, request, render_template
from services.stations import getStations
import random

app = Flask(__name__)
# Read suburbs from file
with open('server_assets/suburbs.txt') as f:
    suburbs = f.readlines()

# Trim, Capitalize and Escape each suburb
suburbs = [escape(s.rstrip().capitalize()) for s in suburbs]

# List of Products
products = [
    {'id': 1, 'name': 'Unleaded Petrol'},
    {'id': 2, 'name': 'Premium Unleaded'},
    {'id': 4, 'name': 'Diesel'},
    {'id': 5, 'name': 'LPG'},
    {'id': 6, 'name': '98 RON'},
    {'id': 10, 'name': 'E85'},
    {'id': 11, 'name': 'Brand diesel'}
]

@app.route('/')
def main():
    suburb = random.choice(suburbs)
    stations = getStations(suburb)
    print(stations[0])
    return render_template('index.html', stations=stations, suburb=suburb, suburbs=suburbs, product=1, products=products)

@app.route('/<suburb>/<int:productid>')
def per_suburb(suburb, productid):
    sub = escape(suburb).capitalize()
    stations = getStations(sub,productid)
    return render_template('index.html', stations=stations, suburb=sub, suburbs=suburbs, productId=productid, products=products)

if __name__ == "__main__":
    app.run(debug=True)