from django.shortcuts import render,get_
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

def update(request,unique_squirrel_id):
    upd=Squirrel.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    print(upd,": Updating the Squirrel")
    if request.method=='POST':
        form =SquirrelForm(request.POST, instance=upd)
        print(form)
        if form.is_valid():
            upd=form.save()
            upd.save()
            message.success(request,"Now Updating the Squirrel")
            return redirect(f'/st/sightings')
        else:
            form=SquirrelForm(instance=to_update)
        context={
                'form':form,
                }
        return render(request,'st/update.html',context)
        

