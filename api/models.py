from __future__ import unicode_literals

from django.db import models


class ApiComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_source_id = models.ForeignKey('ApiUserBasic')
    comment_destination_id = models.ForeignKey('ApiPosts')
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(auto_now=True)
    comment_data = models.TextField()

    class Meta:
        #managed = False
        db_table = 'api_comments'


class ApiPosts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_source_id = models.ForeignKey('ApiUserBasic')
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)
    post_data = models.TextField()

    class Meta:
        #managed = False
        db_table = 'api_posts'


class ApiRecommends(models.Model):
    recommend_id = models.AutoField(primary_key=True)
    recommend_source_id = models.ForeignKey('ApiUserBasic')
    recommend_destination_id = models.ForeignKey('ApiPosts')
    recommend_updated = models.DateTimeField(auto_now=True)

    class Meta:
        #managed = False
        db_table = 'api_recommends'


class ApiStars(models.Model):
    star_id = models.AutoField(primary_key=True)
    star_updated = models.DateTimeField(auto_now=True)
    star_destination_id = models.ForeignKey('ApiPosts')
    star_source_id = models.ForeignKey('ApiUserBasic')

    class Meta:
        #managed = False
        db_table = 'api_stars'


class ApiUserBasic(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=128)

    class Meta:
        #managed = False
        db_table = 'api_user_basic'
        
class ApiUserAdvanced(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=32)
    user_lname = models.CharField(max_length=32)
    user_sex_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified'),
    )
    user_sex = models.CharField(max_length=1, choices=user_sex_choice)
    user_birth_date = models.DateField()
    user_location = models.CharField(max_length=64)


    class Meta:
        db_table = 'api_user_advanced'

class ApiAccessToken(models.Model):
    access_token_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('ApiUserBasic')
    application_id = models.CharField(max_length=128)
    access_token = models.CharField(max_length=128)
    token_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'api_access_token'

class ApiMessages(models.Model):
    message_id = models.AutoField(primary_key=True)
    message_source_id = models.IntegerField()
    message_destination_id = models.IntegerField()
    message_timestamp = models.DateTimeField(auto_now=True)
    message_text = models.TextField()

    class Meta:
        db_table = 'api_messages'
