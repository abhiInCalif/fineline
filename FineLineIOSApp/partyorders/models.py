from django.db import models

# Create your models here.

class ShoppingItem(models.Model):
    """
    ShoppingItem is an item that we sell through our app
    Contains general information regarding the item including
    Name, Photo URL, and Price.
    """
    name = models.CharField(max_length=128)
    sku = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()
    photo = models.URLField(max_length=512)
    
class Delivery(models.Model):
    """
    Delivery is the object containing the address and time information
    about when the package should be delivered
    """
    address = models.CharField(max_length=512)
    datetime = models.CharField(max_length=512)

class Order(models.Model):
    """
    Order is the complete order purchased by one person
    """
    personName = models.CharField(max_length=128)
    delivery = models.OneToOneField(Delivery)

class OrderItem(models.Model):
    """
    OrderItem is an item ordered by someone
    It belongs to one and only one order
    """
    item = models.OneToOneField(ShoppingItem)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order)
