# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='cuerpo',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(blank=True, choices=[('noticia', 'Noticia'), ('info_academica', 'Información Académica'), ('institucion', 'Nuestra Institución'), ('extraescolares', 'Actividades Extraescolares'), ('docentes_escolares', 'Servicios Docentes y Escolares')], default='noticia', max_length=20, null=True),
        ),
    ]
