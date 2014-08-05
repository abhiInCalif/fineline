from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.
from django.views.generic import CreateView
from django.core import serializers
from FineLineIOSApp.partyorders.models import ShoppingItem
from FineLineIOSApp.partyorders.models import Delivery
from FineLineIOSApp.partyorders.models import Order
from FineLineIOSApp.partyorders.models import OrderItem

# purpose of class is to provide an endpoint for getting all shopping items
# mobile endpoint only though.
class ShoppingItemsView(View):
    """
    This view supports the display of all the shopping items in the database
    """
    def get(self, request, *args, **kwargs):
        
        items = ShoppingItem.objects.filter();
        json = serializers.serialize('json', items)
        return HttpResponse(json, mimetype='application/json')


# purpose of this class is to allow you to post an order
# an order contains Name, Delivery time, Delivery Address
# Item name and quantity, sku number is used instead of
# name to look up the item
class PlaceOrderView(View):
    """
    This view supports placing an order
    """
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            delivery_address = form.cleaned_data.get('address')
            name = form.cleaned_data.get('name')
            datetime = form.cleaned_data.get('datetime')
            sku_list = request.POST.getlist('sku[]')
            
            # first save all the delivery and order information
            delivery = Delivery(address=delivery_address, datetime=datetime)
            delivery.save()
            order = Order(personName=name, delivery=delivery)
            order.save()
            
            for (sku, quantity) in sku_list:
                items = ShoppingItem.objects.filter(sku=sku)
                if items.length == 0:
                    return HttpResponse("500");
                
                item = items[0]
                order_item = OrderItem(item=item, quantity=quantity, order=order)
                order_item.save()
                
            data = simplejson.dumps({'return': True})
            return HttpResponse(data, mimetype='application/json')
        
        return HttpResponse('', mimetype='application/json')

class AddItemView(CreateView):
    """
    Adds an item to the catalogue
    """
    model = ShoppingItem
    template_name = 'addItem.html'

    def get_success_url(self):
        return reverse('catalogue-view')