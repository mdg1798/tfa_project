from django.contrib import admin
from .models import Squirrel

class IncidencesAdmin(admin.ModelAdmin):
    list_display=('latitude','longitude')

admin.site.register(Squirrel, IncidencesAdmin)

# Register your models here.
