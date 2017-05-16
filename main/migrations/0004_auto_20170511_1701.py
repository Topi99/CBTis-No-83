# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170511_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(blank=True, choices=[('extraescolares', 'Actividades Extraescolares'), ('docentes_escolares', 'Servicios Docentes y Escolares'), ('noticia', 'Noticia'), ('info_academica', 'Información Académica'), ('institucion', 'Nuestra Institución')], default='noticia', max_length=20, null=True),
        ),
    ]
