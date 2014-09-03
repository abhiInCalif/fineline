from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.http import HttpResponse
from django.core import serializers
import json

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
        jsonData = json.dumps(token_dict)
        return HttpResponse(jsonData, mimetype='application/json')

    def perform_transaction(self, amount, nonce):
        """
        overwriting the super class definition here
        """
        result = braintree.Transaction.sale({
            'amount': str(amount),
            'payment_method_nonce': nonce
        })

        return result

