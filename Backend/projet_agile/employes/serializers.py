# employes/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)

    class Meta:
        model = Employe
        fields = ['id', 'username', 'role', 'date_embauche']

    def create(self, validated_data):
        username = validated_data.pop('username')
        role = validated_data.pop('role')

        # Créer l'utilisateur avec un mot de passe par défaut
        user = User.objects.create_user(username=username, password="motdepasse1234")
        
        # Assigner le groupe en fonction du rôle
        group, created = Group.objects.get_or_create(name=role)
        user.groups.add(group)
        
        # Créer l'employé
        employe = Employe.objects.create(user=user, role=role, **validated_data)
        
        return employe
