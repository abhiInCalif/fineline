from django.conf.urls import patterns, url
from FineLineIOSApp.payment import views

urlpatterns = patterns('',
        url(r'^clienttoken/$', views.BraintreePayment.as_view(), name='get-client-token'),
        )
