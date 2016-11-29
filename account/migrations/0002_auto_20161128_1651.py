# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/%Y/%m/%d', verbose_name='头像图像'),
        ),
    ]
