# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-13 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0006_auto_20190213_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_rental',
            name='location_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Locations'),
        ),
    ]
