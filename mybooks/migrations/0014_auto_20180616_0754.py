# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0013_auto_20180616_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='About game'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.SmallIntegerField(choices=[(0, 'fantasy'), (1, 'action'), (2, 'adventure'), (3, 'strategy'), (4, 'horror'), (5, 'rpg'), (6, 'sport')], default=0),
        ),
    ]
