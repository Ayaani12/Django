# Generated by Django 5.0.7 on 2024-07-19 01:14

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_invoiceentrylineproduct_amount_after_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceentrylineproduct',
            name='amount_after_tax',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoiceentrylineproduct',
            name='amount_before_tax',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
