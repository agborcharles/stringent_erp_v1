from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal
from configs_settings.models import *
from product.models import *

# Create your models here.
class Storage(models.Model):
    Category = (
        ('WareHouse', 'Warehouse'),
        ('Distribution Point', 'Distribution Point'),

    )
    storage_category =  models.CharField(max_length = 500, choices=Category, default='', null = True, blank = True, verbose_name = 'Storage Type')
    storage_name   = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Storage Name')
    storage_code   = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Storage Code')
    capacity = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Storage Capacity(Sq M)')
    city = models.ForeignKey(Cities, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Address')
    storage_manager = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name = 'Storage Manager')

    latitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Latitude')
    longitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Longitude')

    start_date = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)

    def __str__(self):
        return str(self.storage_name)

    class Meta:
        verbose_name = 'Storage'
        verbose_name_plural = 'Storages'

#------------------------------------------------------------------------------------------------#