from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from api import models
import json

@csrf_exempt
def error404(request):
    message = ({"error":"404", "message":"resource not found"})
    return HttpResponse(json.dumps(message), content_type="application/json")

def error500(request):
    message = ({"error":"500", "message":"internal server error"})
    return HttpResponse(json.dumps(message), content_type="application/json")

def error403(request):
    message = ({"error":"403", "message":"permission denied"})
    return HttpResponse(json.dumps(message), content_type="application/json")

def error400(request):
    message = ({"error":"400", "message":"bad request"})
    return HttpResponse(json.dumps(message), content_type="application/json")
