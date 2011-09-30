from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^$', 'views.home', name='home'),

    url(r'^404/$', direct_to_template, {'template': '404.html'}),
    url(r'^500/$', direct_to_template, {'template': '500.html'}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT.replace('\\','/')
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT.replace('\\','/')
        }),

