# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-19 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='blk_flg',
            field=models.BooleanField(default=False),
        ),
    ]
