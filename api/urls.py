from django.conf.urls import url
from api import views

urlpatterns = [
    url('^register/$', views.vRegister.register, name='register'),
    url('^login/$', views.vLogin.login, name='login'),
    
    url('^new/post/$', views.vNew.newPost, name='newpost'),
    url('^new/comment/$', views.vNew.newComment, name='newcomment'),
    url('^new/star/$', views.vNew.newStar, name='newstar'),
    url('^new/recommend/$', views.vNew.newRecommend, name='newrecommend'),
    
    url('^users/(?P<user_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getUser, name='getuser'),
    url('^posts/(?P<post_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getPost, name='getpost'),
    url('^comments/(?P<comment_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getComment, name='getcomment'),
    url('^stars/(?P<star_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getStar, name='getStar'),
    url('^recommends/(?P<recommend_id>[0-9]+)/(?P<access_token>[0-9a-z\-]+)/$', views.vInfo.getRecommend, name='getrecommend'),

    url('^edit/user/$', views.vEdit.user, name='edituser'),
    url('^edit/post/$', views.vEdit.post, name='editpost'),
    url('^edit/comment/$', views.vEdit.comment, name='editcomment'),

    url('^delete/user/$', views.vDelete.user, name='deleteuser'),
    url('^delete/post/$', views.vDelete.post, name='deletepost'),
    url('^delete/comment/$', views.vDelete.comment, name='deletecomment'),
    url('^delete/star/$', views.vDelete.star, name='deletestar'),
    url('^delete/recommend/$', views.vDelete.recommend, name='deleterecommend'),
    
]
