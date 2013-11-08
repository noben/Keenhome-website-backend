from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    #main page (be directed to login page if not authenticated)
    url(r'^$', views.index, name='index'),
    
    url(r'^control/$', views.control, name='control'),
    url(r'^control/current_status/$', views.current_status, name='current_status'),
)