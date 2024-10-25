# employes/urls.py
from django.urls import path
from .views import EmployeListCreateView

urlpatterns = [
    path('api/', EmployeListCreateView.as_view(), name='employe-list-create'),
]
