from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from .models import Category
from .models import Sale
from .models import Stock
from .models import Product
from .models import Supplier
from rest_framework import generics 
from .serializers import ProductSerializer, CategorySerializer, StockSerializer, SaleSerializer, SupplierSerializer
from rest_framework import permissions
from .forms import StockForm
from django.contrib import messages

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


##################################### Section des fournisseurs ############################
class SupplierListView(ListView):
    model = Supplier
    template_name = 'gestion_stocks/Suppliers/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'gestion_stocks/Suppliers/supplier_detail.html'
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'gestion_stocks/Suppliers/supplier_form.html'
    fields = ['name', 'contact_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'gestion_stocks/Suppliers/supplier_form.html'
    fields = ['name', 'contact_name', 'phone_number', 'email', 'address']
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'gestion_stocks/Suppliers/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')


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

class StockCreateView(CreateView):
    model = Stock
    fields = ['product', 'quantity', 'last_restock_date']
    template_name = 'gestion_stocks/Stocks/add_stock.html'
    success_url = reverse_lazy('stock_list')
    form = StockForm
    
# def add_stock(request):
#     if request.method == 'POST':
#         form = StockForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Stock ajouté avec succès.")
#             return render(request, "gestion_stocks/Stocks/stock_list.html")  # Redirection vers la même page après l'ajout
#         else:
#             messages.error(request, "Erreur lors de l'ajout du stock.")
#     else:
#         form = StockForm()
    
#     return render(request, 'gestion_stocks/Stocks/add_stock.html', {'form': form})

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
    fields = ['product', 'quantity_sold', 'sale_date', 'total_price', 'employe', 'action']
    template_name = 'gestion_stocks/Sales/sale_form.html'
    success_url = reverse_lazy('sale_list')

    def has_permission(self):
        return True

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

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SalePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Seuls les caissières peuvent ajouter ou voir, pas modifier
        if view.action in ['create', 'list']:
            return request.user.groups.filter(name='Caissiere').exists()
        return False

class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [SalePermission]
