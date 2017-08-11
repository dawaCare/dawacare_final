# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outpatients', '0002_auto_20170811_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='quarter',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='emergencycontact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='address',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='outpatient',
            name='address',
        ),
        migrations.AddField(
            model_name='doctor',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.City'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Quarter'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.City'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Quarter'),
        ),
        migrations.AddField(
            model_name='facility',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='facility',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='facility',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.City'),
        ),
        migrations.AddField(
            model_name='facility',
            name='quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Quarter'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 1'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Address Line 2'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.City'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Quarter'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='doctor',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.District'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Region'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.District'),
        ),
        migrations.AddField(
            model_name='emergencycontact',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Region'),
        ),
        migrations.AddField(
            model_name='facility',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.District'),
        ),
        migrations.AddField(
            model_name='facility',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Region'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.District'),
        ),
        migrations.AddField(
            model_name='outpatient',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outpatients.Region'),
        ),
    ]
