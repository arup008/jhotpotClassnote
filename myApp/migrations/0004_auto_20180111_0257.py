# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_course_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_table',
            old_name='depertment',
            new_name='department',
        ),
    ]
