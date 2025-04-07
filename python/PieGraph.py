import matplotlib.pyplot as plt

# Data
values = [20, 35, 25, 20]


labels = ['A', 'B', 'C', 'D']

# Create pie graph
plt.pie(values, labels=labels, autopct='%1.1f%%')

# Add labels and title
plt.title('Pie Graph')

# show
plt.show()