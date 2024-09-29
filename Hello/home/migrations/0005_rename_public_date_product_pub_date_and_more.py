# Generated by Django 4.1.5 on 2024-04-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_category_remove_product_subcategory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='public_date',
            new_name='pub_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50),
        ),
    ]