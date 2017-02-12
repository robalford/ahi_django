# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20170212_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('photo', models.ImageField(upload_to='project_photos/')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandingPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='project_photos/')),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='credit',
            new_name='photo_credit',
        ),
        migrations.RemoveField(
            model_name='project',
            name='orientation',
        ),
    ]
