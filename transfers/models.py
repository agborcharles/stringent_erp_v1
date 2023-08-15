from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal
from product.models import *
from storage_location.models import *


# Create your models here.
#-------------------------------------------PURCHASES-----------------------------------------------------#

def increment_invoice_number():
    last_invoice = TransferInvoice.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'TRANS0001'

    transfer_id = last_invoice.transfer_id
    invoice_int = int(transfer_id.split('TRANS000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'TRANS000'  + str(new_invoice_int)
    return new_invoice_id


class TransferInvoice(models.Model):
    TRANSFER_TYPE = (

        ('Transfer Outwards', 'Transfer Outwards'),
        ('Transfer Inwards', 'Transfer Inwards'),

    )

    created = models.DateField(default=now, help_text = "e.g 2023-07-01", verbose_name = "Date of Purchase")
    transfer_id = models.CharField(max_length = 500, default=increment_invoice_number, null = True, blank = True, help_text = "Auto Generated", verbose_name="Purchase Invoice Id")
    transfer_type = models.CharField(max_length=100, choices=TRANSFER_TYPE , help_text = "Transfer Outwards/Inwards", null = True, blank = True, verbose_name = "Transfer Type")
    sender = models.CharField(max_length=100, default='', null = True, blank = True, verbose_name = "Sender")
    reciever = models.CharField(max_length=100, default='', null = True, blank = True, verbose_name = "Reciever")
    storage_location = models.ForeignKey(Storage, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g WareHouse Name", verbose_name = "WareHouse")
  

    def __str__(self):
        return str(self.transfer_id)

    class Meta:
        verbose_name = 'Transfer Invoice'
        verbose_name_plural = 'Transfer Invoices'


class TransferDetail(models.Model):

    transfer_invoice_id = models.ForeignKey(TransferInvoice, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Purchase Invoice Id")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Product")
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name="Quantity")
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")
    total_at_cost = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Transfer Details'
        verbose_name_plural = 'Transfer Details'

# Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.total_at_cost = (Decimal(self.quantity) * Decimal(self.cost_price))
        #self.vat = self.total_at_cost * Decimal(19.25/100)

        #self.invoice.save()
        super().save(*args, **kwargs)