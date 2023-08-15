from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
#from .resources import *



class TransferInvoiceAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'transfer_id', 'transfer_type', "sender" , 'reciever', 'storage_location']
    search_fields = [ ]
    list_display_links = [ 'id', 'created', 'transfer_id', 'transfer_type', "sender" , 'reciever', 'storage_location']

    #resource_class = TransferTransactionAdminResource

class TransferDetailAdmin(ImportExportModelAdmin):
    list_display = ['id', 'transfer_invoice_id',  'product', 'quantity', 'cost_price', 'total_at_cost', ]
    search_fields = [ ]
    list_display_links = ['id', 'transfer_invoice_id',  'product', 'quantity', 'cost_price', 'total_at_cost', ]

    #resource_class = PurchaseInvoicesDetailAdminResource



admin.site.register(TransferInvoice, TransferInvoiceAdmin)
admin.site.register(TransferDetail, TransferDetailAdmin)