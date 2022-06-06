# Segfault-Project

Segfault est un projet de robot Discord permettant de faire un ensemble de choses variées. L'idée de départ viens d'un ensemble d'inspirations que j'ai vu au cours de mes nombreuses années sur Discord. Les principaux robots dont je m'inspire cela dit sont Vexera (https://vexera.io/), Koya (https://koya.gg/) et UnbelieveaBoat (https://unbelievaboat.com/). Certaines idées viennent aussi de mon cerveau étrange.

Le but ultime de ce bot est de pouvoir automatiser toutes les actions un peu lourde qu'un utilisateur peut faire. Également, le but est de créer un robot interconnecté avec un maximum de services utiles pour les développeurs.euse.s (Exemple: Documentation de la librairie standard Python).

Actuellement, les features implémentées sont des outils de modérations, une documentation complète de la librairie standard de Python, des connexions aux sites Tenor, Giphy ainsi que Gelbooru. Des outils de supports pour des Jeux de Rôles (JDR) sont disponibles aux côtés d'un module musical.

## Documentation résumée des modules actuellement implémentés

### ⚖️ Modération

- <u>Ban</u>: Permet de bannir un membre
- <u>Clear</u>: Permet de supprimer un grand nombre de messages
- <u>Create_category</u>: Permet de créer une nouvelle catégorie
- <u>Create_channels</u>: Permet de créer un nombre déterminé de salons (textuels et vocaux) dans une catégorie spécifique
- <u>Get_categories</u>: Permet d'avoir la liste complète des catégories avec leur identifiants
- <u>Kick</u>: Permet d'expulser un membre
- <u>Unban</u>: Permet de débannir un membre


### 📚 Aide Python

- <u>Stdlib</u>: Renvoie la liste complète des modules de la librairie standard
- <u>Pyfunc</u>: Renvoie la documentation d'une fonction d'un module de la librairie standard
- <u>Pymodule</u>: Renvoie la documentation d'un module de la librairie standard

### 📸 Images et Gifs

- <u>Giphy</u>: Permet de récupérer et d'afficher un gif issu de Giphy.com
- <u>Nsfwbooru</u>: Permet de récupérer et d'afficher une image aléatoire issue du site Gelbooru.com (Les tags "Not Safe At Work" sont activés)
- <u>Sfwbooru</u>: Permet de récupérer et d'afficher une image aléatoire issue du site Gelbooru.com (Les tags "Not Safe At Work" sont désactivés)
- <u>Tenor</u>: Permet de récupérer et d'afficher un gif issu de Tenor Gif

### 🎭 Jeu de Rôle

- <u>Area</u>: Affiche la fiche JDR d'une zone (enregistrée à la main dans une base de donnée, pour le moment)
- <u>Aventure</u>: Affiche le synopsis d'un JDR (enregistrée à la main dans une base de donnée, pour le moment)
- <u>Dice</u>: Lance un dé à n face et renvoie le résultat
- <u>Fiche</u>: Affiche la fiche d'une PNJ (enregistrée à la main dans une base de donnée, pour le moment)

### 🎷 Musique

- <u>Clearqueue</u>: Supprime les musiques dans la file d'attentes
- <u>Leave</u>: Permet de déconnecter le robot du salon vocal
- <u>Now_playing</u>: affiche la musique en cours de lecture
- <u>Pause</u>: Met en pause la musique actuellement jouée
- <u>Play</u>: Lance une musique présente sur Youtube
- <u>Queue</u>: Affiche la file d'attent
- <u>Resume</u>: Reprend la lecture d'une musique mise en pause
- <u>Skip</u>: Passe à la musique suivante
- <u>Summon</u>: Permet au robot de rejoindre un salon vocal

