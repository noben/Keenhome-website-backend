from django.conf.urls import patterns, url
from learning_record import views

urlpatterns = patterns('',
    
    url(r'^records/$', views.show_records, name='records'),
    
)