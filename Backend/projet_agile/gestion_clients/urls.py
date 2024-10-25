# gestion_clients/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/update/<int:pk>/', views.client_update, name='client_update'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),

    #route et urls des commandes
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/<int:client_id>/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),

    ########################################################################################
    #################################      Route des api        ############################
    ########################################################################################

    # Orders
    path('api/clients/', views.ClientList.as_view(), name='api_client_list'),
    path('api/Clients/<int:pk>/', views.ClientDetail.as_view(), name='api_client_detail'),

    # OrderItems
    path('api/orderItem/', views.OrderItemList.as_view(), name='api_order_item_list'),
    path('api/orders/<int:pk>/', views.OrderItemDetail.as_view(), name='api_order_item_detail'),

    # Order
    path('api/orders/', views.OrderList.as_view(), name='api_order_list'),
    path('api/orders/<int:pk>/', views.OrderDetail.as_view(), name='api_order_detail'),
    path('api/orders/<int:order_id>/items/', views.OrderItemByOrderView.as_view(), name='api_order_items'),
]
