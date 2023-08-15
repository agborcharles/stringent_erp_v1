from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *

#------------------------------- WORK LOCATION -------------------------------------#

class InventoryAdminResource(resources.ModelResource):
    storage_location = fields.Field(column_name='storage_location', attribute='storage_location',
                        widget=ForeignKeyWidget(Storage, field='storage_name'))

    class Meta:
        model = Inventory
        fields = (
            'id', 'created', 'inventory_id', 'employee', 'supervised_by', 'storage_location',
        )


class InventoryItemsAdminResource(resources.ModelResource):
    inventory_id = fields.Field(column_name='inventory_id', attribute='inventory_id',
                        widget=ForeignKeyWidget(Inventory, field='inventory_id'))

    product_name= fields.Field(column_name='product_name', attribute='product_name',
                        widget=ForeignKeyWidget(Product, field='product_name'))
    class Meta:
        model = InventoryItems
        fields = (
            'id', 'created', 'inventory_id', 'status', 'product_name', 
            'quantity', 'cost_price', 'total_cost',
        )

