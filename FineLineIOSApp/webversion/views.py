from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
import json as simplejson

# Create your views here.
from FineLineIOSApp.partyorders.models import ShoppingItem

class BrowseView(View):
    """
    Allows the user to browse all the available items up for purchase
    """

    def get(self, request, *args, **kwargs):
        items = ShoppingItem.objects.filter()
        return render(request,'browse.html', {'items': items})
