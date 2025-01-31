# Generated by Django 5.0.7 on 2024-07-19 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_rename_amount_invoiceentrylineproduct_amount_before_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceentrylineproduct',
            name='amount_after_tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='invoiceentrylineproduct',
            name='amount_before_tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
