from django.db import models
from django.utils.translation import gettext as _


class Incidences(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    def __str__(self):
        return self.name

