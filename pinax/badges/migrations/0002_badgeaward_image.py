# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-22 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_badges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgeaward',
            name='image',
            field=models.ImageField(default='badges/badges1.png', upload_to='badges/'),
        ),
    ]
