# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-20 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Car_Rental', '0001_initial'),
        ('Countries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_reservation',
            name='location_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Countries.Locations'),
        ),
    ]
