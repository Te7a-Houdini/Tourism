# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-13 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20190213_1801'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([]),
        ),
    ]
