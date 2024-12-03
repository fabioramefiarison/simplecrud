from django.shortcuts import render, redirect, get_object_or_404
from .models import Utilisateur
from .forms import UtilisateurForm

def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'utilisateurs/liste.html', {'utilisateurs': utilisateurs})

def ajouter_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurForm()
    return render(request, 'utilisateurs/ajouter.html', {'form': form})

def modifier_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    if request.method == 'POST':
        form = UtilisateurForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurForm(instance=utilisateur)
    return render(request, 'utilisateurs/modifier.html', {'form': form})

def supprimer_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)
    if request.method == 'POST':
        utilisateur.delete()
        return redirect('liste_utilisateurs')
    return render(request, 'utilisateurs/supprimer.html', {'utilisateur': utilisateur})
