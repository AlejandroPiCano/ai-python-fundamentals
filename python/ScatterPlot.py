import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 2, 100)

# Create diagram box
plt.scatter(x, y, alpha=0.5)

# Add labels and title
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title('Scatter Plot')

# Show the graphics
plt.show()