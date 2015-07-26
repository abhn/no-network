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
