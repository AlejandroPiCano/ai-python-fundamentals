import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

# Calculate correlation
correlation = np.corrcoef(x, y)[0, 1]

# Show the data and the regresion line
plt.scatter(x, y)
plt.title('Correlation = ' + str(correlation))
plt.xlabel('x')
plt.ylabel('y')
plt.show()