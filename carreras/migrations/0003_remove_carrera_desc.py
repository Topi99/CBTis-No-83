# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0002_auto_20170331_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrera',
            name='desc',
        ),
    ]