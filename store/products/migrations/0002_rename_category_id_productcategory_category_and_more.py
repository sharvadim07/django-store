# Generated by Django 4.2.1 on 2023-05-17 12:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="productcategory",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="productcategory",
            old_name="product_id",
            new_name="product",
        ),
    ]
