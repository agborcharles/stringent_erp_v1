from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



class PurchaseInvoicesAdminResource(resources.ModelResource):
    vendor = fields.Field(column_name='vendor', attribute='vendor',
                            widget=ForeignKeyWidget(Vendor, field='supplier_name'))
    
    storage_location = fields.Field(column_name='storage_location', attribute='storage_location',
                            widget=ForeignKeyWidget(Storage, field='storage_name'))
    class Meta:
        model = PurchaseInvoices
        fields = ( 'id', 'created', 'invoice_id', 'vendor', "employee" , 'storage_location', 'due_date',)

class PurchaseInvoicesDetailAdminResource(resources.ModelResource):
    invoice = fields.Field(column_name='invoice', attribute='invoice',
                        widget=ForeignKeyWidget(PurchaseInvoices, field='invoice_id'))

    product= fields.Field(column_name='product', attribute='product',
                        widget=ForeignKeyWidget(Product, field='product_name'))
    class Meta:
        model = PurchaseInvoicesDetail
        fields = (
            'id', 'invoice',  'product', 'quantity', 'cost_price', 'total_at_cost',
            )