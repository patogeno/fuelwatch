#from django.http import HttpResponse
from django.shortcuts import render
from fuelwatch.main import getStations

def index(request):
    return render(request, 'index.html', {
        'suburb': 'Como',
        'stations': getStations('Como'),
    })