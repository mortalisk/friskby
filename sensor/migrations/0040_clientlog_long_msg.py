# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0039_clientlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlog',
            name='long_msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
