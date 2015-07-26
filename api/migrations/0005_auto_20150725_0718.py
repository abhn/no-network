# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150725_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiaccesstoken',
            name='application_id',
            field=models.CharField(max_length=128),
        ),
    ]
