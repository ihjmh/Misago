# Generated by Django 1.9.7 on 2016-07-17 02:05
from __future__ import unicode_literals

from django.db import migrations, models

import misago.users.models.user


class Migration(migrations.Migration):

    dependencies = [
        ('misago_users', '0004_default_ranks'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', misago.users.models.user.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='rank',
            name='roles',
            field=models.ManyToManyField(blank=True, to='misago_acl.Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups'
            ),
        ),
    ]
