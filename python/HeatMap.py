import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
data = np.random.random((10, 10))

# Create heat map
plt.imshow(data, cmap='hot', interpolation='nearest')

# Add colorbar
plt.colorbar()

# Add labels and title
plt.xlabel('Column')
plt.ylabel('Row')
plt.title('Hear map')

# Show the graphics
plt.show()