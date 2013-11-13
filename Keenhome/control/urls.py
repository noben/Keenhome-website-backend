from django.conf.urls import patterns, url
from control import views

urlpatterns = patterns('',
    
    url(r'^control/$', views.control, name='control'),
    url(r'^control/current_status/$', views.current_status, name='current_status'),
    
    #ulrs for each room:
    url(r'^control/living_room/$', views.living_room, name='living_room'),
    url(r'^control/dinning_room/$', views.dinning_room, name='dinning_room'),
    url(r'^control/kitchen/$', views.kitchen, name='kitchen'),
    url(r'^control/bed_room1/$', views.bed_room1, name='bed_room1'),
    url(r'^control/bed_room2/$', views.bed_room2, name='bed_room2'),
    url(r'^control/bed_room3/$', views.bed_room2, name='bed_room2'),
)