# Inscription des Élèves avec Interface Graphique (Tkinter) et SQLite

Ce projet permet de gérer l'inscription des élèves à l'aide d'une interface graphique construite avec **Tkinter** et d'une base de données SQLite. Il permet de saisir des informations sur les élèves (nom, prénom, âge, date de naissance, adresse, sexe, nom des parents, classe) et de les afficher dans une table. Le tout est sécurisé par un mot de passe pour l'accès à l'interface d'administration.

## Fonctionnalités

- Authentification avec mot de passe administrateur
- Ajout des informations des élèves dans une base de données SQLite
- Affichage des élèves dans une interface graphique
- Vérification des formats des informations (date de naissance au format `YYYY-MM-DD`)
- Gestion de la base de données avec création dynamique de colonnes manquantes

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les bibliothèques nécessaires :

- **Python 3.x**
- **Tkinter** (généralement inclus avec Python)
- **SQLite3** (également inclus avec Python)

## Installation

1. Clonez ce dépôt ou téléchargez le fichier.
2. Assurez-vous d'avoir Python installé sur votre machine.
3. Exécutez le script Python pour démarrer l'application.

## Utilisation

1. Lancez le fichier Python avec la commande suivante :

    ```bash
    python index.py
    ```

2. Une fenêtre de connexion apparaîtra. Entrez le mot de passe administrateur `admin123` pour accéder à l'interface.
3. Une fois connecté, vous pourrez ajouter des élèves dans la base de données en remplissant le formulaire et en cliquant sur "Ajouter".
4. Vous pouvez également afficher la liste des élèves déjà enregistrés en cliquant sur "Afficher".

## Structure de la base de données

Le projet utilise SQLite pour stocker les informations des élèves. La table `eleves` contient les colonnes suivantes :

- `id` (INTEGER) : Identifiant unique de l'élève (clé primaire)
- `nom` (TEXT) : Nom de l'élève
- `prenom` (TEXT) : Prénom de l'élève
- `age` (INTEGER) : Âge de l'élève
- `date_naissance` (TEXT) : Date de naissance au format `YYYY-MM-DD`
- `adresse` (TEXT) : Adresse de l'élève
- `sexe` (TEXT) : Sexe de l'élève
- `nom_parents` (TEXT) : Nom des parents de l'élève
- `classe` (TEXT) : Classe de l'élève

## Contribution

Si vous souhaitez contribuer à ce projet, vous pouvez forker le dépôt et proposer des modifications sous forme de pull requests. N'hésitez pas à signaler des bugs ou des améliorations potentielles.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
