from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.
# Register your models here.

class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'employee_name', 'role', 'manager',]
    list_display_links = ['id',  'role', 'manager',]
    list_per_page =100

    resource_class = EmployeeAdminResource


admin.site.register(Employee, EmployeeAdmin)
