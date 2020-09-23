from flask import Flask, escape, request, render_template
from services.stations import getStations
#from modules.views import createHeader, createBody, createFooter, stationsTable

app = Flask(__name__)

@app.route('/')
def main():
    stations = getStations('como')
    return render_template('index.html', stations=stations, suburb='Como')

@app.route('/<suburb>')
def per_suburb(suburb):
    sub = escape(suburb).capitalize()
    stations = getStations(sub)
    return render_template('index.html', stations=stations, suburb=sub)

if __name__ == "__main__":
    app.run()