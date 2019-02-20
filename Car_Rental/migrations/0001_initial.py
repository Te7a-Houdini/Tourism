# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-19 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('pick_up', models.CharField(max_length=200, null=True)),
                ('drop_off', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
