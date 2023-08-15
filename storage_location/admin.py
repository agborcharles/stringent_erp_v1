from django.contrib import admin
from . models import *
from configs_settings.models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.

class StorageAdmin(ImportExportModelAdmin):
    list_display = ['id',  'storage_name', 'storage_code', 'storage_category', 'storage_manager', 'city', 
                    'capacity', 'latitude', 'longitude', 'start_date', 'updated', ]
    list_display_links = ['id',  'storage_name', 'storage_code', 'storage_category', 'storage_manager', 'city', 
                    'capacity', 'latitude', 'longitude', 'start_date', 'updated', ]
    list_per_page =100

    resource_class = StorageAdminResource

admin.site.register(Storage,  StorageAdmin)
