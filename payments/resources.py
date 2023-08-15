from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *
from sales.models import *

class PaymentAdminResource(resources.ModelResource):
    #customer = fields.Field(column_name='customer', attribute='customer',
                            #widget=ForeignKeyWidget(Customer, field='customer_name'))
    
    invoice_id = fields.Field(column_name='invoice_id', attribute='invoice_id',
                        widget=ForeignKeyWidget(SalesInvoices, field='invoice_id'))
    class Meta:
        model = Payment
        fields = ('id', 'payment_date','payment_id', 'invoice_id', 'payment_method', 'installment', 
                    'amount_paid', 'bank_name', 'account_number', 'employee',)

