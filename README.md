# Gestion des Utilisateurs - Projet Django

## Description
Ce projet est une application Django permettant de gérer des utilisateurs. L'application inclut des fonctionnalités pour afficher une liste d'utilisateurs, ajouter, modifier et supprimer des utilisateurs, ainsi qu'une fonctionnalité de recherche pour filtrer les utilisateurs par nom.

## Fonctionnalités
- **Liste des utilisateurs** : Affichage d'une liste de tous les utilisateurs enregistrés.
- **Ajout d'un utilisateur** : Un formulaire pour ajouter de nouveaux utilisateurs.
- **Modification d'un utilisateur** : Un formulaire pour modifier les informations des utilisateurs existants.
- **Suppression d'un utilisateur** : Option de supprimer un utilisateur.
- **Recherche d'un utilisateur** : Fonctionnalité pour rechercher un utilisateur par son nom.

## Technologies utilisées
- **Python 3.x**
- **Django 5.x**
- **SQLite** (base de données par défaut)

## Installation

### Prérequis
Assurez-vous d'avoir Python 3.x et pip installés sur votre machine. Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).

### Cloner le repository
Commencez par cloner ce projet depuis GitHub (ou utilisez votre propre méthode de clonage) :

```bash
git clone https://github.com/votre-utilisateur/gestion-utilisateur.git
```

### Installer les dépendances
Naviguez dans le répertoire du projet et installez les dépendances avec pip :

```bash
cd gestion-utilisateur
pip install -r requirements.txt
```

### Configurer la base de données
Ensuite, appliquez les migrations pour créer la base de données et les tables nécessaires :

```bash
python manage.py migrate
```

### Lancer le serveur de développement
Lancez le serveur de développement de Django :

```bash
python manage.py runserver
```

Vous pouvez maintenant accéder à l'application en ouvrant votre navigateur à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Structure du projet
Voici la structure de base du projet :

```
gestion_utilisateur/
│
├── utilisateurs/          # Application principale
│   ├── migrations/        # Migrations de la base de données
│   ├── __init__.py
│   ├── admin.py           # Configuration du panneau d'administration
│   ├── apps.py
│   ├── forms.py           # Formulaires pour les utilisateurs
│   ├── models.py          # Modèles pour les utilisateurs
│   ├── tests.py           # Tests unitaires
│   ├── views.py           # Logique de vue pour afficher et gérer les utilisateurs
│   └── urls.py            # URL routage pour l'application utilisateurs
│
├── gestion_utilisateur/   # Projet Django principal
│   ├── __init__.py
│   ├── settings.py        # Paramètres de l'application
│   ├── urls.py            # URLs principales du projet
│   ├── wsgi.py
│   └── asgi.py
│
├── db.sqlite3             # Base de données SQLite par défaut
├── manage.py              # Script pour gérer le projet Django
└── requirements.txt       # Liste des dépendances
```

## Utilisation

1. **Page d'accueil** : Vous accédez à la liste des utilisateurs en visitant la page d'accueil de l'application.
2. **Ajouter un utilisateur** : En cliquant sur le bouton "Ajouter un utilisateur", vous serez redirigé vers un formulaire où vous pourrez entrer les informations de l'utilisateur (nom, prénom, email, etc.).
3. **Modifier un utilisateur** : Chaque utilisateur a un lien "Modifier" à côté de son nom, vous permettant de modifier ses informations.
4. **Supprimer un utilisateur** : Chaque utilisateur a également un lien "Supprimer" pour le supprimer de la base de données.
5. **Recherche** : Utilisez la barre de recherche pour filtrer les utilisateurs par leur nom.

## Customisation
Vous pouvez personnaliser l'apparence et le comportement de l'application en modifiant les fichiers suivants :
- **`utilisateurs/templates/utilisateurs/liste.html`** : Page d'affichage des utilisateurs.
- **`utilisateurs/templates/utilisateurs/ajouter.html`** : Formulaire pour ajouter un utilisateur.
- **`utilisateurs/forms.py`** : Définition des formulaires utilisateurs.
- **`utilisateurs/models.py`** : Modèle pour l'utilisateur.
- **`static/css/styles.css`** : Feuille de style pour personnaliser l'apparence de l'application.

## Tests
Les tests unitaires pour l'application sont inclus dans le fichier `tests.py` dans l'application `utilisateurs`.

### Lancer les tests
Pour exécuter les tests, utilisez la commande suivante :

```bash
python manage.py test
```

## Contributions
Les contributions sont les bienvenues ! Si vous avez des suggestions d'amélioration ou souhaitez corriger des bugs, n'hésitez pas à soumettre une pull request.

## Auteurs
- [Votre nom](https://github.com/fabioramefiarison)



