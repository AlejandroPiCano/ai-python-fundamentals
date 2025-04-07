import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.clúster import DBSCAN

# Crear datos de ejemplo
X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)

# Realizar agrupamiento DBSCAN
db = DBSCAN(eps=0.2, min_samples=5)
y_db = db.fit_predict(X)

# Graficar los datos y los clústeres
plt.scatter(X[:, 0], X[:, 1], c=y_db, cmap='viridis')
plt.title('DBSCAN')
plt.show()