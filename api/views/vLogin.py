from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from api import models
import json, hashlib, uuid
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        login = LoginForm(request.POST)
        if login.is_valid():
            email = login.cleaned_data['user_email']
            password = login.cleaned_data['user_password']
            if(models.ApiUserBasic.objects.all().filter(user_email=email).exists() == False):
                return HttpResponse(json.dumps({"error": "email or password incorrect"}), content_type="application/json")
            
            from_db_login = models.ApiUserBasic.objects.get(user_email=email)
            try:
                if(from_db_login.user_password == hashlib.sha224(password).hexdigest()):
                    access_token = models.ApiAccessToken()
                    access_token.user_id_id = from_db_login.user_id
                    access_token.application_id = str(uuid.uuid4())
                    access_token.access_token = str(uuid.uuid4())
                    resp = {"application_id": access_token.application_id, "access_token": access_token.access_token}
                    access_token.save()
                    return HttpResponse(json.dumps(resp), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"error": "email or password incorrect"}), content_type="application/json")
            except IndexError:
                return HttpResponse(json.dumps({"error": "email or password incorrect"}), content_type="application/json")
            
    else:
        return HttpResponse(json.dumps({"error": "POST request expected"}), content_type="application/json")
