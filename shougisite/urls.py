from django.conf.urls import include, url
from shougisite import views

urlpatterns = [
    url(r'^$', views.logout_top, name='logout_top'),
    url(r'^login_top/$', views.login_top, name='login_top'),
    url(r'^mypage_top/$', views.mypage_top, name='mypage_top'),
    url(r'^mypage_add/$', views.mypage_add, name='mypage_add'),
    # url(r'^withdraw/$', views.withdraw, name='withdraw'),
    # url(r'^withdraw_confirm/$', views.withdraw_confirm, name='withdraw'),
    # url(r'^game_option/$', views.game_option, name='game_option'),
    # url(r'^game/$', views.game, name='game'),
    # url(r'^game_result/$', views.game_result, name='game_result'),
    # url(r'^view_game_record/$', views.view_game_record, name='view_game_record'),
    # url(r'^site_option/$', views.site_option, name='site_option'),
]