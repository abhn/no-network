from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api import models
import json

@csrf_exempt
def user(request):
    if request.method == "POST":
        if request.is_ajax:
            nEdit = json.loads(request.body)
            db_user_basic = models.ApiUserBasic()
            db_user_advanced = models.ApiUserAdvanced()

            if(models.ApiAccessToken.objects.all().filter(user_id=nEdit['user_id']).filter(access_token=nEdit['access_token']).exists()):
                first_name = nEdit['first_name']
                last_name = nEdit['last_name']
                user_name = nEdit['user_name']
                user_email = nEdit['user_email']
                user_password = nEdit['user_password']
                birth_date = nEdit['birth_date']
                gender = nEdit['gender']
                location = nEdit['location']

                if(models.ApiUserBasic.objects.all().filter(user_email=user_email).exists() == True):
                    return HttpResponse(json.dumps({"error": "email already in use"}), content_type="application/json")
                if(models.ApiUserBasic.objects.all().filter(user_name=user_name).exists() == True):
                    return HttpResponse(json.dumps({"error": "username already in use"}), content_type="application/json")

                api_basic = models.ApiUserBasic()
            
                api_basic.user_name = user_name
                api_basic.user_email = user_email
                api_basic.user_password = hashlib.sha224(user_password).hexdigest()

                api_advanced = models.ApiUserAdvanced()
                api_advanced.user_fname = first_name
                api_advanced.user_lname = last_name
                api_advanced.user_sex = gender
                api_advanced.user_birth_date = birth_date
                api_advanced.user_location = location
                
                api_basic.save()
                api_advanced.save()

                return HttpResponse(json.dumps({"message": "successfully edited user"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")
    
@csrf_exempt
def post(request):
    if request.method == "POST":
        if request.is_ajax:
            nData = json.loads(request.body)
            if(models.ApiAccessToken.objects.all().filter(user_id=nData['user_id']).filter(access_token=nData['access_token']).exists()):
                if(models.ApiPosts.objects.all().filter(post_source_id=nData['user_id']).filter(post_id=nData['post_id']).exists()):
                    post_data = nData['data']
                    post_db = models.ApiPosts.objects.get(post_id=nData['post_id'])
                    post_db.post_data = post_data
                    post_db.save()
                    return HttpResponse(json.dumps({"message": "successfully edited post"}), content_type="application/json")
                return HttpResponse(json.dumps({"message": "post does not exist"}), content_type="application/json")
            return HttpResponse(json.dumps({"message": "authentication required to perform this action"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")
