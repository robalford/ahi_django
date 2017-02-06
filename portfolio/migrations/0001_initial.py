# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='project_photos/')),
                ('main_photo', models.BooleanField()),
                ('credit', models.CharField(max_length=100)),
                ('caption', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True)),
                ('project', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('architect', models.CharField(max_length=100)),
                ('awards', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Project'),
        ),
    ]
