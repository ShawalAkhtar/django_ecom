# Generated by Django 4.0.1 on 2022-01-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220120_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='staticfiles/img'),
        ),
    ]
