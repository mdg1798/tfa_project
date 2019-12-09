from django.shortcuts import render,get_object_or_404,HttpResponse,redirect
from .models import Squirrel
from django.http import HttpResponse
from .forms import SquirrelForm
import random
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

def index(request):
    return HttpResponse("Welcome to our Squirrel Tracker App !")
def general_state(request):
    s=Squirrel.objects.all()
    title='general state'
    context={
            'title':title,
            's':s,
            }
    return render(request,'stat.html',context)

def list_sightings(request):
    squirrel=Squirrel.objects.all()
    link_list=[]
    for s in squirrel:
        link_list.append(s.Unique_Squirrel_ID)
    title='list of sightings'
    context={
            'title':title,
            'link_list':link_list,
            }
    return render(request,'sightings.html',context)

def get_map(request):
    squirrel=Squirrel.objects.all()
    myitems=[]
    for i in range(100):
        j=random.randint(0,len(squirrel))
        item=list(squirrel)[j]
        item_list=[float(item.Longitude),float(item.Latitude)]
        myitems.append(item_list)
    title='squirrel map'
    context={
            'title':title,
            'myItems':myitems,
            }
    return render(request,'map.html',context)

def add(request):
    if request.method == 'POST':
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'update')
    else:
        form = SquirrelForm()
    title='add new squirrel'
    context={
            'form':form,
            'title':title
            }
    return render(request,'add.html',context)

def update(request,unique_squirrel_id):
    to_update=Squirrel.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    print(to_update)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=to_update)
        print(form)
        if form.is_valid():
            to_update=form.save()
            to_update.save()
            messages.success(request,'Now you can update this squirrel')
            return redirect(f'sightings')
    else:
        form = SquirrelForm(instance=to_update)

    context={
            'form':form,
            }
    return render(request,'update.html',context)

#Create your views here.
