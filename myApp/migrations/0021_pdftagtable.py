# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_userpreviewtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfTagTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdfID', models.CharField(max_length=40)),
                ('Tag', models.CharField(max_length=30)),
            ],
        ),
    ]