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

class Vendor(models.Model):

    VENDOR_TYPE = (

        ('Company', 'Company'),
        ('Enterprise', 'Enterprise'),
        ('Individual', 'Individual'),

    )

    '''General information fields'''
    supplier_name = models.CharField(max_length=200,  verbose_name = "Supplier Name")
    supplier_type = models.CharField(max_length=100, choices=VENDOR_TYPE , null = True, blank = True, verbose_name = "Supplier Type")
    company_name = models.CharField(max_length=200, default='', null = True, blank = True, verbose_name = "Company Name")
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    '''Contact details fields'''
    address = models.TextField(max_length=2550, null = True, blank = True, verbose_name = "Address")
    city = models.CharField(max_length=100, default='Kumba', null = True, blank = True, verbose_name = "City")
    phone1 = models.CharField(max_length=15, null=True, blank = True, verbose_name = "Phone 1 +237")
    phone2 = models.CharField(max_length=15, null=True, blank = True, verbose_name = "Phone 2 +237")
    email = models.EmailField(blank=True, null=True, help_text = "e.g ag@gmail.com", verbose_name = "Email")
    website = models.URLField(blank=True, null=True, help_text = "e.g www.google.com", verbose_name = "Website")

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return "{}".format(self.supplier_name)


    #def get_absolute_url(self):
        #return reverse('supplier:supplier-details', args=[self.slug])

    def save(self, *args, **kwargs):
            self.slug = slugify(self.supplier_name)
            super(Vendor, self).save(*args, **kwargs)

#-------------------------------------------PURCHASES-----------------------------------------------------#

def increment_invoice_number():
    last_invoice = PurchaseInvoices.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'PURINV0001'

    invoice_id = last_invoice.invoice_id
    invoice_int = int(invoice_id.split('PURINV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'PURINV000'  + str(new_invoice_int)
    return new_invoice_id


class PurchaseInvoices(models.Model):
    created = models.DateField(default=now, help_text = "e.g 2023-07-01", verbose_name = "Date of Purchase")
    invoice_id = models.CharField(max_length = 500, default=increment_invoice_number, null = True, blank = True, help_text = "Auto Generated", verbose_name="Purchase Invoice Id")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g Robertson Winery", verbose_name = "Supplier")
    employee =  models.CharField(max_length=200, default='',help_text = "e.g Agbor Charles",  verbose_name = "Employee")
    due_date = models.DateField(null=True, blank=True, help_text = "e.g 2023-07-01", verbose_name = "Due Date")
    storage_location = models.ForeignKey(Storage, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g WareHouse Name", verbose_name = "WareHouse")

    def __str__(self):
        return str(self.invoice_id)

    def save(self, *args, **kwargs):
        if not self.id:
            #self.due_date = datetime.datetime.now()+ datetime.timedelta(days=3)
            self.due_date = self.created + datetime.timedelta(days=3)

        return super(PurchaseInvoices, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Purchase Invoice'
        verbose_name_plural = 'Purchase Invoices'


class PurchaseInvoicesDetail(models.Model):

    invoice = models.ForeignKey(PurchaseInvoices, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Purchase Invoice Id")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Product")
    quantity = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name="Quantity")
    cost_price = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")
    total_at_cost = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True)
    #vat = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Cost Price")

    class Meta:
        verbose_name = 'Purchase Invoices Items'
        verbose_name_plural = 'Purchase Invoices Items'

# Overriding the save method to update invoice total for each new item
    def save(self, *args, **kwargs):
        self.total_at_cost = (Decimal(self.quantity) * Decimal(self.cost_price))
        #self.vat = self.total_at_cost * Decimal(19.25/100)

        #self.invoice.save()
        super().save(*args, **kwargs)