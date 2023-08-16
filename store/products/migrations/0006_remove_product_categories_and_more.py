# Generated by Django 4.2.1 on 2023-08-16 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_alter_productbasket_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="categories",
        ),
        migrations.AlterField(
            model_name="productbasket",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="ProductCategory",
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
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.category",
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
