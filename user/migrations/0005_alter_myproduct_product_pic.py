# Generated by Django 3.2.4 on 2023-09-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_myproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproduct',
            name='product_pic',
            field=models.ImageField(null=True, upload_to='static/product/'),
        ),
    ]
