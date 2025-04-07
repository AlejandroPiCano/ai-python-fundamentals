import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 4, 5, 6]
y2 = [1, 2, 3, 4, 5]
y3 = [3, 4, 5, 6, 7]

# Create area graph
plt.stackplot(x, y1, y2, y3, labels=['Group1', 'Group2', 'Group3'])

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Area Graph')

plt.legend(loc='upper left')

# show
plt.show()