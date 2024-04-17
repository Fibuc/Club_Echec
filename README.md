# Club d'échecs

Cette application est un gestionnaire de tournois d'échecs. Celui-ci permet de réaliser des tournois ayant des rondes de matchs basées sur la méthode de tournois suisse.

## Installation

**IMPORTANT :** L'application utilise les matchs cases et les opérateurs OU logique et ET logique. Pour cela, vous aurez donc besoin d'une version minimum de python 3.10 pour pouvoir le lancer.

### Cloner le dépôt

Pour cloner le dépôt, vous devrez ouvrir le terminal et effectuer la commande suivante dans le dossier de votre choix :
```bash
    git clone https://github.com/Fibuc/Club_Echec.git
```

### Créer un environnement virtuel

Ensuite, vous aurez besoin de créer un environnement virtuel que vous devrez nommer "env" afin d'éviter son push dans le repository. Si toutefois, vous désirez utiliser un autre nom d'environnement, merci de bien vouloir l'ajouter au ".gitignore".


Ouvrez le terminal et rendez-vous dans le dossier du dépôt local "Club_Echec" puis tapez la commande suivante :
```bash
    python -m venv env
```

### Activer votre environnement virtuel

Pour activer votre environnement virtuel la méthode est différente selon votre système d'exploitation.

#### Linux & MacOS :
```bash
    source chemin_de_votre_env/bin/activate
```
#### Windows : 
```bash
    chemin_de_votre_env\Scripts\activate.bat
```

### Installer les packages

Enfin, lorsque vous aurez activé votre environnement virtuel, vous aurez également besoin d'installer les packages essentiels pour le lancement disponibles dans le requirements.txt

```bash
    pip install -r requirements.txt
```
    
Veillez également à bien vous situer sur la branche "main" lors de l'exécution de script.py.

## Utilisation

En lançant l'application, vous vous retrouverez sur le menu principal avec différentes options disponibles.

- Créer/Reprendre un tournoi
- Ajouter/modifier un joueur
- Ajouter/modifier un club
- Afficher des rapports
- Quitter l'application

Suivez les étapes pour utiliser l'application de la bonne manière :

### 1/ Créez un ou plusieurs clubs

Pour bien démarrer, vous devrez commencer par créer un club car celui-ci vous sera demandé lors de la création d'un nouveau joueur. A ce moment-là, rendez-vous dans l'option 3, "Ajouter/modifier un club", sélectionnez l'option "Ajouter un club", rentrez les données puis valider.

### 2/ Créez les joueurs

Une fois le(s) club(s) créé(s), rendez-vous dans l'option principale 2, "Ajouter/modifier un joueur" puis sur "Ajouter un joueur", rentrez les informations demandées et répétez l'opération selon le nombre de joueurs que vous voulez créer. Vous aurez également la possibilité lors de la création du joueur de l'ajouter directement au prochain tournoi.

**A noter :** Par défaut un tournoi doit comprendre au minimum 8 joueurs afin qu'il puisse être lancé. Cette option peut être modifiée dans le module de configuration.

### 3/ Créez un tournoi

Maintenant que les joueurs sont créés, nous allons pouvoir passer au plus important, la création et le lancement du premier tournoi.

Pour cela, rendez-vous dans l'option 1 du menu principal, "Créer/reprendre un tournoi".

#### A. Reprise d'un tournoi
A cette étape, si un tournoi n'a pas été terminé, l'application vous proposera de le reprendre ou non. Si vous acceptez, le tournoi reprendra là où il s'est arrêté, sinon vous serez au menu pour créer un nouveau tournoi.

#### B. Création d'un nouveau tournoi
Vous verrez la liste des participants au tournoi que vous voudrez lancer. Si jamais vous voulez ajouter ou retirer des participants, sélectionnez l'option "Ajouter/retirer des participants" sinon sélectionnez Valider et lancer le tournoi. Vous pouvez lancer les matchs pour chaque round, les terminer et rentrer les vainqueurs pour chacun des matchs.

**A noter :** Ne vous en faites pas pour la sauvegarde, celle-ci est réalisée à chaque action que vous effectuez dans l'application.

#### C. Fin d'un tournoi.

Lorsque tous les rounds ont été effectués, l'application déterminera le vainqueur et affichera le classement.

### Affichez des rapports

Dans cette option "Afficher des rapports", vous aurez la possibilité d'afficher plusieurs rapports :

- Afficher la liste de tous les joueurs triés dans l'ordre alphabétique
- Afficher la liste de tous les clubs
- Afficher la liste de tous les tournois terminés.

Si vous demandez à afficher les tournois, ceux-ci afficheront les informations limitées. Si vous voulez afficher toutes les informations comme la liste des participants, la liste de chaque tour ou bien le classement final, vous serez invité à en sélectionner un.

## Configurations

Pour modifier les configurations de l'application, vous pouvez ouvrir et modifier les variables dans le module **config.py**.

Dans ce module, vous pourrez modifier les paramètres suivants :

- La taille des bordures
- La taille des espacements
- Le temps d'affichage des messages
- Le nombre de rounds d'un tournoi
- Le nombre minimum de joueurs nécessaire pour un tournoi
- Le nombre par défaut de points des joueurs
- Les répertoires d'enregistrement

A modifier selon votre désir !

## Générez un rapport flake8

L'application a été contrôlée par flake8.

Pour générer un rapport flake8 de l'application en format HTML, vous devrez vous rendre dans votre terminal à la racine du répertoire de l'application puis utiliser la fonction suivante :

```bash
    flake8 --format=html --htmldir=flake-report
```

Ce rapport sera généré dans le dossier "flake-report".
 



