# Generated by Django 5.0.7 on 2024-07-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COA', '0003_accounttypes_detailtypes_delete_coa'),
    ]

    operations = [
        migrations.CreateModel(
            name='COA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Accounts Receivable (A/R)', 'Accounts Receivable (A/R)'), ('Current Assets', 'Current Assets'), ('Bank', 'Bank'), ('Property, Plant and equipment', 'Property, Plant and equipment'), ('Long-Term Assets', 'Long-Term Assets'), ('Accounts Payable (A/P)', 'Accounts Payable (A/P)'), ('Credit Card', 'Credit Card'), ('Other Current Liabilities', 'Other Current Liabilities'), ('Long Term Liabilities', 'Long Term Liabilities'), ('Equity', 'Equity'), ('Income', 'Income'), ('Other Income', 'Other Income'), ('Cost of Goods Sold', 'Cost of Goods Sold'), ('Expenses', 'Expenses'), ('Other Expenses', 'Other Expenses')], max_length=50)),
                ('detail_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
    ]
