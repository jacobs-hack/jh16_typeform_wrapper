# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-11 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typeform_viz', '0008_auto_20160919_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='jhapp',
            name='slack_invite',
            field=models.BooleanField(default=False),
        ),
    ]
