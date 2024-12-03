from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('ajouter/', views.ajouter_utilisateur, name='ajouter_utilisateur'),
    path('modifier/<int:utilisateur_id>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('supprimer/<int:utilisateur_id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
]
