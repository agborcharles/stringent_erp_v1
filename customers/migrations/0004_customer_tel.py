# Generated by Django 4.2.3 on 2023-07-17 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_customer_payment_terms_alter_customer_customer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tel',
            field=models.CharField(blank=True, help_text='Phone Number of Contact Person', max_length=15, null=True, verbose_name='Tel'),
        ),
    ]