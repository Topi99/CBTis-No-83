# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0005_auto_20170406_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='submodulo',
            name='horas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
