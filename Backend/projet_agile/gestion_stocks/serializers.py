###############################################################################################################################
###############################################################################################################################
########################                                                                #######################################
########################               section de seriazilsation des models             #######################################
########################                                                                #######################################    
###############################################################################################################################
###############################################################################################################################

from rest_framework import serializers
from .models import Product, Category, Stock, Sale, Supplier

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Ou spécifiez les champs que vous voulez exposer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
