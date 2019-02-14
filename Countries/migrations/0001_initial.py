
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0002_user_blk_flg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('city_ID', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50)),
                ('local_name', models.CharField(max_length=3)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
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
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('exper_ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('city_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Cities')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.User')),
            ],
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('location_ID', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('city_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Cities')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='exper_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Experience'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.User'),
        ),
        migrations.AddField(
            model_name='cities',
            name='country_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.Countries'),
        ),
    ]
