# forms.py
from django import forms
from .models import Stock, Product

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'quantity', 'last_restock_date']
        widgets = {
            'last_restock_date': forms.DateInput(attrs={'type': 'date'}),
        }
