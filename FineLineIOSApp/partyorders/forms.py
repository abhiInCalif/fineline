from django import forms

class OrderForm(forms.Form):
    """
    Form for processing a single order placement
    """
    address = forms.CharField(required=True)
    name = forms.CharField(required=True)
    datetime = forms.CharField(required=True)
    payment_nonce = forms.CharField(required=True)
    
