from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    Longitude = models.FloatField(
    help_text=_('Enter the Longitude'),
    )

    Latitude = models.FloatField(
    help_text=_('Enter the Latitude'),
    )   
    
    Unique_Squirrel_ID = models.CharField(
    max_length=60, 
    help_text=_('Unique ID of squirrel'), 
    )
    
    PM='PM'
    AM='AM'

    Shift_Choices=( (PM,'PM'),
    (AM,'AM'),
     )

    Shift = models.CharField(
    max_length=2,
    choices=Shift_Choices,
    )


    Date = models.DateField(
    help_text=_('Date of squirrel'),
    )

    Adult='Adult'
    Juvenile='Juvenile'
    Other='Other'

    Age_Choices=( (Adult,'Adult'), 
    (Juvenile,'Juvenile'),
    (Other,'Other')
     )  

    Age = models.CharField( 
    max_length=20, 
    choices=Age_Choices,  
    default=Other,
    help_text=_('Age of Squirrel'),
    )

    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    Other='Other'

    Primary_Fur_Color_Choices=( (Gray,'Gray'),
    (Cinnamon,'Cinnamon'),
    (Black,'Black'),
    (Other,'Other')
    )

    Primary_Fur_Color = models.CharField(
    max_length=100,
    choices=Primary_Fur_Color_Choices,
    default=Other,
    )

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'

    Location_Choices=( (Ground_Plane,'Ground_Plane'), 
    (Above_Ground,'Above_Ground'),
    (Other,'Other')
     )  

    Location = models.CharField( 
    max_length=100, 
    choices=Location_Choices,  
    default=Other,
    help_text=_('Locations of the squirrel'),
    )

    Specific_Location= models.CharField(
    max_length=100,
    help_text=_('Specific Locations of Squirrel'),
    )

    Running = models.BooleanField(default=False)
    Chasing = models.BooleanField(default=False)
    Climbing = models.BooleanField(default=False)
    Eating = models.BooleanField(default=False)
    Foraging = models.BooleanField(default=False)

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('Other activities'),
            )

    Kuks = models.BooleanField(default=False)
    Quaas= models.BooleanField(default=False)
    Moans =models.BooleanField(default=False)
    Tail_flags =models.BooleanField(default=False)
    Tail_twitches =models.BooleanField(default=False)
    Approaches=models.BooleanField(default=False)
    Indifferent =models.BooleanField(default=False)
    Runs_from =models.BooleanField(default=False)
