# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-14 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Countries', '0005_auto_20190213_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
