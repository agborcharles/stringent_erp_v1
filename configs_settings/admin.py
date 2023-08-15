from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *

# Register your models here.
# Register your models here.

class BranchManagerAdmin(ImportExportModelAdmin):
    list_display = ['id',  'manager_name', ]
    list_display_links = ['id', 'manager_name', ]
    list_per_page =100

    resource_class = BranchManagerAdminResource

class WorkLocationAdmin(ImportExportModelAdmin):
    list_display = ['id', 'location_name', 'branch_manager', 'address','city',  'status' ]
    search_fields = [ ]
    list_display_links = ['id', 'location_name', 'branch_manager', 'address','city', 'status' ]
    #list_per_page =30
    #list_filter = (, )
    list_editable = ( )

    resource_class = WorkLocationAdminResource

class DepartmentAdmin(ImportExportModelAdmin):
    list_display = ['id',  'name', 'manager_name', ]
    list_display_links = ['id', 'name', 'manager_name',]
    list_per_page =100

    resource_class = DepartmentAdminResource

class SubDepartmentAdmin(ImportExportModelAdmin):
    list_display = ['id', 'department', 'name', ]
    list_display_links = ['id', 'department', 'name', ]
    list_per_page =100

    resource_class = SubDepartmentAdminResource


class JobPositionAdmin(ImportExportModelAdmin):
    list_display = ['id',  'job_position_name', 'sub_department',]
    list_display_links = ['id', 'job_position_name', 'sub_department',]
    list_per_page =100

    resource_class = RoleAdminResource





class RegionAdmin(ImportExportModelAdmin):
    list_display = ['id', 'region_name',]
    search_fields = [ ]
    list_display_links = ['id', 'region_name',]
    list_per_page =100
    #list_filter = (, )
    list_editable = ( )

    #resource_class = CourseAdminResource

class CountryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'country_name', 'region']
    search_fields = [ ]
    list_display_links = ['id', 'country_name',]
    list_per_page =100
    #list_filter = (, )
    list_editable = ( )

    #resource_class = CountryAdminResource

class CitiesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'city_name','country','latitude', 'longitude' ]
    search_fields = [ ]
    list_display_links = ['id', 'city_name','country',]
    #list_per_page =30
    #list_filter = (, )
    list_editable = ( )

    resource_class = CitiesAdminResource




admin.site.register(WorkLocation,  WorkLocationAdmin)
admin.site.register(Region,  RegionAdmin)
admin.site.register(Cities,  CitiesAdmin)
admin.site.register(Country,  CountryAdmin)
admin.site.register(JobPosition, JobPositionAdmin)
admin.site.register(BranchManager, BranchManagerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(SubDepartment, SubDepartmentAdmin)

