from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FineLineIOSApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-orders/', include("FineLineIOSApp.partyorders.urls")),
    url(r'^api-payments/', include('FineLineIOSApp.payment.urls')),
    url(r'^/', include('FineLineIOSApp.company_website.urls')),
)
