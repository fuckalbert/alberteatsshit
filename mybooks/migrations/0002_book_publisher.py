# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-02 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]