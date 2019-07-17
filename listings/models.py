from django.db import models
from datetime import datetime
from realtors.models import Realtor

# google maps
from django_google_maps import fields as map_fields
# end of google maps

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = map_fields.AddressField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    latitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=100)
    APARTMENT= 'APARTMENT'
    INDEPENDENT = 'INDEPENDENT'
    LISTING_TYPE = (
        (APARTMENT, 'Apartment'),
        (INDEPENDENT, 'Independent'),
        
    )
    house_type = models.CharField(max_length=20,
                                      choices=LISTING_TYPE,
                                      default=APARTMENT)
    
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    balcony = models.IntegerField(default=0)
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    video = models.BinaryField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    water_supply = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    lawn = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    water_heater = models.BooleanField(default=False)
    TILE= 'TILE'
    MOSSAIC = 'MOSSAIC'
    GRANITE = 'GRANITE'
    MARBLE = 'MARBLE'
    TILE_TYPE = (
         (TILE, 'Tile'),
         (MOSSAIC, 'Mossaic'),
         (GRANITE, 'Granite'),
         (MARBLE, 'Marble'),
        
     )
    tile_type = models.CharField(max_length=10,
                                       choices=TILE_TYPE,
                                       default=TILE)
    
    def __str__(self):
        return self.title