# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAccessToken',
            fields=[
                ('access_token_id', models.AutoField(serialize=False, primary_key=True)),
                ('application_id', models.IntegerField()),
                ('access_token', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'api_access_token',
            },
        ),
        migrations.CreateModel(
            name='ApiComments',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('comment_created', models.DateTimeField()),
                ('comment_updated', models.DateTimeField()),
                ('comment_data', models.TextField()),
            ],
            options={
                'db_table': 'api_comments',
            },
        ),
        migrations.CreateModel(
            name='ApiPosts',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('post_created', models.DateTimeField()),
                ('post_updated', models.DateTimeField()),
                ('post_data', models.TextField()),
            ],
            options={
                'db_table': 'api_posts',
            },
        ),
        migrations.CreateModel(
            name='ApiRecommends',
            fields=[
                ('recommend_id', models.AutoField(serialize=False, primary_key=True)),
                ('recommend_updated', models.DateTimeField()),
                ('recommend_destination_id', models.ForeignKey(to='api.ApiPosts')),
            ],
            options={
                'db_table': 'api_recommends',
            },
        ),
        migrations.CreateModel(
            name='ApiStars',
            fields=[
                ('star_id', models.AutoField(serialize=False, primary_key=True)),
                ('star_updated', models.DateTimeField()),
                ('star_destination_id', models.ForeignKey(to='api.ApiPosts')),
            ],
            options={
                'db_table': 'api_stars',
            },
        ),
        migrations.CreateModel(
            name='ApiUserAdvanced',
            fields=[
                ('user_advanced_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_fname', models.CharField(max_length=32)),
                ('user_lname', models.CharField(max_length=32)),
                ('user_sex', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')])),
                ('user_birth_date', models.DateField()),
                ('user_location', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'api_user_advanced',
            },
        ),
        migrations.CreateModel(
            name='ApiUserBasic',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=32)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'api_user_basic',
            },
        ),
        migrations.AddField(
            model_name='apiuseradvanced',
            name='user_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
        migrations.AddField(
            model_name='apistars',
            name='star_source_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
        migrations.AddField(
            model_name='apirecommends',
            name='recommend_source_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
        migrations.AddField(
            model_name='apiposts',
            name='post_source_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
        migrations.AddField(
            model_name='apicomments',
            name='comment_destination_id',
            field=models.ForeignKey(to='api.ApiPosts'),
        ),
        migrations.AddField(
            model_name='apicomments',
            name='comment_source_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
        migrations.AddField(
            model_name='apiaccesstoken',
            name='user_id',
            field=models.ForeignKey(to='api.ApiUserBasic'),
        ),
    ]
