# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150725_0605'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiMessages',
            fields=[
                ('message_id', models.AutoField(serialize=False, primary_key=True)),
                ('message_source_id', models.IntegerField()),
                ('message_destination_id', models.IntegerField()),
                ('message_timestamp', models.DateTimeField(auto_now=True)),
                ('message_text', models.TextField()),
            ],
            options={
                'db_table': 'api_messages',
            },
        ),
        migrations.AddField(
            model_name='apiaccesstoken',
            name='token_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 25, 6, 23, 44, 422838, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apicomments',
            name='comment_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='apicomments',
            name='comment_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apiposts',
            name='post_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='apiposts',
            name='post_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apirecommends',
            name='recommend_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apistars',
            name='star_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
