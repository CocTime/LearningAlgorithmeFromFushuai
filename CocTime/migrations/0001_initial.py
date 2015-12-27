# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armys',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField(default=1, max_length=20)),
                ('numbers', models.IntegerField(default=0, max_length=200)),
                ('time', models.IntegerField()),
            ],
        ),
    ]
