# Generated by Django 4.2.3 on 2023-07-18 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage_location', '0001_initial'),
        ('sales', '0005_salesinvoicedetail_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoices',
            name='customer',
            field=models.ForeignKey(blank=True, help_text='e.g DS AKWA', null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage_location.storage', verbose_name='Customer'),
        ),
    ]
