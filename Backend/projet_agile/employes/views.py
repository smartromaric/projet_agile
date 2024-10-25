from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employe
from .serializers import EmployeSerializer

class EmployeListCreateView(generics.ListCreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]