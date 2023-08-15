from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal
from configs_settings.models import *
from product.models import *
from storage_location.models import *



# Create your models here.


#------------------------------------------// INVENTORY //------------------------------------------------------#

def increment_inventory_number():
    last_invoice = Inventory.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'INVEN0001'

    invoice_id = last_invoice.inventory_id
    invoice_int = int(invoice_id.split('INVEN000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'INVEN000'  + str(new_invoice_int)
    return new_invoice_id

class Inventory(models.Model):
    
    created = models.DateField(default=now, verbose_name = "Date")
    inventory_id = models.CharField(max_length = 500,default=increment_inventory_number, null = True, blank = True, verbose_name="Inventory Id")
    storage_location = models.ForeignKey(Storage, on_delete=models.SET_NULL, default=1, null = True, blank = True, verbose_name = "Product Category")
    employee = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name="Employee")
    supervised_by = models.CharField(max_length = 500,  default='', null = True, blank = True, verbose_name="Supervisor By")
    

    def __str__(self):
        return str(self.inventory_id)

    class Meta():
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventory'

#---------------------------------// INVENTORY //------------------------------------------#
class InventoryItems(models.Model):
    Status = (
        ('Opening Stock', 'Opening Stock'),
        ('Closing Stock', 'Closing Stock'),
    )
    created = models.DateField(default=now, verbose_name = "Date")
    inventory_id = models.ForeignKey(Inventory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Inventory Id")
    status =  models.CharField(max_length = 500, choices=Status,  default='', null = True, blank = True )
    product_name = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Product Name")
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    total_cost = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True,)

    class Meta():
        verbose_name = 'Inventory Item'
        verbose_name_plural = 'Inventory Items Details'

    # Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.total_cost = self.quantity * self.cost_price

        #self.total_amount = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        #self.invoice.save()
        super().save(*args, **kwargs)