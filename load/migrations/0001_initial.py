# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('time', models.DateTimeField(verbose_name='generate time')),
                ('filename', models.CharField(max_length=80)),
                ('fullname', models.CharField(max_length=102)),
            ],
            options={
                'ordering': ['filename'],
            },
        ),
        migrations.CreateModel(
            name='RawCsv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('time', models.DateTimeField(verbose_name='upload time')),
                ('filename', models.CharField(max_length=80)),
                ('fullname', models.CharField(max_length=102)),
            ],
            options={
                'ordering': ['filename'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('time', models.DateTimeField(verbose_name='generate time')),
                ('data', models.CharField(max_length=80)),
                ('date', models.DateField(verbose_name='date')),
                ('prefix', models.CharField(max_length=122)),
                ('n', models.IntegerField(verbose_name='.name line count')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('holiday', models.IntegerField(default=0, verbose_name='holiday')),
                ('maxTemp', models.IntegerField(default=0, verbose_name='maxTemp')),
                ('minTemp', models.IntegerField(default=0, verbose_name='minTemp')),
                ('typeDay', models.IntegerField(default=0, verbose_name='typeDay')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
