# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-28 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0004_auto_20160728_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailer',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='trailer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='trailer',
            name='width_field',
        ),
    ]
