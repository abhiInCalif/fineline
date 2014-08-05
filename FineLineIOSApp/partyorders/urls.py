from django.conf.urls import patterns, url

from FineLineIOSApp.partyorders import views

urlpatterns = patterns('',
        url(r'^catalogue/$', views.ShoppingItemsView.as_view(), name='catalogue-view'),
        url(r'^placeorder/$', views.PlaceOrderView.as_view(), name='placeorder-view'),
        url(r'^additem/$', views.AddItemView.as_view(), name='additem-view'),
        )