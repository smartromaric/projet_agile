from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Category
from .models import Sale
from .models import Stock
from .models import Product
from rest_framework import generics 
from .serializers import ProductSerializer, CategorySerializer, StockSerializer, SaleSerializer


class Index(TemplateView):
    template_name = 'index.html'

################################ Section des categories ##############################
# Liste des catégories
class CategoryListView(ListView):
    model = Category
    template_name = 'gestion_stocks/Categories/category_list.html'

# Créer une nouvelle catégorie
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'gestion_stocks/Categories/category_form.html'
    success_url = reverse_lazy('category_list')

# Modifier une catégorie existante
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'gestion_stocks/Categories/category_form.html'
    success_url = reverse_lazy('category_list')

# Supprimer une catégorie
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'gestion_stocks/Categories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


##################################### Section des stocks ##################################
# Liste du stock
class StockListView(ListView):
    model = Stock
    template_name = 'gestion_stocks/Stocks/stock_list.html'

# Détail du stock d'un produit
class StockDetailView(ListView):
    model = Stock
    template_name = 'gestion_stocks/Stocks/stock_detail.html'

# Mettre à jour le stock d'un produit
class StockUpdateView(UpdateView):
    model = Stock
    fields = ['quantity', 'last_restock_date']
    template_name = 'gestion_stocks/Stocks/stock_form.html'
    success_url = reverse_lazy('stock_list')


################################### Section des produits ####################################
# Liste des produits
class ProductListView(ListView):
    model = Product
    template_name = 'gestion_stocks/Products/product_list.html'

# Créer un nouveau produit
class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'supplier', 'price', 'description']
    template_name = 'gestion_stocks/Products/product_form.html'
    success_url = reverse_lazy('product_list')

# Modifier un produit existant
class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'supplier', 'price', 'description']
    template_name = 'gestion_stocks/Products/product_form.html'
    success_url = reverse_lazy('product_list')

# Supprimer un produit
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'gestion_stocks/Products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


################################### Section des ventes #######################################
# Liste des ventes
class SaleListView(ListView):
    model = Sale
    template_name = 'gestion_stocks/Sales/sale_list.html'

# Créer une nouvelle vente
class SaleCreateView(CreateView):
    model = Sale
    fields = ['product', 'quantity_sold']
    template_name = 'gestion_stocks/Sales/sale_form.html'
    success_url = reverse_lazy('sale_list')

# Détail d'une vente
class SaleDetailView(ListView):
    model = Sale
    template_name = 'gestion_stocks/Sales/sale_detail.html'


##############################################################################################
##############################################################################################
#########################                                           ##########################
#########################       Section des vues pour l'api         ##########################
#########################                                           ##########################        
##############################################################################################
##############################################################################################  
 

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StockList(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
 