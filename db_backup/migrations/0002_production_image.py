# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import scratch_api.models
import scratch_api.storage


class Migration(migrations.Migration):

    dependencies = [
        ('scratch_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='image',
            field=models.ImageField(null=True, storage=scratch_api.storage.OverwriteStorage(), upload_to=scratch_api.models.get_upload_path),
        ),
    ]
