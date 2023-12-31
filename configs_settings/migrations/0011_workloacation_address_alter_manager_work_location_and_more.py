# Generated by Django 4.2.3 on 2023-07-09 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0010_alter_jobposition_options_department_manager_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workloacation',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='Work Address'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='work_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.workloacation', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='workloacation',
            name='city',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.cities', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='workloacation',
            name='location_name',
            field=models.CharField(default='', max_length=100, verbose_name='Work Location'),
        ),
    ]
