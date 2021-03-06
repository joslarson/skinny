# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_verb',
            field=models.CharField(blank=True, default='Updated', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='version',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.TextField(blank=True),
        ),
    ]
