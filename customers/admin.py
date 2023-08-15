from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

class CustomerAdmin(ImportExportModelAdmin):
    list_display = ['id', 'customer_name', 'customer_type', 'contact_person', 'phone1', 'tel', 'phone2', 'email', 
                    'city', 'quarter', 'payment_terms', 'latitude', 'longitude', ]
    search_fields = [ ]
    list_display_links = ['id', 'customer_name', 'customer_type', 'contact_person', 'tel', 'phone1', 'phone2', 'email', 
                    'city', 'quarter', 'payment_terms', 'latitude', 'longitude',]
    
    list_per_page = 20
    list_max_show_all = 3
    
    resource_class = CustomerAdminResource

admin.site.register(Customer, CustomerAdmin)
