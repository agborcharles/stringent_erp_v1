from django.contrib import admin
from . models import *
from configs_settings.models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.
# Register your models here.


class InventoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'created', 'inventory_id', 'employee', 'supervised_by', 'storage_location', ]
    list_display_links = ['id', 'created', 'inventory_id', 'employee', 'supervised_by', 'storage_location',   ]
    list_per_page =500

    resource_class = InventoryAdminResource

class InventoryItemsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'inventory_id', 'status', 'product_name', 'quantity', 'cost_price', 'total_cost', ]
    search_fields = [ ]
    list_display_links = ['id', 'inventory_id', 'status', 'product_name', 'quantity', 'cost_price',  'total_cost',  ]
    list_per_page = 500

    resource_class = InventoryItemsAdminResource

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(InventoryItems, InventoryItemsAdmin)