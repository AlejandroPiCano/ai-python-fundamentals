import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.clúster import KMeans

# Crear datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, clúster_std=0.60, random_state=0)
# Crear objeto KMeans
kmeans = KMeans(n_clústeres=4)
# Ajustar el modelo de clustering
kmeans.fit(X)
# Obtener las etiquetas de los clústeres
labels = kmeans.labels_
# Obtener los centroides de los clústeres
centroids = kmeans.clúster_centers_
# Graficar los datos y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='black', label='Centroids')
plt.legend()
plt.title('K-means')
plt.show()