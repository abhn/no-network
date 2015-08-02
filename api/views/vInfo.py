from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api import models
import json

@csrf_exempt
def getUser(request, user_id, access_token):
    db_user_basic = models.ApiUserBasic()
    db_user_advanced = models.ApiUserAdvanced()
    db_access = models.ApiAccessToken()

    if(models.ApiUserBasic.objects.all().filter(user_id=user_id).exists()):
        if(models.ApiAccessToken.objects.all().filter(access_token=access_token).exists()):
            data = ({"username":models.ApiUserBasic.objects.get(user_id=user_id).user_name, "email":models.ApiUserBasic.objects.get(user_id=user_id).user_email, "first_name":models.ApiUserAdvanced.objects.get(user_id=user_id).user_fname, "last_name":models.ApiUserAdvanced.objects.get(user_id=user_id).user_lname, "gender":models.ApiUserAdvanced.objects.get(user_id=user_id).user_sex, "location":models.ApiUserAdvanced.objects.get(user_id=user_id).user_location})
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"authentication is required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"userID is orphaned"}), content_type="application/json")
    
def getPost(request, post_id, access_token):
    db_posts = models.ApiPosts()
    db_access = models.ApiAccessToken()
    if(models.ApiPosts.objects.all().filter(post_id=post_id).exists()):
        if(models.ApiAccessToken.objects.all().filter(access_token=access_token).exists()):
            data = ({"created":models.ApiPosts.objects.get(post_id=post_id).post_created, "updated":models.ApiPosts.objects.get(post_id=post_id).post_updated, "data":models.ApiPosts.objects.get(post_id=post_id).post_data, "source":models.ApiPosts.objects.get(post_id=post_id).post_source_id})
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"authentication is required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"postID is orphaned"}), content_type="application/json")

def getComment(request, comment_id, access_token):
    db_comments = models.ApiComments()
    db_access = models.ApiAccessToken()
    if(models.ApiPosts.objects.all().filter(post_id=comment_id).exists()):
        if(models.ApiAccessToken.objects.all().filter(access_token=access_token).exists()):
            data = ({"created":models.ApiComments.objects.get(comment_id=comment_id).comment_created, "updated":models.ApiComments.objects.get(comment_id=comment_id).comment_updated, "data":models.ApiPosts.objects.get(post_id=post_id).post_data, "source":models.ApiComments.objects.get(comment_id=comment_id).comment_source_id, "destination":models.ApiComments.objects.get(comment_id=comment_id).comment_destination_id })
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"authentication is required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"commentID is orphaned"}), content_type="application/json")

def getStar(request, star_id, access_token):
    db_stars = models.ApiStars()
    db_access = models.ApiAccessToken()
    if(models.ApiPosts.objects.all().filter(star_id=star_id).exists()):
        if(models.ApiAccessToken.objects.all().filter(access_token=access_token).exists()):
            data = ({"updated":models.ApiStars.objects.get(star_id=star_id).star_updated, "source":models.ApiStars.objects.get(star_id=star_id).star_source_id, "destination":models.ApiStars.objects.get(star_id=star_id).star_destination_id})
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"authentication is required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"starID is orphaned"}), content_type="application/json")

def getRecommend(request, recommend_id, access_token):
    db_recommends = models.ApiRecommends()
    db_access = models.ApiAccessToken()
    if(models.ApiPosts.objects.all().filter(recommend_id=recommend_id).exists()):
        if(models.ApiAccessToken.objects.all().filter(access_token=access_token).exists()):
            data = ({"updated":models.ApiRecommends.objects.get(recommend_id=recommend_id).recommend_updated, "source":models.ApiRecommend.objects.get(recommend_id=recommend_id).recommend_source_id, "destination":models.ApiRecommends.objects.get(recommend_id=recommend_id).recommend_destination_id})
            return HttpResponse(json.dumps(data), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"error":"authentication is required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"recommendID is orphaned"}), content_type="application/json")
