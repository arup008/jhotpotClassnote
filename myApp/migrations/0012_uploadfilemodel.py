# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_auto_20180117_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('CourseTeacher', models.CharField(max_length=40)),
            ],
        ),
    ]
