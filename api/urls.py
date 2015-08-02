from django.conf.urls import url
from api import views

urlpatterns = [
   # url('^register/$', views.vRegister.register, name='register'),
   # url('^login/$', views.vLogin.login, name='login'),
    
    url('^new/post/$', views.vNew.newPost, name='newpost'),
    url('^new/comment/$', views.vNew.newComment, name='newcomment'),
    url('^new/star/$', views.vNew.newStar, name='newstar'),
    url('^new/recommend/$', views.vNew.newRecommend, name='newrecommend'),
    
    url('^users/(?P<user_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getUser, name='getuser')
]
