# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-20 06:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160420_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 6, 37, 45, 545724, tzinfo=utc)),
        ),
    ]