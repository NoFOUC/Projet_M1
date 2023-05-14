import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Générer les valeurs des paramètres
nbr_nodes = np.arange(0, 100000, 1000)
pourc_0 = np.linspace(0, 1, num=100)
pourc_2 = np.linspace(0, 1, num=100)

# Créer une grille de coordonnées
nbr_nodes, pourc_0, pourc_2 = np.meshgrid(nbr_nodes, pourc_0, pourc_2)

# Calculer le nombre de nœuds en fonction des paramètres
nombre_noeuds = np.power(np.sqrt(nbr_nodes * (1 + pourc_2) * (1 + pourc_0))+1, 2)

# Créer la figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotter les données
scatter = ax.scatter(pourc_0, pourc_2, nbr_nodes, c=nombre_noeuds, cmap='viridis')

# Configurer les axes et les étiquettes
ax.set_xlabel('pourc_0')
ax.set_ylabel('pourc_2')
ax.set_zlabel('nbr_node', labelpad=15)

# Ajouter une barre de couleur
cbar = plt.colorbar(scatter, orientation="horizontal", pad=0.1)
cbar.set_label('Nombre de nœuds total')

# Move the z-axis tick values to the right
ax.tick_params(axis='z', pad=6)

# Ajuster les marges du graphique
plt.tight_layout()

# Afficher le graphique
plt.show()
