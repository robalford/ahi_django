# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20170212_1348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
    ]