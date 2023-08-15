from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal

# Create your models here.
class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=100, default='')



    def __str__(self):
        return str(self.product_category_name)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

#------------------------------------------------------------------------------------------------#
class Product(models.Model):
    product_name = models.CharField(max_length=100, default='', unique=True, verbose_name = "Product Name")
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, default=1, null = True, blank = True, verbose_name = "Product Category")
    bar_code = models.CharField(max_length=100, default='', null = True, blank = True, unique=True, verbose_name = "Bar Code")
    reorder_level = models.DecimalField(max_digits=20, decimal_places=2, default=0, null = True, blank = True, verbose_name = "Reorder Level(Units)")
    cost_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, null = True, blank = True, verbose_name = "Cost Price")
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, default=0, null = True, blank = True, verbose_name = "Selling Price")
    slug = models.SlugField(max_length=100, unique=True, blank=True)


    def __str__(self):
        return str(self.product_name)

    #def get_absolute_url(self):
        #return reverse('product:product-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.product_name)
            super(Product, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

