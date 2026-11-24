
## TP5 - Docker et Docker Compose

### 1. Difference entre une image et un conteneur ?
L'image est un modele fige en lecture seule (systeme, Python, bibliotheques, code).
Le conteneur est une instance en cours d'execution de cette image.

### 2. Pourquoi installer requirements.txt avant de copier app.py ?
Pour profiter du cache des couches : le code change souvent, les bibliotheques rarement.
Une modification de app.py ne relance donc pas pip install.

### 3. Que se passe-t-il sans l'option -p ?
L'API tourne dans le conteneur mais le port n'est pas publie : localhost:8000 ne repond pas.

### 4. Pourquoi http://mlflow:5000 et non localhost:5000 dans Compose ?
Dans un conteneur, localhost designe le conteneur lui-meme. Compose cree un reseau
ou chaque service est joignable par son nom.

### 5. Difference entre down et down -v ?
down supprime conteneurs et reseau mais garde les volumes (donnees conservees).
down -v supprime aussi les volumes : MLflow repart vide.

### 6. Pourquoi model/ hors de Git alors que le Dockerfile y est ?
Le Dockerfile est du texte, versionnable. Le modele est un binaire regenerable,
gere par le Registry MLflow.

### 7. Pourquoi une branche dediee plutot que develop ?
Pour garder develop stable, isoler les essais et ne fusionner qu'un travail valide.
