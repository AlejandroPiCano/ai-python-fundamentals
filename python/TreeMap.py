import matplotlib.pyplot as plt
import squarify
import pandas as pd

# Data
categories = ['A', 'B', 'C', 'D']
values = [20, 30, 25, 35]


# Create dataframe
df = pd.DataFrame({'Category':categories, 'Value':values})


# Order dataframe
df = df.sort_values(by='Value', ascending=False)

# Create tree map
plt.figure(figsize=(10, 6))
squarify.plot(sizes=df['Value'], label=df['Category'], alpha=0.8, color=['red', 'blue', 'green', 'orange'])

# Add labels and title
plt.axis('off')
plt.title('Treemap')

# Show the graphics
plt.show()