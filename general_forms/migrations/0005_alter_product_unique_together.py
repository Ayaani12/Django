# Generated by Django 5.0.7 on 2024-07-18 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_forms', '0004_alter_product_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
