from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



class SalesInvoicesAdminResource(resources.ModelResource):
    customer = fields.Field(column_name='customer', attribute='customer',
                            widget=ForeignKeyWidget(Customer, field='customer_name'))
    
    distribution_point = fields.Field(column_name='distribution_point', attribute='distribution_point',
                            widget=ForeignKeyWidget(Storage, field='storage_name'))
    class Meta:
        model = SalesInvoices
        fields = (  'id', 'invoiced_date', 'invoice_id', 'sales_person', 'due_date', 'distribution_point','status',)

class SalesInvoiceDetailAdminResource(resources.ModelResource):
    invoice = fields.Field(column_name='invoice', attribute='invoice',
                        widget=ForeignKeyWidget(SalesInvoices, field='invoice_id'))

    product= fields.Field(column_name='product', attribute='product',
                        widget=ForeignKeyWidget(Product, field='product_name'))
    class Meta:
        model = SalesInvoiceDetail
        fields = (
                    'id', 'invoice',  'product', 'quantity', 'cost_price', 'vat', 'discount', 'total_at_cost', 
            )