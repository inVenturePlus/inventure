# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycustomemailuser',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='mycustomemailuser',
            name='entrepreneur',
            field=models.IntegerField(null=True),
        ),
    ]