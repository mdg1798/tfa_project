from django.core.management.base import BaseCommand,CommandError
from .models import Squirrel
import csv
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_arguments('args')

    def handle(self, *args, **options):
        path=''.join(list(args))
        meta=Squirrel._meta
        field_names=[field.name for field in meta.fields]
        with open(path,'w') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(field_names)
            for obj in Squirrel.objects.all():
                row=writer.writerow([getattr(obj,field) for field in field_names])
