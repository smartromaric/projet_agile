# Create your views here.
# gestion_clients/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Client, Order, OrderItem
from .forms import ClientForm
from gestion_stocks.models import Product
from django.forms import modelformset_factory


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'gestion_clients/Clients/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client ajouté avec succès.")
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'gestion_clients/Clients/client_form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client mis à jour avec succès.")
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'gestion_clients/Clients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, "Client supprimé avec succès.")
        return redirect('client_list')
    return render(request, 'gestion_clients/Clients/client_confirm_delete.html', {'client': client})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'gestion_clients/Orders/order_list.html', {'orders': orders})

def order_create(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    products = Product.objects.all()
    if request.method == 'POST':
        order = Order.objects.create(client=client)
        total_price = 0
        for product in products:
            quantity = int(request.POST.get(f'quantity_{product.id}', 0))
            if quantity > 0:
                order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)
                total_price += order_item.price
        order.total_price = total_price
        order.save()
        messages.success(request, "Commande créée avec succès.")
        return redirect('order_list')
    return render(request, 'gestion_clients/Orders/order_form.html', {'client': client, 'products': products})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'gestion_clients/Orders/order_detail.html', {'order': order})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, "Commande supprimée avec succès.")
        return redirect('order_list')
    return render(request, 'gestion_clients/Orders/order_confirm_delete.html', {'order': order})



##############################################################################################
##############################################################################################
#########################                                           ##########################
#########################       Section des vues pour l'api         ##########################
#########################                                           ##########################        
##############################################################################################
##############################################################################################  
 

# gestion_clients/views.py
from rest_framework import viewsets
from .models import Client, Order, OrderItem
from gestion_stocks.models import Product
from .serializers import ClientSerializer, OrderSerializer, OrderItemSerializer, ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer    


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderItemSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderItemSerializer    