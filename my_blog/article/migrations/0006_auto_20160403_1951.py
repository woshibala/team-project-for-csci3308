# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-03 19:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20160331_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='data_time',
        ),
        migrations.AddField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 19, 51, 9, 978997, tzinfo=utc)),
        ),
    ]
