# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeform_viz', '0002_auto_20160918_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jhapp',
            name='cv',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]