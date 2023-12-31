# Generated by Django 4.2.3 on 2023-07-08 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0007_manager_alter_role_options_alter_role_role_name'),
        ('human_resource', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.role', verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='configs_settings.manager', verbose_name='Manager'),
        ),
    ]
