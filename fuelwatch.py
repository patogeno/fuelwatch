from flask import Flask, escape, request, render_template
from services.stations import getStations
#from modules.views import createHeader, createBody, createFooter, stationsTable

app = Flask(__name__)

@app.route('/')
def main():
    stations = getStations('Como')
    return render_template('index.html', stations=stations, suburb='Como')
    #page = createHeader('Fuel Prices','style.css') + createBody(stationsTable(stations)) + createFooter()
    #return page

if __name__ == "__main__":
    app.run()