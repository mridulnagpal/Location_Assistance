# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-14 19:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location_assist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savesettings',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
