# -*- coding: utf-8 -*-
"""CDC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls.i18n import i18n_patterns
from solar import views as solar
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import *
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', solar.home, name='home'),
    url(r'^projects/$', solar.projects, name='projects'),
    url(r'^price/(?P<price_l>\w+)/$', solar.price, name='price'),
    url(r'^service/$', solar.service, name='service'),
    url(r'^aticles/(?P<order>\w+)/$', solar.articles, name='articles'),
    url(r'^contact/$', solar.contact, name='contact'),
    url(r'^service_sort/$', solar.service_sort, name='service_sort'),
    url(r'^projects_pagi/$', solar.projects_pagi, name='projects_pagi'),
    url(r'^mass/$', solar.mass, name='mass'),
    url(r'^massgen/$', solar.massgen, name='massgen'),
    url(r'^summernote/$', include('django_summernote.urls')),
    url('^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^$', solar.home, name='home'),
    url(r'^projects$', solar.projects, name='projects'),
    url(r'^service_sort/$', solar.service_sort, name='service_sort'),
    url(r'^price/(?P<price_l>\w+)/$', solar.price, name='price'),
    url(r'^service/$', solar.service, name='service'),
    url(r'^aticles/(?P<order>\w+)/$', solar.articles, name='articles'),
    url(r'^contact/$', solar.contact, name='contact'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^projects_pagi/', solar.projects_pagi, name='projects_pagi'),
    url(r'^mass/$', solar.mass, name='mass'),
    url(r'^massgen/$', solar.massgen, name='massgen'),
    url('^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
