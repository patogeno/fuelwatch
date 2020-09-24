import requests
import feedparser
#from pprint import pprint

def addDayToStations(stations, day):
        for station in stations:
            station.update(day=day)

def by_price(item):
    return float(item['price'])

def getStations(suburb, product=1):
    # --- Requests ---
    req_today = requests.get(f'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb={suburb}&Day=today&Product={product}')
    req_tomorrow = requests.get(f'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb={suburb}&Day=tomorrow&Product={product}')
    req_yesterday = requests.get(f'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb={suburb}&Day=yesterday&Product={product}')

    # --- Format, Merge and Sort Records ---
    stations_today = feedparser.parse(req_today.content)['entries']
    stations_tomorrow = feedparser.parse(req_tomorrow.content)['entries']
    stations_yesterday = feedparser.parse(req_yesterday.content)['entries']
    addDayToStations(stations_today, "today")
    addDayToStations(stations_tomorrow, "tomorrow")
    addDayToStations(stations_yesterday, "yesterday")
    stations = stations_tomorrow + stations_today + stations_yesterday
    stations = sorted(stations, key=by_price)

    return stations
