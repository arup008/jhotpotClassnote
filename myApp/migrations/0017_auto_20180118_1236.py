# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_pdf_table_lastaccessed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_table',
            name='uploadDate',
            field=models.DateTimeField(),
        ),
    ]
