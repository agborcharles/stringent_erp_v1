from inspect import Attribute
from tkinter import Widget
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *




class ProductCategoryAdminResource(resources.ModelResource):
    class Meta:
        model = ProductCategory
        fields = ( 'id', 'category_name', )


class ProductAdminResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category',
                        widget=ForeignKeyWidget(ProductCategory, field='product_category_name'))
    class Meta:
        model = Product
        fields = (
            'id','created','product_name', 'product_category', 'bar_code', 'cost_price', 'selling_price', 'slug', 'reorder_level',
        )
