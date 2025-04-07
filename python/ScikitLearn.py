import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Create sample data
X = np.random.randint(1, 100, size=(100, 3))

# Create a PCA object
pca = PCA(n_components=2)

# Fit and transform the data
X_pca = pca.fit_transform(X)

# Check the variance explained by each principal component
print(pca.explained_variance_ratio_)

# Plot the original data
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Datos originales')

# Plot the PCA-transformed data
plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('Primer Componente Principal')
plt.ylabel('Segundo Componente Principal')
plt.title('PCA')
plt.tight_layout()
plt.show()