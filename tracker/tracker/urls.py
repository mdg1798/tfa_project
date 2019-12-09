"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from st import views

urlpatterns = [
    path('map/', views.get_map),
    path('sightings/', views.list_sightings),
    path('sightings/add/',views.add),
    path('sightings/stats/',views.general_state),
    path('sightings/<unique_squirrel_id>/',views.update),
    path('',views.index),
    path('admin/', admin.site.urls),
]
