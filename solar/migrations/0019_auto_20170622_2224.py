# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0018_price_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price_item',
            old_name='head',
            new_name='power',
        ),
        migrations.RemoveField(
            model_name='price_item',
            name='text',
        ),
        migrations.AddField(
            model_name='price_item',
            name='price',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]