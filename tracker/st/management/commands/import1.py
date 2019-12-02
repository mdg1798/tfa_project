import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from st.models import Squirrel
class Command(BaseCommand):

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.model_name = Squirrel

        def insert_upazila_report_to_db(self, data):
            try:
                latitude=data
            except Exception as e:
                raise CommandError("Error in inserting {}: {}".format(self.model_name, str(e)))
        def get_current_app_path(self):
                return apps.get_app_config('st').path

        def get_csv_file(self, filename):
                 app_path = self.get_current_app_path()
                 file_path = os.path.join(app_path, "management", "commands", filename)
                 return file_path
        def add_arguments(self, parser):
                    parser.add_argument('filenames',nargs='+',type=str,help="Inserts Upazila Office reports from CSV file")
        def handle(self, *args, **options):
            for filename in options['filenames']:
                    self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
                    file_path = self.get_csv_file(filename)
                    try:
                        with open(file_path) as csv_file:
                             csv_reader = csv.reader(csv_file, delimiter=',')
                             for row in csv_reader:
                                if row != "":
                                     words = [word.strip() for word in row]
                                     data1= {}
                                     data1["Lat/Long"] = words[0]
                                     self.insert_upazila_report_to_db(data1)

                    except FileNotFoundError:
                             raise CommandError("File {} does not exist".format( file_path))
