# Generated by Django 4.2.1 on 2023-10-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_remove_basket_id_alter_basket_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="products_images"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]