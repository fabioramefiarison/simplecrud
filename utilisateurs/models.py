from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)  # Nouveau champ
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)  # Nouveau champ
    sexe = models.CharField(max_length=10, choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme')  # Nouveau champ
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
