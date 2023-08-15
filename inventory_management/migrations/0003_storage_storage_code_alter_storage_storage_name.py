# Generated by Django 4.2.3 on 2023-07-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_rename_startdate_storage_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='storage_code',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Code'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storage_name',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Storage Name'),
        ),
    ]