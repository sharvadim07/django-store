# Generated by Django 4.2.1 on 2023-08-15 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_remove_productcategory_category_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="basket",
            name="products",
        ),
        migrations.CreateModel(
            name="ProductBasket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "basket",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.basket",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
