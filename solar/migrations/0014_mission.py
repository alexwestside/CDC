# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0013_circle_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mission',
                'verbose_name': '\u041c\u0438\u0441\u0441\u0438\u044f',
                'verbose_name_plural': '\u041c\u0438\u0441\u0441\u0438\u044f',
            },
        ),
    ]
