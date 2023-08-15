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

#-------------------------------------------PURCHASES-----------------------------------------------------#

def increment_invoice_number():
    last_invoice = SalesInvoices.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'INV0001'

    invoice_id = last_invoice.invoice_id
    invoice_int = int(invoice_id.split('INV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'INV000'  + str(new_invoice_int)
    return new_invoice_id

class SalesInvoices(models.Model):
    Payment_Terms = (
        ('Immediate Payment', 'Immediate Payment'),
        ('15 Days', '15 Days'),
        ('30 Days', '30 Days'),
        ('45 Days', '45 Days'),
        ('2 Months', '2 Months'),
        ('End of Following Month', 'End of Following Month'),
    )

    STATUS = (
        ('Sales', 'Sales'),
        ('Returns', 'Returns'),
    )

    invoiced_date = models.DateField(default=now, help_text = "e.g 2023-07-01", verbose_name = "Invoiced Date")
    invoice_id = models.CharField(max_length = 500, default=increment_invoice_number, null = True, blank = True, help_text = "Auto Generated", verbose_name="Purchase Invoice Id")
    status = models.CharField(max_length = 500, choices=STATUS , default="Sales", null = True, blank = True, help_text = "Sales / Returns", verbose_name="Transaction Status")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g Meno", verbose_name = "Customer")
    distribution_point = models.ForeignKey(Storage, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g DS AKWA", verbose_name = "Distribution Points")
    sales_person =  models.CharField(max_length=200, default='',help_text = "e.g Agbor Charles",  verbose_name = "Sales Person")
    due_date = models.DateField(null=True, blank=True, help_text = "e.g 2023-07-01", verbose_name = "Due Date")
   
    def __str__(self):
        return str(self.invoice_id)

    def save(self, *args, **kwargs):
        if not self.id:
            #self.due_date = datetime.datetime.now()+ datetime.timedelta(days=3)
            self.due_date = self.invoiced_date + datetime.timedelta(days=3)

        return super(SalesInvoices, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Sales Invoice'
        verbose_name_plural = 'Sales Invoices'


class SalesInvoiceDetail(models.Model):

    invoice = models.ForeignKey(SalesInvoices, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Purchase Invoice Id")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Product")
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name="Quantity")
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")
    discount = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Discount")
    vat = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Vat")
    total_at_cost = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Amount")

    class Meta:
        verbose_name = 'Sales Invoice Items'
        verbose_name_plural = 'Sales Invoice Items'

# Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.vat = self.cost_price * Decimal(0.1925)
        self.total_at_cost = (Decimal(self.quantity) * Decimal(self.cost_price) + self.vat)
        
        self.invoice.save()
        super().save(*args, **kwargs)