# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-26 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solar', '0031_form_cont_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form_cont_main',
            old_name='text_prview',
            new_name='text_preview',
        ),
        migrations.RemoveField(
            model_name='form_cont_main',
            name='head_ans',
        ),
    ]
