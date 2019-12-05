from django.core.management.base import BaseCommand
import csv
from st.models import Squirrel

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args , **kwargs):
        path=kwargs['path']
        with open(path,'r') as data_file:  
            data = csv.reader(data_file)
            for i in data:  
                a = i[0]
                b = i[1]
                c = i[2]
                d = i[4]
                e = i[5][4:]+'/'+i[5][:2]+'/'+i[5][2:4]
                f = i[7]
                g = i[8]
                h = i[12]
                i = i[14]
                j = i[15]
                k = i[16]
                l = i[17]
                m = i[18]
                n = i[19]
                o = i[20]
                p = i[21]
                q = i[22] 
                r = i[23]
                s = i[24]
                t = i[25]
                u = i[26]
                v = i[27]
                w = i[28]
                try:
                    s,c = Squirrel.objects.get_or_create(
                        Longitude = a,
                        Latitude = b,
                        Unique_Squirrel_ID = c,
                        Shift = d,
                        Date =e,
                        Age =f,
                        Primary_Fur_Color=g,
                        Location =h,
                        Specific_location=i,
                        Running = j,
                        Chasing = k,
                        Climbing = l,
                        Eating = m,
                        Foraging = n,
                        Other_Activities = o,
                        Kuks = p,
                        Quaas = q,
                        Moans = r,
                        Tail_flags = s,
                        Tail_twitches = t,
                        Approaches = u,
                        Indifferent = v,
                        Runs_from = w,
                        )
                    if created:
                        squirrel.save()
                            
                except Exception as ex:
                    print("Exception occured")

