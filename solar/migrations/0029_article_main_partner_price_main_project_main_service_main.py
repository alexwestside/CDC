# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0028_auto_20170625_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('img_back', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Article_main',
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0441\u0442\u0430\u0442\u0435\u0439',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0441\u0442\u0430\u0442\u0435\u0439',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Partner',
                'verbose_name': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='Price_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('img_back', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Price_main',
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0446\u0435\u043d',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0446\u0435\u043d',
            },
        ),
        migrations.CreateModel(
            name='Project_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('img_back', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Project_main',
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Service_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('img_back', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Service_main',
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0443\u0441\u043b\u0443\u0433\u0438',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0447\u043a\u0430_\u0443\u0441\u043b\u0443\u0433\u0438',
            },
        ),
    ]
