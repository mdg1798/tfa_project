from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    Longitude = models.FloatField(
    help_text=_('Longitude'),
    )

    Latitude = models.FloatField(
    help_text=_('Latitude'),
    )   
    
    Unique_Squirrel_ID = models.CharField(
    max_length=100, 
    help_text=_('ID of squirrel'), 
    )
    
    PM='PM'
    AM='AM'

    Shift_CHOICES=( (PM,'PM'),
    (AM,'AM'),
     )

    Shift = models.CharField(
    max_length=2,
    choices=Shift_CHOICES,
    )


    Date = models.DateField(
    help_text=_('Date of squirrel'),
    )

    Adult='Adult'
    Juvenile='Juvenile'
    Other='Other'

    Age_CHOICES=( (Adult,'Adult'), 
    (Juvenile,'Juvenile'),
    (Other,'Other')
     )  

    Age = models.CharField( 
    max_length=20, 
    choices=Age_CHOICES,  
    default=Other,
    help_text=_('Age of Squirrel'),
    )

    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    Other='Other'

    Primary_Fur_Color_CHOICES=( (Gray,'Gray'),
    (Cinnamon,'Cinnamon'),
    (Black,'Black'),
    (Other,'Other')
    )

    Primary_Fur_Color = models.CharField(
    max_length=100,
    choices=Primary_Fur_Color_CHOICES,
    default=Other,
    )

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'

    Location_CHOICES=( (Ground_Plane,'Ground_Plane'), 
    (Above_Ground,'Above_Ground'),
    (Other,'Other')
     )  

    Location = models.CharField( 
    max_length=100, 
    choices=Location_CHOICES,  
    default=Other,
    help_text=_('locations of squirrel'),
    )

    Specific_Location= models.CharField(
    max_length=100,
    help_text=_('Specific Locations of Squirrel'),
    )
    
    TRUE = 'True'
    FALSE = 'False'

    CHOICES = (
            (TRUE,'True'),
            (FALSE,'False'),
            )

    Running = models.CharField(
    max_length=10,
    choices=CHOICES,
    help_text=_('Running or not'),
    )

    Chasing = models.CharField(
    max_length=10,
    choices=CHOICES,
    help_text=_('Chasing or not'),
    )

    Climbing = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Climb or not'),
            )

    Eating = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Eat or not'),
            )

    Foraging = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Forage or not'),
            )

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('Other activities'),
            )

    Kuks = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Kuks or not'),
            )

    Quaas = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Quaas or not'),
            )

    Moans = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Moans or not'),
            )

    Tail_flags = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Tail flags or not'),
            )

    Tail_twitches = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Tail twitches or not'),
            )

    Approaches = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Approaches or not'),
            )

    Indifferent= models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Indifferent or not'),
            )

    Runs_from = models.CharField(
            max_length=5,
            choices=CHOICES,
            help_text=_('Runs from or not'),
            )
