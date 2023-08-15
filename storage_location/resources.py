from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



#------------------------------- WORK LOCATION -------------------------------------#

class StorageAdminResource(resources.ModelResource):
    city = fields.Field(column_name='city', attribute='city',
                            widget=ForeignKeyWidget(Cities, field='city_name'))

    class Meta:
        model = Storage
        fields = ('id',  'storage_name', 'storage_code', 'storage_category', 'storage_manager', 'city', 
                    'capacity', 'latitude', 'longitude', 'start_date', 'updated', )
        
