# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0002_auto_20170618_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='first',
            field=models.BooleanField(default=False),
        ),
    ]
