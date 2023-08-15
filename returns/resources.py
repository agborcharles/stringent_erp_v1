from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



class ReturnAdminResource(resources.ModelResource):
    customer = fields.Field(column_name='customer', attribute='customer',
                            widget=ForeignKeyWidget(Customer, field='customer_name'))
    
    storage_location = fields.Field(column_name='storage_location', attribute='storage_location',
                            widget=ForeignKeyWidget(Storage, field='storage_name'))
    class Meta:
        model = Return
        fields = ( 'id', 'created', 'return_id', 'customer', "employee" , 'storage_location')

class ReturnDetailAdminResource(resources.ModelResource):
    return_id = fields.Field(column_name='return_id', attribute='return_id',
                        widget=ForeignKeyWidget(Return, field='return_id'))

    product= fields.Field(column_name='product', attribute='product',
                        widget=ForeignKeyWidget(Product, field='product_name'))
    class Meta:
        model = ReturnDetail
        fields = (
            'id', 'invoice',  'product', 'quantity', 'cost_price', 'total_at_cost',
            )