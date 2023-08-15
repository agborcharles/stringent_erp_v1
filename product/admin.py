from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *
# Register your models here.

class ProductAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product_name', 'product_category', 'bar_code', 
                    'cost_price', 'selling_price', 'slug', 'reorder_level',]
    search_fields = []
    list_display_links = ['id', 'product_name', 'product_category', 'bar_code', 
                    'cost_price', 'selling_price', 'slug', 'reorder_level', ]

    resource_class = ProductAdminResource


class ProductCategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product_category_name',]
    search_fields = []
    list_display_links = ['id', 'product_category_name', ]
    resource_class = ProductCategoryAdminResource

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)