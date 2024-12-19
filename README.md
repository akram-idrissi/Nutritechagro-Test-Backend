# Nutritechagro-Test-Backend


## Description

Ce projet constitue le backend d'une application e-commerce qui fait parti du test de Nutritechagro, développé avec Django, Django Rest Framework et MySQL. Il gère la logique de l'application, les API et les interactions avec la base de données.

## Pourquoi Django et Django Rest Framework ?

### **Django**
1. **Cadre robuste et sécurisé** :
   - Django est un framework web Python mature et sécurisé, avec des fonctionnalités intégrées pour la gestion des utilisateurs, l'authentification et les permissions.
   
2. **Facilité d'administration** :
   - Django offre une interface d'administration prête à l'emploi, permettant de gérer facilement les utilisateurs, les produits et les commandes.

3. **Rapidité de développement** :
   - La philosophie "batteries included" de Django permet de démarrer rapidement avec des fonctionnalités comme les formulaires, la validation, les migrations et les tests intégrés.

### **Django Rest Framework (DRF)**
1. **API facile à créer** :
   - DRF simplifie la création d'API RESTful, avec des vues basées sur des classes et une sérialisation intuitive des données.
   
2. **Sécurité intégrée** :
   - DRF inclut des fonctionnalités pour gérer la sécurité de l'API, comme l'authentification via JWT, le filtrage des requêtes, et la gestion des permissions.

3. **Support des formats modernes** :
   - DRF prend en charge différents formats comme JSON, XML, et rend les API facilement extensibles pour gérer des cas complexes.

### **MySQL**
1. **Base de données relationnelle robuste** :
   - MySQL est une base de données relationnelle bien établie, idéale pour gérer les informations d'un e-commerce telles que les utilisateurs, les produits et les commandes.
   
2. **Scalabilité et performance** :
   - MySQL permet de gérer de grandes quantités de données avec une bonne performance et peut être facilement configurée pour des applications à grande échelle.

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/akram-idrissi/Nutritechagro-Test-Backend.git
cd Nutritechagro-Test-Backend
```

2. Créez un environnement virtuel et activez-le :
  ```python
  python3 -m venv venv
  source venv/bin/activate  # Pour Linux/Mac
  venv\Scripts\activate
  ```

3. Installez les dépendances :
  ```bash
  pip install -r requirements.txt
  ```

4. Appliquez les migrations :
  ```
  python manage.py migrate
  ```

## Endpoints
- Page de connexion: [http://localhost:8000/api/signin](http://localhost:8000/api/signin)
- Page d'inscription: [http://localhost:8000/api/signup](http://localhost:8000/api/signup)
- Page d'un produit: [http://localhost:8000/api/products/id](http://localhost:8000/api/products/id)
- Page d'une categorie (les filtres ne sont pas implementé): [http://localhost:8000/api/categories/name](http://localhost:8000/api/categories/name)
