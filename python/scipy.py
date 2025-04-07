import numpy as np
from matplotlib import pyplot as plt
from scipy.clúster.hierarchy import dendrogram, linkage

# Crear datos de ejemplo
np.random.seed(4711)
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
X = np.concatenate((a, b),)
print(X.shape) # Check the shape

# Realizar agrupamiento jerárquico
linked = linkage(X, 'ward')

# Crear el dendrograma
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=np.arange(len(X)))
plt.title('Dendrograma de Agrupamiento Jerárquico')
plt.show()