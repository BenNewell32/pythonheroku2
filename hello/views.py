from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
import os


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # times = int(os.environ.get('TIMES',5))
    # return HttpResponse('Hello' * times)
    return render(request, "index.html")



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
