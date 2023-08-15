# Generated by Django 4.2.3 on 2023-07-30 17:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import payments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0010_alter_salesinvoices_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(default=django.utils.timezone.now, help_text='e.g 2023-07-01', verbose_name='Payment Date')),
                ('payment_id', models.CharField(blank=True, default=payments.models.increment_invoice_number, help_text='Auto Generated', max_length=500, null=True, verbose_name='Payment Id')),
                ('payment_method', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Mobile Money', 'Mobile Money'), ('Orange Money', 'Orange Money'), ('Visa', 'Visa')], help_text='Auto Generated', max_length=500, null=True, verbose_name='Payment Method')),
                ('installment', models.CharField(blank=True, choices=[('1st Installment', '1st Installment'), ('2nd Installment', '2nd Installment'), ('3rd Installment', '3rd Installment'), ('4th Installment', '4th Installment'), ('5th Installment', '5th Installment'), ('6th Installment', '6th Installment'), ('7th Installment', '7th Installment'), ('8th Installment', '8th Installment'), ('9th Installment', '9th Installment')], help_text='Choose from List', max_length=500, null=True, verbose_name='Installment #')),
                ('bank_name', models.CharField(blank=True, default='', help_text='If Payment is Bank', max_length=500, null=True, verbose_name='Bank Name')),
                ('account_number', models.CharField(blank=True, default='', help_text='If Payment is Bank', max_length=500, null=True, verbose_name='Bank Name')),
                ('employee', models.CharField(blank=True, default='', help_text='e.g Jane', max_length=500, null=True, verbose_name='Employee')),
                ('invoice_id', models.ForeignKey(blank=True, help_text='e.g Meno', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.salesinvoices', verbose_name='Invoice Id')),
            ],
            options={
                'verbose_name': 'Payments',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
