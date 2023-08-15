from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

class VendorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'supplier_name', 'supplier_type', 'company_name', 'phone1', 'phone2', 'email', 'website']
    search_fields = [ ]
    list_display_links = ['id', 'supplier_name', 'supplier_type','company_name', 'phone1', 'phone2', 'email', 'website']



class PurchaseInvoicesAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'invoice_id', 'vendor', "employee" , 'due_date', 'storage_location']
    search_fields = [ ]
    list_display_links = [ 'id', 'created', 'invoice_id', 'vendor', "employee" , 'due_date',  'storage_location']

    resource_class = PurchaseInvoicesAdminResource

class PurchaseInvoicesDetailAdmin(ImportExportModelAdmin):
    list_display = ['id', 'invoice',  'product', 'quantity', 'cost_price', 'total_at_cost', ]
    search_fields = [ ]
    list_display_links = ['id', 'invoice',  'product', 'quantity', 'cost_price', 'total_at_cost', ]

    resource_class = PurchaseInvoicesDetailAdminResource


admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseInvoices, PurchaseInvoicesAdmin)
admin.site.register(PurchaseInvoicesDetail, PurchaseInvoicesDetailAdmin)