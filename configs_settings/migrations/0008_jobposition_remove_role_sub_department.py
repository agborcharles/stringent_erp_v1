# Generated by Django 4.2.3 on 2023-07-09 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs_settings', '0007_manager_alter_role_options_alter_role_role_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_position_name', models.CharField(max_length=125, verbose_name='Job Position')),
                ('startdate', models.DateField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
                'ordering': ['job_position_name'],
            },
        ),
        migrations.RemoveField(
            model_name='role',
            name='sub_department',
        ),
    ]