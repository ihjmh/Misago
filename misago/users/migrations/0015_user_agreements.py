# Generated by Django 1.11.15 on 2018-08-16 17:29
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misago_users', '0014_datadownload'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='agreements',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=list, size=None),
        ),
    ]
