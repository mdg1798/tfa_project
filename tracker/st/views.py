from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Squirrel

def map_view(request):
    s_list=Squirrel.objects.all()[0:100]
    l=[{"Longitude": float(i.Longitude), "Latitude": float(i.Latitude)} for i in s_list]
    context={'s_list': json.dumps(l)}

    return render(request, "maps1.html", context)

def home_view(request, *args,**kwargs):
    return render(request,"home.html",{})
        
#def map_view(request, *args,**kwargs):
#    queryset=Squirrel.objects.all()
#    context={
#            'sightings':queryset
#            }
#    return render(request,"maps1.html",context)

def sightings_view(request, *args,**kwargs):
    return render(request,"sightings.html",{})

def add_view(request, *args,**kwargs):
    return render(request,"add.html",{})
