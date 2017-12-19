# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 21:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 29, 21, 38, 17, 288182, tzinfo=utc), verbose_name='Date de parution'),
        ),
        migrations.AlterField(
            model_name='article',
            name='urlGitHub',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de parution'),
        ),
    ]