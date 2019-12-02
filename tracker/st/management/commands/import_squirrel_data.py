from django.core.management.base import BaseCommand
import csv
from st.models import Squirrel

class Command(BaseCommand):
    def import_squirrel_data(self,path):
        with open(path,'r') as data_file:  
            data = csv.reader(data_file)
            for data_object in data:                
                Chasing = data_object[16]
                Climbing = data_object[17]
                Eating = data_object[18]
                Foraging = data_object[19]
                Other_Activities = data_object[20]
                Kuks = data_object[21]
                Quaas = data_object[22] 
                Moans = data_object[23]
                Tail_flags = data_object[24]
                Tail_twitches = data_object[25]
                Approaches = data_object[26]
                Indifferent = data_object[27]
                Runs_from = data_object[28]
                try:
                    squirrel, created = Squirrel.objects.get_or_create(
                        Running = Running,
                        Chasing = Chasing,
                        Climbing = Climbing,
                        Eating = Eating,
                        Foraging = Foraging,
                        Other_Activities = Other_Activities,
                        Kuks = Kuks,
                        Quaas = Quaas,
                        Moans = Moans,
                        Tail_flags = Tail_flags,
                        Tail_twitches = Tail_twitches,
                        Approaches = Approaches,
                        Indifferent = Indifferent,
                        Runs_from = Runs_from,
                        )
                    if created:
                        squirrel.save()
                            
                except Exception as ex:
                    pass

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **kwargs):
        """
        Call the function to import data
        """
        path = kwargs['path']
