# Generated by Django 3.0.5 on 2022-06-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_manufacture_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacture',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='manufacture',
            name='noninventory',
        ),
        migrations.AddField(
            model_name='manufacture',
            name='amount',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='price',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='productname',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]