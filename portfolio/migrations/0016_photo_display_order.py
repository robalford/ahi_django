# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20170209_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='display_order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]