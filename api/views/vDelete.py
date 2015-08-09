from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api import models
import json

@csrf_exempt
def user(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                models.ApiPosts.objects.filter(post_source_id=nData['user_id']).delete()
                models.ApiComments.objects.filter(comment_source_id=nData['user_id']).delete()
                models.ApiRecommends.objects.filter(recommend_source_id=nData['user_id']).delete()
                models.ApiStars.objects.filter(star_source_id=nData['user_id']).delete()
                models.ApiAccessToken.objects.filter(user_id=nData['user_id']).delete()
                models.ApiUserBasic.objects.filter(user_id=nData['user_id']).delete()
                models.ApiUserAdvanced.objects.filter(user_id=nData['user_id']).delete()
                return HttpResponse(json.dumps({"message": "user deleted successfully"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "POST request expected"}), content_type="application/json")

@csrf_exempt
def post(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                models.ApiPosts.objects.filter(post_id=nData['post_id']).delete()
                return HttpResponse(json.dumps({"message": "post deleted successfully"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "POST request expected"}), content_type="application/json")

@csrf_exempt
def comment(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                models.ApiComments.objects.filter(comment_id=nData['comment_id']).delete()
                return HttpResponse(json.dumps({"message": "comment deleted successfully"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "POST request expected"}), content_type="application/json")

@csrf_exempt
def star(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                models.ApiStars.objects.filter(star_id=nData['star_id']).delete()
                return HttpResponse(json.dumps({"message": "star deleted successfully"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "POST request expected"}), content_type="application/json")

@csrf_exempt
def recommend(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                models.ApiRecommends.objects.filter(recommend_id=nData['recommend_id']).delete()
                return HttpResponse(json.dumps({"message": "recommend deleted successfully"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    return HttpResponse(json.dumps({"message": "POST request expected"}), content_type="application/json")
