# Generated by Django 4.2.3 on 2023-07-09 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0009_delete_role_jobposition_sub_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobposition',
            options={'ordering': ['job_position_name'], 'verbose_name': 'Job Position', 'verbose_name_plural': 'Job Positions'},
        ),
        migrations.AddField(
            model_name='department',
            name='manager_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='configs_settings.manager'),
        ),
        migrations.AddField(
            model_name='manager',
            name='work_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.cities', verbose_name='Country'),
        ),
        migrations.CreateModel(
            name='WorkLoacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100, verbose_name='Manager Name')),
                ('startdate', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.cities', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Work Loacation',
                'verbose_name_plural': 'Work Loacations',
                'ordering': ['location_name'],
            },
        ),
    ]
