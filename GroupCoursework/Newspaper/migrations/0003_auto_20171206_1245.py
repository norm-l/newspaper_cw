# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-06 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newspaper', '0002_auto_20171206_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]