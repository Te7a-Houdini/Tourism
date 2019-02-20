# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-19 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('city_ID', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('local_name', models.CharField(max_length=3, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_ID', models.AutoField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=50)),
                ('local_name', models.CharField(max_length=3)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('exper_ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('city_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Cities')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_ID', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('description', models.TextField()),
                ('city_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Cities')),
            ],
        ),
    ]
