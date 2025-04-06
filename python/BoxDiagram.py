import matplotlib.pyplot as plt
import numpy as np

# Data
np.random.seed(0)
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(0, 2, 100)
data3 = np.random.normal(0, 3, 100)

# Create diagram box
plt.boxplot([data1, data2, data3], labels=['Data1', 'Data2', 'Data3'])

# Add labels and title
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Diagram Box')
# Show the graphics
plt.show()