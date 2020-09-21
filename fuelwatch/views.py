#from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #num = 1
    #return HttpResponse('<p>My favourite number is {}</p>'.format(num))
    return render(request, 'index.html', {
        'num': 123,
    })