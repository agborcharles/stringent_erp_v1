from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal
from product.models import *
from storage_location.models import *
from customers.models import *


# Create your models here.

#-------------------------------------------RETURNS-----------------------------------------------------#

def increment_invoice_number():
    last_invoice = Return.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'RET0001'

    return_id = last_invoice.return_id
    invoice_int = int(return_id.split('RET000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'RET000'  + str(new_invoice_int)
    return new_invoice_id


class Return(models.Model):
    created = models.DateField(default=now, help_text = "e.g 2023-07-01", verbose_name = "Date of Return")
    return_id = models.CharField(max_length = 500, default=increment_invoice_number, null = True, blank = True, help_text = "Auto Generated", verbose_name="Return Invoice Id")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g santa lucia", verbose_name = "Customer")
    employee =  models.CharField(max_length=200, default='',help_text = "e.g Agbor Charles",  verbose_name = "Employee")
    storage_location = models.ForeignKey(Storage, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g WareHouse Name", verbose_name = "WareHouse")

    def __str__(self):
        return str(self.return_id)

    def save(self, *args, **kwargs):
        if not self.id:
            #self.due_date = datetime.datetime.now()+ datetime.timedelta(days=3)
            self.due_date = self.created + datetime.timedelta(days=3)

        return super(Return, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Return'
        verbose_name_plural = 'Returns'


class ReturnDetail(models.Model):

    return_id = models.ForeignKey(Return, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Purchase Invoice Id")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Product")
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name="Quantity")
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")
    total_at_cost = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True)
    #vat = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")

    class Meta:
        verbose_name = 'Return  Items'
        verbose_name_plural = 'Return  Items'

# Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.total_at_cost = (Decimal(self.quantity) * Decimal(self.cost_price))
        #self.vat = self.total_at_cost * Decimal(19.25/100)

        #self.invoice.save()
        super().save(*args, **kwargs)