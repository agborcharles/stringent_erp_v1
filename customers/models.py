from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal
from product.models import *
from storage_location.models import *
from configs_settings.models import *


# Create your models here.

class Customer(models.Model):

    Customer_TYPE = (

        ('Supermarket', 'Supermarket'),
        ('Wine Shop', 'Wine Shop'),
        ('Convenience Store', 'Convenience Store'),
        ('Restaurants', 'Restaurants'),
        ('Hotel', 'Hotel'),
        ('Snack Bar', 'Snack Bar'),
        ('Catering Service', 'Catering Service'),
        ('Individual', 'Individual'),
        ('Others', 'Others'),

    )

    Payment_Terms = (

        ('Immediate Payment', 'Immediate Payment'),
        ('15 Days', '15 Days'),
        ('30 Days', '30 Days'),
        ('45 Days', '45 Days'),
        ('2 Months', '2 Months'),
        ('End of Following Month', 'End of Following Month'),

    )

    '''General information fields'''
    customer_name = models.CharField(max_length=200,  verbose_name = "Customer Name")
    customer_type = models.CharField(max_length=100, choices=Customer_TYPE , null = True, blank = True, verbose_name = "Customer Type")
    contact_person = models.CharField(max_length=200, default='', verbose_name = "Contact Person")
    tel = models.CharField(max_length=15, null=True, blank = True, help_text = "Phone Number of Contact Person", verbose_name = "Tel")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    '''Contact details fields'''
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g Douala", verbose_name = "City")
    address = models.TextField(max_length=2550, null = True, blank = True, verbose_name = "Address")
    quarter = models.CharField(max_length=100, default='', null = True, blank = True, verbose_name = "Quarter")
    phone1 = models.CharField(max_length=15, null=True, blank = True, verbose_name = "Phone 1 +237")
    phone2 = models.CharField(max_length=15, null=True, blank = True, verbose_name = "Phone 2 +237")
    email = models.EmailField(blank=True, null=True, help_text = "e.g ag@gmail.com", verbose_name = "Email")

    payment_terms = models.CharField(max_length=100, choices=Payment_Terms , null = True, blank = True, verbose_name = "Payment Terms")

    latitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Latitude')
    longitude =  models.FloatField(null=True, default=0, blank = True, verbose_name = 'Longitude')

    startdate = models.DateField(auto_now_add=True, blank=True,null=True, verbose_name='Created')
    updated = models.DateTimeField(verbose_name=('Updated'),auto_now=True,null=True)


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "{}".format(self.customer_name)


    #def get_absolute_url(self):
        #return reverse('supplier:supplier-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.customer_name)
            super(Customer, self).save(*args, **kwargs)