# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-15 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_assist', '0004_auto_20161015_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savesettings',
            old_name='blouetooth',
            new_name='bluetooth',
        ),
    ]
