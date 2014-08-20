from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers

# Custom imports here
import braintree

# Create your views here.


# superclass payment definition
class Payments:

    def get_client_token(self):
        """
        returns client token
        """
        pass

    def perform_transaction(self, amount, nonce):
        """
        performs a transaction
        """
        pass



class BraintreePayment(Payments, View):
    """
    This view handles payment processing through the braintree
    processing system
    """
    def get(self, request, *args, **kwargs):
        client_token = braintree.ClientToken.generate()
        token_dict = {'token': client_token}
        json = serializers.serialize('json', [token_dict])
        return HttpResponse(json, mimetype='application/json')

    def perform_transaction(self, amount, nonce):
        """
        overwriting the super class definition here
        """
        result = braintree.Transaction.sale({
            'amount': amount,
            'payment_method_nonce': nonce
        })

        return result

