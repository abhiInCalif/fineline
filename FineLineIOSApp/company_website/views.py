from django.shortcuts import render
from django.core import serializers
from FineLineIOSApp.company_website import views
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse

class bouncingBots(View):
    def get(self, request,*args,**kwargs):
        return render(request, "bouncingBots.html")
 