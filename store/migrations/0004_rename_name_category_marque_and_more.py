# Generated by Django 4.1.5 on 2023-02-27 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_cart_product_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='marque',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image_produit',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='marque',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='small_description',
            new_name='petite_description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='original_price',
            new_name='prix',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='quantité',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selling_price',
        ),
    ]
