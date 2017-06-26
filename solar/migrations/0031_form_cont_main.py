# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0030_articles_facebook_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_cont_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('head_preview', models.CharField(blank=True, max_length=1000, null=True)),
                ('text_prview', models.CharField(blank=True, max_length=2000, null=True)),
                ('head_ans', models.CharField(blank=True, max_length=1000, null=True)),
                ('text_ans', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'Form_cont',
                'verbose_name': '\u0422\u0435\u043a\u0441\u0442_\u0444\u043e\u0440\u043c\u044b',
                'verbose_name_plural': '\u0422\u0435\u043a\u0441\u0442\u044b_\u0444\u043e\u0440\u043c',
            },
        ),
    ]