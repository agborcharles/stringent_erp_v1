from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *



class EmployeeAdminResource(resources.ModelResource):
    role = fields.Field(column_name='role', attribute='role',
                            widget=ForeignKeyWidget(JobPosition, field='job_position_name'))
    
    manager = fields.Field(column_name='manager', attribute='manager',
                            widget=ForeignKeyWidget(BranchManager, field='manager_name'))
    class Meta:
        model = Employee
        fields = ('id', 'employee_name', 'role', 'manager',)

