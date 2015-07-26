from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from api import models
import json, hashlib, uuid

def register(request):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            first_name = register.cleaned_data['first_name']
            last_name = register.cleaned_data['last_name']
            user_name = register.cleaned_data['user_name']
            user_email = register.cleaned_data['user_email']
            user_password = register.cleaned_data['user_password']
            birth_date = register.cleaned_data['birth_date']
            gender = register.cleaned_data['gender']
            location = register.cleaned_data['location']

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

            return HttpResponse(json.dumps({"message": "successfully created user"}), content_type="application/json")
            
    else:
        return HttpResponse(json.dumps({"error":"POST request expected"}), content_type="application/json")
