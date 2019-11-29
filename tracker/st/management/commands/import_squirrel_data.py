import csv
import os
from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from st.models import Question
class Command(BaseCommand):
        help = "Insert Upazila office reports from a CSV file. " \
                           "CSV file name(s) should be passed. " \
                                      "If no optional argument (e.g.: --acland) is passed, " \
                                                 "this command will insert UNO office reports."

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.model_name = Question

        def insert_upazila_report_to_db(self, data):
            try:
                self.model_name.objects.create(
                upazila=data["X"],
                rank=data["Y"] 
                )
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
                                     upazila_name = words[0]
                                     rank = words[1]
                                     data= {}
                                     data["upazila"] = upazila_name
                                     data["rank"] = rank
                                     self.insert_upazila_report_to_db(data)
                                     self.stdout.write(
                                            self.style.SUCCESS('{}_{}: {}'.format(upazila_name,rank))
                                                )
                    except FileNotFoundError:
                             raise CommandError("File {} does not exist".format( file_path))
