from django.conf.urls import patterns, url

from FineLineIOSApp.webversion import views

urlpatterns = patterns('',
        url(r'^browse/$', views.BrowseView.as_view(), name='browse-view'),
        )
