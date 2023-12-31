# Generated by Django 4.2.3 on 2023-07-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0002_department_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='startdate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='cities',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='department',
            name='startdate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='department',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='role',
            name='startdate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='role',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
    ]
