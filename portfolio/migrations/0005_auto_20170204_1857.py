# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_project_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='main_photo',
            field=models.ImageField(default='', upload_to='main_photos/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='main_photo_credit',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
