from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('UrlShortener.redutor.views',
    # Examples:
    # url(r'^$', 'UrlShortener.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$' , 'index', name= 'index'),
    url(r'^(?P<pk>\d+)/$', 'modf' , name='modf' ),
    
    
    #url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
)


