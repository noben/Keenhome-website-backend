from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    #main page (be directed to login page if not authenticated)
    url(r'^$', views.index, name='index'),
    
    #user login/logout page
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/user_profile/$', views.user_profile, name='user_profile'),
    
    #user signup page
    url(r'^accounts/register/$', views.register, name='register'),
    
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)