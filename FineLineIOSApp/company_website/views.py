from django.shortcuts import render
from django.core import serializers
from django.views.generic import View
from django.http import HttpResponse

class bouncingBots(View):
    def get(self, request,*args,**kwargs):
        return render(request, "bouncingBots.html")
 