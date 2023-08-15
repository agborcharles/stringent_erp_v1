from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *


class CitiesAdminResource(resources.ModelResource):
    country = fields.Field(column_name='country', attribute='country',
                            widget=ForeignKeyWidget(Country, field='country_name'))

    class Meta:
        model = Cities
        fields = ('id','city_name','country_name','latitude', 'longitude')

#------------------------------- WORK LOCATION -------------------------------------#
class BranchManagerAdminResource(resources.ModelResource):
    class Meta:
        model = BranchManager
        fields = ('id','manager_name', )

class WorkLocationAdminResource(resources.ModelResource):
    city = fields.Field(column_name='city', attribute='city',
                            widget=ForeignKeyWidget(Cities, field='city_name'))
    branch_manager = fields.Field(column_name='manager_name', attribute='manager_name',
                            widget=ForeignKeyWidget(BranchManager, field='branch_manager'))

    class Meta:
        model = WorkLocation
        fields = ('id','location_name','address', 'branch_manager', 'city', 'status' 'startdate', 'updated' )

#------------------------------- WORK LOCATION END // -------------------------------------#




class DepartmentAdminResource(resources.ModelResource):
    manager_name = fields.Field(column_name='manager_name', attribute='manager_name',
                            widget=ForeignKeyWidget(BranchManager, field='manager_name'))

    class Meta:
        model = Department
        fields = ('id','name', 'manager_name','work_location', 'startdate', 'updated', )

class SubDepartmentAdminResource(resources.ModelResource):
    department = fields.Field(column_name='department', attribute='department',
                            widget=ForeignKeyWidget(Department, field='name'))

    class Meta:
        model = SubDepartment
        fields = ('id','name','department', )

class RoleAdminResource(resources.ModelResource):
    sub_department = fields.Field(column_name='sub_department', attribute='sub_department',
                            widget=ForeignKeyWidget(SubDepartment, field='name'))

    class Meta:
        model = JobPosition
        fields = ('id', 'job_position_name', 'sub_department',)