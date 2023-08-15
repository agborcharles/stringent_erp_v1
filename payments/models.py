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
from sales.models import *

# Create your models here.

#-------------------------------------------PURCHASES-----------------------------------------------------#

def increment_invoice_number():
    last_invoice = Payment.objects.all().order_by('id').last()
    today = datetime.date.today()
    today_string = today.strftime("%Y-%m-%d")

    if not last_invoice:
            return today_string + "-" + 'PAYINV0001'

    payment_id = last_invoice.payment_id
    invoice_int = int(payment_id.split('PAY-INV000')[-1])
    new_invoice_int = invoice_int + 1

    new_invoice_id = today_string + "-" + 'PAY-INV000'  + str(new_invoice_int)
    return new_invoice_id

class Payment(models.Model):
    Payment_Method = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('Mobile Money', 'Mobile Money'),
        ('Orange Money', 'Orange Money'),
        ('Visa', 'Visa'),

    )

    INSTALLMENTS = (
        ('1st Installment', '1st Installment'),
        ('2nd Installment', '2nd Installment'),
        ('3rd Installment', '3rd Installment'),
        ('4th Installment', '4th Installment'),
        ('5th Installment', '5th Installment'),
        ('6th Installment', '6th Installment'),
        ('7th Installment', '7th Installment'),
        ('8th Installment', '8th Installment'),
        ('9th Installment', '9th Installment'),
    )

    payment_date = models.DateField(default=now, help_text = "e.g 2023-07-01", verbose_name = "Payment Date")
    payment_id = models.CharField(max_length = 500, default=increment_invoice_number, null = True, blank = True, help_text = "Auto Generated", verbose_name="Payment Id")
    invoice_id = models.ForeignKey(SalesInvoices, on_delete=models.SET_NULL, blank=True, null=True, help_text = "e.g Meno", verbose_name = "Invoice Id")
    payment_method = models.CharField(max_length = 500, choices=Payment_Method, null = True, blank = True, help_text = "Auto Generated", verbose_name="Payment Method")
    installment= models.CharField(max_length = 500, choices=INSTALLMENTS, null = True, blank = True, help_text = "Choose from List", verbose_name="Installment #")
    amount_paid = models.DecimalField(max_digits=20, decimal_places=0, default=0, blank=True, null=True, verbose_name="Amount Paid")
    bank_name = models.CharField(max_length = 500, default="", null = True, blank = True, help_text = "If Payment is Bank", verbose_name="Bank Name")
    account_number = models.CharField(max_length = 500, default="", null = True, blank = True, help_text = "If Payment is Bank", verbose_name="Bank Name")
    employee =  models.CharField(max_length = 500, default="", blank=True, null=True, help_text = "e.g Jane", verbose_name = "Employee")
   
   
    def __str__(self):
        return str(self.payment_id)


    class Meta:
        verbose_name = 'Payments'
        verbose_name_plural = 'Payments'


