# Generated by Django 4.2.3 on 2023-07-13 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_reorder_level'),
        ('storage_location', '0001_initial'),
        ('purchase', '0003_purchaseinvoicesdetail_delete_invoicesdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseinvoices',
            name='storage_location',
            field=models.ForeignKey(blank=True, help_text='e.g WareHouse Name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage_location.storage', verbose_name='WareHouse'),
        ),
        migrations.AlterField(
            model_name='purchaseinvoicesdetail',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase.purchaseinvoices', verbose_name='Purchase Invoice Id'),
        ),
        migrations.AlterField(
            model_name='purchaseinvoicesdetail',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='purchaseinvoicesdetail',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='Quantity'),
        ),
    ]
