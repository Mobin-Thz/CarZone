from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField 
# Create your models here.
class Car (models.Model):

    state_choice= (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    drivetrain_choices = (
        ('RWD','RWD'),
        ('FWD','FWD'),
        ('AWD','AWD'),
    )

    car_title = models.CharField(max_length=100,)
    model = models.CharField(max_length=100,)
    city = models.CharField(max_length=50,)
    state = models.CharField(choices=state_choice, max_length=100,)
    color = models.CharField(max_length=50,)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=50,)
    price = models.IntegerField()
    description = RichTextField(max_length=1000,)
    car_image = models.ImageField(upload_to='photos/%Y/%M/%D/')
    car_image1 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    car_image2 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    car_image3 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    car_image4 = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    features = MultiSelectField(choices=features_choices ,max_length=100,)
    body_style = models.CharField(max_length=50,)
    transmission = models.CharField(max_length=50,)
    interior = models.CharField(max_length=50,)
    miles = models.IntegerField()
    drivetrain = models.CharField(choices=drivetrain_choices, max_length=50, blank=True)
    doors = models.CharField(choices=door_choices , max_length=50,)
    passengers= models.CharField(max_length=50,)
    vin_no= models.CharField(max_length=50,)
    milage= models.IntegerField()
    fuel_type= models.CharField(max_length=50,)
    no_of_owners = models.CharField(max_length=50,)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)





    def __str__(self):
        return self.car_title