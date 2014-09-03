from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
import json as simplejson
from threading import RLock


# Create your views here.
from django.views.generic import CreateView
from FineLineIOSApp.partyorders.models import ShoppingItem
from FineLineIOSApp.partyorders.models import Delivery
from FineLineIOSApp.partyorders.models import Order
from FineLineIOSApp.partyorders.models import OrderItem
from FineLineIOSApp.partyorders.forms import OrderForm
from FineLineIOSApp.payment.views import BraintreePayment


# some utility functions
# there are not enough of them to warrant another file, when this list grows beyond 3 a new file will ahve to be created
def calculate_order_total(order):
    items = order.orderitem_set.all()
    price = 0
    for item in items:
        price = price + item.quantity * item.item.price

    return price

def check_inStock(item, quantity):
    """
    Checks if an item is in stock in a atomic fashion
    """
    # Update the stock amount, if the stock left is 0 return -1
    inStock = True
    lock = RLock()
    lock.acquire()
    try:
        if item.stock - int(quantity) >= 0:
            item.stock = item.stock - int(quantity)
            item.save()
        else:
            # we have a problem, the stock is not there, time to
            # cleanup and return -1
            inStock = False
    finally:
        lock.release()

    return inStock


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
            nonce = form.cleaned_data.get('payment_nonce')
            delivery_address = form.cleaned_data.get('address')
            name = form.cleaned_data.get('name')
            datetime = form.cleaned_data.get('datetime')
            sku_list = request.POST.getlist('sku[]')
            # first save all the delivery and order information
            delivery = Delivery(address=delivery_address, datetime=datetime)
            delivery.save()
            order = Order(personName=name, delivery=delivery)
            order.save()

            for i in range(0, len(sku_list),2):
                sku = sku_list[i]
                quantity = sku_list[i + 1]
                items = ShoppingItem.objects.filter(sku=sku)
                if len(items) == 0:
                    return HttpResponse("500");

                item = items[0]
                import pdb; pdb.set_trace()
                if not check_inStock(item, quantity):
                    order.delete()
                    data = simplejson.dumps({
                                             'stock': item.stock,
                                             'item': item.name
                                            })
                    return HttpResponse(data, mimetype='application/json')

                order_item = OrderItem(item=item, quantity=quantity, order=order)
                order_item.save()

            order_total = calculate_order_total(order)

            # process payment
            payment_handler = BraintreePayment()
            result = payment_handler.perform_transaction(order_total, nonce)
            if result.is_success is not True:
                # erase the order
                order.delete()
                return HttpResponse('', mimetype='application/json')

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

