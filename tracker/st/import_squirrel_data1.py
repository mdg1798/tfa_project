import os
import csv

from django.core.management/base import BaseCommad, CommandError
from django.db.models.loading import get_model

class Command(BaseCommand):
    args = 'data.csv'
    def handle(self, *args, **options):
        model, _= os.path.splitext(os.path.basename(csvPath))
        Model =get_model("Squirrel",model.title())
        moel_fields=[f.name for f in Model._meta.fields]
        fields_name=[]
        with open (csvPath, 'rb') as csvFile:
            reader=csv.reader(csvFile, delimeter=',', quotechar="\"")
            fields_name=reader.next()
            for i, _ in enumerate(fields_name):
                fields_name[i]=fields_name[i].lower()
                fields_name[i]=fields_name[i].replace(' ','_')
                if not fields_name[i] in model_fields:
                    raise CommandError ("%s field doesnt exists in %s Model" %(fields_name[i], Model))
             for row in reader:
                 try:
                     obj=Model()
                     for i, field in enumerate(row):
                         setattr(obj, fields_name[i], field)
                     obj.save()
                 except Exception,e:
                     raise CommandError(e)








