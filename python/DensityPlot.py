import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
np.random.seed(0)
data = np.random.normal(0, 1, 100)

# Create density plot
sns.kdeplot(data, color='skyblue', shade=True)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density plot')

# show
plt.show()