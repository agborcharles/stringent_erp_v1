# Generated by Django 4.2.3 on 2023-07-09 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0015_delete_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branchmanager',
            name='work_location',
        ),
        migrations.AddField(
            model_name='worklocation',
            name='branch_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.branchmanager', verbose_name='Location'),
        ),
        migrations.CreateModel(
            name='DepartmentManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100, verbose_name='Branch Manager Name')),
                ('startdate', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('work_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.worklocation', verbose_name='Location')),
            ],
            options={
                'verbose_name': 'Department Manager',
                'verbose_name_plural': 'Department Managers',
                'ordering': ['manager_name'],
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='manager_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='configs_settings.departmentmanager'),
        ),
    ]
