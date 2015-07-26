# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150725_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiuseradvanced',
            name='user_advanced_id',
        ),
        migrations.AlterField(
            model_name='apiuseradvanced',
            name='user_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
