# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CocTime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='armys',
            name='cost_black_water',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='armys',
            name='cost_water',
            field=models.IntegerField(default=0),
        ),
    ]
