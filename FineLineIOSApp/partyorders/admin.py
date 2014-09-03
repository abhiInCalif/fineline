from django.contrib import admin

# Register your models here.
from FineLineIOSApp.partyorders.models import ShoppingItem, Delivery, Order, OrderItem

admin.site.register(ShoppingItem)
admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(OrderItem)
