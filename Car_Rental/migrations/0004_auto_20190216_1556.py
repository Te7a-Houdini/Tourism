# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-16 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0003_auto_20190216_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_rental',
            name='location_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Countries.Locations'),
        ),
    ]
