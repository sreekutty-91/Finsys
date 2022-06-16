# Generated by Django 3.0.5 on 2022-06-16 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20220616_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetable',
            name='product',
        ),
        migrations.AddField(
            model_name='pricetable',
            name='productname',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pricetable',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
