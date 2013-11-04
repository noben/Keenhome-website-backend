from django.conf.urls import patterns, include, url

#usr login/logout module
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^keenhome/', include('polls.urls', namespace="polls")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Examples:
    # url(r'^$', 'hello.views.home', name='home'),
    # url(r'^hello/', include('hello.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

