from django.conf.urls import url
from api import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url('^(?P<id>[0-9]+)/$', views.user_info, name='user_info'),
    url('^register/$', views.vRegister.register, name='register'),
    url('^login/$', views.vLogin.login, name='login'),
    url('^new/post/$', views.vNew.newPost, name='newpost')
]
