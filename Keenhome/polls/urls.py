from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    #main page (be directed to login page if not authenticated)
    url(r'^$', views.index, name='index'),
    
    #user login/logout page
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/user_profile/$', views.user_profile, name='user_profile'),
    url(r'^accounts/user_profile_update/$', views.user_profile_update, name='user_profile_update'),
    
    #user signup page
    url(r'^accounts/register/$', views.register, name='register'),
    
    #information sites:
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^comments/$', views.comments, name='comments'),
    
    #voting module
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)