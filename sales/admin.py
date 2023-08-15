from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *



class SalesInvoicesAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'invoiced_date','invoice_id', 'customer', 'sales_person', 'due_date', 'distribution_point', 'status',]
    search_fields = [ ]
    list_display_links = [ 'id', 'invoiced_date', 'invoice_id', 'customer', 'sales_person', 'due_date', 'distribution_point', 'status',]

    resource_class = SalesInvoicesAdminResource

class SalesInvoiceDetailAdmin(ImportExportModelAdmin):
    list_display = ['id', 'invoice',  'product', 'quantity', 'cost_price', 'vat', 'discount', 'total_at_cost', ]
    search_fields = [ ]
    list_display_links = ['id', 'invoice',  'product', 'quantity', 'cost_price', 'vat', 'discount', 'total_at_cost', ]

    resource_class = SalesInvoiceDetailAdminResource


admin.site.register(SalesInvoices, SalesInvoicesAdmin)
admin.site.register(SalesInvoiceDetail, SalesInvoiceDetailAdmin)