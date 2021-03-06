# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0038_device_locked'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('msg', models.CharField(max_length=256)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.Device')),
            ],
        ),
    ]
