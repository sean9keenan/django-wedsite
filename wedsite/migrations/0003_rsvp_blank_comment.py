# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-16 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedsite', '0002_rsvp_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='comment',
            field=models.TextField(blank=True, help_text='RSVP Comment'),
        ),
    ]