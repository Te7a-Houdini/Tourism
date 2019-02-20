# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-20 14:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Cities')),
            ],
        ),
        migrations.CreateModel(
            name='HotelReservationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('no_of_adults', models.IntegerField()),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Hotel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
