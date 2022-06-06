# Segfault-Project (FR)

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

### 🔗 Social
*Ces commandes sont inspirées de celles de Koya*

- <u>Bang</u>: Vous tirez sur quelqu'un
- <u>Hi</u>: Vous saluez quelqu'un
- <u>Hug</u>: Vous câlinez quelqu'un
- <u>Kiss</u>: Vous embrassez quelqu'un
- <u>Pat</u>: Vous donnez des pats pats à quelqu'un

### 🆘 Aide

- <u>Help</u>: Affiche l'aide complète du robot
- <u>Module</u>: Affiche l'aide complète d'un module du robot
- <u>Module_list</u>: Affiche la liste des modules implémentés pour le robot

### 🗃️ Diverses

- <u>Members</u>: Affiche le nombre de membres présents sur le serveur
- <u>Me</u>: Affiche une fiche complète d'informations sur la personne lançant la commande
- <u>Pancakes</u>: Make pancakes great again !
- <u>Ping</u>: Renvoie la latence du robot
- <u>Randomchoose</u>: Choisi une solution aléatoirement parmis un ensemble d'options
- <u>Say</u>: Faites dire quelquechose au robot
- <u>Strawpoll</u>: Permet de créer un strawpoll
- <u>Userinfo</u>: Permet d'affiche une fiche complète d'informations sur un membre précis

### 📔 À propos

- <u>Github</u>: Affiche le lien de ce reposetory
- <u>Version</u>: Affiche la version du robot ainsi que le lien de ce reposetory

<hr/>

# Segfault-Project (EN)

Segfault is a Discord robot project that can do a variety of things. The initial idea comes from a set of inspirations I've seen in my many years on Discord. The main bots I'm inspired by though are Vexera (https://vexera.io/), Koya (https://koya.gg/) and UnbelieveaBoat (https://unbelievaboat.com/). Some ideas also come from my strange brain.

The ultimate goal of this bot is to be able to automate all the heavy actions a user can do. Also, the goal is to create an interconnected bot with a maximum of useful services for developers (Example: Documentation of the standard Python library).

Currently, the implemented features are moderation tools, a complete documentation of the standard Python library, connections to Tenor, Giphy and Gelbooru. Role-playing game (RPG) support tools are available alongside a music module.


## Summary documentation of the currently implemented modules

### ⚖️ Moderation

- <u>Ban</u>: Allows you to ban a member
- <u>Clear</u>: Allows you to delete a large number of posts
- <u>Create_category</u>: Allows you to create a new category
- <u>Create_channels</u>: Allows you to create a set number of channels (text and voice) in a specific category
- <u>Get_categories</u>: Allows you to have a complete list of categories with their identifiers
- <u>Kick</u>: Allows you to kick out a member
- <u>Unban</u>: Allows you to unban a member


### 📚 Python Help

- <u>Stdlib</u>: Returns the complete list of modules in the standard library
- <u>Pyfunc</u>: Returns the documentation of a function of a module in the standard library
- <u>Pymodule</u>: Returns the documentation of a module of the standard library

### 📸 Images and Gifs

- <u>Giphy</u>: Retrieves and displays a gif from Giphy.com
- <u>Nsfwbooru</u>: Retrieves and displays a random image from Gelbooru.com (Not Safe At Work tags are enabled)
- <u>Sfwbooru</u>: Retrieves and displays a random image from Gelbooru.com (Not Safe At Work tags are disabled)
- <u>Tenor</u>: Retrieves and displays a gif from Tenor Gif

### 🎭 Role Playing Game

- <u>Area</u>: Displays the RPG record of an area (saved by hand in a database, for now)
- <u>Adventure</u>: Displays the synopsis of a RPG (saved by hand in a database, for now)
- <u>Dice</u>: Rolls an n-sided die and returns the result
- <u>Sheet</u>: Displays the sheet of an NPC (saved by hand in a database, for now)

### 🎷 Music

- <u>Clearqueue</u>: Deletes music in the queue
- <u>Leave</u>: Disconnects the robot from the voice lounge
- <u>Now_playing</u>: Displays the music currently playing
- <u>Pause</u>: Pauses the currently playing music
- <u>Play</u>: Starts a music present on Youtube
- <u>Queue</u>: Displays the waiting queue
- <u>Resume</u>: Resumes playing a paused music
- <u>Skip</u>: Switches to the next music
- <u>Summon</u>: Allows the robot to join a voice lounge

### 🔗 Social
*These commands are inspired by Koya's commands*

- <u>Bang</u>: You shoot someone
- <u>Hi</u>: You wave at someone
- <u>Hug</u>: You hug someone
- <u>Kiss</u>: You kiss someone
- <u>Pat</u>: You give pats pats to someone

### 🆘 Help

- <u>Help</u>: Displays the full help of the robot
- <u>Module</u>: Displays full help for a module of the robot
- <u>Module_list</u>: Displays the list of modules implemented for the robot

### 🗃️ Miscellaneous

- <u>Members</u>: Displays the number of members present on the server
- <u>Me</u>: Displays a full record of information about the person initiating the order
- <u>Pancakes</u>: Make pancakes great again!
- <u>Ping</u>: Returns the latency of the robot
- <u>Randomchoose</u>: Chooses a solution randomly from a set of options
- <u>Say</u>: Make the robot say something
- <u>Strawpoll</u>: Allow to create a strawpoll
- <u>Userinfo</u>: Allows you to display a complete information sheet about a specific member

### 📔 About

- <u>Github</u>: Displays the link to this reposetory
- <u>Version</u>: Displays the version of the bot as well as the link to this reposetory
