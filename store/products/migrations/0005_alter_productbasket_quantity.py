# Generated by Django 4.2.1 on 2023-08-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_remove_basket_products_productbasket"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productbasket",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]
