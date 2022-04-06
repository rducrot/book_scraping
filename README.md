Book Scraping
-
Ce programme permet d'extraire les données du site http://books.toscrape.com/

Préparation de votre environnement depuis le répertoire du programme :

    $ python -m venv venv # Mise en place de l'environnement virtuel
    $ venv/bin/activate # Activation de l'environnement virtuel
    (venv) $ pip install -r requirements.txt # Installation des librairies requises

Enfin, vous pouvez lancer le programme avec la commande suivante :

    (venv) $ python3 script.py

Les données sont enregistrées dans deux dossiers :
  - **books** : chaque catégorie de livres crée un fichier CSV contenant les informations de tous les livres de la catégorie.
  - **covers** : contient toutes les couvertures des livres au format JPG.