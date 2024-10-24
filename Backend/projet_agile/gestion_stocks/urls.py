"""
URL configuration for projet_agile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),

    # Routes pour les catégories
    path('categories/', views.CategoryListView.as_view(), name='category_list'),  # Liste des catégories
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),  # Créer une catégorie
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),  # Modifier une catégorie
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),  # Supprimer une catégorie

    # Routes pour les produits
    path('products/', views.ProductListView.as_view(), name='product_list'),  # Liste des produits
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),  # Créer un produit
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),  # Modifier un produit
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),  # Supprimer un produit

    # Routes pour le stock
    path('stock/', views.StockListView.as_view(), name='stock_list'),  # Liste des stocks
    path('stock/<int:pk>/', views.StockDetailView.as_view(), name='stock_detail'),  # Détails du stock d'un produit
    path('stock/<int:pk>/update/', views.StockUpdateView.as_view(), name='stock_update'),  # Mettre à jour le stock

    # Routes pour les ventes
    path('sales/', views.SaleListView.as_view(), name='sale_list'),  # Liste des ventes
    path('sales/create/', views.SaleCreateView.as_view(), name='sale_create'),  # Créer une vente
    path('sales/<int:pk>/', views.SaleDetailView.as_view(), name='sale_detail'),  # Détails d'une vente

    ################### sections des apis pour l'utilisation avec reactJs ########################
    path('api/products/', views.ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('api/categories/', views.CategoryList.as_view(), name='category-list'),
    path('api/stocks/', views.StockList.as_view(), name='stock-list'),
    path('api/sales/', views.SaleList.as_view(), name='sale-list'),
]
