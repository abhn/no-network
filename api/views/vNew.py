from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api import models
import json

@csrf_exempt
def newPost(request):
    if(request.method == "POST"):
        if(request.is_ajax):
            nPost = json.loads(request.body)
            db_posts = models.ApiPosts()
            db_posts.post_created = None
            db_posts.post_updated = None
            db_posts.post_data = nPost["post_data"]

            access_t = nPost["access_token"]
            app_id = nPost["application_id"]
            if(models.ApiAccessToken.objects.all().filter(access_token=access_t).exists()):
                db_access = models.ApiAccessToken.objects.get(access_token=access_t)
                db_posts.post_source_id = db_access.user_id
                db_posts.save()
                return HttpResponse(json.dumps({"message":"successfully created post"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error":"authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")

def newComment(request):
    if(request.method == "POST"):
        if(request.is_ajax):
            nComment = json.loads(request.body)
            db_comments = models.ApiComments()
            db_comments.comment_created = None
            db_comments.comment_updated = None
            db_comment.comment_data = nComment['comment_data']
            access_t = nComment['access_token']
            app_id = nComment['app_id']
            if(models.ApiAccessToken.objects.all().filter(access_token=access_t).exists()):
                db_access = models.ApiAccessToken.objects.get(access_token=access_t)
                db_comments.comment_source_id = db_access.user_id
                db_comments.save()
                return HttpResponse(json.dumps({"message":"successfully created comment"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error":"authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")

def newStar(request):
    if(request.method == "POST"):
        if(request.is_ajax):
            nStar = json.loads(request.body)
            db_star = models.ApiStars()
            db_star.star_updated = None
            db_star.star_destination_id = nStar['destination_id']
            access_t = nComment['access_token']
            app_id = nComment['app_id']
            if(models.ApiAccessToken.objects.all().filter(access_token=access_t).exists()):
                db_access = models.ApiAccessToken.objects.get(access_token=access_t)
                db_star.star_source_id = db_access.user_id
                db_star.save()
                return HttpResponse(json.dumps({"message":"successfully stared"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error":"authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")

def newRecommend(request):
    if(request.method == "POST"):
        if(request.is_ajax):
            nRecommend = json.loads(request.body)
            db_recommend = models.ApiRecommends()
            db_recommend.recommend_updated = None
            db_recommend.recommend.recommend_destination_id = nRecommend['destination_id']
            access_t = nComment['access_token']
            app_id = nComment['app_id']
            if(models.ApiAccessToken.objects.all().filter(access_token=access_t).exists()):
                db_access = models.ApiAccessToken.objects.get(access_token=access_t)
                db_recommend.recommend_source_id = db_access.user_id
                db_recommend.save()
                return HttpResponse(json.dumps({"message":"successfully recommended"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"error":"authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")
            
            
