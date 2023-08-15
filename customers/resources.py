from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



class CustomerAdminResource(resources.ModelResource):
    city = fields.Field(column_name='city', attribute='city',
                            widget=ForeignKeyWidget(Cities, field='city_name'))
    

    class Meta:
        model = Customer
        fields = ( 'id', 'customer_name', 'customer_type', 'contact_person', 'tel', 'phone1', 'phone2', 'email', 
                    'city', 'quarter', 'payment_terms', 'latitude', 'longitude', 'address',)
