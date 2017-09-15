# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-04 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0003_remove_orderitem_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='city', to='shop.City'),
            preserve_default=False,
        ),
    ]