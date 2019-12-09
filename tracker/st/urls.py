from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
            path('admin/', admin.site.urls),
            path('map', views.get_map),
            path('sightings/', views.list_sightings),
            path('sightings/add',views.add),
            path('sightings/stats/',views.general_state),
            path('sightings/<unique_squirrel_id>/',views.update),
            path('', views.index),
            ]
