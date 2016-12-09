from django.conf.urls import include, url
from shougisite import views

urlpatterns = [
    url(r'^$', views.logout_top, name='logout_top'),
    url(r'^login_top/$', views.login_top, name='login_top'),
    url(r'^mypage_top/$', views.mypage_top, name='mypage_top'),
    url(r'^mypage_add/$', views.mypage_add, name='mypage_add'),

]