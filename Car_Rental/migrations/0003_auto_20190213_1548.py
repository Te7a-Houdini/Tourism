# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-13 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0002_car_rental_location_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_rental',
            name='location_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Locations'),
        ),
    ]
