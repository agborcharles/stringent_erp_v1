# Generated by Django 4.2.3 on 2023-07-09 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0011_workloacation_address_alter_manager_work_location_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkLoacation',
            new_name='WorkLocation',
        ),
        migrations.AlterModelOptions(
            name='worklocation',
            options={'ordering': ['location_name'], 'verbose_name': 'Work Location', 'verbose_name_plural': 'Work Locations'},
        ),
    ]
