import matplotlib.pyplot as plt
import numpy as np
# Data
np.random.seed(0)
data = np.random.normal(0, 1, 1000)
# Create histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Data histogram')
# Show the histogram
plt.show()