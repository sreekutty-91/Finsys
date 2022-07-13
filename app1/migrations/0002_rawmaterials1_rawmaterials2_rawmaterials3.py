# Generated by Django 3.0.5 on 2022-07-12 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rawmaterials3',
            fields=[
                ('rawmaterialsid', models.AutoField(primary_key=True, serialize=False, verbose_name='RAWMATERIALSID')),
                ('Type', models.CharField(blank=True, default='', max_length=255)),
                ('product16', models.CharField(blank=True, default='', max_length=255)),
                ('sku16', models.CharField(blank=True, default='', max_length=255)),
                ('qty16', models.IntegerField()),
                ('price16', models.IntegerField()),
                ('total16', models.IntegerField()),
                ('product17', models.CharField(blank=True, default='', max_length=255)),
                ('sku17', models.CharField(blank=True, default='', max_length=255)),
                ('qty17', models.IntegerField()),
                ('price17', models.IntegerField()),
                ('total17', models.IntegerField()),
                ('product18', models.CharField(blank=True, default='', max_length=255)),
                ('sku18', models.CharField(blank=True, default='', max_length=255)),
                ('qty18', models.IntegerField()),
                ('price18', models.IntegerField()),
                ('total18', models.IntegerField()),
                ('product19', models.CharField(blank=True, default='', max_length=255)),
                ('sku19', models.CharField(blank=True, default='', max_length=255)),
                ('qty19', models.IntegerField()),
                ('price19', models.IntegerField()),
                ('total19', models.IntegerField()),
                ('totalquantity3', models.CharField(blank=True, default='', max_length=255)),
                ('subtotal3', models.CharField(blank=True, default='', max_length=255)),
                ('costofcomponents3', models.CharField(blank=True, default='', max_length=255)),
                ('typeofaddnlcost3', models.CharField(blank=True, default='', max_length=255)),
                ('percentage3', models.CharField(blank=True, default='', max_length=255)),
                ('amount3', models.CharField(blank=True, default='', max_length=255)),
                ('totaladdnlcost3', models.CharField(blank=True, default='', max_length=255)),
                ('effectivecost3', models.CharField(blank=True, default='', max_length=255)),
                ('effectiverate3', models.CharField(blank=True, default='', max_length=255)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('productionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.production')),
            ],
        ),
        migrations.CreateModel(
            name='rawmaterials2',
            fields=[
                ('rawmaterialsid', models.AutoField(primary_key=True, serialize=False, verbose_name='RAWMATERIALSID')),
                ('Type', models.CharField(blank=True, default='', max_length=255)),
                ('product11', models.CharField(blank=True, default='', max_length=255)),
                ('sku11', models.CharField(blank=True, default='', max_length=255)),
                ('qty11', models.IntegerField()),
                ('price11', models.IntegerField()),
                ('total11', models.IntegerField()),
                ('product12', models.CharField(blank=True, default='', max_length=255)),
                ('sku12', models.CharField(blank=True, default='', max_length=255)),
                ('qty12', models.IntegerField()),
                ('price12', models.IntegerField()),
                ('total12', models.IntegerField()),
                ('product13', models.CharField(blank=True, default='', max_length=255)),
                ('sku13', models.CharField(blank=True, default='', max_length=255)),
                ('qty13', models.IntegerField()),
                ('price13', models.IntegerField()),
                ('total13', models.IntegerField()),
                ('product14', models.CharField(blank=True, default='', max_length=255)),
                ('sku14', models.CharField(blank=True, default='', max_length=255)),
                ('qty14', models.IntegerField()),
                ('price14', models.IntegerField()),
                ('total14', models.IntegerField()),
                ('product15', models.CharField(blank=True, default='', max_length=255)),
                ('sku15', models.CharField(blank=True, default='', max_length=255)),
                ('qty15', models.IntegerField()),
                ('price15', models.IntegerField()),
                ('total15', models.IntegerField()),
                ('totalquantity2', models.CharField(blank=True, default='', max_length=255)),
                ('subtotal2', models.CharField(blank=True, default='', max_length=255)),
                ('costofcomponents2', models.CharField(blank=True, default='', max_length=255)),
                ('typeofaddnlcost2', models.CharField(blank=True, default='', max_length=255)),
                ('percentage2', models.CharField(blank=True, default='', max_length=255)),
                ('amount2', models.CharField(blank=True, default='', max_length=255)),
                ('totaladdnlcost2', models.CharField(blank=True, default='', max_length=255)),
                ('effectivecost2', models.CharField(blank=True, default='', max_length=255)),
                ('effectiverate2', models.CharField(blank=True, default='', max_length=255)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('productionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.production')),
            ],
        ),
        migrations.CreateModel(
            name='rawmaterials1',
            fields=[
                ('rawmaterialsid', models.AutoField(primary_key=True, serialize=False, verbose_name='RAWMATERIALSID')),
                ('Type', models.CharField(blank=True, default='', max_length=255)),
                ('product5', models.CharField(blank=True, default='', max_length=255)),
                ('sku5', models.CharField(blank=True, default='', max_length=255)),
                ('qty5', models.IntegerField()),
                ('price5', models.IntegerField()),
                ('total5', models.IntegerField()),
                ('product6', models.CharField(blank=True, default='', max_length=255)),
                ('sku6', models.CharField(blank=True, default='', max_length=255)),
                ('qty6', models.IntegerField()),
                ('price6', models.IntegerField()),
                ('total6', models.IntegerField()),
                ('product7', models.CharField(blank=True, default='', max_length=255)),
                ('sku7', models.CharField(blank=True, default='', max_length=255)),
                ('qty7', models.IntegerField()),
                ('price7', models.IntegerField()),
                ('total7', models.IntegerField()),
                ('product8', models.CharField(blank=True, default='', max_length=255)),
                ('sku8', models.CharField(blank=True, default='', max_length=255)),
                ('qty8', models.IntegerField()),
                ('price8', models.IntegerField()),
                ('total8', models.IntegerField()),
                ('product9', models.CharField(blank=True, default='', max_length=255)),
                ('sku9', models.CharField(blank=True, default='', max_length=255)),
                ('qty9', models.IntegerField()),
                ('price9', models.IntegerField()),
                ('total9', models.IntegerField()),
                ('product10', models.CharField(blank=True, default='', max_length=255)),
                ('sku10', models.CharField(blank=True, default='', max_length=255)),
                ('qty10', models.IntegerField()),
                ('price10', models.IntegerField()),
                ('total10', models.IntegerField()),
                ('totalquantity1', models.CharField(blank=True, default='', max_length=255)),
                ('subtotal1', models.CharField(blank=True, default='', max_length=255)),
                ('costofcomponents1', models.CharField(blank=True, default='', max_length=255)),
                ('typeofaddnlcost1', models.CharField(blank=True, default='', max_length=255)),
                ('percentage1', models.CharField(blank=True, default='', max_length=255)),
                ('amount1', models.CharField(blank=True, default='', max_length=255)),
                ('totaladdnlcost1', models.CharField(blank=True, default='', max_length=255)),
                ('effectivecost1', models.CharField(blank=True, default='', max_length=255)),
                ('effectiverate1', models.CharField(blank=True, default='', max_length=255)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
                ('productionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.production')),
            ],
        ),
    ]
