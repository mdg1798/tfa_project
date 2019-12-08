from django.contrib import admin
from .models import Squirrel

class IncidencesAdmin(admin.ModelAdmin):
    list_display=('Unique_Squirrel_ID')

admin.site.register(Squirrel)

# Register your models here.
