# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-13 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Car_Rental', '0009_auto_20190213_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_rental',
            name='location_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Locations'),
        ),
    ]
