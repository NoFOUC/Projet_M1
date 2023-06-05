# Planar Graph Project

Ce projet est conçu pour être utilisé avec l'IDE PyCharm et fournit un environnement préconfiguré.

## Installation

1. Assurez-vous d'avoir [Python](https://www.python.org/downloads/) installé sur votre système.
2. Clonez ce dépôt en utilisant la commande suivante :

   ```shell
   git clone https://github.com/NoFOUC/Projet_M1
   ```

3. Ouvrez le répertoire `planar_graph_projet` avec PyCharm. Si vous n'avez pas encore installé PyCharm, vous pouvez le télécharger à partir du [site officiel de PyCharm](https://www.jetbrains.com/pycharm/download/).

## Exécution du projet

Maintenant que l'environnement est configuré, vous pouvez exécuter le projet dans PyCharm.

1. Dans la barre d'outils de PyCharm, sélectionnez la configuration d'exécution appropriée dans ce projet, 'main.py'.
2. Cliquez sur le bouton "Run" (Exécuter) pour lancer l'exécution du projet.


## Paramètres de la fonction graph_generation

La fonction `graph_generation` accepte plusieurs paramètres qui contrôlent le processus de génération du graphe. Voici une explication de chaque paramètre :

- `Nbr_node` : Le nombre de nœuds dans le graphe (l'ordre de grandeur réel varie en fonction de la génération).
- `Funct_deg` : Un tableau de taille 2 contenant les valeurs `a` et `b` de l'exponentielle décroissante prédéfinie lors de l'analyse de la répartition des degrés des nœuds.
- `Pourc_2` : Le pourcentage de nœuds de degré 2 constituant le graphe (la valeur par défaut est de 65%).
- `Pourc_0` : Le pourcentage de nœuds de degré 0 constituant le graphe (la valeur par défaut est de 60%).
- `Noise` : Le bruit aléatoire ajouté à la position des nœuds pour permettre une répartition aléatoire tout en maintenant la planarité.
- `Reduce_deg_1` : Ce paramètre permet de réduire la quantité de nœuds de degré 1 dans le graphe.
- `Usa` : Si vrai, le graphe ressemble à un graphe américain avec moins de bruit et une probabilité plus élevée d'avoir des nœuds avec des arcs verticaux et horizontaux.
- `Color` : Ce paramètre permet de différencier les nœuds en fonction de leur degré.

Ces paramètres permettent de contrôler la taille, la structure et l'apparence visuelle du graphe généré.

