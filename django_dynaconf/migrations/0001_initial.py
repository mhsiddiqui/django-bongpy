# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-02-15 20:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Key can only contains uppercase letters, numbers and _', regex=b'[A-Z\\d_]+')])),
                ('description', models.CharField(blank=True, help_text='Description of configuration', max_length=200, null=True)),
                ('value', models.TextField()),
                ('type', models.CharField(choices=[(b'string', 'String'), (b'number', 'Number'), (b'boolean', 'Boolean'), (b'json', 'Json'), (b'date', 'Date'), (b'datetime', 'Datetime'), (b'time', 'Time')], default=b'string', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]