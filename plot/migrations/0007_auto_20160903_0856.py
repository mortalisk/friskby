# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-03 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot', '0006_auto_20160706_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='tag',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
