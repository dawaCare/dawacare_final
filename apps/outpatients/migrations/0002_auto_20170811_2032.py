# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outpatients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='medication_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.MedicationCategory'),
        ),
    ]
