# Generated by Django 4.2.3 on 2023-07-08 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0005_rename_department_role_sub_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['role_name'], 'verbose_name': 'Role', 'verbose_name_plural': 'Role'},
        ),
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='role_name',
        ),
    ]
