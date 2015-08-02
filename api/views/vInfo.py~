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
    pass

def getComment(request, comment_id, access_token):
    pass

def getStar(request, star_id, access_token):
    pass

def getRecommend(request, recommend_id, access_token):
    pass
