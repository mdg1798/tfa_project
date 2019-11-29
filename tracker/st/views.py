from django.shortcuts import render
from django.http import HttpResponse

from .models import Squirrel

def index(request):
        s=Squirrel.objects.all()
        return render(request, 'squirrel/map.html')

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
        
def map_view(request, *args,**kwargs):
    return render(request,"maps1.html",{})

def sightings_view(request, *args,**kwargs):
    return render(request,"sightings.html",{})

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})
