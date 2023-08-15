from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *


class ReturnAdmin(ImportExportModelAdmin):
    list_display = [ 'id', 'created', 'return_id', 'customer', "employee" , 'storage_location']
    search_fields = [ ]
    list_display_links = [ 'id', 'created', 'return_id', 'customer', "employee" ,  'storage_location']

    resource_class = ReturnAdminResource

class ReturnDetailAdmin(ImportExportModelAdmin):
    list_display = ['id', 'return_id',  'product', 'quantity', 'cost_price', 'total_at_cost', ]
    search_fields = [ ]
    list_display_links = ['id', 'return_id',  'product', 'quantity', 'cost_price', 'total_at_cost', ]

    resource_class = ReturnDetailAdminResource


admin.site.register(Return, ReturnAdmin)
admin.site.register(ReturnDetail, ReturnDetailAdmin)