# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-25 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0025_articles_general'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Adres',
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(blank=True, max_length=1000, null=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('img_back', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'db_table': 'Contact',
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solar.Contacts')),
            ],
            options={
                'db_table': 'Email',
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solar.Contacts')),
            ],
            options={
                'db_table': 'Phone',
                'verbose_name': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d',
                'verbose_name_plural': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='adres',
            name='contact_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='solar.Contacts'),
        ),
    ]
