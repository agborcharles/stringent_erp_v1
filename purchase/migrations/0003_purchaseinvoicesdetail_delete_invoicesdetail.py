# Generated by Django 4.2.3 on 2023-07-13 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_reorder_level'),
        ('purchase', '0002_purchaseinvoices_invoicesdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseInvoicesDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('cost_price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, null=True, verbose_name='Cost Price')),
                ('total_at_cost', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchase.purchaseinvoices', verbose_name='Invoice Id')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='Product Name')),
            ],
            options={
                'verbose_name': 'Purchase Invoices Items',
                'verbose_name_plural': 'Purchase Invoices Items',
            },
        ),
        migrations.DeleteModel(
            name='InvoicesDetail',
        ),
    ]
