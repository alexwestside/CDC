# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0006_auto_20170618_1431'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '\u041f\u0440\u043e\u0435\u043a\u0442', 'verbose_name_plural': '\u041f\u0440\u043e\u0435\u0442\u043a\u044b'},
        ),
        migrations.AddField(
            model_name='project',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]
