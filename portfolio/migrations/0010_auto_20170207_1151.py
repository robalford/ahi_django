# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20170205_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
