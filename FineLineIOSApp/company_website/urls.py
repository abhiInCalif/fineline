from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializersfrom FineLineIOSApp.company_website import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^/$', views.bouncingBots.as_view(), name='bouncingBots'),
        )
