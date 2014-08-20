from FineLineIOSApp.company_website import views
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^index/$', views.bouncingBots.as_view(), name='bouncingBots'),
        )
