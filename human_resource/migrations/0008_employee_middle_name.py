# Generated by Django 4.2.3 on 2023-07-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0007_remove_employee_sub_deparment'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='Middle Name (optional)'),
        ),
    ]
