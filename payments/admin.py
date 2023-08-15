from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *



class PaymentAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'payment_date','payment_id', 'invoice_id', 'payment_method', 'installment', 
                    'amount_paid', 'bank_name', 'account_number', 'employee']
    search_fields = [ ]
    list_display_links = [ 'id', 'payment_date','payment_id', 'invoice_id', 'payment_method', 'installment', 
                    'amount_paid', 'bank_name', 'account_number', 'employee']
    list_per_page = 20
    list_max_show_all = 3

    resource_class = PaymentAdminResource



admin.site.register(Payment, PaymentAdmin)
