import matplotlib.pyplot as plt
import numpy as np


variables = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5']

values_1 = [1, 2, 3, 4, 5]
values_2 = [5, 4, 3, 2, 1]

# Calculate the angle for each variable
angles = np.linspace(0, 2 * np.pi, len(variables), endpoint=False).tolist()

# Add the first value to the end to close the graph
values_1 += values_1[:1]
values_2 += values_2[:1]
angles += angles[:1]

# Create a figure and a spider graph
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values_1, 'b', alpha=0.1)
ax.fill(angles, values_2, 'r', alpha=0.1)

# Define the legend and the labels
ax.set_title('Gráfico de Arana', va='bottom', fontsize=20)
ax.set_yticklabels([])
plt.xticks(angles[:-1], variables, size=10)

# Add a label and a unit label to y axis
ax.set_rlabel_position(-22.5)
plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="black", size=10)
plt.ylim(0, 5)

# show
plt.show()