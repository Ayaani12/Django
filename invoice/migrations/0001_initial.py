# Generated by Django 5.0.7 on 2024-07-18 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Journal_Entries', '0021_customer_store_vendor_store'),
        ('general_forms', '0002_product_store_service_store'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Journal_Entries.customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceEntryLineProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('taxable', models.BooleanField(default=False)),
                ('gst_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('amount_after_tax', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('invoice_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoiceentry')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_forms.product')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceEntryLineService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('taxable', models.BooleanField(default=False)),
                ('gst_percentage', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('amount_after_tax', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('invoice_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoiceentry')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_forms.service')),
            ],
        ),
    ]
