# employes/models.py
from django.contrib.auth.models import User
from django.db import models

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    date_embauche = models.DateField()
    # autres champs si nécessaire
