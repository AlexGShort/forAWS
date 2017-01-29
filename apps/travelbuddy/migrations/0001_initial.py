# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('participant', models.ManyToManyField(related_name='participantToTrip', to='login.User')),
            ],
        ),
    ]
