# Generated by Django 4.2.3 on 2023-07-07 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human_resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='human_resource.department'),
        ),
    ]