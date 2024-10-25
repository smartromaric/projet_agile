# gestion_clients/forms.py
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = []