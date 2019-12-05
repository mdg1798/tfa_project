import os
import csv

from django.core.management.base import BaseCommand, CommandError
from st.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')
    def handle(self, *args, **kwargs):
        csvPath =kwargs['path']
        if not os.path.exists(csvPath):
            raise CommandError("%s doesnt exists." %csvPath)
        model_fields=[f.name for f in Squirrel._meta.fields]
        read= csv.reader(open(csvPath))
        fields_name=next(read)
        with open (csvPath, 'rb') as csvFile:
            reader=csv.reader(csvFile, delimiter=',', quotechar="\"")
            
            for i, _ in enumerate(fields_name):
                    fields_name[i]=fields_name[i]
                    fields_name[i]=fields_name[i].replace(' ','_')
                    if not fields_name[i] in model_fields:
                        print("%s field doesnt exists in Squirrel model, hence continuing.\n" %(fields_name[i]))
                        continue
            for row in read:
                #try:
                obj= Squirrel()
                for i, field in enumerate(row):
                         if field=='Date':
                             field= field[4:]+'-'+field[:2]+'-'+field[2:4]
                         setattr(obj, fields_name[i], field)
                obj.save()
                # except Exception:
                #     raise CommandError("Nothing Happening")








