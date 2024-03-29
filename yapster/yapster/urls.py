from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'users.views.index'),
                       url(r'^api/\.1/', include('users.urls_api')),
                       url(r'^api/\.1/yap/', include('yap.urls_api')),
                       url(r'^api/\.1/feed/', include('feed.urls_api')),
                       url(r'^api/\.1/accounts/',
                           include('registration.backends.default.urls_api')),
                       # temp: login and logout in rest_frameworks
                       url(r'^auth/', include(
                           'rest_framework.urls', namespace='rest_framework')),
                       # oauth2 for client. (ios app)
                       url(r'^oauth2/', include(
                           'provider.oauth2.urls', namespace='oauth2')),
                       # url(r'^accounts/',
                       #     include('registration.backends.default.urls')),
                       url(r'^django-rq/', include('django_rq.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
