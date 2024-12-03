from django import forms
from .models import Utilisateur

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'email', 'age', 'sexe']  # Ajout des nouveaux champs
