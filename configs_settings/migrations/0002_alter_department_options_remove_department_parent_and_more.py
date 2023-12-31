# Generated by Django 4.2.3 on 2023-07-07 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Department', 'verbose_name_plural': 'Department'},
        ),
        migrations.RemoveField(
            model_name='department',
            name='parent',
        ),
        migrations.AddField(
            model_name='role',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='configs_settings.department'),
        ),
    ]
