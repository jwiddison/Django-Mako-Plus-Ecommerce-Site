# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
